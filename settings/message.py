# импортируем настройки для отражения эмоджи
from .config import KEYBOARD, VERSION, AUTHOR

# ответ пользователю при посещении блока "О магазине"
trading_store = """

<b>Добро пожаловать в приложение
            Игра в фанты !!!</b>

Данное приложение разработано 
специально для игр в "интересных" компаниях.

Данное приложение является НЕ комерческим и развивается 
только за счет инициативной группы. Если вам понравилось 
это приложение, то вы можете пожертвовать 
некоторое количество денежных средств на развитие проекта. 
Сбер: 22022002.......
Яндекс: ........

Все свои пожелания по доработке игры можете отправлять на адрес: 
rsa-company@yandex.ru
"""
rules_game = """

<b>ПРАВИЛА ИГРЫ !!!</b>

Вам будет предложено три уровня игры.

На первом уровне будут легкие, эротические вопросы, в основном 
"поболтать" и рассказать про свой сексуальный опыт.

На втором уровне вопросы будут намного смелее. Будут вопросы и
с поцелуями и снятие каких-то элементов одежды. В конце второго 
уровня все игроки должны быть полностью обнажены.

Третий уровень финальный. Здесь вам будут предложены вопросы открытого секса.

Вы готовы? 

Поехали...

"""
message_final = """
Вы перешли на финальный уровень. Для соблюдения правил гигиены рекомендовано принять душ.
"""
# ответ пользователю при посещении блока "Настройки"
settings = """
<b>Общее руководство приложением:</b>

<i>Навигация:</i>

-<b>({}) - </b><i>назад</i>
-<b>({}) - </b><i>вперед</i>
-<b>({}) - </b><i>увеличить</i>
-<b>({}) - </b><i>уменьшить</i>
-<b>({}) - </b><i>следующий</i>
-<b>({}) - </b><i>предыдующий</i>

<i>Специальные кнопки:</i>

-<b>({}) - </b><i>удалить</i>
-<b>({}) - </b><i>заказ</i>
-<b>({}) - </b><i>Оформить заказ</i>

<i>Общая информация:</i>

-<b>версия программы: - </b><i>({})</i>
-<b>разработчик: - </b><i>({})</i>


<b>{}Ваше имя</b>

""".format(
    KEYBOARD['<<'],
    KEYBOARD['>>'],
    KEYBOARD['UP'],
    KEYBOARD['DOUWN'],
    KEYBOARD['NEXT_STEP'],
    KEYBOARD['BACK_STEP'],
    KEYBOARD['X'],
    KEYBOARD['ORDER'],
    KEYBOARD['APPLAY'],
    VERSION,
    AUTHOR,
    KEYBOARD['COPY'],
)
# ответ пользователю при добавлении товара в заказ
product_order = """
Выбранный товар:

{}
{}
Cтоимость: {} руб

добавлен в заказ!!!

На складе осталось {} ед. 
"""
# ответ пользователю при посещении блока с заказом
order = """

<i>Название:</i> <b>{}</b>

<i>Описание:</i> <b>{}</b>

<i>Cтоимость:</i> <b>{} руб за 1 ед.</b>

<i>Количество позиций:</i> <b>{} ед.</b> 
"""

order_number = """

<b>Позиция в заказе № </b> <i>{}</i>

"""
# ответ пользователю, когда заказа нет
no_orders = """
<b>Заказ отсутствует !!!</b>
"""
# ответ пользователю при подтверждении оформления заказа
applay = """
<b>Ваш заказ оформлен !!!</b>

<i>Общая стоимость заказа составляет:</i> <b>{} руб</b>

<i>Общее количество позиций составляет:</i> <b>{} ед.</b>

<b>ЗАКАЗ НАПРАВЛЕН НА СКЛАД,
ДЛЯ ЕГО КОМПЛЕКТОВКИ !!!</b>
"""
# словарь ответов пользователю
MESSAGES = {
    'trading_store': trading_store,
    'product_order': product_order,
    'order': order,
    'order_number': order_number,
    'no_orders': no_orders,
    'applay': applay,
    'settings': settings,
    'rules_game': rules_game,
    'message_final': message_final
}
