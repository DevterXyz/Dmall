import discord
import pystyle

from pystyle import *


banner = """

 ██░ ██  ▒█████   ▒█████  ▓█████▄    ▓█████▄  ███▄ ▄███▓ ▄▄▄       ██▓     ██▓    
▓██░ ██▒▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌   ▒██▀ ██▌▓██▒▀█▀ ██▒▒████▄    ▓██▒    ▓██▒    
▒██▀▀██░▒██░  ██▒▒██░  ██▒░██   █▌   ░██   █▌▓██    ▓██░▒██  ▀█▄  ▒██░    ▒██░    
░▓█ ░██ ▒██   ██░▒██   ██░░▓█▄   ▌   ░▓█▄   ▌▒██    ▒██ ░██▄▄▄▄██ ▒██░    ▒██░    
░▓█▒░██▓░ ████▓▒░░ ████▓▒░░▒████▓    ░▒████▓ ▒██▒   ░██▒ ▓█   ▓██▒░██████▒░██████▒
 ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒     ▒▒▓  ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░
 ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒     ░ ▒  ▒ ░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░
 ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░     ░ ░  ░ ░      ░     ░   ▒     ░ ░     ░ ░   
 ░  ░  ░    ░ ░      ░ ░     ░          ░           ░         ░  ░    ░  ░    ░  ░
                           ░          ░                                           

"""

print(Colorate.Horizontal(Colors.green_to_blue, banner, 1))
print()
print()
token = Write.Input("[+]      Token Discord -> ", Colors.green_to_blue, interval=0.0025)

dmallmessage = Write.Input("[+]      Message de dmall -> ", Colors.green_to_blue, interval=0.0025)

client = discord.Client()


@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(dmallmessage)
      print(Colorate.Horizontal(Colors.green_to_blue, f"Message envoyé avec succès à {user.name}", 1))
    except:
       print(Colorate.Horizontal(Colors.green_to_blue, f"Je n'ai pas pu envoyer un message à {user.name}", 1))
client.run(token, bot=False)