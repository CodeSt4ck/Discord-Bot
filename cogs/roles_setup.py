import discord
from discord.ext import commands


class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    # ROLES EMBED
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roles(self, ctx):
        channel = self.client.get_channel(764220072080048140)
        inst = discord.Embed(
            title="Welcome to the self-assignable roles system of the Robot Nation :robot:",
            description="Here you can give yourself specific roles in order to let other members know exactly who you are. To assign yourself a role, simply react with the appropriate emote. It's only possible to choose one role in each category, and you can change your roles whenever you desire.",
            color=discord.Color.red()
        )
        await channel.send(embed=inst)

        devices = discord.Embed(
            title="DEVICES",
            description="React with :computer: if you play on PC.\nReact with :mobile_phone: if you play on Mobile.",
            color=discord.Color.red()
        )
        msg = await channel.send(embed=devices)
        await msg.add_reaction("💻")
        await msg.add_reaction("📱")

        games = discord.Embed(
            title="GAMES",
            description="Valorant: :video_game:\nCSGO: :police_officer:",
            color=discord.Color.red()
        )
        msg = await channel.send(embed=games)
        await msg.add_reaction("🎮")
        await msg.add_reaction("👮")

    # ROLE ASSIGNMENT

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        payload_message_id = payload.message_id
        target_message_id1 = 843154267748696074
        target_message_id2 = 843154274673491989
        guild_id = payload.guild_id
        guild = self.client.get_guild(guild_id)
        if payload_message_id == target_message_id1:

            if payload.emoji.name == "💻":
                role = discord.utils.get(guild.roles, name="PC")
                await payload.member.add_roles(role)

            elif payload.emoji.name == "📱":
                role = discord.utils.get(guild.roles, name="MOBILE")
                await payload.member.add_roles(role)

        elif payload_message_id == target_message_id2:

            if payload.emoji.name == "🎮":
                role = discord.utils.get(guild.roles, name="Valorant")
                await payload.member.add_roles(role)

            elif payload.emoji.name == "👮":
                role = discord.utils.get(guild.roles, name="CSGO")
                await payload.member.add_roles(role)

    # ROLES REMOVAL

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        target_message_id1 = 843154267748696074
        target_message_id2 = 843154274673491989
        member = None

        if target_message_id1 == payload.message_id:
            guild = await(self.client.fetch_guild(payload.guild_id))

            if payload.emoji.name == "💻":
                role = discord.utils.get(guild.roles, name="PC")
                member = await(guild.fetch_member(payload.user_id))

            elif payload.emoji.name == "📱":
                role = discord.utils.get(guild.roles, name="MOBILE")
                member = await(guild.fetch_member(payload.user_id))

            if member is not None:
                await member.remove_roles(role)

        if target_message_id2 == payload.message_id:
            guild = await(self.client.fetch_guild(payload.guild_id))

            if payload.emoji.name == "🎮":
                role = discord.utils.get(guild.roles, name="Valorant")
                member = await(guild.fetch_member(payload.user_id))

            elif payload.emoji.name == "👮":
                role = discord.utils.get(guild.roles, name="CSGO")
                member = await(guild.fetch_member(payload.user_id))

            if member is not None:
                await member.remove_roles(role)


def setup(client):
    client.add_cog(Roles(client))
