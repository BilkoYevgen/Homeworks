SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases FROM purchases
INNER JOIN users ON purchases.user_id = users.id
INNER JOIN books ON books.id = purchases.book_id
GROUP BY purchases.user_id;