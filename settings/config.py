import os
# импортируем модуль enum для фиксирования состояния пользователя
from enum import Enum

# импортируем модуль emoji для отображения эмоджи
from emoji import emojize

# токен выдается при регистрации приложения
TOKEN = 
# название БД
NAME_DB = 'game.db'
# версия приложения
VERSION = '0.0.1'
# автор приложния
AUTHOR = 'ipi'
# Состояние пользователя
stat = None
# Текущая (выбранная) игра
CURRENT_GAME = None
# Имя первого мужчины
NAME_MAN_ONE = None
# Имя второго мужчины
NAME_MAN_TWO = None
# Имя первой женщины
NAME_WOMEN_ONE = None
# Имя второй женщины
NAME_WOMEN_TWO = None
# Текущий список вопросов
CURRENT_LIST = None
# Текущий уровень игры
CURRENT_LEVEL_GAME = None
# Счетчик вопросов каждого игрока
COUNT_QUEST = None

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///' + BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'YES': emojize('👍 мне больше 18'),
    'NO': emojize('👎 мне нет 18'),
    'MF': emojize('♂♀\n‍МЖ'),
    'MFM': emojize('♂♀♂\n‍МЖМ'),
    'FFM': emojize('♀♂♀\nЖМЖ'),
    'MFMF': emojize('♂♀♂♀\nМЖМЖ'),
    'START_GAME': emojize('Начать игру'),
    'REPEAT_GAME': emojize('Начать игру сначала'),
    'INFO': emojize(':speech_balloon: О игре'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEND_MESS': emojize('Отправить сообщение боту'),
    # 'MAN1': emojize('‍🙋 Имя первого мужчины'),
    # 'MAN2': emojize('‍🙋 Имя второго мужчины'),
    # 'WOMEN1': emojize('🙋‍♀️ Имя первой женщины'),
    # 'WOMEN2': emojize('‍🙋‍♀️ Имя второй женщины'),
    'START_MENU': emojize('Главное меню'),
    'FOLLOWING_LEVEL': emojize('Следующий уровень'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    'GAME_OVER': emojize('Закончить игру'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩ Следующий вопрос'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}


# класс для фиксирования состояния пользователя
class States(Enum):
    S_ENTER_NAME_M1 = "0"  # Ввод имени 1 мужчины
    S_ENTER_NAME_M2 = "1"  # Ввод имени 2 мужчины
    S_ENTER_NAME_W1 = "2"  # Ввод имени 1 женщины
    S_ENTER_NAME_W2 = "3"  # Ввод имени 2 женщины
