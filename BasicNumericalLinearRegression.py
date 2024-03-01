import itertools
PizzaSize=[6,8,12,14,18]
PizzaPrice=[350,775,1150,1395,1675]
SizeAvg=0
SizeAvgSq=0
PriceAvg=0
SizeAndPrice=0
for item,item2 in zip(PizzaSize,PizzaPrice):
    SizeAvg+=item
    PriceAvg+=item2
    SizeAndPrice+=item*item2
for item in PizzaSize:
    SizeAvgSq+=item**2
SizeAvg/=len(PizzaSize)
PriceAvg/=len(PizzaPrice)
SizeAndPrice/=len(PizzaPrice)
SizeAvgSq/=len(PizzaSize)
print(f"Average Pizza Size: {SizeAvg} Average Pizza Price: {PriceAvg} {SizeAndPrice}")

m=((PriceAvg*SizeAvg)-SizeAndPrice)/(SizeAvg**2-SizeAvgSq)
c=PriceAvg-(m*SizeAvg)
x=int(input("Pizza Size: "))
print(f"Predicted Price = {m*x+c}")
