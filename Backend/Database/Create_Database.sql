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
    `ID`         INT          NOT NULL,
    `Conference` VARCHAR(255) NOT NULL,
    PRIMARY KEY (ID, Conference),
    CONSTRAINT FK_journal_conferences_journal_id FOREIGN KEY (ID) REFERENCES journal (ID) ON DELETE CASCADE
);

CREATE TABLE paper
(
    `ID`         INT PRIMARY KEY,
    `Topic`      VARCHAR(255)                  NOT NULL,
    `Status`     ENUM ('Published', 'Ongoing') NOT NULL DEFAULT 'Ongoing',
    `Start_Date` DATE                          NOT NULL,
    `End_Date`   DATE                          NULL,
    `Journal_ID` INT                           NULL,
    CONSTRAINT FK_paper_journal_id FOREIGN KEY (Journal_ID) REFERENCES journal (ID) ON DELETE SET NULL
);

CREATE TABLE meeting
(
    `ID`         INT PRIMARY KEY,
    `Paper_ID`   INT                                        NOT NULL,
    `Start_Time` DATETIME                                   NOT NULL,
    `End_Time`   DATETIME                                   NOT NULL,
    `Link`       VARCHAR(255) UNIQUE                        NOT NULL,
    `Status`     ENUM ('Accepted', 'Rejected', 'Requested') NOT NULL DEFAULT 'Requested',
    `Remarks`    VARCHAR(255)                               NOT NULL,
    CONSTRAINT FK_meeting_paper_id FOREIGN KEY (Paper_ID) REFERENCES paper (ID) ON DELETE CASCADE
);

CREATE TABLE student
(
    `SRN`        CHAR(13) PRIMARY KEY,
    `First_Name` VARCHAR(25)                              NOT NULL,
    `Last_Name`  VARCHAR(25)                              NOT NULL,
    `Department` ENUM ('CSE', 'ECE', 'EEE', 'AIML', 'ME') NOT NULL,
    `Semester`   NUMERIC(1)                               NOT NULL,
    `Section`    CHAR(1)                                  NOT NULL,
    `Password`   VARCHAR(20)                              NOT NULL
);

CREATE TABLE student_writes_paper
(
    `SRN`      CHAR(13),
    `Paper_ID` INT,
    PRIMARY KEY (SRN, Paper_ID),
    CONSTRAINT FK_student_writes_paper_student_srn FOREIGN KEY (SRN) REFERENCES student (SRN) ON DELETE CASCADE,
    CONSTRAINT FK_student_writes_paper_paper_id FOREIGN KEY (Paper_ID) REFERENCES paper (ID) ON DELETE CASCADE
);

CREATE TABLE faculty
(
    `ID`         CHAR(8) PRIMARY KEY,
    `First_Name` VARCHAR(25)                              NOT NULL,
    `Last_Name`  VARCHAR(25)                              NOT NULL,
    `Department` ENUM ('CSE', 'ECE', 'EEE', 'AIML', 'ME') NOT NULL,
    `Domain`     VARCHAR(50)                              NOT NULL,
    `Password`   VARCHAR(20)                              NOT NULL
);

CREATE TABLE faculty_advises_paper
(
    `Faculty_ID`  CHAR(8)      NOT NULL,
    `Paper_ID`    INT          NOT NULL,
    `Suggestions` VARCHAR(200) NOT NULL DEFAULT '',
    `Timestamp`   DATETIME     NOT NULL DEFAULT '2020-01-01 00:00:00',
    PRIMARY KEY (Faculty_ID, Paper_ID, Suggestions),
    CONSTRAINT FK_faculty_advises_paper_faculty_id FOREIGN KEY (Faculty_ID) REFERENCES faculty (ID) ON DELETE CASCADE,
    CONSTRAINT FK_faculty_advises_paper_paper_id FOREIGN KEY (Paper_ID) REFERENCES paper (ID) ON DELETE CASCADE
);

CREATE TABLE literature_survey
(
    `DOI`      VARCHAR(50) PRIMARY KEY,
    `Keywords` VARCHAR(300) NOT NULL,
    `Date`     DATE         NOT NULL
);

CREATE TABLE literature_survey_authors
(
    `DOI`        VARCHAR(50) NOT NULL,
    `First_Name` VARCHAR(25) NOT NULL,
    `Last_Name`  VARCHAR(25) NOT NULL,
    PRIMARY KEY (DOI, First_Name, Last_Name),
    CONSTRAINT FK_literature_survey_authors_literature_survey_doi
        FOREIGN KEY (DOI) REFERENCES literature_survey (DOI) ON DELETE CASCADE
);

CREATE TABLE literature_survey_datasets
(
    `DOI`     VARCHAR(50) NOT NULL,
    `Dataset` VARCHAR(50) NOT NULL,
    PRIMARY KEY (DOI, Dataset),
    CONSTRAINT FK_literature_survey_datasets_literature_survey_doi
        FOREIGN KEY (DOI) REFERENCES literature_survey (DOI) ON DELETE CASCADE
);

CREATE TABLE paper_refs_literature_survey
(
    `DOI`      VARCHAR(50) NOT NULL,
    `Paper_ID` INT         NOT NULL,
    PRIMARY KEY (DOI, Paper_ID),
    CONSTRAINT FK_paper_refs_literature_survey_literature_survey_doi
        FOREIGN KEY (DOI) REFERENCES literature_survey (DOI) ON DELETE RESTRICT,
    CONSTRAINT FK_paper_refs_literature_survey_paper_id FOREIGN KEY (Paper_ID) REFERENCES paper (ID) ON DELETE CASCADE
);
