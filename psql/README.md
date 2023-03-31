# Slash commands
* \l - список всех бд
* \c - показывает через какого юзера и к какой бд мы подключены
* \c name_of_db - подключаемся к какой-то бд
* \du - список всех юзеров в postges


# Создание бд и таблиц
``` sql
CREATE DATABASE name_of_db;
- создание база данных
``` 

``` sql
CREATE TABLE name_of_table (
    column1 data_type1,
    column2 data_type2,
    ...
);


# alter user name_user with superuser 
#даем какой - то супер права юзеру


# grant all privileges on database name_of_database to name_user
даем привилегии хуй пойми какие нашему юзеру

# 
-- создание таблицы с полями
```
1 -- atomicity
2 -- consistency
3 -- isolation
4 -- durability

--  psql postgres
вход в psql

# чтобы поставить пароль для юзера - create user (название бд) with password ''
# чтобы дать права user и обьезательно прописываем какие это права (например):
alter role (название бд) with superuser(мы дали права на)






## ПОЧЕМУ Ж В БАЗЕ ДАННЫХ НЕКОТОРЫЕ СЛОВА С БОЛЬЩЫМИ БУКВАМИ СПРОСИШЬ ТЫ АМИНА?
## BECAUSE - НЕ ПУТАТЬСЯ ГДЕ КЛЮЧЕВЫЕ КОМАНДЫ А ГДЕ ПРОСТО СЛОВА
# VALUES - Клюевое слово
delete product where price = 100; - удаление всех
записей из таблицы который подходит под нашу
условие(100)


# Создание бд и таблиц

* CREATE DATABASE name_of_db;
-- создает базу данных
* CREATE TABLE name_of_table (
    column1 data_type1,
    column2 data_type2,
    ...
);
-- создает таблицу с полями
DROP DATABASE name_of_db;
-- удаление бд
DROP TABLE name_of_table;
-- удаление таблицы
Заполнение таблиц

``` sql
INSERT INTO name_of_table VALUES 
(val1, val2), 
(val2.1, val2.2);
-- запись данных в таблицу (заполнение всех полей)
INSERT INTO name_of_table (column1, column2) VALUES
(val1.1, val1.2),
(val2.1, val2.2);
``` 

-- запись определенных полей в таблицу 
Вывод данных из таблицы

``` sql
SELECT * FROM name_of_table;
-- получение всех записей с таблицы (всех полей) 
Удаление записей из таблицы

DELETE FROM name_of_table;
-- удаление всех записей из таблицы
Обновление записей в таблице

UPDATE name_of_table SET col = new_val;
-- обновление всех записей в таблице
UPDATE name_of_table SET col = new_val WHERE id < 10;
-- обновление нескольких записей


# Условия
DELETE FROM name_of_table WHERE column1 = value1;
-- удаление всех записей соответствующих этому условию
SELECT * FROM name_of_table WHERE title like '%world%';
-- выбирает все записи у которых в поле title есть названия содержащие world
-- hello world
-- world
-- world hello


``` sql
SELECT * FROM name_of_table WHERE column = 'hello';
-- cтрогое равенство
```



``` sql
# (короче ilike и like чаше используется в поиске в таблице)
-- like - чувствительный к регистру (World - не пройдет)
SELECT * FROM name_of_table WHERE title ilike '%world%';
-- ilike - не чувствительный к регистру
-- WORLD
-- World
-- worLD
-- hello World
-- world Hello
-- HEllo WORLD hello
SELECT * FROM name_of_table ORDER BY column1;
-- сортировка по определенному полю (по возрастанию ASC)
 SELECT * FROM name_of_table ORDER BY column1 DESC;
-- сортировка по определенному полю (по убыванию DESC)
SELECT * FROM name_of_table LIMIT 10;
-- выводит первые 10 записей
# select * from product  where id > 4 limit 3;
(тут я поставила условие если айдишка больше 4 - букв вытащи мне 3 таких продуктов)
SELECT * FROM name_of_table OFFSET 10;
-- пропускает первые 10 записей
SELECT * FROM name_of_table LIMIT 5 OFFSET 10;
-- пропускает первые 10 записей
-- выбирает следующие 5 записей



# Ограничение 

``` 
# Связи

pk fk

* * PRIMARY KEY (pk) - первичный ключ, ограничение, которое накладывается на поле, которое будет использованно в связях (создаетbtree для быстрого поиска) 
как UNIQUE и NOT NULL+ строит binary tree для быстрого поиска



* * FOREIGN KEY (fk) - внешний ключ, ограничение, которое накладывается на поле, которое ссылается на pk в другой таблице
и проверяет сущ ли такой id

``` sql
CREATE TABLE blogger (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    body text,
    blogger_id INT,

    CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id)
    REFERENCES blogger (id)
);
``` 
## реализация one2many в postgres


##  Виды связей

> One to one - один к одному
* один человек - один ID
* один автор - одна автобиография

> One to many - один ко многим
* один блоггер - много постов
* один куратор - много студентов
* один продукт - много комментариев


> Many to many - многие ко мгногим
* один ментор - много студентов. один студент - много менторов
* один разработчик - много проектов. один проект - много разработчиков
* один банк - много клиентов. один клиент - много банков


Виды связей (практика)
# One to one:
``` sql
CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

CREATE TABLE autobiography (
    id SERIAL PRIMARY KEY,
    body TEXT,
    created_at DATE,
    author_id INT UNIQUE, -- unique мы ставим, чтобы сделать one 2 one

    CONSTRAINT fk_author_bio 
    FOREIGN KEY (author_id) REFERENCES author (id)
);
```
## One to Many
``` sql
CREATE TABLE curator (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    language VARCHAR(2),
    curator_id INT,

    CONSTRAINT fk_student_curator
    FOREIGN KEY (curator_id) REFERENCES curator (id)
);

```
# Many to Many
```sql
CREATE TABLE developer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    experience INT
);

CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    tz TEXT,
    start DATE,
    finish DATE
);

CREATE TABLE dev_proj (
    dev_id INT,
    proj_id INT,

    CONSTRAINT fk_dev FOREIGN KEY (dev_id) REFERENCES developer (id),
    CONSTRAINT fk_proj FOREIGN KEY (proj_id) REFERENCES project (id)
);
```

## Joins

- - JOIN - инструкция, которая позволяет в запросах SELECT брать данные из нескольких таблиц
INNER JOIN (JOIN) - достаются только те записи, у которых есть связь
FULL JOIN - достаются все записи с обеих таблиц
LEFT JOIN - достает все записи с левой таблицы, и с правой таблицы у которых есть связь с левой таблицей
RIGHT JOIN - достает все записи с правой таблицы, и с левой таблицы у которых есть связь с правой таблицей
где 'левая' таблица - та, которая написана до join а 'правая' таблица - та, которая написана после join
Практика

blog
``` sql
-- создание таблиц
CREATE TABLE blogger (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    blogger_id INT,
    body TEXT,
    created_at DATE,

    CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);



``` sql
SELECT * FROM table1 JOIN table2 ON table1.id = table2.t_id;





-- заполнение таблиц
``` sql
INSERT INTO blogger (name) VALUES ('blogger 1'), ('blogger 2'), ('blogger 3'); 

INSERT INTO post (blogger_id, body, created_at) VALUES
(1, 'my first blog', '01.08.2020'),
(1, 'today is a good day', '02.09.2020'),
(1, 'it is my b-day!', '30.09.2021');

INSERT INTO post (blogger_id, body, created_at) VALUES
(2, 'my first post', '10.05.2013'),
(2, 'some post', '23.06.2022');

INSERT INTO post (blogger_id, body, created_at) VALUES
(3, 'i am not a blogger', '15.08.2022');
shop

-- создание таблиц
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    price DECIMAL
);

CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,

    CONSTRAINT cart_customer FOREIGN KEY (customer_id) REFERENCES customer (id), 
    CONSTRAINT cart_product FOREIGN KEY (product_id) REFERENCES product (id)
);

-- заполнение таблиц
INSERT INTO customer (name) VALUES ('customer 1'), ('customer 2'), ('customer 3'); 

INSERT INTO product (title, price) VALUES
('product 1', 340),
('product 2', 503),
('product 3', 470),
('product 4', 236),
('product 5', 452);

INSERT INTO cart (customer_id, product_id) VALUES
(1, 1), (1, 2), (1, 4),
(2, 3),
(3, 4), (3, 5);


# Агрегатные функции
> все агрегатные функции мы используем с 'group by'

SUM - функция, считающая сумму всех записей в сгруппированном поле
> до это у нас была такая таблица с продуктами:
--  id |   title   | price | id | customer_id | product_id | id |    name    
-- ----+-----------+-------+----+-------------+------------+----+------------
--   1 | product 1 |   340 |  1 |           1 |          1 |  1 | customer 1
--   2 | product 2 |   503 |  2 |           1 |          2 |  1 | customer 1
--   4 | product 4 |   236 |  3 |           1 |          4 |  1 | customer 1
--   3 | product 3 |   470 |  4 |           2 |          3 |  2 | customer 2
--   4 | product 4 |   236 |  5 |           3 |          4 |  3 | customer 3
--   5 | product 5 |   452 |  6 |           3 |          5 |  3 | customer 3

> достаем сумму
-- пример из shop
-- SELECT customer.name, SUM(product.price) FROM customer
--  JOIN cart ON customer.id = cart.customer_id
-- JOIN product ON product.id = cart.product_id
-- shop-# GROUP BY (customer.id);
--     name    | sum  
-- ------------+------
--  customer 2 |  470
--  customer 3 |  688
--  customer 1 | 1079
-- (3 rows)


-- среднее значение:
> **AVG** - считает среднее значение всех записей в сгруппированном поле

shop=# SELECT customer.name, AVG(product.price) FROM customer
 JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart.product_id
GROUP BY (customer.id);
    name    |         avg          
------------+----------------------
 customer 2 | 470.0000000000000000
 customer 3 | 344.0000000000000000
 customer 1 | 359.6666666666666667
(3 rows)



-- чтобы округлить:
shop=# SELECT customer.name, ROUND(AVG(product.price),2) FROM customer
 JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart.product_id
GROUP BY (customer.id);
    name    | round  
------------+--------
 customer 2 | 470.00
 customer 3 | 344.00
 customer 1 | 359.67
(3 rows)



ARRAY_AGG - обьединяет записи сгрупированного поля в массив
-- пример из blog
-- до этого  у нас было так:
   name    |        body         
-----------+---------------------
 blogger 1 | my first blog
 blogger 1 | today is a good day
 blogger 1 | it is my b-day!
 blogger 2 | my first post
 blogger 2 | some post
 blogger 3 | i am not a blogger
(6 rows)

SELECT blogger.name, ARRAY_AGG(post.body) AS posts
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);
   name    |                         array_agg                         
-----------+-----------------------------------------------------------
 blogger 1 | {"my first blog","today is a good day","it is my b-day!"}
 blogger 2 | {"my first post","some post"}
 blogger 3 | {"i am not a blogger"}
(3 rows)



# # MIN, MAX - высчитывают минимальное и максимальное значение среди записей в сгруппированном поле
-- пример из post


``
SELECT blogger.name, MIN(post.created_at) AS first, MAX(post.created_at) AS last
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);
--    name    |   first    |    last    
-- -----------+------------+------------
--  blogger 2 | 2013-05-10 | 2022-06-23
--  blogger 1 | 2020-08-01 | 2021-09-30
--  blogger 3 | 2022-08-15 | 2022-08-15


COUNT - считает кол-во записей в сгруппированном поле
-- пример из blog
SELECT blogger.name, COUNT(post.id) AS posts_count
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);
--    name    | posts_count 
-- -----------+-------------
--  blogger 2 |           2
--  blogger 1 |           3
--  blogger 3 |           1


ORDER BY (blogger.name) -- отсортирует по имени:

SELECT blogger.name, COUNT(post.id) AS posts_count
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name) ORDER BY (blogger.name);
   name    | posts_count 
-----------+-------------
 blogger 1 |           3
 blogger 2 |           2
 blogger 3 |           1
(3 rows)


Изменение таблиц
``

* ALTER TABLE name_of_table ADD COLUMN col_name type constraint;
-- добавляет новую колонку в таблицу
ALTER TABLE name_of_table DROP COLUMN col_name;
-- удаляет колонку из таблицы
ALTER TABLE name_of_table ADD CONSTRAINT constr_name constraint;
-- добавление ограничения на поле
ALTER TABLE test ADD CONSTRAINT col_unq UNIQUE (col);
-- test - название таблицы
-- col - название поля
ALTER TABLE test ADD CONSTRAINT fk_test_test2 FOREIGN KEY (test2_id) REFERENCES test2 (id);
ALTER TABLE name_of_table RENAME COLUMN old_name TO new_name;
-- переименовать поле
ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_data_type;

ALTER TABLE name_of_table ALTER COLUMN col_name TYPE new_data_type;
-- изменение типа данных у поля


-- команды для экспорта(файла импортировать) в терминале:
brew install libpq
echo 'export PATH="/usr/local/opt/libpq/bin:$PATH"' >> ~/.zshrc
pg_dump


Import / export баз данных

write from file to db

psql db_name < file.sql
# db_name должна существовать в postgresql


write from db to file
# pg_dump db_name > file.sql
-- тут суш баз д записываем файл, но не об чтоб баз.д существовала


## Разбор с лекции
# функционал psql
1 -- atomicity
2 -- consistency
3 -- isolation
4 -- durability

--  psql postgres
вход в psql

# создание бд - create database название бд;
# удаление бд - drop database название бд;
#  увидеть список бд  - \ l 
# чтобы зайти (коннект) с бд - \c название бд (не нужно ставить двойные точки)
# чтобы увидеть всех user - \du
# чтобы поставить пароль для юзера - create user (название бд) with password ''
# чтобы дать права user и обьезательно прописываем какие это права (например):
alter role (название бд) with superuser(мы дали права на)






## ПОЧЕМУ Ж В БАЗЕ ДАННЫХ НЕКОТОРЫЕ СЛОВА С БОЛЬЩЫМИ БУКВАМИ СПРОСИШЬ ТЫ АМИНА?
## BECAUSE - НЕ ПУТАТЬСЯ ГДЕ КЛЮЧЕВЫЕ КОМАНДЫ А ГДЕ ПРОСТО СЛОВА



## Для чего VARCHAR?
При использовании char или varchar рекомендуется: Если размеры записей данных столбцов постоянны, используйте char. Если размеры записей данных столбцов значительно изменяются, используйте varchar


-- shop=# SELECT * FROM product JOIN cart on product.id = cart.product_id
-- JOIN customer on customer.id = cart.customer_id;
--  id |   title   | price | id | customer_id | product_id | id |    name    
-- ----+-----------+-------+----+-------------+------------+----+------------
--   1 | product 1 |   340 |  1 |           1 |          1 |  1 | customer 1
--   2 | product 2 |   503 |  2 |           1 |          2 |  1 | customer 1
--   4 | product 4 |   236 |  3 |           1 |          4 |  1 | customer 1
--   3 | product 3 |   470 |  4 |           2 |          3 |  2 | customer 2
--   4 | product 4 |   236 |  5 |           3 |          4 |  3 | customer 3
--   5 | product 5 |   452 |  6 |           3 |          5 |  3 | customer 3
-- (6 rows)


-- корзина где хранятся продукты