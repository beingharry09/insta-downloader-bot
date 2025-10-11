from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Instagram Downloader Bot is running!"

@app.route('/start')
def start_bot():
    subprocess.Popen(["python3", "best_instagram_downloader.py"])
    return "Bot started successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
