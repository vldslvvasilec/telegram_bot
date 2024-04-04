from datetime import datetime

import sqlite3
import telebot
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage()

token = '6027166861:AAEW9T3NrhebBK9kF3p9wIaQz7HP7o2yQhY'
bot = telebot.TeleBot(token=token)
chat_id = 12345


# class MyStates(StatesGroup): - состояния, включающиеся при вводе значений с клавиатуры:
class MyStates(StatesGroup):
    language = State()
    tool_bar = State()
    state_none = State()
    base_sal = State()
    hour_sal = State()
    premium_sal = State()
    len_holid_sal = State()
    final_tool_bar = State()
    feedback = State()
    history_start = State()
    history_final = State()
    history_answer = State()


# class DBHelper: - управление БД:
class DBHelper:
    def setup(self, setup_id, name):
        with sqlite3.connect("bot_mzda.db") as db:
            curr = db.cursor()
            stmt = """CREATE TABLE IF NOT EXISTS baza_list (
            id INT,
            name TEXT,
            lang TEXT,
            datum TEXT,
            month TEXT,
            base_sal INT,
            hour_sal INT,
            premium_sal INT,
            public_holiday INT,
            len_holid INT,
            saturday INT,
            night TEXT,
            result INT);
            CREATE TABLE IF NOT EXISTS result (
            id INT,
            name TEXT,
            lang TEXT,
            datum TEXT,
            result TEXT);
            CREATE TABLE IF NOT EXISTS feedback (
            id INT,
            name TEXT,
            lang TEXT,
            datum TEXT,
            coments TEXT)
            """
            curr.executescript(stmt)

        curr.execute(f"SELECT id FROM baza_list WHERE id = '{setup_id}'")
        if curr.fetchone() is None:
            curr.execute("INSERT INTO baza_list VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (setup_id, name, 'TEXT', 'TEXT', 'TEXT', 0, 0, 0, 0, 0, 0, 'TEXT', 0))
            db.commit()
        curr.close()
        db.close()

    def updater(self, updater_id, colum, data):
        db = sqlite3.connect('bot_mzda.db')
        curr = db.cursor()
        curr.execute("SELECT * FROM baza_list")
        curr.execute(f"UPDATE baza_list SET {colum} = '{data}' WHERE id = {updater_id}")
        db.commit()

    def select(self, select_id, colum):
        db = sqlite3.connect('bot_mzda.db')
        curr = db.cursor()
        for values in curr.execute(f"SELECT {colum} FROM baza_list WHERE id = '{select_id}'"):
            for value in values:
                return value

    def select_result(self, select_result_id, colum):
        db = sqlite3.connect('bot_mzda.db')
        curr = db.cursor()
        for values in curr.execute(f"SELECT {colum} FROM baza_list WHERE id = {select_result_id}"):
            for value in values:
                return value

    def add_result(self, add_result_id, name, date, lang, res):
        db = sqlite3.connect('bot_mzda.db')
        curr = db.cursor()
        curr.execute("SELECT * FROM result")
        curr.execute("INSERT INTO result VALUES(?, ?, ?, ?, ?)",
                     (add_result_id, name, lang, date, res))
        db.commit()

    def add_feedback(self, add_feedback_id, name, lang, feed):
        db = sqlite3.connect('bot_mzda.db')
        curr = db.cursor()
        date = datetime.now()
        curr.execute("SELECT * FROM feedback")
        curr.execute("INSERT INTO feedback VALUES(?, ?, ?, ?, ?)",
                     (add_feedback_id, name, lang, date, feed))
        db.commit()

    def select_histori(self, user_id):
        db = sqlite3.connect('bot_mzda.db')
        curr = db.cursor()
        hist_list = []
        for values in curr.execute(f"SELECT * FROM result WHERE id = {user_id}"):
            hist_list.append(values)
        return hist_list


def parsing(final_result):
    while True:
        start = time.time()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.mesec.cz/kalkulacky/vypocet-ciste-mzdy/')
        try:
            input_value = WebDriverWait(driver, 100).until(
                ec.presence_of_element_located((By.ID, "frm-maxiCalc-maxiWage-mzda")))
            input_value.send_keys(final_result)
            input_value.send_keys(Keys.RETURN)
            output_value = WebDriverWait(driver, 100).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="calcResult"]/div[1]/div[1]')))
            result_text = ''.join(map(str, ((output_value.text.split())[:-1])))
            try:
                result = int(result_text)
                return result
            except ValueError:
                print(f"Неверно полученные данные: {result_text}. Повторная потытка.")
                time.sleep(2)

            finally:
                driver.close()
                driver.quit()

        finally:
            print(time.time() - start)
