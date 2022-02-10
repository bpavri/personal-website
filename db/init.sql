-- CREATE DATABASE `flask-vue-mysql-docker`;
-- USE `flask-vue-mysql-docker`;

CREATE TABLE `pricing` (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(512) NOT NULL,
    `product_title` VARCHAR(512) NOT NULL,
    `product_url` VARCHAR(512) NOT NULL,
    `initial_price` DECIMAL(6,2) NOT NULL,
    `created` DATETIME DEFAULT CURRENT_TIMESTAMP(),
    `last_checked` DATETIME DEFAULT CURRENT_TIMESTAMP()
);