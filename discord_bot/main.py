# インストールした discord.py を読み込む
import asyncio

import discord

# アクセストークンを読み込み
import env
from GSpreadModel import GSpreadSheet

# インテントの設定
intents = discord.Intents.all()

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print(f"{client.user}がログインしました")
    guild = client.get_guild(967802307926442084)
    print(f"{guild.name}のメンバー数は{guild.member_count}です！")


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author == client.user:
        return
    if message.author == "くみちょ#8691":
        await message.channel.send(
            "{}\nメッセージを削除します。\n発言にはくみちょ#8691様の許可をとってください".format(message.author.mention)
        )
        await message.delete()
    else:
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content.startswith("/neko"):
            await message.channel.send("にゃーん")
        if message.content.startswith("/mention"):
            await message.add_reaction("🙈")
        if message.content.startswith("/edit name"):
            guild = client.get_guild(967802307926442084)
            await guild.edit(name="test")

        if message.content.startswith("write words"):
            channel = message.channel
            await channel.send("スプレッドシートに書きたい言葉を入力してください")

            def check(m):
                return m.channel == channel

            meg = await client.wait_for("message", check=check)
            gss = GSpreadSheet()
            sheet = await gss.getSheet()
            print(gss.credentials)
            print(gss.spreadsheet_url)
            await channel.send(await gss.write(sheet, meg.content) + "書き込み終了")


# gss.write(sheet, meg.content) +

# Botの起動とDiscordサーバーへの接続
client.run(env.BOT_TOKEN)
