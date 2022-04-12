import pynput
import json
import time



class main:
    def __init__(self):
        self.keyboard = pynput.keyboard.Controller()
        self.text = "Hello World!"
        self.time = 0

    def write(self):
        time.sleep(self.time)
        self.keyboard.type(self.text)

    def main(self):
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