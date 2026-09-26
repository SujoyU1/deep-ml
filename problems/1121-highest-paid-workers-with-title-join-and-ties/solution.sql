-- your query
with table1 as(
    select a.*, b.title, dense_rank() over(order by a.salary desc) as rnk
    from workers a left join titles b on a.title_id=b.title_id
)
SELECT name, salary, title from table1 where rnk=1 order by name 

