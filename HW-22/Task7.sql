SELECT books.author, SUM(books.price) AS total_earned, COUNT(purchases.user_id) AS sells_amount
FROM purchases
JOIN books ON purchases.book_id = books.id
GROUP BY books.author;

