drop table IF EXISTS paperauths cascade;
drop table IF EXISTS authors cascade;
drop table IF EXISTS papers cascade;
drop table IF EXISTS venue cascade;

CREATE TABLE authors (
    id integer,
    name character varying(200),
    primary key (id)
);

CREATE TABLE venue (
    id integer,
    name character varying(200) NOT NULL,
    year integer NOT NULL,
    school character varying(200),
    volume character varying(30),
    number character varying(30),
    type integer,
    primary key (id)
);


CREATE TABLE papers (
    id integer,
    name character varying(2048) NOT NULL,
    venue integer,
    pages character varying(50),
    url character varying(512),
    primary key(id),
    foreign key (venue) references venue(id)
);


CREATE TABLE paperauths (
    paperid integer,
    authid integer
);
