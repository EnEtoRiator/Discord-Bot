import disnake
from disnake.ext import commands

def register_command(client: commands.Bot):

    @client.slash_command()
    async def ping(inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(content='pong!')