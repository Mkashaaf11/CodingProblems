# Write your MySQL query statement below
SELECT a.customer_id, COUNT(*) as count_no_trans FROM Visits a
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions )
GROUP BY customer_id;
