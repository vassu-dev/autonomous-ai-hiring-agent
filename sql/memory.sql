create extension if not exists vector;

create table memory (
  id uuid primary key default uuid_generate_v4(),
  candidate_id uuid,
  content text,
  embedding vector(1536),
  metadata jsonb
);
