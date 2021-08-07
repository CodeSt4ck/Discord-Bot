import discord
import os
import json
import requests
from bs4 import BeautifulSoup
from discord.ext import commands


class CSGO(commands.Cog):

    def __init__(self, client):
        self.client = client

    os.chdir(r'/Users/jangi/Desktop/Discord Bot')

    # UPDATE COMMAND
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def update(self, ctx):
        channel = self.client.get_channel(844441212006301697)

        updates_url = requests.get(
            'https://blog.counter-strike.net/index.php/category/updates/').text

        soup = BeautifulSoup(updates_url, 'lxml')

        post_link = soup.find('h2').a['href']

        info_url = requests.get(str(post_link)).text

        info_soup = BeautifulSoup(info_url, 'lxml')

        release_note = info_soup.find('h2').text

        post_date = info_soup.find(
            'p', class_='post_date').text.replace('-', '')
        post_date = 'Date : ' + post_date

        update_info = info_soup.find_all('p', class_=None)[0:-1]
        patches = ''
        for info in update_info:
            patches = patches + info.get_text()

        with open('data/updates.json', 'r') as f:
            updates = json.load(f)

        if post_link not in updates:
            updates[str(post_link)] = {}
            updates[str(post_link)]['ReleaseNotes'] = release_note
            updates[str(post_link)]['Date'] = post_date
            updates[str(post_link)]['PatchNotes'] = patches
            details = discord.Embed(
                title=str(release_note),
                description=str(post_date) + '\nPATCHNOTES',
                color=discord.Color.blue()
            )
            for info in update_info:
                details.add_field(name='--------------------------------------------------------------------------------------------------',
                                  value=str(info.get_text()), inline=False)
            await channel.send(embed=details)
        else:
            await channel.send('No new updates.')

        with open('data/updates.json', 'w') as f:
            json.dump(updates, f)

    # UPDATE_ERROR HANDLER
    @update.error
    async def update_error(self, ctx, error):
        channel = self.client.get_channel(844441212006301697)
        if isinstance(error, commands.CheckFailure):
            await channel.send("Permission denied!")


def setup(client):
    client.add_cog(CSGO(client))
