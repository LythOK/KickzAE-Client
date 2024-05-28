import discord, json
from discord import app_commands
from discord.ext import commands

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

with open("config.json", "r") as chrome_controller_config:
            controller_config_raw = chrome_controller_config.read()
            config = json.loads(controller_config_raw)

@client.event
async def on_ready():
    print("KickzAE Client | Loaded")

    try:
        synced = await client.tree.sync()
        print(f"KickzAE Client | Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name="test")
@app_commands.describe(test_arg="Enter Arg Here")
async def test(interaction: discord.Interaction, test_arg: str):
    await interaction.response.send_message(f"KickzAE Client | Loaded | Arg: {test_arg}", ephemeral=True)

@client.tree.command(name="new_order")
@app_commands.describe(name="Customer's Name",
                       phone_number="Customer's Number",
                       address="Customer's Address (Maps Link)",
                       product_name="Product Name",
                       product_photo_link="Link to Product Photo (Discord Message Link)",
                       note="Extra Info")
async def new_order(interaction: discord.Interaction,
                    name: str, phone_number: str,
                    address: str, product_name: str,
                    product_photo_link: str, note: str):
    
    # Create an embed
    embed = discord.Embed(title="New Order", description="A new order has been placed.", color=discord.Color.blue())
    embed.add_field(name="Customer's Name", value=name, inline=False)
    embed.add_field(name="Phone Number", value=phone_number, inline=False)
    embed.add_field(name="Address", value=address, inline=False)
    embed.add_field(name="Product Name", value=product_name, inline=False)
    embed.add_field(name="Note", value=note, inline=False)
    embed.set_image(url=product_photo_link)  # Set the image of the product

    await interaction.response.send_message("KickzAE Client ->| > Placing Order", ephemeral=True)  # Ephemeral means only you can see the message
    await interaction.channel.send(embed=embed)  # Send the embed to the channel

client.run(config["kickzae_client_token"])