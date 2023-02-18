SELECT purchases.id, purchases.date, users.first_name, users.last_name FROM purchases
INNER JOIN users ON purchases.user_id = users.id;