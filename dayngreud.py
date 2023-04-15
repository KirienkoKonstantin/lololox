import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
яяя = "scxac"
token = '5916819071:AAHLpf8PXta5Nzo6yAG3Yz-Fbhx3Bbmejpo'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
    )

    await message.answer(response['choices'][0]['text'])
executor.start_polling(dp, skip_updates=True)