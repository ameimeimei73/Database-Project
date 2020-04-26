DROP TABLE IF EXISTS dataset3 cascade;

CREATE TABLE dataset3(
		pid INTEGER,
        aid INTEGER,
        vid INTEGER,
        year INTEGER,
        type INTEGER,
        coauthors INTEGER
        );

INSERT INTO dataset3
SELECT P.id, A.id, V.id, V.year, V.type, M.coauthors  
FROM graphpapers P, coau_papers M, paperauths_small PA, graphauthors A, venue_small V 
WHERE A.id = PA.authid AND P.id = PA.paperid AND V.id = P.venue AND P.id = M.id;