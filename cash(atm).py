print("===ATM Cash Dispenser===\n")
total_100=total_50=total_20=total_10=0
customers_served=0
total_dispensed=0
serving=True
while serving:
    name=input('enter name')
    amount=int(input(f"Hello{name}!Enter withdrawal amount:"))
    if amount <= 0 or amount%10!=0:
        print('Invalid amount.Please enter a positive no. that has a zero at the end eg- 20.\n')
        continue
    print(f'\nDispensing{amount} units for {name}')
    remaining = amount
    idx=1
    while idx <=4:
        if idx == 1:value=100
        elif idx == 2:value=50
        elif idx == 3:value=20
        elif idx == 4:value=10
        count = remaining//value
        if count>0:
            print(f'{count}x{value}-unit note(s)={count*value}')
            remaining -= count*value
            if value == 100:total_100 += count
            if value == 50:total_50 += count
            if value == 20:total_20 += count
            if value == 10:total_10 += count
        idx += 1

    customers_served += 1
    total_dispensed += amount
    print(f"transaction complete{name}!\n")
    again=input('Next customer?(y/n)').strip().lower()
    if again !="y":
        serving = False
print("\n===Daily Denomination Report===")
for slot in range(1,7):
    if slot == 1:value, total = 100,total_100
    elif slot == 2:value, total = 100,total_50
    elif slot == 3:value, total = 100,total_20
    elif slot == 4:value, total = 100,total_10
    if total>0:
        print(f'{value}-unit notes dispensed:{total}',end='')
        for note in range(total):
            print("=",end='')
        print()
print(f"\nCustomers served : {customers_served}")

print(f"Total dispensed : {total_dispensed} units")

print("ATM session closed. Goodbye!")