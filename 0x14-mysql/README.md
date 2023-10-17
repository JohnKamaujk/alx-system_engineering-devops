# Task 0:

https://www.devart.com/dbforge/mysql/how-to-install-mysql-on-ubuntu/

# Task 1:

(add checker public key in web-02)

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;

# Task 2:

CREATE DATABASE tyrell_corp;

USE tyrell_corp;

CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));

INSERT INTO nexus6 (name) VALUES ('Leon');

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

# Task 3:
## only on web-01:

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';

GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

# Task 4:

sudo ufw allow 3306/tcp

sudo ufw reload

sudo sed -i "s/bind-address\t= 127.0.0.1/# bind-address\t= 127.0.0.1/" /etc/mysql/mysql.conf.d/mysqld.cnf

## in master server:

echo 'server-id = 1' | sudo tee -a /etc/mysql/mysql.conf.d/mysqld.cnf

## in slave server:

echo 'server-id = 2' | sudo tee -a /etc/mysql/mysql.conf.d/mysqld.cnf

echo 'relay-log               = /var/log/mysql/mysql-relay-bin.log' | sudo tee -a /etc/mysql/mysql.conf.d/mysqld.cnf

## in both servers:

echo 'log_bin = /var/log/mysql/mysql-bin.log' | sudo tee -a /etc/mysql/mysql.conf.d/mysqld.cnf

sudo service mysql restart

## in master server (save file and position for later use):

SHOW MASTER STATUS;

## in slave server (use the saved info from master server):

CHANGE MASTER TO

MASTER_HOST = '<master server ip>',

MASTER_USER = 'replica_user',

MASTER_PASSWORD = '<replica_user_password>',

MASTER_LOG_FILE = '<file>',

MASTER_LOG_POS = <position>;

START SLAVE;
