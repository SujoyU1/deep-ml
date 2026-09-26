-- your query
select 
sum (case when department='Engineering' then salary else 0 end) as engineering_total,
sum (case when department='Sales' then salary else 0 end) as sales_total,
sum (case when department='Engineering' then salary else 0 end)-sum (case when department='Sales' then salary else 0 end) as salary_difference from employees
