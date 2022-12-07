# Ayiin - Ubot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/AyiinUbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/AyiinUbot/blob/main/LICENSE/>.
#
# FROM AyiinUbot <https://github.com/AyiinXd/AyiinUbot>
# t.me/AyiinChat & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit
# ========================×========================

import time

from fipper import Client, __version__ as fip_ver
from fipper.types import Message
from platform import python_version

from pyAyiin import __version__, ayiin_ver
from pyAyiin import CMD_HELP, HOSTED_ON, adB
from pyAyiin.decorator import Ayiin


from . import *


@Ayiin(["alive", "yins"])
async def aliveme(client: Client, message: Message):
    chat_id = message.chat.id
    user = await client.get_me()
    output = (
        f"**Tʜᴇ [Gcast Ubot](https://t.me/itachipremium)**\n\n"
        f"**{var.ALIVE_TEXT}**\n\n"
        f"╭✠╼━━━━━━━━━━━━━━━✠╮\n"
        f"≽ **Bᴀsᴇ Oɴ :** •[{adB.name}]•\n"
        f"≽ **Oᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"≽ **Mᴏᴅᴜʟᴇs :** `{len(CMD_HELP)} Modules` \n"
        f"≽ **Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{python_version()}`\n"
        f"≽ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{fip_ver}`\n"
        f"≽ **Vᴇʀsɪᴏɴ :** `{__version__}`\n"
        f"≽ **𝖦𝖼𝖺𝗌𝗍 Vᴇʀsɪᴏɴ :** `{ayiin_ver}` [{HOSTED_ON}]\n"
        "╰✠╼━━━━━━━━━━━━━━━✠╯\n\n"
    )
    await message.delete()
    try:
        if var.ALIVE_PIC:
            endsw = (".mp4", ".gif")
            if var.ALIVE_PIC.endswith(endsw):
                await client.send_video(chat_id=chat_id, video=var.ALIVE_PIC, caption=output)
            else:
                await client.send_photo(chat_id=chat_id, photo=var.ALIVE_PIC, caption=output)
        else:
            await message.reply_text(output)
    except BaseException as xd:
        await message.reply(xd)


CMD_HELP.update(
    {"alive": (
        "alive",
        {
            "alive": "Chech Your Userbot.",
        }
    )
    }
)
