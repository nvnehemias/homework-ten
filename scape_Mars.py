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

    #Attain the div class and create a new empty list
    results_2 = soup.find_all('div',class_ = "article_teaser_body")
    new_list_title = []

    #Run for loop that outputs the news paragraph
    for answer in results_2:
        new_list_title.append(answer.text)
    news_p = new_list_title[0]

    mars_scrape_info["news_title"] = news_title
    mars_scrape_info["news_paragraph"] = news_p

    return mars_scrape_info


# Featured Image
def featured_image_scrape():

    # URL of page to be scraped
    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    #Visit website
    browser.visit(url_2)

    #Parse html with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #
    new_result = soup.find_all('article')
    split_url = new_result[0].attrs['style'][23:-3]
    featured_image_url = f"https://www.jpl.nasa.gov{split_url}"
    
    
    mars_scrape_info["featured_image_url"] = featured_image_url
    return mars_scrape_info



# Mars Weather
def scrape_mars_weather():

    # URL of page to be scraped
    url_3 = "https://twitter.com/marswxreport?lang=en"

    #Visit website
    browser.visit(url_3)

    #Parse html with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #
    results_3 = soup.find_all('p', class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_weather = print(results_3[0].text[0:-26])
     
     
    mars_scrape_info["mars_weather"] = mars_weather
    return mars_scrape_info

# Mars Facts
def scrape_mars_facts():

    # URL of page to be scraped
    url_4 = "https://space-facts.com/mars/"

    #Visit website
    browser.visit(url_4)

    #read html to pandas dataframe
    df = pd.read_html(url_4)

    #Rename columns
    df1.columns = ["description","Value"]

    #Setting index
    df1.set_index("description", inplace = True)

    #Convert dataframe to html
    data = df1.to_html()

    mars_scrape_info["mars_facts"] = data
    return mars_scrape_info

# Mars Hemispheres
def scrape_mars_hemispheres():

    # URL of page to be scraped
    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    #Visit website
    browser.visit(url_5)

    #Parse html with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #
    new_images = soup.find_all("img",class_ = "thumb")

    #
    hemisphere_image_urls = []
    list_names = ["Cerberus Hemisphere","Schiaparelli Hemisphere","Syrtis Major Hemisphere","Valles Marineris Hemisphere"]

    #
    for i in range(len(new_images)):
        src_url = new_images[i].attrs["src"]
        dictionary = {"title": list_names[i],"image url": f"https://astrogeology.usgs.gov{src_url}"}
        hemisphere_image_urls.append(dictionary)


    mars_scrape_info["hemisphere_image_urls"] = hemisphere_image_urls
    return mars_scrape_info