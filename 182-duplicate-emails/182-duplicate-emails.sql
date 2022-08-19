# Write your MySQL query statement below
SELECT email as Email from Person
GROUP BY Email
HAVING count(Email) > 1;
