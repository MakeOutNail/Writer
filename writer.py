#@message HAVE FUN :)
#
#@author MakeOutNail
#@created 12.04.2022
#@LastUpdate 12.12.2022
#



import pynput
from pynput.keyboard import Key
import json
import time
import sys



class main:
    def __init__(self):
        self.keyboard = pynput.keyboard.Controller()
        self.save = []
        self.config = {
            "text": "Hello World!",
            "message": "Good day!",
            "time": 0,
            "wordwrap": "True"
        }
        try:
            with open('config.json', 'r') as i:
                self.save = json.load(i)

            self.text = self.save['text']
            self.message = self.save['message']
            self.time = int(self.save['time'])
            self.wordwrap = self.save['wordwrap']

            if(self.text == ""):
                self.text = "Hello World!"
            if(self.message == ""):
                self.message = "Good Day!"
            if(self.time == None):
                self.time = 0
            if(self.wordwrap == None):
                self.wordwrap = "True"

        except:
            with open('config.json', 'w') as i:
                json.dump(self.config, i)

    def settings(self):
        print("*****************************************")
        print("M - Changes the initial message")
        print("N - Line break settings(True-->Line break after each word)(False-->No line break)")
        print("T - Changes the time(Pause after each word)")
        print("W - Changes the text")
        print("Q - Exit")
        option = input("Options/")

        if(option == 'm' or option == 'M'):
            self.message = input("Options/Message/")
            self.save['message'] = self.message
            with open('config.json', 'w') as i:
                json.dump(self.save, i)
            self.settings()
        if(option == 't' or option == 'T'):
            self.time = input("Options/Time/")

            if(self.time.isnumeric() == False):
                self.time = 1

            self.save['time'] = int(self.time)
            with open('config.json', 'w') as i:
                json.dump(self.save, i)
            self.settings()
        if(option == 'w' or option == 'W'):
            self.text = input("Options/Text/")
            self.save['text'] = self.text
            with open('config.json', 'w') as i:
                json.dump(self.save, i)
            self.settings()
        if(option == 'n' or option == 'N'):
            self.wordwrap = input("Options/LineBreak/")
            if(self.wordwrap == "True" or self.wordwrap == "true" or self.wordwrap == "T" or self.wordwrap == "t"):
                self.wordwrap = "True"
            else:
                self.wordwrap = "False"
            self.save['wordwrap'] = self.wordwrap
            with open('config.json', 'w') as i:
                json.dump(self.save, i)
            self.settings()
        elif(option == 'Q' or option == 'q'):
            self.main()
        else:
            self.main()


    def write(self):
        time.sleep(self.time)
        self.keyboard.type(self.text)
        if(self.wordwrap == "True"):
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)

    def main(self):

        print("*****************************************")
        print(self.message)
        print("*****************************************")

        print("Y - Go to the settings")
        print("Press ENTER - Start the process")
        settings = input("/")

        if(settings == 'y' or settings == 'Y'):
            self.settings()
        elif(settings == "exit" or settings == "Exit" or settings == "quit" or settings == "close"):
            sys.exit()

        count_begin = 4
        while(count_begin > 0):
            count_begin-=1

            sys.stdout.write("\r" + str(count_begin) + " Seconds")
            sys.stdout.flush()

            time.sleep(1)

        while(True):
            self.write()


if __name__ == "__main__":
    main = main()
    main.main()