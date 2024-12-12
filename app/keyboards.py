from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from .languages import languages_dict

languages = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'{lang} {data_lang['emoji']}', callback_data=data_lang['code'])] \
                                  for lang, data_lang in languages_dict.items()
                                  ])
