-- CREATE table "notes"
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(45),
    subtitle VARCHAR(45),
    body TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP

);

--INSERT 1 record

-- INSERT INTO notes (
--     title,
--     subtitle,
--     body
-- ) VALUES (
--     "Shopping List",
--     "Ralphs",
--     "Pick up milk"
-- );

