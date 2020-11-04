from selenium import webdriver
import time
#https://rahulshettyacademy.com/#/practice-project


driver=webdriver.Chrome(executable_path="C:\\Users\\rahul.saxena\\OneDrive - Qualitest Group\\Desktop\\Python Practice\\ChromeDriver\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

driver.find_element_by_link_text("Multiple Windows").click()
time.sleep(2)

driver.find_element_by_link_text("Click Here").click()

parent_window = driver.window_handles[0]
child_window = driver.window_handles[1]

driver.switch_to.window(child_window)

heading = driver.find_element_by_xpath("//h3").text

print("Child Window :", heading)

driver.switch_to.window(parent_window)
time.sleep(2)

heading = driver.find_element_by_xpath("//h3").text
print("Parent Window :", heading)

driver.quit()