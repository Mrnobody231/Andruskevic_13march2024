1. Список уникальных классов. Вывести только названия
SELECT DISTINCT class_name
FROM visits;

2. Количество часов, проведенных на занятиях для каждого пользователя. 
Вывести фамилию, имя и количество часов.
SELECT u.user_surname, u.user_name, SUM(v.hours_spent)
FROM user AS u
JOIN visits AS v ON u.id_user = v.id_user
GROUP BY u.user_surname, u.user_name;

3. Средний возраст пользователей, посещающих класс Flex.
SELECT AVG(u.age)
FROM user AS u
JOIN visits AS v ON u.id_user = v.id_user
WHERE v.class_name = 'Flex';

4. Вывести пользователей, которые ни разу не посещали бассейн (Swimming pool).
SELECT u.user_name, u.user_surname 
FROM users AS u
Left JOIN visits AS v ON u.id_user = v.id_user AND v.class_name = 'Swimming pool'
WHERE v.id_user IS NULL;