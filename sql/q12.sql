use ai_hajeera;
create table ai_use_delimiter 
(s_no int not null primary key auto_increment,
first_name varchar (50) not null,
middle_name varchar(50) not null,
last_name varchar (50) not null,
age int,
gender varchar(50));
delimiter $$
drop procedure if exists c1;$$
create procedure c1()
begin
select * from ai_use_delimiter;
end $$	
delimiter ;
call c1();



delimiter @@
drop procedure if exists clmd

create procedure clmd(
in tablename varchar(200),
in columnname varchar (80))
begin

 set @statement =concat('alter table',tablename,'drop column' ,colmnname);
 prepare stmt from @statement;
 execute stmt;
 end @@
 delimiter ;

call clmd( 'ai_use_delimiter','last_name');