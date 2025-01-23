from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime
import faker

# Initialize Faker for random data generation
fake = faker.Faker()

# Define the base class for models
Base = declarative_base()

# Define the Article model
class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(Integer, nullable=False)
    user_id = Column(String(255), nullable=False)
    ipaddr = Column(String(255), nullable=False)
    context = Column(String(255))
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, onupdate=datetime.utcnow)


# 创建一个引擎，目的是连接到我们的数据库上
engine = create_engine("mysql+pymysql://root:root@192.168.101.63:3306/flask_db", echo=True)

# 创建一个 sessionmaker，并绑定到引擎
Session = sessionmaker(bind=engine)

# 使用 scoped_session 保证线程安全
db_session = scoped_session(Session)

# Generate and insert 100 rows into the table
for article_id in range(1, 101):
    user_id = f"user_{article_id:03d}"
    ipaddr = fake.ipv4()
    context = f"Sample article content {article_id}"
    create_time = datetime.now()
    update_time = None  # NULL for new rows

    # 获取 session 对象
    session = db_session()

    # Create an Article instance
    article = Article(
        article_id=article_id,
        user_id=user_id,
        ipaddr=ipaddr,
        context=context,
        create_time=create_time,
        update_time=update_time
    )

    # Add the article to the session
    session.add(article)

    # Commit the transaction to save the data
    session.commit()

    # Close the session
    session.close()

# Close the db_session (important for scoped sessions)
db_session.remove()

print("100 rows have been inserted successfully.")
