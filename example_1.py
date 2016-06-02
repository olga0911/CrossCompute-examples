grocery = {"bananas": 3, "apples": 2, "kiwi": 5, "strawberries": 5}
price = {"bananas" : 2, "apples": 1, "kiwi": 0.5, "strawberries": 3}


for item in grocery:
	x = grocery[item] * price[item]
	print (x) 

	if x <= 10:
		print ("Good price")
	else:
		print ("Expensive!")
