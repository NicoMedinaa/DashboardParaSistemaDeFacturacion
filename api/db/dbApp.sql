CREATE DATABASE IF NOT EXISTS  sistemaFacturacion;
USE sistemaFacturacion;
-- Crear la tabla de empresa la cual va a adquirir nuestro sistema
CREATE TABLE empresa ( --- dejar solo empresa para el registro de usuario
    nombre VARCHAR(50) PRIMARY KEY NOT NULL,
    direccion VARCHAR(255) NOT NULL, 
    telefono VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    fechaIngreso DATE NOT NULL, --NOW
    CUIT_CUIL VARCHAR(12) NOT NULL UNIQUE KEY
    FOREIGN KEY (nombre) REFERENCES user(nombre),
    password VARCHAR(255) NOT NULL,
);

-- Crear la tabla de categoria
CREATE TABLE categoria (
    nombre VARCHAR(50) PRIMARY KEY NOT NULL, 
    descripcion TEXT
);

-- Crear la tabla de proveedor
CREATE TABLE proveedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) UNIQUE KEY NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    descripcion TEXT
);

INSERT INTO proveedor (descripcion, direccion, email, nombre, telefono)
VALUES (
  'Proveedor de productos A',
  'Calle Proveedor 1',
  'proveedor1@example.com',
  'Proveedor 1',
  '111-222-3333'
);

INSERT INTO proveedor (descripcion, direccion, email, nombre, telefono)
VALUES (
  'Proveedor de productos B',
  'Avenida Proveedor 2',
  'proveedor2@example.com',
  'Proveedor 2',
  '444-555-6666'
);


-- Crear la tabla de cliente
CREATE TABLE cliente (
    dni INT(9) PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fechaRegistro DATE NOT NULL
);
-- Crear la tabla de factura
CREATE TABLE factura (
    numeroFactura INT PRIMARY KEY NOT NULL,
    cliente INT(9),
    subtotal DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    impuestos DECIMAL(10, 2) NOT NULL,
    metodoPago VARCHAR(50),
    descripcion VARCHAR(255),
    fechaEmision DATE NOT NULL,
    fechaVencimiento DATE NOT NULL,
    FOREIGN KEY (cliente) REFERENCES cliente(dni)
);

-- Crear la tabla de servicios
CREATE TABLE servicios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    categoria VARCHAR(50),
    empresa VARCHAR(50),
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    duracion INT,
    unidadMedida VARCHAR(5),
    fechaInicio DATE NOT NULL,
    fechaFinalizacion DATE NOT NULL,
    fechaCreacion DATE TIMESTAMP, --now
    fechaModificacion TIMESTAMP, -- now and update
    estado VARCHAR(10),
    FOREIGN KEY (empresa) REFERENCES empresa(nombre),
    FOREIGN KEY (categoria) REFERENCES categoria(nombre)

);

-- Crear la tabla de productos le pones una id unica y auto incremental para evitar conflitos en la carda de datos sin repeticion.
CREATE TABLE productos (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    codigo_barra VARCHAR(255),
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    categoria VARCHAR(50),
    proveedor VARCHAR(50),
    fecha_lanzamiento DATE,
    fecha_vencimiento DATE,
    fecha_modificacion TIMESTAMP,
    empresa VARCHAR(50),
    FOREIGN KEY (categoria) REFERENCES categoria(nombre) ,
    FOREIGN KEY (empresa) REFERENCES empresa(nombre),
    FOREIGN KEY (proveedor) REFERENCES proveedor(nombre)
);
INSERT INTO productos (codigo_barra, nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion, empresa)
VALUES ('123456789', 'iPhone 13 Pro', 'El último smartphone de Apple con pantalla ProMotion y cámara mejorada.', 1099.99, 50, 'Electrónica', 'Proveedor 1', '2023-09-24', NULL, CURRENT_TIMESTAMP, 'A');

INSERT INTO productos (codigo_barra, nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion, empresa)
VALUES ('987654321', 'Café Arabica Premium', 'Granos de café Arabica de alta calidad, tostados y molidos.', 12.99, 100, 'Alimentos', 'Proveedor 2', '2023-10-01', '2024-10-01', CURRENT_TIMESTAMP, 'B');
