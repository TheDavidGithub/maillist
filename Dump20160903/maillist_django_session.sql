CREATE DATABASE  IF NOT EXISTS `maillist` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `maillist`;
-- MySQL dump 10.13  Distrib 5.5.50, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: maillist
-- ------------------------------------------------------
-- Server version	5.5.50-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3ktud5h74mm3lbw80climsj3q7kye1yl','YTIwNTE3YzE0NDIyNjBiNWZjYTQ5NzQ5M2ZhNThiNzUxODEyODg3YTp7fQ==','2016-09-17 13:15:36'),('chn06a076f0f0b707ed401d9db251149','OGZjMjhhYzQ3MzczMWY2OWQyZmFjNzc5MzA1MWZkY2ZkNmZjNDI3Njp7InVzZXIiOjF9','2016-09-17 13:15:36'),('chn56fa047cd134913f85dbafc436ecb','OGZjMjhhYzQ3MzczMWY2OWQyZmFjNzc5MzA1MWZkY2ZkNmZjNDI3Njp7InVzZXIiOjF9','2016-09-17 13:15:38'),('chn8c1050799bff2f2db08e6ea038ab0','YTIwNTE3YzE0NDIyNjBiNWZjYTQ5NzQ5M2ZhNThiNzUxODEyODg3YTp7fQ==','2016-09-17 13:15:36'),('dkrvrexgp8z9aclphl7mo9suykeo1vy0','YTIwNTE3YzE0NDIyNjBiNWZjYTQ5NzQ5M2ZhNThiNzUxODEyODg3YTp7fQ==','2016-09-17 13:15:36'),('q7qc56rciwspa65mirjcz2bktnf72k6l','YTIwNTE3YzE0NDIyNjBiNWZjYTQ5NzQ5M2ZhNThiNzUxODEyODg3YTp7fQ==','2016-09-17 13:15:38');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-03 21:16:46
