-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               11.5.2-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping data for table idvs_portal.agency: ~3 rows (approximately)
INSERT IGNORE INTO `agency` (`id`, `name`, `address`) VALUES
	(1, 'Guyana Revenue Authority', NULL),
	(2, 'General Register Office', NULL),
	(3, 'Ministry of Home Affairs', NULL);

-- Dumping data for table idvs_portal.auth_group: ~0 rows (approximately)

-- Dumping data for table idvs_portal.auth_group_permissions: ~0 rows (approximately)

-- Dumping data for table idvs_portal.auth_permission: ~52 rows (approximately)
INSERT IGNORE INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add agency', 7, 'add_agency'),
	(26, 'Can change agency', 7, 'change_agency'),
	(27, 'Can delete agency', 7, 'delete_agency'),
	(28, 'Can view agency', 7, 'view_agency'),
	(29, 'Can add document type', 8, 'add_documenttype'),
	(30, 'Can change document type', 8, 'change_documenttype'),
	(31, 'Can delete document type', 8, 'delete_documenttype'),
	(32, 'Can view document type', 8, 'view_documenttype'),
	(33, 'Can add app log', 9, 'add_applog'),
	(34, 'Can change app log', 9, 'change_applog'),
	(35, 'Can delete app log', 9, 'delete_applog'),
	(36, 'Can view app log', 9, 'view_applog'),
	(37, 'Can add user log', 10, 'add_userlog'),
	(38, 'Can change user log', 10, 'change_userlog'),
	(39, 'Can delete user log', 10, 'delete_userlog'),
	(40, 'Can view user log', 10, 'view_userlog'),
	(41, 'Can add Police User', 11, 'add_policeuser'),
	(42, 'Can change Police User', 11, 'change_policeuser'),
	(43, 'Can delete Police User', 11, 'delete_policeuser'),
	(44, 'Can view Police User', 11, 'view_policeuser'),
	(45, 'Can add Document Owner', 12, 'add_publicuser'),
	(46, 'Can change Document Owner', 12, 'change_publicuser'),
	(47, 'Can delete Document Owner', 12, 'delete_publicuser'),
	(48, 'Can view Document Owner', 12, 'view_publicuser'),
	(49, 'Can add document', 13, 'add_document'),
	(50, 'Can change document', 13, 'change_document'),
	(51, 'Can delete document', 13, 'delete_document'),
	(52, 'Can view document', 13, 'view_document');

-- Dumping data for table idvs_portal.auth_user: ~1 rows (approximately)
INSERT IGNORE INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$870000$EbtNbZTXxp6b0BUtPVd5Ur$7DepLLrk5k8XuKXVMHulB5Mb+1JNil1MMbTvxIjVw2g=', '2025-08-26 21:47:40.805019', 1, 'perny', '', '', 'pernell.christophe@gmail.com', 1, 1, '2025-08-26 19:55:42.105577');

-- Dumping data for table idvs_portal.auth_user_groups: ~0 rows (approximately)

-- Dumping data for table idvs_portal.auth_user_user_permissions: ~0 rows (approximately)

-- Dumping data for table idvs_portal.django_admin_log: ~11 rows (approximately)
INSERT IGNORE INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2025-08-26 19:56:35.262071', '1', 'Guyana Revenue Authority', 1, '[{"added": {}}]', 7, 1),
	(2, '2025-08-26 19:56:51.341554', '2', 'General Register Office', 1, '[{"added": {}}]', 7, 1),
	(3, '2025-08-26 19:57:04.229504', '3', 'Ministry Of Home Affairs', 1, '[{"added": {}}]', 7, 1),
	(4, '2025-08-26 19:57:41.370392', '1', 'Driver\'S License', 1, '[{"added": {}}]', 8, 1),
	(5, '2025-08-26 19:57:49.179011', '1', 'Driver\'S License', 2, '[]', 8, 1),
	(6, '2025-08-26 19:58:07.210944', '2', 'Tax Identification Number(Tin)', 1, '[{"added": {}}]', 8, 1),
	(7, '2025-08-26 19:58:21.410019', '3', 'Birth Certificate', 1, '[{"added": {}}]', 8, 1),
	(8, '2025-08-26 19:58:28.335071', '4', 'Passport', 1, '[{"added": {}}]', 8, 1),
	(9, '2025-08-26 21:09:52.906070', '1', 'Malcolm Damian Welcome', 1, '[{"added": {}}]', 12, 1),
	(10, '2025-08-26 21:10:22.750961', '2', 'Carlo Maximus Douglas', 1, '[{"added": {}}]', 12, 1),
	(11, '2025-08-26 21:48:11.537858', '1', 'SC-2653234 - Joe Smith', 1, '[{"added": {}}]', 11, 1);

-- Dumping data for table idvs_portal.django_content_type: ~13 rows (approximately)
INSERT IGNORE INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(7, 'document_portal', 'agency'),
	(13, 'document_portal', 'document'),
	(8, 'document_portal', 'documenttype'),
	(9, 'logs', 'applog'),
	(10, 'logs', 'userlog'),
	(6, 'sessions', 'session'),
	(11, 'user_portal', 'policeuser'),
	(12, 'user_portal', 'publicuser');

-- Dumping data for table idvs_portal.django_migrations: ~31 rows (approximately)
INSERT IGNORE INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2025-08-26 01:36:41.142232'),
	(2, 'auth', '0001_initial', '2025-08-26 01:36:41.476024'),
	(3, 'admin', '0001_initial', '2025-08-26 01:36:41.540547'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2025-08-26 01:36:41.558397'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-08-26 01:36:41.563468'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2025-08-26 01:36:41.618750'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2025-08-26 01:36:41.651174'),
	(8, 'auth', '0003_alter_user_email_max_length', '2025-08-26 01:36:41.667190'),
	(9, 'auth', '0004_alter_user_username_opts', '2025-08-26 01:36:41.667190'),
	(10, 'auth', '0005_alter_user_last_login_null', '2025-08-26 01:36:41.698876'),
	(11, 'auth', '0006_require_contenttypes_0002', '2025-08-26 01:36:41.698876'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2025-08-26 01:36:41.714421'),
	(13, 'auth', '0008_alter_user_username_max_length', '2025-08-26 01:36:41.731074'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2025-08-26 01:36:41.746271'),
	(15, 'auth', '0010_alter_group_name_max_length', '2025-08-26 01:36:41.768491'),
	(16, 'auth', '0011_update_proxy_permissions', '2025-08-26 01:36:41.781040'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2025-08-26 01:36:41.793436'),
	(18, 'document_portal', '0001_initial', '2025-08-26 01:36:41.819084'),
	(19, 'logs', '0001_initial', '2025-08-26 01:36:41.825239'),
	(20, 'logs', '0002_userlog', '2025-08-26 01:36:41.832927'),
	(21, 'logs', '0003_userlog_last_active_alter_userlog_logged_in', '2025-08-26 01:36:41.890373'),
	(22, 'logs', '0004_alter_userlog_last_active_alter_userlog_logged_in_and_more', '2025-08-26 01:36:41.904088'),
	(23, 'logs', '0005_alter_userlog_options', '2025-08-26 01:36:41.904088'),
	(24, 'logs', '0006_alter_userlog_options', '2025-08-26 01:36:41.920549'),
	(25, 'logs', '0007_remove_userlog_is_active_remove_userlog_last_active_and_more', '2025-08-26 01:36:42.032023'),
	(26, 'logs', '0008_alter_userlog_options', '2025-08-26 01:36:42.032023'),
	(27, 'sessions', '0001_initial', '2025-08-26 01:36:42.063354'),
	(28, 'user_portal', '0001_initial', '2025-08-26 21:08:11.645053'),
	(29, 'document_portal', '0002_document', '2025-08-27 18:14:27.450475'),
	(30, 'document_portal', '0003_document_date_submitted', '2025-08-27 18:43:52.221808'),
	(31, 'user_portal', '0002_policeuser_passw_publicuser_email_addr_and_more', '2025-08-27 20:01:00.302259');

-- Dumping data for table idvs_portal.django_session: ~3 rows (approximately)
INSERT IGNORE INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('dpqzwpfb4p1du322sk4b251sxldsha47', '.eJxVjEEOwiAQRe_C2hDKTIfWpXvPQBgYpGpoUtqV8e7apAvd_vfefykftrX4rcnip6TOqlOn341DfEjdQbqHept1nOu6TKx3RR-06euc5Hk53L-DElr51pgAI1AQ4RHBGMvQAUKEAVl6zL0ZiSKT5YwGxbJjYZcd0SCREqr3B9UYN80:1uqzm7:VSdCjwzZwHNhK1ZJGtFxFr6TGSM0SgtNlY6ci5g32r0', '2025-09-09 19:56:11.458657'),
	('jiifa4fie6uexshr9welxklsh8mvhtbn', 'e30:1urMxx:At3m6KGG2HYTeUGINOiCEiXwzgREMSwAeT6yY6UMDPY', '2025-09-10 20:41:57.609832'),
	('rmd0yv3c6vqcrxa7bpllvg84ohhr27pr', '.eJxVjEEOwiAQRe_C2hDKTIfWpXvPQBgYpGpoUtqV8e7apAvd_vfefykftrX4rcnip6TOqlOn341DfEjdQbqHept1nOu6TKx3RR-06euc5Hk53L-DElr51pgAI1AQ4RHBGMvQAUKEAVl6zL0ZiSKT5YwGxbJjYZcd0SCREqr3B9UYN80:1ur1W0:r8UUTV6_apv2bZh_vZXFy0hb2j70EawZEGqzmHfFOXI', '2025-09-09 21:47:40.805019');

-- Dumping data for table idvs_portal.doc_type: ~4 rows (approximately)
INSERT IGNORE INTO `doc_type` (`id`, `doc_type`) VALUES
	(3, 'Birth Certificate'),
	(1, 'Driver\'s License'),
	(4, 'Passport'),
	(2, 'Tax Identification Number(TIN)');

-- Dumping data for table idvs_portal.logs_userlog: ~0 rows (approximately)

-- Dumping data for table idvs_portal.pol_user: ~1 rows (approximately)
INSERT IGNORE INTO `pol_user` (`id`, `fname`, `oth_names`, `lname`, `reg_num`, `passw`) VALUES
	(1, 'Joe', 'Michael', 'Smith', 'SC-2653234', 'open12');

-- Dumping data for table idvs_portal.pub_user: ~2 rows (approximately)
INSERT IGNORE INTO `pub_user` (`id`, `fname`, `oth_names`, `lname`, `uid`, `added_on`, `email_addr`, `passw`) VALUES
	(1, 'Malcolm', 'Damian', 'Welcome', 'GUY-MDW01', '2025-08-26 21:09:05.000000', NULL, 'open12'),
	(2, 'Carlo', 'Maximus', 'Douglas', 'GUY-CMD0231', '2025-08-26 21:09:52.000000', NULL, 'open12');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
