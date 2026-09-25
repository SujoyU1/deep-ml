-- your query
with table1 as(
    select a.name, a.salary as employee_salary,b.salary as manager_salary
    from employees a left join employees b on a.manager_id=b.id
)

select name  as employee from table1 where employee_salary>manager_salary
