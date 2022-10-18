DROP TABLE IF EXISTS "Visitors"; -- drop current table if exists (aka overwrite)
CREATE TABLE "Visitors" (
    "id" INTEGER PRIMARY KEY,
    "name" VARCHAR (64) NOT NULL,
    "password" VARCHAR(64) NOT NULL,
    "address" VARCHAR (256) NOT NULL, -- large value incase very long adress
    "city" VARCHAR (64) NOT NULL,
    "phone_number" INTEGER,
    "email" VARCHAR (64) NOT NULL,
    "has_covid" INTEGER -- value that can be altered by hospital (1 = covid, 0 = no covid)
);

DROP TABLE IF EXISTS "Places";
CREATE TABLE "Places" (
    "id" INTEGER PRIMARY KEY,
    "name" VARCHAR(128) NOT NULL,
    "password" VARCHAR (256) NOT NULL,
    "address" VARCHAR(128) NOT NULL,
    "phone_number" INTEGER,
    "email" VARCHAR (64),
    "occupants" VARCHAR(2048) NOT NULL -- string to store all visitors in location
);

DROP TABLE IF EXISTS "Agency";
CREATE TABLE "Agency" (
    "id" INTEGER PRIMARY KEY,
    "name" VARCHAR (256) NOT NULL,
    "password" VARCHAR (256) NOT NULL
);

INSERT INTO "Agency" VALUES (1, 'agency', 'pbkdf2:sha256:260000$ConIpPmHGroTUndO$696c40b95e944f2fd3638a18419f5317ea2d95599f0dbf2e4e40883746031986');

DROP TABLE IF EXISTS 'Hospital';
CREATE TABLE "Hospital" (
    "id" INTEGER PRIMARY KEY,
    "name" VARCHAR (256) NOT NULL,
    "password" VARCHAR (256) NOT NULL
);

DROP TABLE IF EXISTS 'VisitorToPlaces';
CREATE TABLE "VisitorToPlaces" (
    "id" INTEGER PRIMARY KEY,
    "device_ID" VARCHAR (256) NOT NULL,
    "entry_datetime" VARCHAR (256),
    "exit_datetime" VARCHAR (256)
);

-- To get datetime, use "SELECT datetime('now','localtime');"
-- to insert datetime, use "INSERT INTO VisitorToPlaces (entry_datetime, exit_datetime)
--     VALUES(datetime('now', 'localtime'),datetime('now', 'localtime'));"
-- refer to https://www.sqlitetutorial.net/sqlite-date/


