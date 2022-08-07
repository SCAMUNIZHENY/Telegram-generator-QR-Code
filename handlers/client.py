from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher, types
from keyboards import kb_client, kb_cancel
from scripts import make_qrcode
from os import remove


class QR(StatesGroup):
    user_id = State()
    сontent = State()


async def cmd_start(message: types.Message):
    await message.answer(f"Hello", reply_markup=kb_client)


async def cmd_make(message: types.Message, state: FSMContext):
    await QR.user_id.set()
    await state.update_data(user_id=message.from_user.id)
    await QR.сontent.set()
    await message.answer('Enter text or link', reply_markup=kb_cancel)


async def send(message: types.Message, state: FSMContext):
    await state.update_data(сontent=message.text)
    user_data = await state.get_data()
    await message.answer_photo(await make_qrcode(user_data["сontent"], user_data['user_id']), reply_markup=kb_client)
    remove(f"images/{user_data['user_id']}.png")
    await state.finish()


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Action canceled", reply_markup=kb_client)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(
        equals="cancel", ignore_case=True), state="*")
    dp.register_message_handler(cmd_make, Text(
        equals='Create qr code'), state="*")
    dp.register_message_handler(
        send, state=QR.сontent, content_types=types.ContentTypes.TEXT)
