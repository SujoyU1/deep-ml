WITH table1 AS (
    SELECT
        user_id,
        login_date,
        LAG(login_date) OVER (
            PARTITION BY user_id
            ORDER BY login_date
        ) AS lag_date
    FROM logins
),

table2 AS (
    SELECT DISTINCT user_id
    FROM table1
    WHERE login_date - lag_date = 1
)

SELECT
    table1.user_id,
    MIN(table1.login_date) AS first_login
FROM table1
INNER JOIN table2
    ON table1.user_id = table2.user_id
GROUP BY table1.user_id
ORDER BY table1.user_id ASC;