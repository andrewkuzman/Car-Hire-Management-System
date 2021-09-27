CREATE DATABASE Car_Hire_Management_System;
USE Car_Hire_Management_System;

CREATE TABLE vehicle (
    vehicle_id INT NOT NULL,
    vehicle_type CHAR NOT NULL,
    model CHAR NOT NULL,
    manf_year YEAR NOT NULL,
    PRIMARY KEY (vehicle_id)
);

CREATE TABLE customer (
    customer_id INT NOT NULL,
    customer_name CHAR NOT NULL,
    email CHAR,
    PRIMARY KEY (customer_id)
);

CREATE TABLE customer_phone(
    phone CHAR(11) NOT NULL,
    customer_id INT NOT NULL,
    PRIMARY KEY (phone),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);

CREATE TABLE bookings(
    booking_num INT NOT NULL,
    vehicle_id INT NOT NULL,
    customer_id INT NOT NULL,
    hire_date DATE NOT NULL,
    return_date DATE NOT NULL,
    invoice_num INT NOT NULL UNIQUE,
    invoice_date DATE NOT NULL,
    amount FLOAT NOT NULL,
    PRIMARY KEY (booking_num),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicle(vehicle_id) ON DELETE CASCADE
);
