import requests
import csv
import re

# Function to extract content manually between start and end tags
def extract_content(html, start_tag, end_tag):
    start_idx = html.find(start_tag)
    if start_idx == -1:
        return None, html  # Tag not found
    start_idx += len(start_tag)
    end_idx = html.find(end_tag, start_idx)
    if end_idx == -1:
        return None, html  # End tag not found
    return html[start_idx:end_idx].strip(), html[end_idx + len(end_tag):]

# Function to remove unwanted patterns from text
def remove_unwanted_text(text):
    unwanted_patterns = [
        "CNN Sans ™ & © 2016 Cable News Network.",
        ",",  # Remove commas
        "Show&nbsp;all",
        "'.concat(e,\"",
        "'.concat(i,\"",
        "'.concat(a,\"",
        "This page will automatically redirect in 5 seconds...",
        "\n      ",
        "\n                    "
    ]
    for pattern in unwanted_patterns:
        text = text.replace(pattern, "")
    return text.strip()

# Function to process a single news link
def process_news_link(link):
    try:
        response = requests.get(link)
        if response.status_code != 200:
            print(f"Failed to fetch the link: {link}")
            return None
        html_content = response.text

        # Extract headline (h1 tag)
        headline, html_content = extract_content(html_content, '<h1', '</h1>')
        if headline:
            headline = headline.split('>')[-1]  # Get the text after the last ">"
            headline = re.sub(r'\s+', ' ', headline)
            headline.strip()
        # Extract content (only paragraphs)
        content = ""
        while True:
            # Look for paragraphs
            paragraph, html_content = extract_content(html_content, '<p class="paragraph inline-placeholder', '</p>')
            if paragraph:
                paragraph = paragraph.split('>')[-1]  # Get the text after ">"
                paragraph = remove_unwanted_text(paragraph)  # Remove unwanted patterns
                if paragraph:  # Skip empty paragraphs
                    content += paragraph + "\n"  # Add paragraph with a line break
            
            # Stop if no more paragraphs
            if not paragraph:
                break

        return [headline, content.strip(), link]
    except Exception as e:
        print(f"Error processing link {link}: {e}")
        return None

# Step 1: Extract links from the CNN homepage
url = "https://edition.cnn.com"

# Fetch the HTML content from the homepage
response = requests.get(url)
if response.status_code != 200:
    print("Failed to fetch the webpage. Please check the URL.")
    exit()

html_content = response.text

# Function to extract links manually from HTML
def extract_links(html):
    links = set()  # Use a set to store unique links
    start = 0
    while True:
        # Find the next anchor tag
        start_idx = html.find('<a href="', start)
        if start_idx == -1:
            break  # No more links
        start_idx += len('<a href="')
        end_idx = html.find('"', start_idx)
        if end_idx == -1:
            break
        # Extract the link
        link = html[start_idx:end_idx]
        # Validate the link format
        if "/index.html" in link:
            # Ensure absolute URLs
            if link.startswith("/"):
                link = "https://edition.cnn.com" + link
            links.add(link)  # Add to the set
        start = end_idx
    return list(links)  # Convert back to a list

# Extract all unique news links
news_links = extract_links(html_content)
if not news_links:
    print("No news links found.")
    exit()

print(f"Total Unique Links Extracted: {len(news_links)}")
print("Processing all unique links...")

# Step 2: Process each unique news link and save to CSV
news_data = []
for link in news_links:
    print(f"Processing link: {link}")
    news_entry = process_news_link(link)
    if news_entry:
        news_data.append(news_entry)

# Save the processed data to a CSV file
with open("cnn_news_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(["Headline", "Content", "Link"])
    # Write all news data
    writer.writerows(news_data)

print("Data extraction completed.")
print("Check 'cnn_news_data.csv'.")
