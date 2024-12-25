# Automata-Based Web Scraping and Content Filtering Tool

This project leverages automata theory and regular expressions to create a versatile web scraping tool for extracting and filtering data from websites. The tool effectively targets specific content, such as news articles and Wikipedia pages, while filtering irrelevant sections like ads or metadata.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributors](#contributors)

---

## Introduction

Web scraping is a valuable technique for extracting meaningful data from websites. However, challenges such as handling noisy or irrelevant content, including advertisements or metadata, often arise. This project tackles these challenges using automata theory and regular expressions. Applications include news aggregation, content analysis, and educational research.

---

## Features

- **CNN Scraper**:
  - Extracts unique news links from the CNN homepage.
  - Retrieves headlines and relevant content for each news article.
  - Filters out noisy metadata and ads.
  - Saves data in a structured CSV format.
- **Wikipedia Scraper**:
  - Fetches and processes structured content from Wikipedia pages.
  - Extracts main titles, infobox tables, introductions, and sections.
  - Filters out unwanted headings such as "References" and "See also."
  - Saves extracted data in a CSV file named after the search term.
- **Content Filtering**:
  - Removes irrelevant sections and ensures clean data output.
- **Output Format**:
  - Results are stored in CSV files for further analysis.

---

## Requirements

The project requires the following Python libraries:

- `beautifulsoup4`
- `requests`
- `lxml`
- Built-in modules: `os`, `sys`, `re`, and `csv`.

Refer to the `requirements.txt` file for third-party package versions.

---

## Setup Instructions

1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Install Required Libraries**: Use the following command to install the necessary libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Project**: Ensure all files (`main_scraper.py`, `cnn_scraper.py`, and `wikipedia_scraper.py`) are in the same directory.

---

## Usage

1. **Run the Main Scraper Tool**:
   Execute the main script to start the tool:
   ```bash
   python main_scraper.py
   ```
2. **Choose an Option**:
   - Select **Option 1** to scrape news from CNN.
   - Select **Option 2** to search and scrape content from Wikipedia.
3. **Follow Prompts**:
   - For Wikipedia scraping, provide the name of the page you wish to search.

---

## Future Work

- **Integration of Frontend**: Develop a user-friendly web-based interface to allow users to input website URLs or search terms and view the extracted data in real-time.
- **Dynamic Content Handling**: Add support for scraping JavaScript-rendered pages using tools like Selenium or Puppeteer.
- **Expansion to More Websites**: Extend the scraping logic to include e-commerce platforms, academic repositories, and government portals.
- **Enhanced Filtering Logic**: Improve handling of complex and nested HTML structures.
- **Advanced Analytics**: Incorporate additional features such as sentiment analysis, market trend forecasting, or content summarization.

---

## Contributors

- **Ghulam Hussain Khan Sherwani**  
  National University of Sciences and Technology, Islamabad, Pakistan  
  [sherwani.bscs21seecs@seecs.edu.pk](mailto:sherwani.bscs21seecs@seecs.edu.pk)

- **Zartab Khalid Khan**  
  National University of Sciences and Technology, Islamabad, Pakistan  
  [zkhan.bscs20seecs@seecs.edu.pk](mailto:zkhan.bscs20seecs@seecs.edu.pk)

- **Abdullah Shamshad Cheema**  
  National University of Sciences and Technology, Islamabad, Pakistan  
  [acheema.bscs21seecs@seecs.edu.pk](mailto:acheema.bscs21seecs@seecs.edu.pk)
