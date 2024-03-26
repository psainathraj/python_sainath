from tabulate import tabulate

data = []

while True:
    slno = input("Enter the slno (or 'q' to quit): ")
    
    if slno.lower() == 'q':
        break

    item = str(input('Enter the item: '))
    quantity = int(input('Enter the quantity: '))
    
    data.append([slno, item, quantity])
    
if data:
    headers = ["slno", "item", "quantity"]
    table = tabulate(data, headers, tablefmt="fancy_grid")
    print(table)
else:
    print("No data to display.")
