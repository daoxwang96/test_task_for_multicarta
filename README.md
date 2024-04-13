# test_task_for_multicarta
Тестовое задание для компании "Мультикарта"

Часть Python:
1. Напишите программу на Python для проверки, является ли
число простым
2. Напишите программу на питоне, которая посчитает
количество различных(без учета регистра) букв в файле.
3. Можете написать функцию для генерации такой пирамиды?

![image](https://github.com/daoxwang96/test_task_for_multicarta/assets/166912105/ac164a5a-3184-4d66-b848-c7ab3bdd0af5)


Или такой:

![image](https://github.com/daoxwang96/test_task_for_multicarta/assets/166912105/697b0ece-b9ef-488e-ab89-51123ce30105)

P.S. Просьба написать программу оригинальную, а не из просторов сети
И с комментариями.

**

Часть SQL:

В торговой Компании эксплуатируется база данных следующей структуры (скрипты по ее созданию
приведены на второй странице задания):
![image](https://github.com/daoxwang96/test_task_for_multicarta/assets/166912105/c09947b7-1b5c-40d5-85f7-ffa06354e2f0)

Требуется с помощью SQL запросов решить следующие задачи: 

1. Планируется отослать поздравительные сообщения по электронной почте всем клиентам Компании  на 23 Февраля и 8 Марта. Требуется одним запросом определить количество сообщений, которые  нужно будет отправить отдельно 23 Февраля и 8 Марта. 
2. Вывести список заказов клиентов: [Фамилия + имя, название фирмы, дата заказа, сумма заказа], отсортированный по фамилии, имени, дате заказа. 
3. Компания намеревается ввести скидку в размере 10% от суммы заказа, если заказ выполнен в день  рождения клиента. Требуется определить общую сумму скидки по всем клиентам за 2022 год, как  если бы скидка действовала. 
4. Перед Новым 2023-м Годом решено отправить ценные подарки руководителям фирм, сотрудники  которых за год в общей сложности сделали заказов более чем на 1 000 000 руб. Необходимо  подготовить такой список: [Название фирмы, адрес, сумма заказов]. 
5. С помощью одного SQL запроса подготовить список мужчин - потенциальных близнецов среди  клиентов (с совпадением фамилии и даты рождения): [ID клиента, фамилия, имя, день рождения]. 
6. Выбрать топ-3 покупателей среди фирм (просуммировав заказы всех представителей фирмы) и  клиентов-физических лиц (у которых Firm_ID не указан) с самым большим объемом заказов за  декабрь 2022 года: [Фамилия+имя или название фирмы, сумма заказов].
   
Примечания: 

• Решая задачи, можно пользоваться любыми источниками, кроме чужого разума ☺ 

• Пожалуйста, не выкладывайте задачи в Интернет, нам не хочется придумывать новые ☺ 

Желаем Вам взлетов творческой мысли при решении задач. Удачи!

Свое решение Вы можете проверить на сайте http://sqlfiddle.com/ или https://www.db-fiddle.com/.  В решении, пожалуйста, укажите версию базы данных (желательно использовать PostgreSQL). 

Для создания тестовой базы данных (схемы) можно использовать следующий скрипт: 

CREATE TABLE Client (ID INTEGER NOT NULL PRIMARY KEY, Name varchar(50), Surname Varchar(50), Firm_ID INTEGER NULL,  Gender Varchar(1), Birthday Date, EMail Varchar(100) NULL); 

INSERT INTO Client (ID, Name, Surname, Firm_ID, Gender, Birthday, EMail) VALUES (1,'Елена', 'Сидорова', NULL, 'F',  TIMESTAMP '1993-04-05 00:00:00', 'E.Sidorova@mail.ru'); 

INSERT INTO Client (ID, Name, Surname, Firm_ID, Gender, Birthday, EMail) VALUES (2,'Петр', 'Иванов', 1, 'M',  TIMESTAMP '1990-12-02 00:00:00', 'P.Ivanov@mail.ru'); 

INSERT INTO Client (ID, Name, Surname, Firm_ID, Gender, Birthday, EMail) VALUES (3,'Aннa', 'Петрова', 1, 'F',  TIMESTAMP '1993-05-13 00:00:00', 'A.Petrova@mail.ru'); 

INSERT INTO Client (ID, Name, Surname, Firm_ID, Gender, Birthday, EMail) VALUES (4,'Иван', 'Иванов', 1, 'M',  TIMESTAMP '1990-12-02 00:00:00', NULL); 

INSERT INTO Client (ID, Name, Surname, Firm_ID, Gender, Birthday, EMail) VALUES (5,'Даниил','Пупкин', 2, 'M',  TIMESTAMP '1991-12-05 00:00:00', NULL); 

INSERT INTO Client (ID, Name, Surname, Firm_ID, Gender, Birthday, EMail) VALUES (6,'Янина', 'Котикова', NULL, 'F',  TIMESTAMP '1991-10-20 00:00:00', 'Koteiko@mail.ru'); 

INSERT INTO Client (ID, Name, Surname, Firm_ID, Gender, Birthday, EMail) VALUES (7,'Ян', 'Шнайдмиллер', 2, 'M',  TIMESTAMP '1990-12-02 00:00:00', 'ya.shnaid@mail.ru'); 

INSERT INTO Client (ID, Name, Surname, Firm_ID, Gender, Birthday, EMail) VALUES (8,'Георг', 'Иванов', NULL, 'M',  TIMESTAMP '1995-11-02 00:00:00', NULL); 

CREATE TABLE Firm (ID INTEGER NOT NULL PRIMARY KEY, Name varchar(100), Address Varchar(100)); 

INSERT INTO Firm (ID, Name, Address) VALUES(1, 'ООО "Рога & Копыта"', 'Барнаул, ул. Кривая, 2'); 

INSERT INTO Firm (ID, Name, Address) VALUES(2, 'ПАО "Копыта & Рога"', 'Барнаул, ул. Ровная, 5'); 

CREATE TABLE Orders (ID INTEGER NOT NULL PRIMARY KEY, Ord_Time Date NOT NULL, Amount INTEGER NOT NULL, Client_ID  INTEGER NOT NULL); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (1, TIMESTAMP '2022-12-01 11:35:45', 115000, 1); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (2, TIMESTAMP '2022-12-02 12:25:56', 307000, 1); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (3, TIMESTAMP '2022-12-02 13:15:07', 350000, 2); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (4, TIMESTAMP '2022-12-03 14:05:18', 670000, 1); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (5, TIMESTAMP '2022-12-04 15:55:29', 70000, 3); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (6, TIMESTAMP '2022-12-04 16:45:30', 150000, 4); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (7, TIMESTAMP '2022-12-05 17:35:41', 250000, 5); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (8, TIMESTAMP '2022-12-06 18:25:52', 650000, 2); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (9, TIMESTAMP '2022-12-06 19:15:03', 450000, 6); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (10, TIMESTAMP '2023-01-10 19:15:03', 37000, 6); 

INSERT INTO Orders (ID, Ord_Time, Amount, Client_ID) VALUES (11, TIMESTAMP '2023-01-11 10:15:03', 29000, 7); 

COMMIT;



