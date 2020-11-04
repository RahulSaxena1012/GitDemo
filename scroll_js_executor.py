from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
#https://rahulshettyacademy.com/#/practice-project


driver=webdriver.Chrome(executable_path="C:\\Users\\rahul.saxena\\OneDrive - Qualitest Group\\Desktop\\Python Practice\\ChromeDriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/WebTable.html")
driver.maximize_window()
time.sleep(2)

item_size_dd = Select(driver.find_element_by_xpath("//select"))
item_size_dd.select_by_visible_text("30")
time.sleep(5)
driver.execute_script("document.querySelector('div.ui-grid-viewport ng-isolate-scope').scrollTop=500;")

#add_btn = driver.find_element_by_xpath("//app-card-list/app-card[4]//button[@class='btn btn-info']")

#driver.execute_script("arguments[0].scrollIntoView();",add_btn)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

