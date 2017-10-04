CREATE DATABASE  IF NOT EXISTS 'friendships';
USE 'friendships';

CREATE TABLE 'user' (
  'id' int(11) NOT NULL AUTO_INCREMENT,
  'first_name' varchar(45) NOT NULL DEFAULT '',
  'last_name' varchar(45) NOT NULL DEFAULT '',
  'created_at' DATETIME NOT NULL DEFAULT '',
  'updated_at' DATETIME NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
)