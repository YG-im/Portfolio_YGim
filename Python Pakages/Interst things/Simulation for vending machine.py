
# coding: utf-8

# # Vending machine

# - 자판기 시뮬레이션 프로그램입니다. 
# - 이 자판기는 총 10잔의 커피를 판매할 수 있습니다.
# - 커피 한잔에 300원입니다.

# In[2]:



coffee=10

while True:
    money=int(input("돈을 넣어주세요:"))
    if money==300:
        print("커피가 나왔습니다.")
        coffee=coffee-1
        print("남은 커피는 %s잔입니다."%coffee)
    elif money>300:
        print("커피가 나왔습니다. 거스름돈은 %s원 입니다."%(money-300))
        coffee=coffee-1
        print("남은 커피는 %s잔입니다."%coffee)
    else:
        print("돈이 %s원 부족합니다."%(300-money))
    while money<300:
        money1=int(input("돈을 %s원 더 넣어주세요:"%(300-money)))
        money=money+money1
        if money==300:
            print("커피가 나왔습니다.")
            coffee=coffee-1
            print("남은 커피는 %s잔입니다."%coffee)
        elif money>300:
            print("커피가 나왔습니다. 거스름돈은 %s원 입니다."%(money-300))
            coffee=coffee-1
            print("남은 커피는 %s잔입니다."%coffee)
    if not coffee:
        print("Sold out")
        break

