from re import S
import discord
import time
import sys
from pip import main
import requests
import threading
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#state var setup and global setup
global tabs
global state
state = 0

def read_file(fn,line):
    # returns line of any file
    temp = []
    read = open(fn, "r")
    for i in read:
        temp.append(i)
    return(temp[int(line)])


def check_stock(url,driver):
    print("thread " + str(driver) + " is running")
    run = True

    # loop to check stock continously
    while run == True and state == 1:
        time.sleep(1)
        temp = []
        page = requests.get(url)
        for i in page:
            temp.append(i)

        # checks if item is in stock and calls function to buy
        find = str(temp).find("Sorry, this item is out of")
        find2 = str(temp).find("Out of stock")
        if find == -1 or find2 == -1:
            # check stock for each website you can buy for
            if url[12:23] == "endclothing":
                EndClothing_buy(url, driver)
            elif url[12:18] == "currys":
                currys_buy(url, driver)
            run = False
        else:
            print("out of stock")

def create_threads():
    # create threads and chrome windows

    # configure driver
    cwd = os.getcwd()
    PATH = cwd + "/chromedriver"
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    service = Service(PATH)

    # configure vars
    thread_body = {}
    tabs = {}
    count = 0

    # iterate through all urls
    read = open("urls.txt", "r")
    for line in read:
        url = line[0:-3]
        instances = line[-2:-1]

        for i in range(int(instances)):
        # create thread and chrome windows for each link
            tabs["{0}".format(count)] = webdriver.Chrome(service=service, desired_capabilities=caps)
            thread_body["{0}".format(count)] = threading.Thread(target=check_stock, args=(url, tabs["{0}".format(count)]))
            thread_body[str(count)].start()

            count = count + 1

    read.close()

def test_buy(url, driver):
    # test buying on oscarg.co.uk

    driver.get(url)

    run = True
    while run:
        try:
            checkout = driver.find_element(
                By.XPATH, "//*[@id='post-39']/div/div/div/a")
            driver.execute_script("arguments[0].click();", checkout)
            run = False
        except:
            print("Button not there")


def currys_buy(url, driver):
    # buys on currys.co.uk
    driver.get(url)
    run = True
    while run:
        time.sleep(2)
        try:
            checkout = driver.find_element(
                By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
            driver.execute_script("arguments[0].click();", checkout)
            run = False
        except:
            print("Button not there")

def EndClothing_buy(url, driver):
    # buys on endclothing.com
    print("endcloting.com")
    driver.get(url)

    run = True
    while run:
        time.sleep(10)
        #try:
        seize = driver.find_element(By.LINK_TEXT, "UK 10.5")
        driver.execute_script("arguments[0].click();", seize)
        run = False
        #except:
            #print("failed")
    
    basket = driver.find.element(By.XPATH, "//*[@id='__page_wrapper']/div/div[1]/div[3]/div/div[4]/div[1]/button/div")
    driver.execute_script("arguments[0].click();", basket)

    

def discord_main(token):
    # discord remote control function
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        global message_date
        message_date = message
        if message.content == "!start":
            print("start")
            await message.channel.send("Starting search")

            state_change = open("state.txt", "w")
            state_change.write("True")
            state_change.close()

        elif message.content == "!stop":
            print("stop")
            await message.channel.send("Stopping search")

            state_change = open("state.txt", "w")
            state_change.write("False")
            state_change.close()

        elif message.content == "!exit":
            print("exiting")
            await message.channel.send("quiting")
            sys.exit()

    client.run(token)

main_run = True
while main_run:
    # control loop
    menu = int(input("""
0: Quit
1: Start
2: Stop
    """))
    if menu == 0:
        sys.exit()
    if menu == 1:
        state = 1
        create_threads()
    if menu == 2:
        state = 0
