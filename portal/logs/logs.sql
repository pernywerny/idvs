create database police_logs,

create table hr_logs
    (
        id bigint not null auto_increment,
        user varchar(32),
        client_ip varchar(256),
        user_action varchar(5096),
        date_done datetime,
        success_status boolean default 1,

        constraint primary key(id)
    );




create table auth_logs
    (
        id bigint not null auto_increment,
        user varchar(32),
        client_ip varchar(256),
        user_action varchar(5096),
        date_done datetime,
        success_status boolean default 1,
        constraint primary key(id)
    );




create table access_logs
    (
        id bigint not null auto_increment,
        user varchar(32),
        client_ip varchar(256),
        user_action varchar(5096),
        date_done datetime,
        success_status boolean default 1,
        constraint primary key(id)
    );




create table user_log
    (
        id bigint not null auto_increment,
        username varchar(128),
        session_key varchar(1024),
        logged_in datetime not null,
        logged_out datetime,
        is_active boolean default 1,
        last_active datetime,

        index(session_key),
        index(username),
        index(is_active),
        
        constraint primary key(id)
    );