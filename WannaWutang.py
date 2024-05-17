# Time to make web scraping tool for wutang name generator!

# from selenium import webdriver
import re
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options if needed (optional)
from selenium.webdriver.chrome.options import Options


def talk_to_website(input):
    file_path = "test.txt"
    
    
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')  # Ignore SSL certificate errors (optional)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) #mfin devTools messages are annoying ainnit https://stackoverflow.com/questions/47417581/selenium-chromedriver-how-to-disable-the-messagedevtools-on-ws
        # chrome_options.add_argument('--disable-proxy-certificate-handler')
        # chrome_options.add_argument('--disable-content-security-policy')
        #chrome_options.add_argument('--no-sandbox')  # Bypass OS security model (optional, not recommended for production)

        # Initialize the driver with automatic management of the executable
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    url = 'https://www.mess.be/inickgenwuname.php'
    #print("hello1")
    driver.get(url)
    #print("hello2")
    driver.find_element(By.NAME, 'realname').send_keys(input)
    #print("hello3")
    driver.find_element(By.NAME, "Submit").click()

    elements = driver.find_elements(By.CLASS_NAME, 'normalText')
    with open(file_path, 'w', encoding='utf-8') as file:
        for e in elements:
            #print(e.text)
            file.write(e.text)
    
    driver.quit()
    process_file(file_path)

def process_file(file_path):
    f = open(file_path, 'r')
    
    f.readline()
    f.readline()
    str = f.readline()
    str = re.sub('you will also be known as' , '', str) 
    str = re.sub('ï¿½', '', str)
    str = re.sub('TweetUPDATE: Like the Wu-Tang Name Generator on Facebook and share your Wu name on our page! And stay tuned for a massive update, cheats, etc.', '', str)
    print(str)
    
      


def main():
        print("HELLO! Welcome to the web scrapper python script for the wutang website,")
        user_input = input("Enter your name you wish to be wutanged:\n")
        #print(f"\nDearest {user_input}, from this day forward your name is no longer {user_input}, :") for as anyone is concered,I hast thou power with GOD and with humans, and hast prevailed!
        print(f"\nAs I speaketh in a tongue you can understand, thy name shall be called no more {user_input}, You shall now be known as:")
        talk_to_website(user_input)
        print("Buh bye!")


if __name__=="__main__":
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