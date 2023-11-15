USE research_mgmt;


-- Insert into journal table
INSERT INTO journal
VALUES  (1, 'https://www.sciencedirect.com/journal/decision-analytics-journal', 0.9),
        (2, 'https://www.sciencedirect.com/journal/advances-in-engineering-software', 7),
        (3, 'https://www.sciencedirect.com/journal/slas-discovery', 6.4),
        (4, 'https://www.sciencedirect.com/journal/journal-of-computational-science', 4.5),
        (5, 'https://www.sciencedirect.com/journal/information-systems', 8.2),
        (6, 'https://www.sciencedirect.com/journal/journal-of-visual-communication-and-image-representation', 5.8),
        (7, 'https://www.sciencedirect.com/journal/computers-and-security', 6.7),
        (8, 'https://www.sciencedirect.com/journal/computer-languages-systems-and-structures', 7.1),
        (9, 'https://www.sciencedirect.com/journal/journal-of-computational-and-applied-mathematics', 9.3),
        (10, 'https://www.sciencedirect.com/journal/theoretical-computer-science', 8.6);


-- Insert into journal_conferences table
INSERT INTO journal_conferences
VALUES  (1, 'Conference 1'),
        (2, 'Conference 2'),
        (3, 'Conference 3'),
        (4, 'Conference 4'),
        (5, 'Conference 5'),
        (6, 'Conference 6'),
        (7, 'Conference 7'),
        (8, 'Conference 8'),
        (9, 'Conference 9'),
        (10, 'Conference 10');

-- Insert into paper table
INSERT INTO paper
VALUES  (1, 'Most-Influential nodes in a spacio-temporal network', 'Ongoing', '2022-05-03', NULL, 1),
        (2, '', 'Ongoing', '2022-05-03', NULL, NULL),
        (3, 'Identifying Kannada Letters Using LLMs', 'Published', '2023-10-11', NULL, 2),
        (4, 'Analysis of Machine Learning Algorithms', 'Published', '2022-08-20', '2022-11-15', 4),
        (5, 'Blockchain Technology in Cybersecurity', 'Ongoing', '2023-01-10', NULL, 5),
        (6, 'Digital Image Processing Techniques', 'Published', '2023-05-25', NULL, 6),
        (7, 'Secure Data Transmission in IoT', 'Ongoing', '2023-03-15', NULL, 7),
        (8, 'Programming Language Trends', 'Ongoing', '2023-04-30', NULL, NULL),
        (9, 'Numerical Methods for Scientific Computing', 'Published', '2022-12-01', NULL, 9),
        (10, 'Human-Computer Interaction Studies', 'Published', '2023-09-05', NULL, 10);


-- Insert into meeting table
INSERT INTO meeting VALUES
(1, 1, '2023-02-01 10:00:00', '2023-02-01 12:00:00', 'https://meeting1.com', 'Accepted', 'Good presentation'),
(2, 2, '2023-03-15 14:00:00', '2023-03-15 16:00:00', 'https://meeting2.com', 'Requested', 'Pending review'),
(3, 3, '2023-03-02 11:30:00', '2023-03-02 13:30:00', 'https://meeting3.com', 'Accepted', 'Excellent work'),
(4, 4, '2023-09-01 09:30:00', '2023-09-01 11:30:00', 'https://meeting4.com', 'Accepted', 'Great insights'),
(5, 5, '2023-08-15 13:00:00', '2023-08-15 15:00:00', 'https://meeting5.com', 'Requested', 'Pending review'),
(6, 6, '2023-09-10 11:30:00', '2023-09-10 13:30:00', 'https://meeting6.com', 'Accepted', 'Interesting findings'),
(7, 7, '2023-10-05 10:00:00', '2023-10-05 12:00:00', 'https://meeting7.com', 'Requested', 'Awaiting response'),
(8, 8, '2023-11-20 14:30:00', '2023-11-20 16:30:00', 'https://meeting8.com', 'Accepted', 'Positive feedback'),
(9, 9, '2023-12-10 10:45:00', '2023-12-10 12:45:00', 'https://meeting9.com', 'Requested', 'Pending decision');




-- Insert into student table
INSERT INTO student VALUES
('PES2UG21CS001', 'John', 'Doe', 'CSE', 5, 'A', 'password1'),
('PES2UG21CS002', 'Jane', 'Smith', 'CSE', 5, 'B', 'password2'),
('PES2UG21CS003', 'Bob', 'Johnson', 'ECE', 4, 'C', 'password3'),
('PES2UG21CS004', 'Alice', 'Williams', 'AIML', 6, 'A', 'password4'),
('PES2UG21CS005', 'Charlie', 'Brown', 'ME', 4, 'B', 'password5'),
('PES2UG21CS006', 'Eva', 'Miller', 'EEE', 6, 'C', 'password6'),
('PES2UG21CS007', 'David', 'Davis', 'CSE', 5, 'A', 'password7'),
('PES2UG21CS008', 'Grace', 'White', 'AIML', 6, 'B', 'password8'),
('PES2UG21CS009', 'Frank', 'Taylor', 'ECE', 4, 'C', 'password9'),
('PES2UG21CS010', 'Helen', 'Clark', 'EEE', 6, 'A', 'password10');


-- Insert into student_writes_paper table
INSERT INTO student_writes_paper VALUES
('PES2UG21CS004', 4),
('PES2UG21CS005', 5),
('PES2UG21CS006', 6),
('PES2UG21CS007', 7),
('PES2UG21CS008', 8),
('PES2UG21CS009', 9),
('PES2UG21CS010', 10),
('PES2UG21CS001', 1),
('PES2UG21CS002', 2),
('PES2UG21CS003', 3);

-- Insert into faculty table
INSERT INTO faculty VALUES
('PESCS001', 'Dr. Michael', 'Johnson', 'CSE', 'Machine Learning', 'faculty_password1'),
('PESCS002', 'Prof. Sarah', 'Smith', 'ECE', 'Signal Processing', 'faculty_password2'),
('PESCS003', 'Dr. Robert', 'Brown', 'AIML', 'Natural Language Processing', 'faculty_password3'),
('PESCS004', 'Prof. Emily', 'Jones', 'ME', 'Thermal Engineering', 'faculty_password4'),
('PESCS005', 'Dr. Chris', 'Taylor', 'EEE', 'Power Systems', 'faculty_password5'),
('PESCS006', 'Prof. Jessica', 'Clark', 'CSE', 'Database Systems', 'faculty_password6'),
('PESCS007', 'Dr. Andrew', 'Williams', 'AIML', 'Computer Vision', 'faculty_password7'),
('PESCS008', 'Prof. Laura', 'Davis', 'ECE', 'Communication Systems', 'faculty_password8'),
('PESCS009', 'Dr. Daniel', 'White', 'ME', 'Fluid Dynamics', 'faculty_password9'),
('PESCS010', 'Prof. Megan', 'Miller', 'EEE', 'Power Electronics', 'faculty_password10');


-- Insert into faculty_advises_paper table
INSERT INTO faculty_advises_paper VALUES
('PESCS003', 3, 'Impressive research', '2023-03-20 10:45:00'),
('PESCS004', 4, 'Well-documented findings', '2023-06-01 14:15:30'),
('PESCS005', 5, 'Consider statistical analysis', '2023-04-10 11:30:45'),
('PESCS006', 6, 'Interesting topic, explore further', '2023-05-25 09:20:00'),
('PESCS007', 7, 'Good progress, keep it up', '2023-03-15 13:45:00'),
('PESCS008', 8, 'Address security concerns', '2023-04-30 16:00:00'),
('PESCS009', 9, 'Well-structured paper', '2023-01-15 12:10:00'),
('PESCS010', 10, 'Incorporate user feedback', '2023-09-10 17:30:00'),
('PESCS002', 1, 'Excellent analysis', '2023-08-02 10:00:00'),
('PESCS001', 2, 'Explore comparative studies', '2023-07-20 11:45:00');

-- Insert into literature_survey table
INSERT INTO literature_survey VALUES
('DOI001', 'Machine Learning, Artificial Intelligence', '2023-01-15'),
('DOI002', 'Signal Processing, Communication', '2023-02-20'),
('DOI003', 'Natural Language Processing', '2023-03-10'),
('DOI004', 'Thermal Engineering, Fluid Dynamics', '2023-04-05'),
('DOI005', 'Power Systems, Power Electronics', '2023-05-22'),
('DOI006', 'Database Systems, Computer Vision', '2023-06-10'),
('DOI007', 'Computer Vision, Artificial Intelligence', '2023-07-18'),
('DOI008', 'Fluid Dynamics, Signal Processing', '2023-08-02');


-- Insert into literature_survey_authors table
INSERT INTO literature_survey_authors VALUES
('DOI001', 'John', 'Doe'),
('DOI002', 'Bob', 'Johnson'),
('DOI003', 'Eva', 'Miller'),
('DOI004', 'Charlie', 'Brown'),
('DOI005', 'Grace', 'White'),
('DOI006', 'David', 'Davis'),
('DOI007', 'Frank', 'Taylor'),
('DOI008', 'Helen', 'Clark');


-- Insert into literature_survey_datasets table
INSERT INTO literature_survey_datasets VALUES
('DOI001', 'Dataset 1'),
('DOI002', 'Dataset 2'),
('DOI003', 'Dataset 3'),
('DOI004', 'Dataset 4'),
('DOI005', 'Dataset 5'),
('DOI006', 'Dataset 6'),
('DOI007', 'Dataset 7'),
('DOI008', 'Dataset 8');

-- Insert into paper_refs_literature_survey table
INSERT INTO paper_refs_literature_survey VALUES
('DOI001', 1),
('DOI002', 2),
('DOI003', 3),
('DOI004', 4),
('DOI005', 5),
('DOI006', 6),
('DOI007', 7),
('DOI008', 8);

