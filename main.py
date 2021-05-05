from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "/Users/meemteam/Desktop/rtxbot/chromedriver"
driver = webdriver.Chrome(PATH)

def read_file(step):
    count = 0
    read = open("details.txt","r")
    for i in read:
        print(i)
        if count == step:
            return i
        else:
            count += 1

driver.get("https://www.currys.co.uk/gbuk/computing/pc-monitors/pc-monitors/dell-se2219h-full-hd-22-led-monitor-black-10186886-pdt.html")

try:
    cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookies.click()
except:
    print("\n")

try:
    basket_add = driver.find_element(By.XPATH, "//*[@id='product-actions-touch']/div[4]/div[1]/button")
    time.sleep(2)
    driver.execute_script("arguments[0].click();", basket_add)

    time.sleep(1)

    #driver.get("https://www.currys.co.uk/app/basket")

    #time.sleep(2)
    #check_out = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div/button")
    #driver.execute_script("arguments[0].click();", check_out)

    driver.get("https://www.currys.co.uk/app/checkout")

    time.sleep(4)



except:
    print("Add to basket failed")

number = 0
post_code = read_file(number)

address = driver.find_element(By.XPATH, "//*[@id='delivery_location']/input").send_keys(post_code)

time.sleep(2)

address_select = driver.find_element(By.XPATH, "//*[@id='delivery_location']/button[2]")
driver.execute_script("arguments[0].click();", address_select)

time.sleep(2)

address_confirm = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[3]/div[1]/button").click()

number = 1
mail = read_file(number)

time.sleep(4)

email = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[1]/div/input").send_keys(mail)

time.sleep(4)

try:
    email_confirm = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/button")
    driver.execute_script("arguments[0].click();", email_confirm)
except:
    print("pycharm bad")

time.sleep(10)

number = 2
password = read_file(number)

password_enter = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/input").send_keys(password)

time.sleep(4)

password_confirm = driver.find_element(By.XPATH, "//*[@id='password']/div[4]/button").click()

time.sleep(2)

pay = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/button").click()
