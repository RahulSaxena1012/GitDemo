from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\rahul.saxena\\OneDrive - Qualitest Group\\Desktop\\Python Practice\\ChromeDriver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkbox in checkboxes:
	if checkbox.get_attribute('value')=="option2":
		checkbox.click()
		break

radiobuttons = driver.find_elements_by_xpath("//input[@class='radioButton']")

for radiobutton in radiobuttons:
	if radiobutton.get_attribute('value')=="radio3":
		radiobutton.click()
		break

driver.find_element_by_xpath("//input[@id='name']").send_keys("Rahul")
driver.find_element_by_xpath("//input[@id='alertbtn']").click()
time.sleep(2)
alert = driver.switch_to.alert
alerttext = alert.text

print(alerttext)
assert "Rahul" in alerttext
alert.accept()


time.sleep(2)

driver.find_element_by_xpath("//input[@id='name']").send_keys("Rahul")
driver.find_element_by_xpath("//input[@id='confirmbtn']").click()
time.sleep(2)
alert = driver.switch_to.alert
alerttext = alert.text

print(alerttext)
assert "Rahul" in alerttext
alert.dismiss()