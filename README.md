# MasLeads Challenge - Backend Developer

## The challenge...

### Instructions:

* Perform the test by recording the screen with ide + browser. There is no problem in to search websites/software for methodologies, doubts, errors... The recording is to see the ease you have.
* Upload the test video, documentation and generated code to a drive and send us the drive link.
* Send the link to `\<name\>@masleads.es` indicating in the email your name and surname, like any consideration you want to contemplate.

### Statement:

1. According to the DDL provided:
2. Create a method that prints on the screen all the elements with `status=60`.
3. Expose a POST web service in which an insertion request is received elements `status=xx` and `name=yy` and perform the insert. Returns the codes that you consider necessary.
4. Create a docker container and launch the application.

### Notes:

* It is mandatory to use the entire stack of skills you have: Entities, validators, DAO's, DTO's, Controllers, Threading, SQLAlchemy, Flask, Docker, Docker-compose, Ports, Volumes, From scratch, TDD, DDD, Arq Hexagonal, everything that you consider necessary to give the best of yourself.
* Technical additions that you consider to be of value will be highly valued. utility: Login, TDD, DDD, Arq Hexag, Compose, Swarm, Kubern....
* Additional documentation such as swagger, comments, explanations and arguments.

### DDL:
```sql
CREATE TABLE `ElementsToProcess` (
`id` int NOT NULL AUTO_INCREMENT,
`idBulk` int NOT NULL,
`retries` int DEFAULT NULL,
`status` int NOT NULL,
`name` varchar(100) NOT NULL,
PRIMARY KEY (`id`),
KEY `ElementsToProcess_idBulk_IDX` (`idBulk`,`status`) USING BTREE,
KEY `ElementsToProcess_status_IDX` (`status`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=142812 DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (1, 0, 20, 'Element 1');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (1, 1, 20, 'Element 2');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (2, 2, 20, 'Element 3');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (2, 0, 20, 'Element 4');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (3, 0, 60, 'Element 5');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (3, 1, 60, 'Element 6');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (4, 2, 60, 'Element 7');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (5, 0, 80, 'Element 8');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (5, 1, 80, 'Element 9');
INSERT INTO ElementsToProcess (idBulk, retries, status, name) VALUES (6, 0, 100, 'Element 10');
```

## My solution:

### Requirements:

> 1. Env file:

```bash
# API
API_PORT=6001

# POSTGRES
POSTGRES_HOST=postgres
POSTGRES_DATA_PATH=./postgres/data/
POSTGRES_PORT=5432
POSTGRES_DB=masleads
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# TESTING
DATABASE_URI_TEST="sqlite:////testing_data/db.sqlite3"
```

> 2. Deploy the `docker-compose.yml` file:

```bash
# .masleads root path
> docker-compose up --build
```

> 3. PostgreSQL database creation:

Enter to the `api` container with:

```bash
> docker exec -it api python
```

And execute this script to build the database using the SQLAlchemy ORM.

```python
# >>> Python REPL
from main import app
from api.extensions import db
from api.elements.model import ElementToProcess

with app.app_context():
    db.create_all()

# exit with:
>>>exit()
```

> 4. Execute the insert statements:

##### **`inserts.sql`**
```sql
-- DDL provided with a few modifications for PostgreSQL compatibility
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (1, 0, 20, 'Element 1');
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (1, 1, 20, 'Element 2');
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (2, 2, 20, 'Element 3');
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (2, 0, 20, 'Element 4');
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (3, 0, 60, 'Element 5');
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (3, 1, 60, 'Element 6');
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (4, 2, 60, 'Element 7');
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (5, 0, 80, 'Element 8');
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (5, 1, 80, 'Element 9');
INSERT INTO "ElementsToProcess" ("idBulk", retries, status, name) VALUES (6, 0, 100, 'Element 10');
```

Copy the `ìnserts.sql` file into the postgres container and execute it:

```bash
> docker cp inserts.sql postgres:/inserts.sql
Successfully copied 2.56kB to postgres:/inserts.sql

> docker exec -it postgres psql -U postgres -h postgres -f /inserts.sql masleads
Password for user postgres: # type postgres and hit enter
INSERT 0 1
...
```

> 5. It's ready!

Browse to http://localhost:6001

### Tests and misc

Run the next command:

```bash
> docker exec -it api pytest . -W ignore::DeprecationWarning
```

> Note:

The `-W ignore::DeprecationWarning` part is because the `flask-restx` library is using some elements next to be deprecated. Someone should update that awesome library!

If you want do some pre-commit checks, use the next command:

```bash
> pre-commit run --all-files
```
