-- create a new view
CREATE OR REPLACE VIEW vw_staff_common AS
    SELECT 
        employeeID,
        firstName,
        lastName,
        jobtitle,
        managerID,
        department
        -- we don't want anyone except from HR to see people's salaries or dob, so the view would hid ethe info
    FROM
        staff
    WHERE
        jobtitle LIKE '%DB%';
   
-- vw_staff_common is a simple view, so it is possible to update it

-- Let's insert a row into the staff table through the vw_staff_common view.
INSERT INTO vw_staff_common (
    employeeID,
    firstName,
    lastName,
    jobtitle,
    managerID,
    department
) 
VALUES(
    8888,
    'Mike',
    'Davies',
    'Developer',
    2323,
    'Database Administrators'
);

-- NBthat the newly created employee is not visible through the vw_staff_common view 
-- because employee's job title is Developer, which is not like the %DB% pattern. Y

select * from vw_staff_common; -- cannot see the new person

select * from staff;  --  can see the new person