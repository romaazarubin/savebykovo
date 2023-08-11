from aiogram.dispatcher.filters import Command, Text
from main import dp, bot
from keyboards.all_keyboards import markup_inline, first_markup_inline, \
    second_markup_inline, third_markup_inline
from config import PAYMENTS_TOKEN, admin_id
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery, CallbackQuery
from aiogram.types.message import ContentType


# @dp.message_handler(Command('start'))
# async def start(message: Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Привет, ты заглянул, чтобы принять участие в благотворительной '
#                                 'беспроигрышной лотерее в рамках Йога фестиваля в усадьбе Быково @savebykovo?',
#                            reply_markup=first_markup)
#
#
# @dp.message_handler(Text("Да"))
# async def word_yes(message: Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Беспроигрышная благотворительная лотерея - это прекрасные подарки от партнеров, мастеров и художников, '
#                                 'творческих и инициативных друзей нашего проекта #SAVEBYKOVO. Хотите принять участие?',
#                            reply_markup=second_markup)
#
#
# @dp.message_handler(Text("Возможно"))
# async def word_mb(message: Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Беспроигрышная благотворительная лотерея - это прекрасные подарки от партнеров, мастеров и художников, '
#                                 'творческих и инициативных друзей нашего проекта #SAVEBYKOVO. Хотите принять участие?',
#                            reply_markup=second_markup)
#
#
# @dp.message_handler(Text("ДА"))
# async def offline(message: Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Все собранные АНО "проект возрождение" средства от благотворительной лотереи идут в помощь проекту @savebykovo на содержание и восстановление Усадьбы БЫКОВО.',
#                            reply_markup=third_markup)
#
#
# @dp.message_handler(Text("Естественно"))
# async def offline(message: Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Все собранные АНО "проект возрождение" средства от благотворительной лотереи идут в помощь проекту @savebykovo на содержание и восстановление Усадьбы БЫКОВО.',
#                            reply_markup=third_markup)
#
# @dp.message_handler(Text("Ок"))
# async def offline(message: Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='УРА! Для вас есть 3 вида билетов! Стоимость билета не влияет на стоимость подарка. '
#                                 'Вы можете получить очень дорогой подарок одинаково приобретя билет номиналом 300₽, 500₽ или 1000₽,'
#                                 ' суть лотереи в рамках нашего фестиваля - помощь проекту @savebykovo на содержание и восстановление Усадьбы БЫКОВО.',
#                            reply_markup=markup_inline)
#
#
# @dp.message_handler(Text("Понятно"))
# async def offline(message: Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='УРА! Для вас есть 3 вида билетов! Стоимость билета не влияет на стоимость подарка. '
#                                 'Вы можете получить очень дорогой подарок одинаково приобретя билет номиналом 300₽, 500₽ или 1000₽,'
#                                 ' суть лотереи в рамках нашего фестиваля - помощь проекту @savebykovo на содержание и восстановление Усадьбы БЫКОВО.',
#                            reply_markup=markup_inline)

@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет, ты заглянул, чтобы принять участие в благотворительной беспроигрышной лотерее в рамках проекта восстановления и сохранения усадьбы Быково в рамках проекта по сохранению усадьбы Быково @savebykovo?',
                           reply_markup=first_markup_inline)


@dp.callback_query_handler(text_contains='yes')
async def word_yes(call: CallbackQuery):
    await call.message.edit_text(
        text='Беспроигрышная благотворительная лотерея - это прекрасные подарки от партнеров, мастеров и художников, '
             'творческих и инициативных друзей нашего проекта #SAVEBYKOVO. Хотите принять участие?',
        reply_markup=second_markup_inline)


@dp.callback_query_handler(text_contains='mb')
async def word_mb(call: CallbackQuery):
    await call.message.edit_text(
        text='Беспроигрышная благотворительная лотерея - это прекрасные подарки от партнеров, мастеров и художников, '
             'творческих и инициативных друзей нашего проекта #SAVEBYKOVO. Хотите принять участие?',
        reply_markup=second_markup_inline)


@dp.callback_query_handler(text_contains='YES')
async def offline(call: CallbackQuery):
    await call.message.edit_text(
        text='Все собранные средства от беспроигрышной лотереи будут направлены на сохранение усадьбы Быково и работы с парком усадьбы на счёт #SAVEBYKOVO АНО «Центр сохранения исторического и культурного наследия «Проект Возрождения» ОГРН 1197700016381»',
        reply_markup=third_markup_inline)


@dp.callback_query_handler(text_contains="naturally")
async def offline(call: CallbackQuery):
    await call.message.edit_text(
        text='Все собранные средства от беспроигрышной лотереи будут направлены на сохранение усадьбы Быково и работы с парком усадьбы на счёт #SAVEBYKOVO АНО «Центр сохранения исторического и культурного наследия «Проект Возрождения» ОГРН 1197700016381»',
        reply_markup=third_markup_inline)


@dp.callback_query_handler(text_contains="ok")
async def offline(call: CallbackQuery):
    await call.message.edit_text(
        text='Стоимость билета не влияет на стоимость подарка. Вы можете получить очень дорогой подарок одинаково приобретя билет номиналом 300₽, 500₽ или 1000₽',
        reply_markup=markup_inline)


@dp.callback_query_handler(text_contains="undst")
async def offline(call: CallbackQuery):
    await call.message.edit_text(
        text='Стоимость билета не влияет на стоимость подарка. Вы можете получить очень дорогой подарок одинаково приобретя билет номиналом 300₽, 500₽ или 1000₽',
        reply_markup=markup_inline)


@dp.callback_query_handler(text_contains='data1')
async def buy_process(message: Message):
    prices = [
        LabeledPrice(label="1 БИЛЕТ номиналом 300₽", amount=30000)
    ]

    await bot.send_invoice(
        message.from_user.id,
        title="1 БИЛЕТ номиналом 300₽",
        description="Оплата",
        provider_token=PAYMENTS_TOKEN,
        currency="rub",
        photo_width=416,
        photo_height=234,
        photo_size=416,
        is_flexible=False,
        prices=prices,
        start_parameter="subscription-options",
        payload="test-invoice-payload"
    )


@dp.callback_query_handler(text_contains='data2')
async def buy_process(call: CallbackQuery):
    prices = [
        LabeledPrice(label="2 БИЛЕТ номиналом 500₽", amount=50000)
    ]

    await bot.send_invoice(
        call.from_user.id,
        title="2 БИЛЕТ номиналом 500₽",
        description="Оплата",
        provider_token=PAYMENTS_TOKEN,
        currency="rub",
        photo_width=416,
        photo_height=234,
        photo_size=416,
        is_flexible=False,
        prices=prices,
        start_parameter="subscription-options",
        payload="test-invoice-payload"
    )


@dp.callback_query_handler(text_contains='data3')
async def buy_process(call: CallbackQuery):
    prices = [
        LabeledPrice(label="3 БИЛЕТ номиналом 1000₽", amount=100000)
    ]

    await bot.send_invoice(
        call.from_user.id,
        title="3 БИЛЕТ номиналом 1000₽",
        description="Оплата",
        provider_token=PAYMENTS_TOKEN,
        currency="rub",
        photo_width=416,
        photo_height=234,
        photo_size=416,
        is_flexible=False,
        prices=prices,
        start_parameter="subscription-options",
        payload="test-invoice-payload"
    )


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    # Проверьте информацию о платеже и подтвердите его
    # await db.add_user(pre_checkout_query.from_user.username)
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=['successful_payment'])
async def process_successful_payment(message: Message):
    # id = await db.take_id(message.from_user.username)
    # Обработайте успешный платеж
    await message.answer(
        f'Получить подарок вы можете на любом нашем мероприятии, опубликованном в официальном ТГ канале  @savebykovo, показав этот {message.from_user.id} номер на стойке благотворительной лотереи, а можете и не забирать свой подарок, а просто поддержать наш проект своим пожертвованием.')
    await message.answer(
        'Благодарим Вас сердечно и всегда рады видеть вас на мероприятиях в усадьбе Быково, ведь усадьба живёт людьми и событиями.\nУзнать новости проекта savebykovo.ru\n'
        'Начать заново - /start \n'
        'Отправить ссылку другу - https://t.me/Savebykovo_Bot')
