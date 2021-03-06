from CustomCommand import Commands
import discord, json
from discord.ext import commands

class CustomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 커맨드추가(self, ctx, a, b):
        Commands.Custom("Custom", ctx.author.id, a, b)
        await ctx.send(f"`{a}` 라고 하시면 `{b}` 라고 할게요!")

    @commands.Cog.listener()
    async def on_message(self, message):
        with open("Custom.json", 'r', encoding="UTF-8") as f:
            data = json.load(f)
        if message.content.startswith(""):
            msg = message.content[0:]
            try:
                for i in data[str(message.author.id)]:
                    if i == msg:
                        await message.channel.send(data[str(message.author.id)][msg])
            except:
                pass

def setup(bot):
    bot.add_cog(CustomCommands(bot))