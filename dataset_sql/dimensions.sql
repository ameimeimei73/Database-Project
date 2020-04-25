
\copy (SELECT DISTINCT A.id FROM authors_small A) To 'authorid.csv' With CSV;

\copy (SELECT DISTINCT V.id FROM venue_small V) To 'venueid.csv' With CSV;

\copy (SELECT DISTINCT V.year FROM venue_small V) To 'venueyear.csv' With CSV;

\copy (SELECT DISTINCT V.type FROM venue_small V) To 'venuetype.csv' With CSV;

\copy (SELECT DISTINCT M.coauthors FROM coau_papers M) To 'coauthors.csv' With CSV;

