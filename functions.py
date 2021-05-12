from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.request import urlopen
import sys
import requests

PATH = "/Users/meemteam/Desktop/rtxbot/chromedriver"
driver = webdriver.Chrome(PATH)

url = "https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/asus-geforce-rtx-3070-8-gb-dual-graphics-card-10215777-pdt.html"

#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "element_id")))

def read_file(step):
    count = 0
    read = open("details.txt","r")
    for i in read:
        if count == step:
            return i
        else:
            count += 1

def cookies(driver):
    running = True
    count = 0
    while running == True:
        if count <= 1:
            try:
                cookies = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
                cookies.click()
                running = False
            except:
                print("cookie accept failed")
                count += 1
        else:
            running = False

def basket(driver):
    running = True
    while running == True:
        try:
            basket_add = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='product-actions-touch']/div[4]/div[1]/button")))
            driver.execute_script("arguments[0].click();", basket_add)

            running = False
            driver.get("https://www.currys.co.uk/app/checkout")

        except:
            print("basket add failed")

def address(driver):
    number = 0
    post_code = read_file(number)

    running = True
    while running == True:
        try:
            address = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='delivery_location']/input"))).send_keys(post_code)
            running = False
        except:
            print("address input failed")

    time.sleep(2)

    running = True
    while running == True:
        try:
            address_select = driver.find_element(By.XPATH, "//*[@id='delivery_location']/button[2]")
            driver.execute_script("arguments[0].click();", address_select)
            running = False
        except:
            print("address select failed")

    running = True
    while running == True:
        try:
            address_confirm = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[3]/div[1]/button")
            driver.execute_script("arguments[0].click();", address_confirm)
            running = False
        except:
            try:
                address_select = driver.find_element(By.XPATH, "//*[@id='delivery_location']/button[2]")
                driver.execute_script("arguments[0].click();", address_select)
            except:
                print("address confirm failed")

def email(driver):
    number = 1
    mail = read_file(number)
    running = True
    while running == True:
        try:
            email = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[1]/div/input").send_keys(mail)
            running = False
        except:
            print("Email input failed")

    running = True
    while running == True:
        try:
            email_confirm = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/button")
            driver.execute_script("arguments[0].click();", email_confirm)
            running = False
        except:
            print("email confirm failed")

def password(driver):
    number = 2
    password = read_file(number)

    running = True
    while running == True:
        try:
            password_enter = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/input").send_keys(password)
            password_confirm = driver.find_element(By.XPATH, "//*[@id='password']/div[4]/button")
            driver.execute_script("arguments[0].click();", password_confirm)
            running = False
        except:
            print("password confirm failed")

def pay(driver):
    running = True
    while running == True:
        try:
            pay = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/button")
            driver.execute_script("arguments[0].click();", pay)
            running = False
        except:
            print("Go to payment failed")

def pay_card(driver):
    number = 3
    card_number = read_file(number)

    running = True
    while running == True:
        try:
            card_enter = driver.find_element(By.ID, "cardNumber").send_keys(card_number)
            running = False
        except:
            print("card number failed")

    number = 4
    card_number = read_file(number)

    running = True
    while running == True:
        try:
            card_enter = driver.find_element(By.ID, "expiryMonth").send_keys(card_number)
            running = False
        except:
            print("card number failed")

    number = 5
    card_number = read_file(number)

    running = True
    while running == True:
        try:
            card_enter = driver.find_element(By.ID, "expiryYear").send_keys(card_number)
            running = False
        except:
            print("card number failed")

    number = 6
    card_number = read_file(number)

    running = True
    while running == True:
        try:
            card_enter = driver.find_element(By.ID, "securityCode").send_keys(card_number)
            running = False
        except:
            print("card number failed")

    number = 7
    card_number = read_file(number)

    running = True
    while running == True:
        try:
            card_enter = driver.find_element(By.ID, "cardholderName").send_keys(card_number)
            running = False
        except:
            print("card number failed")

    running = True
    while running:
        try:
            pay = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[4]/div/input").click()
            running = False
        except:
            print("Pay Now Failed")

def main_loop_1():
    url = "https://www.currys.co.uk/gbuk/computing/pc-monitors/pc-monitors/samsung-c24f396-full-hd-24-curved-led-monitor-10146138-pdt.html"
    running = True
    while running == True:
        state = open("state.txt","r")
        for i in state:
            if i == "True":
                check = check_stock(url)
                if check == True:
                    driver.get(url)
                    basket(driver)
                    address(driver)
                    email(driver)
                    password(driver)
                    pay(driver)
                    pay_card(driver)
                    print("############################### GPU bought ###############################")
                else:
                    print("Not in stock")

def check_stock(url):
    temp = []
    page = requests.get(url)
    for i in page:
        temp.append(i)
    find = str(temp).find("Sorry, this item is out of")
    if find == -1:
        return True
    else:
        return False