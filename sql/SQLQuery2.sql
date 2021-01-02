USE Bikestores
 # LIKE- pattern matching % -any no of characters _A single character
 select * from sales.customers
 where first_name like '__m'

 /* select starting from m*/
 select * from sales.customers
 where first_name like 'm%'

 select * from sales.customers
 where last_name like '%man'
 
 select * from sales.customers
 where city like '%city%'

 select * from sales.customers
 where first_name like 'm___'

 select * from sales.customers
 where first_name like '__m%'
 
# USE of TOP clauses  
select top 3  first_name from sales.customers;

select top 3 * from sales.customers
use learn3
select * from stu1

# DML: Data manipulation Language:Impact the data not the structure
# Update command

insert into stu1 
values(2,'ram',24),(3,'ajay',35),(4,'manas',34)
 
 update stu1
set age= 42
where name ='ram'

#SQL delete statement

delete from stu1 where rno=3

insert into stu1
 values(2,'ra',24),(3,'aja',35),(4,'mana',33)
select * from stu1

delete stu1
# there are no difference from delete and delete from

insert into stu1 
values(2,'ram',24),(3,'ajay',35),(4,'manas',34)

# alter table :DDL( Data definition Language)

insert into stu1 
values(5,'rm',23),(6,'aay',37),(7,'mnas',39)

alter table stu1
alter column name varchar(20)

alter table stu1
add class char(5)

select * from stu1

update stu1
set class = '7th'

select * from stu1

alter table stu1
drop column class

# not everyone got the access of drop in realtime

#Truncate table : to make the empty/part of DDL

truncate table stu1
#delete accepts 'where' clause but truncate do not accept any clause

#SQL Operators
use Bikestores

select * from production.products
where brand_id=9 and category_id=6

select * from production.products
where not  brand_id=9 

/* Constraints- Chapter 3*/
 use learn3
 select * from emp;

 create table emp
 (EID CHAR(5),
 NAME VARCHAR(20),
 ADDR VARCHAR(50),
 CITY VARCHAR(20),
 PHONE CHAR(15),
 EMAIL VARCHAR(50),
 DOB DATE)

 insert into emp(EID,ADDR,CITY,PHONE,EMAIL,DOB)
 VALUES ('E001','sector 11 dwarka','delhi','999999001','abc@gmail.com','10-oct-1998');

 insert into emp(EID,NAME,ADDR,CITY,PHONE,EMAIL,DOB)
 VALUES ('E002','babita','b32 11 dwarka','delhi','999999001','abcd@gmail.com','10-nov-1998');

 insert into emp(EID,ADDR,CITY,PHONE,EMAIL,DOB,NAME)
 VALUES ('E003','okhlaa part','delhi','922999001','kapil@gmail.com','10-jan-1997','kapil');

 #Implement constraints in not null in the data

 update emp set name ='ajay'
 alter table emp
 alter column name VARCHAR(20) NOT NULL

 # default constraint
 alter table emp
 add constraint defcty default 'delhi' for city;

 insert into emp(EID,ADDR,PHONE,EMAIL,DOB,NAME)
 VALUES ('E003','sector3','999099001','pkmishra@outlook.com','10-mar-1987','mohit');

 select * from emp;
 alter table emp
 ADD CONSTRAINT ukph UNIQUE (PHONE)

 #age constraint check 

 alter table emp
 add CONSTRAINT CKDB CHECK (DOB<='1-JAN-2020');

 UPDATE EMP SET EID = 'E005'
 WHERE NAME = 'kapil'

 ALTER TABLE EMP
 ALTER COLUMN EID CHAR(5) NOT NULL;


 insert into emp(EID,CITY,ADDR,PHONE,EMAIL,DOB,NAME)
 VALUES ('E004','HNC 420','DELHI','999099001','RG07@yahoo.co.in','01-Nov-2001','Rajat Gupta');

 alter table emp
 ADD CONSTRAINT PKEID PRIMARY KEY (EID) 

 insert into emp(EID,CITY,ADDR,PHONE,EMAIL,DOB,NAME)
 VALUES ('E005','rajouri garden block 2','DELHI','999099881','rsharma@gmail.com','15-Nov-1995','Rohan Sharma');

 CREATE TABLE EMP_SAL
 (EID CHAR(5),
 DEPT VARCHAR(10),
 DESI VARCHAR(30),
 SALARY INT);

 USE learn3
 INSERT INTO EMP_SAL
 VALUES ('E0010','LEGAL','SUPERVISOR',20000);

 SELECT * FROM EMP_SAL;
 UPDATE EMP_SAL SET EID ='E0001';

 ALTER TABLE EMP_SAL
 ADD CONSTRAINT FKID FOREIGN KEY (EID) REFERENCES EMP (EID)

