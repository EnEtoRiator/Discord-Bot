import disnake
from disnake.ext import commands

def register_command(client: commands.Bot):

    @client.event
    async def on_guild_join(guild: disnake.Guild):
        print(f"Joined guild: {guild.name}")