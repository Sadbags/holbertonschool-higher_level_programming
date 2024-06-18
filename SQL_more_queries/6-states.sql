-- Script that creates database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
Use hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
    id INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(256) NOT NULL
	);