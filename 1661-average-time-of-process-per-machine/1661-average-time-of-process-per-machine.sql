# Write your MySQL query statement below
SELECT start.machine_id, ROUND(AVG(end.timestamp -start.timestamp),3) AS processing_time 
FROM ACTIVITY start
JOIN ACTIVITY end
ON start.machine_id = end.machine_id and start.process_id = end.process_id 
and start.activity_type = 'start' and end.activity_type = 'end'
GROUP BY start.machine_id
