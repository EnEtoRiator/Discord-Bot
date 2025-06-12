# MAIN IMPORTS
import os
from disnake.ext import commands

def START_UP(client: commands.Bot) -> None:
    """
    # CLIENT RUN

    Args:
        client (commands.Bot):
        Takes your initialized bot class.
    
    Also before \"client.run()\" can be added some code to make some stuff before bot will started up.
    """
    client.run(open('TOKEN', 'r').read())