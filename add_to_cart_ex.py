from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#promoCodes = ["rahulshettyacademy","rahul","123"]

#for promoCode in promoCodes:
driver=webdriver.Chrome(executable_path="C:\\Users\\rahul.saxena\\OneDrive - Qualitest Group\\Desktop\\Python Practice\\ChromeDriver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

searchbtn = driver.find_element_by_xpath("//input[@type='search']")
searchbtn.send_keys("be")

time.sleep(2)

add_to_cart_btns=driver.find_elements_by_xpath("//div[@class='product-action']/button")
#product_names= driver.find_elements_by_xpath("//div[@class='product-action']/button/parent::*/parent::*/h4")
#product_names = add_to_cart_btns.find_elements_by_xpath("/parent::*/parent::*/h4")

list_of_items =[]

for add_to_cart_btn in add_to_cart_btns:
	product_name = add_to_cart_btn.find_element_by_xpath("parent::*/parent::*/h4")
	list_of_items.append(product_name.text)
	add_to_cart_btn.click()

cart_icon=driver.find_element_by_xpath("//a[@class='cart-icon']/img")
cart_icon.click()

time.sleep(2)

proceed_to_checkout_btn = driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
proceed_to_checkout_btn.click()

time.sleep(2)

items_on_payment_page = driver.find_elements_by_xpath("//p[@class='product-name']")
list_of_items_on_payment_page =[]

for item_on_payment_page in items_on_payment_page:
	list_of_items_on_payment_page.append(item_on_payment_page.text)

sum_of_items=0

items_amount = driver.find_elements_by_xpath("//table/tbody/tr/td[5]/p")

for item_amount in items_amount:
	sum_of_items += float(item_amount.text)

print("Total : ", sum_of_items)

total_amount_field = driver.find_element_by_xpath("//span[@class='discountAmt']")
total_amount = float(total_amount_field.text)
cost_before_discount = total_amount
print(cost_before_discount)

assert (list_of_items == list_of_items_on_payment_page)
assert sum_of_items == cost_before_discount

promocode_txtbox=driver.find_element_by_xpath("//input[@class='promoCode']")
promocode_txtbox.send_keys("rahulshettyacademy")

promocode_btn=driver.find_element_by_xpath("//button[text()='Apply']")
promocode_btn.click()

wait = WebDriverWait(driver,10)
promoCode_success = wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
#promoCode_success = driver.find_element_by_xpath("//span[@class='promoInfo']")
#total_amount_field = driver.find_element_by_xpath("//span[@class='discountAmt']")
total_amount = float(total_amount_field.text)
cost_after_discount = total_amount
print(cost_after_discount)

assert (cost_before_discount>cost_after_discount)
driver.close()
