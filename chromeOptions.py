from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")

driver=webdriver.Chrome(executable_path="C:\\Users\\rahul.saxena\\OneDrive - Qualitest Group\\Desktop\\Python Practice\\ChromeDriver\\chromedriver.exe",options=chrome_options)
driver.get("http://demo.automationtesting.in/WebTable.html")
print(driver.title)