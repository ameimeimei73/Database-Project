drop table IF EXISTS papers_small cascade;
drop table IF EXISTS venue_small cascade;
drop table IF EXISTS authors_small cascade;
drop table IF EXISTS paperauths_small cascade;
drop view IF EXISTS paperids cascade;

CREATE VIEW paperids AS
    SELECT DISTINCT paperid
    FROM paperauths
    LIMIT 31416;

CREATE TABLE papers_small AS
    SELECT *
    FROM papers p, paperids pid
    WHERE p.id = pid.paperid;

ALTER TABLE papers_small
DROP COLUMN paperid;

DROP VIEW paperids;

CREATE TABLE paperauths_small AS
    SELECT *
    FROM paperauths pa, papers_small p
    WHERE pa.paperid = p.id;

ALTER TABLE paperauths_small
DROP COLUMN id;

CREATE TABLE authors_small AS
    SELECT a.id, a.name
    FROM paperauths_small pa, authors a
    WHERE pa.authid = a.id;

CREATE TABLE venue_small AS
    SELECT DISTINCT v.id, v.name, v.year, v.type
    FROM venue v, papers_small p
    WHERE v.id = p.venue;
