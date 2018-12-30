from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///catalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
user1 = User(name="Marvin", email="marvin@mbm.com",
             picture='http://placekitten.com/400/400')
session.add(user1)
session.commit()

# Items for Doctor
category1 = Category(name="Doctor", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Bad News", user_id=1, description="Doctor: I have good news and bad news", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="At the Pharmacy", user_id=1,  description="Woman: Can I get Viagra here? Pharmacist: Maybe.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Dental Plan", user_id=1, description="I finally got dental plan. I chew the other side.", category=category1)

session.add(item3)
session.commit()

# Items for Food
category2 = Category(name="Food", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Beer Nuts vs Deer Nuts", user_id=1, description="Beer nuts are 1.39, deer nuts are under a buck.", category=category2)

session.add(item1)
session.commit()

# Items for Kids
category3 = Category(name="Kids", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="A joke of genius", user_id=1, description="Do these genes make my butt look fat.", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Musical Chairs", user_id=1, description="Q: What did one chair say to another chair?", category=category3)

session.add(item2)
session.commit()

# Items for Marriage
category4 = Category(name="Marriage", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Modern Science", user_id=1, description="What food diminishes a womans sex drive by 90%?", category=category4)

session.add(item1)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name