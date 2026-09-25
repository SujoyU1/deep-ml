-- your query
with table1 as(
SELECT *, lag(num,1) over(order by id) as prev1,
lag(num,2) over(order by id) as prev2
from logs)
select distinct num from table1
where num=prev1 and num=prev2
order by num asc
