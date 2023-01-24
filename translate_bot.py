
import logging
from transliterate import translit
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_message(message: types.Message):
    
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name}!"
    logging.info(f"{user_name=} {user_id} send_message: {message.text}")
    await message.reply(text)


@dp.message_handler()
async def translate_message(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    translite_letters = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh',
      'ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'ie','ы':'y','ь':'','э':'e',
      'ю':'iu','я':'ia', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'KH',
      'Ц':'TS','Ч':'CH','Ш':'SH','Щ':'SHCH','Ъ':'IE','Ы':'y','Ь':'','Э':'E',
      'Ю':'IU','Я':'IA'}
    text = message.text
    for key in translite_letters:
        text = text.replace(key, translite_letters.get(key))
    logging.info(f"{user_name=} {user_id=} sent_message: {text}")
    return await bot.send_message(user_id, text)



if __name__ == '__main__':
    executor.start_polling(dp) 
    
    
