amount = int(input("Enter a sum:"))
coin1 = amount//50
jaak = amount % 50
coin2 = jaak//20
jaak2 = jaak % 20
coin3 = jaak2//10
jaak3 = jaak2 % 10
coin4 = jaak3//5
jaak4 = jaak3 % 5
coin5 = jaak4//1
jaak5 = jaak4 % 1
coins = (coin1+coin2+coin3+coin4+coin5)

print(f"Amount of coins needed: {coins}")