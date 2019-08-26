# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re


def browser_start():
    #https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    #!which chromedriver
    executable_path = {'executable_path': '/Users/nehemias/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

mars_scrape_info = {}


# NASA Mars News
def scrape_news():
    # URL of page to be scraped
    url_1 = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    #Visit website
    browser.visit(url_1)

    #Parse html with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Attain the div class and create a new empty list
    results = soup.find_all('div',class_ = "content_title")
    list_title = []

    #Run for loop that outputs the news title 
    for answer in results:
        list_title.append(answer.text)
    news_title = list_title[0]
    news_title

    #Attain the div class and create a new empty list
    results_2 = soup.find_all('div',class_ = "article_teaser_body")
    new_list_title = []

    #Run for loop that outputs the news paragraph
    for answer in results_2:
        new_list_title.append(answer.text)
    news_p = new_list_title[0]
    news_p

def featured_image_scrape():
