import requests
import bs4
import openpyxl
from datetime import datetime

def get_soup(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        return bs4.BeautifulSoup(response.text, "lxml")
    except:
        return None

def extract_price(soup, css_id):
    element = soup.select_one(f"#{css_id} > span:nth-child(2) > span:nth-child(1)")
    return element.text.strip() if element else "Not Found"

def main():
    soup = get_soup("https://www.tgju.org/")
    if not soup:
        print("Could not fetch data.")
        return

    targets = {
        "Coin": "l-sekee",
        "Gold 18k": "l-geram18",
        "Dollar": "l-price_dollar_rl",
        "Bitcoin": "l-crypto-bitcoin"
    }

    prices = {name: extract_price(soup, css_id) for name, css_id in targets.items()}

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Item", "Price", "Date"]) 
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    for name, price in prices.items():
        ws.append([name, price, now])

    wb.save("Web_Scraper.xlsx")
    print("Data saved successfully!")

if __name__ == "__main__":
    main()
