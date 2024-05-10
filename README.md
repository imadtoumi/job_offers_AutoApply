# Automated Job Application System

## Overview

This project aims to automate the process of job searching and application by scraping job listings from a website and applying for them automatically (This may not be usefull to you since the website is a moroccan web).

## Usage

To use this automated system, follow these steps:

1. **Set up Environment:**
   - Ensure you have Python installed on your system.
   - Install necessary Python libraries.
   - Download the appropriate version of ChromeDriver and place it in the project directory.

2. **Prepare Configuration Files:**
   - Create a CSV file named `info.csv` containing login credentials and applicant information.
   - Populate `info.csv` with the following columns: `login_name`, `login_pass`, `name`, `phone`, `city`.

3. **Run Scripts:**
   - Execute the `main.py` script to start the automation process.
     ```
     python main.py
     ```

## Files

- **autoapply.py:** Automates the job application process. Reads login details and applicant information from `info.csv`, applies for job listings obtained from `links.txt`, and updates the file after applying.
- **linkscrap.py:** Automates the job listing scraping process. Scrapes job listings from a specified website based on keyword, domain, and city, compares retrieved links to existing ones in `links.txt`, and appends new links to the file.
- **main.py:** Entry point for executing `linkscrap.py` and `autoapply.py` sequentially.

## Requirements

- Python 3.x
- ChromeDriver
- Selenium
- BeautifulSoup

## Note

- Ensure proper internet connectivity and website accessibility for successful scraping and application processes.
- Review and customize the XPath and element locators if changes has been made in the website code and the python code doesn't work as expected.
