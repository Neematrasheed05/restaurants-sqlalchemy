from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Restaurant,Review,Customer


if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# Create some restaurants
restaurant1 = Restaurant(name="Pizza inn", price=10)
restaurant2 = Restaurant(name="pronto", price=25)

# Create some customers
customer1 = Customer(first_name="Jane", last_name="Doe")
customer2 = Customer(first_name="John", last_name="Smith")


review1 = Review(star_rating=2, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)

session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()
