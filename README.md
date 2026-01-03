# 📈 TGJU Price Scraper (Python) A powerful and simple Python script to fetch real-time financial data (Gold, Coins, Currency, and Crypto) from the **TGJU** website and export it into a clean Excel file. > **Note:** This project specifically uses [TGJU (شبکه اطلاع‌رسانی طلا، سکه و ارز)](https://www.tgju.org/) as the primary data source for all price extractions. ## 🚀 Features - **Real-time Data:** Fetches the latest prices for Gold 18k, Dollar, Coins, and Bitcoin. - **Automated Export:** Automatically saves and organizes data into an .xlsx (Excel) file. - **Smart Parsing:** Uses BeautifulSoup and CSS selectors for precise data extraction. - **Timestamping:** Every record is saved with a precise date and time of execution. ## 🛠 Prerequisites This script requires a few external libraries. You can install them using pip:
bash
pip install requests beautifulsoup4 lxml openpyxl
Libraries used:

requests: To send HTTP requests and fetch the website's HTML.

bs4 (BeautifulSoup): For parsing HTML and extracting data.

openpyxl: To create and manage Excel spreadsheets.

datetime: To record the exact time of price fetching.

⚙️ How to Setup
To run this scraper on your system:

Clone the repository:

Bash

git clone [https://github.com/MrMani-kt/TGJUPriceScraper.git](https://github.com/MrMani-kt/TGJUPriceScraper.git)
Install dependencies: Run pip install requests beautifulsoup4 lxml openpyxl

Run the script:

Bash

python Web_Scraper.py
Check the output: An Excel file named Web_Scraper.xlsx will be created in your project folder.

🔍 How it Works
Connection: The script sends a request to https://www.tgju.org/ using a custom User-Agent to bypass basic bot blocks.

Extraction: It targets specific CSS IDs (like l-sekee or l-geram18) from the TGJU homepage to find the price values.

Organization: It stores the scraped prices in a Python dictionary.

Storage: It creates a new Excel workbook, adds a header row, and appends the prices along with the current timestamp.

⚠️ Important Notes
Source Dependence: Since the script fetches data directly from tgju.org, it requires an active internet connection.

Excel File: If the Web_Scraper.xlsx file is open in another program, the script might throw an error when trying to save. Make sure to close the Excel file before running.

Selectors: If the website's UI changes, the CSS selectors in the code might need an update.

🤝 Contributing
Feel free to fork this project and submit a Pull Request if you'd like to add more assets to track, or implement a database storage feature!
