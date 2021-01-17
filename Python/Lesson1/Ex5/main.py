print("Type costs")
costs = int(input())
print("Type profit")
profit = int(input())
if profit >= costs:
    balance = 100 * profit / costs - 100
    print("Balance positive for", "{:.2f}".format(balance), "percents")
    print("Type the number of employees")
    emp = int(input())
    print("Each employee earned a prize", "{:.2f}".format((profit-costs)/emp), "smiles")
else:
    print("Balance negative")
