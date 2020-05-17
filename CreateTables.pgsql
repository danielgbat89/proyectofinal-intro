CREATE TABLE aeros (
    id SERIAL PRIMARY KEY,
    id_feilure INTEGER NOT NULL,
    power FLOAT NOT NULL,
    windFarm VARCHAR NOT NULL,
    OEM VARCHAR NOT NULL    
);

CREATE TABLE staff (
    id SERIAL PRIMARY KEY,          
    username VARCHAR NOT NULL,
    hash VARCHAR NOT NULL,
    id_job VARCHAR NOT NULL            
);

CREATE TABLE feilures (
    id SERIAL PRIMARY KEY,        /* symbol and ends with */ 
    category INTEGER NOT NULL,
    subsystem VARCHAR NOT NULL,
    ACK VARCHAR,
    description VARCHAR
);

CREATE TABLE fails (
    id SERIAL PRIMARY KEY,
    id_aero VARCHAR NOT NULL,
    id_operator INTEGER NOT NULL,
    category VARCHAR NOT NULL,
    subystem VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    submitDate TIME
);

CREATE TABLE job (
    id SERIAL PRIMARY KEY,          
    jobType VARCHAR NOT NULL                   
);
