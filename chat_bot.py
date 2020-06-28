from chatterbot import ChatBot


class Bot:
    def __init__(self):
        self.chatbot = ChatBot('Rauff')

    def chat(self, input_str):
        response = self.chatbot.get_response(input_str)
        print(f"Input : {input_str}")
        print(f"{self.chatbot.name}: {response}")
        return response

