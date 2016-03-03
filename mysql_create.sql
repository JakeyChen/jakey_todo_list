# database init
# $  mysql -u root -p < mysql_create.sql 
drop database if exists todo;
create database todo;

-- create user jakey IDENTIFIED by 'cjs168';

GRANT ALL ON todo.* TO jakey IDENTIFIED BY 'cjs168';
