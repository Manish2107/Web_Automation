from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)

# Install ChromeDriver and get its path
chrome_driver_path = ChromeDriverManager().install()

# Create ChromeService with the path to the ChromeDriver executable
service = ChromeService(chrome_driver_path)

# Initialize Chrome WebDriver with the specified options and service
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the website
driver.get("https://www.neuralnine.com/")
driver.maximize_window()

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break

book_links = driver.find_elements("xpath", "//div[contains(@class, 'elementor-column-wrap') and .//h2[contains(text(), '7 IN 1')] and count(.//a)=2]//a")




book_links[0].click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")

for button in buttons:
    print(button.get_attribute("innerHTML"))
