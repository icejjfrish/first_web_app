# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:34:17 2021

@author: Jaclyn Frishcosy
"""
# import matplotlib.pyplot as plt

# print("This is a test for Heroku deploying.\n")
# print(1)

# plt.plot(2, 7)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello this is the new version!"
