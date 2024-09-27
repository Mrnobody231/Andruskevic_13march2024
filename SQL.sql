SELECT DISTINCT product_name
FROM Products

SELECT p.product_id, p.product_name, p.price
FROM Products AS p
JOIN Nutritional_Information AS n ON p.product_id = n.product_id
WHERE n.fiber > 5

SELECT p.product_name
FROM Products AS p
JOIN Nutritional_Information AS n ON p.product_id = n.product_id
ORDER BY n.protein DESC
LIMIT 1

SELECT p.category_id, SUM(p.calories) 
FROM Products AS p
JOIN Nutritional_Information AS n ON p.product_id = n.product_id
WHERE n.fat > 0
GROUP BY p.category_id

SELECT c.category_name, AVG(p.price) 
FROM Products AS p
JOIN Categories AS c ON p.category_id = c.category_id
GROUP BY c.category_name