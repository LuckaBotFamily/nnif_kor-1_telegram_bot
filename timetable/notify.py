from datetime import datetime

import gspread
from aiogram import types, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from . import days_mess, days
from create_bot import bot, dp
import logger

worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1w5xOv-074pijwpOt-rN53FMs_m38ahkL0b02NfVdsJk/edit#gid=1805467367').get_worksheet(1)

async def notify_togl(message: types.Message):
    if message.get_args() == "on":
        x = 1
        if str(message.chat.id) in worksheet.col_values(2):
                text = 'Повідомлення вже увімкнені'
        else:
            while (x < 100):
                if str(worksheet.acell(f"B{x}").value) == "None":
                    worksheet.update(f"B{x}", str(message.chat.id))
                    if message.chat.id == message.from_user.id:
                        worksheet.update(f"A{x}", str(message.from_user.username))
                    else:
                        worksheet.update(f"A{x}", str("Chat"))
                    text = 'Повідомлення успішно увімкнені'
                    break
                x = x + 1
    elif message.get_args() == "off":
        worksheet.update(f"A{worksheet.find(str(message.chat.id)).row}", "None")
        worksheet.update(f"B{worksheet.find(str(message.chat.id)).row}", "None")
        text = 'Повідомлення успішно вимкнено'
    else:
        text = 'Будь ласка, введіть аргумент "on" щоб увімкнути повідомлення, або "off" щоб їх вимкнути'
    await logger.logger_mess(message)
    await bot.send_message(chat_id=message.chat.id, text=text)

async def notify(pars):
    week = datetime.date(datetime.today()).strftime("%V")
    users = ""
    for user in worksheet.col_values(2):
        if int(week) % 2 == 0:
            line = str(days_mess.getLine(day=datetime.isoweekday(datetime.today()), color=1, line=int(pars)))
        else:
            line = str(days_mess.getLine(day=datetime.isoweekday(datetime.today()), color=0, line=int(pars)))
        if line != "None":
            await bot.send_message(chat_id=user, text=f"Через 5 хвилин розпочнеться пара\n<b>{line}</b>")
            users += user + "\n"
        await logger.logger_notify(users)

async def newday():
    global newday_mess
    if datetime.weekday(datetime.today()) == 0:
        text = days_mess.day_mess("monday",  week=int(datetime.date(datetime.today()).strftime("%V")))
    if datetime.weekday(datetime.today()) == 1:
        text = days_mess.day_mess("tuesday",  week=int(datetime.date(datetime.today()).strftime("%V")))
    if datetime.weekday(datetime.today()) == 2:
        text = days_mess.day_mess("wednesday",  week=int(datetime.date(datetime.today()).strftime("%V")))
    if datetime.weekday(datetime.today()) == 3:
        text = days_mess.day_mess("thursday",  week=int(datetime.date(datetime.today()).strftime("%V")))
    if datetime.weekday(datetime.today()) == 4:
        text = days_mess.day_mess("friday",  week=int(datetime.date(datetime.today()).strftime("%V")))
    message = await bot.send_message(chat_id=-753982236, text=text)
    await bot.pin_chat_message(chat_id=-753982236, message_id=message.message_id)
    await logger.logger_newday()


scheduler = AsyncIOScheduler()
scheduler.add_job(newday, 'cron', day_of_week='mon-fri', hour='8', minute='10')
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='08', minute='15', args='1')
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='09', minute='45', args='2')
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='11', minute='30', args='3')
scheduler.add_job(notify, 'cron', day_of_week='mon-fri', hour='12', minute='55', args='4')
scheduler.start()

def register_handlers_notify(dp: Dispatcher):
    dp.register_message_handler(notify_togl, commands=['notify'])
    dp.register_message_handler(notify, commands=['notify_test'])