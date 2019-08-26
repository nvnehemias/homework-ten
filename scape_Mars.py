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

    browser.visit(url_1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')