from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\rahul.saxena\\OneDrive - Qualitest Group\\Desktop\\Python Practice\\ChromeDriver\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
title=driver.title
print("Title :", title)
name=driver.find
driver.close()



#https://www.rahulshettyacademy.com/angularpractice/