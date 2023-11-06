-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT * FROM crime_scene_reports
WHERE street = "Humphrey Street" ;
-- bakery witnesses --
SELECT * FROM interviews WHERE transcript LIKE "%bakery%" ;
--Witness 1 Ruth--
SELECT  * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day= 28 AND hour = 10 AND minute BETWEEN  15 AND 25;
--Check against licence plates

