import pandas as pd
import sqlite3


conn = sqlite3.connect('data.sqlite')
# products = pd.read_sql("""
# SELECT *
#  FROM products;
# """, conn)

# print(products)


count_each_product_line = pd.read_sql("""
    SELECT productLine, COUNT(*) AS count FROM products
    GROUP BY productLine
    ORDER BY count DESC;
""", conn)

print(count_each_product_line)


avg_price_pl = pd.read_sql("""
    SELECT productLine, AVG(buyPrice) AS avgPrice FROM products
    GROUP BY productLine
    ORDER BY avgPrice DESC
""", conn)

print(avg_price_pl)


min_max_msrp = pd.read_sql("""
    SELECT productLine, MIN(MSRP) AS minMSRP, MAX(MSRP) AS maxMSRP FROM products
    GROUP BY productLine
""", conn)

print(min_max_msrp)


min_max_msrp_more_50 = pd.read_sql("""
    SELECT productLine, MIN(MSRP) AS minMSRP, MAX(MSRP) AS maxMSRP FROM products
    WHERE MSRP >= 50
    GROUP BY productLine
""", conn)

print(min_max_msrp_more_50)


avg_price_pl_more_50 = pd.read_sql("""
    SELECT productLine, AVG(buyPrice) AS avgPrice FROM products
    GROUP BY productLine
    HAVING avgPrice >= 50
    ORDER BY avgPrice DESC
""", conn)

print(avg_price_pl_more_50)


avg_buy_price = pd.read_sql("""
    SELECT productLine, AVG(buyPrice) AS avgPrice, AVG(MSRP) AS avgMSRP
        FROM products
        WHERE MSRP >= 50
        GROUP BY productLine
        HAVING avgPrice >= 50
        ORDER By avgPrice ASC
""", conn)

print(avg_buy_price)

conn.close()