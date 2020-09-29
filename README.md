# 디스코드 봇 커스텀 커맨드 생성기


## 사용법
`
pip install CustomCommands
`
```py
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
```

`
Custom.Commands("Custom", ctx.author.id, a, b)
`
해당 부분은 Custom이라는 json파일이 있어야합니다. 예를 들어 File.json 파일을 만드시고 그럼 Custom.Commands("File" ...) 가
됩니다.

## Licence
- 도움말이나, 임베드 Footer에 크레딧을 남겨주세요.
- ex) 도움 : STORM#9999

## Contact
- [Mail](mailto:storm@stormdev.club)
- [STORM#9999](https://invite.gg/freeai)
- [Github](https://github.com/AODevStorm)
