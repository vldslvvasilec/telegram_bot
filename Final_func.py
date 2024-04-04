import config
from config import DBHelper
from config import datetime
from telebot import types
import messages_lang

bot = config.bot


@bot.message_handler(commands=['test'])
def result(message):
    user_id = message.from_user.id
    DBHelper.updater(self=message, updater_id=user_id, colum='datum',
                     data=(datetime.now()).strftime(' %d-%m-%Y  %H:%M'))
    line_str = '---------------------------------------------------------------'
    # общая информация
    # 1 месяц:
    f_month = int((DBHelper.select_result(self=message, select_result_id=user_id, colum='month')).split('/')[1])
    # 2 Оклад:
    f_sale = int(DBHelper.select_result(self=message, select_result_id=user_id, colum='base_sal'))
    # 3 Оплата за час
    f_hour_sale = (DBHelper.select_result(self=message, select_result_id=user_id, colum='hour_sal'))

    # Импорт данных с БД:
    sale = int(DBHelper.select_result(self=message, select_result_id=user_id, colum='base_sal'))
    hour_sale = int(DBHelper.select_result(self=message, select_result_id=user_id, colum='hour_sal'))
    premium = int(DBHelper.select_result(self=message, select_result_id=user_id, colum='premium_sal'))
    len_public_1 = int((DBHelper.select_result(self=message, select_result_id=user_id, colum='month')).split('/')[3])
    len_days = int((DBHelper.select_result(self=message, select_result_id=user_id, colum='month')).split('/')[2])
    len_public = int(DBHelper.select_result(self=message, select_result_id=user_id, colum='public_holiday'))
    len_holidays = int(DBHelper.select_result(self=message, select_result_id=user_id, colum='len_holid'))
    len_saturday = int(DBHelper.select_result(self=message, select_result_id=user_id, colum='saturday'))
    len_night = (DBHelper.select_result(self=message, select_result_id=user_id, colum='night'))

    # расчетная информация
    # месяц:
    fr_month = []
    if f_month == 1:
        fr_month.append(messages_lang.month_1[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 2:
        fr_month.append(messages_lang.month_2[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 3:
        fr_month.append(messages_lang.month_3[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 4:
        fr_month.append(messages_lang.month_4[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 5:
        fr_month.append(messages_lang.month_5[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 6:
        fr_month.append(messages_lang.month_6[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 7:
        fr_month.append(messages_lang.month_7[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 8:
        fr_month.append(messages_lang.month_8[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 9:
        fr_month.append(messages_lang.month_9[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 10:
        fr_month.append(messages_lang.month_10[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 11:
        fr_month.append(messages_lang.month_11[DBHelper.select(message, user_id, 'lang')])
    elif f_month == 12:
        fr_month.append(messages_lang.month_12[DBHelper.select(message, user_id, 'lang')])
    # 4 оклад расчетный:
    fr_sale = [f"\n<b>{messages_lang.fr_sale[DBHelper.select(message, user_id, 'lang')]}</b>", 'kč']
    # 5 если был праздник:
    fr_public_holid_1 = [
        f"\n<b>{messages_lang.fr_public_holid_1[DBHelper.select(message, user_id, 'lang')]}</b>", 'kč']
    # 6 если работал праздник:
    fr_public_holid = [
        f"\n<b>{messages_lang.fr_public_holid_2[DBHelper.select(message, user_id, 'lang')]}</b>", 'kč']
    # 7 оплата за субботы:
    fr_saturday = [f"\n<b>{messages_lang.fr_saturday_1[DBHelper.select(message, user_id, 'lang')]}</b>",
                   'kč']
    # 8 доплата 10%:
    fr_pres_saturday10 = [
        f"\n<b>{messages_lang.fr_saturday_2[DBHelper.select(message, user_id, 'lang')]}</b>", 'kč']
    # 9 доплата 25%:
    fr_pres_saturday25 = [
        f"\n<b>{messages_lang.fr_saturday_3[DBHelper.select(message, user_id, 'lang')]}</b>", 'kč']
    # 10 ночные:
    fr_night = [f"\n<b>{messages_lang.fr_night[DBHelper.select(message, user_id, 'lang')]}</b>", 'kč']
    # 11 Отпуск:
    fr_holideys = [f"\n<b>{messages_lang.fr_holidays[DBHelper.select(message, user_id, 'lang')]}</b>",
                   'kč']
    # 12 Премия:
    fr_premium = [f"\n<b>{messages_lang.fr_premium[DBHelper.select(message, user_id, 'lang')]}</b>", 'kč']
    # 13 Итого грубая зп:
    fr_result = [f"<b>{messages_lang.fr_result[DBHelper.select(message, user_id, 'lang')]}</b>", 0, 'kč']
    # 14 Итого чистая зп:
    fr_result_1 = [f"\n<b>{messages_lang.fr_result_1[DBHelper.select(message, user_id, 'lang')]}</b>",
                   'kč']
    # 15 Стравенки:
    fr_food_stamps = [f"\n<b>{messages_lang.food_stamps[DBHelper.select(message, user_id, 'lang')]}</b>",
                      'kč']

    fr_result_list = [fr_sale,
                      fr_public_holid_1,
                      fr_holideys,
                      fr_public_holid,
                      fr_saturday,
                      fr_pres_saturday10,
                      fr_pres_saturday25,
                      fr_night,
                      fr_premium]

    # Основная информация текст:
    text_translate = DBHelper.select(message, user_id, 'lang')
    main_result = (f"<b><u>{messages_lang.result[text_translate]}</u></b> \n"
                   f"<b>{messages_lang.month[text_translate]}</b>{''.join(fr_month)} 2024, \n"
                   f"<b>{messages_lang.base_sale[text_translate]}</b>{f_sale}kč, \n"
                   f"<b>{messages_lang.hour[text_translate]}</b>{f_hour_sale}kč")

    # Расчетная информация:
    final_text = [f"<b><u>{messages_lang.cunt_result[DBHelper.select(message, user_id, 'lang')]}</u></b>"]

    # Праздники расчет:
    if len_public_1 > 0:
        fr_public_holid_1.insert(1, int(sale / len_days) * len_public_1)
        if len_public > 0:
            fr_public_holid.insert(1, int(hour_sale * 8 * len_public))
        else:
            fr_public_holid.insert(1, 0)
    else:
        fr_public_holid_1.insert(1, 0), fr_public_holid.insert(1, 0)

    # Отпуск расчет:
    if len_holidays > 0:
        fr_holideys.insert(1, int(len_holidays * hour_sale * 7.5))
    else:
        fr_holideys.insert(1, 0)

    # Субботы расчет:
    if len_saturday > 0:
        fr_saturday.insert(1, int(len_saturday * sale / len_days / 7.5 * 8))
        fr_pres_saturday10.insert(1, int(len_saturday * hour_sale * 8 / 10))
        fr_pres_saturday25.insert(1, int(len_saturday * hour_sale * 8 / 4))
    else:
        fr_saturday.insert(1, 0), fr_pres_saturday10.insert(1, 0), fr_pres_saturday25.insert(1, 0)
    fr_sale.insert(1, int(sale - fr_public_holid_1[1] - (len_holidays * sale / len_days)))

    # Ночные расчет:
    if len_night == 'mdn':
        fr_night.insert(1, int(hour_sale * 3.3))
    elif len_night == 'md':
        fr_night.insert(1, int(hour_sale))
    elif len_night == 'm':
        fr_night.insert(1, 0)

    # Премия расчет:
    if len_holidays == 0:
        fr_premium.insert(1, int(premium))
    else:
        fr_premium.insert(1, int(premium / len_days * (len_days - len_holidays)))

    # Стравенки расчет:
    fr_food_stamps.insert(1, int(44 * (int(len_days + len_saturday + len_public - len_public_1 - len_holidays))))

    # Добавление в финальный список (если значение не равно 0) и сумма грубой зп:
    for value in fr_result_list:
        fr_result[1] += value[1]
        if value[1] != 0:
            for i in value:
                final_text.append(i)

    # Чистая зп:
    fr_result_1.insert(1, (config.parsing(str(fr_result[1]))) + int(fr_food_stamps[1]))
    final_result = (fr_result + fr_food_stamps + fr_result_1)

    DBHelper.select_result(message, message.from_user.id, 'result')
    DBHelper.updater(message, message.from_user.id, 'result', int(fr_result[1]))

    # Добавление грубой зп, преобразование в строку и вывод финального расчетного результата:

    # Добавляем данные в result DB:
    user_name = str(message.from_user.first_name) + '/' + str(message.from_user.last_name) + '/' + str(
        message.from_user.username)
    DBHelper.add_result(message,
                        user_id,
                        user_name,
                        str(DBHelper.select(message, user_id, 'datum')),
                        str(DBHelper.select(message, user_id, 'lang')),
                        str(f"{main_result}\n{line_str}\n"
                            f"{' '.join(map(str, final_text))}\n{line_str}\n"
                            f"{' '.join(map(str, final_result))}"))

    # Вывод сообщения:
    bot.send_message(user_id, f"{main_result}\n{line_str}\n"
                                           f"{' '.join(map(str, final_text))}\n{line_str}\n"
                                           f"{' '.join(map(str, final_result))}", parse_mode='HTML')

    final_tool_bar(message)


def final_tool_bar(message):
    user_id = message.from_user.id
    bot.set_state(user_id, config.MyStates.final_tool_bar)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    final_text = f"{messages_lang.final_tool_bar[DBHelper.select(message, user_id, 'lang')]}"
    item1 = types.KeyboardButton(
        messages_lang.final_tool_bar_btn1[DBHelper.select(message, user_id, 'lang')])
    item2 = types.KeyboardButton(
        messages_lang.final_tool_bar_btn2[DBHelper.select(message, user_id, 'lang')])
    item3 = types.KeyboardButton(
        messages_lang.choice_start_but3[DBHelper.select(message, user_id, 'lang')])
    item4 = types.KeyboardButton(messages_lang.cansel[DBHelper.select(message, user_id, 'lang')])
    markup.add(item1, item2, item3, item4)
    bot.send_message(user_id, final_text, reply_markup=markup)
