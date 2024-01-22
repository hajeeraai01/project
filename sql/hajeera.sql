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
drop procedure if exists d1;@@

create procedure d1(
in first_nameparam varchar(70),
in middle_nameparam varchar(70),
in last_nameparam varchar(60),
in age_param int,
in gender_param varchar(70)
)
begin
insert into ai_use_delimiter(first_name,middle_name,last_name,age,gender)
values( first_nameparam, middle_nameparam, last_nameparam,age_param, gender_param);
end @@
delimiter ;

call d1( 'hajeera','sithika','azar',31,'female');
call d1('aysha','sithika','nazurul',35,'female');
call d1('irfana','sithika','abu',29,'female');
call d1('jakiriya','syed','kamila',34,'male');
call c1();


delimiter &&
drop procedure if exists f1;&&
create procedure f1
(
in gudian varchar(60),
in vayasu int
)

begin
update ai_use_delimiter set last_name=gudian where age= 29;
end&&
delimiter ;

call f1('kanila',31);
call f1('kamila',31);
call f1('azar', 31);
call f1('nazrul',35);
call c1();
delimiter ##
drop procedure if exists s_update;##
create procedure s_update
(
in tablename varchar (200),
in columnname varchar (50),
in valuechange varchar(30),
in idname varchar(50),
in idparam int 
) 
begin
set @statement=concat('update', tablename,'set',columnname,'=\'',valuechange,'\' ' ,'where ',idname,'=',idparam);
prepare stmt from @statement;
execute stmt;
end ##
delimiter ;


call s_update('ai_batch_stud_list','year_of_passing','250000000000','sno',1);

