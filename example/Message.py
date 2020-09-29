from CustomCommands import Commands
import discord, json
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("!커맨드추가"):
        msg = message.content[7:].split("/")
        a = msg[0]
        b = msg[1]
        Commands.Custom("Custom", message.author.id, a, b)
        await message.channel.send(f"`{a}` 라고 하시면 `{b}` 라고 할게요!")

    if message.content.startswith(""):
        with open("Custom.json", 'r', encoding="UTF8") as f:
            data = json.load(f)
        msg = message.content[0:]
        try:
            for i in data[str(message.author.id)]:
                if i == msg:
                    await message.channel.send(data[str(message.author.id)][msg])
        except:
            pass

client.run("Your Token")