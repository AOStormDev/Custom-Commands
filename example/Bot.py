from CustomCommands.Commands import Custom
import discord, json
from discord.ext import commands

bot = commands.Bot(command_prefix="/")

@bot.command()
async def 커맨드추가(ctx, a, b):
    Custom("Custom", ctx.author.id, a, b)
    await ctx.send(f"`{a}` 라고 하시면 `{b}` 라고 할게요!")

@bot.event
async def on_message(message):
    with open("Custom.json", 'r', encoding='UTF8') as f:
        data = json.load(f)
    if message.content.startswith(""):
        msg = message.content[0:]
        try:
            for i in data[str(message.author.id)]:
                if i == msg:
                    await message.channel.send(data[str(message.author.id)](msg))
        except:
            pass

bot.run("Your Token")
