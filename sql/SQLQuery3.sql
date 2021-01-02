use Bikestores;

select count(*) from production.products

select * from production.products;
select distinct (product_name) from production.products;

SELECT  product_name, sum(list_price) as 'total list price' from production.products
group by product_name
having sum(list_price)>4000

#WAP to find the the product name 'women' and list_price total
SELECT  product_name, sum(list_price) as 'total list price' from production.products
where product_name like'%women%'
group by product_name
having sum(list_price)>4000
order by sum(list_price) desc
# group by is mandatory for having because we can use having after grouping it
# WHERE-->GROUP BY-->HAVING-->ORDER BY

#join sql

USE Bikestores

SELECT * FROM production.categories
SELECT * FROM production.products

#INNER JOIN as table area
SELECT ap.product_id, ap.product_name,aq.category_name, ap.category_id ,ap.list_price
FROM production.products as ap
INNER JOIN production.categories as aq
ON ap.category_id = aq.category_id

#LEFT JOIN AS TABLE AREA
SELECT ap.product_id, ap.product_name,aq.category_name, ap.category_id ,ap.list_price
FROM production.products as ap
LEFT JOIN production.categories as aq
ON ap.category_id = aq.category_id

#RIGHT JOIN AS TABLE AREA
SELECT ap.product_id, ap.product_name,aq.category_name, ap.category_id ,ap.list_price
FROM production.products as ap
RIGHT JOIN production.categories as aq
ON ap.category_id = aq.category_id

SELECT ap.product_id, ap.product_name,aq.category_name, ap.category_id ,ap.list_price
FROM production.products as ap
FULL JOIN production.categories as aq
ON ap.category_id = aq.category_id

SELECT ap.product_id, ap.product_name,aq.category_name, ap.category_id ,ap.list_price
FROM production.products as ap
FULL JOIN production.categories as aq
ON ap.category_id = aq.category_id

# CROSS JOIN + WHERE =INNER JOIN 
SELECT ap.product_id, ap.product_name,aq.category_name, ap.category_id ,ap.list_price
FROM production.products as ap
CROSS JOIN production.categories as aq
WHERE ap.category_id = aq.category_id

/* In Union all duplicate members are added and it is not equal to Full JOIN */

#it can be used ehen the query should be give same no of columns,sequence and types of data

