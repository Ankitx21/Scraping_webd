import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Open the website
# driver = webdriver.Chrome()
# driver.get("https://dev.to/t/webdev")

# driver.maximize_window()

# time.sleep(2)

# article_title = driver.find_element(By.ID, 'article-link-1884166')
# print(article_title.text)

##############################################################################
#############################################################################

# # Find all h2 elements with the specified class name
# article_titles = driver.find_elements(By.CLASS_NAME, 'crayons-story__title')

# # Iterate through the first two articles to get their titles
# for i in range(100):  # Assuming you want to scrape the titles of the first two articles
#     # Find the anchor tag within the h2 element
#     anchor_tag = article_titles[i].find_element(By.TAG_NAME, 'a')
    
#     # Print the href attribute of the anchor tag
#     print(anchor_tag.get_attribute('href'))

################################################################################################
############################################################################################

# # Function to scroll down the page
# def scroll_down(driver):
#     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
#     time.sleep(3)  # Wait for new articles to load

# # List to hold the article links
# article_links = []

# # Keep scrolling and collecting article links until we have enough
# while len(article_links) < 500:
#     # Scroll down to load more articles
#     scroll_down(driver)
    
#     # Find all h2 elements with the specified class name
#     article_titles = driver.find_elements(By.CLASS_NAME, 'crayons-story__title')
    
#     # Iterate through the articles to get their links
#     for title in article_titles:
#         anchor_tag = title.find_element(By.TAG_NAME, 'a')
#         link = anchor_tag.get_attribute('href')
#         if link not in article_links:  # Avoid duplicates
#             article_links.append(link)
    
#     # Print the progress
#     print(f'Collected {len(article_links)} articles...')

# # Print the links of the first 500 articles
# for link in article_links[:500]:
#     print(link)

##################################################################################################
############################################################################################


def collect_article_links(url, num_articles=1):
    # Set up the WebDriver (this example uses Chrome)
    driver = webdriver.Chrome()
    
    # Navigate to the page containing the articles
    driver.get(url)

    driver.maximize_window()

    time.sleep(2)
    
    # Function to scroll down the page
    def scroll_down(driver):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)  # Wait for new articles to load
    
    # List to hold the article links
    article_links = []
    
    # Keep scrolling and collecting article links until we have enough
    while len(article_links) < num_articles:
        # Scroll down to load more articl
        scroll_down(driver)
        
        # Find all h2 elements with the specified class name
        article_titles = driver.find_elements(By.CLASS_NAME, 'crayons-story__title')
        
        # Iterate through the articles to get their links
        for title in article_titles:
            anchor_tag = title.find_element(By.TAG_NAME, 'a')
            link = anchor_tag.get_attribute('href')
            if link not in article_links:  # Avoid duplicates
                article_links.append(link)
        
        # Print the progress
        print(f'Collected {len(article_links)} articles...')
    
    # Clean up and close the browser
    driver.quit()
    
    # Return the list of article links
    return article_links

# Example usage
url = 'https://dev.to/t/webdev'
article_links = collect_article_links(url, num_articles=1)
print(article_links)


# # Clean up and close the browser
# driver.quit()


