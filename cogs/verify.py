import discord
from discord.ext import commands


class Verify(discord.ui.View):
	def __init__(self):
		super().__init__(timeout = None)
	
	@discord.ui.button(label = "Verify", style = discord.ButtonStyle.grey, custom_id = "verifybutton", emoji = "🔓")
	async def verification(self, button:discord.ui.Button, interaction:discord.Interaction):
		bot = interaction.client
		await interaction.response.send_message("You have been verified!", ephemeral = True)
		await interaction.user.add_roles(interaction.guild.get_role(bot.role))

class Verification(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.persistent_views_added = False
	
	@commands.Cog.listener()
	async def on_ready(self):
		if not self.persistent_views_added:
			self.bot.add_view(Verify())
			self.persistent_views_added = True
	
	@commands.command()
	async def verify(self, ctx):
		embed = discord.Embed(title = "Verification Required!", description = "In order to get access to SoloNodes' Discord Server you must click the button below..", color = 0x78347c)
		await ctx.send(embed = embed, view = Verify())

def setup(bot):
	bot.add_cog(Verification(bot))
