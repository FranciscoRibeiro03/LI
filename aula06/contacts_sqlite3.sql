CREATE TABLE contacts(
    firstname TEXT,
    middlename TEXT,
    lastname TEXT,
    email TEXT,
    phone TEXT
);

INSERT INTO contacts VALUES ( "João", "Manuel", "Fonseca", "jmf@gmail.com", "912345654" );
INSERT INTO contacts VALUES ( "Pedro", "Albuquerque", "Silva", "pedro23@gmail.com", "932454349" );
INSERT INTO contacts VALUES ( "Maria", "Carreira", "Dinis", "mariadi@ua.pt", "234958673" );
INSERT INTO contacts VALUES ( "Catarina", "Alexandra", "Rodrigo", "calexro@sapo.pt", "963343386" );

SELECT * FROM contacts;
SELECT email,phone FROM contacts WHERE firstname="Pedro";
SELECT * FROM contacts ORDER BY firstname ASC;
SELECT * FROM contacts ORDER BY phone DESC;

UPDATE contacts SET phone = 912345653 WHERE email="jmf@gmail.com";
UPDATE contacts SET lastname = "Sousa" WHERE phone="963343386";

DELETE FROM contacts WHERE phone = 912345653;




CREATE TABLE companies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    vatnumber INTEGER
);

CREATE TABLE contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT,
    middlename TEXT,
    lastname TEXT,
    email TEXT,
    phone TEXT,
    company_id INTEGER
);

INSERT INTO companies(name, address, vatnumber) VALUES ( "MaxiPlano", "Aveiro", 123123123123 );
INSERT INTO companies(name, address, vatnumber) VALUES ( "Luis Manuel & Filhos", "Águeda", 54534343435 );
INSERT INTO companies(name, address, vatnumber) VALUES ( "ProDesign", "Porto", 54534343435 );

INSERT INTO contacts
    (firstname, middlename, lastname, email, phone, company_id) VALUES
    ( "João", "Manuel", "Fonseca", "jmf@gmail.com", "912345654", 3 );
INSERT INTO contacts
    (firstname, middlename, lastname, email, phone, company_id) VALUES 
    ( "Pedro", "Albuquerque", "Silva", "pedro23@gmail.com", "932454349", 2 );
INSERT INTO contacts
    (firstname, middlename, lastname, email, phone, company_id) VALUES 
    ( "Maria", "Carreira", "Dinis", "mariadi@ua.pt", "234958673", 1 );
INSERT INTO contacts
    (firstname, middlename, lastname, email, phone, company_id) VALUES 
    ( "Catarina", "Alexandra", "Rodrigo", "calexro@sapo.pt", "963343386", 1 );
    

SELECT contacts.* FROM contacts,companies WHERE contacts.company_id = companies.id AND companies.address = "Aveiro";