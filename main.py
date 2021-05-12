
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import functions
import time
import sys
import threading

from urllib.request import urlopen

PATH = "/bin/chromedriver"
driver = webdriver.Chrome(PATH)

def checkStock(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("latin-1")
    if html.find("Sorry, this item is out of stock.") == -1:
        print("In Stock")
        return True
    else:
        print("Not In Stock")
        print(url)
        time.sleep(5)
        return False

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
    #functions.payConfirm(driver)
    print("Found in Stock")
    sys.exit()

def mainLoop():
    urlList = []
    read = open("urls.txt","r")
    for line in read:
        urlList.append(line)
    print("No of URLS:",len(urlList))
    for i in range(len(urlList)):
        print(i)
        globals()["thread" + str(i)] = threading.Thread(target=checkStockLoop,args=(urlList[i],))
        globals()["thread" + str(i)].start()
         

def checkStockLoop(url):
    running = True
    while running == True:
        if checkStock(url) == True:
            print("Stock Found")
            runBuy(url)

mainLoop()