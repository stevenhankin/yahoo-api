# Yahoo API


Simple Python application demonstrating how to connect to the Yahoo Fantasy Sport API using Yahoo OAuth

---

![](https://media.giphy.com/media/UmtyHb5JfCH3WfTsEr/giphy.gif)

---

## Contents
- [Yahoo API](#yahoo-api)
  - [Contents](#contents)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)

---

## Requirements

* Python 3

---

## Installation

```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Usage
1) Setup your "app" on Yahoo: https://developer.yahoo.com/apps/

    ⚠ **Important** - set Redirect URI(s) as follows:   `https://127.0.0.1:5000/logon`

2) Set your environment variables
    ```
    export CLIENT_ID=<Your Yahoo Client ID>
    export CLIENT_SECRET=<Your Yahoo Client Secret>
    ```
3) Start app
    ```
    export FLASK_APP=yahoo-api
    python -m flask run --cert=adhoc
    ```
4) Open in browser [https://127.0.0.1:5000/](https://127.0.0.1:5000/)

5) Accept the warnings about the ad hoc certificate and proceed

The API Data should hopefully be displayed both in your browser and in the terminal
