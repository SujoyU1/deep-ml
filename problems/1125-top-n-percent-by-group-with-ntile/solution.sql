-- your query
with table1 as(
SELECT *, dense_rank() over(partition by region order by amount desc) as rnk
from sales)
select region, amount from table1 where rnk=1 

