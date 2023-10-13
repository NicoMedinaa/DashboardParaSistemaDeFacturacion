CREATE DATABASE IF NOT EXISTS  Comercio;
USE Comercio;
-- Crear la tabla de categoria
CREATE TABLE categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);


-- Crear la tabla de proveedor
CREATE TABLE proveedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100)
);
;

-- Crear la tabla de productos
CREATE TABLE productos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    categoria INT,
    proveedor INT,
    fecha_lanzamiento DATE,
    fecha_vencimiento DATE,
    fecha_modificacion TIMESTAMP,
    FOREIGN KEY (categoria) REFERENCES categoria  (id) ,
    FOREIGN KEY (proveedor) REFERENCES proveedor  (id)
);


INSERT INTO categoria( nombre, descripcion) VALUES
('Electrónica', 'productos electrónicos y dispositivos'),
('Alimentos', 'productos de alimentos'),
('Ropa', 'Ropa de moda para hombres y mujeres'),
('Hogar', 'productos para el hogar y decoración');
INSERT INTO proveedor(nombre, direccion, telefono, email) VALUES
('ElectroTec', '123 Calle Principal, Ciudad', '555-123-4567', 'info@electrotec.com'),
('ModaStyle', '456 Avenida Central, Ciudad', '555-789-0123', 'contacto@modastyle.com'),
('CasaDecor', '789 Calle del Hogar, Ciudad', '555-234-5678', 'contacto@casadecor.com');
INSERT INTO productos(nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion) VALUES
('Smartphone Android', 'telefono inteligente Android de alta gama', 599.99, 100, 1, 1, '2023-01-15', '2023-12-31', NOW()),
('Camiseta de Manga Corta', 'Camiseta de algodón para hombres, talla M', 19.99, 200, 2, 2, '2023-02-10', '2023-12-31', NOW()),
('Sofá de Cuero', 'Sofá de cuero para la sala de estar', 799.99, 10, 3, 3, '2023-03-20', '2024-03-20', NOW());
