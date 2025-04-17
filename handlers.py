from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.inline import goal_keyboard, level_keyboard, equipment_keyboard
from data.training_plans import get_training_plan  # Предполагается, что планы хранятся здесь

# Инициализируем роутер
router = Router()

# Описываем состояния для FSM (машины состояний)
class TrainingPlan(StatesGroup):
    goal = State()
    level = State()
    equipment = State()
    show_plan = State()

# Обработчик команды /start
@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await message.answer("Привет! Я бот, который поможет тебе подобрать план тренировок. Выбери свою цель:", reply_markup=goal_keyboard)
    await state.set_state(TrainingPlan.goal)

# Обработчик выбора цели (callback)
@router.callback_query(TrainingPlan.goal)
async def process_goal(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(goal=callback.data)
    await callback.message.edit_text("Отлично! Теперь выбери свой уровень подготовки:", reply_markup=level_keyboard)
    await state.set_state(TrainingPlan.level)
    await callback.answer()

# Обработчик выбора уровня (callback)
@router.callback_query(TrainingPlan.level)
async def process_level(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(level=callback.data)
    await callback.message.edit_text("Хорошо. Теперь укажи, какое оборудование тебе доступно:", reply_markup=equipment_keyboard)
    await state.set_state(TrainingPlan.equipment)
    await callback.answer()

# Обработчик выбора оборудования (callback)
@router.callback_query(TrainingPlan.equipment)
async def process_equipment(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(equipment=callback.data)
    data = await state.get_data()
    goal = data.get('goal')
    level = data.get('level')
    equipment = data.get('equipment')
    plan = get_training_plan(goal, level, equipment)
    if plan:
        await callback.message.edit_text(f"Вот твой план тренировок:\n\n{plan}")
    else:
        await callback.message.edit_text("К сожалению, для выбранных параметров план тренировок не найден.")
    await state.finish()
    await callback.answer()

# Обработчик для некорректного ввода в любом состоянии (опционально)
@router.message()
async def incorrect_input(message: types.Message):
    await message.answer("Пожалуйста, используйте кнопки для выбора.")
