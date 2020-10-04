import telebot

bot=telebot.TeleBot('token')

def clear_bot_updates(bot):
    new_update=bot.get_updates()
    if new_update:
        new_id=new_update[-1].update_id+1
        bot.get_updates(offset=new_id)
        print("Pending updates clear")
    else:
        print('No pending updates')


clear_bot_updates(bot)

bot.polling()
