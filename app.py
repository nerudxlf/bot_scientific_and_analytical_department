from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)
    from utils.notify_admins import on_startup_notify
    await db.create()
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    from loader import db
    executor.start_polling(dp, on_startup=on_startup)
