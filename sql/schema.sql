create extension if not exists "uuid-ossp";

create table candidates (
  id uuid primary key default uuid_generate_v4(),
  name text,
  skills text[],
  experience int,
  resume text,
  score float
);

create table interviews (
  id uuid primary key default uuid_generate_v4(),
  candidate_id uuid,
  question text,
  answer text,
  evaluation text,
  ai_flag text
);

create table weights (
  id int primary key default 1,
  skill float,
  experience float,
  resume float
);

insert into weights values (1, 0.4, 0.3, 0.3);
