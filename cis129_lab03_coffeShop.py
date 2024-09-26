print('***************************************')
print('My Coffee, Muffin, and More Shop')
print('Number of coffees bought?')
numCoffees=int(input())
print('Number of muffins bought?')
value2=int(input()) # variable name could be more descriptive
print('Number of scones bought?')
value3=int(input()) # variable name could be more descriptive
print('Number of teas bought?')
value4=int(input()) # variable name could be more descriptive
print('***************************************')
print('***************************************')
print('My Coffee, Muffin, and More Shop Receipt')
coffee=numCoffees*5
print(str(numCoffees)+ " Coffee at $5 each: $ " + str(coffee)+ ".00")
muffin=value2*4
print(str(value2)+ " Muffins at $4 each: $ " + str(muffin)+ ".00")
scone=value3*3
print(str(value3)+ " Scones at $3 each: $ " + str(scone)+ ".00")
tea=value4*2
print(str(value4)+ " Tea at $2 each: $ " + str(tea)+ ".00")
itemsTotal = (coffee+muffin+scone+tea)
taxAmount=(itemsTotal*0.06)
print("6% tax: " + str(taxAmount))
print('---------')
print("Total: " + str(itemsTotal+taxAmount))
print('***************************************')
print('Thank You For Choosing "My Coffee, Muffins, and More Shop"! We Hope To See You Again!')
#Great job! - Brittany
