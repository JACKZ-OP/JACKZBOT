from userbot import *
from userbot.utils import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "JACKZ User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

Jackz = bot.uid

PM_IMG = "https://file2linkrobot.herokuapp.com/2178086617326744/coollogo_com-17240882.gif.mp4"
pm_caption = "__**𝔧𝔞𝔠𝔨𝔷𝔟𝔬𝔱 𝔦𝔰 𝔞𝔩𝔦𝔳𝔢**__\n\n"

pm_caption += (
  

    f" -ⓜⒶⓈⓉⒺⓇ-    \n**♔〘[{DEFAULTUSER}](tg://user?id={kraken})〙♔ **\n\n"
)




pm_caption += f"👿☠jå¢kzßð†☠👿      : __**{jackzvision}**__\n"



pm_caption += "✨OUR CHANNEL✨  : [ʝօɨռ](https://t.me/jackzbot_official)\n"



pm_caption +="OUR GROUP   :[ʝօɨռ](https://t.me/jackzbot_official_chat)\n"


pm_caption += "   : \n\n"



pm_caption += "    [ʟɪɴᴋ ᴛᴏ ʙᴏᴛ]](https://github.com/jayesh-jd/JACKZBOT) 🔹 [📜License📜](https://github.com/jayesh-jd/JACKZBOT/blob/main/LICENSE)"



@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
