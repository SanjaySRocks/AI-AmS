import discord
from discord.ext import commands
from prsaw import RandomStuff

# Enter Discord bot token here

TOKEN = ''
BOT_PREFIX = '.'
CHANNEL_ID = 836574013077454878

client = commands.Bot(command_prefix=BOT_PREFIX)
rs = RandomStuff(async_mode=True)

client.remove_command('help')

@client.event
async def on_ready():
    print(f'AI Bot Ready !')


@client.event
async def on_message(message):
    if client.user == message.author:
        return

    if message.channel.id == CHANNEL_ID:
        response = await rs.get_ai_response(message.content)
        await message.reply(response)
    
    await client.process_commands(message)

client.run(TOKEN)
