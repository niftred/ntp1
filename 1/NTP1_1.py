import discord_webhook
import discord_webhook as dw
import public_ip
import psutil
import platform
import datetime


toMBnum = 1024000
WebhookURL = "https://discord.com/api/webhooks/1167869383448727764/IE8mo1irZGeLe6SiGbnpx0eGLlHeqE4ktDuXOxrlkdzFJYB2bA4eaEE2M_bVpqY5Hi0h"


class App():
    version = "1.2"
    release_date = "28.10.23"
    debug = True


msg_strokes = ["## Запуск!",
               f"IP: `{public_ip.get()}`",
               f"OS: `{platform.system()}({platform.release()})`",
               f"ОЗУ: `{psutil.virtual_memory().free/toMBnum}/{psutil.virtual_memory().total/toMBnum}`",
               f"""Date: `{datetime.date.today().strftime("%d.%m.%y")}`""",
               f"""Time: `{datetime.datetime.now().strftime("%H:%M")}`""",
               f"NTP-INF: `{App.version}_{App.release_date}`"]


def get_msg(msg_strokes_massive):
    msg = ""
    for i in range(len(msg_strokes)):
        msg = msg + msg_strokes[i] + "\n"
    if App.debug:
        msg += "\nDebug Launch"
    return str(msg)


msg = get_msg(msg_strokes)
wh = discord_webhook.DiscordWebhook(url=WebhookURL,content=msg)
wh.execute()
