-- your query
with table1 as(
SELECT order_date, customer_id, sum(amount) as total_cost from orders where order_date>= '2024-01-01' and order_date<  '2024-01-31'
group by order_date,customer_id )
select max(total_cost) as m from table1  
