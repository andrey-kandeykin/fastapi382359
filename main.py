import socket
import asyncio
import time
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from data import users_settings_dict
import pickle
import time
import os
import os.path
import threading
import random
import requests
from pydantic import BaseModel
import json
from fastapi import FastAPI, Request
app = FastAPI()

# class User(BaseModel):
#     user: str
#     password: str


@app.post("/")
async def root(user: Request):
    # print(user['user'], user['password'])
    res = await user.json()
    return res

@app.get("/lol")
async def root():
    return {"hahaha"}
