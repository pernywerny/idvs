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

-- Dumping data for table idvs_dev.agency: ~3 rows (approximately)
INSERT IGNORE INTO `agency` (`id`, `name`, `address`) VALUES
	(1, 'Guyana Revenue Authority', NULL),
	(2, 'General Register Office', NULL),
	(3, 'Ministry of Home Affairs', NULL);

-- Dumping data for table idvs_dev.auth_group: ~0 rows (approximately)

-- Dumping data for table idvs_dev.auth_group_permissions: ~0 rows (approximately)

-- Dumping data for table idvs_dev.auth_permission: ~44 rows (approximately)
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
	(33, 'Can add document', 9, 'add_document'),
	(34, 'Can change document', 9, 'change_document'),
	(35, 'Can delete document', 9, 'delete_document'),
	(36, 'Can view document', 9, 'view_document'),
	(37, 'Can add Police User', 10, 'add_policeuser'),
	(38, 'Can change Police User', 10, 'change_policeuser'),
	(39, 'Can delete Police User', 10, 'delete_policeuser'),
	(40, 'Can view Police User', 10, 'view_policeuser'),
	(41, 'Can add Document Owner', 11, 'add_publicuser'),
	(42, 'Can change Document Owner', 11, 'change_publicuser'),
	(43, 'Can delete Document Owner', 11, 'delete_publicuser'),
	(44, 'Can view Document Owner', 11, 'view_publicuser');

-- Dumping data for table idvs_dev.auth_user: ~1 rows (approximately)
INSERT IGNORE INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$870000$AsE2oxvkIlmOnvzdM8RgM2$HFNHlxInMrGoffc4aOkdDzMny9ruZNLZwEg+WD0iL6k=', '2025-08-26 21:49:02.777752', 1, 'perny', '', '', 'pernell.christophe@gmail.com', 1, 1, '2025-08-26 21:44:52.566819');

-- Dumping data for table idvs_dev.auth_user_groups: ~0 rows (approximately)

-- Dumping data for table idvs_dev.auth_user_user_permissions: ~0 rows (approximately)

-- Dumping data for table idvs_dev.django_admin_log: ~1 rows (approximately)
INSERT IGNORE INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2025-08-26 21:50:22.224880', '1', 'Carlo Maximus Douglas - Birth Certificate: BC-155647896', 1, '[{"added": {}}]', 9, 1);

-- Dumping data for table idvs_dev.django_content_type: ~11 rows (approximately)
INSERT IGNORE INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(7, 'agency', 'agency'),
	(9, 'agency', 'document'),
	(8, 'agency', 'documenttype'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(6, 'sessions', 'session'),
	(10, 'user', 'policeuser'),
	(11, 'user', 'publicuser');

-- Dumping data for table idvs_dev.django_migrations: ~20 rows (approximately)
INSERT IGNORE INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2025-08-25 15:41:14.803465'),
	(2, 'auth', '0001_initial', '2025-08-25 15:41:15.361271'),
	(3, 'admin', '0001_initial', '2025-08-25 15:41:15.473275'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2025-08-25 15:41:15.473275'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-08-25 15:41:15.490549'),
	(6, 'user', '0001_initial', '2025-08-25 15:41:15.541128'),
	(7, 'agency', '0001_initial', '2025-08-25 15:41:15.775814'),
	(8, 'contenttypes', '0002_remove_content_type_name', '2025-08-25 15:41:15.854990'),
	(9, 'auth', '0002_alter_permission_name_max_length', '2025-08-25 15:41:15.918883'),
	(10, 'auth', '0003_alter_user_email_max_length', '2025-08-25 15:41:15.966237'),
	(11, 'auth', '0004_alter_user_username_opts', '2025-08-25 15:41:15.986348'),
	(12, 'auth', '0005_alter_user_last_login_null', '2025-08-25 15:41:16.045787'),
	(13, 'auth', '0006_require_contenttypes_0002', '2025-08-25 15:41:16.045787'),
	(14, 'auth', '0007_alter_validators_add_error_messages', '2025-08-25 15:41:16.061448'),
	(15, 'auth', '0008_alter_user_username_max_length', '2025-08-25 15:41:16.093895'),
	(16, 'auth', '0009_alter_user_last_name_max_length', '2025-08-25 15:41:16.125836'),
	(17, 'auth', '0010_alter_group_name_max_length', '2025-08-25 15:41:16.175878'),
	(18, 'auth', '0011_update_proxy_permissions', '2025-08-25 15:41:16.192739'),
	(19, 'auth', '0012_alter_user_first_name_max_length', '2025-08-25 15:41:16.244194'),
	(20, 'sessions', '0001_initial', '2025-08-25 15:41:16.300299');

-- Dumping data for table idvs_dev.django_session: ~2 rows (approximately)
INSERT IGNORE INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('31r6utaci9m9dk4kvp4unxxb7nigfrmu', '.eJxVjEEOwiAQRe_C2hCgMFCX7j0DmYFBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4ZXEWWpx-N8L04LaDfMd2m2Wa27pMJHdFHrTL65z5eTncv4OKvX7rgM6xd5xI4cCKwTpSxVLyuozWeQ4BMhCkwmDMyCbwoJFAQVGoEMX7A_SXOF4:1ur1XK:W-4FTanuWYRYpQ3C4BZDgah5X19QA6dS2iXe9a3BWtc', '2025-09-09 21:49:02.777752'),
	('yh382djn9k711bqgkxu7t84zk2l536m3', '.eJxVjEEOwiAQRe_C2hCgMFCX7j0DmYFBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4ZXEWWpx-N8L04LaDfMd2m2Wa27pMJHdFHrTL65z5eTncv4OKvX7rgM6xd5xI4cCKwTpSxVLyuozWeQ4BMhCkwmDMyCbwoJFAQVGoEMX7A_SXOF4:1ur1Uw:l3XoIxYT0orcI7QxItAiV9EN2P1kNemudVLVGkM3-6w', '2025-09-09 21:46:34.735027');

-- Dumping data for table idvs_dev.document: ~1 rows (approximately)
INSERT IGNORE INTO `document` (`id`, `document_id`, `last_accessed_on`, `issuing_agency_id`, `last_accessed_by_id`, `owner_id`, `document_type_id`) VALUES
	(1, 'BC-155647896', '2025-08-26 21:49:02.000000', 2, 1, 2, 3);

-- Dumping data for table idvs_dev.doc_type: ~4 rows (approximately)
INSERT IGNORE INTO `doc_type` (`id`, `doc_type`) VALUES
	(3, 'Birth Certificate'),
	(1, 'Driver\'s License'),
	(4, 'Passport'),
	(2, 'Tax Identification Number(TIN)');

-- Dumping data for table idvs_dev.pol_user: ~1 rows (approximately)
INSERT IGNORE INTO `pol_user` (`id`, `fname`, `oth_names`, `lname`, `reg_num`) VALUES
	(1, 'Joe', 'Michael', 'Smith', 'SC-2653234');

-- Dumping data for table idvs_dev.pub_user: ~2 rows (approximately)
INSERT IGNORE INTO `pub_user` (`id`, `fname`, `oth_names`, `lname`, `uid`, `added_on`) VALUES
	(1, 'Malcolm', 'Damian', 'Welcome', 'GUY-MDW01', '2025-08-26 21:09:05.000000'),
	(2, 'Carlo', 'Maximus', 'Douglas', 'GUY-CMD0231', '2025-08-26 21:09:52.000000');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
