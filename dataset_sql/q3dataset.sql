drop table IF EXISTS graphpapers cascade;
drop table IF EXISTS graphauthors cascade;

create table graphpapers(
        id integer primary key,
        venue integer,
        foreign key(venue) references Venue(id)
        );

create table graphauthors(
        id integer primary key
        );

INSERT INTO graphpapers 
SELECT P.id, P.venue 
FROM papers_small P
WHERE to_tsvector('english', P.name) @@ to_tsquery('english', 'graph');

INSERT INTO graphauthors
SELECT DISTINCT A.id
FROM authors_small A, paperauths_small P, graphpapers G
WHERE A.id = P.authid AND P.paperid = G.id;