open_file = open('CupcakeInvoices.csv')

for row in open_file:
    print(row)
open_file.seek(0,0)

for row in open_file:
    values = row.split(',')
    print(values[2])


open_file.seek(0,0)

invoice_total = 0

for row in open_file:
    values = row.split(',')
   
    quantity = float(values[3])
    price = float(values[4])
    total = quantity * price
    print(total)
    invoice_total += total
    
    

print(invoice_total)

open_file.seek(0,0)

total_choc = 0
total_van = 0
total_straw = 0

for row in open_file:
    item = row.split(',')
    for value in item:
        if value == "Chocolate":
            total_choc += 1
        elif value == "Vanilla":
            total_van += 1
        elif value == "Strawberry":
            total_straw += 1

print("Chocolate", total_choc)
print("Vanilla", total_van)
print("Strawberry", total_straw)

open_file.close()


