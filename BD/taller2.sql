create database CompanyDB;

use CompanyDB;

create table Employees(
EmployeeID int primary key auto_increment,
FirstName varchar(50),
LastName varchar(50),
Email varchar(50),
Salary decimal(10,2)
);

INSERT INTO Employees (FirstName, LastName, Email, Salary) 
VALUES 
('John', 'Doe', 'john.doe@example.com', 50000.00),
('Jane', 'Smith', 'jane.smith@example.com', 55000.00),
('Michael', 'Brown', 'michael.brown@example.com', 60000.00),
('Emily', 'Jones', 'emily.jones@example.com', 62000.00),
('Chris', 'Johnson', 'chris.johnson@example.com', 58000.00);

DELIMITER //
CREATE PROCEDURE GetEmployees()
BEGIN
    SELECT 
        JSON_ARRAYAGG(
            JSON_OBJECT(
                'EmployeeID', EmployeeID,
                'FirstName', FirstName,
                'LastName', LastName,
                'Email', Email,
                'Salary', Salary
            )
        ) AS employees_json
    FROM Employees;
END //

DELIMITER ;
