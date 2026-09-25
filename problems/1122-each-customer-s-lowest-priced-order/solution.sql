-- your query
with table1 as(
SELECT order_id, customer_id, amount, row_number() over(partition by customer_id order by amount asc) as rnk
from orders 
)

select order_id, customer_id, amount
from table1 where rnk=1

