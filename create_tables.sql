create table users (
    id int primary key auto_increment,
    refferal_link varchar(50) unique not null ,
    credits float default 0,
    administrator boolean not null default 0,
    refferaled_id int,
    FOREIGN KEY (refferaled_id) REFERENCES users(id)
);

create table promo_code (
    id int primary key auto_increment,
    code varchar(50) unique not null ,
    is_used boolean default 0,
    discount_percentage float not null,
    start_date datetime not null ,
    end_date datetime not null,
    user_id int,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table vaucher (
    id int primary key auto_increment,
    code varchar(50) unique not null ,
    is_used boolean default 0,
    amount float not null,
    start_date datetime not null ,
    end_date datetime not null,
    user_id int,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table plans (
    id int primary key auto_increment,
    name varchar(50),
    num_servers int,
    price float
);

INSERT INTO plans(name, num_servers, price)
VALUES
    ('Tier1',1,50),
    ('Tier2',3,40),
    ('Tier3',5,35),
    ('Tier4',10,30),
    ('Tier5',25,25),
    ('Tier6',50,20)


