from Controller import Controller
from tkinter import ttk
from tkinter import *
import tkinter as tk


class Interface:
    def __init__(self):
        self.root = Tk()
        self.signInWindow = None
        self.startWindow = Frame(self.root)
        self.signUpWindow = Frame(self.root)
        self.clientInterface = ClientInterface(self)
        self.driverInterface = DriverInterface(self)

    def showStartWindow(self):
        self.startWindow.grid(row=10, column=0, padx=80, pady=160)
        signInButton = ttk.Button(self.startWindow, text='Вход', command=lambda: self.presButtonSignIn())
        signInButton.grid(row=3, column=1, padx=10, pady=10)

        sigUpButton = ttk.Button(self.startWindow, text='Регистрация', command=lambda: self.pressButtonSignUp())
        sigUpButton.grid(row=4, column=1, padx=10, pady=10)
        self.startWindow.tkraise()
        self.root.mainloop()

    def pressButtonSignUp(self):
        pass

    def presButtonSignIn(self):
        self.startWindow.destroy()
        self.signInWindow = Frame(self.root)
        self.signInWindow.grid(row=10, column=0, padx=80, pady=160)
        loginVar = tk.StringVar()
        loginEntry = ttk.Entry(self.signInWindow, width=30)
        loginEntry.grid(row=1, column=1, sticky=tk.NSEW)

        passwordVar = tk.StringVar()
        passwordEntry = ttk.Entry(self.signInWindow, width=30)
        passwordEntry.grid(row=2, column=1, sticky=tk.NSEW)

        signInAsClient = ttk.Button(self.signInWindow, text='Sign in as client',
                                    command=lambda: self.clientInterface.showActionWindow())
        signInAsClient.grid(row=3, column=1, padx=10, pady=10)

        signInAsDriver = ttk.Button(self.signInWindow, text='Sign in as driver',
                                    command=lambda: self.driverInterface.showActionWindow())
        signInAsDriver.grid(row=4, column=1, padx=10, pady=5)
        self.signInWindow.tkraise()


class ClientInterface(Interface):
    def __init__(self, parent):
        self.parent = parent
        self.actionWindow = Frame(parent.root)
        self.settingsWindow = Frame(parent.root)
        self.infoWindow = Frame(parent.root)
        self.orderWindow = Frame(parent.root)
        self.changePasswordWindow = Frame(parent.root)
        self.changeLanguageWindow = Frame(parent.root)
        self.changeCreditCardWindow = Frame(parent.root)

    def showActionWindow(self):
        self.parent.signInWindow.destroy()
        self.actionWindow.grid(row=10, column=0, padx=80, pady=160)
        label = ttk.Label(text="Ваш статус - Клиент. Добро пожаловать в систему!")
        label.grid(row=1, column=0, padx=1, pady=5)
        buttonOrderTaxi = ttk.Button(self.actionWindow, text='Заказать такси',
                                     command=lambda: self.pressButtonOrderTaxi())
        buttonOrderTaxi.grid(row=1, column=1, padx=10, pady=10)

        buttonShowInfo = ttk.Button(self.actionWindow, text='Просмотр информации',
                                    command=lambda: self.pressButtonShowInfo())
        buttonShowInfo.grid(row=2, column=1, padx=10, pady=10)

        buttonSettings = ttk.Button(self.actionWindow, text='Настройки',
                                    command=lambda: self.pressButtonSettings())
        buttonSettings.grid(row=3, column=1, padx=10, pady=10)
        self.actionWindow.tkraise()

    def pressButtonSettings(self):
        self.showSettingsWindow()

    def showSettingsWindow(self):
        self.actionWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.settingsWindow = Frame(self.parent.root)
        self.settingsWindow.grid(row=10, column=0, padx=80, pady=160)

        buttonChangeLanguage = ttk.Button(self.settingsWindow, text='Изменить язык',
                                          command=lambda: self.pressButtonLanguage())
        buttonChangeLanguage.grid(row=1, column=1, padx=10, pady=10)

        buttonChangeCreditCardNumber = ttk.Button(self.settingsWindow, text='Изменить номер кредитной карты',
                                                  command=lambda: self.pressButtonChangeCreditCardNumber())
        buttonChangeCreditCardNumber.grid(row=1, column=2, padx=10, pady=10)

        buttonChangePassword = ttk.Button(self.settingsWindow, text='Изменить пароль',
                                          command=lambda: self.pressButtonChangePassword())
        buttonChangePassword.grid(row=1, column=3, padx=10, pady=10)
        self.settingsWindow.tkraise()

    def showInfoWindow(self):
        self.actionWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.infoWindow = Frame(self.parent.root)
        self.infoWindow.grid(row=10, column=0, padx=80, pady=160)
        label = ttk.Label(text="Для вас скидка 5%")
        label.grid(row=1, column=0, padx=1, pady=5)
        self.infoWindow.tkraise()

    def pressButtonShowInfo(self):
        self.showInfoWindow()

    def pressButtonRate(self):
        pass

    def pressButtonOrderTaxi(self):
        self.showOrderWindow()

    def showOrderWindow(self):
        self.actionWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.orderWindow = Frame(self.parent.root)
        self.orderWindow.grid(row=10, column=0, padx=80, pady=160)
        label = ttk.Label(text="Ваш заказ активен")
        label.grid(row=1, column=0, padx=1, pady=5)

        buttonOrderTaxi = ttk.Button(self.orderWindow, text='Оценить поездку',
                                     command=lambda: self.pressButtonRate())
        buttonOrderTaxi.grid(row=1, column=1, padx=10, pady=10)

        buttonOrderTaxi = ttk.Button(self.orderWindow, text='Оплатить поездку',
                                     command=lambda: self.pressButtonPayTrip())
        buttonOrderTaxi.grid(row=1, column=2, padx=10, pady=10)
        self.orderWindow.tkraise()

    def pressButtonPayTrip(self):
        pass

    def pressButtonChangePassword(self):
        self.showChangePasswordWindow()

    def showChangePasswordWindow(self):
        self.settingsWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.changePasswordWindow = Frame(self.parent.root)
        self.changePasswordWindow.grid(row=10, column=0, padx=80, pady=160)
        passwEntry = ttk.Entry(self.changePasswordWindow, width=30)
        passwEntry.grid(row=1, column=1, sticky=tk.NSEW)

        buttonChangePassword = ttk.Button(self.changePasswordWindow, text='Изменить пароль')
        buttonChangePassword.grid(row=1, column=2, padx=10, pady=10)

        self.changePasswordWindow.tkraise()

    def pressButtonLanguage(self):
        self.showChangeLanguageWindow()

    def showChangeLanguageWindow(self):
        self.settingsWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.changeLanguageWindowWindow = Frame(self.parent.root)
        self.changeLanguageWindowWindow.grid(row=10, column=0, padx=80, pady=160)
        langEntry = ttk.Entry(self.changeLanguageWindowWindow, width=30)
        langEntry.grid(row=1, column=1, sticky=tk.NSEW)

        buttonChangeLanguage = ttk.Button(self.changeLanguageWindowWindow, text='Изменить язык')
        buttonChangeLanguage.grid(row=1, column=2, padx=10, pady=10)

        self.changeLanguageWindowWindow.tkraise()

    def pressButtonChangeCreditCardNumber(self):
        self.showChangeCreditCardWindow()

    def showChangeCreditCardWindow(self):
        self.settingsWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.changeCreditCardWindow = Frame(self.parent.root)
        self.changeCreditCardWindow.grid(row=10, column=0, padx=80, pady=160)
        cardEntry = ttk.Entry(self.changeCreditCardWindow, width=30)
        cardEntry.grid(row=1, column=1, sticky=tk.NSEW)

        buttonChangeLanguage = ttk.Button(self.changeCreditCardWindow, text='Изменить номер кредитной карты')
        buttonChangeLanguage.grid(row=1, column=2, padx=10, pady=10)

        self.changeCreditCardWindow.tkraise()


class DriverInterface(Interface):
    def __init__(self, parent):
        self.parent = parent
        self.actionWindow = Frame(parent.root)
        self.settingsWindow = Frame(parent.root)
        self.infoWindow = Frame(parent.root)
        self.startWorkWindow = Frame(parent.root)
        self.changePasswordWindow = Frame(parent.root)
        self.changeLanguageWindow = Frame(parent.root)
        self.changeOptionsWindow = Frame(parent.root)

    def showActionWindow(self):
        self.parent.signInWindow.destroy()
        self.actionWindow.grid(row=10, column=0, padx=80, pady=160)
        label = ttk.Label(text="Ваш статус - Водитель. Добро пожаловать в систему!")
        label.grid(row=1, column=0, padx=1, pady=5)
        buttonOrderTaxi = ttk.Button(self.actionWindow, text='Начать работу',
                                     command=lambda: self.pressButtonStartWork())
        buttonOrderTaxi.grid(row=1, column=1, padx=10, pady=10)

        buttonShowInfo = ttk.Button(self.actionWindow, text='Просмотр информации',
                                    command=lambda: self.pressButtonInfo())
        buttonShowInfo.grid(row=2, column=1, padx=10, pady=10)

        buttonSettings = ttk.Button(self.actionWindow, text='Настройки',
                                    command=lambda: self.pressButtonSettings())
        buttonSettings.grid(row=3, column=1, padx=10, pady=10)
        self.actionWindow.tkraise()

    def pressButtonSettings(self):
        self.showSettingsWindow()

    def showSettingsWindow(self):
        self.actionWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.settingsWindow = Frame(self.parent.root)
        self.settingsWindow.grid(row=10, column=0, padx=80, pady=160)

        buttonChangeLanguage = ttk.Button(self.settingsWindow, text='Изменить язык',
                                          command=lambda: self.pressButtonLanguage())
        buttonChangeLanguage.grid(row=1, column=1, padx=10, pady=10)

        buttonChangeCreditCardNumber = ttk.Button(self.settingsWindow, text='Изменить опции',
                                                  command=lambda: self.pressButtonChangeOptions())
        buttonChangeCreditCardNumber.grid(row=1, column=2, padx=10, pady=10)

        buttonChangePassword = ttk.Button(self.settingsWindow, text='Изменить пароль',
                                          command=lambda: self.pressButtonChangePassword())
        buttonChangePassword.grid(row=1, column=3, padx=10, pady=10)
        self.settingsWindow.tkraise()

    def showInfoWindow(self):
        self.actionWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.infoWindow = Frame(self.parent.root)
        self.infoWindow.grid(row=10, column=0, padx=80, pady=160)
        label = ttk.Label(text="Чем больше заказов выполняете, тем больше у вас выручка.")
        label.grid(row=1, column=0, padx=1, pady=5)
        self.infoWindow.tkraise()

    def pressButtonInfo(self):
        self.showInfoWindow()

    def pressButtonRate(self):
        pass

    def pressButtonStartWork(self):
        self.showWorkWindow()

    def showWorkWindow(self):
        self.actionWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.startWorkWindow = Frame(self.parent.root)
        self.startWorkWindow.grid(row=10, column=0, padx=80, pady=160)
        label = ttk.Label(text="Вы успешно вышли на линию")
        label.grid(row=1, column=0, padx=1, pady=5)
        self.startWorkWindow.tkraise()

    def pressButtonChangePassword(self):
        self.showChangePasswordWindow()

    def showChangePasswordWindow(self):
        self.settingsWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.changePasswordWindow = Frame(self.parent.root)
        self.changePasswordWindow.grid(row=10, column=0, padx=80, pady=160)
        passwEntry = ttk.Entry(self.changePasswordWindow, width=30)
        passwEntry.grid(row=1, column=1, sticky=tk.NSEW)

        buttonChangePassword = ttk.Button(self.changePasswordWindow, text='Изменить пароль')
        buttonChangePassword.grid(row=1, column=2, padx=10, pady=10)

        self.changePasswordWindow.tkraise()

    def pressButtonLanguage(self):
        self.showChangeLanguageWindow()

    def showChangeLanguageWindow(self):
        self.settingsWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.changeLanguageWindowWindow = Frame(self.parent.root)
        self.changeLanguageWindowWindow.grid(row=10, column=0, padx=80, pady=160)
        langEntry = ttk.Entry(self.changeLanguageWindowWindow, width=30)
        langEntry.grid(row=1, column=1, sticky=tk.NSEW)

        buttonChangeLanguage = ttk.Button(self.changeLanguageWindowWindow, text='Изменить язык')
        buttonChangeLanguage.grid(row=1, column=2, padx=10, pady=10)

        self.changeLanguageWindowWindow.tkraise()

    def pressButtonChangeOptions(self):
        self.showChangeOptionsWindow()

    def showChangeOptionsWindow(self):
        self.settingsWindow.destroy()
        for widget in self.parent.root.winfo_children():
            widget.destroy()
        self.changeOptionsWindow = Frame(self.parent.root)
        self.changeOptionsWindow.grid(row=10, column=0, padx=80, pady=160)
        optionsEntry = ttk.Entry(self.changeOptionsWindow, width=30)
        optionsEntry.grid(row=1, column=1, sticky=tk.NSEW)

        buttonChangeOptions = ttk.Button(self.changeOptionsWindow, text='Изменить опции')
        buttonChangeOptions.grid(row=1, column=2, padx=10, pady=10)

        self.changeOptionsWindow.tkraise()
