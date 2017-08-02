from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Website, User

engine = create_engine('postgresql://item:sillypassword@localhost/item')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Omar Mansour", email="omar.ad.mansour@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Websites for politcs
politcs = Category(user_id=1, name="Politcs")

session.add(politcs)
session.commit()

pltcsWeb1 = Website(user_id=1, name="Mada Masr", url="https://www.madamasr.com",
                     description="Egypt-based media organization interested in producing intelligent and engaging journalism, and more generally in re-examining the role of media in relation to its public.",
                     category=politcs)
session.add(pltcsWeb1)
session.commit()

pltcsWeb1 = Website(user_id=1, name="Sasa Post", url="https://www.sasapost.com",
                     description="Egypt-based media organization interested in producing intelligent and engaging journalism, and more generally in re-examining the role of media in relation to its public.",
                     category=politcs)
session.add(pltcsWeb1)
session.commit()

# Websites for Business
business = Category(user_id=1, name="Business")

session.add(business)
session.commit()

bsnsWeb1 = Website(user_id=1, name="Al Borsa News", url="https://alborsanews.com",
                     description=" Al Borsa News is a completely independent news provider for Egypt and the wider MENA region.",
                     category=business)
session.add(bsnsWeb1)
session.commit()


# Websites for Sports
sports = Category(user_id=1, name="Sports")

session.add(sports)
session.commit()

sporWeb1 = Website(user_id=1, name="YallaKora", url="http://www.yallakora.com",
                     description="Yallakora.com the leading sports portal in Egypt, delivers the best in sports with quick access to the latest scores, standings, videos, Galleries and detailed matches coverage",
                     category=sports)
session.add(sporWeb1)
session.commit()



# Websites for Arts
arts = Category(user_id=1, name="Arts")

session.add(arts)
session.commit()

artsWeb1 = Website(user_id=1, name="Arageek", url="https://www.arageek.com",
                     description="Arageek.com is the leading internet magazine and the destination for premium quality Arabic content in the Arab world, covering various topic from apps, smart phones tutorials to infotainment, technology, social, business tips and news. ",
                     category=arts)
session.add(artsWeb1)
session.commit()


print "added Websites!"
