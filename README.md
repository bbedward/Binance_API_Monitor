# Binance API Monitor

Just a simple python script I whipped up to call me when XRB is added to binance

I'm not a proficient python coder, so it probably looks bad to someone who is.

I also don't know if this is the best way to check for new coins to be added to binance, but it works as intended

# Setup

Tested w/ python 2.7

Requires twilio

`pip install twilio`

Sign up for a twilio free account, add verified caller IDs (the numbers you want the script to call have to be verified or it won't work).

Create a twilio phone number (first is free)

Update config.py with info for twilio API key, key secret, phone number, numbers to call, etc.

# Usage

`python main.py --frequency=30 --symbol='XRB'`

--frequency represents how often it will check the API (in seconds)

--symbol is the symbol to look for

# Notes

Binance API has a request limit (I believe 1200 requests per minute at time of writing), if this script exceeds it they may ban your IP (I'm not responsible if this happens to you obviously)

You can run the script first with a pair that already exists on binance, to test if phone calls work

