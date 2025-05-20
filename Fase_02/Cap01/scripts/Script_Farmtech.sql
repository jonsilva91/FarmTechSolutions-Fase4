-- Gerado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   em:        2025-04-22 05:18:18 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE Aplicacao CASCADE CONSTRAINTS 
;

DROP TABLE Area_Plantio CASCADE CONSTRAINTS 
;

DROP TABLE Cultura CASCADE CONSTRAINTS 
;

DROP TABLE Leitura_Sensor CASCADE CONSTRAINTS 
;

DROP TABLE Responsavel CASCADE CONSTRAINTS 
;

DROP TABLE Sensor CASCADE CONSTRAINTS 
;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE Aplicacao 
    ( 
     cd_aplicacao  INTEGER  NOT NULL , 
     dt_aplicacao  DATE  NOT NULL , 
     tp_aplicacao  VARCHAR2 (50)  NOT NULL , 
     vl_quantidade FLOAT  NOT NULL , 
     cd_area       INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Aplicacao 
    ADD CONSTRAINT PK_Aplicacao PRIMARY KEY ( cd_aplicacao ) ;

CREATE TABLE Area_Plantio 
    ( 
     cd_area           INTEGER  NOT NULL , 
     vl_area_ha        FLOAT  NOT NULL , 
     vl_espacamento    FLOAT  NOT NULL , 
     vl_densidade      FLOAT  NOT NULL , 
     vl_taxa_semeadura FLOAT  NOT NULL , 
     vl_peso_ha        FLOAT  NOT NULL , 
     cd_cultura        INTEGER  NOT NULL , 
     cd_responsavel    INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Area_Plantio 
    ADD CONSTRAINT PK_Area_Plantio PRIMARY KEY ( cd_area ) ;

CREATE TABLE Cultura 
    ( 
     cd_cultura INTEGER  NOT NULL , 
     nm_cultura VARCHAR2 (50)  NOT NULL , 
     tp_cultura VARCHAR2 (50)  NOT NULL 
    ) 
;

ALTER TABLE Cultura 
    ADD CONSTRAINT PK_Cultura PRIMARY KEY ( cd_cultura ) ;

CREATE TABLE Leitura_Sensor 
    ( 
     cd_leitura INTEGER  NOT NULL , 
     dt_leitura DATE  NOT NULL , 
     vl_valor   FLOAT , 
     cd_sensor  INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Leitura_Sensor 
    ADD CONSTRAINT PK_Leitura_Sensor PRIMARY KEY ( cd_leitura, cd_sensor ) ;

CREATE TABLE Responsavel 
    ( 
     cd_responsavel INTEGER  NOT NULL , 
     nm_responsavel VARCHAR2 (50)  NOT NULL , 
     nm_telefone    VARCHAR2 (50)  NOT NULL , 
     nm_email       VARCHAR2 (50)  NOT NULL 
    ) 
;

ALTER TABLE Responsavel 
    ADD CONSTRAINT PK_Responsavel PRIMARY KEY ( cd_responsavel ) ;

CREATE TABLE Sensor 
    ( 
     cd_sensor INTEGER  NOT NULL , 
     tp_sensor VARCHAR2 (50)  NOT NULL , 
     nm_modelo VARCHAR2 (50)  NOT NULL , 
     cd_area   INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Sensor 
    ADD CONSTRAINT PK_Sensor PRIMARY KEY ( cd_sensor ) ;

ALTER TABLE Aplicacao 
    ADD CONSTRAINT FK_Aplicacao_Area_Plantio FOREIGN KEY 
    ( 
     cd_area
    ) 
    REFERENCES Area_Plantio 
    ( 
     cd_area
    ) 
;

ALTER TABLE Area_Plantio 
    ADD CONSTRAINT FK_Area_Plantio_Cultura FOREIGN KEY 
    ( 
     cd_cultura
    ) 
    REFERENCES Cultura 
    ( 
     cd_cultura
    ) 
;

ALTER TABLE Area_Plantio 
    ADD CONSTRAINT FK_Area_Plantio_Responsavel FOREIGN KEY 
    ( 
     cd_responsavel
    ) 
    REFERENCES Responsavel 
    ( 
     cd_responsavel
    ) 
;

ALTER TABLE Leitura_Sensor 
    ADD CONSTRAINT FK_Leitura_Sensor_Sensor FOREIGN KEY 
    ( 
     cd_sensor
    ) 
    REFERENCES Sensor 
    ( 
     cd_sensor
    ) 
;

ALTER TABLE Sensor 
    ADD CONSTRAINT FK_Sensor_Area_Plantio FOREIGN KEY 
    ( 
     cd_area
    ) 
    REFERENCES Area_Plantio 
    ( 
     cd_area
    ) 
;



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
