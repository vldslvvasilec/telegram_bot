from telebot import types, custom_filters
import config
from config import DBHelper, datetime, time
import Final_func
import messages_lang

bot = config.bot


@bot.message_handler(commands=['start'])
def start_language(message):
    bot.set_state(message.chat.id, config.MyStates.language)
    user_name = str(message.from_user.first_name) + '/' + str(message.from_user.last_name) + '/' + str(
        message.from_user.username)
    DBHelper.setup(message, message.from_user.id, user_name)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lang_text = messages_lang.choose_lang[DBHelper.select(message, message.from_user.id, 'lang')]
    item1 = types.KeyboardButton('🇺🇦 Українська')
    item2 = types.KeyboardButton('🇨🇿 Čeština')
    item3 = types.KeyboardButton('🇷🇺 Русский')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, lang_text.format(message.from_user), reply_markup=markup)


def start_tool_bar(message):
    bot.set_state(message.chat.id, config.MyStates.tool_bar)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_text_lang_child = messages_lang.start_text[DBHelper.select(message, message.from_user.id, 'lang')]
    start_text = f"{message.from_user.first_name}, {start_text_lang_child}"
    item1 = types.KeyboardButton(
        messages_lang.choice_start_but1[DBHelper.select(message, message.from_user.id, 'lang')])
    item2 = types.KeyboardButton(
        messages_lang.choice_start_but2[DBHelper.select(message, message.from_user.id, 'lang')])
    item3 = types.KeyboardButton(
        messages_lang.choice_start_but3[DBHelper.select(message, message.from_user.id, 'lang')])
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, start_text.format(message.from_user), reply_markup=markup)


def hist_tool_bar(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(messages_lang.main_menu[DBHelper.select(message, message.from_user.id, 'lang')])
    item2 = types.KeyboardButton(
        messages_lang.choice_start_but2[DBHelper.select(message, message.from_user.id, 'lang')])
    markup.add(item1, item2)
    bot.send_message(message.from_user.id,
                     f"{messages_lang.fill_data[DBHelper.select(message, message.from_user.id, 'lang')]}",
                     reply_markup=markup)

    hist_markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(messages_lang.last_sett[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='history/last')
    btn2 = types.InlineKeyboardButton(
        messages_lang.last_calculate[DBHelper.select(message, message.from_user.id, 'lang')],
        callback_data='history/5')
    hist_markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     messages_lang.select_story[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=hist_markup)


def feedback_func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Главное меню:
    item1 = types.KeyboardButton(messages_lang.main_menu[DBHelper.select(message, message.from_user.id, 'lang')])
    # Назад:
    item2 = types.KeyboardButton(
        messages_lang.choice_start_but2[DBHelper.select(message, message.from_user.id, 'lang')])
    markup.add(item1, item2)
    bot.send_message(message.from_user.id,
                     f"{messages_lang.feedback_1[DBHelper.select(message, message.from_user.id, 'lang')]}",
                     reply_markup=markup)


def month(message):
    month_text = f"{messages_lang.month_text[DBHelper.select(message, message.from_user.id, 'lang')]}"
    markup_month = types.InlineKeyboardMarkup(row_width=3)
    but1 = types.InlineKeyboardButton(
        f"{messages_lang.January[DBHelper.select(message, message.from_user.id, 'lang')]}",
        callback_data='month/1/23/1/4')
    but2 = types.InlineKeyboardButton(
        f"{messages_lang.February[DBHelper.select(message, message.from_user.id, 'lang')]}",
        callback_data='month/2/21/0/4')
    but3 = types.InlineKeyboardButton(f"{messages_lang.March[DBHelper.select(message, message.from_user.id, 'lang')]}",
                                      callback_data='month/3/21/1/5')
    but4 = types.InlineKeyboardButton(f"{messages_lang.April[DBHelper.select(message, message.from_user.id, 'lang')]}",
                                      callback_data='month/4/22/1/4')
    but5 = types.InlineKeyboardButton(f"{messages_lang.May[DBHelper.select(message, message.from_user.id, 'lang')]}",
                                      callback_data='month/5/23/2/4')
    but6 = types.InlineKeyboardButton(f"{messages_lang.June[DBHelper.select(message, message.from_user.id, 'lang')]}",
                                      callback_data='month/6/20/0/5')
    but7 = types.InlineKeyboardButton(f"{messages_lang.July[DBHelper.select(message, message.from_user.id, 'lang')]}",
                                      callback_data='month/7/23/1/4')
    but8 = types.InlineKeyboardButton(f"{messages_lang.August[DBHelper.select(message, message.from_user.id, 'lang')]}",
                                      callback_data='month/8/22/0/5')
    but9 = types.InlineKeyboardButton(
        f"{messages_lang.September[DBHelper.select(message, message.from_user.id, 'lang')]}",
        callback_data='month/9/21/0/4')
    but10 = types.InlineKeyboardButton(
        f"{messages_lang.October[DBHelper.select(message, message.from_user.id, 'lang')]}",
        callback_data='month/10/23/1/4')
    but11 = types.InlineKeyboardButton(
        f"{messages_lang.November[DBHelper.select(message, message.from_user.id, 'lang')]}",
        callback_data='month/11/21/0/5')
    but12 = types.InlineKeyboardButton(
        f"{messages_lang.December[DBHelper.select(message, message.from_user.id, 'lang')]}",
        callback_data='month/12/22/3/4')
    markup_month.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10, but11, but12)
    bot.send_message(chat_id=message.from_user.id, text=month_text, reply_markup=markup_month)


def base_salary(message):
    markup_salary = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('25500 kč', callback_data='salary/25500')
    btn2 = types.InlineKeyboardButton('28000 kč', callback_data='salary/28000')
    btn3 = types.InlineKeyboardButton('30200 kč', callback_data='salary/30200')
    btn4 = types.InlineKeyboardButton(messages_lang.other_var[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='salary_you_var')
    markup_salary.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id,
                     messages_lang.base_sale[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=markup_salary)


def hour_sale(message):
    bot.set_state(message.chat.id, config.MyStates.hour_sal)
    bot.send_message(message.chat.id, messages_lang.hour_sale[DBHelper.select(message, message.from_user.id, 'lang')])


def premium(message):
    markup_premium = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('6500 kč', callback_data='premium/6500')
    btn2 = types.InlineKeyboardButton(messages_lang.other_var[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='premium_you_var')
    markup_premium.add(btn1, btn2)
    bot.send_message(message.from_user.id,
                     messages_lang.premium[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=markup_premium)


def public_holiday_ques(message):
    markup_public_holiday_ques = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(messages_lang.yes[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='public_holiday_ques/yes')
    btn2 = types.InlineKeyboardButton(messages_lang.no[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='public_holiday_ques/no')
    markup_public_holiday_ques.add(btn1, btn2)
    bot.send_message(message.from_user.id,
                     messages_lang.public_hol_1[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=markup_public_holiday_ques)


def public_holiday(message):
    markup_public_holiday = types.InlineKeyboardMarkup()
    quantity = int((DBHelper.select(message, message.from_user.id, 'month')).split('/')[3])
    for btn in range(quantity):
        markup_public_holiday.add(types.InlineKeyboardButton(f'{btn + 1}', callback_data=f'public_holid/{btn + 1}'))
    bot.send_message(message.from_user.id,
                     messages_lang.public_hol_2[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=markup_public_holiday)


def holid_hospit(message):
    markup_salary1 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(messages_lang.yes[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='holid_hospit/yes')
    btn2 = types.InlineKeyboardButton(messages_lang.no[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='holid_hospit/no')
    markup_salary1.add(btn1, btn2)
    bot.send_message(message.from_user.id,
                     messages_lang.holid_hospit_1[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=markup_salary1)


def holidays(message):
    markup_holidays = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(messages_lang.holidays[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='holidays/holid')
    btn2 = types.InlineKeyboardButton(messages_lang.hospit_1[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='holidays/hospit')
    markup_holidays.add(btn1, btn2)
    bot.send_message(message.from_user.id,
                     messages_lang.holid_hospit_2[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=markup_holidays)


def len_holidays(message):
    bot.set_state(config.MyStates.len_holid_sal)
    bot.send_message(message.from_user.id,
                     messages_lang.len_holid[DBHelper.select(message, message.from_user.id, 'lang')])


def hospitals(message):
    bot.send_message(message.from_user.id,
                     messages_lang.hospit_2[DBHelper.select(message, message.from_user.id, 'lang')])
    return holidays(message)


def saturday_ques(message):
    markup_saturday_ques_ques = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(messages_lang.yes[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='saturday_ques/yes')
    btn2 = types.InlineKeyboardButton(messages_lang.no[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='saturday_ques/no')
    markup_saturday_ques_ques.add(btn1, btn2)
    bot.send_message(message.from_user.id,
                     messages_lang.saturday_1[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=markup_saturday_ques_ques)


def saturday(message):
    markup_saturday = types.InlineKeyboardMarkup()
    quantity = int((DBHelper.select(message, message.from_user.id, 'month')).split('/')[4])
    for btn in range(quantity):
        markup_saturday.add(types.InlineKeyboardButton(f'{btn + 1}', callback_data=f'saturday/{btn + 1}'))
    bot.send_message(message.from_user.id,
                     messages_lang.saturday_2[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=markup_saturday)


def night(message):
    markup_night = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(messages_lang.night_2[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='night/mdn')
    btn2 = types.InlineKeyboardButton(messages_lang.night_3[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='night/md')
    btn3 = types.InlineKeyboardButton(messages_lang.night_4[DBHelper.select(message, message.from_user.id, 'lang')],
                                      callback_data='night/m')
    markup_night.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,
                     messages_lang.night_1[DBHelper.select(message, message.from_user.id, 'lang')],
                     reply_markup=markup_night)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'bot_starting':
            month(call)

        if call.data.split('/')[0] == 'month':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='month', data=call.data)
            base_salary(call)

        if call.data.split('/')[0] == 'salary':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='base_sal', data=int(call.data.split('/')[1]))
            bot.set_state(call.message.chat.id, config.MyStates.hour_sal)
            bot.send_message(call.message.chat.id,
                             messages_lang.hour_sale[DBHelper.select(call, call.from_user.id, 'lang')])
        elif call.data == 'salary_you_var':
            bot.set_state(call.message.chat.id, config.MyStates.base_sal)
            bot.send_message(call.message.chat.id,
                             messages_lang.sale_you[DBHelper.select(call, call.from_user.id, 'lang')])

        if call.data.split('/')[0] == 'premium':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='premium_sal', data=int(call.data.split('/')[1]))
            DBHelper.select(call, call.from_user.id, 'month')
            if int((DBHelper.select(call, call.from_user.id, 'month')).split('/')[3]) == 0:
                DBHelper.updater(self=call, updater_id=call.from_user.id, colum='public_holiday', data=int('0'))
                holid_hospit(call)
            else:
                public_holiday_ques(call)

        elif call.data == 'premium_you_var':
            bot.set_state(call.message.chat.id, config.MyStates.premium_sal)
            bot.send_message(call.message.chat.id,
                             messages_lang.premium_you[DBHelper.select(call, call.from_user.id, 'lang')])

        if call.data == 'public_holiday_ques/yes':
            public_holiday(call)
        elif call.data == 'public_holiday_ques/no':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='public_holiday', data=int('0'))
            holid_hospit(call)

        if call.data.split('/')[0] == 'public_holid':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='public_holiday', data=int(call.data.split('/')[1]))
            holid_hospit(call)

        if call.data == 'holid_hospit/yes':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='len_holid', data=int('0'))
            saturday_ques(call)
        elif call.data == 'holid_hospit/no':
            holidays(call)

        if call.data == 'holidays/holid':
            bot.set_state(call.message.chat.id, config.MyStates.len_holid_sal)
            bot.send_message(call.message.chat.id,
                             messages_lang.len_holid_err[DBHelper.select(call, call.from_user.id, 'lang')])
        elif call.data == 'holidays/hospit':
            hospitals(call)

        if call.data == 'saturday_ques/yes':
            saturday(call)
        elif call.data == 'saturday_ques/no':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='saturday', data=int('0'))
            night(call)

        if call.data.split('/')[0] == 'saturday':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='saturday', data=int(call.data.split('/')[1]))
            night(call)

        if call.data == 'night/mdn':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='night', data=(call.data.split('/')[1]))
            bot.send_message(call.message.chat.id,
                             messages_lang.calculated[DBHelper.select(call, call.from_user.id, 'lang')])
            Final_func.result(call)
        elif call.data == 'night/md':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='night', data=(call.data.split('/')[1]))
            bot.send_message(call.message.chat.id,
                             messages_lang.calculated[DBHelper.select(call, call.from_user.id, 'lang')])
            Final_func.result(call)
        elif call.data == 'night/m':
            DBHelper.updater(self=call, updater_id=call.from_user.id, colum='night', data=(call.data.split('/')[1]))
            bot.send_message(call.message.chat.id,
                             messages_lang.calculated[DBHelper.select(call, call.from_user.id, 'lang')])
            Final_func.result(call)

        if call.data == 'history/5':
            txt_lng = messages_lang.last_calculate[DBHelper.select(call.message.chat.id, call.from_user.id, 'lang')]
            text = f"<b><u>{txt_lng}</u></b>"
            date_text = f"<b>{messages_lang.date[DBHelper.select(call.message.chat.id, call.from_user.id, 'lang')]}</b>"
            result = (config.DBHelper.select_histori(call.message.chat.id, call.message.chat.id))[-5:]
            bot.send_message(call.message.chat.id, f"{text}", parse_mode='HTML')
            for value in result:
                bot.send_message(call.message.chat.id, f"{date_text}{value[3]}\n{value[-1]}", parse_mode='HTML')
        elif call.data == 'history/last':
            txt_lng = messages_lang.last_sett[DBHelper.select(call.message.chat.id, call.from_user.id, 'lang')]
            text = f"<b><u>{txt_lng}</u></b>"
            date_text = f"<b>{messages_lang.date[DBHelper.select(call.message.chat.id, call.from_user.id, 'lang')]}</b>"
            date = ((config.DBHelper.select_histori(call.message.chat.id, call.message.chat.id))[-1])[3]
            result = ((config.DBHelper.select_histori(call.message.chat.id, call.message.chat.id))[-1])[-1]
            bot.send_message(call.message.chat.id, f"{text}\n{date_text}{date}\n{result}", parse_mode='HTML')


@bot.message_handler(state=config.MyStates.language)
def user_lang(message):
    if message.chat.type == "private":
        if message.text == '🇺🇦 Українська':
            DBHelper.select(message, message.from_user.id, 'lang')
            DBHelper.updater(message, message.from_user.id, 'lang', 'UA')
            start_tool_bar(message)
        elif message.text == '🇨🇿 Čeština':
            DBHelper.select(message, message.from_user.id, 'lang')
            DBHelper.updater(message, message.from_user.id, 'lang', 'CZ')
            start_tool_bar(message)
        elif message.text == '🇷🇺 Русский':
            DBHelper.select(message, message.from_user.id, 'lang')
            DBHelper.updater(message, message.from_user.id, 'lang', 'RU')
            start_tool_bar(message)
        else:
            bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(state=config.MyStates.tool_bar)
def setting_tool_bar(message):
    # Продолжить:
    if message.text == f"{messages_lang.choice_start_but1[DBHelper.select(message, message.from_user.id, 'lang')]}":
        bot.set_state(message.chat.id, config.MyStates.state_none)
        bot.send_message(message.from_user.id,
                         f"{messages_lang.fill_data[DBHelper.select(message, message.from_user.id, 'lang')]}",
                         reply_markup=types.ReplyKeyboardRemove())
        month(message)
    # Назад к выбору языка:
    elif message.text == f"{messages_lang.choice_start_but2[DBHelper.select(message, message.from_user.id, 'lang')]}":
        bot.set_state(message.chat.id, config.MyStates.language)
        start_language(message)
    # История:
    elif message.text == f"{messages_lang.choice_start_but3[DBHelper.select(message, message.from_user.id, 'lang')]}":
        bot.set_state(message.chat.id, config.MyStates.history_start)
        hist_tool_bar(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(state=config.MyStates.history_start)
def history_start(message):
    if message.text == messages_lang.main_menu[DBHelper.select(message, message.from_user.id, 'lang')]:
        bot.set_state(message.chat.id, config.MyStates.language)
        start_language(message)
    elif message.text == messages_lang.choice_start_but2[DBHelper.select(message, message.from_user.id, 'lang')]:
        bot.set_state(message.chat.id, config.MyStates.tool_bar)
        start_tool_bar(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        pass


@bot.message_handler(state=config.MyStates.history_final)
def history_final(message):
    if message.text == messages_lang.choice_start_but2[DBHelper.select(message, message.from_user.id, 'lang')]:
        bot.set_state(message.from_user.id, config.MyStates.final_tool_bar)
        Final_func.final_tool_bar(message)
    elif message.text == messages_lang.main_menu[DBHelper.select(message, message.from_user.id, 'lang')]:
        bot.set_state(message.chat.id, config.MyStates.language)
        start_language(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        pass


@bot.message_handler(state=config.MyStates.final_tool_bar)
def setting_final_tool_bar(message):
    if message.text == f"{messages_lang.final_tool_bar_btn1[DBHelper.select(message, message.from_user.id, 'lang')]}":
        bot.set_state(message.chat.id, config.MyStates.state_none)
        bot.send_message(message.from_user.id,
                         f"{messages_lang.fill_data[DBHelper.select(message, message.from_user.id, 'lang')]}",
                         reply_markup=types.ReplyKeyboardRemove())
        month(message)
    elif message.text == f"{messages_lang.final_tool_bar_btn2[DBHelper.select(message, message.from_user.id, 'lang')]}":
        bot.set_state(message.chat.id, config.MyStates.feedback)
        feedback_func(message)

    elif message.text == f"{messages_lang.choice_start_but3[DBHelper.select(message, message.from_user.id, 'lang')]}":
        bot.set_state(message.chat.id, config.MyStates.history_final)
        hist_tool_bar(message)
    elif message.text == f"{messages_lang.cansel[DBHelper.select(message, message.from_user.id, 'lang')]}":
        bot.set_state(message.chat.id, config.MyStates.language)
        start_language(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(state=config.MyStates.state_none)
def state_non(message):
    bot.delete_message(message.chat.id, message.message_id)
    pass


@bot.message_handler(state=config.MyStates.base_sal)
def base_salary_you_var(message):
    try:
        base_sal_you = float(message.text.strip().replace(',', '.'))
        DBHelper.updater(self=message, updater_id=message.from_user.id, colum='base_sal', data=base_sal_you)
    except ValueError:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id,
                         messages_lang.error_value[DBHelper.select(message, message.from_user.id, 'lang')])
        return
    if base_sal_you > 0:
        bot.set_state(message.chat.id, config.MyStates.state_none)
        hour_sale(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.from_user.id,
                         messages_lang.error_value[DBHelper.select(message, message.from_user.id, 'lang')])
        bot.register_next_step_handler(message, base_salary_you_var)


@bot.message_handler(state=config.MyStates.hour_sal)
def hour_sale_you_var(message):
    try:
        data_hour_sal = float(message.text.strip().replace(',', '.'))
        DBHelper.updater(self=message, updater_id=message.from_user.id, colum='hour_sal', data=data_hour_sal)
    except ValueError:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id,
                         messages_lang.error_value[DBHelper.select(message, message.from_user.id, 'lang')])
        return
    if data_hour_sal > 0:
        bot.set_state(message.chat.id, config.MyStates.state_none)
        premium(message)

    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.from_user.id,
                         messages_lang.error_value[DBHelper.select(message, message.from_user.id, 'lang')])
        bot.register_next_step_handler(message, hour_sale_you_var)


@bot.message_handler(state=config.MyStates.premium_sal)
def premium_you_var(message):
    try:
        data_premium_sal = float(message.text.strip().replace(',', '.'))
        DBHelper.updater(self=message, updater_id=message.from_user.id, colum='premium_sal', data=data_premium_sal)
    except ValueError:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id,
                         messages_lang.error_value[DBHelper.select(message, message.from_user.id, 'lang')])
        return
    if data_premium_sal >= 0:
        bot.set_state(message.chat.id, config.MyStates.state_none)
        if int((DBHelper.select(message, message.from_user.id, 'month')).split('/')[3]) == 0:
            DBHelper.updater(self=message, updater_id=message.from_user.id, colum='public_holiday', data=int('0'))
            holid_hospit(message)
        else:
            public_holiday_ques(message)

    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.from_user.id,
                         messages_lang.error_value[DBHelper.select(message, message.from_user.id, 'lang')])
        bot.register_next_step_handler(message, premium_you_var)


@bot.message_handler(state=config.MyStates.len_holid_sal)
def len_holid_sale(message):
    try:
        len_holid_sal = float(message.text.strip().replace(',', '.'))
        if 0 <= len_holid_sal <= int(DBHelper.select(message, message.from_user.id, 'month').split('/')[2]):
            DBHelper.updater(self=message, updater_id=message.from_user.id, colum='len_holid', data=len_holid_sal)
    except ValueError:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id,
                         messages_lang.error_value_holid[DBHelper.select(message, message.from_user.id, 'lang')])
        return
    DBHelper.select(message, message.from_user.id, 'month')
    if 0 <= len_holid_sal <= int(DBHelper.select(message, message.from_user.id, 'month').split('/')[2]):
        bot.set_state(message.chat.id, config.MyStates.state_none)
        saturday_ques(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.set_state(message.chat.id, config.MyStates.state_none)
        bot.send_message(message.from_user.id,
                         messages_lang.error_value_holid[DBHelper.select(message, message.from_user.id, 'lang')])
        bot.register_next_step_handler(message, len_holid_sale)


@bot.message_handler(state=config.MyStates.feedback)
def feedback(message):
    if message.text == messages_lang.main_menu[DBHelper.select(message, message.from_user.id, 'lang')]:
        bot.set_state(message.chat.id, config.MyStates.language)
        start_language(message)
    elif message.text == messages_lang.choice_start_but2[DBHelper.select(message, message.from_user.id, 'lang')]:
        bot.set_state(message.from_user.id, config.MyStates.final_tool_bar)
        Final_func.final_tool_bar(message)
    else:
        feed_mess = message.text
        bot.send_message(message.chat.id,
                         messages_lang.feedback_2[DBHelper.select(message, message.from_user.id, 'lang')])
        user_name = str(message.from_user.first_name) + '/' + str(message.from_user.last_name) + '/' + str(
            message.from_user.username)
        DBHelper.add_feedback(message, message.from_user.id, user_name,
                              str(DBHelper.select(message, message.from_user.id, 'lang')),
                              feed_mess)
        bot.set_state(message.from_user.id, config.MyStates.final_tool_bar)
        Final_func.final_tool_bar(message)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        pass
        print(f"error: {datetime.now()}")
        time.sleep(25)
