## Description
Every year, K-Pop agency, SM Entertainment also known as SMTOWN released many albums that their artist sang. This is the project to scrape the title, artist, and release date of every album that SMTOWN had released from its official website using python.

## Specification
Below are the libraries that we used for this project:
1. BeautifulSoup
This library is used for scraping. BeautifulSoup is one of the easiest offered by python for data scraping. It is easy to learn and user-friendly for beginner.
2. requests dan get
Used for requesting the URL Page and get the response from the page. Later used for parse the HTML Page.
3. time
Only used for give interval by using time.sleep(x), x = interval in seconds for scraping every page to prevent spamming the website.
4. json
This library will be used to dump or export data we obtained into JSON file.

This project is all done using Jupyter Notebook from Anaconda. The file extension will be .ipynb instead of the normal .py

## How to use
1. Clone this repository https://github.com/cindyoji/Seleksi-2020-Tugas-1.git
2. Using jupyter notebook, open file smtown.ipynb
3. Run the code from kernel tab

## JSON Structure
Here is an example of the data stored in the JSON file
{
  "30": {
        "Title": "EXO The 6th Album \u2018OBSESSION\u2019",
        "Artist": "EXO",
        "Date": "2019.11.27"
    },
}

## Screenshot
1. Obtaining Data Progress
![ObtainingDataProgress](/screenshot/ObtainingDataProgress.png)
2. Array content post-scraping
![Title](/screenshot/title_containers.png)
![Name](/screenshot/name_containers.png)
![Date](/screenshot/date_containers.png)

## Reference
1. Target website for scraping: https://www.smtown.com/album
2. Tutorial for data scraping:
   https://stackoverflow.com/questions/41063019/python-web-scraping-page-loop
   https://www.dataquest.io/blog/web-scraping-beautifulsoup/
3. Tutorial for dump data to JSON:
   https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
   https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

## Author
Cindy Olivia Gunawan
18218017
Information System and Technology