USE Parts;

-- EXERCISE 1 Use the table 'parts' to return all unique part names. What happens if we want to return all unique parts and their ID names? Why?
SELECT DISTINCT 
p.PNAME
FROM part p;

SELECT DISTINCT  -- here it selects distint based on P_ID therefore you have some duplicates in PNAME column 
p.P_ID, p.PNAME 
FROM part p;
-- After normalising databases, you will not need to use distinct often 

-- EXERCISE 2 Refer to the table 'projects' and return all projects that are in London 
SELECT 
j.J_ID, j.JNAME, j.CITY
FROM project j
WHERE CITY = "London";
