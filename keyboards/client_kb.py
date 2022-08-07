from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

but_start = KeyboardButton('Create qr code')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(but_start)

but_cancel = KeyboardButton('Cancel')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(but_cancel)
