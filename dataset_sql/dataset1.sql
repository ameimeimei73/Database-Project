DROP TABLE IF EXISTS dataset1 cascade;

CREATE TABLE dataset1(
		pid INTEGER,
        aid INTEGER,
        vid INTEGER,
        year INTEGER,
        type INTEGER,
        coauthors INTEGER
        );

INSERT INTO dataset1
SELECT P.id, A.id, V.id, V.year, V.type, M.coauthors  
FROM papers_small P, coau_papers M, paperauths_small PA, authors_small A, venue_small V 
WHERE A.id = PA.authid AND P.id = PA.paperid AND V.id = P.venue AND P.id = M.id;