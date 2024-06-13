# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Load the list of links from article_title.py
# from article_title import article_links

# # Open the website
# driver = webdriver.Chrome()
# driver.get("https://dev.to/alvaromontoro/10-cool-codepen-demos-may-2024-1cpb")

# driver.maximize_window()

# time.sleep(1)

# cross = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[6]/div/div/div[1]/button'))
# )

# cross.click()

# time.sleep(1)


# title = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, 'fs-3xl'))
# )
# print(title.text)

# author_name = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, 'items-start'))
# )
# print(author_name.text)
# time.sleep(5)


# # Clean up and close the browser
# driver.quit()

####################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Load the list of links from article_title.py
# from article_title import article_links

# # Set up the WebDriver (this example uses Chrome)
# driver = webdriver.Chrome()
# driver.maximize_window()

# # Function to scrape the title and author from the page
# def scrape_title_and_author(driver):
#     try:
#         # Click on the cross button if present
#         try:
#             cross = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[6]/div/div/div[1]/button'))
#             )
#             cross.click()
#         except:
#             pass  # If the cross button is not found, continue

#         # Wait for the title element and extract the text
#         title = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, 'fs-3xl'))
#         )
#         title_text = title.text.strip()
        
#         # Wait for the author element and extract the text
#         author_name = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, 'items-start'))
#         )
#         author_name_text = author_name.text.strip()

#         return title_text, author_name_text
#     except Exception as e:
#         print(f"Error occurred: {e}")
#         return None, None

# # Iterate through each link in the list of article links
# for link in article_links:
#     # Open a new tab with the link
#     driver.execute_script("window.open('');")
#     driver.switch_to.window(driver.window_handles[-1])
#     driver.get(link)

#     # Add a sleep to wait for 2 seconds
#     time.sleep(2)
    
#     # Scrape the title and author name
#     title, author_name = scrape_title_and_author(driver)
    
#     # Print the title and author name
#     if title and author_name:
#         print(f"Title: {title}\nAuthor: {author_name}\n")
#     else:
#         print(f"Title or author not found for: {link}\n")
    
#     # Close the current tab
#     driver.close()
    
#     # Switch back to the original tab
#     driver.switch_to.window(driver.window_handles[0])

# # Clean up and close the browser
# driver.quit()

#############################################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Load the list of links from article_title.py
from article_title import article_links

# Set up the WebDriver (this example uses Chrome)
driver = webdriver.Chrome()
driver.maximize_window()

# Function to scrape the title and author from the page
def scrape_title_and_author(driver):
    try:
        # Click on the cross button if present
        try:
            cross = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[6]/div/div/div[1]/button'))
            )
            cross.click()
        except:
            pass  # If the cross button is not found, continue

        # Wait for the title element and extract the text
        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'fs-3xl'))
        )
        title_text = title.text.strip()
        
        # Wait for the author and published date element and extract the text
        author_and_published = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'items-start'))
        )
        author_and_published_text = author_and_published.text.strip()

        # Split the text to separate author name and published date
        author_name, published_date = author_and_published_text.split('\n')

        return title_text, author_name.strip(), published_date.strip()
    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None, None

# List to hold article details
articles = []

# Iterate through each link in the list of article links
for link in article_links:
    # Open a new tab with the link
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(link)
    
    # Add a sleep to wait for 2 seconds
    time.sleep(2)

    # Scrape the title, author name, and published date
    title, author_name, published_date = scrape_title_and_author(driver)
    
    # Add the details to the articles list if found
    if title and author_name and published_date:
        articles.append({
            "title": title,
            "author": author_name,
            "published_date": published_date,
            "url": link
        })
    else:
        print(f"Details not found for: {link}\n")
    
    # Close the current tab
    driver.close()
    
    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])

# Clean up and close the browser
driver.quit()

# Save the articles to a JSON file
with open('articles.json', 'w') as json_file:
    json.dump(articles, json_file, indent=4)

print("Articles have been saved to articles.json")








