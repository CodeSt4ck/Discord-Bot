from discord.ext import commands
import json
import os


# COMMAND PREFIX
client = commands.Bot(command_prefix="!")

os.chdir(r'/Users/jangi/Desktop/Discord Bot')

# VERIFYING BOT IS ONLINE OR NOT


@client.event
async def on_ready():
    print(f'{client.user} is now online!')

# PING COMMAND


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

# LOAD COMMAND


@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} Loaded successfully.")

# LOAD_ERROR HANDLER


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Module already loaded or module not found.")

# UNLOAD COMMAND


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} Unloaded successfully.")

# UNLOAD_ERROR HANDLER


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Module already unloaded or module not found.")

# RELOAD COMMAND


@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} Reloaded successfully.")

# RELOAD_ERROR HANDLER


@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Module must be loaded first or module not found.")
    else:
        await ctx.send("Missing module name.")

# SEARCHING FILE
for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# ON MESSAGE EVENT


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith(f'!'):
        commands = [
            '!help', '!load', '!unload', '!reload',
            '!ping', '!list', '!weapon', '!place',
            '!tictactoe', '!roles', '!connect',
            '!disconnect', '!pause', '!play',
            '!resume', '!stop', '!ban', '!kick',
            '!clear', '!server', '!unban', '!level', '!update'
        ]
        msg = msg.split()[0]
        result = "Command not found."
        for command in commands:
            if command == msg:
                result = "Command found."
                break
        if result == "Command found.":
            await client.process_commands(message)
        else:
            await message.channel.send(result)


with open('data/token.json', 'r') as f:
    token = json.load(f)

client.run(token["TOKEN"])

with open('data/token.json', 'r') as f:
    json.dump(token, f)
