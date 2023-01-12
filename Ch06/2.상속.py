"""
날짜 : 2023/01/11
이름 : 황원진
내용 : 파이썬 상속 실습하기
"""

from sub1.StockAccount import StockAccount

kb = StockAccount('kb증권', '101-12-1001', '홍길동', 50000, '삼성전자', 10, 60000)
kb.deposit(100000)
kb.sell(5, 65000)
kb.show()