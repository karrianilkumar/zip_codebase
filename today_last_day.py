 1. SQL Keywords are NOT Case-Sensitive   
Keywords like:
SELECT
FROM
WHERE
INSERT
UPDATE
DELETE
JOIN 
2. Table Names and Column Names
Without Double Quotes
CREATE TABLE Employee (
    EmpID INT
);
PostgreSQL automatically converts them to lowercase.
Internally:
employee
empid
So these work:
SELECT * FROM employee;
SELECT empid FROM employee;
✅ Works
With Double Quotes
CREATE TABLE "Employee" (
    "EmpID" INT
);
Now PostgreSQL preserves the exact case.
You must use:
SELECT "EmpID"
FROM "Employee";
✅ Works
But:
SELECT empid
FROM employee;
❌ Error
because:
"Employee" ≠ employee
"EmpID" ≠ empid  
3. String Comparison is Case-Sensitive
SELECT 'Anil' = 'anil';
Output:
false
4. ILIKE is Case-Insensitive
LIKE
SELECT *
FROM users
WHERE name LIKE 'anil';
Matches only:
anil
ILIKE
SELECT *
FROM users
WHERE name ILIKE 'anil';
Matches:
anil
Anil
ANIL
aNiL
✅ Case-insensitive search
Case-Insensitive Alternatives
ILIKE
LOWER()
UPPER()
One-Line Interview Answer
PostgreSQL SQL keywords are case-insensitive, but string comparisons and identifiers created with double quotes are case-sensitive. For case-insensitive text searches, we can use ILIKE, LOWER(), or UPPER().
LENGTH()       -- Length of string
UPPER()        -- Uppercase
LOWER()        -- Lowercase
CONCAT()       -- Join strings
TRIM()         -- Remove spaces
REPLACE()      -- Replace text
SUBSTRING()    -- Extract text
SPLIT_PART()   -- Split string
NOW()          -- Current timestamp
CURRENT_DATE   -- Current date
AGE()          -- Age difference
EXTRACT()      -- Get year/month/day
DATE_TRUNC()   -- Round timestamp
TO_CHAR()      -- Format date
TO_DATE()      -- String to date
INTERVAL       -- Add/Subtract time
EXTRACT()
1. String Functions
LENGTH()
Returns the length of a string.
SELECT LENGTH('ANIL');
Output:
4
UPPER()
Converts to uppercase.
SELECT UPPER('anil');
Output:
ANIL
LOWER()
Converts to lowercase.
SELECT LOWER('ANIL');
Output:
anil
INITCAP()
Capitalizes the first letter of each word.
SELECT INITCAP('anil kumar');
Output:
Anil Kumar
CONCAT()
Joins strings.
SELECT CONCAT('Anil',' ','Kumar');
Output:
Anil Kumar
CONCAT_WS()
Concatenates with a separator.
SELECT CONCAT_WS('-', '2026', '06', '02');
Output:
2026-06-02
TRIM()
Removes spaces from both sides.
SELECT TRIM('  Anil  ');
Output:
Anil
LTRIM()
Removes left spaces.
SELECT LTRIM('   Anil');
RTRIM()
Removes right spaces.
SELECT RTRIM('Anil   ');
REPLACE()
Replace text.
SELECT REPLACE('Hello World','World','Anil');
Output:
Hello Anil
SUBSTRING()
Extract part of a string.
SELECT SUBSTRING('Anil Kumar',1,4);
Output:
Anil
POSITION()
Find position of a substring.
SELECT POSITION('Kumar' IN 'Anil Kumar');
Output:
6
SPLIT_PART()
Very commonly used.
SELECT SPLIT_PART('anil@gmail.com','@',1);
Output:
anil
SELECT SPLIT_PART('anil@gmail.com','@',2);
Output:
gmail.com
LEFT()
Get leftmost characters.
SELECT LEFT('Anil Kumar',4);
Output:
Anil
RIGHT()
Get rightmost characters.
SELECT RIGHT('Anil Kumar',5);
Output:
Kumar
Extract year, month, day, hour, etc.  
2. Date & Timestamp Functions
CURRENT_DATE
Current date.
SELECT CURRENT_DATE;
Example:
2026-06-02
CURRENT_TIME
Current time.
SELECT CURRENT_TIME;
CURRENT_TIMESTAMP
Current date and time.
SELECT CURRENT_TIMESTAMP;
NOW()
Most commonly used.
SELECT NOW();
