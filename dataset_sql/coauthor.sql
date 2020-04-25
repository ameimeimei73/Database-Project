drop table IF EXISTS coau_papers cascade;

CREATE TABLE coau_papers(
        id integer primary key,
        coauthors integer
        );

INSERT INTO coau_papers 
SELECT P.id, M.coauthors 
FROM papers P, (SELECT L.paperid AS id, COUNT(L.paperid) AS coauthors FROM paperauths L GROUP BY L.paperid) AS M
WHERE P.id = M.id;