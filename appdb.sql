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
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Sự Im Lặng Của Bầy Cừu','Những cuộc phỏng vấn ở xà lim với kẻ ăn thịt người ham thích trò đùa trí tuệ, những tiết lộ nửa chừng hắn chỉ dành cho kẻ nào thông minh, những cái nhìn xuyên thấu thân phận và suy tư của cô mà đôi khi cô muốn lảng tránh... Clarice Starling đã dấn thân vào cuộc điều tra án giết người lột da hàng loạt như thế, để rồi trong tiếng bức bối của chiếc đồng hồ đếm ngược về cái chết, cô phải vật lộn để chấm dứt tiếng kêu bao lâu nay vẫn đeo đẳng giấc mơ mình: tiếng kêu của bầy cừu sắp bị đem đi giết thịt.Sự im lặng của bầy cừu hội tụ đầy đủ những yếu tố làm nên một cuốn tiểu thuyết trinh thám kinh dị xuất sắc nhất: không một dấu vết lúng túng trong những chi tiết thuộc lĩnh vực chuyên môn, với các tình tiết giật gân, cái chết luôn lơ lửng, với cuộc so găng của những bộ óc lớn mà không có chỗ cho kẻ ngu ngốc để cuộc chơi trí tuệ trở nên dễ dàng. Bồi đắp vào cốt truyện lôi cuốn đó là cơ hội được trải nghiệm trong trí não của cả kẻ gây tội lẫn kẻ thi hành công lý, khi mỗi bên phải vật vã trong ngục tù của đau đớn để tìm kiếm, khẩn thiết và liên tục, một sự lắng dịu cho tâm hồn.','Bìa mềm','assets/img/book_img/img6.jpg',115000,37),(2,'Án Mạng Mười Một Chữ','Tình cờ phát hiện những điều bất thường sau cái chết thảm khốc của người yêu, nhân vật “tôi”, một nữ nhà văn viết tiểu thuyết trinh thám đã cùng bạn mình, Hagio Fuyuko, cũng là biên tập viên phụ trách sách của “tôi” quyết định điều tra về cái chết này. Trong quá trình điều tra hai người phát hiện người yêu của “tôi” đã từng gặp tai nạn lật thuyền trong chuyến du lịch đảo một năm trước. Và khi họ tìm tới những người cũng tham gia chuyến đi đó để tìm hiểu thì những người này cũng lần lượt bị sát hại. Cuối cùng “tôi” buộc phải tự mình phán đoán, điều tra để tìm ra chân tướng sự việc.','Bìa mềm','assets/img/book_img/img8.jpg',110000,0),(3,'Rừng Nauy (Tái Bản 2018)','Bất chợt lắng nghe bài hát mà nàng vẫn ưa thích nhất của Beatles, Toru Watanbe hồi tưởng lại mối tình đầu của mình với Naoko, người yêu của người bạn thân nhất là Kizuki. Ký ức ngay lập tức mang anh trở về những ngày sinh viên của 20 năm trước , ở Tokyo, những ngày chơi vơi trong một thế giới của tình bạn khó khăn, của tình dục buông thả, của đam mê mầt mát, trở về cái thời mà một cô gái mạnh mẽ tên là Modori đã bước vào cuộc đời anh, khiến anh phải chọn lựa, hoặc tương lai, hoặc quá khứ...\nCùng thoát thai từ nỗi buồn thương trong sáng về tồn tại, Rừng Na Uy, bài hát năm nào của Beatles, đã được lấy làm tên gọi cho cuốn tiểu thuyết tình yêu ngọt ngào và u sầu của Haruki Murakami. Bước vào cõi sống của Rừng Na Uy, qua sự sớm cô đơn như định mệnh của những người trẻ tuổi, qua mối tình tay ba vừa quấn quýt xác thân vừa u mặc sầu bi của Naoko-Toru-Midori, người ta cảm thấy ngỡ ngàng trước tình yêu như là nơi trú ngụ duy nhất của người đàn ông và người đàn bà trên thế gian này, và khám phá ra một nỗi buồn mênh mang, trống vắng rất Nhật Bản của thời hiện đại. Trong nỗi ưu tư và cô đơn như một định mệnh đã cài đặt nơi những người mới lớn, trong sự tuyệt vọng của những tâm hồn trong sáng sẵn sàng hy sinh thân mình để khỏi thoả hiệp với cuộc sống thế gian. Và tình yêu đã là nơi trú ngụ duy nhất. tình yêu và sự giải phóng của xác thân bao bọc lấy nó, làm cho người đàn ông và người đàn bà có thể yêu nhau với tất cả những gì có thể trước cuộc đời ngắn ngủi và quý giá. Với ý nghĩa đó, mối tình tay ba Naoko-Toru-Midori đã lay động hàng chục triệu độc giả trên toàn thề giới trong một tác phẩm được coi là tuyệt bút của Murakami.','Bìa mềm','assets/img/book_img/img1.jpg',128000,87),(4,'Naruto Tập 43','Tuyệt đối không thể tránh khỏi thuật này! Sasuke tung đòn cuối hòng dẫn dụ “Amaterasu” của Itachi! Trong lúc bị mây giông bủa vây, thuật Sasuke vừa phóng ra liệu có vượt nổi Itachi!? Cùng lúc ấy, đội Naruto cũng bị “Akatsuki” ngáng đường, cả bọn đã đứng ra liều mình ngăn cản Tobi!','Bìa mềm','assets/img/book_img/img12.jpg',22000,40),(5,'Hai Số Phận','“Hai số phận” (Kane & Abel) là câu chuyện về hai người đàn ông đi tìm vinh quang. William Kane là con một triệu phú nổi tiếng trên đất Mỹ, lớn lên trong nhung lụa của thế giới thượng lưu. Wladek Koskiewicz là đứa trẻ không rõ xuất thân, được gia đình người bẫy thú nhặt về nuôi. Một người được ấn định để trở thành chủ ngân hàng khi lớn lên, người kia nhập cư vào Mỹ cùng đoàn người nghèo khổ.\n \nTrải qua hơn sáu mươi năm với biết bao biến động, hai con người giàu hoài bão miệt mài xây dựng vận mệnh của mình . “Hai số phận” nói về nỗi khát khao cháy bỏng, những nghĩa cử, những mối thâm thù, từng bước đường phiêu lưu, hiện thực thế giới và những góc khuất... mê hoặc người đọc bằng ngôn từ cô đọng, hai mạch truyện song song được xây dựng tinh tế từ những chi tiết nhỏ nhất.','Bìa Cứng','assets/img/book_img/img4.jpg',175000,49),(6,'Sherlock Holmes (Trọn Bộ 3 Cuốn)','Nhân vật Sherlock Holmes từ lâu đã trở thành nguồn cảm hứng cho hàng trăm, hàng ngàn tác phẩm ở nhiều loại hình nghệ thuật khác: từ âm nhạc, ca kịch đến điện ảnh… Bộ sách Sherlock Holmes toàn tập (boxset trọn bộ 3 tập) một lần nữa mang đến cho người đọc cơ hội được nhìn ngắm, ngưỡng mộ và đánh giá nhân vật độc đáo của nhà văn tài năng Conan Doyle. Chân dung cuộc đời, sự nghiệp và nhân cách của Sherlock Holmes chưa bao giờ được tái hiện chân thực, đầy đủ và sống động đến thế… Chỉ từ một giọt nước, người giỏi suy luận có thể đoán ra rất nhiều chuyện liên quan đến một thác nước hay một đại dương dù họ chưa bao giờ tận mắt nhìn thấy chúng. Như vậy, cuộc sống là một chuỗi mắt xích rộng lớn nhất của nó, nếu ta biết được một mắt xích. Như tất cả mọi khoa học khác, “suy đoán và phân tích” là một khoa học mà ta chỉ có thể làm chủ nó sau một quá trình nghiên cứu dài lâu, bền bỉ.','Bìa mềm','assets/img/book_img/img7.jpg',345000,50),(7,'Án Mạng Trên Chuyến Tàu Tốc Hành Phương Đông','Kẻ sát nhân đang đồng hành cùng chúng ta – trên chuyến tàu này…”\n\n\nVừa quá nửa đêm, chuyến tàu tốc hành phương Đông nổi tiếng buộc phải ngừng lại vì tuyết rơi quá dày. Vào buổi sáng, tay triệu phú Simon Ratchett được phát hiện nằm chết trong toa riêng của mình với mười hai nhát dao, cửa khoang được khóa từ bên trong. Một trong những hành khách có mặt trên chuyến tàu là thủ phạm.\n\n\nMột mình giữa cơn bão tuyết cùng nhân dạng mù mờ về tên sát nhân qua lời chứng của mọi người, thám tử Hercule Poirot phải tìm ra chân tướng kẻ thủ ác giữa mười hai kẻ thù của nạn nhân, trước khi tên giết người kịp đào thoát…','Bìa mềm','assets/img/book_img/img2.jpg',110000,49),(8,'Tôi Thấy Hoa Vàng Trên Cỏ Xanh','Những câu chuyện nhỏ xảy ra ở một ngôi làng nhỏ: chuyện người, chuyện cóc, chuyện ma, chuyện công chúa và hoàng tử , rồi chuyện đói ăn, cháy nhà, lụt lội,... Bối cảnh là trường học, nhà trong xóm, bãi tha ma. Dẫn chuyện là cậu bé 15 tuổi tên Thiều. Thiều có chú ruột là chú Đàn, có bạn thân là cô bé Mận. Nhưng nhân vật đáng yêu nhất lại là Tường, em trai Thiều, một cậu bé học không giỏi. Thiều, Tường và những đứa trẻ sống trong cùng một làng, học cùng một trường, có biết bao chuyện chung. Chúng nô đùa, cãi cọ rồi yêu thương nhau, cùng lớn lên theo năm tháng, trải qua bao sự kiện biến cố của cuộc đời.\n\nTác giả vẫn giữ cách kể chuyện bằng chính giọng trong sáng hồn nhiên của trẻ con. 81 chương ngắn là 81 câu chuyện hấp dẫn với nhiều chi tiết thú vị, cảm động, có những tình tiết bất ngờ, từ đó lộ rõ tính cách người. Cuốn sách, vì thế, có sức ám ảnh.','Bìa mềm','assets/img/book_img/img5.jpg',125000,50),(9,'Mắt Biếc','Mắt biếc là một tác phẩm được nhiều người bình chọn là hay nhất của nhà văn Nguyễn Nhật Ánh. Tác phẩm này cũng đã được dịch giả Kato Sakae dịch sang tiếng Nhật để giới thiệu với độc giả Nhật Bản.\n\n\n“Tôi gửi tình yêu cho mùa hè, nhưng mùa hè không giữ nổi. Mùa hè chỉ biết ra hoa, phượng đỏ sân trường và tiếng ve nỉ non trong lá. Mùa hè ngây ngô, giống như tôi vậy. Nó chẳng làm được những điều tôi ký thác. Nó để Hà Lan đốt tôi, đốt rụi. Trái tim tôi cháy thành tro, rơi vãi trên đường về.”\n\n\n… Bởi sự trong sáng của một tình cảm, bởi cái kết thúc buồn, rất buồn khi xuyên suốt câu chuyện vẫn là những điều vui, buồn lẫn lộn… ','Bìa mềm','assets/img/book_img/img11.jpg',110000,50),(10,'Ở Một Góc Nhân Gian','Mười hai năm trước, cô bé và cậu bé tình cờ quen nhau qua một lần gặp nạn và thoát nạn. Trong mười năm tiếp theo, họ trải qua nhịp sống bình tĩnh điểm chút lãng mạn tuổi hoa niên ở hậu phương. Khi chiến tranh leo thang, hậu phương dần bị đẩy lên thành tiền tuyến, khói lửa đập nát không khí bình tĩnh, tuổi trưởng thành xua đuổi mơ mộng hoa niên… cũng là lúc dòng đời xô đẩy cho họ gặp lại nhau, cùng tạo dựng một góc nhỏ chèo chống giữa nhân gian đầy biến động.\n\n\nSử dụng cách kể lời ít ý nhiều, lấy nhỏ tả lớn, lồng ghép tưởng tượng vào hiện thực, Ở một góc nhân gian là cánh cửa mở vào giữa chiến địa hung tàn một cách nhẹ nhàng nhưng lại trực tiếp, kiên cường, và vô cùng thấm thía.','Bìa mềm','assets/img/book_img/img13.jpg',80000,50),(11,'Toán 2','Sách giáo khoa Toán 2 - (2020)','Bìa mềm','assets/img/book_img/img9.jpg',13000,50),(12,'Sách Giáo Khoa Bộ Lớp 9 (Bộ 12 Cuốn)','Sách Giáo Khoa Bộ Lớp 9 - Sách Bài Học (Bộ 11 Cuốn) (2020)','Bìa mềm','assets/img/book_img/img10.jpg',136000,50),(13,'Thám Tử Lừng Danh Conan - Tập 97','Conan, Mori Kogoro, Amuro Toru, và Wakita Kanenori.\n\n\nBộ tứ kì lạ ấy cùng nhau đi tới một nhà thờ bỏ hoang ẩn mình trong núi sâu ở Nagano.\n\n\nPhải chăng chờ đợi họ ở đó là những án mạng và những mật mã bí ẩn!?\n\n\nGiữa lúc ấy, Conan cố gắng tìm kiếm gợi ý quan trọng liên quan tới chân tướng của “RUM” từ Amuro…!','Bìa mềm','assets/img/book_img/img3.jpg',20000,50),(16,'Naruto Tập 1','Chuyện xảy ra ở làng Lá với nhân vật chính là Naruto, học sinh trường đào tạo Ninja, chuyên đi quấy rối khắp làng!! Naruto có một ước mơ to lớn là đạt được danh hiệu Hokage - Một vị trí dành cho Ninja ưu tú nhất - Và vượt qua các Ninja tiền nhiệm. Tuy nhiên, bí mật về thân thế của Naruto là…!?','Bìa mềm','assets/img/book_img/img14.jpg',20900,50);
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
INSERT INTO `book_author` VALUES (1,1),(2,2),(3,3),(4,4),(16,4),(5,5),(6,6),(7,7),(8,8),(9,8),(10,9),(10,10),(11,11),(12,11),(13,12);
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
INSERT INTO `book_cate` VALUES (3,1),(8,1),(9,1),(10,1),(1,4),(2,4),(6,4),(7,4),(4,6),(13,6),(16,6),(11,7),(12,7),(5,9);
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_image`
--

LOCK TABLES `book_image` WRITE;
/*!40000 ALTER TABLE `book_image` DISABLE KEYS */;
INSERT INTO `book_image` VALUES (1,'assets/img/300x452/img6.jpg',1),(2,'assets/img/300x452/img8.jpg',2),(3,'assets/img/300x452/img1.jpg',3),(4,'assets/img/300x452/img12.jpg',4),(5,'assets/img/300x452/img4.jpg',5),(6,'assets/img/300x452/img7.jpg',6),(7,'assets/img/300x452/img2.jpg',7),(8,'assets/img/300x452/img5.jpg',8),(9,'assets/img/300x452/img11.jpg',9),(10,'assets/img/300x452/img13.jpg',10),(11,'assets/img/300x452/img9.jpg',11),(12,'assets/img/300x452/img10.jpg',12),(13,'assets/img/300x452/img3.jpg',13),(14,'assets/img/300x452/img14.jpg',16);
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
  `address` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Tran Van A','371 Nguyen Kiem','0977477916','ban12@gmail.com'),(3,'Tran Van C','37 Quang Trung','0838855548','hrhsrhrs@gmail.com'),(4,'Nguyen Van B','24 fuoaauf','0457492147','fdsnbj@gmail.com'),(6,'Phan Van Trung','432 Nguyen Van Cong','0123456789','trung123@gmail.com'),(10,'Tran Van A','371 Nguyen Kiem','0977477916','ban@gmail.com'),(11,'Tran Trong Tin','46 Nguyen Van Cong','4561234812','dasd@gmail.com'),(12,'Phan  ','','',''),(13,'Phan Van Trung','371 Nguyen Kiem','0977477916','ban@gmail.com'),(17,'a b','c','0977477916','ba2n@gmail.com'),(18,'Anh Khoa','371 Nguyen Kiem','0977477916','Khoa123@gmail.com'),(19,'Tran Trong Tin','46 Nguyen Van Cong','0933445672','Tin123@gmail.com'),(20,'Tran Trong Tin','371 Nguyen Kiem','0912345678','Tin123@gmail.com'),(21,'Tran Van A','371 Nguyen Kiem','0977477916','bandgsgsg@gmail.com'),(22,'Tran Van A','371 Nguyen Kiem','+84977477916','ban@gmail.com'),(23,'Tran Thi C','371 Nguyen Trai','+849774779162','ban@gmail.com'),(24,'Tran Van A','371 Nguyen Kiem','0123456789','ban@gmail.com');
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
  `quantity` int DEFAULT NULL,
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
INSERT INTO `detail_inventory_report` VALUES (1,1,50),(2,1,50),(3,3,98),(3,6,50),(4,1,39),(4,12,50),(4,13,50);
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
INSERT INTO `detail_invoice` VALUES (2,2,1,110000),(2,3,1,128000),(2,4,1,22000),(6,3,13,128000),(7,1,5,115000),(8,5,1,175000),(9,4,1,22000),(10,1,1,115000),(11,2,1,110000),(12,11,1,13000),(13,2,1,110000),(14,1,1,115000),(14,3,1,128000),(15,1,1,115000),(16,3,2,128000),(17,2,1,110000),(18,1,5,115000),(24,3,1,128000),(27,3,1,128000),(28,1,1,115000),(28,3,1,128000),(29,1,1,115000),(29,3,1,128000),(30,3,7,128000),(31,3,1,128000),(32,4,5,22000),(33,3,1,128000),(34,5,1,175000),(35,7,1,110000),(36,4,4,22000);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_report`
--

LOCK TABLES `inventory_report` WRITE;
/*!40000 ALTER TABLE `inventory_report` DISABLE KEYS */;
INSERT INTO `inventory_report` VALUES (1,'2021-04-24'),(2,'2021-04-24'),(3,'2021-04-24'),(4,'2021-05-02');
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
  `note` longtext COLLATE utf8mb4_unicode_520_ci,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
INSERT INTO `invoice` VALUES (2,'2021-02-01',260000,6,NULL),(6,'2021-02-25',1664000,10,''),(7,'2021-04-23',575000,10,''),(8,'2021-04-23',175000,10,''),(9,'2021-04-23',22000,10,''),(10,'2021-04-23',115000,10,''),(11,'2021-04-23',110000,10,''),(12,'2021-04-23',13000,10,''),(13,'2021-04-23',110000,10,''),(14,'2021-04-26',243000,10,NULL),(15,'2021-04-26',115000,10,NULL),(16,'2021-04-26',128000,10,'hnsnsglh'),(17,'2021-04-26',110000,10,''),(18,'2021-04-26',115000,10,''),(24,'2021-04-27',128000,17,''),(27,'2021-05-02',128000,10,''),(28,'2021-05-04',243000,18,''),(29,'2021-05-04',243000,10,''),(30,'2021-05-07',896000,10,''),(31,'2021-05-08',128000,19,''),(32,'2021-05-08',22000,20,''),(33,'2021-05-08',128000,21,''),(34,'2021-05-08',175000,22,''),(35,'2021-05-08',110000,23,''),(36,'2021-05-08',22000,24,'');
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Duc Bang','abc@gmail.com','admin123','$2b$15$lms2Ym.cESGtAv8h3cu.vOzLvJfT0LSX/J8wZKCyPyQ3YFuX1idBG',1,'2021-04-10','ADMIN'),(2,'Van Trung','trung123@gmail.com','trung123','$2b$15$Vntfv7CjBCt8kGptf8Btvu5yQUkSkXThaXnnp/bxNhRskTLxRqRJ.',1,'2021-04-10','USER'),(3,'Anh Khoa','Khoa123@gmail.com','khoa123','$2b$15$4WEA89IQw7BltfyXU4V7mOor3sHajNP7lhKt/C8p6N8S6oVylKrey',1,'2021-04-10','USER'),(6,'Tran Trong Tin','Tin123@gmail.com','tin123','$2b$15$BzR6JXh0AabKD0bbU4i/keznWWydUj2RsPyW240DkTcnMIMnfDxsm',1,'2021-05-02','USER'),(7,'Tran Van B','gssigsi@gmail.com','adbc123','$2b$15$V/NlqQd4OnM.Lif.C54NtuFwK.Kfa1rRM0soZUQX1OhDZCBt6sHcu',1,'2021-05-02','USER'),(12,'Tran Van A','ban@gmail.com','user123','$2b$15$NoIXaHv8W0ReZmFYolzX0.ciSquepc64QS0Sj82SniAd/4VOkoXX2',1,'2021-05-10','USER');
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

-- Dump completed on 2021-05-10 21:52:23
