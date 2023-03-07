# Dahlia Stock Checkr

Checks whether certain dahlias are in stock and sends an alert if so.

## Usage

First clone the repo or copy main.py and requirements.txt.

Create a virtual environment, activate it, and then install dependencies:
```
venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, in main.py, enter your Twilio account credentials.

Note that once the product comes in stock, Python's logger will write to a
log file. This prevents further messages from being sent.

I have this set up as a cronjob on my NAS.
