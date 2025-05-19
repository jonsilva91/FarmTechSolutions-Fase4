-- Gerado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   em:        2025-04-22 05:18:18 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g





-- Criação da tabela Cultura
CREATE TABLE Cultura (
    cd_cultura INTEGER NOT NULL,
    nm_cultura VARCHAR2(50) NOT NULL,
    tp_cultura VARCHAR2(50) NOT NULL,
    CONSTRAINT PK_Cultura PRIMARY KEY (cd_cultura)
);

-- Criação da tabela Responsavel
CREATE TABLE Responsavel (
    cd_responsavel INTEGER NOT NULL,
    nm_responsavel VARCHAR2(50) NOT NULL,
    nm_telefone VARCHAR2(50) NOT NULL,
    nm_email VARCHAR2(50) NOT NULL,
    CONSTRAINT PK_Responsavel PRIMARY KEY (cd_responsavel)
);

-- Criação da tabela Area_Plantio
CREATE TABLE Area_Plantio (
    cd_area INTEGER NOT NULL,
    vl_area_ha FLOAT NOT NULL,
    vl_espacamento FLOAT NOT NULL,
    vl_densidade FLOAT NOT NULL,
    vl_taxa_semeadura FLOAT NOT NULL,
    vl_peso_ha FLOAT NOT NULL,
    cd_cultura INTEGER NOT NULL,
    cd_responsavel INTEGER NOT NULL,
    CONSTRAINT PK_Area_Plantio PRIMARY KEY (cd_area),
    CONSTRAINT FK_Area_Plantio_Cultura FOREIGN KEY (cd_cultura) REFERENCES Cultura(cd_cultura),
    CONSTRAINT FK_Area_Plantio_Responsavel FOREIGN KEY (cd_responsavel) REFERENCES Responsavel(cd_responsavel)
);

-- Criação da tabela Sensor
CREATE TABLE Sensor (
    cd_sensor INTEGER NOT NULL,
    tp_sensor VARCHAR2(50) NOT NULL,
    nm_modelo VARCHAR2(50) NOT NULL,
    cd_area INTEGER NOT NULL,
    CONSTRAINT PK_Sensor PRIMARY KEY (cd_sensor),
    CONSTRAINT FK_Sensor_Area_Plantio FOREIGN KEY (cd_area) REFERENCES Area_Plantio(cd_area)
);

-- Criação da tabela Leitura_Sensor
CREATE TABLE Leitura_Sensor (
    cd_leitura INTEGER NOT NULL,
    dt_leitura DATE NOT NULL,
    vl_valor FLOAT,
    cd_sensor INTEGER NOT NULL,
    CONSTRAINT PK_Leitura_Sensor PRIMARY KEY (cd_leitura, cd_sensor),
    CONSTRAINT FK_Leitura_Sensor_Sensor FOREIGN KEY (cd_sensor) REFERENCES Sensor(cd_sensor)
);

-- Criação da tabela Aplicacao com novos campos para P, K, N e produto
CREATE TABLE Aplicacao (
    cd_aplicacao INTEGER NOT NULL,
    dt_aplicacao DATE NOT NULL,
    tp_aplicacao VARCHAR2(50) NOT NULL,
    vl_quantidade FLOAT,
    vl_fosforo FLOAT,
    vl_potassio FLOAT,
    vl_nitrogenio FLOAT,
    ds_produto VARCHAR2(100),
    cd_area INTEGER NOT NULL,
    CONSTRAINT PK_Aplicacao PRIMARY KEY (cd_aplicacao),
    CONSTRAINT FK_Aplicacao_Area_Plantio FOREIGN KEY (cd_area) REFERENCES Area_Plantio(cd_area)
);




-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             6
-- CREATE INDEX                             0
-- ALTER TABLE                             11
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
