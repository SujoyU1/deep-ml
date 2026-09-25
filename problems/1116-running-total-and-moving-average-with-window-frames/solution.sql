-- your query
SELECT 
day,amount,sum(amount) over(order by day asc) as running_total, 
avg(amount) over(order by day asc ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg
from sales 
order by day asc