CREATE DATABASE IF NOT EXISTS  sistemaFacturacion;
USE sistemaFacturacion;
-- Crear la tabla de empresa la cual va a adquirir nuestro sistema
CREATE TABLE empresa ( --- dejar solo empresa para el registro de usuario
    nombre VARCHAR(50) PRIMARY KEY NOT NULL,
    direccion VARCHAR(255) NOT NULL, 
    telefono VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    fechaIngreso TIMESTAMP,
    CUIT_CUIL VARCHAR(12) NOT NULL UNIQUE KEY,
    password VARCHAR(255) NOT NULL
);

-- Crear la tabla de categoria
CREATE TABLE categoria (
    nombre VARCHAR(50) PRIMARY KEY NOT NULL, 
    descripcion TEXT
);

-- Crear la tabla de proveedor
CREATE TABLE proveedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    descripcion TEXT
    empresa VARCHAR(50), 
    FOREIGN KEY (empresa) REFERENCES empresa(nombre),
);

INSERT INTO proveedor (descripcion, direccion, email, nombre, telefono,empresa)
VALUES (
  'Proveedor de productos A',
  'Calle Proveedor 1',
  'proveedor1@example.com',
  'Proveedor 1',
  '111-222-3333',
  'B'
);

INSERT INTO proveedor (descripcion, direccion, email, nombre, telefono,empresa)
VALUES (
  'Proveedor de productos B',
  'Avenida Proveedor 2',
  'proveedor2@example.com',
  'Proveedor 2',
  '444-555-6666',
  'A'
);


-- Crear la tabla de cliente
CREATE TABLE cliente (
    dni INT(9) PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fechaRegistro TIMESTAMP
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
    fechaCreacion DATE TIMESTAMP,
    fechaModificacion CURRENT_TIMESTAMP,
    estado VARCHAR(10),
    FOREIGN KEY (empresa) REFERENCES empresa(nombre),
    FOREIGN KEY (categoria) REFERENCES categoria(nombre)

);

INSERT INTO servicios (nombre, categoria, empresa, descripcion, precio, duracion, unidadMedida, fechaInicio, fechaFinalizacion, fechaCreacion, fechaModificacion, estado)
VALUES ('Servicio 3', 'Electrónica', 'A', 'Descripción del servicio 3', 120.75, 45, 'Horas', '2023-11-10', '2023-12-10', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Activo');

INSERT INTO servicios (nombre, categoria, empresa, descripcion, precio, duracion, unidadMedida, fechaInicio, fechaFinalizacion, fechaCreacion, fechaModificacion, estado)
VALUES ('Servicio 4', 'Electrónica', 'B', 'Descripción del servicio 4', 90.25, 60, 'Días', '2023-11-20', '2023-12-20', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Inactivo');

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
    fecha_lanzamiento TIMESTAMP,
    fecha_vencimiento DATE,
    fecha_modificacion CURRENT_TIMESTAMP,
    empresa VARCHAR(50),
    FOREIGN KEY (categoria) REFERENCES categoria(nombre) ,
    FOREIGN KEY (empresa) REFERENCES empresa(nombre),
    FOREIGN KEY (proveedor) REFERENCES proveedor(nombre)
);
INSERT INTO productos (codigo_barra, nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion, empresa)
VALUES ('123456789', 'iPhone 13 Pro', 'El último smartphone de Apple con pantalla ProMotion y cámara mejorada.', 1099.99, 50, 'Electrónica', 'Proveedor 1', '2023-09-24', NULL, CURRENT_TIMESTAMP, 'A');

INSERT INTO productos (codigo_barra, nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion, empresa)
VALUES ('987654321', 'Café Arabica Premium', 'Granos de café Arabica de alta calidad, tostados y molidos.', 12.99, 100, 'Alimentos', 'Proveedor 2', '2023-10-01', '2024-10-01', CURRENT_TIMESTAMP, 'B');















--------
CREATE DATABASE IF NOT EXISTS  sistemaFacturacion;
USE sistemaFacturacion;

CREATE TABLE empresa (
    nombre VARCHAR(50) PRIMARY KEY NOT NULL,
    direccion VARCHAR(255) NOT NULL, 
    telefono VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    fechaIngreso TIMESTAMP,
    CUIT_CUIL VARCHAR(12) NOT NULL UNIQUE KEY,
    password VARCHAR(255) NOT NULL
);


CREATE TABLE categoria (
    nombre VARCHAR(50) PRIMARY KEY NOT NULL, 
    descripcion TEXT
);


CREATE TABLE proveedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    descripcion TEXT,
    empresa VARCHAR(50), 
    FOREIGN KEY (empresa) REFERENCES empresa(nombre)
);



CREATE TABLE cliente (
    dni INT(9) PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fechaRegistro TIMESTAMP
);

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


CREATE TABLE servicios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    categoria VARCHAR(50),
    empresa VARCHAR(50),
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    duracion INT,
    unidadMedida VARCHAR(5),
    fechaInicio DATE NOT NULL,
    fechaFinalizacion DATE NOT NULL,
    fechaCreacion TIMESTAMP,
    fechaModificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(10),
    FOREIGN KEY (empresa) REFERENCES empresa(nombre),
    FOREIGN KEY (categoria) REFERENCES categoria(nombre)
);


CREATE TABLE productos (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    codigo_barra VARCHAR(255),
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    categoria VARCHAR(50),
    proveedor VARCHAR(50),
    fecha_lanzamiento TIMESTAMP,
    fecha_vencimiento DATE,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    empresa VARCHAR(50),
    id_proveedor INT,
    FOREIGN KEY (categoria) REFERENCES categoria(nombre) ,
    FOREIGN KEY (empresa) REFERENCES empresa(nombre),
    FOREIGN KEY (id_proveedor) REFERENCES proveedor(id)
);