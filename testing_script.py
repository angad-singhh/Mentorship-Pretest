import os
from edgar import Company
import requests

ticker = "AAPL"  # Replace with the company's ticker symbol
output_dir = "./press_releases"
os.makedirs(output_dir, exist_ok=True)

def fetch_latest_press_release(ticker):
    company = Company(ticker)
    filings = company.get_filings(form="8-K")
    latest_filing = filings.latest(1)
    
    if latest_filing:
        document_url = latest_filing.document.url
        return document_url
    else:
        raise Exception("No press release filings found for the given ticker.")

def save_webpage(url, output_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"Press release saved as: {output_path}")
    else:
        raise Exception(f"Failed to retrieve the press release. Status code: {response.status_code}")

def main():
    try:
        press_release_url = fetch_latest_press_release(ticker)
        output_file_path = os.path.join(output_dir, f"{ticker}_latest_press_release.html")
        save_webpage(press_release_url, output_file_path)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
