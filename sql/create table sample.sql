create database ai_hajeera;
drop database ai_hajeera;
show databases;
use ai_hajeera;
create table ad_user_reg
(user_id int not null primary key auto_increment,
f_name varchar(200) not null,
m_name varchar(200)not null,
l_name varchar(200)not null,
dob date,
phone_no long,
user_name varchar(50) not null,
pass_word varchar(50) not null);
drop table ad_user_reg;

alter table ad_user_reg add column create_by varchar(50)not null;
alter table ad_user_reg add column modifiy_by varchar(50)not null;
alter table ad_user_reg add column create_on date;
alter table ad_user_reg add column modifiy_on date;
insert into ad_user_reg  
(user_id,f_name,m_name,l_name,dob,phone_no,user_name,pass_word,create_by,modifiy_by,create_on,modifiy_on)
values
(1,'syed','azar','deen','1988-02-09',444444444444,'shgf##','fhfr*&^%','ghjkl','fdsahlj','1954-03-08','1956-05-13');
insert into ad_user_reg  
(user_id,f_name,m_name,l_name,dob,phone_no,user_name,pass_word,create_by,modifiy_by,create_on,modifiy_on)
values
(2,'syed','rafnu','nudeen','2016-03-22',4567890321,'hgaf##gt','fkhfar%','ghjkl87','fdsahkih','1954-04-06','1955-05-19');
insert into ad_user_reg  
(user_id,f_name,m_name,l_name,dob,phone_no,user_name,pass_word,create_by,modifiy_by,create_on,modifiy_on)
values
(3,'hajeera','sithika','beauty','2015-12-11',9876543210,'jgsdaaew','u8uiuei','hajrrr','azaer','1957-04-06','1998-05-19');
insert into ad_user_reg  
(user_id,f_name,m_name,l_name,dob,phone_no,user_name,pass_word,create_by,modifiy_by,create_on,modifiy_on)
values
(4,'aafridah','mahreeb','jallima','2015-12-11',9876543210,'jgsdaaew','u8uiuei','hajrrr','azaer','1957-04-06','1998-05-19');
update  ad_user_reg set modifiy_on="1987-07-11" where user_id=4; 
update ad_user_reg set create_on="1987-09-09" where user_id=3;
insert into ad_user_reg  
(user_id,f_name,m_name,l_name,dob,phone_no,user_name,pass_word,create_by,modifiy_by,create_on,modifiy_on)
values
(5,'ramiza','bagum','ameera','1965-05-07',4567854322,'begummm2','hgfds*&','azarer','rafan','1567-08-14','1987-07-09');
update ad_user_reg set dob="1992-11-16" where user_id=3;
truncate ad_user_reg;








create table ad_user_login
(
login_id int not null primary key,
user_name varchar(80) not null unique,
password varchar(56) not null,
new_password varchar(20) not null,
user_id int not null,
create_by varchar(50),
modifiy_by varchar(40),
create_on date,
modifiy_on date,
foreign key(user_id) references ad_user_reg(user_id)
);
insert into ad_user_login
(





