SET foreign_key_checks = 0;
drop table if exists user_image;
create table user_image (
	id integer primary key auto_increment,
    name varchar(50) not null,
    tree_image LONGBLOB,
    house_image LONGBLOB
);

drop table if exists user_tree_result;
create table user_tree_result(
    id integer primary key,
    type TEXT,
    root TEXT, 
    branch TEXT,
    leap TEXT,
    stem TEXT, 
    size TEXT,
    characters integer,
    figures_gen float,
    figures_con float,
    figures_hap float,
    figures_soc float,
    figures_hig float
);

drop table if exists user_house_result;
create table user_house_result(
    id integer primary key,
    type TEXT,
    roof TEXT,
    door TEXT,
    windows TEXT
);

select * from user_image;
select * from user_tree_result;
select * from user_house_result;

