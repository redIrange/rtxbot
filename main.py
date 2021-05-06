from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import functions
import time
from urllib.request import urlopen
PATH = "/bin/chromedriver"
driver = webdriver.Chrome(PATH)

def checkStock(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("latin-1")
    file = open("file.txt","w")
    for line in html:
        file.write(line)
    with open('file.txt') as f:        
        if 'Sorry, this item is out of stock.' in f.read():
            print("Not In Stock")
            return False
            
        else:
            print("In Stock")
            return True
            


def read_url_file(step):
    count = 0
    read = open("urls.txt","r")
    for i in read:
        print(i)
        if count == step:
            return i
        else:
            count += 1

def runBuy(url):
    driver.get(url)
    functions.acceptCookies(driver)
    functions.addToBasket(driver)
    functions.inputAdress(driver)
    functions.searchAdress(driver)
    functions.confirmAdress(driver)
    functions.enterEmail(driver)
    functions.enterPassword(driver)
    functions.payButton(driver)
    functions.enterCCNum(driver)
    functions.enterCName(driver)
    functions.enterMM(driver)
    functions.enterYY(driver)
    functions.enterCVC(driver)
    functions.payConfirm(driver)


programRunning = True
while programRunning:
    count = 0
    read = open("urls.txt","r")
    for url in read:
        result = checkStock(url)
        if result ==True:
            runBuy(url)

