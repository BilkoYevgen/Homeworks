SELECT books.title, COUNT(purchases.book_id) AS sells_amount FROM books
LEFT JOIN purchases ON books.id = purchases.book_id
GROUP BY books.id
ORDER BY sells_amount DESC