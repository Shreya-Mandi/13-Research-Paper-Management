USE research_mgmt;

-- Insert into journal table
INSERT INTO journal
VALUES (1, 'https://www.sciencedirect.com/journal/decision-analytics-journal', 0.9),
       (2, 'https://www.sciencedirect.com/journal/advances-in-engineering-software', 7),
       (3, 'https://www.sciencedirect.com/journal/slas-discovery', 6.4);

-- Insert into journal_conferences table
INSERT INTO journal_conferences
VALUES (1, 'Conference 1'),
       (2, 'Conference 2'),
       (3, 'Conference 3');

-- Insert into paper table
INSERT INTO paper
VALUES (1, 'Most-Influential nodes in a spacio-temporal network', 'Ongoing', '2022-05-03', NULL, 1),
       (2, '', 'Ongoing', '2022-05-03', NULL, NULL),
       (3, 'Identifying Kannada Letters Using LLMs', 'Published', '2023-10-11', NULL, 2);

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

-- Insert into meeting table
INSERT INTO meeting VALUES
(1, 1, '2023-02-01 10:00:00', '2023-02-01 12:00:00', 'https://meeting1.com', 'Accepted', 'Good presentation'),
(2, 2, '2023-03-15 14:00:00', '2023-03-15 16:00:00', 'https://meeting2.com', 'Requested', 'Pending review'),
(3, 3, '2023-03-02 11:30:00', '2023-03-02 13:30:00', 'https://meeting3.com', 'Accepted', 'Excellent work');

-- Insert into student_writes_paper table
INSERT INTO student_writes_paper VALUES
('PES2UG21CS001', 1),
('PES2UG21CS002', 2),
('PES2UG21CS003', 3);

-- Insert into faculty_advises_paper table
INSERT INTO faculty_advises_paper VALUES
('PESCS001', 1, 'Excellent work', '2023-02-05 15:00:00'),
('PESCS002', 2, 'Consider blockchain', '2023-05-11 15:34:23'); -- Replace 'YYYY-MM-DD HH:MI:SS' with the actual timestamp
-- Continue with additional records if needed

