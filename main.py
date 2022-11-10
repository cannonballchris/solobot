import os
#download the packages
os.system("pip install -r requirements.txt")

import discord
from discord.ext import commands
import json
import os 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

class SoloBot(commands.Bot):
	def __init__(self):
		intents = discord.Intents.all()
		super().__init__(command_prefix='!', intents=intents)
	
	async def on_ready(self):
		with open("config.json") as f:
			config = json.load(f)
		
		setattr(self, "role", config["verification_role"])
		print(f"Logged in as : {self.user.name}")

bot = SoloBot()

bot.load_extension("cogs.verify")
bot.run(TOKEN)
		
