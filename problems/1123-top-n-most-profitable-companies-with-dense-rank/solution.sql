-- your query
with table1 as(
    select company,sum(profit) as total_profit
    from sales
    group by company
),
table2 as(
    select company,total_profit,
    dense_rank()over(order by total_profit desc) as rnk
    from table1
)

select company, total_profit as profit from table2
where rnk<4

