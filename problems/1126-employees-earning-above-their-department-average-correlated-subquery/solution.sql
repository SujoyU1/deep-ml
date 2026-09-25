-- your query
with table1 as(
    select *, avg(salary) over(partition by department)  as dept_avg
    from employees
)
select id,name,department, salary from table1  where salary>dept_avg 