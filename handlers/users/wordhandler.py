from aiogram import types
from loader import dp,db,bot




@dp.message_handler(commands='countword')
async def count_word(message:types.Message):

    count= await db.count_words()
    msg=f"Bazada {count} ta lug'at bor"
    await message.answer(msg)




@dp.message_handler(commands=['dictionary'])
async def get_all_words(message: types.Message):
    words = await db.select_all_words()
    uz = []
    en = []

    if words:
        for word in words:
            uz.append(word[1])
            en.append(word[2])

        msg = "<b>O'zbekcha</b> - <b>Inglizcha</b>\n\n"
        for i in range(len(uz)):
            msg += f"{uz[i]} - {en[i]}\n"

        await message.answer(msg)
    else:
        await message.answer("There are no words in the dictionary.")





