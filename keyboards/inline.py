from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

goal_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Набор мышечной массы", callback_data="muscle_gain")],
    [InlineKeyboardButton(text="Сжигание жира", callback_data="fat_loss")],
    [InlineKeyboardButton(text="Увеличение выносливости", callback_data="endurance")]
])

level_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новичок", callback_data="beginner")],
    [InlineKeyboardButton(text="Средний", callback_data="intermediate")],
    [InlineKeyboardButton(text="Продвинутый", callback_data="advanced")]
])

equipment_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Гантели", callback_data="dumbbells")],
    [InlineKeyboardButton(text="Турник и брусья", callback_data="pullups_dips")],
    [InlineKeyboardButton(text="Без оборудования", callback_data="no_equipment")]
])
