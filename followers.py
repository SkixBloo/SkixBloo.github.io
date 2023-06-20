from flask import Flask, render_template, jsonify, send_file, redirect
from datetime import datetime
import requests
import random
import json
import os

def follower_count(self):
  id = os.environ['ID']
  data = requests.get(f"https://api.allorigins.win/get?url=https://scratchstats.com/api2/live/id/{id}").json()["contents"] # JSON won't split during requesting process
  data = data.split('{"count":')[1]
  data = data.split(',')[0]
  return data

app = Flask("")
followers = follower_count('BluShuMon')

@app.route("/")
def homepage():
  return render_template('index.html', count=followers)
