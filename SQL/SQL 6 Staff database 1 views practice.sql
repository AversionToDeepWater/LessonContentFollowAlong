CREATE DATABASE sqlsix;
use sqlsix; -- or create any other temporary DB

-- PART 1

CREATE TABLE sqlsix.staff (
  `employeeID` INT NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `jobtitle` VARCHAR(45) NOT NULL,
  `managerID` INT NOT NULL,
  `department` VARCHAR(45) NULL,
  `salary` INT NOT NULL,
  `dateofbirth` DATE NOT NULL,
  PRIMARY KEY (`employeeID`));

INSERT INTO staff(
    employeeID,
    firstName,
    lastName,
    jobtitle,
    managerID,
    department,
    salary,
    dateofbirth
) 
VALUES(
    1245,
    'Julie',
    'Smith',
    'DBA',
    '3333',
    'Database Administrators',
    50000,
    '1985-10-20'
),
(
    4578,
    'Jame',
    'Blogs',
    'DBA',
    '3333',
    'Database Administrators',
    52000,
    '1970-10-22'
);

ALTER TABLE sqlsix.staff 
CHANGE COLUMN `salary` `salary` INT(11) NULL DEFAULT 0 ,
CHANGE COLUMN `dateofbirth` `dateofbirth` DATE NULL DEFAULT '1900-01-01' ;

SELECT * FROM sqlsix.staff;
