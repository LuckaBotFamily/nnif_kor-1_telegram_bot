from datetime import datetime
import gspread
worksheet = gspread.service_account(filename='level-slate-280111-4930953f5702.json').open_by_url('https://docs.google.com/spreadsheets/d/1w5xOv-074pijwpOt-rN53FMs_m38ahkL0b02NfVdsJk/edit#gid=1805467367').get_worksheet(0)


def day_mess(day, week):
    if int(week) % 2 == 0:
        if str(day) == "monday":
            text = "    ◀ Понеділок ▶ 🔶  \n"
            x = 3
        if str(day) == "tuesday":
            text = "    ◀ Вівторок ▶ 🔶  \n"
            x = 13
        if str(day) == "wednesday":
            text = "    ◀ Середа ▶ 🔶  \n"
            x = 23
        if str(day) == "thursday":
            text = "    ◀ Четверг ▶ 🔶  \n"
            x = 33
        if str(day) == "friday":
            text = "    ◀ П'ятниця ▶ 🔶  \n"
            x = 43
    else:
        if str(day) == "monday":
            text = "    ◀ Понеділок ▶ 🔷  \n"
            x = 4
        if str(day) == "tuesday":
            text = "    ◀ Вівторок ▶ 🔷  \n"
            x = 14
        if str(day) == "wednesday":
            text = "    ◀ Середа ▶ 🔷  \n"
            x = 24
        if str(day) == "thursday":
            text = "    ◀ Четверг ▶ 🔷  \n"
            x = 34
        if str(day) == "friday":
            text = "    ◀ П'ятниця ▶ 🔷 \n"
            x = 44
    first = str(worksheet.acell('C' + str(x) + ':F' + str(x) + '').value)
    if first != "None":
        first = f"<a href='{str(worksheet.acell('G' + str(x)).value)}'>{first}</a>"
    else:
        first = "None"
    second = str(worksheet.acell('C' + str(x + 2) + ':F' + str(x + 2) + '').value)
    if second != "None":
        second = f"<a href='{str(worksheet.acell('G' + str(x + 2)).value)}'>{second}</a>"
    else:
        second = "None"
    third = str(worksheet.acell('C' + str(x + 4) + ':F' + str(x + 4) + '').value)
    if third != "None":
        third = f"<a href='{str(worksheet.acell('G' + str(x + 4)).value)}'>{third}</a>"
    else:
        third = "None"
    fourth = str(worksheet.acell('C' + str(x + 6) + ':F' + str(x + 6) + '').value)
    if fourth != "None":
        fourth = f"<a href='{str(worksheet.acell('G' + str(x + 6)).value)}'>{fourth}</a>"
    else:
        fourth = "None"
    text += "════════════════\n"
    if first != "None":
        text += "Ⅰ.   [08.20 - 09.40] <b>" + first + "</b>\n"
        pass
    if second != "None":
        text += "Ⅱ.  [09.50 - 11.10] <b>" + second + "</b>\n"
        pass
    if third != "None":
        text += "Ⅲ. [11.30 - 12.50] <b>" + third + "</b>\n"
        pass
    if fourth != "None":
        text += "Ⅳ. [13.00 - 14.20] <b>" + fourth + "</b>\n"
        pass
    return  text

def getLine(day, color, line):
    if color == 0:
        "🔶 - четная"
        if day == 1:
            x = 4
        if day == 2:
            x = 14
        if day == 3:
            x = 24
        if day == 4:
            x = 34
        if day == 5:
            x = 44
    else:
        "🔷 - нечетная"
        if day == 1:
            x = 3
        if day == 2:
            x = 13
        if day == 3:
            x = 23
        if day == 4:
            x = 33
        if day == 5:
            x = 43
    if line == 1:
        para = str(worksheet.acell('C' + str(x) + ':F' + str(x) + '').value)
        if para != "None":
            text = f"<a href='{str(worksheet.acell('G' + str(x)).value)}'>{para}</a>"
        else:
            return "None"
    if line == 2:
        para = str(worksheet.acell('C' + str(x + 2) + ':F' + str(x + 2) + '').value)
        if para != "None":
            text = f"<a href='{str(worksheet.acell('G' + str(x + 2)).value)}'>{para}</a>"
        else:
            return "None"
    if line == 3:
        para = str(worksheet.acell('C' + str(x + 4) + ':F' + str(x + 4) + '').value)
        if para != "None":
            text = f"<a href='{str(worksheet.acell('G' + str(x + 4)).value)}'>{para}</a>"
        else:
            return "None"
    if line == 4:
        para = str(worksheet.acell('C' + str(x + 6) + ':F' + str(x + 6) + '').value)
        if para != "None":
            text = f"<a href='{str(worksheet.acell('G' + str(x + 6)).value)}'>{para}</a>"
        else:
            return "None"
    return text

def getFullDay(day):
    z = 1
    text = ""
    if day == 1:
        text += "\n\n    ◀ Понеділок ▶   \n"
    if day == 2:
        text += "\n\n    ◀ Вівторок ▶   \n"
    if day == 3:
        text += "\n\n    ◀ Середа ▶   \n"
    if day == 4:
        text += "\n\n     ◀ Четверг ▶   \n"
    if day == 5:
        text += "\n\n    ◀ П'ятниця ▶   \n"
    text += "════════════════\n"
    while (z < 5):
        up = str(getLine(day=day, color=1, line=z))
        down = str(getLine(day=day, color=0, line=z))
        if up != "None" or down != "None":
            if z == 1:
                text += "Ⅰ.   [08.20 - 09.40]\n"
            if z == 2:
                text += "Ⅱ.  [09.50 - 11.10]\n"
            if z == 3:
                text += "Ⅲ. [11.30 - 12.50]\n"
            if z == 4:
                text += "Ⅳ. [13.00 - 14.20]\n"
            if up == down:
                text += up + "\n"
            else:
                if not ("None" in up):
                    text += up + "\n"
                if not ("None" in down):
                    text += down + "\n"
        z = z + 1
    return text