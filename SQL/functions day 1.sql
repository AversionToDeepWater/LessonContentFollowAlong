
SELECT LENGTH('CodeFirstGirls'), LENGTH('CodeFirstGirls_12345');

SELECT CONCAT('Code', 'First', 'Girls') AS 'Concatenated Result'; 

SELECT CONCAT("Let's", ' ', 'learn', ' SQL') AS 'Concatenated Result';

SELECT CONCAT('Learn', NULL, 'coding') AS 'Concatenated Result';


SELECT LCASE('CodeFirstGirls'), LOWER('LOWER CASE WORD');


SELECT UCASE('CodeFirstGirls'), UPPER('upper case word');

SELECT LEFT('CodeFirstGirls', 4), LEFT('Database', 3);

SELECT RIGHT('CodeFirstGirls', 5), RIGHT('Database', 4);

SELECT RTRIM('   CodeFirstGirls   '), LENGTH(RTRIM('   CodeFirstGirls   ')), LENGTH(RTRIM('   CodeFirstGirls'));

SELECT LTRIM('   CodeFirstGirls   '), LENGTH(LTRIM('CodeFirstGirls   '));


SELECT TRIM('   CodeFirstGirls   '), LENGTH(TRIM('CodeFirstGirls'));


SELECT 	STRCMP('MyCodeFirstGirls', 'CodeFirstGirls'), 
		STRCMP('CodeFirstGirls', 'MyCodeFirstGirls'), 
		STRCMP('CodeFirstGirls', 'CodeFirstGirls');


SELECT REVERSE('CodeFirstGirls');