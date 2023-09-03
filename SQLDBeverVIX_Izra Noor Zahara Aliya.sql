SELECT
    marital_status,
    AVG(age) AS rata_rata_umur
FROM
    customer
GROUP BY
    marital_status;

   
 SELECT
    gender,
    AVG(age) AS rata_rata_umur
FROM
    customer
GROUP BY
    gender;
   
SELECT
    store.storename,
    SUM(transaction.qty) AS total_quantity
FROM
    store
JOIN
    transaction
ON
    store.storeid = transaction.storeid
GROUP BY
    store.storename
ORDER BY
    total_quantity desc
limit 1

SELECT
    p.productname,
    SUM(t.totalamount) AS total_amount
FROM
    produck p 
JOIN
    transaction t
ON
    p.productid  = t.productid 
GROUP BY
    p.productname 
ORDER BY
    total_amount desc
limit 1



  