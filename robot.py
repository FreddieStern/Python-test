# robot_price = 900
# print(robot_price * 2 * 1.25 + 100 * 1.06)

# robot_count = 2
# robot_price = 900
# robot_tax = 1.25

# book_count = 1
# book_price = 100
# book_tax = 1.06

# print(robot_price * robot_count * robot_tax + book_count * book_price * book_tax)

# robot = {"price": 900, "count": 2, "tax": 1.25}

# print (robot["price"] * robot["count"] * robot["tax"] + 100 * 1.06)

# book = {"price": 100, "count": 1, "tax": 1.06}

# print (robot["price"] * robot["count"] * robot["tax"] + book["price"] * book["tax"])

# class Product:
# 	price = 0
# 	count = 0
# 	tax = 1

# robot = Product()
# robot.price = 900
# robot.count = 2
# robot.tax = 1.25

# book = Product()
# book.price = 100
# book.count = 1
# book.count = 1.06

# class Product:
# 		price = 0
# 		count = 0
# 		tax = 1

# 		def price_with_tax(self):
# 			return self.price * self.count * self.tax

# robot = Product()
# robot.price = 900
# robot.count = 2
# robot.tax = 1.25

# book = Product()
# book.price = 100
# book.count = 1
# book.tax = 1.06

# print(robot.price_with_tax() + book.price * book.tax) 

# print(robot.price_with_tax() + book.price_with_tax())

class Product:
	def __init__(self, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax

	def price_with_tax(self):
		total = self.price * self.count * self.tax
		if total > 500:
			return 0.9 * total
		else:
			return total

# robot = Product(price=900, count=2, tax=1.25)
# book = Product(price=100, count=1, tax=1.06)

# print(robot.price_with_tax() + book.price_with_tax())

# products = [Product(price=900,count=2,tax=1.25), Product(price=100,count=1,tax=1.06)]
# total_price = products[0].price_with_tax() + products[0].price_with_tax()
# print(total_price)

products = [Product(price=900,count=2,tax=1.25), Product(price=100,count=1,tax=1.06)]
total_price = 0
for product in products: 
	total_price = total_price + product.price_with_tax()
print(total_price) 







 


