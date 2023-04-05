from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# driver://user:password@host:port/db_name как мы прописываем:
db_url = 'postgresql://Amina:1@127.0.0.1:5432/sqlalchemy_test'
engine = create_engine(db_url)
# подключение к базе данных
Base = declarative_base()
# базовый класс для таблиц

class Product(Base):
    __tablename__ = 'product'  #название таблички(встроенная)
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)



    def __repr__(self) -> str:
        return f"({self.id} -> {self.title})"

Base.metadata.create_all(bind=engine)
#записываем таблицу в бд

SessionLocal = sessionmaker(bind=engine)
# мы создаем класс для сессий(один обьект от одного класса открывает одну сессию)

session = SessionLocal()
# создаем сессию

new_product = Product(title='product1', price=120)
#создаем продукт(запись в таблицу)
# для орм создаем запрос на запись в таблицу

# session.add(new_product)
# # добавляем запрос в сессию

# session.commit()
#отправляем набор запросов бд

# products = session.query(Product).all()
# # получаем все записи из таблицы product
# print(products)

# session.add(Product(title='product2',price=34))
# session.add(Product(title='product3',price=300))
# session.add(Product(title='product4',price=365))
# session.add(Product(title='product5',price=790))
# session.add(Product(title='product6',price=100))
# session.commit()
products = session.query(Product).all()
# получаем все записи из таблицы product
print(products)
#[(1 -> product1), (2 -> product2), (3 -> product3), (4 -> product4), (5 -> product5), 
# (6 -> product6), (7 -> product2), (8 -> product3), (9 -> product4), (10 -> product5), 
# (11 -> product6), (12 -> product2), (13 -> product3), (14 -> product4), (15 -> product5), (16 -> product6)]

res =session.query(Product).filter(Product.price > 100).all()
#получаем все записи из таблицы product у которых цена больще 100
print(res)
product3 = session.query(Product).get(3)
#получаем продукт под id 3
print(product3)   #(3 -> product3)

product4 = session.query(Product).get(4)
# session.delete(product4)   #удаляем 4 продукт
# session.commit()  #сохраняем изменение в бд
# мы удалили:
#  id |  title   | price 
# ----+----------+-------
#   1 | product1 |   120
#   2 | product2 |    34
#   3 | product3 |   300
#   5 | product5 |   790
#   6 | product6 |   100
#   7 | product2 |    34
#   8 | product3 |   300
#   9 | product4 |   365
#  10 | product5 |   790
#  11 | product6 |   100
#  12 | product2 |    34
#  13 | product3 |   300
#  14 | product4 |   365
#  15 | product5 |   790
#  16 | product6 |   100
# (15 rows)

product3.title = 'new title'
product3.price = 100
# изменяем продукт
session.commit()
#сохраняем изменение
#  id |   title   | price 
# ----+-----------+-------
#   1 | product1  |   120
#   2 | product2  |    34
#   5 | product5  |   790
#   6 | product6  |   100
#   7 | product2  |    34
#   8 | product3  |   300
#   9 | product4  |   365
#  10 | product5  |   790
#  11 | product6  |   100
#  12 | product2  |    34
#  13 | product3  |   300
#  14 | product4  |   365
#  15 | product5  |   790
#  16 | product6  |   100
#   3 | new title |   100
# (15 rows)
