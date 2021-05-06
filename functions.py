from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "/bin/chromedriver"
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

def acceptCookies(driver):
    running = True
    while running:
        cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies.click()
        running = False


def addToBasket(driver):
    running = True
    while running == True:
        try:
            time.sleep(1)
            basket_add = driver.find_element(By.XPATH, "//*[@id='product-actions-touch']/div[4]/div[1]/button")
            driver.execute_script("arguments[0].click();", basket_add)
            time.sleep(1)
            driver.get("https://www.currys.co.uk/app/checkout")
            
            running = False
        except:
            print("Add to basket failed")

def inputAdress(driver):
    number = 0
    post_code = read_file(number)
    running = True
    while running == True:
        try:
            address = driver.find_element(By.XPATH, "//*[@id='delivery_location']/input").send_keys(post_code)
            running = False
        except:
            print("Input Adress Failed")

def searchAdress(driver):
    running = True
    time.sleep(2)
    while running == True:
        try:
            address_select = driver.find_element(By.XPATH, "//*[@id='delivery_location']/button[2]")
            driver.execute_script("arguments[0].click();", address_select)
            running = False
        except:
            print("Search Click failed")

def confirmAdress(driver):
    running = True
    while running:
        try:
            address_confirm = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[3]/div[1]/button").click()
            running = False
        except:
            print("Adress Confirm Failed")

def enterEmail(driver):         
    number = 1
    mail = read_file(number)

    running = True
    while running:
        try:
            email = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[1]/div/input").send_keys(mail)
            running = False
        except:
            print("Enter Email Failed")

def confirmEmail(driver):
    running = True
    while running:
        try:
            email_confirm = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/button")
            driver.execute_script("arguments[0].click();", email_confirm)
            running = False
        except:
            print("Confirm Email Failed")

def enterPassword(driver):
    number = 2
    password = read_file(number)
    running = True
    while running:
        try:
            password_enter = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/input").send_keys(password)
            running = False
        except:
            print("Enter Password Failed")
def payButton(driver):
    running = True
    while running:
        try:
            pay = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/button").click()
            running = False
        except:
            print("Pay Confirm Failed")
def enterCCNum(driver):
    number = 3
    ccNum = read_file(number)
    running = True
    while running:
        try:
            cardNumberEnter = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[1]/p[1]/input").send_keys(ccNum)
            running = False
        except:
            print("Enter CC Failed")

def enterCName(driver):
    number = 4
    CardName = read_file(number)

    running = True
    while running:
        try:
            cardNumberEnter = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[1]/p[2]/input").send_keys(CardName)
            running = False
        except:
            print("Enter C Name Failed")

def enterMM(driver):
    number = 5
    MMNum = read_file(number)
    running = True

    while running:
        try:
            cardNumberEnter = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[2]/p/span/input[1]").send_keys(MMNum)
            running = False
        except:
            print("Enter MM Failed")

def enterYY(driver):
    number = 6
    YYNum = read_file(number)
    #Expiry date YY
    running = True
    while running:
        try:
            cardNumberEnter = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[2]/p/span/input[2]").send_keys(YYNum)
            running = False
        except:
            print("Enter YY Failed")
#CVC
def enterCVC(driver):
    number = 7
    CVCNum = read_file(number)
    running = True
    while running:
        try:
            cardNumberEnter = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[2]/div/p/span[1]/span/input").send_keys(CVCNum)
            running = False
        except:
            print("Enter CVC Failed")

def payConfirm(driver):
    running = True
    while running:
        try:
            pay = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[4]/div/input").click()
            running = False
        except:
            print("Pay Now Failed")