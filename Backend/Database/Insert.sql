USE research_mgmt;

INSERT INTO journal
VALUES (1, 'https://www.sciencedirect.com/journal/decision-analytics-journal', 0.9),
       (2, 'https://www.sciencedirect.com/journal/advances-in-engineering-software', 7),
       (3, 'https://www.sciencedirect.com/journal/slas-discovery', 6.4);

INSERT INTO journal_conferences
VALUES (1, 'Conference 1'),
       (2, 'Conference 2'),
       (3, 'Conference 3');

INSERT INTO paper
VALUES ('1', 'Most-Influential nodes in a spacio-temporal network', 'Ongoing', '2022-05-03', NULL, 1),
       ('2', '', 'Ongoing', '2022-05-03', NULL, NULL),
       ('3', 'Identifying Kannada Letters Using LLMs', 'Published', '2023-10-11', NULL, 2);