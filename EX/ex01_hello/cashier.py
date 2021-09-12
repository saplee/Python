"""cashier."""
# asks amount of coins
amount = int(input("Enter a sum:"))
coins = 0
# calculates how many coins fits to amount
coins += amount // 50
# calculates amount residue
residue = amount % 50
# calculates how many coins fits to residue
coins += residue // 20
# calculates amount residue
second_residue = residue % 20
# calculates how many coins fits to residue
coins += second_residue // 10
# calculates amount residue
third_residue = second_residue % 10
# calculates how many coins fits to residue
coins += third_residue // 5
# calculates amount residue
fourth_residue = third_residue % 5
# calculates how many coins fits to residue
coins += fourth_residue // 1
# calculates amount residue
fifth_residue = fourth_residue % 1
# prints amount of coins needed
print(f"Amount of coins needed: {coins}")
