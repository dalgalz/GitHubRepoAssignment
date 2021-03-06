CREATE DATABASE  IF NOT EXISTS friendships;
USE friendships;

CREATE TABLE users (
  id int(11) NOT NULL AUTO_INCREMENT,
  first_name varchar(45) NOT NULL DEFAULT '',
  last_name varchar(45) NOT NULL DEFAULT '',
  created_at DATETIME DEFAULT NULL,
  updated_at DATETIME DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE friendships (
  id int(11) NOT NULL AUTO_INCREMENT,
  user_id int(11) NOT NULL,
  friend_id int(11) NOT NULL,
  created_at datetime DEFAULT NULL,
  updated_at datetime DEFAULT NULL,
  PRIMARY KEY (id),
  KEY fk_users_has_users_users1_idx (friend_id),
  KEY fk_users_has_users_users_idx (user_id)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

LOCK TABLES friendships WRITE;
INSERT INTO friendships VALUES (1,1,2,NULL,NULL),(2,1,3,NULL,NULL),(3,1,4,NULL,NULL),(4,2,1,NULL,NULL),(5,2,3,NULL,NULL),(6,3,1,NULL,NULL),(7,3,2,NULL,NULL),(8,3,4,NULL,NULL),(9,4,1,NULL,NULL),(10,4,3,NULL,NULL);
UNLOCK TABLEs;

LOCK TABLES users WRITE;
INSERT INTO users VALUES (1,'Todd','Enders',NULL,NULL),(2,'Dylan','Sharkey',NULL,NULL),(3,'Jonathan','Ben-ammi',NULL,NULL),(4,'Michael','Arbogast',NULL,NULL),(5,'John','Doe',NULL,NULL);
UNLOCK TABLES;
