create table post(id integer primary key, title text);

insert into
    post (title)
values
    ('first post'),
    ('second post');

CREATE TABLE comment(
    id integer primary key,
    body text,
    post_id integer,
    FOREIGN KEY (post_id) REFERENCES post(id)
);

insert into
    comment (body, post_id)
values
    ('first comment of first post', 1);

insert into
    comment (body, post_id)
values
    ('second comment of first post', 1);

insert into
    comment (body, post_id)
values
    ('first comment of second post', 2);

insert into
    comment (body, post_id)
values
    ('second comment of second post', 2);

select
    *
from
    comment
    join post on comment.post_id = post.id;

-- +----+-------------------------------+---------+----+-------------+
-- | id |             body              | post_id | id |    title    |
-- +----+-------------------------------+---------+----+-------------+
-- | 1  | first comment of first post   | 1       | 1  | first post  |
-- | 2  | second comment of first post  | 1       | 1  | first post  |
-- | 3  | first comment of second post  | 2       | 2  | second post |
-- | 4  | second comment of second post | 2       | 2  | second post |
-- +----+-------------------------------+---------+----+-------------+
select
    comment.id as comment_id,
    post.id as post_id,
    comment.body as comment_body,
    post.title as post_title
from
    comment
    join post on comment.post_id = post.id;

-- +------------+---------+-------------------------------+-------------+
-- | comment_id | post_id |         comment_body          | post_title  |
-- +------------+---------+-------------------------------+-------------+
-- | 1          | 1       | first comment of first post   | first post  |
-- | 2          | 1       | second comment of first post  | first post  |
-- | 3          | 2       | first comment of second post  | second post |
-- | 4          | 2       | second comment of second post | second post |
-- +------------+---------+-------------------------------+-------------+