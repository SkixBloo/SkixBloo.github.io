from flask import Flask, render_template, jsonify, send_file, redirect
from datetime import datetime
import requests
import random
import json
import os

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

def follower_count(self):
  id = os.environ['ID']
  data = requests.get(f"https://api.allorigins.win/get?url=https://scratchstats.com/api2/live/id/{id}").json()["contents"] # JSON won't split during requesting process
  data = data.split('{"count":')[1]
  data = data.split(',')[0]
  return data
# sorry for taking this Knightbot lol
