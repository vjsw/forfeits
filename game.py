# импортируем настройки и утилиты
from settings import config
# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager
import random


class Game:
    """
    Класс Game предназначен описания логики игры
    """

    # инициализация разметки

    def __init__(self):
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()

    # def set_one_quest(self, sex):
    #     """
    #     Функция работы со списком вопросов игры. Получает во входной параметр список,
    #     передает его в глобальную переменную CURRENT_LIST, возвращает первый вопрос и
    #     удаляет его из CURRENT_LIST.
    #     """
    #     # config.CURRENT_LIST = list_quest
    #     i = 0
    #     for quest in config.CURRENT_LIST:
    #         if quest.accessory == sex:
    #             config.CURRENT_LIST.pop(i)
    #             return quest.text
    #         i = i + 1
    #
    #     # text_quest = config.CURRENT_LIST[0].text
    #     # config.CURRENT_LIST.pop(0)
    #     # if not config.CURRENT_LIST:
    #     #     config.CURRENT_LEVEL_GAME = + 1
    #     # return text_quest

    def search_quest(self, sex):
        """
        Функция поиска вопросов для определенного пола из списка.
        Параметры:
            sex - 1 мужчина, 2 девушка
        Возвращает:
            Список [текст вопроса, картинку вопроса]
        """
        i = 0
        for quest in config.CURRENT_LIST:
            if quest.accessory == sex:
                config.CURRENT_LIST.pop(i)
                return [quest.text, quest.image]
            i = i + 1
        return [" извини, но для тебя вопросов в этом уровне не осталось.", None]

    def read_bd_quest(self, current_level):
        """
        Функция чтения вопросов из БД и возвращает список строк отсортированный в
        'случайном' порядке. Если результат чтения из БД пустой - Игра окончена.
        Параметры:
            current_level - уровень (число от 1 до 3)
        """
        # В переменную all_line_quest записываем результат запроса к БД с отбором по игре и уровню
        game = config.CURRENT_GAME.partition('\n')[-1]
        all_line_quest = self.BD.select_all_quests_category(game, current_level)

        #Если запрос пустой, то возвращаем "Игра Закончена"
        if not all_line_quest:
            # Нужно очищать параметры????
            return "Игра Закончена"

        # Сортируем вопросы в случайном порядке
        random.shuffle(all_line_quest)
        return all_line_quest

    def start(self, level):
        """
        Обработка события 'начало игры'.
        Параметры:
            level - уровень (число от 1 до 3)
        """
        # Получаем весь список вопросов из БД
        all_quest_level = self.read_bd_quest(level)
        # Если возвращается строка "Конец игры", то возвращаем ее для показу пользователю
        if type(all_quest_level) == str:
            return all_quest_level

        # Получаем имя пользователя
        name_user = self.set_name_user()

        # Присваеваем глобальной переменной список полученных из БД вопросов
        config.CURRENT_LIST = all_quest_level
        # Обнуляем счетчик вопросов
        config.COUNT_QUEST = 0

        # Если игрок мужчина, то ищем ему вопрос
        if name_user == config.NAME_MAN_ONE or name_user == config.NAME_MAN_TWO:
            text_quest = self.search_quest(1)

        # Если игрок женщина, то ищем ей вопрос
        if name_user == config.NAME_WOMEN_ONE or name_user == config.NAME_WOMEN_TWO:
            text_quest = self.search_quest(2)

        return [name_user, str(config.CURRENT_LEVEL_GAME), text_quest[0], text_quest[1]]

    def next_quests(self):
        """
        Обработка события 'следующий вопрос'.
        """
        # Если вопросы из списка закончились, то переходим на следующий уровень.
        if not config.CURRENT_LIST:
            config.CURRENT_LEVEL_GAME = config.CURRENT_LEVEL_GAME + 1
            return self.start(config.CURRENT_LEVEL_GAME)

        # Если всем игрокам было задано 10 вопросов, то переходим на следующий уровень.
        if config.COUNT_QUEST == 31:
            config.CURRENT_LEVEL_GAME = config.CURRENT_LEVEL_GAME + 1
            return self.start(config.CURRENT_LEVEL_GAME)

        # Определяем имя игрока
        name_user = self.set_name_user()

        # Если игрок мужчина, то ищем ему вопрос
        if name_user == config.NAME_MAN_ONE or name_user == config.NAME_MAN_TWO:
            text_quest = self.search_quest(1)
            # text_quest = config.CURRENT_LIST[0].text
            # config.CURRENT_LIST.pop(0)

        # Если игрок девушка, то ищем ей вопрос
        if name_user == config.NAME_WOMEN_ONE or name_user == config.NAME_WOMEN_TWO:
            text_quest = self.search_quest(2)
            # text_quest = config.CURRENT_LIST[0].text
            # config.CURRENT_LIST.pop(0)


        return [name_user, str(config.CURRENT_LEVEL_GAME), text_quest[0], text_quest[1]]
        # return name_user + " твой ход: Уровень " + str(config.CURRENT_LEVEL_GAME) + ": \n" + text_quest[0]

    def set_name_user(self):
        """
        Функция получения имени текущего игрока
        :return: Имя игрока (str)
        """
        # Поиск имени для игы "МЖ"
        if config.CURRENT_GAME == config.KEYBOARD['MF']:
            num_count = config.COUNT_QUEST % 2
            config.COUNT_QUEST = config.COUNT_QUEST + 1
            if num_count == 1:
                return config.NAME_MAN_ONE

            if num_count == 0:
                return config.NAME_WOMEN_ONE

        # Поиск имени для игы "МЖМ"
        if config.CURRENT_GAME == config.KEYBOARD['MFM']:
            num_count = config.COUNT_QUEST % 3
            config.COUNT_QUEST = config.COUNT_QUEST + 1
            if num_count == 1:
                return config.NAME_MAN_ONE

            if num_count == 2:
                return config.NAME_WOMEN_ONE

            if num_count == 0:
                return config.NAME_MAN_TWO

        # Поиск имени для игы "МЖЖ"
        if config.CURRENT_GAME == config.KEYBOARD['FFM']:
            num_count = config.COUNT_QUEST % 3
            config.COUNT_QUEST = config.COUNT_QUEST + 1
            if num_count == 1:
                return config.NAME_WOMEN_ONE

            if num_count == 2:
                return config.NAME_MAN_ONE

            if num_count == 0:
                return config.NAME_WOMEN_TWO

        # Поиск имени для игы "МЖМЖ"
        if config.CURRENT_GAME == config.KEYBOARD['MFMF']:
            num_count = config.COUNT_QUEST % 4
            config.COUNT_QUEST = config.COUNT_QUEST + 1
            if num_count == 1:
                return config.NAME_MAN_ONE

            if num_count == 2:
                return config.NAME_WOMEN_ONE

            if num_count == 3:
                return config.NAME_MAN_TWO

            if num_count == 0:
                return config.NAME_WOMEN_TWO
