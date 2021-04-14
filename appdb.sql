-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: appdb
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `author` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `image` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (1,'Thomas Harris','assets/img/140x140/img1.jpg'),(2,'Higashino Keigo','assets/img/140x140/img2.jpg'),(3,'Haruki Murakami','assets/img/140x140/img3.jpg'),(4,'Masashi Kishimoto','assets/img/140x140/img4.jpg'),(5,'Jeffrey Archer','assets/img/140x140/img5.jpg'),(6,'Sir Arthur Conan Doyle','assets/img/140x140/img6.jpg'),(7,'Agatha Christie','assets/img/140x140/img7.jpg'),(8,'Nguyễn Nhật Ánh','assets/img/140x140/img8.jpg'),(9,'Fumiyo Kono',NULL),(10,'Maita Yohei',NULL),(11,'Bộ Giáo Dục Và Đào Tạo',NULL),(12,'Gosho Aoyama',NULL);
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_520_ci,
  `description` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `image` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Sự Im Lặng Của Bầy Cừu',NULL,'Bìa mềm','assets/img/book_img/img6.jpg',115000),(2,'Án Mạng Mười Một Chữ',NULL,'Bìa mềm','assets/img/book_img/img8.jpg',110000),(3,'Rừng Nauy (Tái Bản 2018)',NULL,'Bìa mềm','assets/img/book_img/img1.jpg',128000),(4,'Naruto Tập 43',NULL,'Bìa mềm','assets/img/book_img/img12.jpg',22000),(5,'Hai Số Phận',NULL,'Bìa Cứng','assets/img/book_img/img4.jpg',175000),(6,'Sherlock Holmes (Trọn Bộ 3 Cuốn)',NULL,'Bìa mềm','assets/img/book_img/img7.jpg',345000),(7,'Án Mạng Trên Chuyến Tàu Tốc Hành Phương Đông',NULL,'Bìa mềm','assets/img/book_img/img2.jpg',110000),(8,'Tôi Thấy Hoa Vàng Trên Cỏ Xanh',NULL,'Bìa mềm','assets/img/book_img/img5.jpg',125000),(9,'Mắt Biếc',NULL,'Bìa mềm','assets/img/book_img/img11.jpg',110000),(10,'Ở Một Góc Nhân Gian',NULL,'Bìa mềm','assets/img/book_img/img13.jpg',80000),(11,'Toán 2',NULL,'Bìa mềm','assets/img/book_img/img9.jpg',13000),(12,'Sách Giáo Khoa Bộ Lớp 9 (Bộ 12 Cuốn)',NULL,'Bìa mềm','assets/img/book_img/img10.jpg',136000),(13,'Thám Tử Lừng Danh Conan - Tập 97',NULL,'Bìa mềm','assets/img/book_img/img3.jpg',20000);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_author`
--

DROP TABLE IF EXISTS `book_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_author` (
  `book_id` int NOT NULL,
  `author_id` int NOT NULL,
  PRIMARY KEY (`book_id`,`author_id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `book_author_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`),
  CONSTRAINT `book_author_ibfk_2` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_author`
--

LOCK TABLES `book_author` WRITE;
/*!40000 ALTER TABLE `book_author` DISABLE KEYS */;
INSERT INTO `book_author` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,8),(10,9),(10,10),(11,11),(12,11),(13,12);
/*!40000 ALTER TABLE `book_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_cate`
--

DROP TABLE IF EXISTS `book_cate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_cate` (
  `book_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`book_id`,`category_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `book_cate_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`),
  CONSTRAINT `book_cate_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_cate`
--

LOCK TABLES `book_cate` WRITE;
/*!40000 ALTER TABLE `book_cate` DISABLE KEYS */;
INSERT INTO `book_cate` VALUES (3,1),(8,1),(9,1),(10,1),(1,4),(2,4),(6,4),(7,4),(4,6),(13,6),(11,7),(12,7),(5,9);
/*!40000 ALTER TABLE `book_cate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_image`
--

DROP TABLE IF EXISTS `book_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_image` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `book_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `book_image_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_image`
--

LOCK TABLES `book_image` WRITE;
/*!40000 ALTER TABLE `book_image` DISABLE KEYS */;
/*!40000 ALTER TABLE `book_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Tiểu thuyết'),(2,'Truyện ngắn'),(3,'Light Novel'),(4,'Truyện trinh thám'),(5,'Truyện kiếm hiệp'),(6,'Manga - Comic'),(7,'Sách giáo khoa'),(8,'Sách tham khảo'),(9,'Tác phẩm kinh điển');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `username` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `password` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `username_2` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detail_inventory_report`
--

DROP TABLE IF EXISTS `detail_inventory_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detail_inventory_report` (
  `report_id` int NOT NULL,
  `book_id` int NOT NULL,
  `quantity_before` int DEFAULT NULL,
  `quantity_after` int DEFAULT NULL,
  `arise` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`report_id`,`book_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `detail_inventory_report_ibfk_1` FOREIGN KEY (`report_id`) REFERENCES `inventory_report` (`id`),
  CONSTRAINT `detail_inventory_report_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail_inventory_report`
--

LOCK TABLES `detail_inventory_report` WRITE;
/*!40000 ALTER TABLE `detail_inventory_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `detail_inventory_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detail_invoice`
--

DROP TABLE IF EXISTS `detail_invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detail_invoice` (
  `invoice_id` int NOT NULL,
  `book_id` int NOT NULL,
  `quantity` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`invoice_id`,`book_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `detail_invoice_ibfk_1` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`),
  CONSTRAINT `detail_invoice_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail_invoice`
--

LOCK TABLES `detail_invoice` WRITE;
/*!40000 ALTER TABLE `detail_invoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `detail_invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_report`
--

DROP TABLE IF EXISTS `inventory_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `report_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_report`
--

LOCK TABLES `inventory_report` WRITE;
/*!40000 ALTER TABLE `inventory_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date_of_invoice` date DEFAULT NULL,
  `total` float DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `username` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `password` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `joined_date` date DEFAULT NULL,
  `user_role` enum('USER','ADMIN') COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `username_2` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Duc Bang','abc@gmail.com','admin123','$2b$15$lms2Ym.cESGtAv8h3cu.vOzLvJfT0LSX/J8wZKCyPyQ3YFuX1idBG',1,'2021-04-10','ADMIN'),(2,'Van Trung','trung123@gmail.com','trung123','$2b$15$Vntfv7CjBCt8kGptf8Btvu5yQUkSkXThaXnnp/bxNhRskTLxRqRJ.',1,'2021-04-10','USER'),(3,'Anh Khoa','Khoa123@gmail.com','khoa123','$2b$15$4WEA89IQw7BltfyXU4V7mOor3sHajNP7lhKt/C8p6N8S6oVylKrey',1,'2021-04-10','USER');
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

-- Dump completed on 2021-04-14 10:40:15
