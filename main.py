from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "/Users/meemteam/Desktop/rtxbot/chromedriver"
driver = webdriver.Chrome(PATH)

#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "element_id")))

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
    cookies = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
    cookies.click()
except:
    print(" ")
    

try:
    time.sleep(1)
    basket_add = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='product-actions-touch']/div[4]/div[1]/button")))
    driver.execute_script("arguments[0].click();", basket_add)

    time.sleep(1)

    driver.get("https://www.currys.co.uk/app/checkout")


except:
    print(" ")


number = 0
post_code = read_file(number)

address = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='delivery_location']/input"))).send_keys(post_code)

time.sleep(1)

running = True
while running == True:
    try:
        address_select = driver.find_element(By.XPATH, "//*[@id='delivery_location']/button[2]")
        driver.execute_script("arguments[0].click();", address_select)
        running = False
    except:
        print(" ")

running = True
while running == True:
    try:
        address_confirm = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[3]/div[1]/button"))).click()
        rinning = False
    except:
        print(" ")


number = 1
mail = read_file(number)

time.sleep(1)

email = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[1]/div/input").send_keys(mail)

#time.sleep(1)

try:
    email_confirm = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/button")
    driver.execute_script("arguments[0].click();", email_confirm)
except:
    print(" ")

time.sleep(1)

number = 2
password = read_file(number)

try:
    password_enter = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/input").send_keys(password)
    password_confirm = driver.find_element(By.XPATH, "//*[@id='password']/div[4]/button").click()

except:
    time.sleep(1)
    password_enter = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/input").send_keys(password)
    password_confirm = driver.find_element(By.XPATH, "//*[@id='password']/div[4]/button").click()

trying = True

while trying == True:
    try:
        pay = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/button")
        pay.click()
        trying = False
    except:
        print(" ")