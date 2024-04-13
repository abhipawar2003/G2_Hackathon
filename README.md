# G2_Hackathon


Problem Statement 3</br>
G2 regularly updates its website with new products by creating new categories and refining existing ones. One crucial aspect of this process is ensuring that each product has a precise description and URL before it is added to the site. We are interested in automating the process of updating product descriptions in our database. We will provide you with a few product URLs, and your output will be a brief 3-4 lines description of each product.
</br>

Proposed Solution:</br>
The proposed solution involves developing a robust system that can automate the process of updating product descriptions on the G2 website. This system will leverage web scraping techniques to extract relevant information from product pages and text summarization algorithms to generate brief descriptions. Additionally, data cleaning and normalization techniques will be employed to ensure the accuracy and consistency of the extracted data. The system will adhere to legal and ethical guidelines regarding web scraping and data privacy, and measures will be implemented to optimize scalability and performance.

To run the file we need few libraries to be installed.
</br></br>
before this creare an virtual python environment. the python environment helps to run the files smoother and easier way.</br>
pip install vitualenv</br>
virtenv myenv</br>


</br>
pip install -r requirements.txt

the detailed explaination of the code
import necessary libraries. requests is used to fetch HTML content from URLs, BeautifulSoup is used for parsing HTML, and csv is used for writing data to CSV files.</br>
A function scrape_product_descriptions that takes a list of URLs as input and initializes an empty dictionary descriptions to store the scraped product descriptions.</br>
loop iterates over each URL in the list urls. It tries to fetch the HTML content of each URL using the requests.get method, specifying a user agent in the headers to mimic a web browser. Then, it parses the HTML content using BeautifulSoup and stores it in the soup variable.</br>
Later, attempts to find the product description using the Open Graph meta tag (og:description). If found, it extracts the content of the tag and stores it in the descriptions dictionary.</br>
If the meta tag is not found, it tries to extract the description from other HTML elements, such as tags. If a description is found, it is stored in the descriptions dictionary. If not, a default message is stored indicating that the description was not found.</br>
catches any exceptions that occur during the scraping process, prints an error message indicating which URL caused the error, and stores an error message in the descriptions dictionary for that URL.</br>
Finally, the function returns the dictionary containing the scraped product descriptions.</br>
Finally the scraped details will be stored in the csv file. A csv file will be generated and stored.

<img width="980" alt="Screenshot 2024-04-12 at 2 19 35 PM" src="https://github.com/abhipawar2003/G2_Hackathon/assets/112234264/5aa080f4-3b38-4195-9009-9d597a218cee">

