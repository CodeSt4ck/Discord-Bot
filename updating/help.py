# REMOVING DEFAULT HELP COMMAND
client.remove_command("help")

# HELP COMMAND


@client.command()
async def help(ctx):
    owner = str(ctx.guild.owner)
    embed = discord.Embed(
        title="CONAN-BOT",
        description="Commands",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(
        url="https://www.pngitem.com/pimgs/m/122-1222931_discord-bot-logo-hd-png-download.png")
    embed.add_field(name="!help", value="List all commands", inline=True)
    embed.add_field(name="!ping", value="Reply with 'pong!'", inline=True)
    embed.add_field(name="Owner", value=owner, inline=False)

    await ctx.send(embed=embed)