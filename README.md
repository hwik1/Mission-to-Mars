# Mission-to-Mars
Module 10 challenge prepared by Hannah Wikum - February 2022

## Resources
Data Source: Information scraped from https://data-class-mars.s3.amazonaws.com/Mars/index.html, https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html, https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html, https://marshemispheres.com/

Software: Jupyter Notebook, Visual Studio Code, MongoDB, Splinter, BeautifulSoup, Flask and WebDriverManager
___
## Overview of Project
This project was completed to automate a web scraping procedure with a click of a button in order to pull the most recent news, images, facts, and hemisphere images for the planet of Mars and display it in a web application.

Here is a high-level summary of the steps:
1. Use Splinter, Beautiful Soup, and WebDriver dependencies in Jupyter Notebook to visit a Chrome browser for specific URLs, click on buttons or titles if necessary, and use HTML tags to find the correct attribute (i.e. title, paragraph summary, image, etc.)

2. Export results to a Python file in Visual Studio Code and clean up extra lines

3. Turn the code written in the Jupyter Notebook/Python file into a function that can be called

4. Create an app.py file that connects the scraping file to MongoDB and Flask

5. Use HTML coding in the index.html file under templates to customize the resulting web application
    * Included adding a header and button to automate scraping, formatting images and tables, etc.

6. Run the app.py file using Anaconda Prompt/PythonData environment where the dependencies were installed

7. Open the web application and click the scraping button to load new information

8. Make the web application mobile responsive by adding xs column size to the existing medium code

9. Customize the web application by changing the color of the button and changing the color/centering the orientation of the caption showing each hemisphere name
