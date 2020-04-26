drop table IF EXISTS copapers cascade;

create table copapers(
        id integer primary key,
        venue integer,
        foreign key(venue) references Venue(id)
        );

INSERT INTO copapers 
SELECT P.id, P.venue 
FROM papers_small P, coau_papers AS M
WHERE P.id = M.id AND (M.coauthors > 1);