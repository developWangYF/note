DROP TABLE IF EXISTS `gonggao`; -- #如果数据库中存在xxx_book表，就把它从数据库中drop掉
CREATE TABLE `gonggao`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `face_user_id` int(10) UNSIGNED DEFAULT NULL COMMENT 'face_user_list表中的id',
  `task_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '任务id',
  `lib_id` int(10) NOT NULL COMMENT '人脸库id',
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '姓名',
  `id_card` varchar(19) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '身份证号',
  `image_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '人像',
  `status` tinyint(1) UNSIGNED DEFAULT NULL COMMENT '0成功1失败 2待审批 -1审批未通过',
  `fail_reason` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `time_created` datetime(0) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `id_type` int(1) DEFAULT 0 COMMENT '0 为 身份证，1 为 护照',
  `appr_user` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '审批人员信息',
  `appr_text` text CHARACTER SET utf8 COLLATE utf8_general_ci COMMENT '审批备注',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `task_id`(`task_id`) USING BTREE,
  INDEX `li`(`lib_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 63424 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '人脸库批量上传临时表' ROW_FORMAT = Dynamic;
-- ROW_FORMAT行记录格式，行格式影响性能

CREATE TABLE `gonggao`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `task_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '任务id',
  `lib_id` int(10) NOT NULL COMMENT '人脸库id',
  `name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '姓名',
  `id_card` varchar(19) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '身份证号',
  `image_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '人像',
  `status` tinyint(1) UNSIGNED DEFAULT NULL COMMENT '0成功1失败 2待审批 -1审批未通过',
  `fail_reason` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `time_created` datetime(0) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `id_type` int(1) DEFAULT 0 COMMENT '0 为 身份证，1 为 护照',
  `appr_user` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '发布人',
  `公告内容` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '审批备注',
  PRIMARY KEY (`id`),
) ENGINE = InnoDB AUTO_INCREMENT = 2000 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '公告表';