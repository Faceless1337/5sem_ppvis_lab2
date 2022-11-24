from User import User
from Order import Order

class Client(User):
    def __init__(self):
        self.pinCode: int = None
        self.creditCardNumber: str = None
        self.bonusBalance: float = None
