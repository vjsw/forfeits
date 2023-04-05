# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Boolean, LargeBinary

from data_base.dbcore import Base


class Quest(Base):
    """
    Класс-модель для описания таблицы "Вопросы игры",
    основан на декларативном стиле SQLAlchemy
    id - №п/п
    level - уровень (число: от 1 до 3)
    accessory - Пол игрока, для которого предназначен вопрос (число: 1 - мужчина, 2 - девушка)
    name_game - Название игры, для которой этот вопрос (строка: МЖ, МЖМ, МЖЖ, МЖМЖ)
    text - текст вопроса (строка)
    image - картинка вопроса

    """
    # название таблицы
    __tablename__ = 'quest_game'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    level = Column(Integer)
    accessory = Column(Integer)
    name_game = Column(String, index=True)
    text = Column(String, index=True)
    image = Column(LargeBinary)
    is_active = Column(Boolean)

    def __init__(self, level, accessory, text, name_game, image, is_active):
        self.level = level
        self.accessory = accessory
        self.text = text
        self.name_game = name_game
        self.image = image
        self.is_active = is_active


    def __str__(self):
        return f"{self.level} {self.text} {self.accessory}"
