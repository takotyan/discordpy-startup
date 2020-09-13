from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",
    help_command=None
)

import discord
from discord.ext import commands

class FetchUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # commands.Botインスタンスを代入

    @commands.command()
    async def fetch_user(self, target_id: int):
        try:
            target = await self.bot.fetch_user(target_id)
        except discord.NotFound:
            # ユーザーが見つからなかった場合の処理（以下は一例）
            await ctx.send("ユーザーが見つかりませんでした。")
            return

        await ctx.send(str(target)) # Username#0000


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def help(ctx):
    await ctx.send('現在作成中です。')

bot.run(token)
