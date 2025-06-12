"""
# DISCORD BOT sample
**by EnEtoRiator** akka *a system issue*

New presented version of discord bot blank with some functional.

**Feel free to use** all samples of code,
**BUT** if these samples were usefull for you, please give a star at my repository at GitHub:
https://github.com/EnEtoRiator
"""
# MAIN IMPORTS
import disnake
from disnake.ext import commands
# SUPPORT IMPORTS
from classes import startup
from classes.slash_commands import ping_pong
from classes.events import on_guild_join
# BOT INITIALIZATION
client = commands.Bot(command_prefix='!', intents=disnake.Intents.all())


if __name__ == '__main__':
    # write all comands and events register below
    
    # Commands
    ping_pong.register_command(client=client)
    
    # Events
    on_guild_join.register_command(client=client)
    
    # actually logic end of code by looped bot activation.
    startup.START_UP(client=client)
    # there code will be work after you turn off bot.
    print("Bot is offline.")
    input("")