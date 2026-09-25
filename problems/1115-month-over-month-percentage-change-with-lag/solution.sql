-- your query
with table1 as(
SELECT DATE_TRUNC('month', sale_date) as month1, sum(amount) as total
from sales group by DATE_TRUNC('month', sale_date) order by month1
)
select month1, total, 100.0*(total-lag(total) over (order by month1))/lag(total) over (order by month1) as pct_change from table1 order by month1

