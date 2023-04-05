# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Boolean, DateTime

from data_base.dbcore import Base


class Users(Base):
    """
    Класс-модель для описания таблицы "Пользователи игры",
    основан на декларативном стиле SQLAlchemy
    id - уникальный номер
    name - имя пользователя
    id_name - id пользователя
    date - дата и время игры
    game - в какую игру играл пользователь
    is_active - активность пользователя
    """
    # название таблицы
    __tablename__ = 'users'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    id_name = Column(String, index=True)
    date = Column(DateTime)
    game = Column(String, index=True)
    is_active = Column(Boolean)

    def __init__(self, name, id_name, date, game, is_active):
        self.name = name
        self.id_name = id_name
        self.date = date
        self.game = game
        self.is_active = is_active

    def __str__(self):
        return f"{self.name} {self.id_name} {self.date} {self.game}"
