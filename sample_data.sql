-- Sample SQL to create `student` table and insert rows (for MySQL)
CREATE DATABASE IF NOT EXISTS studentdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE studentdb;

CREATE TABLE IF NOT EXISTS students_student (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  roll_no VARCHAR(30),
  ppt_url VARCHAR(500),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO students_student (name, roll_no, ppt_url) VALUES
('Karthik','R001','https://res.cloudinary.com/demo/sample.pdf'),
('Anita','R002','https://res.cloudinary.com/demo/sample.pdf');
