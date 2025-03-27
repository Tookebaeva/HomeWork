CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
);




INSERT INTO categories (code, title) VALUES
('FD', 'Food products'),
('EL', 'Electronics'),
('CL', 'Clothing');

CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL
);

INSERT INTO stores (title) VALUES
('Asia'),
('Globus'),
('Spar');



CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(250) NOT NULL,
    category_code VARCHAR(2) NOT NULL,
    unit_price FLOAT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER NOT NULL,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);







INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id) VALUES
('chocolate', 'FD', 10.5, 129, 1),
('laptop', 'EL', 750.0, 15, 2),
('T-Shirt', 'CL', 20.0, 50, 3),
('bread', 'FD', 2.0, 200, 1),
('smartphone', 'EL', 500.0, 10, 2),
('jeans', 'CL', 45.0, 30, 3);
('egg', 'FD', 2.0, 100, 10),
('phone', 'EL', 300.0, 10, 2),
('dress', 'CL', 45.0, 30, 3);
