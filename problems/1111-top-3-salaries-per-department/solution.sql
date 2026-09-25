-- your query
with table1 as(
    select *,
    dense_rank () over(partition by department order by salary desc) as rnk
    from employees 
)
SELECT department, name,salary, rnk from table1 where rnk<4
order by department ASC, salary DESC, name ASC
  

