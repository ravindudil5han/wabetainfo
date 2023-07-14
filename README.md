<p align="center">
  <a href="" rel="1337.x">
 <img width=150px height=150px src="https://raw.githubusercontent.com/ravindudil5han/1337x/main/lib/icon.jpeg" alt="1337.x"></a>
</p>

<br><br>


# WABETAINFO

This Python script utilizes web scraping techniques to gather the latest technology news from the website WABetaInfo (https://wabetainfo.com/). The script extracts information such as article ID, publication time, operating system, title, link, and summary of each news article from the website's front page.

## Prerequisites

To run this script, you need to have the following dependencies installed:
- Python 3.x
- Requests library
- Beautiful Soup library (bs4)

You can install the required libraries using the following commands:
```
pip install requests
pip install beautifulsoup4
```

## Usage

The script consists of two main functions:

### 1. `frontpage()`

This function retrieves the latest news articles from the front page of WABetaInfo. It returns the information as a JSON string, containing the article ID, publication time, operating system, title, link, and summary of each article.

Example usage:
```python
articles = frontpage()
print(articles)
```

### 2. `news_content(link)`

This function takes a link to a specific news article on WABetaInfo and retrieves the content of the article. It returns the article content as a string.

Example usage:
```python
link = 'https://wabetainfo.com/sample-article'
content = news_content(link)
print(content)
```

## User-Agent Header

To ensure successful scraping, the script sets the User-Agent header in the HTTP requests to mimic a web browser. This helps to avoid any potential blocking or restrictions imposed by the website.

## Error Handling

The script checks for valid HTTP responses (status code 200) before proceeding with scraping. If an error occurs, an error message with the corresponding status code is displayed.

Please note that web scraping should be conducted responsibly and in compliance with the website's terms of service. Make sure to respect the website's robots.txt file and avoid overwhelming the server with excessive requests.

Feel free to modify and enhance the script according to your needs. Happy scraping!
