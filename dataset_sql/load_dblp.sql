\COPY authors (id, name) FROM 'authors.csv' WITH (FORMAT CSV); 

\COPY venue (id, name, year, school, volume, number, type) FROM 'venue.csv' WITH (FORMAT CSV, HEADER);  

\COPY papers (id, name, venue, pages, url) FROM 'papers.csv' WITH (FORMAT CSV, HEADER);

\COPY paperauths (paperid, authid) FROM 'paperauths.csv' WITH (FORMAT CSV, HEADER);
