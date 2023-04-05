# импортируем специальные типы телеграм бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
# импортируем настройки и утилиты
from settings import config
# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """
    # инициализация разметки

    def __init__(self):
        self.markup = None
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам
        """

        return KeyboardButton(config.KEYBOARD[name])

    def start_menu_start(self):
        """
        Создает разметку кнопок в основном меню (вопрос возраста) и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('YES')
        itm_btn_2 = self.set_btn('NO')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2)
        return self.markup
    def start_menu_finish(self):
        """
        Создает разметку кнопок в основном меню и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('MF')
        itm_btn_2 = self.set_btn('MFM')
        itm_btn_3 = self.set_btn('FFM')
        itm_btn_4 = self.set_btn('MFMF')
        itm_btn_5 = self.set_btn('INFO')
        # itm_btn_6 = self.set_btn('SEND_MESS')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3, itm_btn_4)
        self.markup.row(itm_btn_5)
        return self.markup

    def info_menu(self):
        """
        Создает разметку кнопок в меню 'О магазине'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def before_game(self):
        """
        Создает разметку кнопок в меню 'Игра'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        itm_btn_2 = self.set_btn('INFO')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2)
        return self.markup

    def start_game(self):
        """
        Создает разметку кнопок в меню 'Начать игру'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('START_GAME')
        itm_btn_2 = self.set_btn('GAME_OVER')
        # itm_btn_3 = self.set_btn('INFO')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2)
        return self.markup

    def game(self):
        """
        Создает разметку кнопок в меню 'Игра'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('>>')
        itm_btn_2 = self.set_btn('GAME_OVER')
        itm_btn_3 = self.set_btn('FOLLOWING_LEVEL')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def game_over(self):
        """
        Создает разметку кнопок в меню 'Конец игры'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('REPEAT_GAME')
        itm_btn_2 = self.set_btn('START_MENU')
        itm_btn_3 = self.set_btn('INFO')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    @staticmethod
    def remove_menu():
        """
        Удаляет меню
        """
        return ReplyKeyboardRemove()
