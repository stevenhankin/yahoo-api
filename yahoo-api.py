from flask import Flask, redirect, request
import requests
import os

app = Flask(__name__)

# Get environment variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

@app.route("/")
def start_page():
    """
    The root page just redirects to Yahoo to get the access code
    and will return to the /logon route
    """
    url=f"https://api.login.yahoo.com/oauth2/request_auth?client_id={client_id}&response_type=code&redirect_uri=https://127.0.0.1:5000/logon"
    return redirect(url,302)

@app.route("/logon")
def logon():
  # Should have received our code from Yahoo
  code=request.args.get("code") 
  myobj={"client_id":client_id,"client_secret":client_secret,"redirect_uri":"https://127.0.0.1:5000/logon","code":code,"grant_type":"authorization_code"}
  # Get Bearer Token using new Yahoo Code + Client ID + Client Secret
  x = requests.post("https://api.login.yahoo.com/oauth2/get_token", data = myobj)
  access_token = x.json().get("access_token")
  # Call Fantasy Sports API and ask for JSON format (and supplying Bearer Token)
  headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {access_token}'
  }
  y=requests.get("https://fantasysports.yahooapis.com/fantasy/v2/game/nfl?format=json",headers=headers)
  # And show the results in the server terminal
  print(y.json())
  # ...and in the browser
  return f"<h5>Access code: {code}</h5><h5>token: {access_token}</h5><h4>Data: {y.json()}</h4>"
