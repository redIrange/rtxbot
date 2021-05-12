import discord
import os
import multiprocessing
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
import threading
import functions as fc
PATH = "/Users/meemteam/Desktop/rtxbot/chromedriver"
driver = webdriver.Chrome(PATH)

main_loop = threading.Thread(target=fc.main_loop_1)


state_change = open("state.txt","w")
state_change.write("False")
state_change.close()


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


main_loop.start()


@client.event
async def on_message(message):
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

  message_channel = message.channel
  

client.run("ODA4MzU2MjY5MzY1OTE5NzQ0.YCFWcQ.segduLeCKR9HDaklGhllaQEZrVs")