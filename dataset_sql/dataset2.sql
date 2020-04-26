DROP TABLE IF EXISTS dataset2 cascade;

CREATE TABLE dataset2(
		pid INTEGER,
        aid INTEGER,
        vid INTEGER,
        year INTEGER,
        type INTEGER,
        coauthors INTEGER
        );

INSERT INTO dataset2
SELECT P.id, A.id, V.id, V.year, V.type, M.coauthors  
FROM copapers P, coau_papers M, paperauths_small PA, authors_small A, venue_small V 
WHERE A.id = PA.authid AND P.id = PA.paperid AND V.id = P.venue AND P.id = M.id;