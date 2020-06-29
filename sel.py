import time
from chat_bot import Bot
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WaBot:

    def __init__(self, group_name="PUBG ki fauj kare mauj😎"):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://web.whatsapp.com")
        self.last_message = []
        time.sleep(15)
        group = self.driver.find_element_by_xpath(f"//span[@title='{group_name}']")
        group.click()
        self.RauffBot = Bot()

    def send_message(self, response):

        message = self.driver.find_element_by_xpath('''//*[@id="main"]/footer/div[1]/div[2]/div/div[2]''')
        message.send_keys(response)
        send = self.driver.find_element_by_xpath('''//*[@id="main"]/footer/div[1]/div[3]/button''')
        send.click()

    def rauff_speak(self, input_message):
        self.send_message(str(self.RauffBot.chat(input_message)))

    def read_message(self):
        while True:
            # print("this is the sub_func")
            curr_message = self.driver.find_element_by_xpath('''//div[contains(@class, "message-in focusable-list-item")]
                    [last()]''').text.split("\n")
            if curr_message == self.last_message:
                time.sleep(15)
                print("Sleepingzzzzzzz.......")
            else:
                break
        self.last_message=curr_message
        print(f"This is the last message: {curr_message[0]} at: {curr_message[-1]}")
        return self.last_message[0]


if __name__ == "__main__":

    wb = WaBot(group_name="PUBG ki fauj kare mauj😎")
    # wb.rauff_speak("How are you my friend")
    while True:
        ww = wb.read_message()
        wb.rauff_speak(str(ww))
