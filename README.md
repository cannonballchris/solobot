# Solobot

```py
Requirements: python 3.8 and above
```

## About 

Solobot is a bot made for [Solonodes](https://discord.gg/solonodes-redefining-the-techniques-of-hosting-839742744099422208). The bot as of now is meant for verification purposes.
## Usage

### For Windows

Download the bot as zip file.<br/>
After downloading it, simply edit its config.json file to change the verify role. Use a valid role id, as not using it will make the bot throw errors.<br/>
Once, that is done, simply enter the bot token from discord developer portal in the .env file at the token field.<br/>

And, done, save the files, and run the main.py file.


### For Linux/Pterodactyl Panel

Download the code as zip, use a discord.py/python egg of 3.8 or 3.9 and configure its verify role in `config.json` file. Once its done, head to the .env file and add the token. Save the bot and once, its done, you may now head to startup tab and set the bot file name to `main.py`. You don't have to worry about installation packages, the bot auto installs it. Once all that is done, hit run and the bot is ready to use.

# Commands

Use `!verify` command in the desired channel once to set the bot's verification. Delete the command after it, and the bot is ready to verify people. Do not worry about bot's restarts, the verification works even after bot's restarts.



