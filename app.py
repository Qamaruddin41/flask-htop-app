from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Mohammed Qamaruddin"  
    username = os.getenv("USER", "Unknown")

    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

