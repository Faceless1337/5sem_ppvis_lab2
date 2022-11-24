import tkinter as tk
from Interface import Interface
from Controller import Controller
from Order import Order
from User import User


class Application:
    def launch(self):
        controller = Controller()
        interface = Interface()
        order = Order()
        user = User()
        interface.showStartWindow()





if __name__ == '__main__':
    app = Application()
    app.launch()

