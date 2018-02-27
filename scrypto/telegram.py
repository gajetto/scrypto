import telepot

token = '461226220:AAG-QSiVeUqn5uuC4JVxCyIkI2pJeyrRqPo'
TelegramBot = telepot.Bot(token)

update = TelegramBot.getUpdates()
TelegramBot.sendMessage(476895805, "Avec un peu de chance ça va marcher comme sur des roulettes")
#id = update['']['']['']