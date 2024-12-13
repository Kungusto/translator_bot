from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from .translation import translate

from .keyboards import languages

from .languages import languages_dict

class Translation(StatesGroup) :
    language = State()
    text = State()

router = Router()

LANGUAGE = 'en'

@router.message(CommandStart())
async def cmd_start(message: Message) :
    await message.reply(f'''👋 Привет! Я — ваш персональный помощник по переводу! 🌍

Неважно, в какой части света вы находитесь, я помогу вам понять и быть понятым на любом языке! 🚀

💬 Переводите текст быстро и легко!

🌐 Поддерживаю множество языков, включая английский, русский, испанский и многие другие. Просто выберите нужный язык, а я сделаю всё остальное! 😉

Для более подробной информации введите /help

Нажмите кнопку ниже, чтобы начать перевод! 👇''', reply_markup=languages)

@router.message(Command('help'))
async def get_help(message: Message) :
    await message.answer('/help - помощь\n/change_language - сменить язык')
    
@router.message(Command('change_language'))
async def ch_lg(message: Message) :
    await message.answer('Выберите нужный вам язык', reply_markup=languages)
    
# Выбор языка    

@router.callback_query(F.data == 'en')
async def get_en(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'en'
    await callback.message.answer('You have selected English 🇬🇧')

@router.callback_query(F.data == 'ru')
async def get_ru(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'ru'
    await callback.message.answer('Вы выбрали русский 🇷🇺')

@router.callback_query(F.data == 'es')
async def get_es(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'es'
    await callback.message.answer('Has seleccionado español 🇪🇸')

@router.callback_query(F.data == 'fr')
async def get_fr(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'fr'
    await callback.message.answer('Vous avez sélectionné le français 🇫🇷')

@router.callback_query(F.data == 'de')
async def get_de(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'de'
    await callback.message.answer('Sie haben Deutsch ausgewählt 🇩🇪')

@router.callback_query(F.data == 'it')
async def get_it(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'it'
    await callback.message.answer('Hai selezionato l\'italiano 🇮🇹')

@router.callback_query(F.data == 'pt')
async def get_pt(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'pt'
    await callback.message.answer('Você selecionou português 🇵🇹')

@router.callback_query(F.data == 'ja')
async def get_ja(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'ja'
    await callback.message.answer('日本語を選択しました 🇯🇵')

@router.callback_query(F.data == 'zh-CN')
async def get_zh(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'zh-CN'
    await callback.message.answer('您选择了中文 🇨🇳')

@router.callback_query(F.data == 'ar')
async def get_ar(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'ar'
    await callback.message.answer('لقد اخترت اللغة العربية 🇸🇦')

@router.callback_query(F.data == 'hi')
async def get_hi(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'hi'
    await callback.message.answer('आपने हिंदी चुना 🇮🇳')

@router.callback_query(F.data == 'ko')
async def get_ko(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'ko'
    await callback.message.answer('당신은 한국어를 선택했습니다 🇰🇷')

@router.callback_query(F.data == 'tr')
async def get_tr(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'tr'
    await callback.message.answer('Türkçe seçtiniz 🇹🇷')

@router.callback_query(F.data == 'el')
async def get_el(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'el'
    await callback.message.answer('Επιλέξατε ελληνικά 🇬🇷')

@router.callback_query(F.data == 'nl')
async def get_nl(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'nl'
    await callback.message.answer('Je hebt Nederlands geselecteerd 🇳🇱')

@router.callback_query(F.data == 'sv')
async def get_sv(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'sv'
    await callback.message.answer('Du har valt svenska 🇸🇪')

@router.callback_query(F.data == 'pl')
async def get_pl(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'pl'
    await callback.message.answer('Wybrałeś język polski 🇵🇱')

@router.callback_query(F.data == 'uk')
async def get_uk(callback: CallbackQuery):
    global LANGUAGE
    LANGUAGE = 'uk'
    await callback.message.answer('Ви вибрали українську 🇺🇦')
    
@router.message() 
async def translation(message: Message) :
    global LANGUAGE
    await message.answer(translate(word=message.text, target_lang=LANGUAGE))
    
