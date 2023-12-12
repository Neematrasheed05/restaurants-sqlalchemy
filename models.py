from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,session
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())
    reviews = relationship('Review', back_populates='restaurant')
    
    def __repr__(self):
        return f'Restaurant{self.id},'+\
            f'name{self.name},'+\
            f'price{self.price})'
    
    def all(self):
        reviews = []
        for review in self.reviews:
            customer_name = f"{review.customer.first_name} {review.customer.last_name}"
            review_text = f"{self.name}: {customer_name}: {review.star_rating}"
            reviews.append(review_text)
        return reviews
    def fancy(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    reviews = relationship('Review', back_populates='customer')

    def __repr__(self):
        return f'Customer{self.id},'+\
            f'first_name{self.first_name},'+\
            f'last_name{self.last_name})'
    def full_name(self):
        return f'{self.first_name}{self.last_name}'
        
    def favorite(self):
        
        customer_reviews = [review for review in self.reviews]
        
        if customer_reviews:
            highest_rated_review = max(customer_reviews, key=lambda x: x.star_rating)
            return highest_rated_review.restaurant
        else:
            return None 
        
    def add(self, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        session.add(new_review)
        session.commit()

    def delete(self, restaurant):
        reviews_to_delete = session.query(Review).filter_by(customer_id=self.id, restaurant_id=restaurant.id).all()
        
        
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

    
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def __repr__(self):
        return f'Review(id={self.id},'+\
            f'star_rating={self.star_rating})'
   
    def full_review(self):
        customer_name = f"{self.customer.first_name} {self.customer.last_name}"
        return f"Review for {self.restaurant.name} by {customer_name}: {self.star_rating} stars"