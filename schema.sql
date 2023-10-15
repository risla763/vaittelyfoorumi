CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE headlines (
    headline_id SERIAL PRIMARY KEY,
    headline_text TEXT NOT NULL
);


CREATE TABLE messages1 (
    message_id SERIAL PRIMARY KEY,
    message_text TEXT NOT NULL,
    user_id INT NOT NULL,
    headline_id INT,
    answer TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (headline_id) REFERENCES headlines(headline_id)
);

CREATE INDEX idx_timestamp ON messages1 (timestamp);

CREATE TABLE started_debates (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    headline TEXT NOT NULL
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    headline TEXT NOT NULL,
    username TEXT NOT NULL,
    answer TEXT NOT NULL
);

CREATE TABLE percentages (
    id SERIAL PRIMARY KEY,
    headline TEXT NOT NULL,
    agree INT NOT NULL,
    disagree INT NOT NULL
);