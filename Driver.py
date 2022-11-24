from User import User

class Driver(User):
    def __init__(self):
        self.vehicleNumber: str = None
        self.accountBalance: float = None
        self.options: dict = None
        self.doesWork: bool = None
        self.isOrder: bool = None
