from models import Restaurant, Review, Customer

# Create some restaurants
restaurant1 = Restaurant(name="Pizza Palace", price=10)
restaurant2 = Restaurant(name="Fancy French", price=25)

# Create some customers
customer1 = Customer(first_name="Jane", last_name="Doe")
customer2 = Customer(first_name="John", last_name="Smith")

# Add reviews
customer1.add(restaurant1, 5)
customer1.add(restaurant2, 4)
customer2.add(restaurant1, 3)
customer2.add(restaurant2, 5)

# Add to session and commit
session.add_all([restaurant1, restaurant2, customer1, customer2])
session.commit()
