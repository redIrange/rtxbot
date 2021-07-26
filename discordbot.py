import discord
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import requests
import threading
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

run = True

PATH = "/Users/meemteam/Desktop/rtxbot/chromedriver"
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
driver = webdriver.Chrome(desired_capabilities=caps, executable_path=PATH)


state_change = open("state.txt","w")
state_change.write("True")
state_change.close()


def check_stock(url):
  global run
  print("thread is running")
  running = True
  while running == True:
    temp = []
    page = requests.get(url)
    for i in page:
      temp.append(i)
    find = str(temp).find("Sorry, this item is out of")
    find2 = str(temp).find("Out of stock")
    if find == -1 or find2 == -1:
      state = open("state.txt","r")
      for i in state:
        if i == "True":
          if run == True:
            run = False
            buy_gpu(url)
      state.close()
    else:
      print("out of stock")

def buy_gpu(url):
  #driver_thread = threading.Thread(target=driver_test(url))
  #driver_thread.start()
  driver.get(url)
  basket(driver)
  address(driver)
  email(driver)
  password(driver)
  pay(driver)
  pay_card(driver)
  print("############################### GPU bought ###############################")
  #message_date.channel.send("@red_range GPU bought")
  stop_search = open("state.txt","w")
  stop_search.write("False")
  stop_search.close()

def driver_test(url):
  driver.get(url)

def create_threads():
  urlList = []
  read = open("urls.txt","r")
  for line in read:
    urlList.append(line)
  print("Nomber of URLS:",len(urlList))
  range_len = len(urlList)
  for i in range(len(urlList)):
    print(i)
    globals()["thread" + str(i)] = threading.Thread(target=check_stock,args=(urlList[i],))
    globals()["thread" + str(i)].start()

def read_file(step):
    count = 0
    read = open("details.txt","r")
    for i in read:
        if count == step:
            return i
        else:
            count += 1

def basket(driver):
  count = 0
  running = True
  while running == True:
    try:
      basket_add = driver.find_element(By.XPATH, "//*[@id='product-actions-touch']/div[4]/div[1]/button")
      driver.execute_script("arguments[0].click();", basket_add)
      
      time.sleep(1)
      running = False
      driver.get("https://www.currys.co.uk/app/checkout")

      #try:
        #basket_add = driver.find_element(By.XPATH, "//*[@id='product-actions-touch']/div[4]/div[1]/button")
        #driver.execute_script("arguments[0].click();", basket_add)

      #except:
        #time.sleep(1)
        #running = False
        #driver.get("https://www.currys.co.uk/app/checkout")

    except:
      #count += 1

      #if count > 30:
        #running = False
      #else:
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
      address_confirm = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[2]/div[2]/div/div[3]/div[1]/button")
      driver.execute_script("arguments[0].click();", address_confirm)
      running = False
    except:
      running = True
      while running == True:
        try:
          address = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='delivery_location']/input"))).send_keys(post_code)
          running = False
        except:
          print("address input2 failed")

      time.sleep(6)
      
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
          shipping_confirm = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[6]/button")
          driver.execute_script("arguments[0].click();", shipping_confirm)
          running = False
        except:
          print("idk == true")
          try:
            shipping_confirm = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[2]/div[2]/div/div[3]/div[1]/button")
            driver.execute_script("arguments[0].click();", shipping_confirm)
            running = False
          except:
            print("idk 2 failed")


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
      cookie = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
      driver.execute_script("arguments[0].click();", cookie)
      running = False
    except:
      print("Go to payment failed")

  time.sleep(2)
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

create_threads()

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
    await message.channel.send("Starting GPU search")

    state_change = open("state.txt","w")
    state_change.write("True")
    state_change.close()

  elif message.content == "!stop":
    print("stop")
    await message.channel.send("Stopping GPU search")
    
    state_change = open("state.txt","w")
    state_change.write("False")
    state_change.close()

  elif message.content == "!exit":
    print("exiting")
    await message.channel.send("quiting")
    sys.exit()


client.run("ODA4MzU2MjY5MzY1OTE5NzQ0.YCFWcQ.2xBMhc3KgZPSG2YqeiQBdKn3UUM")