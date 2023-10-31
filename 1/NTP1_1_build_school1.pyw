import discord_webhook
import discord_webhook as dw
import public_ip
import psutil
import platform
import datetime


toMBnum = 1024000
WebhookURL = "https://discord.com/api/webhooks/1167869383448727764/IE8mo1irZGeLe6SiGbnpx0eGLlHeqE4ktDuXOxrlkdzFJYB2bA4eaEE2M_bVpqY5Hi0h"


class App():
    version = "1.4.1"
    release_date = "31.10.23"
    build = "school-1"
    debug = False


msg_strokes = ["## Запуск!",
               f"IP: `{public_ip.get()}`",
               f"ОС: `{platform.system()}({platform.release()})`",
               f"ОЗУ: `{int(psutil.virtual_memory().free/toMBnum)}/{int(psutil.virtual_memory().total/toMBnum)}`",
               f"""Дата: `{datetime.date.today().strftime("%d.%m.%y")}`""",
               f"""Время: `{datetime.datetime.now().strftime("%H:%M")}`""",
               f"NTP-INF: ||`NTP1_1_v{App.version}_b-{App.build}-{App.release_date}`||"]


def get_msg(msg_strokes_massive):
    msg = ""
    for i in range(len(msg_strokes)):
        msg = msg + msg_strokes[i] + "\n"
    if App.debug:
        msg += "\n*Тестовый запуск*"
    return str(msg)


msg = get_msg(msg_strokes)
wh = discord_webhook.DiscordWebhook(url=WebhookURL,content=msg)
wh.execute()
