from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

chatbot = ChatBot('Rauff')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
print("Finished")
