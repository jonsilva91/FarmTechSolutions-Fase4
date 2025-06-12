-- SQLite DDL para Farmtech (FASE 4) com seed de Responsável

PRAGMA foreign_keys = ON;

-- Limpa o ambiente caso exista de execuções anteriores
DROP TABLE IF EXISTS Aplicacao;
DROP TABLE IF EXISTS Leitura_Sensor;
DROP TABLE IF EXISTS Sensor;
DROP TABLE IF EXISTS Area_Plantio;
DROP TABLE IF EXISTS Responsavel;
DROP TABLE IF EXISTS Cultura;

-- Criação da tabela Cultura
CREATE TABLE Cultura (
    cd_cultura   INTEGER PRIMARY KEY AUTOINCREMENT,
    nm_cultura   TEXT    NOT NULL,
    tp_cultura   TEXT    NOT NULL
);

-- Criação da tabela Responsavel
CREATE TABLE Responsavel (
    cd_responsavel INTEGER PRIMARY KEY AUTOINCREMENT,
    nm_responsavel TEXT    NOT NULL,
    nm_telefone    TEXT    NOT NULL,
    nm_email       TEXT    NOT NULL
);
-- Seed: usuário padrão para Responsavel
INSERT INTO Responsavel (nm_responsavel, nm_telefone, nm_email)
VALUES ('Responsável Padrão', '(00)0000-0000', 'default@farmtech.local');

-- Criação da tabela Área de Plantio
CREATE TABLE Area_Plantio (
    cd_area           INTEGER PRIMARY KEY AUTOINCREMENT,
    vl_area_ha        REAL    NOT NULL,
    vl_espacamento    REAL    NOT NULL,
    vl_densidade      REAL    NOT NULL,
    vl_taxa_semeadura REAL    NOT NULL,
    vl_peso_ha        REAL    NOT NULL,
    cd_cultura        INTEGER NOT NULL,
    cd_responsavel    INTEGER NOT NULL,
    ds_produtividade  TEXT,
    FOREIGN KEY (cd_cultura)     REFERENCES Cultura(cd_cultura),
    FOREIGN KEY (cd_responsavel) REFERENCES Responsavel(cd_responsavel)
);

-- Criação da tabela Sensor
CREATE TABLE Sensor (
    cd_sensor  INTEGER PRIMARY KEY AUTOINCREMENT,
    tp_sensor  TEXT    NOT NULL,
    nm_modelo  TEXT    NOT NULL,
    cd_area    INTEGER NOT NULL,
    FOREIGN KEY (cd_area) REFERENCES Area_Plantio(cd_area)
);

-- Criação da tabela Leitura de Sensor
CREATE TABLE Leitura_Sensor (
    cd_leitura  INTEGER PRIMARY KEY AUTOINCREMENT,
    cd_sensor   INTEGER NOT NULL,
    dt_leitura  TEXT    NOT NULL,
    vl_valor    REAL,
    FOREIGN KEY (cd_sensor) REFERENCES Sensor(cd_sensor)
);

-- Criação da tabela Aplicacao (adubação / fungicida)
CREATE TABLE Aplicacao (
    cd_aplicacao  INTEGER PRIMARY KEY AUTOINCREMENT,
    dt_aplicacao  TEXT    NOT NULL,
    tp_aplicacao  TEXT    NOT NULL,
    vl_quantidade REAL,
    vl_fosforo    REAL,
    vl_potassio   REAL,
    vl_nitrogenio REAL,
    nm_produto    TEXT,
    cd_area       INTEGER NOT NULL,
    FOREIGN KEY (cd_area) REFERENCES Area_Plantio(cd_area)
);
