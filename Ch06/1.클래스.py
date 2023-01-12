"""
날짜 : 2023/01/11
이름 : 황원진
내용 : 파이썬 클래스 실습하기
"""
from sub1.Car import Car
from sub1.Account import Account

sonata = Car('소나타', '흰색', 3000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

bmw = Car('BMW', '검정', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

kb = Account('국민은행', '101-12-2999', '김유신', 30000)
kb.deposit(20000)
kb.withdraw(2000)
kb.show()
