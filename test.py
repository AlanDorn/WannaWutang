from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options if needed (optional)
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')  # Ignore SSL certificate errors (optional)
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model (optional, not recommended for production)

# Initialize the driver with automatic management of the executable
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# Open a webpage
driver.get('https://www.mess.be/inickgenwuname.php')

# Example interaction: Search in Google
search_box = driver.find_element("name", "q")  # Find the search box by name attribute (q is the name of Google's search box)
search_box.send_keys('Hello, world!')  # Type a search query
search_box.submit()  # Submit the search

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()
