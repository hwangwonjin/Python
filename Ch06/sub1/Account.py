class Account:

    def __init__(self, bank, id, name, blance):
        self._bank  =bank
        self._id = id
        self._name = name
        self._blance  = blance


    def deposit(self, money):
        self._blance += money

    def withdraw(self, money):
        self._blance -= money

    def show(self):
        print('은행명 : ', self._bank)
        print('계좌번호 : ', self._id)
        print('이름 : ', self._name)
        print('잔액 : ', self._blance)