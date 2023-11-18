USE research_mgmt;


INSERT INTO journal
VALUES (1, 'https://www.sciencedirect.com/journal/decision-analytics-journal', 0.9),
       (2, 'https://www.sciencedirect.com/journal/advances-in-engineering-software', 7),
       (3, 'https://www.sciencedirect.com/journal/slas-discovery', 6.4),
       (4, 'https://www.sciencedirect.com/journal/journal-of-computational-science', 4.5),
       (5, 'https://www.sciencedirect.com/journal/information-systems', 8.2),
       (6, 'https://www.sciencedirect.com/journal/journal-of-visual-communication-and-image-representation', 5.8),
       (7, 'https://www.sciencedirect.com/journal/computers-and-security', 6.7),
       (8, 'https://www.sciencedirect.com/journal/computer-languages-systems-and-structures', 7.1),
       (9, 'https://www.sciencedirect.com/journal/journal-of-computational-and-applied-mathematics', 9.3),
       (10, 'https://www.sciencedirect.com/journal/theoretical-computer-science', 8.6);


INSERT INTO journal_conferences
VALUES (1, 'Conference 1'),
       (2, 'Conference 2'),
       (2, 'Conference 3'),
       (3, 'Conference 11'),
       (4, 'Conference 4'),
       (4, 'Conference 6'),
       (5, 'Conference 5'),
       (6, 'Conference 12'),
       (7, 'Conference 7'),
       (8, 'Conference 13'),
       (9, 'Conference 9'),
       (10, 'Conference 8'),
       (10, 'Conference 10');


INSERT INTO paper
VALUES (1, 'Most-Influential nodes in a spacio-temporal network', 'Ongoing', '2022-05-03', NULL, 1),
       (2, 'How to kill a person in 3 days', 'Ongoing', '2022-05-03', NULL, NULL),
       (3, 'Identifying Kannada Letters Using LLMs', 'Published', '2023-10-11', '2023-12-14', 2),
       (4, 'Analysis of Machine Learning Algorithms', 'Published', '2022-08-20', '2022-11-15', 4),
       (5, 'Blockchain Technology in Cybersecurity', 'Ongoing', '2023-01-10', NULL, 5),
       (6, 'Digital Image Processing Techniques', 'Published', '2023-05-25', '2023-09-28', 6),
       (7, 'Secure Data Transmission in IoT', 'Ongoing', '2023-03-15', NULL, 7),
       (8, 'Programming Language Trends', 'Ongoing', '2023-04-30', NULL, NULL),
       (9, 'Numerical Methods for Scientific Computing', 'Published', '2022-12-01', '2023-03-23', 9),
       (10, 'Human-Computer Interaction Studies', 'Published', '2023-09-05', '2023-12-15', 10);


INSERT INTO meeting
VALUES
       (1, 1, '2023-02-01 10:00:00', '2023-02-01 12:00:00', 'https://meeting1.com', 'Accepted', 'Requesting resources as per requirement. Need guidance on project scope and resources.'),
       (2, 2, '2023-03-15 14:00:00', '2023-03-15 16:00:00', 'https://meeting2.com', 'Requested', 'Requesting an update on final deliverable and project progress.'),
       (3, 3, '2023-03-02 11:30:00', '2023-03-02 13:30:00', 'https://meeting3.com', 'Accepted', 'Discussion needed due to insufficient data for ongoing project.'),
       (4, 4, '2023-09-01 09:30:00', '2023-09-01 11:30:00', 'https://meeting4.com', 'Accepted', 'Interested in discussing and implementing the great insights gathered.'),
       (5, 5, '2023-08-15 13:00:00', '2023-08-15 15:00:00', 'https://meeting5.com', 'Requested', 'Stuck with machine tool; seeking guidance and solution.'),
       (6, 6, '2023-09-10 11:30:00', '2023-09-10 13:30:00', 'https://meeting6.com', 'Accepted', 'Excited to discuss and explore interesting findings.'),
       (7, 7, '2023-10-05 10:00:00', '2023-10-05 12:00:00', 'https://meeting7.com', 'Requested', 'Clarity needed on project scope to align efforts.'),
       (8, 8, '2023-11-20 14:30:00', '2023-11-20 16:30:00', 'https://meeting8.com', 'Accepted', 'Positive feedback; discussing further improvements.'),
       (9, 9, '2023-12-10 10:45:00', '2023-12-10 12:45:00', 'https://meeting9.com', 'Requested', 'Align on budget allocation and project priorities.'),
       (10, 1, '2023-04-05 11:00:00', '2023-04-05 13:00:00', 'https://meeting10.com', 'Accepted', 'Good progress made; providing a progress update.'),
       (11, 1, '2023-06-15 14:30:00', '2023-06-15 16:30:00', 'https://meeting11.com', 'Rejected', 'Not aligned with project goals; reconsidering approach.'),
       (12, 2, '2023-05-10 09:00:00', '2023-05-10 11:00:00', 'https://meeting12.com', 'Accepted', 'In-depth discussion needed for project details and direction.'),
       (13, 2, '2023-07-20 13:30:00', '2023-07-20 15:30:00', 'https://meeting13.com', 'Accepted', 'Reviewing promising outcomes for implementation.'),
       (14, 3, '2023-08-01 10:15:00', '2023-08-01 12:15:00', 'https://meeting14.com', 'Rejected', 'Insufficient data presented for decision-making.'),
       (15, 3, '2023-09-25 15:00:00', '2023-09-25 17:00:00', 'https://meeting15.com', 'Accepted', 'Positive feedback on methodology; exploring improvements.'),
       (16, 4, '2023-11-10 12:30:00', '2023-11-10 14:30:00', 'https://meeting16.com', 'Requested', 'Seeking approval for project extension.'),
       (17, 4, '2023-12-05 09:45:00', '2023-12-05 11:45:00', 'https://meeting17.com', 'Accepted', 'Considering a change in project direction; discussing implications.'),
       (18, 5, '2023-10-20 14:00:00', '2023-10-20 16:00:00', 'https://meeting18.com', 'Rejected', 'Not aligning with the current focus; revisiting later.'),
       (19, 5, '2023-11-30 11:30:00', '2023-11-30 13:30:00', 'https://meeting19.com', 'Requested', 'Discussing team resource allocation and workload balancing.'),
       (20, 6, '2023-12-15 10:00:00', '2023-12-15 12:00:00', 'https://meeting20.com', 'Accepted', 'Reviewing and implementing encouraging results.'),
       (21, 6, '2023-01-05 14:30:00', '2023-01-05 16:30:00', 'https://meeting21.com', 'Rejected', 'Not aligned with current priorities; considering future engagement.'),
       (22, 7, '2023-02-10 09:00:00', '2023-02-10 11:00:00', 'https://meeting22.com', 'Requested', 'Pending review; seeking guidance and direction.'),
       (23, 7, '2023-03-25 13:30:00', '2023-03-25 15:30:00', 'https://meeting23.com', 'Rejected', 'Insufficient details provided; request more comprehensive information.'),
       (24, 8, '2023-04-20 10:15:00', '2023-04-20 12:15:00', 'https://meeting24.com', 'Accepted', 'Positive feedback on methodology; discussing implementation strategies.'),
       (25, 8, '2023-05-25 15:00:00', '2023-05-25 17:00:00', 'https://meeting25.com', 'Requested', 'Pending decision; seeking approval for next steps.');

INSERT INTO student
VALUES ('PES2UG21CS001', 'John', 'Doe', 'CSE', 5, 'A', 'pesu@123'),
       ('PES2UG21CS002', 'Jane', 'Smith', 'CSE', 5, 'B', 'password2'),
       ('PES2UG21CS003', 'Bob', 'Johnson', 'ECE', 4, 'C', 'password3'),
       ('PES2UG21CS004', 'Alice', 'Williams', 'AIML', 6, 'A', 'password4'),
       ('PES2UG21CS005', 'Charlie', 'Brown', 'ME', 4, 'B', 'password5'),
       ('PES2UG21CS006', 'Eva', 'Miller', 'EEE', 6, 'C', 'password6'),
       ('PES2UG21CS007', 'David', 'Davis', 'CSE', 5, 'A', 'password7'),
       ('PES2UG21CS008', 'Grace', 'White', 'AIML', 6, 'B', 'password8'),
       ('PES2UG21CS009', 'Frank', 'Taylor', 'ECE', 4, 'C', 'password9'),
       ('PES2UG21CS010', 'Helen', 'Clark', 'EEE', 6, 'A', 'password10');


INSERT INTO student_writes_paper
VALUES ('PES2UG21CS001', 1),
       ('PES2UG21CS001', 2),
       ('PES2UG21CS001', 4),
       ('PES2UG21CS002', 2),
       ('PES2UG21CS002', 3),
       ('PES2UG21CS003', 3),
       ('PES2UG21CS003', 4),
       ('PES2UG21CS004', 4),
       ('PES2UG21CS004', 5),
       ('PES2UG21CS005', 5),
       ('PES2UG21CS005', 6),
       ('PES2UG21CS006', 6),
       ('PES2UG21CS006', 7),
       ('PES2UG21CS007', 7),
       ('PES2UG21CS007', 8),
       ('PES2UG21CS008', 8),
       ('PES2UG21CS008', 9),
       ('PES2UG21CS009', 9),
       ('PES2UG21CS009', 10),
       ('PES2UG21CS010', 10);


INSERT INTO faculty
VALUES ('PESCS001', 'Dr. Michael', 'Johnson', 'CSE', 'Machine Learning', 'pesadm@123'),
       ('PESCS002', 'Prof. Sarah', 'Smith', 'ECE', 'Signal Processing', 'faculty_password2'),
       ('PESCS003', 'Dr. Robert', 'Brown', 'AIML', 'Natural Language Processing', 'faculty_password3'),
       ('PESCS004', 'Prof. Emily', 'Jones', 'ME', 'Thermal Engineering', 'faculty_password4'),
       ('PESCS005', 'Dr. Chris', 'Taylor', 'EEE', 'Power Systems', 'faculty_password5'),
       ('PESCS006', 'Prof. Jessica', 'Clark', 'CSE', 'Database Systems', 'faculty_password6'),
       ('PESCS007', 'Dr. Andrew', 'Williams', 'AIML', 'Computer Vision', 'faculty_password7'),
       ('PESCS008', 'Prof. Laura', 'Davis', 'ECE', 'Communication Systems', 'faculty_password8'),
       ('PESCS009', 'Dr. Daniel', 'White', 'ME', 'Fluid Dynamics', 'faculty_password9'),
       ('PESCS010', 'Prof. Megan', 'Miller', 'EEE', 'Power Electronics', 'faculty_password10');


INSERT INTO faculty_advises_paper
VALUES ('PESCS001', 1, 'Excellent work', '2023-02-05 15:00:00'),
       ('PESCS001', 4, '', '2023-02-05 15:00:00'),
       ('PESCS002', 2, 'Consider blockchain', '2023-05-11 15:34:23'),
       ('PESCS003', 3, 'Impressive research', '2023-03-20 10:45:00'),
       ('PESCS004', 4, 'Well-documented findings', '2023-06-01 14:15:30'),
       ('PESCS005', 5, 'Consider statistical analysis', '2023-04-10 11:30:45'),
       ('PESCS006', 6, 'Interesting topic, explore further', '2023-05-25 09:20:00'),
       ('PESCS007', 7, 'Good progress, keep it up', '2023-03-15 13:45:00'),
       ('PESCS008', 8, 'Address security concerns', '2023-04-30 16:00:00'),
       ('PESCS009', 9, 'Well-structured paper', '2023-01-15 12:10:00'),
       ('PESCS010', 10, 'Incorporate user feedback', '2023-09-10 17:30:00'),
       ('PESCS001', 2, 'In-depth review', '2023-08-25 14:00:00'),
       ('PESCS002', 3, 'Consider additional experiments', '2023-09-15 12:30:00'),
       ('PESCS003', 4, 'Address methodology concerns', '2023-07-05 11:15:00'),
       ('PESCS004', 5, 'Explore real-world applications', '2023-11-10 10:30:00'),
       ('PESCS005', 8, 'Detailed analysis needed', '2023-10-20 13:45:00'),
       ('PESCS006', 9, 'Provide more references', '2023-09-05 09:00:00'),
       ('PESCS007', 10, 'Elaborate on data collection methods', '2023-12-01 15:30:00'),
       ('PESCS008', 1, 'Discuss potential improvements', '2023-08-15 11:00:00'),
       ('PESCS009', 4, 'Clarify experimental setup', '2023-06-20 14:45:00'),
       ('PESCS010', 7, 'Interesting findings, further exploration needed', '2023-07-15 16:30:00'),
       ('PESCS001', 9, 'Consider alternative approaches', '2023-09-30 09:45:00'),
       ('PESCS002', 9, 'Provide more context in the introduction', '2023-10-25 12:00:00'),
       ('PESCS003', 3, 'Address limitations in the discussion', '2023-11-20 17:15:00'),
       ('PESCS004', 2, 'Highlight practical implications', '2023-12-10 10:00:00'),
       ('PESCS005', 5, 'Discuss potential future work', '2023-12-25 14:30:00');


INSERT INTO literature_survey
VALUES ('DOI001', 'Machine Learning, Artificial Intelligence', '2023-01-15'),
       ('DOI002', 'Signal Processing, Communication', '2023-02-20'),
       ('DOI003', 'Natural Language Processing', '2023-03-10'),
       ('DOI004', 'Thermal Engineering, Fluid Dynamics', '2023-04-05'),
       ('DOI005', 'Power Systems, Power Electronics', '2023-05-22'),
       ('DOI006', 'Database Systems, Computer Vision', '2023-06-10'),
       ('DOI007', 'Computer Vision, Artificial Intelligence', '2023-07-18'),
       ('DOI008', 'Fluid Dynamics, Signal Processing', '2023-08-02');


INSERT INTO literature_survey_authors
VALUES ('DOI001', 'John', 'Doe'),
       ('DOI001', 'Jane', 'Smith'),
       ('DOI002', 'Bob', 'Johnson'),
       ('DOI002', 'Alice', 'Williams'),
       ('DOI003', 'Eva', 'Miller'),
       ('DOI003', 'Andrew', 'Jones'),
       ('DOI004', 'Charlie', 'Brown'),
       ('DOI004', 'Emma', 'Johnson'),
       ('DOI005', 'Grace', 'White'),
       ('DOI005', 'Daniel', 'Miller'),
       ('DOI006', 'David', 'Davis'),
       ('DOI006', 'Megan', 'Clark'),
       ('DOI007', 'Frank', 'Taylor'),
       ('DOI007', 'Laura', 'Smith'),
       ('DOI008', 'Helen', 'Clark'),
       ('DOI008', 'Brian', 'Williams');


INSERT INTO literature_survey_datasets
VALUES ('DOI001', 'Dataset 1'),
       ('DOI001', 'Dataset 9'),
       ('DOI002', 'Dataset 2'),
       ('DOI003', 'Dataset 3'),
       ('DOI003', 'Dataset 10'),
       ('DOI003', 'Dataset 11'),
       ('DOI004', 'Dataset 4'),
       ('DOI005', 'Dataset 5'),
       ('DOI006', 'Dataset 6'),
       ('DOI006', 'Dataset 12'),
       ('DOI007', 'Dataset 7'),
       ('DOI008', 'Dataset 8'),
       ('DOI008', 'Dataset 13');


INSERT INTO paper_refs_literature_survey
VALUES ('DOI001', 1),
       ('DOI001', 2),
       ('DOI002', 3),
       ('DOI002', 4),
       ('DOI003', 5),
       ('DOI003', 6),
       ('DOI004', 7),
       ('DOI004', 8),
       ('DOI005', 9),
       ('DOI005', 10),
       ('DOI006', 1),
       ('DOI006', 2),
       ('DOI007', 3),
       ('DOI007', 4),
       ('DOI008', 5),
       ('DOI008', 6);

