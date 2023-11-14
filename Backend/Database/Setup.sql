CREATE DATABASE research_mgmt;
USE research_mgmt;

CREATE TABLE journal
(
    `ID`   INT PRIMARY KEY,
    `Link` VARCHAR(255) UNIQUE NOT NULL,
    `Rank` DECIMAL(4, 2)       NULL
);

CREATE TABLE journal_conferences
(
    `ID`         INT PRIMARY KEY,
    `Conference` VARCHAR(255) NOT NULL,
    CONSTRAINT FK_journal_conferences_journal_id FOREIGN KEY (ID) REFERENCES journal (ID) ON DELETE CASCADE
);

CREATE TABLE paper
(
    `ID`         INT PRIMARY KEY,
    `Topic`      VARCHAR(255)                  NOT NULL,
    `Status`     ENUM ('Published', 'Ongoing') NOT NULL,
    `Start_Date` DATE                          NOT NULL,
    `End_Date`   DATE                          NULL,
    `Journal_ID` INT                           NULL,
    CONSTRAINT FK_paper_journal_id FOREIGN KEY (Journal_ID) REFERENCES journal (ID) ON DELETE NO ACTION
);