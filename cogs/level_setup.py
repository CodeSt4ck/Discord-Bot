import discord
import json
import os
from discord.ext import commands


class Levels(commands.Cog):

    def __init__(self, client):
        self.client = client

    os.chdir(r'/Users/jangi/Desktop/Discord Bot')

    # ON NEW MEMBER JOIN
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('data/users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(self, users, member)

        with open('data/users.json', 'w') as f:
            json.dump(users, f)

    # ON MESSAGE
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        with open('data/users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, message.author)
        await self.add_experience(users, message.author, 5)
        value = await self.level_up(users, message.author)

        if value:
            await message.channel.send(f"Congrats! {message.author.mention} reached Level {users[str(message.author.id)]['level']}.")

        with open('data/users.json', 'w') as f:
            json.dump(users, f)

    # LEVEL COMMAND
    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        channel = self.client.get_channel(843501907028475924)
        if member == None:
            member = ctx.author
        with open('data/users.json', 'r') as f:
            users = json.load(f)
        level = users[str(member.id)]['level']
        await channel.send(f"{member.mention} your Level is {level}.")

    # LEVEL_ERROR HANDLER
    @level.error
    async def level_error(self, ctx, error):
        channel = self.client.get_channel(843501907028475924)
        if isinstance(error, commands.MemberNotFound):
            await channel.send(f'{error}')

    # UPDATE USER DATA
    async def update_data(self, users, user):
        if str(user.id) not in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['level'] = 1

    # ADD USER EXPERIENCE
    async def add_experience(self, users, user, exp):
        users[str(user.id)]['experience'] += exp

    # USER LEVEL UPDATE
    async def level_up(self, users, user):
        experience = users[str(user.id)]['experience']
        level_start = users[str(user.id)]['level']
        level_end = int(experience ** (1/4))

        if level_start < level_end:
            users[str(user.id)]['level'] = level_end
            return True
        else:
            return False


def setup(client):
    client.add_cog(Levels(client))
