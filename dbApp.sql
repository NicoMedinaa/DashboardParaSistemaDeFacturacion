CREATE DATABASE IF NOT EXISTS  Comercio;
USE Comercio;
-- Crear la tabla de Categorías
CREATE TABLE Categorías (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Descripción TEXT
);


-- Crear la tabla de Proveedores
CREATE TABLE Proveedores (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Dirección VARCHAR(255),
    Teléfono VARCHAR(15),
    Email VARCHAR(100)
);
;

-- Crear la tabla de Productos
CREATE TABLE Productos (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255) NOT NULL,
    Descripción TEXT,
    Precio DECIMAL(10, 2) NOT NULL,
    Stock INT NOT NULL,
    Categoría INT,
    Proveedor INT,
    Fecha_Lanzamiento DATE,
    Fecha_Vencimiento DATE,
    Fecha_Modificación TIMESTAMP,
    FOREIGN KEY (Categoría) REFERENCES Categorías(ID),
    FOREIGN KEY (Proveedor) REFERENCES Proveedores(ID)
);



-- Insertar una categoría
INSERT INTO Categorías (Nombre, Descripción) VALUES ('Electrónica', 'Productos electrónicos y dispositivos');

-- Insertar un proveedor
INSERT INTO Proveedores (Nombre, Dirección, Teléfono, Email) VALUES ('ElectroTec', '123 Calle Principal, Ciudad', '555-123-4567', 'info@electrotec.com');

-- Insertar un producto con fecha de vencimiento
INSERT INTO Productos (Nombre, Descripción, Precio, Stock, Categoría, Proveedor, Fecha_Lanzamiento, Fecha_Vencimiento, Fecha_Modificación) VALUES
('Producto 1', 'Descripción del producto 1', 49.99, 100, 1, 1, '2023-01-15', '2023-12-31', NOW());


INSERT INTO Categorías (Nombre, Descripción) VALUES
('Electrónica', 'Productos electrónicos y dispositivos'),
('Ropa', 'Ropa de moda para hombres y mujeres'),
('Hogar', 'Productos para el hogar y decoración');
INSERT INTO Proveedores (Nombre, Dirección, Teléfono, Email) VALUES
('ElectroTec', '123 Calle Principal, Ciudad', '555-123-4567', 'info@electrotec.com'),
('ModaStyle', '456 Avenida Central, Ciudad', '555-789-0123', 'contacto@modastyle.com'),
('CasaDecor', '789 Calle del Hogar, Ciudad', '555-234-5678', 'contacto@casadecor.com');
INSERT INTO Productos (Nombre, Descripción, Precio, Stock, Categoría, Proveedor, Fecha_Lanzamiento, Fecha_Vencimiento, Fecha_Modificación) VALUES
('Smartphone Android', 'Teléfono inteligente Android de alta gama', 599.99, 100, 1, 1, '2023-01-15', '2023-12-31', NOW()),
('Camiseta de Manga Corta', 'Camiseta de algodón para hombres, talla M', 19.99, 200, 2, 2, '2023-02-10', '2023-12-31', NOW()),
('Sofá de Cuero', 'Sofá de cuero para la sala de estar', 799.99, 10, 3, 3, '2023-03-20', '2024-03-20', NOW());
