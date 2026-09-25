-- your query
with table1 as(
    select *, dense_rank() over (order by salary desc) as rnk 
    from employee
)
select distinct(salary) as nth_salary from table1 where rnk=3
