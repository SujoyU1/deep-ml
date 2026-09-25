-- your query
with table1 as(
SELECT user_id,login_date,
lag(login_date)over(partition by user_id order by login_date) as lag_date
from logins),
table2 as (
select distinct user_id from table1 where login_date-lag_date=1)
select table1.user_id, min(table1.login_date) as first_login
from table1 inner join table2 on table1.user_id=table2.user_id group by table1.user_id 


