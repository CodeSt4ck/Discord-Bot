import discord
import datetime
from discord.ext import commands


class Manager(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # SERVER COMMAND


    @commands.command()
    async def server(self, ctx):
        channel = self.client.get_channel(843501907028475924)
        name = ctx.guild.name
        description = ctx.guild.description
        region = ctx.guild.region
        icon = ctx.guild.icon_url
        memberCount = ctx.guild.member_count
        owner = str(ctx.guild.owner)
        embed = discord.Embed(
            title=name,
            description=description,
            color=discord.Color.dark_red()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Members", value=memberCount, inline=True)

        await channel.send(embed=embed)

    # CLEAR COMMAND


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=None, day=None, month=None, year=None):
        if amount == "-":
            amount = None
        else:
            amount = int(amount) + 1
        if day != None and month != None and year != None:
            date = datetime.datetime(int(year), int(month), int(day))
        else:
            date = None

        await ctx.channel.purge(limit=amount, after=date)

    # CLEAR_ERROR HANDLER


    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Permission Denied!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument(s)")
        else:
            await ctx.send("Missing argument(s)")

    # KICK COMMAND


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        channel = self.client.get_channel(843501907028475924)
        await member.kick(reason=reason)
        await channel.send(f"User {member.mention} has been kicked")

    # kick_ERROR HANDLER


    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Permission Denied!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument(s)")
        else:
            await ctx.send("Error: Maybe invalid username or person you trying to kick is admin.")

    # BAN COMMAND


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        channel = self.client.get_channel(843501907028475924)
        await member.ban(reason=reason)
        await channel.send(f"User {member} has been banned")

    # BAN_ERROR HANDLER


    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Permission Denied!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument(s)")
        else:
            await ctx.send("Error: Maybe invalid username or person you trying to ban is admin.")

    # UNBAN COMMAND


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        channel = self.client.get_channel(843501907028475924)
        banned_members = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_members:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await channel.send(f"Unbanned: {user.mention}")

    # UNBAN_ERROR HANDLER


    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Permission Denied!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument(s)")
        else:
            await ctx.send("Error: Maybe invalid username or user is not banned.")

def setup(client):
    client.add_cog(Manager(client))