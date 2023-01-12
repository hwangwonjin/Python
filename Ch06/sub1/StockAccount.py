from sub1.Account import Account

class StockAccount(Account):
    
    def __init__(self, bank, id, name, blance, stock, amount, price):
        super().__init__(bank, id, name, blance)
        self.stock = stock
        self.amount = amount
        self.price = price


    def sell(self, amount, price):
        self._blance += amount * price
        self.amount -= amount

    def buy(self, amount, price):
        self._blance -= amount * price
        self.amount += amount

    def show(self):
        super().show()
        print('주식종목 : ', self.stock)
        print('주식수량 : ', self.amount)
        print('주식가격 : ', self.price)