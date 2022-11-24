from User import User



class Controller:
    def signUp(self, typeOfUser: User):
        pass

    def signIn(self, login: str, password: str):
        pass

    def showInfoAboutUser(self, user: User):
        pass

    def rate(self, user: User):
        pass

    def changePassword(self, passwordOfUser: str):
        pass

    def changeLanguage(self, user: User):
        pass

    def startWork(self, doesDriverWork: bool):
        pass

    def orderTaxi(self, user: User, startPoint: str, endPoint: str, paymentMethod: str, options: [], comments: []):
        pass

    def payTrip(self, user: User):
        pass

    def changeOptions(self, options: dict):
        pass


