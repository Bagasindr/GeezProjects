# Ported By @VckyouuBitch
# FROM GeezProjects <https://github.com/vckyou/GeezProjects>
#


from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError
from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez
from userbot import CMD_HELP, bot


@bot.on(geezbot_cmd(outgoing=True, pattern="frog(?: |$)(.*)"))
async def honkasays(event):
    await event.edit("`Sedang Memproses, Mohon Tunggu Sebentar...`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("Beri Aku Bebeberapa Text, Contoh : `.honka space <text>`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("`Mohon Maaf, Saya Tidak Bisa Menggunakan Hal-Hal Sebaris Disini.`")
    except ChatSendStickersForbiddenError:
        await event.edit("Mohon Maaf, Tidak Bisa Mengirim Sticker Disini.")


CMD_HELP.update(
    {
        "frog": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{geez}frog` space <text>\
    \n↳ : Menampilkan Pesan (text) di Sticker Animasi."
    }
)
