# импортируем ответ пользователю
from settings.message import MESSAGES
from settings import config
# импортируем класс-родитель
from handlers.handler import Handler
#from save_db import SaveUserData
from data_base.dbalchemy import DBManager
from models.users import Users
from datetime import datetime


class HandlerAllText(Handler):
    """
    Класс обрабатывает события нажатия на кнопки
    """

    def __init__(self, bot):
        super().__init__(bot)
        # шаг в заказе
        self.step = 0
        self.BD = DBManager()

    # Функция для сохранения информации о пользователях, играющих в фанты
    def save_current_user(self, str_game, message):
        data_user = Users(message.chat.username, message.chat.id, datetime.utcfromtimestamp(message.date), str_game,
                          None)
        self.BD = DBManager()
        self.BD._session.add(data_user)
        self.BD._session.commit()
        self.BD.close()

        # user_info = [message.chat.username, message.chat.id, message.date, "старт", None]
        # SaveUserData.save_user_bd(user_info)

    def clear_all_parameters(self):
        """
        Очистка всех глобальных переменных
        """
        config.NAME_MAN_ONE = None
        config.NAME_MAN_TWO = None
        config.NAME_WOMEN_ONE = None
        config.NAME_WOMEN_TWO = None
        config.stat = None
        config.CURRENT_GAME = None

    def pressed_btn_yes(self, message):
        """
        Обработка события нажатия на кнопку 'Yes'. А точне
        это подтверждение своего возраста
        """
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.remove_menu())
        self.bot.send_message(message.chat.id, "Выберете, в какой компании вы хотите поиграть.\nСделайте свой выбор",
                              reply_markup=self.keybords.start_menu_finish())

    def pressed_btn_no(self, message):
        """
        Обработка события нажатия на кнопку 'No'. А точне
        это НЕ подтверждение своего возраста
        """
        self.bot.send_message(message.chat.id, "Извини, дружище,\nно ты еще мал играть в такие игры!",
                              reply_markup=self.keybords.start_menu_start())

    def pressed_btn_info(self, message):
        """
        Обработка события нажатия на кнопку 'О игре'
        """
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.info_menu())

    def pressed_btn_settings(self, message):
        # В данный момент не используется
        """
        Обработка события нажатия на кнопку 'Настройки'
        """
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.settings_menu())

    def pressed_btn_back(self, message):
        """
        Обработка события нажатия на кнопку 'Назад'
        """
        config.stat = None
        self.bot.send_message(message.chat.id, "Вы вернулись назад",
                              reply_markup=self.keybords.start_menu_finish())
        self.clear_all_parameters()

    def pressed_btn_mfm(self, message):
        """
        Обработка события нажатия на кнопку 'Игра МЖМ'.
        """
        config.CURRENT_GAME = message.text
        config.stat = config.States.S_ENTER_NAME_M1
        self.bot.send_message(message.chat.id, "Отлично,\nотправьте мне сообщение с именем первого мужчины",
                              reply_markup=self.keybords.before_game())

    def pressed_btn_mf(self, message):
        """
        Обработка события нажатия на кнопку 'Игра МЖ'.
        """
        config.CURRENT_GAME = message.text
        config.stat = config.States.S_ENTER_NAME_M1
        self.bot.send_message(message.chat.id, "Отлично,\nотправьте мне сообщение с именем мужчины",
                              reply_markup=self.keybords.before_game())

    def pressed_btn_ffm(self, message):
        """
        Обработка события нажатия на кнопку 'Игра МЖЖ'.
        """
        config.CURRENT_GAME = message.text
        config.stat = config.States.S_ENTER_NAME_M1
        self.bot.send_message(message.chat.id, "Отлично,\nотправьте мне сообщение с именем мужчины",
                              reply_markup=self.keybords.before_game())

    def pressed_btn_mfmf(self, message):
        """
        Обработка события нажатия на кнопку 'Игра МЖМЖ'.
        """
        config.CURRENT_GAME = message.text
        config.stat = config.States.S_ENTER_NAME_M1
        self.bot.send_message(message.chat.id, "Отлично,\nотправьте мне сообщение с именем первого мужчины",
                              reply_markup=self.keybords.before_game())

    def pressed_btn_start_game(self, message):
        """
        Обработка события после ввода имен всех участников игры.
        """
        config.CURRENT_LEVEL_GAME = 1
        config.COUNT_QUEST = 1
        self.bot.send_message(message.chat.id, MESSAGES['rules_game'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.start_game())

    def pressed_btn_begin_game(self, message):
        """
        Обработка события нажатия на кнопку 'Начать игу'.
        """
        current_quest = self.Game.start(config.CURRENT_LEVEL_GAME)
        self.bot.send_message(message.chat.id, "<b>Уровень: " + current_quest[1] + "</b> \n",
                              parse_mode="HTML")
        self.bot.send_message(message.chat.id, "<b>" + current_quest[0] + " твой ход: </b>",
                              parse_mode="HTML")
        if not current_quest[3] == None:
            self.bot.send_photo(message.chat.id, current_quest[3])
        self.bot.send_message(message.chat.id, current_quest[2],
                              reply_markup=self.keybords.game())

    def pressed_btn_next_quest(self, message):
        """
        Обработка события нажатия на кнопку 'Следующий вопрос'.
        """
        # Проверка на окончание вопросов. Если current_quest = Игра Закончена
        current_quest = self.Game.next_quests()
        if current_quest == "Игра Закончена":
            self.bot.send_message(message.chat.id, current_quest,
                                  reply_markup=self.keybords.game_over())
        else:
            self.bot.send_message(message.chat.id, "<b>Уровень: " + current_quest[1] + "</b> \n",
                                  parse_mode="HTML")
            self.bot.send_message(message.chat.id, "<b>" + current_quest[0] + " твой ход: </b>",
                                  parse_mode="HTML")
            if not current_quest[3] == None:
                self.bot.send_photo(message.chat.id, current_quest[3])
            self.bot.send_message(message.chat.id, current_quest[2],
                                  reply_markup=self.keybords.game())
            # self.bot.send_message(message.chat.id, current_quest,
            #                       reply_markup=self.keybords.game())

    def pressed_btn_folowing_level(self, message):
        """
         Обработка события нажатия на кнопку 'Следующий уровень'.
         """
        config.CURRENT_LIST = None
        if config.CURRENT_LEVEL_GAME == 3:
            self.bot.send_message(message.chat.id, MESSAGES['message_final'],
                                  parse_mode="HTML",
                                  reply_markup=self.keybords.game())
        elif config.CURRENT_LEVEL_GAME > 3:
            self.bot.send_message(message.chat.id, "В этой игре предусмотрено только три уровня.",
                                  reply_markup=self.keybords.game())
        else:
            config.CURRENT_LEVEL_GAME = config.CURRENT_LEVEL_GAME + 1
            self.bot.send_message(message.chat.id, "Вы перешли на " + str(config.CURRENT_LEVEL_GAME) + " уровень",
                                  reply_markup=self.keybords.game())

    def handle(self):
        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # ********** меню ********** #
            if config.stat == config.States.S_ENTER_NAME_W2:
                # Обработка события ПОСЛЕ ввода имени второй женщины
                config.stat = None
                config.NAME_WOMEN_TWO = message.text
                if config.CURRENT_GAME == config.KEYBOARD['FFM']:
                    self.bot.send_message(message.chat.id, "Отлично!\nИгроки: \n" + config.NAME_MAN_ONE + "\n"
                                          + config.NAME_WOMEN_ONE + "\n" + config.NAME_WOMEN_TWO)
                else:
                    self.bot.send_message(message.chat.id, "Отлично!\nИгроки: \n" + config.NAME_MAN_ONE + "\n"
                                          + config.NAME_MAN_TWO + "\n" + config.NAME_WOMEN_ONE + "\n"
                                          + config.NAME_WOMEN_TWO)
                self.pressed_btn_start_game(message)

            if config.stat == config.States.S_ENTER_NAME_W1:
                # Обработка события ПОСЛЕ ввода имени первой женщины
                config.NAME_WOMEN_ONE = message.text
                if config.CURRENT_GAME == config.KEYBOARD['MFM']:
                    config.stat = None
                    self.bot.send_message(message.chat.id, "Отлично!\nИгроки: \n" + config.NAME_MAN_ONE + "\n"
                                          + config.NAME_MAN_TWO + "\n" + config.NAME_WOMEN_ONE)
                    self.pressed_btn_start_game(message)
                elif config.CURRENT_GAME == config.KEYBOARD['MF']:
                    config.stat = None
                    self.bot.send_message(message.chat.id, "Отлично!\nИгроки: \n" + config.NAME_MAN_ONE + "\n"
                                          + config.NAME_WOMEN_ONE)
                    self.pressed_btn_start_game(message)
                else:
                    self.bot.send_message(message.chat.id, "Отлично,\nпервую женщину зовут " +
                                          config.NAME_WOMEN_ONE + "\nТеперь отправьте мне сообщение с именем второй женщины")
                    config.stat = config.States.S_ENTER_NAME_W2

            if config.stat == config.States.S_ENTER_NAME_M2:
                # Обработка события ПОСЛЕ ввода имени второго мужчины
                config.NAME_MAN_TWO = message.text
                if config.CURRENT_GAME == config.KEYBOARD['MFM']:
                    self.bot.send_message(message.chat.id, "Отлично,\nвторого мужчину зовут " +
                                          config.NAME_MAN_TWO + "\nТеперь отправьте мне сообщение с именем женщины")
                else:
                    self.bot.send_message(message.chat.id, "Отлично,\nвторого мужчину зовут " +
                                          config.NAME_MAN_TWO + "\nТеперь отправьте мне сообщение с именем первой женщины")
                config.stat = config.States.S_ENTER_NAME_W1

            if config.stat == config.States.S_ENTER_NAME_M1:
                # Обработка события ПОСЛЕ ввода имени первого мужчины
                config.NAME_MAN_ONE = message.text
                if config.CURRENT_GAME == config.KEYBOARD['MFM'] or config.CURRENT_GAME == config.KEYBOARD['MFMF']:
                    self.bot.send_message(message.chat.id, "Отлично,\nпервого мужчину зовут " +
                                          config.NAME_MAN_ONE + "\nТеперь отправьте мне сообщение с именем второго мужчины")
                    config.stat = config.States.S_ENTER_NAME_M2

                if config.CURRENT_GAME == config.KEYBOARD['FFM']:
                    self.bot.send_message(message.chat.id, "Отлично,\nмужчину зовут " +
                                          config.NAME_MAN_ONE + "\nТеперь отправьте мне сообщение с именем первой женщины")
                    config.stat = config.States.S_ENTER_NAME_W1

                if config.CURRENT_GAME == config.KEYBOARD['MF']:
                    self.bot.send_message(message.chat.id, "Отлично,\nмужчину зовут " +
                                          config.NAME_MAN_ONE + "\nТеперь отправьте мне сообщение с именем женщины")
                    config.stat = config.States.S_ENTER_NAME_W1

            if message.text == config.KEYBOARD['YES']:
                self.save_current_user("СТАРТ", message)
                self.pressed_btn_yes(message)

            if message.text == config.KEYBOARD['NO']:
                self.pressed_btn_no(message)

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            if message.text == config.KEYBOARD['GAME_OVER']:
                self.pressed_btn_back(message)

            if message.text == config.KEYBOARD['MF']:
                self.save_current_user("МЖ", message)
                self.pressed_btn_mf(message)

            if message.text == config.KEYBOARD['MFM']:
                self.save_current_user("МЖМ", message)
                self.pressed_btn_mfm(message)

            if message.text == config.KEYBOARD['FFM']:
                self.save_current_user("МЖЖ", message)
                self.pressed_btn_ffm(message)

            if message.text == config.KEYBOARD['MFMF']:
                self.save_current_user("МЖМЖ", message)
                self.pressed_btn_mfmf(message)

            if message.text == config.KEYBOARD['START_GAME']:
                self.pressed_btn_begin_game(message)

            if message.text == config.KEYBOARD['>>']:
                self.pressed_btn_next_quest(message)

            if message.text == config.KEYBOARD['REPEAT_GAME']:
                self.pressed_btn_start_game(message)

            if message.text == config.KEYBOARD['START_MENU']:
                self.pressed_btn_back(message)

            if message.text == config.KEYBOARD['FOLLOWING_LEVEL']:
                self.pressed_btn_folowing_level(message)
