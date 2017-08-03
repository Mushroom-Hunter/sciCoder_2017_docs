PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE `club` (
	`id`	INTEGER NOT NULL,
	`name`	TEXT NOT NULL,
	PRIMARY KEY(`id`)
);
CREATE TABLE `supervisor` (
	`id`	INTEGER,
	`first_name`	TEXT,
	`last_name`	TEXT,
	`room_number`	INTEGER,
	PRIMARY KEY(`id`)
);
CREATE TABLE `student_to_club` (
	`student_id`	INTEGER,
	`club_id`	INTEGER,
	PRIMARY KEY(`student_id`,`club_id`),
	FOREIGN KEY(`student_id`) REFERENCES student(id),
	FOREIGN KEY(`club_id`) REFERENCES club(id)
);
CREATE TABLE `student` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`first_name`	TEXT,
	`last_name`	TEXT,
	`city_id`	INTEGER,
	`status_id`	INTEGER,
	FOREIGN KEY(`city_id`) REFERENCES city(id),
	FOREIGN KEY(`status_id`) REFERENCES status(id)
);
CREATE TABLE "city" (
	`id`	INTEGER NOT NULL,
	`label`	TEXT UNIQUE,
	PRIMARY KEY(`id`)
);
CREATE TABLE "status" (
	`id`	INTEGER NOT NULL,
	`label`	TEXT UNIQUE,
	PRIMARY KEY(`id`)
);
CREATE TABLE "student_to_supervisor" (
	`student_id`	INTEGER,
	`supervisor_id`	INTEGER,
	PRIMARY KEY(`student_id`,`supervisor_id`),
	FOREIGN KEY(`student_id`) REFERENCES `student`(`id`),
	FOREIGN KEY(`supervisor_id`) REFERENCES `supervisor`(`id`)
);
COMMIT;
