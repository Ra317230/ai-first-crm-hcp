CREATE TABLE hcp (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    hospital VARCHAR(100),
    specialization VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE interaction (
    id SERIAL PRIMARY KEY,
    hcp_id INT REFERENCES hcp(id),
    meeting_date DATE,
    meeting_type VARCHAR(100),
    products TEXT,
    summary TEXT,
    follow_up DATE,
    notes TEXT
);