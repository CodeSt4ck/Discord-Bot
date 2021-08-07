import requests
from bs4 import BeautifulSoup
from discord.ext import commands


class SearchSite(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://blog.counter-strike.net/?s='

    # SEARCH COMMAND
    @commands.command()
    async def search(self, ctx, *, message):

        no_result_message = '''Sorry, we can\'t find what you are searching for. 
        --> https://blog.counter-strike.net'''

        message_content = message.lower()
        key_words, search_words = self.key_words_search_words(message_content)
        result_links = self.search_site(key_words)
        links = self.send_link(result_links, search_words)

        if len(links) > 0:
            for link in links:
                await ctx.send(link)
        else:
            await ctx.send(no_result_message)

    # SEARCH_ERROR HANDLER
    @search.error
    async def search_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            pass

    def key_words_search_words(self, user_message):
        words = user_message.split()[1:]
        keywords = '+'.join(words)
        search_words = ' '.join(words)
        return keywords, search_words

    def search_site(self, keywords):
        response = requests.get(self.url+keywords, headers=self.headers)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        result_links = soup.findAll('a')
        return result_links

    def send_link(self, result_links, search_words):
        send_link = set()
        for link in result_links:
            text = link.text.lower()
            if search_words in text:
                send_link.add(link.get('href'))
                if len(send_link) > 20:
                    break
        return send_link


def setup(client):
    client.add_cog(SearchSite(client))
