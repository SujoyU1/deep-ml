-- your query
with table1 as(
    select *, row_number() over( partition by department order by score desc, employee asc) as rn,
    rank() over( partition by department order by score desc) as rnk,
    dense_rank() over( partition by department order by score desc) as dense_rnk
    from scores

)
select department, employee, score, rn, rnk, dense_rnk 
from table1
order by department asc, score desc, employee asc
