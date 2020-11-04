from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\rahul.saxena\\OneDrive - Qualitest Group\\Desktop\\Python Practice\\ChromeDriver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action= ActionChains(driver)
menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
time.sleep(5)

sub_menu = driver.find_element_by_link_text("Top")
action.move_to_element(sub_menu).click().perform()
