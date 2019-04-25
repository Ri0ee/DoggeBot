from telegram.ext import Updater, CommandHandler
import requests


def get_dogge_url():
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']
    return image_url


def show_dogge(bot, update):
    print('Showing Dogge')
    url = get_dogge_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def show_human(bot, update):
    print('Showing Human')
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo='https://thispersondoesnotexist.com/image')


def main():
    f = open("key.txt", "r")
    key = f.read()[:-1]
    f.close()

    updater = Updater(token=key)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('dogge', show_dogge))
    dp.add_handler(CommandHandler('human', show_human))

    print("Starting polling...")
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
