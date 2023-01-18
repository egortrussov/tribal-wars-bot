# A simple bot for an online game Tribal Wars  

## Initialise and start the project 

### Install dependencies 
```
pip3 install -r requirements.txt
```

### Run the project 
Before staring the project, set a valid cookie string in `cookie_str` field in the `config.py` file 

Run: 
```
python3 run.py
```

## Functionality 

The bot's functionality inclides:

- Fetching and parsing village data from the server 
- Sending attacks on specified coordinates 
- Starting a continous series of attacks with random time intervals between them  

Interraction with the bot is programmed via a simple terminal UI