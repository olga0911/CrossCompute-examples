import sys
from pandas import read_csv


# grocery = {"bananas": 3, "apples": 2, "kiwi": 5, "strawberries": 5}
# price = {"bananas" : 2, "apples": 1, "kiwi": 0.5, "strawberries": 3}


grocery_table_path = sys.argv[1]
print(sys.argv)
grocery_table = read_csv(grocery_table_path) 
for index, row in grocery_table.iterrows():
    x = row['Count'] * row['Price']
    print('The cost of %s %s is %s' % (row['Count'], row['Name'], x))
    if x <= 10:
        print ("Good price")
    else:
        print ("Expensive!")
