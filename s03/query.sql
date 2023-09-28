-- crud

create table person(id integer primary key , name text unique);
insert into  person (name) values ('mohammad'),('ali');
select id,name from person where name='ali';
update person set name='alireza' where name='ali';
delete from person where name='mohammad';