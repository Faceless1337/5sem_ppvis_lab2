

class Order:
    def __init__(self):
        self.startPoint: str = None
        self.endPoint: str = None
        self.options: [] = None
        self.comments: [] = None
        self.orderAmount: float = None

    def calculateSum(self, startPoint: str, endPoint: str) -> None:
        pass