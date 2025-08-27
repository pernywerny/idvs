create table app_log
	(
		log_id int(32) not null auto_increment,
		action_taken varchar(500),
		log_type varchar(128),
		user varchar(128),
		when_done datetime,
		log_session_id varchar(256),
		mac_address varchar(32),
		primary key(log_id)
	)engine =innodb character set = utf8;




create table hr_log
    (
		log_id bigint not null auto_increment,
		log_action varchar(512) not null,
		log_type varchar(16) not null,
		log_user varchar(128) not null,
		action_dt datetime not null default NOW(),
		app varchar(64) not null,
		sesh_id varchar(1024) not null,
		ip_addr varchar(36),
		target_pk bigint,
		index(log_id),
		index(ip_addr),
		index(log_user),
		index(action_dt),
		index(app),
		index(sesh_id),
		primary key(log_id)
    )engine =innodb character set = utf8;