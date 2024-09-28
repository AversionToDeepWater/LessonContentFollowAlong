
SELECT RAND() AS RandomValue;

SELECT LEFT(CEILING(RAND()*888),1) AS RandomValue;

SELECT ABS(5), ABS(-5);

SELECT CEILING(12.34), CEILING(-12.34);

SELECT DEGREES(PI()), DEGREES(PI() / 2);

SELECT FLOOR(12.34), FLOOR(-12.34);

SELECT PI();

SELECT POW(3,2);
SELECT POWER(8,-1);

SELECT SQRT(4);
SELECT SQRT(16);
SELECT SQRT(256);

-- Table Column Fun Example
SELECT 	price, 
		ROUND(price) AS Price,
		price-0.10, 
        cast(price-0.10 AS DECIMAL(3,2)), 
        ROUND(price-0.10, 2) R_Price 
FROM bakery.sweet;