import discord
from discord import app_commands
from discord.ext import commands

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("KickzAE Client | Loaded")

    try:
        synced = await client.tree.sync()
        print(f"KickzAE Client | Synced {len(synced)} command(s)")
    
    except Exception as e:
        print(e)
    
@client.tree.command(name="test")
@app_commands.describe(test_arg = "Enter Arg Here")
async def test(interaction: discord.Interaction, test_arg: str):
    await interaction.response.send_message(f"KickzAE Client | Loaded | Arg: {test_arg}", ephemeral=True) # Ephemeral means only you can see the message



client.run("MTI0NTEwNjcwNzYzMDM5MTQ5OA.Go4CXq.qDpF8sF9q6cKuo5-Oz-3Jr6CIxYltlC38HNGwQ")