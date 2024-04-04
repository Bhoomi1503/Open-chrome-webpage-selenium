# selenium 
# cypress
# phantomJS,kobiton,lambda test

#libraries
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Driver path
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome (service = Service (ChromeDriverManager().install()),
                            options = options)
# Enter to the site
driver.get("https://www.neuralnine.com/")
# Maximize Window
driver.maximize_window()
#path
links = driver.find_elements("xpath", "//a[@href]")

for link in links:
   if "Books" in link.get_attribute("innerHTML"):
    link.click()
    break
time.sleep(3)
book_links = driver.find_elements("xpath", 
                                  "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a")

# for book_link in book_links:
#   print(book_link.get_attribute("innerHTML"))

# for book_link in book_links:
#   print(book_link.get_attribute("href"))

book_links[0].click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(3)

buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Taschenbuch')]]]//span[text()[contains(., '$')]]")

for button in buttons:
  print(button.get_attribute("innerHTML").replace("&nbsp;", " "))