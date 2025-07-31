-- Create the database
CREATE DATABASE IF NOT EXISTS stylehub_tshirts;
USE stylehub_tshirts;

-- Create t_shirts table
CREATE TABLE t_shirts (
    t_shirt_id INT AUTO_INCREMENT PRIMARY KEY,
    brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas', 'Puma', 'Tommy Hilfiger') NOT NULL,
    color ENUM('Red', 'Blue', 'Black', 'White', 'Green', 'Yellow') NOT NULL,
    size ENUM('XS', 'S', 'M', 'L', 'XL', 'XXL') NOT NULL,
    price DECIMAL(10,2) CHECK (price BETWEEN 10 AND 100),
    stock_quantity INT NOT NULL,
    UNIQUE KEY brand_color_size (brand, color, size)
);

-- Create discounts table
CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    t_shirt_id INT NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100),
    FOREIGN KEY (t_shirt_id) REFERENCES t_shirts(t_shirt_id)
);

-- Insert sample data
INSERT INTO t_shirts (brand, color, size, price, stock_quantity) VALUES
('Nike', 'White', 'XS', 24.99, 91),
('Levi', 'Black', 'S', 19.99, 15),
('Adidas', 'White', 'XS', 14.99, 55),
('Puma', 'Blue', 'M', 29.99, 40),
('Tommy Hilfiger', 'Red', 'L', 49.99, 25);

INSERT INTO discounts (t_shirt_id, pct_discount) VALUES
(1, 10.00),
(2, 15.00),
(3, 20.00),
(4, 5.00),
(5, 25.00);