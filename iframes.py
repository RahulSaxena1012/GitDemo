from selenium import webdriver
import time


driver=webdriver.Chrome(executable_path="C:\\Users\\rahul.saxena\\OneDrive - Qualitest Group\\Desktop\\Python Practice\\ChromeDriver\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

frame = driver.switch_to.frame("mce_0_ifr")
text_field_in_frame = driver.find_element_by_id("tinymce")
text_field_in_frame.clear()
time.sleep(1)
text_field_in_frame.send_keys("I am able to write here.")

driver.switch_to.default_content()

print(driver.find_element_by_xpath("//h3").text)

time.sleep(1)

driver.close()