# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the Mars NASA new website
url = 'https://redplanetscience.com/'

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Set-up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# Assign the title and summary text to variables
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# Import entire table with Mars Facts
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# Return the dataframe back to html
df.to_html()

# Quit the automated browser
browser.quit()

# # Deliverable 1
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# Create a for loop to click into the link for each hemisphere and gather the title/image URL
for i in range(0,4):

    # Create an empty dictionary inside the for loop
    hemispheres = {}
        
    # Find and click on the title to get to the image page
    full_image_elems = browser.find_by_tag('h3')
    full_image_elems[i].click()
    
    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    # Find the relative image url
    img_url_rel = img_soup.find('img', class_='wide-image').get('src')
    
    # Make the full image URL
    img_url = f'https://marshemispheres.com/{img_url_rel}'
    
    # Get the image title
    title = img_soup.find('h2', class_='title').get_text()
    
    # Add results to dictionary
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
        
    hemisphere_image_urls.append(hemispheres)
        
    browser.back()
    
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()

