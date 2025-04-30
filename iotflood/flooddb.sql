-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: flood
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add department',7,'add_department'),(26,'Can change department',7,'change_department'),(27,'Can delete department',7,'delete_department'),(28,'Can view department',7,'view_department'),(29,'Can add designation',8,'add_designation'),(30,'Can change designation',8,'change_designation'),(31,'Can delete designation',8,'delete_designation'),(32,'Can view designation',8,'view_designation'),(33,'Can add staff',9,'add_staff'),(34,'Can change staff',9,'change_staff'),(35,'Can delete staff',9,'delete_staff'),(36,'Can view staff',9,'view_staff'),(37,'Can add user registration',10,'add_userregistration'),(38,'Can change user registration',10,'change_userregistration'),(39,'Can delete user registration',10,'delete_userregistration'),(40,'Can view user registration',10,'view_userregistration'),(41,'Can add ngo',11,'add_ngo'),(42,'Can change ngo',11,'change_ngo'),(43,'Can delete ngo',11,'delete_ngo'),(44,'Can view ngo',11,'view_ngo'),(45,'Can add water status',12,'add_waterstatus'),(46,'Can change water status',12,'change_waterstatus'),(47,'Can delete water status',12,'delete_waterstatus'),(48,'Can view water status',12,'view_waterstatus'),(49,'Can add water source',13,'add_watersource'),(50,'Can change water source',13,'change_watersource'),(51,'Can delete water source',13,'delete_watersource'),(52,'Can view water source',13,'view_watersource'),(53,'Can add location',14,'add_location'),(54,'Can change location',14,'change_location'),(55,'Can delete location',14,'delete_location'),(56,'Can view location',14,'view_location'),(57,'Can add amenities',15,'add_amenities'),(58,'Can change amenities',15,'change_amenities'),(59,'Can delete amenities',15,'delete_amenities'),(60,'Can view amenities',15,'view_amenities'),(61,'Can add relief camp',16,'add_reliefcamp'),(62,'Can change relief camp',16,'change_reliefcamp'),(63,'Can delete relief camp',16,'delete_reliefcamp'),(64,'Can view relief camp',16,'view_reliefcamp'),(65,'Can add weather',17,'add_weather'),(66,'Can change weather',17,'change_weather'),(67,'Can delete weather',17,'delete_weather'),(68,'Can view weather',17,'view_weather'),(69,'Can add rainfall location',18,'add_rainfalllocation'),(70,'Can change rainfall location',18,'change_rainfalllocation'),(71,'Can delete rainfall location',18,'delete_rainfalllocation'),(72,'Can view rainfall location',18,'view_rainfalllocation'),(73,'Can add rainfall intensity',19,'add_rainfallintensity'),(74,'Can change rainfall intensity',19,'change_rainfallintensity'),(75,'Can delete rainfall intensity',19,'delete_rainfallintensity'),(76,'Can view rainfall intensity',19,'view_rainfallintensity'),(77,'Can add evacuation location',20,'add_evacuationlocation'),(78,'Can change evacuation location',20,'change_evacuationlocation'),(79,'Can delete evacuation location',20,'delete_evacuationlocation'),(80,'Can view evacuation location',20,'view_evacuationlocation'),(81,'Can add transport method',21,'add_transportmethod'),(82,'Can change transport method',21,'change_transportmethod'),(83,'Can delete transport method',21,'delete_transportmethod'),(84,'Can view transport method',21,'view_transportmethod'),(85,'Can add emergency supply',22,'add_emergencysupply'),(86,'Can change emergency supply',22,'change_emergencysupply'),(87,'Can delete emergency supply',22,'delete_emergencysupply'),(88,'Can view emergency supply',22,'view_emergencysupply'),(89,'Can add evacuation record',23,'add_evacuationrecord'),(90,'Can change evacuation record',23,'change_evacuationrecord'),(91,'Can delete evacuation record',23,'delete_evacuationrecord'),(92,'Can view evacuation record',23,'view_evacuationrecord'),(93,'Can add household member',24,'add_householdmember'),(94,'Can change household member',24,'change_householdmember'),(95,'Can delete household member',24,'delete_householdmember'),(96,'Can view household member',24,'view_householdmember'),(97,'Can add staffuserregistration',25,'add_staffuserregistration'),(98,'Can change staffuserregistration',25,'change_staffuserregistration'),(99,'Can delete staffuserregistration',25,'delete_staffuserregistration'),(100,'Can view staffuserregistration',25,'view_staffuserregistration');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(15,'floodmanager','amenities'),(7,'floodmanager','department'),(8,'floodmanager','designation'),(22,'floodmanager','emergencysupply'),(20,'floodmanager','evacuationlocation'),(23,'floodmanager','evacuationrecord'),(24,'floodmanager','householdmember'),(14,'floodmanager','location'),(11,'floodmanager','ngo'),(19,'floodmanager','rainfallintensity'),(18,'floodmanager','rainfalllocation'),(16,'floodmanager','reliefcamp'),(9,'floodmanager','staff'),(25,'floodmanager','staffuserregistration'),(21,'floodmanager','transportmethod'),(10,'floodmanager','userregistration'),(13,'floodmanager','watersource'),(12,'floodmanager','waterstatus'),(17,'floodmanager','weather'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-10 07:05:16.637930'),(2,'auth','0001_initial','2025-02-10 07:05:17.396949'),(3,'admin','0001_initial','2025-02-10 07:05:17.601787'),(4,'admin','0002_logentry_remove_auto_add','2025-02-10 07:05:17.611977'),(5,'admin','0003_logentry_add_action_flag_choices','2025-02-10 07:05:17.625016'),(6,'contenttypes','0002_remove_content_type_name','2025-02-10 07:05:17.713586'),(7,'auth','0002_alter_permission_name_max_length','2025-02-10 07:05:17.835151'),(8,'auth','0003_alter_user_email_max_length','2025-02-10 07:05:17.865323'),(9,'auth','0004_alter_user_username_opts','2025-02-10 07:05:17.876847'),(10,'auth','0005_alter_user_last_login_null','2025-02-10 07:05:17.961558'),(11,'auth','0006_require_contenttypes_0002','2025-02-10 07:05:17.961558'),(12,'auth','0007_alter_validators_add_error_messages','2025-02-10 07:05:17.974928'),(13,'auth','0008_alter_user_username_max_length','2025-02-10 07:05:18.066327'),(14,'auth','0009_alter_user_last_name_max_length','2025-02-10 07:05:18.132632'),(15,'auth','0010_alter_group_name_max_length','2025-02-10 07:05:18.153314'),(16,'auth','0011_update_proxy_permissions','2025-02-10 07:05:18.160405'),(17,'auth','0012_alter_user_first_name_max_length','2025-02-10 07:05:18.230966'),(18,'floodmanager','0001_initial','2025-02-10 07:05:18.476662'),(19,'sessions','0001_initial','2025-02-10 07:05:18.535320'),(20,'floodmanager','0002_userregistration','2025-02-10 07:44:36.999451'),(21,'floodmanager','0003_rename_name_department_deptname','2025-02-10 10:15:21.003628'),(22,'floodmanager','0004_staff_contact','2025-02-10 11:08:56.690312'),(23,'floodmanager','0005_staff_password_staff_username','2025-02-11 04:13:41.278700'),(24,'floodmanager','0006_userregistration_address_userregistration_full_name_and_more','2025-02-11 09:33:09.301998'),(25,'floodmanager','0007_ngo','2025-02-12 04:31:38.756017'),(26,'floodmanager','0008_remove_ngo_created_at_remove_ngo_updated_at','2025-02-12 04:44:18.944462'),(27,'floodmanager','0009_alter_ngo_email_alter_ngo_ngo_name','2025-02-12 05:17:25.985758'),(28,'floodmanager','0010_waterstatus','2025-02-12 05:55:27.508699'),(29,'floodmanager','0011_watersource','2025-02-12 06:12:42.453787'),(30,'floodmanager','0012_remove_watersource_source_id','2025-02-12 06:15:03.985386'),(31,'floodmanager','0013_location','2025-02-12 07:32:56.030207'),(32,'floodmanager','0014_rename_name_location_locationname','2025-02-12 07:34:04.280425'),(33,'floodmanager','0015_rename_locationname_location_name','2025-02-12 07:36:17.846999'),(34,'floodmanager','0016_amenities','2025-02-12 08:43:06.818604'),(35,'floodmanager','0017_reliefcamp','2025-02-12 09:02:28.001610'),(36,'floodmanager','0018_alter_reliefcamp_name','2025-02-12 09:38:14.738768'),(37,'floodmanager','0019_weather','2025-02-12 10:25:02.606430'),(38,'floodmanager','0020_remove_weather_precipitation_and_more','2025-02-12 12:46:28.498768'),(39,'floodmanager','0021_rainfalllocation','2025-02-12 13:37:13.830953'),(40,'floodmanager','0022_remove_rainfalllocation_created_at','2025-02-12 13:38:38.262675'),(41,'floodmanager','0023_rainfallintensity','2025-02-12 13:55:23.400637'),(42,'floodmanager','0024_evacuationlocation','2025-02-12 16:11:42.111632'),(43,'floodmanager','0025_transportmethod','2025-02-12 16:25:27.534199'),(44,'floodmanager','0026_emergencysupply','2025-02-12 16:38:05.740441'),(45,'floodmanager','0027_evacuationrecord','2025-02-12 16:54:03.379430'),(46,'floodmanager','0028_rename_time_evacuationrecord_evacuationtime_and_more','2025-02-17 04:02:59.317218'),(47,'floodmanager','0029_rename_date_evacuationrecord_evacuationdate','2025-02-17 04:03:58.521512'),(48,'floodmanager','0030_delete_userregistration_and_more','2025-02-17 05:46:54.192883'),(49,'floodmanager','0031_rename_date_evacuationrecord_evacuationdate_and_more','2025-02-17 05:48:41.222119'),(50,'floodmanager','0032_householdmember_staffuserregistration','2025-02-17 07:02:06.580218'),(51,'floodmanager','0033_remove_staffuserregistration_members_and_more','2025-02-17 08:23:01.043459'),(52,'floodmanager','0034_alter_householdmember_name_and_more','2025-02-17 11:06:14.650547'),(53,'floodmanager','0035_staffuserregistration_email','2025-02-19 06:07:36.515723'),(54,'floodmanager','0036_remove_staffuserregistration_email_and_more','2025-02-19 06:41:34.724671'),(55,'floodmanager','0037_alter_staffuserregistration_email','2025-02-19 06:45:48.175540');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4albcwax287gysps5oma3sczvzyoran1','eyJzdGFmZl9pZCI6Nywic3RhZmZfbmFtZSI6IkFTTEFNIn0:1tp1AM:uU43BgPRKIECza4g2Lb-HjRabzHEZuXRSD_ysThNBy0','2025-03-17 08:28:46.839590'),('8ymgyxlwetlvgzlroghyecod4o24n6q1','eyJzdGFmZl9pZCI6Niwic3RhZmZfbmFtZSI6InNyZWUiLCJsb2dpbnVzZXIiOjN9:1tpKPl:IWZwisDPQlICnzzCXjYoMmzPOXMaUOPFhi0RwEaNo3o','2025-03-18 05:01:57.125868'),('hbqcvdu7v7gwgyrq6dlq3p68oc3ub6so','eyJsb2dpbnVzZXIiOjIwLCJzdGFmZl9pZCI6NSwic3RhZmZfbmFtZSI6IkFzbGFtIFNhbGFtIn0:1tp1sW:tqCcP1xyJj3c-tiKrLZ_jLJbiLs6_KcgL9OqUIUEDVo','2025-03-17 09:14:24.443508');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_amenities`
--

DROP TABLE IF EXISTS `floodmanager_amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_amenities` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_amenities`
--

LOCK TABLES `floodmanager_amenities` WRITE;
/*!40000 ALTER TABLE `floodmanager_amenities` DISABLE KEYS */;
INSERT INTO `floodmanager_amenities` VALUES (1,'Clothes'),(2,'Food'),(3,'Medicine');
/*!40000 ALTER TABLE `floodmanager_amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_department`
--

DROP TABLE IF EXISTS `floodmanager_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `deptname` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`deptname`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_department`
--

LOCK TABLES `floodmanager_department` WRITE;
/*!40000 ALTER TABLE `floodmanager_department` DISABLE KEYS */;
INSERT INTO `floodmanager_department` VALUES (4,''),(12,'Admin'),(11,'Maintenance '),(1,'Maintenance Department'),(9,'test');
/*!40000 ALTER TABLE `floodmanager_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_designation`
--

DROP TABLE IF EXISTS `floodmanager_designation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_designation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_designation`
--

LOCK TABLES `floodmanager_designation` WRITE;
/*!40000 ALTER TABLE `floodmanager_designation` DISABLE KEYS */;
INSERT INTO `floodmanager_designation` VALUES (3,'Admin'),(2,'Manager'),(1,'Relief Coordinator');
/*!40000 ALTER TABLE `floodmanager_designation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_emergencysupply`
--

DROP TABLE IF EXISTS `floodmanager_emergencysupply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_emergencysupply` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_emergencysupply`
--

LOCK TABLES `floodmanager_emergencysupply` WRITE;
/*!40000 ALTER TABLE `floodmanager_emergencysupply` DISABLE KEYS */;
INSERT INTO `floodmanager_emergencysupply` VALUES (1,'Medikit');
/*!40000 ALTER TABLE `floodmanager_emergencysupply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_evacuationlocation`
--

DROP TABLE IF EXISTS `floodmanager_evacuationlocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_evacuationlocation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_evacuationlocation`
--

LOCK TABLES `floodmanager_evacuationlocation` WRITE;
/*!40000 ALTER TABLE `floodmanager_evacuationlocation` DISABLE KEYS */;
INSERT INTO `floodmanager_evacuationlocation` VALUES (1,'ktm'),(2,'Thiruvalla'),(3,'Konni');
/*!40000 ALTER TABLE `floodmanager_evacuationlocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_evacuationrecord`
--

DROP TABLE IF EXISTS `floodmanager_evacuationrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_evacuationrecord` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `evacuationdate` date NOT NULL,
  `evacuationtime` time(6) NOT NULL,
  `people_evacuated` int NOT NULL,
  `evacuation_center` varchar(255) NOT NULL,
  `contact_person` varchar(255) NOT NULL,
  `contact_number` varchar(15) NOT NULL,
  `emergency_supply_id` bigint NOT NULL,
  `location_id` bigint NOT NULL,
  `transport_method_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `floodmanager_evacuat_emergency_supply_id_8b448e54_fk_floodmana` (`emergency_supply_id`),
  KEY `floodmanager_evacuat_location_id_9ab820ad_fk_floodmana` (`location_id`),
  KEY `floodmanager_evacuat_transport_method_id_c6e384f3_fk_floodmana` (`transport_method_id`),
  CONSTRAINT `floodmanager_evacuat_emergency_supply_id_8b448e54_fk_floodmana` FOREIGN KEY (`emergency_supply_id`) REFERENCES `floodmanager_emergencysupply` (`id`),
  CONSTRAINT `floodmanager_evacuat_location_id_9ab820ad_fk_floodmana` FOREIGN KEY (`location_id`) REFERENCES `floodmanager_evacuationlocation` (`id`),
  CONSTRAINT `floodmanager_evacuat_transport_method_id_c6e384f3_fk_floodmana` FOREIGN KEY (`transport_method_id`) REFERENCES `floodmanager_transportmethod` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_evacuationrecord`
--

LOCK TABLES `floodmanager_evacuationrecord` WRITE;
/*!40000 ALTER TABLE `floodmanager_evacuationrecord` DISABLE KEYS */;
INSERT INTO `floodmanager_evacuationrecord` VALUES (2,'2025-02-09','02:29:00.000000',86,'ptm','amal','5679965434',1,1,1);
/*!40000 ALTER TABLE `floodmanager_evacuationrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_householdmember`
--

DROP TABLE IF EXISTS `floodmanager_householdmember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_householdmember` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `familyid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `floodmanager_househo_familyid_id_944a1bb8_fk_floodmana` (`familyid_id`),
  CONSTRAINT `floodmanager_househo_familyid_id_944a1bb8_fk_floodmana` FOREIGN KEY (`familyid_id`) REFERENCES `floodmanager_staffuserregistration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_householdmember`
--

LOCK TABLES `floodmanager_householdmember` WRITE;
/*!40000 ALTER TABLE `floodmanager_householdmember` DISABLE KEYS */;
INSERT INTO `floodmanager_householdmember` VALUES (1,'kl','8909876777',1),(2,'km','7689098767',1),(5,'kl','8909876777',3),(6,'sona','2345677888',5),(7,'Sona ','98765433433',6),(8,'Sona m','1234567890',7),(9,'SoNa','9087654323',12),(10,'nipun','9876543210',15),(11,'chuttkii','345',18),(12,'bheem','87654',18),(13,'manu','1234567890',19);
/*!40000 ALTER TABLE `floodmanager_householdmember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_location`
--

DROP TABLE IF EXISTS `floodmanager_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_location` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_location`
--

LOCK TABLES `floodmanager_location` WRITE;
/*!40000 ALTER TABLE `floodmanager_location` DISABLE KEYS */;
INSERT INTO `floodmanager_location` VALUES (1,'Konni'),(2,'TVLA'),(3,'Mallapally'),(4,'PTM Town');
/*!40000 ALTER TABLE `floodmanager_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_ngo`
--

DROP TABLE IF EXISTS `floodmanager_ngo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_ngo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ngo_name` varchar(255) NOT NULL,
  `contact_person` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `address` longtext NOT NULL,
  `mission` longtext NOT NULL,
  `website` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_ngo`
--

LOCK TABLES `floodmanager_ngo` WRITE;
/*!40000 ALTER TABLE `floodmanager_ngo` DISABLE KEYS */;
INSERT INTO `floodmanager_ngo` VALUES (6,'jaya','jaya','jaya@123.com','98767','jaya home','request for medicine','www.google.com'),(7,'amal','Arun p','arun.pkumar@saintgits.org','08129400674','who','request','www.who.com'),(8,'prithi','john wick','weick@gmail.com','09754456','wick ','request for AID','www.wick.com');
/*!40000 ALTER TABLE `floodmanager_ngo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_rainfallintensity`
--

DROP TABLE IF EXISTS `floodmanager_rainfallintensity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_rainfallintensity` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rainfall_id` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `rainfall_intensity` double NOT NULL,
  `location_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `floodmanager_rainfal_location_id_460ad675_fk_floodmana` (`location_id`),
  CONSTRAINT `floodmanager_rainfal_location_id_460ad675_fk_floodmana` FOREIGN KEY (`location_id`) REFERENCES `floodmanager_rainfalllocation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_rainfallintensity`
--

LOCK TABLES `floodmanager_rainfallintensity` WRITE;
/*!40000 ALTER TABLE `floodmanager_rainfallintensity` DISABLE KEYS */;
INSERT INTO `floodmanager_rainfallintensity` VALUES (2,'6','2025-02-11','15:24:00.000000',7,3);
/*!40000 ALTER TABLE `floodmanager_rainfallintensity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_rainfalllocation`
--

DROP TABLE IF EXISTS `floodmanager_rainfalllocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_rainfalllocation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_rainfalllocation`
--

LOCK TABLES `floodmanager_rainfalllocation` WRITE;
/*!40000 ALTER TABLE `floodmanager_rainfalllocation` DISABLE KEYS */;
INSERT INTO `floodmanager_rainfalllocation` VALUES (1,'PTM'),(2,'KTM'),(3,'ekm');
/*!40000 ALTER TABLE `floodmanager_rainfalllocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_reliefcamp`
--

DROP TABLE IF EXISTS `floodmanager_reliefcamp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_reliefcamp` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `capacity` int unsigned NOT NULL,
  `current_occupants` int unsigned NOT NULL,
  `contact_person` varchar(255) NOT NULL,
  `contact_number` varchar(15) NOT NULL,
  `remarks` longtext,
  `amenities_id` bigint NOT NULL,
  `location_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `floodmanager_reliefc_amenities_id_80c10620_fk_floodmana` (`amenities_id`),
  KEY `floodmanager_reliefc_location_id_12ddba8b_fk_floodmana` (`location_id`),
  CONSTRAINT `floodmanager_reliefc_amenities_id_80c10620_fk_floodmana` FOREIGN KEY (`amenities_id`) REFERENCES `floodmanager_amenities` (`id`),
  CONSTRAINT `floodmanager_reliefc_location_id_12ddba8b_fk_floodmana` FOREIGN KEY (`location_id`) REFERENCES `floodmanager_location` (`id`),
  CONSTRAINT `floodmanager_reliefcamp_chk_1` CHECK ((`capacity` >= 0)),
  CONSTRAINT `floodmanager_reliefcamp_chk_2` CHECK ((`current_occupants` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_reliefcamp`
--

LOCK TABLES `floodmanager_reliefcamp` WRITE;
/*!40000 ALTER TABLE `floodmanager_reliefcamp` DISABLE KEYS */;
INSERT INTO `floodmanager_reliefcamp` VALUES (3,'PTM',20,5,'Amal','98766543','welll',1,1),(4,'PTM',20,5,'Amal','98766543','well',1,1),(5,'PTM',20,5,'Amal','98766543','Good',2,2),(6,'SH school',500,250,'Mamooty','456788999','urgent',3,3);
/*!40000 ALTER TABLE `floodmanager_reliefcamp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_staff`
--

DROP TABLE IF EXISTS `floodmanager_staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_staff` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `date_of_joining` date NOT NULL,
  `department_id` bigint NOT NULL,
  `designation_id` bigint NOT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `username` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `floodmanager_staff_department_id_42cb1ada_fk_floodmana` (`department_id`),
  KEY `floodmanager_staff_designation_id_d0257769_fk_floodmana` (`designation_id`),
  CONSTRAINT `floodmanager_staff_department_id_42cb1ada_fk_floodmana` FOREIGN KEY (`department_id`) REFERENCES `floodmanager_department` (`id`),
  CONSTRAINT `floodmanager_staff_designation_id_d0257769_fk_floodmana` FOREIGN KEY (`designation_id`) REFERENCES `floodmanager_designation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_staff`
--

LOCK TABLES `floodmanager_staff` WRITE;
/*!40000 ALTER TABLE `floodmanager_staff` DISABLE KEYS */;
INSERT INTO `floodmanager_staff` VALUES (5,'Aslam Salam','asla@saintgits.org','2025-02-11',1,1,'06235608419','1234','staff1'),(6,'sree','t@gmail.scom','2025-02-18',12,3,'8909878988','admin','admin'),(7,'ASLAM','aslams.mca2325@saintgits.org','2025-03-30',11,3,'5655677656','1234','ASLAM');
/*!40000 ALTER TABLE `floodmanager_staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_staffuserregistration`
--

DROP TABLE IF EXISTS `floodmanager_staffuserregistration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_staffuserregistration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `address` longtext,
  `dob` date DEFAULT NULL,
  `sex` varchar(6) DEFAULT NULL,
  `marital_status` varchar(9) DEFAULT NULL,
  `aadhaar_no` varchar(12) DEFAULT NULL,
  `landscape_level` varchar(200) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `occupation` varchar(200) DEFAULT NULL,
  `house_no` varchar(200) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `username` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_staffuserregistration`
--

LOCK TABLES `floodmanager_staffuserregistration` WRITE;
/*!40000 ALTER TABLE `floodmanager_staffuserregistration` DISABLE KEYS */;
INSERT INTO `floodmanager_staffuserregistration` VALUES (1,'testuser',NULL,'2025-01-27','Male','Single','1234545667','low','06235608419','nothing','1221','PTM','testuser','testuser',NULL),(3,'amal','Saintgits','2025-02-19','Male','Single','6754444444','high','05679965434','nothing','1223','PTM','amal','amal',NULL),(4,'testuser1','test','2025-02-04','Male','Single','1234545667','low','06235608419','nothing','1221','PTM','testuser1','testuser1',NULL),(5,'Nipun','mullamootil house po Ranni','2025-02-19','Male','Single','123456789','low','987654321','coder','1223','Ranni','nipun','1234',NULL),(6,'Nipun','mullamootil house','2025-02-19','Male','Married','1234545667','low','987654321','coder','1223','Ranni','staff1','1234',NULL),(7,'Nipun','Mullamootil House','2025-02-19','Male','Married','1234545667','low','987654321','coder','1223','Ranni','nipun1','12345',NULL),(8,'anand','anand house','2025-02-28','Male','Divorced','567843298','high','8975434556','programmer','8907','Mallapally','anand','1234',NULL),(12,'nipun john09','Nipun house','2025-02-23','Female','Divorced','567998654','moderate','123455','Help','78965432','Pathamuttam','nipun22','1234','nipunjohnkoshy10@gmail.com'),(13,'nipun john08','Nipun house','2025-02-23','Female','Divorced','567998654','moderate','123455','Help','78965432','Pathamuttam','nipun22','1234','nipunjohnkoshy10@gmail.com'),(14,'nipun john10',NULL,'2025-02-28','Male','Single','34567898765','moderate','123455','Help','78965432','Pathamuttam','nipun14','1234','nipunjohnkoshy10@gmail.com'),(15,'jayaraj','testaddress','2025-01-28','Male','Single','56789004','high','7510977535','Help','78965432','vennikulam','jayaraj','1234','jayu1294@gmail.com'),(17,'jayaraj125','jaya home','2025-02-23','Male','Married','56789004','high','7510977535','Help','78965432','vennikulam','raju','1234',NULL),(18,'rajjj',NULL,'2025-02-13','Female','Divorced','56789004','high','75109775378','Help','78965432','vennikulam','jayu','1234','jayu1294@gmail.com'),(19,'Sarath s nair','edasserethu thekkethil kollakadavu po kollakadavu','2000-11-15','Male','Married','125896753','high','7560911621','manager','54','alacode','sarath@12','sa123456','sarathsn.mca2325@saintgits.org'),(20,'chikoos','LAKULATHU THAZHCHAYILL KUTTAPUZHA PO THIRUVALLA','2025-03-30','Male','Single','865745737','high','09947592600','student','2234','Mallapally','ck','1234','aslamsalam8419@gmail.com');
/*!40000 ALTER TABLE `floodmanager_staffuserregistration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_transportmethod`
--

DROP TABLE IF EXISTS `floodmanager_transportmethod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_transportmethod` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_transportmethod`
--

LOCK TABLES `floodmanager_transportmethod` WRITE;
/*!40000 ALTER TABLE `floodmanager_transportmethod` DISABLE KEYS */;
INSERT INTO `floodmanager_transportmethod` VALUES (1,'BUS'),(2,'Car'),(3,'Helicopter'),(4,'Bike'),(5,'Taurus'),(6,'Cycle');
/*!40000 ALTER TABLE `floodmanager_transportmethod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_watersource`
--

DROP TABLE IF EXISTS `floodmanager_watersource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_watersource` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `source_name` varchar(255) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `water_level` double NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  `water_status_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `floodmanager_waterso_water_status_id_393d5221_fk_floodmana` (`water_status_id`),
  CONSTRAINT `floodmanager_waterso_water_status_id_393d5221_fk_floodmana` FOREIGN KEY (`water_status_id`) REFERENCES `floodmanager_waterstatus` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_watersource`
--

LOCK TABLES `floodmanager_watersource` WRITE;
/*!40000 ALTER TABLE `floodmanager_watersource` DISABLE KEYS */;
INSERT INTO `floodmanager_watersource` VALUES (2,'Dam','PTM',20,'2025-02-12 06:31:51.267260',1),(3,'River','KTM',100,'2025-02-12 07:06:36.624828',2);
/*!40000 ALTER TABLE `floodmanager_watersource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_waterstatus`
--

DROP TABLE IF EXISTS `floodmanager_waterstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_waterstatus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_waterstatus`
--

LOCK TABLES `floodmanager_waterstatus` WRITE;
/*!40000 ALTER TABLE `floodmanager_waterstatus` DISABLE KEYS */;
INSERT INTO `floodmanager_waterstatus` VALUES (1,'LOW'),(2,'high'),(3,'moderate');
/*!40000 ALTER TABLE `floodmanager_waterstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floodmanager_weather`
--

DROP TABLE IF EXISTS `floodmanager_weather`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `floodmanager_weather` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `location` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `temperature` double DEFAULT NULL,
  `humidity` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floodmanager_weather`
--

LOCK TABLES `floodmanager_weather` WRITE;
/*!40000 ALTER TABLE `floodmanager_weather` DISABLE KEYS */;
INSERT INTO `floodmanager_weather` VALUES (2,'KTM','2025-02-06',22,94);
/*!40000 ALTER TABLE `floodmanager_weather` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-04 10:38:24
