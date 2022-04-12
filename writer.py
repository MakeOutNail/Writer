import pynput
import json
import time



class main:
    def __init__(self):
        self.keyboard = pynput.keyboard.Controller()
        self.save = []
        self.config = {
            "text": "Hello World!",
            "message": "Good day!",
            "time": "0"
        }
        try:
            with open('config.json', 'r') as i:
                self.save = json.load(i)

            self.text = self.save['text']
            self.message = self.save['message']
            self.time = int(self.save['time'])

            if(self.text == ""):
                self.text = "Hello World!"
            if(self.message == ""):
                self.message = "Good Day!"
            if(self.time == ""):
                self.message = 0
        except:
            with open('config.json', 'w') as i:
                json.dump(self.config, i)

    def settings(self):
        option = input("Options/")

        if(option == 'm' or option == 'M'):
            self.message = input("Options/Message/")
            self.save['message'] = self.message
            with open('config.json', 'w') as i:
                json.dump(self.save, i)
            self.settings()
        elif(option == 'Q' or option == 'q'):
            self.main()


    def write(self):
        time.sleep(self.time)
        self.keyboard.type(self.text)

    def main(self):

        print("")
        print(self.message)
        print("")

        print("Do you want to go into setting mode?[y]")
        settings = input(":")

        if(settings == 'y' or settings == 'Y'):
            self.settings()

        print("****************************************")
        self.text = input("Text:")
        print("****************************************")
        self.time = int(input("Text/PerSecond:"))
        print("****************************************")

        time.sleep(3)

        while(True):
            self.write()


if __name__ == "__main__":
    main = main()
    main.main()