CREATE INDEX authors_name ON authors (name);

ALTER TABLE paperauths ADD CONSTRAINT fk_paperauths_paperid FOREIGN KEY (paperid) REFERENCES papers(id);

ALTER TABLE paperauths ADD CONSTRAINT fk_paperauths_authid FOREIGN KEY (authid) REFERENCES authors(id);

CREATE UNIQUE INDEX ON paperauths (paperid, authid);
