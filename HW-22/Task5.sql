SELECT count(*) AS amount FROM purchases
INNER JOIN books on books.id = purchases.book_id
WHERE author = 'Rowling'