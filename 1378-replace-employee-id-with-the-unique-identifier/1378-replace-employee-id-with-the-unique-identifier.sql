# Write your MySQL query statement below
SELECT B.unique_id,A.name from Employees as A 
LEFT JOIN EmployeeUNI as B on A.id=B.id;