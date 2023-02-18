CREATE TABLE users (
  id INT NOT NULL ,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  age INT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE publishing_house (
  id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  rating INT DEFAULT 5,
  PRIMARY KEY (id)
);

CREATE TABLE books (
  id INT NOT NULL,
  title VARCHAR(100) NOT NULL,
  author VARCHAR(100) NOT NULL,
  year INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  publishing_house_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (publishing_house_id) REFERENCES publishing_house(id)
);

CREATE TABLE purchases (
  id INT NOT NULL,
  user_id INT NOT NULL,
  book_id INT NOT NULL,
  date NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (book_id) REFERENCES books(id)
);