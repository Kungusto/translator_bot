from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from .keyboards import languages

from .languages import languages_dict

import googletrans

class Translation(StatesGroup) :
    language = State()
    text = State()

router = Router()

LANGUAGE = 'en'

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) :
    await message.reply(f'''👋 Привет! Я — ваш персональный помощник по переводу! 🌍

Неважно, в какой части света вы находитесь, я помогу вам понять и быть понятым на любом языке! 🚀

💬 Переводите текст быстро и легко!

🌐 Поддерживаю множество языков, включая английский, русский, испанский и многие другие. Просто выберите нужный язык, а я сделаю всё остальное! 😉

Нажмите кнопку ниже, чтобы начать перевод! 👇''', reply_markup=languages)
    await state.set_state(Translation.language)

@router.message(Command('help'))
async def get_help(message: Message) :
    await message.answer('Скоро тут появится документация')
    


