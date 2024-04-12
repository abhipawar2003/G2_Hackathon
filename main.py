import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape product descriptions from URLs
def scrape_product_descriptions(urls):
    descriptions = {}

    for url in urls:
        try:
            # Fetch HTML content
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Attempt to extract description using meta tag
            description = soup.find('meta', property='og:description')
            if description:
                descriptions[url] = description['content'].strip()
            else:
                # If meta tag not found, try extracting from other elements
                description = soup.find('p')  # You can adjust this to search for other elements
                if description:
                    descriptions[url] = description.get_text().strip()
                else:
                    descriptions[url] = "Description not found."

        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            descriptions[url] = "Error occurred during scraping."

    return descriptions

def main():
    # URLs to scrape
    urls = [
        "https://www.telesign.com/products/trust-engine",
        "https://www.litzia.com/professional-it-services/",
        "https://www.chattechnologies.com/",
        "https://inita.com/",
        "https://aim-agency.com/"
    ]

    # Scrape product descriptions
    product_descriptions = scrape_product_descriptions(urls)

    # Write output to CSV file
    with open('product_descriptions.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for url, description in product_descriptions.items():
            writer.writerow({'url': url, 'description': description})

    print("CSV file has been generated successfully.")

if __name__ == "__main__":
    main()
