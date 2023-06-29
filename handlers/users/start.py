import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menukey import menukeyboard
from loader import dp,db,bot
from data.config import ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user=await db.add_user(telegram_id=message.from_user.id,
                               username=message.from_user.username,
                               full_name=message.from_user.full_name
                               )
    except asyncpg.exceptions.UniqueViolationError:
        user=await db.select_user(telegram_id=message.from_user.id)


    await message.answer("Xush Kelibsiz",reply_markup=menukeyboard)


    # Adminga Xabar yuboramiz

    count= await db.count_users()
    msg=f"{message.from_user.full_name} bazaga qo'shildi \n Bazada {count} ta foydalanuvchi bor"
    await bot.send_message(chat_id=ADMINS[0],text=msg)








