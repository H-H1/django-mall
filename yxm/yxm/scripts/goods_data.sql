-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: yxmall_db
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.16.04.1

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
-- Table structure for table `tb_goods`
--

DROP TABLE IF EXISTS `tb_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(50) NOT NULL,
  `sales` int(11) NOT NULL,
  `comments` int(11) NOT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `category1_id` int(11) NOT NULL,
  `category2_id` int(11) NOT NULL,
  `category3_id` int(11) NOT NULL,
  `desc_detail` longtext NOT NULL,
  `desc_pack` longtext NOT NULL,
  `desc_service` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_goods_brand_id_5c5be571_fk_tb_goods_brand_id` (`brand_id`),
  KEY `tb_goods_category1_id_49c4fab9_fk_tb_goods_category_id` (`category1_id`),
  KEY `tb_goods_category2_id_ea351ced_fk_tb_goods_category_id` (`category2_id`),
  KEY `tb_goods_category3_id_d3ea8415_fk_tb_goods_category_id` (`category3_id`),
  CONSTRAINT `tb_goods_brand_id_5c5be571_fk_tb_goods_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `tb_goods_brand` (`id`),
  CONSTRAINT `tb_goods_category1_id_49c4fab9_fk_tb_goods_category_id` FOREIGN KEY (`category1_id`) REFERENCES `tb_goods_category` (`id`),
  CONSTRAINT `tb_goods_category2_id_ea351ced_fk_tb_goods_category_id` FOREIGN KEY (`category2_id`) REFERENCES `tb_goods_category` (`id`),
  CONSTRAINT `tb_goods_category3_id_d3ea8415_fk_tb_goods_category_id` FOREIGN KEY (`category3_id`) REFERENCES `tb_goods_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_goods`
--

LOCK TABLES `tb_goods` WRITE;
/*!40000 ALTER TABLE `tb_goods` DISABLE KEYS */;
INSERT INTO `tb_goods` VALUES (1,'2020-09-07 20:47:40.451402','2020-09-07 20:56:01.708679','华为 HUAWEI P40 超感光徕卡三摄麒麟980AI智能芯片全面屏屏内指纹版手机',0,0,1,1,5,6,'<p><img alt=\"\" src=\"http://pic.myuxi.com/media/2020/09/07/p40001.jpg\" /></p>\r\n\r\n<p><img alt=\"\" src=\"http://pic.myuxi.com/media/2020/09/07/p40002.jpg\" style=\"height:358px; width:750px\" /></p>\r\n\r\n<p><img alt=\"\" src=\"http://pic.myuxi.com/media/2020/09/07/p40003.jpg\" style=\"height:995px; width:750px\" /></p>\r\n\r\n<p><img alt=\"\" src=\"http://pic.myuxi.com/media/2020/09/07/p40004.jpg\" style=\"height:646px; width:750px\" /></p>\r\n\r\n<p><img alt=\"\" src=\"http://pic.myuxi.com/media/2020/09/07/p40005.jpg\" style=\"height:646px; width:750px\" /></p>\r\n\r\n<p><img alt=\"\" src=\"http://pic.myuxi.com/media/2020/09/07/p40006.jpg\" /></p>\r\n\r\n<p>&nbsp;</p>','<p>手机X1，电池（内置）X1，充电器X1，&nbsp;TYPE-C数据线X1</p>','<p><strong>厂家服务</strong></p>\r\n\r\n<p>本产品全国联保，享受三包服务，质保期为：全国联保一年<br />\r\n如因质量问题或故障，凭厂商维修中心或特约维修点的质量检测证明，享受7日内退货，15日内换货，15日以上在质保期内享受免费保修等三包服务！<br />\r\n(注:如厂家在商品介绍中有售后保障的说明,则此商品按照厂家说明执行售后保障服务。) 您可以查询本品牌在各地售后服务中心的联系方式<br />\r\n<br />\r\n品牌官方网站：<a href=\"http://www.huawei.com/cn/\" target=\"_blank\">http://www.huawei.com/cn/</a><br />\r\n售后服务电话：950800</p>\r\n\r\n<p>&nbsp;<strong>京东承诺</strong></p>\r\n\r\n<p>京东平台卖家销售并发货的商品，由平台卖家提供发票和相应的售后服务。请您放心购买！<br />\r\n注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！</p>\r\n\r\n<p><strong>正品行货</strong></p>\r\n\r\n<p>京东商城向您保证所售商品均为正品行货，京东自营商品开具机打发票或电子发票。</p>\r\n\r\n<p><strong>全国联保</strong></p>\r\n\r\n<p>凭质保证书及京东商城发票，可享受全国联保服务（奢侈品、钟表除外；奢侈品、钟表由京东联系保修，享受法定三包售后服务），与您亲临商场选购的商品享受相同的质量保证。京东商城还为您提供具有竞争力的商品价格和运费政策，请您放心购买！<br />\r\n<br />\r\n注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！</p>\r\n\r\n<p><strong>无忧退货</strong></p>\r\n\r\n<p>客户购买京东自营商品7日内（含7日，自客户收到商品之日起计算），在保证商品完好的前提下，可无理由退货。（部分商品除外，详情请见各商品细则）</p>'),(2,'2020-09-07 21:01:48.774916','2020-09-17 16:26:43.950312','Apple iPhone 11 (A2223)  移动联通电信4G手机 双卡双待',0,0,2,1,5,7,'<p><img alt=\"\" src=\"http://pic.myuxi.com/media/2020/09/07/a01.png\" /></p>','<h3>装有 iOS 13 的 iPhone,采用闪电接头的 EarPods,闪电转 USB 连接线,USB 电源适配器,资料</h3>','<p><strong>厂家服务</strong></p>\r\n\r\n<p>本产品全国联保，享受三包服务，质保期为：一年质保<br />\r\n如因质量问题或故障，凭厂商维修中心或特约维修点的质量检测证明，享受7日内退货，15日内换货，15日以上在质保期内享受免费保修等三包服务！<br />\r\n(注:如厂家在商品介绍中有售后保障的说明,则此商品按照厂家说明执行售后保障服务。)</p>\r\n\r\n<p>&nbsp;<strong>京东承诺</strong></p>\r\n\r\n<p>京东平台卖家销售并发货的商品，由平台卖家提供发票和相应的售后服务。请您放心购买！<br />\r\n注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！</p>\r\n\r\n<p><strong>正品行货</strong></p>\r\n\r\n<p>京东商城向您保证所售商品均为正品行货，京东自营商品开具机打发票或电子发票。</p>\r\n\r\n<p><strong>全国联保</strong></p>\r\n\r\n<p>凭质保证书及京东商城发票，可享受全国联保服务（奢侈品、钟表除外；奢侈品、钟表由京东联系保修，享受法定三包售后服务），与您亲临商场选购的商品享受相同的质量保证。京东商城还为您提供具有竞争力的商品价格和运费政策，请您放心购买！<br />\r\n<br />\r\n注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！</p>\r\n\r\n<p><strong>无忧退货</strong></p>\r\n\r\n<p>客户购买京东自营商品7日内（含7日，自客户收到商品之日起计算），在保证商品完好的前提下，可无理由退货。（部分商品除外，详情请见各商品细则）</p>');
/*!40000 ALTER TABLE `tb_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_goods_brand`
--

DROP TABLE IF EXISTS `tb_goods_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_goods_brand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `first_letter` varchar(1) NOT NULL,
  `brand_sort` smallint(6) NOT NULL,
  `brand_recommend` tinyint(1) NOT NULL,
  `brand_apply` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_goods_brand`
--

LOCK TABLES `tb_goods_brand` WRITE;
/*!40000 ALTER TABLE `tb_goods_brand` DISABLE KEYS */;
INSERT INTO `tb_goods_brand` VALUES (1,'2020-09-15 20:49:58.756029','2020-09-15 20:49:58.756132','华为','huawei.jpg','H',0,1,1),(2,'2020-09-15 20:52:23.987918','2020-09-15 20:52:23.987969','苹果','Apple.jpg','A',0,1,1);
/*!40000 ALTER TABLE `tb_goods_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_goods_category`
--

DROP TABLE IF EXISTS `tb_goods_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_goods_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(10) NOT NULL,
  `clogo` varchar(100) DEFAULT NULL,
  `csort` smallint(6) NOT NULL,
  `c_recommend` tinyint(1) NOT NULL,
  `c_apply` tinyint(1) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_goods_category_parent_id_5abc16fa_fk_tb_goods_category_id` (`parent_id`),
  CONSTRAINT `tb_goods_category_parent_id_5abc16fa_fk_tb_goods_category_id` FOREIGN KEY (`parent_id`) REFERENCES `tb_goods_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_goods_category`
--

LOCK TABLES `tb_goods_category` WRITE;
/*!40000 ALTER TABLE `tb_goods_category` DISABLE KEYS */;
INSERT INTO `tb_goods_category` VALUES (1,'2020-09-15 21:50:36.720983','2020-09-15 21:50:36.721983','数码电器','',0,0,1,NULL),(2,'2020-09-15 21:51:19.498079','2020-09-15 21:51:19.498145','水果特产','',0,0,1,NULL),(3,'2020-09-15 21:51:40.618712','2020-09-15 21:51:40.618775','日常用品','',0,0,1,NULL),(4,'2020-09-15 21:53:21.595529','2020-09-17 15:14:28.497022','电脑配件','csyp.jpg',0,0,1,1),(5,'2020-09-15 21:53:52.968743','2020-09-17 15:14:03.468014','手机','no_logo.jpg',0,0,1,1),(6,'2020-09-15 21:54:33.033830','2020-09-15 21:54:33.033935','华为','hwlogo.jpg',0,0,1,5),(7,'2020-09-15 21:55:01.806238','2020-09-15 21:55:01.806294','iphone','iphone.jpg',0,0,1,5);
/*!40000 ALTER TABLE `tb_goods_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_goods_specification`
--

DROP TABLE IF EXISTS `tb_goods_specification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_goods_specification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `goods_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_goods_specification_goods_id_41f4eda6_fk_tb_goods_id` (`goods_id`),
  CONSTRAINT `tb_goods_specification_goods_id_41f4eda6_fk_tb_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `tb_goods` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_goods_specification`
--

LOCK TABLES `tb_goods_specification` WRITE;
/*!40000 ALTER TABLE `tb_goods_specification` DISABLE KEYS */;
INSERT INTO `tb_goods_specification` VALUES (1,'2020-09-07 21:08:23.017234','2020-09-07 21:34:46.098071','颜色',1),(2,'2020-09-07 21:09:47.015402','2020-09-07 21:34:55.928692','版本',1),(3,'2020-09-17 15:54:36.438113','2020-09-17 15:54:36.438113','颜色',2),(4,'2020-09-17 15:54:49.244881','2020-09-17 15:54:49.244881','版本',2);
/*!40000 ALTER TABLE `tb_goods_specification` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `tb_sku`
--

DROP TABLE IF EXISTS `tb_sku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_sku` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(50) NOT NULL,
  `caption` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `cost_price` decimal(10,2) NOT NULL,
  `market_price` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `sales` int(11) NOT NULL,
  `comments` int(11) NOT NULL,
  `is_launched` tinyint(1) NOT NULL,
  `default_image_url` varchar(200) DEFAULT NULL,
  `category_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_sku_category_id_23dd76b7_fk_tb_goods_category_id` (`category_id`),
  KEY `tb_sku_goods_id_fa5267c2_fk_tb_goods_id` (`goods_id`),
  CONSTRAINT `tb_sku_category_id_23dd76b7_fk_tb_goods_category_id` FOREIGN KEY (`category_id`) REFERENCES `tb_goods_category` (`id`),
  CONSTRAINT `tb_sku_goods_id_fa5267c2_fk_tb_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `tb_goods` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_sku`
--

LOCK TABLES `tb_sku` WRITE;
/*!40000 ALTER TABLE `tb_sku` DISABLE KEYS */;
INSERT INTO `tb_sku` VALUES (1,'2020-09-07 21:15:05.735555','2020-09-07 21:18:26.300045','华为 HUAWEI P40 麒麟990 5G SoC芯片 徕卡三摄 全网通 6GB+128GB','6+128',4088.00,3888.00,4188.00,100,0,0,1,'http://pic.myuxi.com/media/857b2bdf4882dd6f.jpg',6,1),(2,'2020-09-07 21:20:23.340967','2020-09-07 21:20:23.340967','华为 HUAWEI P40 麒麟990 5G SoC芯片 徕卡三摄 全网通 8GB+128GB','8+128',4388.00,4088.00,4488.00,100,0,0,1,'http://pic.myuxi.com/media/857b2bdf4882dd6f.jpg',6,1),(3,'2020-09-07 21:21:59.674263','2020-09-07 21:21:59.675265','华为 HUAWEI P40 麒麟990 5G SoC芯片 徕卡三摄 全网通 8GB+256GB','8+256',4788.00,4288.00,4988.00,100,0,0,1,'http://pic.myuxi.com/media/857b2bdf4882dd6f.jpg',6,1),(4,'2020-09-17 16:02:07.129577','2020-09-17 16:38:27.643257','Apple iPhone 11 (A2223) 移动联通电信4G手机 64GB','嗨购秒杀节，iPhone11领券立减900元！',5499.00,5099.00,5499.00,1000,0,0,1,'http://pic.myuxi.com/media/a1.jpg',7,2),(5,'2020-09-17 16:02:59.545018','2020-09-17 16:38:35.549826','Apple iPhone 11 (A2223) 移动联通电信4G手机 128GB','嗨购秒杀节，iPhone11领券立减900元！',5899.00,5399.00,5899.00,1000,0,0,1,'http://pic.myuxi.com/media/a1.jpg',7,2),(6,'2020-09-17 16:05:57.809450','2020-09-17 16:38:44.534842','Apple iPhone 11 (A2223) 移动联通电信4G手机 256GB','嗨购秒杀节，iPhone11领券立减900元！',6699.00,6199.00,6699.00,1000,0,0,1,'http://pic.myuxi.com/media/a1.jpg',7,2);
/*!40000 ALTER TABLE `tb_sku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_sku_image`
--

DROP TABLE IF EXISTS `tb_sku_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_sku_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `image` varchar(100) NOT NULL,
  `sku_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_sku_image_sku_id_8c6d7195_fk_tb_sku_id` (`sku_id`),
  CONSTRAINT `tb_sku_image_sku_id_8c6d7195_fk_tb_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `tb_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_sku_image`
--

LOCK TABLES `tb_sku_image` WRITE;
/*!40000 ALTER TABLE `tb_sku_image` DISABLE KEYS */;
INSERT INTO `tb_sku_image` VALUES (1,'2020-09-07 21:18:04.467183','2020-09-07 21:18:04.467183','857b2bdf4882dd6f.jpg',1),(2,'2020-09-07 21:23:21.476283','2020-09-07 21:23:21.476283','d1f2bf423c435760.jpg',1),(3,'2020-09-07 21:23:48.558190','2020-09-07 21:23:48.558190','4e9924f5f9a516b4.jpg',1),(4,'2020-09-17 16:37:38.318745','2020-09-17 16:37:38.318745','a1.jpg',4),(5,'2020-09-17 16:37:50.545231','2020-09-17 16:37:50.545231','a2.jpg',4),(6,'2020-09-17 16:38:02.469071','2020-09-17 16:38:02.469071','a3.jpg',4),(7,'2020-09-17 16:38:10.080155','2020-09-17 16:38:10.080155','a4.jpg',4);
/*!40000 ALTER TABLE `tb_sku_image` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `tb_specification_option`
--

DROP TABLE IF EXISTS `tb_specification_option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_specification_option` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `value` varchar(20) NOT NULL,
  `spec_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_specification_opt_spec_id_3f11adee_fk_tb_goods_` (`spec_id`),
  CONSTRAINT `tb_specification_opt_spec_id_3f11adee_fk_tb_goods_` FOREIGN KEY (`spec_id`) REFERENCES `tb_goods_specification` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_specification_option`
--

LOCK TABLES `tb_specification_option` WRITE;
/*!40000 ALTER TABLE `tb_specification_option` DISABLE KEYS */;
INSERT INTO `tb_specification_option` VALUES (1,'2020-09-07 21:09:00.945019','2020-09-07 21:09:00.945019','亮黑色',1),(2,'2020-09-07 21:36:33.374694','2020-09-07 21:36:33.374694','深海蓝',1),(3,'2020-09-07 21:36:44.663791','2020-09-07 21:36:44.663791','冰霜银',1),(4,'2020-09-07 21:36:53.682146','2020-09-07 21:36:53.682146','零度白',1),(5,'2020-09-07 21:37:04.073751','2020-09-07 21:37:04.073751','晨曦金',1),(6,'2020-09-07 21:38:12.677469','2020-09-07 21:38:12.677469','6GB+128GB',2),(7,'2020-09-07 21:38:22.418526','2020-09-07 21:38:22.418526','8GB+128GB',2),(8,'2020-09-07 21:38:35.014628','2020-09-07 21:38:35.014628','8GB+256GB',2),(9,'2020-09-17 15:55:20.227194','2020-09-17 15:56:56.619775','黑色',3),(10,'2020-09-17 15:55:32.627404','2020-09-17 15:55:32.627404','白色',3),(11,'2020-09-17 15:55:43.879182','2020-09-17 15:55:43.879182','红色',3),(12,'2020-09-17 15:55:57.832955','2020-09-17 15:55:57.832955','紫色',3),(13,'2020-09-17 15:56:20.825127','2020-09-17 15:56:20.825127','64GB',4),(14,'2020-09-17 15:56:30.804859','2020-09-17 15:56:30.804859','128GB',4),(15,'2020-09-17 15:56:42.092086','2020-09-17 15:56:42.092086','256GB',4);
/*!40000 ALTER TABLE `tb_specification_option` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `tb_sku_specification`
--

DROP TABLE IF EXISTS `tb_sku_specification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_sku_specification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `option_id` int(11) NOT NULL,
  `sku_id` int(11) NOT NULL,
  `spec_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_sku_specification_option_id_80a17a3d_fk_tb_specif` (`option_id`),
  KEY `tb_sku_specification_sku_id_10aee5ae_fk_tb_sku_id` (`sku_id`),
  KEY `tb_sku_specification_spec_id_5aa6db0c_fk_tb_goods_` (`spec_id`),
  CONSTRAINT `tb_sku_specification_option_id_80a17a3d_fk_tb_specif` FOREIGN KEY (`option_id`) REFERENCES `tb_specification_option` (`id`),
  CONSTRAINT `tb_sku_specification_sku_id_10aee5ae_fk_tb_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `tb_sku` (`id`),
  CONSTRAINT `tb_sku_specification_spec_id_5aa6db0c_fk_tb_goods_` FOREIGN KEY (`spec_id`) REFERENCES `tb_goods_specification` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_sku_specification`
--

LOCK TABLES `tb_sku_specification` WRITE;
/*!40000 ALTER TABLE `tb_sku_specification` DISABLE KEYS */;
INSERT INTO `tb_sku_specification` VALUES (1,'2020-09-07 21:39:15.804571','2020-09-07 21:39:15.804571',1,1,1),(2,'2020-09-07 21:39:44.681586','2020-09-07 21:39:44.681586',2,1,1),(3,'2020-09-07 21:39:54.689674','2020-09-07 21:39:54.689674',3,1,1),(4,'2020-09-07 21:40:03.742333','2020-09-07 21:40:03.742333',4,1,1),(5,'2020-09-07 21:40:12.954816','2020-09-07 21:40:12.954816',5,1,1),(6,'2020-09-17 16:07:02.558957','2020-09-17 16:07:02.558957',6,1,2),(7,'2020-09-17 16:07:24.307426','2020-09-17 16:07:24.307426',7,2,2),(8,'2020-09-17 16:07:38.050153','2020-09-17 16:07:38.050153',8,3,2),(9,'2020-09-17 16:08:11.142825','2020-09-17 16:08:11.142825',9,4,3),(10,'2020-09-17 16:16:26.031460','2020-09-17 16:16:55.115436',10,4,3),(11,'2020-09-17 16:22:59.143674','2020-09-17 16:22:59.143674',11,4,1),(12,'2020-09-17 16:25:10.701668','2020-09-17 16:25:10.701668',12,4,3),(13,'2020-09-17 16:27:20.651757','2020-09-17 16:27:20.651757',13,4,4),(14,'2020-09-17 16:27:35.663030','2020-09-17 16:27:35.663030',14,4,4),(15,'2020-09-17 16:27:47.665136','2020-09-17 16:27:47.665136',15,4,4);
/*!40000 ALTER TABLE `tb_sku_specification` ENABLE KEYS */;
UNLOCK TABLES;

