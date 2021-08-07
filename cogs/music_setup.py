import discord
import youtube_dl
import os
from discord.ext import commands


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    # CONNECT COMMAND

    @commands.command()
    async def connect(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    # CONNECT_ERROR HANDLER

    @connect.error
    async def connect_error(self, ctx, error):
        channel = self.client.get_channel(842291869265559552)
        if isinstance(error, commands.CommandInvokeError):
            await channel.send("Join the voice channel first.")

    # DISCONNECT COMMAND

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
        await self.client.change_presence(activity=None)

    # DISCONNECT_ERROR HANDLER

    @disconnect.error
    async def disconnect_error(self, ctx, error):
        channel = self.client.get_channel(842291869265559552)
        if isinstance(error, commands.CommandInvokeError):
            await channel.send("Bot is already disconnected.")

    # PLAY COMMAND

    @commands.command()
    async def play(self, ctx, url: str):
        channel = ctx.author.voice.channel
        await channel.connect()
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Song already playing! or use the 'stop' command.")
            return

        voice = ctx.voice_client

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))

        activity = discord.Activity(
            name="Music",
            type=discord.ActivityType.playing,
            state="Listening",
            details="Listening"
        )

        await self.client.change_presence(activity=activity)

    # PLAY_ERROR HANDLER

    @play.error
    async def play_error(self, ctx, error):
        channel = self.client.get_channel(842291869265559552)
        if isinstance(error, commands.CommandInvokeError):
            await channel.send("You must join the channel or song is already playing.")

    # PAUSE COMMAND

    @commands.command()
    async def pause(self, ctx):
        channel = self.client.get_channel(842291869265559552)
        voice = ctx.voice_client
        if voice.is_playing():
            voice.pause()
            msg = await channel.send("Paused")
            await msg.add_reaction("⏸️")
        else:
            await channel.send("Song already playing.")

    # PAUSE_ERROR HANDLER

    @pause.error
    async def pause_error(self, ctx, error):
        channel = self.client.get_channel(842291869265559552)
        if isinstance(error, commands.CommandInvokeError):
            await channel.send("Bot must join the channel.")

    # RESUME COMMAND

    @commands.command()
    async def resume(self, ctx):
        channel = self.client.get_channel(842291869265559552)
        voice = ctx.voice_client
        if voice.is_paused():
            voice.resume()
            msg = await channel.send("Resumed")
            await msg.add_reaction("⏯️")
        else:
            await channel.send("Song already playing.")

    # RESUME_ERROR HANDLER

    @resume.error
    async def resume_error(self, ctx, error):
        channel = self.client.get_channel(842291869265559552)
        if isinstance(error, commands.CommandInvokeError):
            await channel.send("Bot must join the channel.")

    # STOP COMMAND

    @commands.command()
    async def stop(self, ctx):
        channel = self.client.get_channel(842291869265559552)
        voice = ctx.voice_client
        voice.stop()
        msg = await channel.send("Stopped")
        await msg.add_reaction("🛑")

    # STOP_ERROR HANDLER

    @stop.error
    async def stop_error(self, ctx, error):
        channel = self.client.get_channel(842291869265559552)
        if isinstance(error, commands.CommandInvokeError):
            await channel.send("Bot must join the channel.")


def setup(client):
    client.add_cog(Music(client))
