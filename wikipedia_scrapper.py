from bs4 import BeautifulSoup
import requests
import csv
import re
import sys

# Check if the user provided a search term as an argument
if len(sys.argv) < 2:
    print("Error: No search term provided. Please provide a Wikipedia page title.")
    sys.exit(1)

# Get the search term from the command-line argument
search_term = sys.argv[1]
url = f"https://en.wikipedia.org/wiki/{search_term.replace(' ', '_')}"

# Fetch the HTML content from the URL
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch the Wikipedia page for '{search_term}'. Please check the page title.")
    sys.exit(1)

html_content = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Function to clean text to avoid CSV issues
def clean_text(text):
    if text:
        # Remove characters other than alphabets, numbers, currencies
        return re.sub(r'[^a-zA-Z0-9\s$€£¥₹]', '', text).strip()
    return ''

# Extract the <h1> heading (main title of the page) and include it as "Full Name"
title = clean_text(soup.find('h1', class_='firstHeading').get_text(strip=True))

# Find the infobox table with a class containing "infobox"
infobox_table = soup.find('table', class_=lambda c: c and 'infobox' in c)

# Extract the infobox table content and prepare it for CSV
table_data = []
if infobox_table:
    rows = infobox_table.find_all('tr')
    for row in rows:
        heading = row.find('th')
        value = row.find('td')
        if heading and value:
            table_data.append([clean_text(heading.get_text(strip=True)), clean_text(value.get_text(strip=True))])

# Extract introductory <p> tags following the infobox
intro_paragraphs = []
intro_start = infobox_table.find_next_sibling() if infobox_table else soup.find('p')
while intro_start and intro_start.name == 'p':
    intro_paragraphs.append(clean_text(intro_start.get_text(strip=True)))
    intro_start = intro_start.find_next_sibling()
intro_text = " ".join(intro_paragraphs)

# Combine infobox and intro into a single introduction
introduction = clean_text(f"{intro_text}")

# List of headings to ignore
ignored_headings = {"See also", "Notes", "References", "Bibliography", "Further reading", "External links"}

# Extract <h2> headings inside <div class="mw-heading mw-heading2">
content = []
h2_divs = soup.find_all('div', class_='mw-heading mw-heading2')

for h2_div in h2_divs:
    h2_heading = h2_div.find('h2')
    if h2_heading:
        heading_text = clean_text(h2_heading.get_text(strip=True))
        # Skip ignored headings
        if heading_text in ignored_headings:
            continue
        # Collect <p> tags and smaller headings until the next <h2>
        section_content = []
        sibling = h2_div.find_next_sibling()
        while sibling:
            if sibling.name == 'p':
                section_content.append(clean_text(sibling.get_text(strip=True)))
            elif sibling.name == 'h2' and sibling.find_parent('div', class_='mw-heading mw-heading2'):
                break
            sibling = sibling.find_next_sibling()
        content.append([heading_text, " ".join(section_content)])

# Write to CSV
with open(f'{search_term}_wikipedia_extracted_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header
    writer.writerow(['Title', 'Introduction', 'Heading', 'Content'] + ['Table Heading', 'Table Content'])
    # Add the "Full Name" row with the <h1> title
    writer.writerow(['Full Name', title, '', ''] + [''] * 2)
    # Write the introduction row
    writer.writerow(['', introduction, '', ''] + [''] * 2)
    # Write all extracted <h2> headings and their content
    for row in content:
        writer.writerow(['', '', row[0], row[1]] + [''] * 2)
    # Add the table content
    writer.writerow(['', '', '', ''] + ['Table'] * 2)  # Add a separator for clarity
    for row in table_data:
        writer.writerow(['', '', '', ''] + row)

print(f"Data extraction completed. Check '{search_term}_wikipedia_extracted_data.csv'.")                                         