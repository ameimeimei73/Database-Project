CREATE TABLE paperauths_temp AS SELECT DISTINCT paperid, authid FROM paperauths, papers, authors WHERE papers.id = paperid AND authors.id = authid;

SELECT COUNT(*) FROM paperauths_temp;

SELECT COUNT(*) FROM paperauths;

DROP TABLE paperauths;

ALTER TABLE paperauths_temp RENAME TO paperauths;

