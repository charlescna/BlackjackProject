import csv

def read_money_amount():
    try:
        with open('money.txt', 'r') as f:
            reader = csv.reader(f)
            money_amount = float(next(reader)[0])
            return money_amount
    except FileNotFoundError:
        print("File cannot be found!")
        return 100
def write_money_amount(money_amount):
    with open('money.txt', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([money_amount])
