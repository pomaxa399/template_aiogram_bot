import asyncio

from create_bot import bot, dp
from core.handlers.start import start_router
from config import settings


@dp.startup()
async def on_startup(bot: bot):
    # await set_command(bot)
    await bot.send_message(settings.admin.id, text='Бот запущен!')


@dp.shutdown()
async def on_shutdown(bot: bot):
    await bot.send_message(settings.admin.id, text='Бот остановлен!')


async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
