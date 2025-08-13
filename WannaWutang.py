# Time to make web scraping tool for wutang name generator!

# from selenium import webdriver
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Setup Chrome options if needed (optional)
from selenium.webdriver.chrome.options import Options


def talk_to_website(user_input):
    file_path = "test.txt"
    
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')  # Ignore SSL certificate errors (optional)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Hide annoying DevTools messages
    
    # Initialize the driver with automatic management of the executable
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    url = 'https://www.mess.be/inickgenwuname.php'
    driver.get(url)

    try:
        driver.find_element(By.NAME, 'realname').send_keys(user_input)
        driver.find_element(By.NAME, "Submit").click()

        # Wait for the result to load
        driver.implicitly_wait(5)  # Wait for up to 5 seconds for elements to be visible
        
        elements = driver.find_elements(By.CLASS_NAME, 'normalText')
        if elements:
            with open(file_path, 'w', encoding='utf-8') as file:
                for e in elements:
                    file.write(e.text)
        else:
            print("No results found!")

    except Exception as e:
        print(f"Error during scraping: {e}")
    
    finally:
        driver.quit()
        process_file(file_path)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.readline()  # Skip unnecessary lines
            f.readline()  # Skip another line
            result = f.readline().strip()  # Read the result and strip extra whitespace
            
            # Clean up unwanted strings
            result = re.sub(r'you will also be known as', '', result)
            result = re.sub(r'ï¿½', '', result)
            result = re.sub(r'TweetUPDATE:.*', '', result)  # Remove anything after "TweetUPDATE"
            
            print(result)
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    print("HELLO! Welcome to the web scrapper python script for the Wu-Tang name generator.")
    user_input = input("Enter your name you wish to be wutanged:\n")
    
    print(f"\nAs I speaketh in a tongue you can understand, thy name shall be called no more {user_input}, You shall now be known as:")
    talk_to_website(user_input)
    print("Buh bye!")

if __name__ == "__main__":
    main()












# submit_button = driver.find_element('Enter the Wu-Tang')

# input_box.send_keys('g')
# submit_button.click()

# result = driver.find_element_by_id('result_element_id_here').text  # Adjust accordingly
# print(result)

# driver.quit()
# # 

# payload = {"name": "grandpa"}

# # response = requests.get(url, verify=False, params=payload) #https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror

# params = urllib.parse.quote_plus("grandpa")
# # response = urllib.request.URLopener(url, params)

# response = requests.get(url, params=evt.fields)


# if response.status_code == 200:

#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup.prettify())
# else:
#     print("Failed to get page")

# with open(url) as fp:
#     soup = BeautifulSoup(fp)

# soup = BeautifulSoup("<html>data</html>")

# http = urllib3.PoolManager(
#     cert_reqs='CERT_NONE',
#     assert_hostname=False
# )
# resp = http.request(
#     "POST",
#     "https://www.mess.be/inickgenwuname.php",
#     fields={'g': 'input'}
#     )

# print(resp.data.decode('utf-8'))