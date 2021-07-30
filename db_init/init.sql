DROP TABLE IF EXISTS employees CASCADE;
CREATE TABLE employees (
	id bigserial PRIMARY KEY,
	email varchar(30) NOT NULL UNIQUE,
	pass_hash varchar(21) NOT NULL,
	is_manager bool NOT NULL DEFAULT false
);


DROP TABLE IF EXISTS requests;
CREATE TABLE requests (
	id bigserial PRIMARY KEY,
	eid bigint,
	pennies int NOT NULL,
	reason varchar(50) DEFAULT 'pay me back',
	is_pending bool NOT NULL DEFAULT true,
	response varchar(50),
	is_approved bool NOT NULL DEFAULT false,
    CONSTRAINT requests_check CHECK (is_pending != true OR is_approved != true),
	FOREIGN KEY (eid) REFERENCES employees(id) ON DELETE SET NULL ON UPDATE CASCADE
);


INSERT INTO employees VALUES
(DEFAULT, 'Tim@lol.com', 'TtE#', true),
(DEFAULT, 'Slim@lol.com','phat#', DEFAULT),
(DEFAULT, 'JimBob@lol.com','imwithbob#', DEFAULT),
(DEFAULT, 'BobJim@lol.com','imwithjim#', DEFAULT),
(DEFAULT, 'deleteableguy@lol.com','whocares#', DEFAULT),
(DEFAULT, 'JC@lol.com','selfinsert#', true);

INSERT INTO requests VALUES
(DEFAULT, 1, 420, 'dank memes', DEFAULT, NULL, DEFAULT),
(DEFAULT, 6, 1337, '$13.37 for the memes', DEFAULT, NULL, DEFAULT),
(DEFAULT, 6, 1337, '$13.37 for the memes', DEFAULT, NULL, DEFAULT),
(DEFAULT, 2, 10000, 'hundred dollar meal with client', false, '10k pennies 4 u', true),
(DEFAULT, 3, 100, DEFAULT, false, 'no dollar for you', DEFAULT),
(DEFAULT, 5, 9001, '$90.01 for the memes', false, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT),
(DEFAULT, 4, 1000, DEFAULT, DEFAULT, NULL, DEFAULT);

DELETE FROM employees WHERE id = 5; -- no user #5
