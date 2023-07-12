from flask import flask, render_template, jsonify, send_file, redirect
import os
import json

def follower_count(self):
  id = os.enviorn['ID']
  data =
  requests.get(f"https://api.allorigins.win/get?url=https://scratchstats.com/api2/live/id/{id}").json()["contents"]
  data = data.split('{"count":')[1]
  data = data.split(',')[0]
  return data
  app = Flask("")
followers = follower_count('BluShuMon')

@app.route('/about')
def about():
  return render_template('Aboutme.html', count=followers)
