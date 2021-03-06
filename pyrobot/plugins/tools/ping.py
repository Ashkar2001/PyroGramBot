"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time

from pyrogram import Client, Filters

from pyrobot import (
    COMMAND_HAND_LER,
    IS_BOT
)


# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ലാ..."
HELP = "CAADAgAD6AkAAowucAABsFGHedLEzeUWBA"
REPO = ("User / Bot is available on GitHub:\n"
        "https://github.com/SpEcHiDe/PyroGramUserBot")
# -- Constants End -- #


@Client.on_message(Filters.command("alive", COMMAND_HAND_LER))
async def check_alive(client, message):
    await message.reply_text(ALIVE)


@Client.on_message(Filters.command("help", COMMAND_HAND_LER))
async def help_me(client, message):
    await message.reply_sticker(HELP)


@Client.on_message(Filters.command("ping", COMMAND_HAND_LER))
async def ping(client, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(Filters.command("repo", COMMAND_HAND_LER))
async def repo(client, message):
    await message.reply_text(REPO)
