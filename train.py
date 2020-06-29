
chatbot = ChatBot('Rauff')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
print("Finished")
