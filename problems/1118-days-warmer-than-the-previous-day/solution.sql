-- your query
with table1 as(
    select *, lag(temperature,1) over(order by recorded_on asc) as prev_day
    from weather

)

select recorded_on from table1 where temperature>prev_day
