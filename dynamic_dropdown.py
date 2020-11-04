from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\rahul.saxena\\OneDrive - Qualitest Group\\Desktop\\Python Practice\\ChromeDriver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

country_box=driver.find_element_by_id("autosuggest")
country_box.send_keys("Ind")
time.sleep(2)

country_list=driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a")

for country in country_list:
	if country.text=="India":
		country.click()
		break

print(country_box.get_attribute('value'))

