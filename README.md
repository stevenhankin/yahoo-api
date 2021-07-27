# Yahoo API

Simple Python application demonstrating how to connect to the Yahoo Fantasy Sport API using Yahoo OAuth

## Requirements

* Python 3

## Installation

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
1) Setup your "app" on Yahoo: https://developer.yahoo.com/apps/
2) Set your environment variables
    ```
    export CLIENT_ID=<Your Yahoo Client ID>
    export CLIENT_SECRET=<Your Yahoo Client Secret>
    ```
3) Start app
    ```
    export FLASK_APP=hello
    python -m flask run --cert=adhoc
    ```
4) Open in browser [https://127.0.0.1:5000/](https://127.0.0.1:5000/)
