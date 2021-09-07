"""cashier."""
# asks amount of coins
amount = int(input("Enter a sum:"))
# calculates how many coins fits to amount
coin1 = amount // 50
# calculates amount residue
jaak = amount % 50
# calculates how many coins fits to jaak
coin2 = jaak // 20
# calculates amount residue
jaak2 = jaak % 20
# calculates how many coins fits to jaak2
coin3 = jaak2 // 10
# calculates amount residue
jaak3 = jaak2 % 10
# calculates how many coins fits to jaak3
coin4 = jaak3 // 5
# calculates amount residue
jaak4 = jaak3 % 5
# calculates how many coins fits to jaak4
coin5 = jaak4 // 1
# calculates amount residue
jaak5 = jaak4 % 1
# calculates coins
coins = (coin1 + coin2 + coin3 + coin4 + coin5)
# prints amount of coins needed
print(f"Amount of coins needed: {coins}")
