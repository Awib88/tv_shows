CREATE DATABASE  IF NOT EXISTS `tv_shows` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tv_shows`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: tv_shows
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
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `show_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`user_id`,`show_id`),
  KEY `fk_users_has_shows_shows1_idx` (`show_id`),
  KEY `fk_users_has_shows_users1_idx` (`user_id`),
  CONSTRAINT `fk_users_has_shows_shows1` FOREIGN KEY (`show_id`) REFERENCES `shows` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_users_has_shows_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (2,1,9,'2023-07-18 03:36:08','2023-07-18 03:36:08'),(3,2,9,'2023-07-18 03:36:22','2023-07-18 03:36:22'),(4,2,3,'2023-07-18 03:36:43','2023-07-18 03:36:43'),(5,2,8,'2023-07-18 03:37:20','2023-07-18 03:37:20'),(6,2,3,'2023-07-18 03:37:31','2023-07-18 03:37:31'),(7,3,3,'2023-07-18 03:37:40','2023-07-18 03:37:40'),(8,3,4,'2023-07-18 03:38:00','2023-07-18 03:38:00'),(12,2,10,'2023-07-18 08:57:44','2023-07-18 08:57:44'),(16,1,6,'2023-07-18 08:58:32','2023-07-18 08:58:32'),(19,3,6,'2023-07-18 12:27:58','2023-07-18 12:27:58'),(20,4,4,'2023-07-18 12:29:54','2023-07-18 12:29:54'),(21,4,11,'2023-07-18 12:29:57','2023-07-18 12:29:57'),(22,4,6,'2023-07-18 12:29:59','2023-07-18 12:29:59'),(23,4,10,'2023-07-18 12:30:01','2023-07-18 12:30:01'),(25,2,11,'2023-07-18 12:35:01','2023-07-18 12:35:01'),(26,1,14,'2023-07-18 12:37:16','2023-07-18 12:37:16');
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shows`
--

DROP TABLE IF EXISTS `shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shows` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `title` varchar(128) DEFAULT NULL,
  `network` varchar(128) DEFAULT NULL,
  `release_date` date DEFAULT NULL,
  `type` varchar(128) DEFAULT 'unspecified',
  `age_limit` varchar(128) DEFAULT 'unspecified',
  `description` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_shows_users_idx` (`user_id`),
  CONSTRAINT `fk_shows_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shows`
--

LOCK TABLES `shows` WRITE;
/*!40000 ALTER TABLE `shows` DISABLE KEYS */;
INSERT INTO `shows` VALUES (3,1,'Sleepy Hollow','UCN','2023-06-26','Series','-16','sdfghjhgfdsdfghjhgfdsqs','2023-07-18 02:43:01','2023-07-18 02:43:01'),(4,1,'Game of thrones','CBS','2007-07-01','Series','-18','gfdsdfghjkjhgfdsdfgh','2023-07-18 02:50:14','2023-07-18 02:50:14'),(6,2,'Shadows','artwork','2023-07-13','2','1','fghjklkdfklkgfg','2023-07-18 03:26:47','2023-07-18 12:34:51'),(8,3,'Bus Wrack','Ford inc.','2023-07-10','1','3','dfghjklkjhgfghjk','2023-07-18 03:30:40','2023-07-18 12:26:25'),(9,3,'Drug dealers','Ford inc.','2023-07-10','Documentary','-18','dfghjklxcvbnfghjk','2023-07-18 03:31:19','2023-07-18 03:31:19'),(10,3,'Zonzon','Ford inc.','2023-07-11','Animation','- Family-friendly','sdfghjhgfdsqsdf','2023-07-18 03:53:39','2023-07-18 03:53:39'),(11,3,'Facebook history','ArtTV','2023-06-26','Documentary','- Family-friendly','tretssbshbdsbdhbsdhbdj','2023-07-18 12:07:57','2023-07-18 12:07:57'),(13,4,'Guy movie!','Sensei Guy prod','2023-07-04','Documentary','- Family-friendly','QSDFGHJKJHGF','2023-07-18 12:32:24','2023-07-18 12:32:24'),(14,2,'Love Story','zeze media','2023-07-02','Animation','-16','sdfghjkjhgfdsdfghjkjhgfds','2023-07-18 12:36:19','2023-07-18 12:36:19');
/*!40000 ALTER TABLE `shows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Amin','Wahib','test@gmail.com','$2b$12$LqBHR7Oca0I0OQPP/4q0YOtinG0H.b88194lc/doG3VtZOuSc.52u','2023-07-18 02:21:12','2023-07-18 02:21:12'),(2,'Zeinab','Matata','test01@gmail.com','$2b$12$0umntEbH0LXl3i9gDpVal.7oJhM0364JZ08u7z5v7u7gqUXG3xVsO','2023-07-18 03:20:30','2023-07-18 03:20:30'),(3,'Ford','Rover','ford@gmail.com','$2b$12$XdExMws0flHV/UdKCJ8/fuIYvB/OzCxm0HnIsRqwbOgVJKfki0vji','2023-07-18 03:28:37','2023-07-18 03:28:37'),(4,'Guy ','Dude','dude@gmail.com','$2b$12$jBpTpWK4McWuFSZ5fnBFu.8Pf8o0tM3mp5vzFzVpZvNg3CvMnp3su','2023-07-18 12:29:47','2023-07-18 12:29:47');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-18 12:54:01
