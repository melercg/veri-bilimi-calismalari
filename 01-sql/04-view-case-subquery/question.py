import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'

def connect_db():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password=password
    )

def create_view_completed_orders():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
CREATE OR REPLACE VIEW completed_orders AS (
  SELECT *FROM orders WHERE status='completed'
); 
""")
            conn.commit()

def create_view_electronics_products(): 
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
CREATE OR REPLACE VIEW electronics_products AS(
 SELECT *FROM products p WHERE category='Electronics'
);""")
            conn.commit()

def total_spending_per_customer():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
WITH spending AS (
 SELECT o.customer_id, SUM(p.price*o.quantity) AS total_spending 
 FROM orders o JOIN products p ON o.product_id=p.product_id 
 GROUP BY  o.customer_id
 
)
SELECT c.full_name,s.total_spending
FROM spending s 
JOIN customers c ON c.customer_id=s.customer_id;""")
            return cur.fetchall()

def order_details_with_total():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""WITH order_details AS (
 SELECT o.order_id, c.full_name, p.product_name, SUM(p.price * o.quantity) AS total_price
 FROM orders o 
 JOIN customers c ON c.customer_id= o.customer_id
 JOIN products p ON o.product_id=p.product_id
 GROUP BY  o.order_id, c.full_name, p.product_name
)
SELECT*FROM order_details;""")
            return cur.fetchall()

def get_customer_who_bought_most_expensive_product():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""SELECT c.full_name FROM customers c 
JOIN orders o ON o.customer_id= c.customer_id 
JOIN products p ON p.product_id= o.product_id
WHERE p.price=(
 SELECT MAX(price) FROM products 
)
""")
    
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 2. Sipariş durumlarına göre açıklama
def get_order_status_descriptions():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
SELECT o.order_id, o.status,
 CASE 
  WHEN status= 'completed' THEN 'Tamamlandı'
  WHEN status= 'cancelled' THEN 'İptal Edildi'
  ELSE 'Bilinmiyor'
 END AS status_description
FROM orders o;
                """)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 3. Ortalama fiyatın üstündeki ürünler
def get_products_above_average_price():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
SELECT p.product_name, p.price FROM products p 
WHERE price> (
 SELECT AVG(price) FROM products
);
""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 4. Müşteri kategorileri
def get_customer_categories():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
SELECT c.full_name ,
 CASE 
  WHEN COUNT(o.order_id) >5 THEN 'Sadık Müşteri'
  WHEN COUNT(o.order_id) >=2 THEN 'Orta Seviye'
  ELSE 'Yeni Müşteri'
 END AS customer_cotegory
FROM customers c 
JOIN orders o ON c.customer_id= o.customer_id
GROUP BY c.full_name;""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 5. Son 30 gün içinde sipariş veren müşteriler
def get_recent_customers():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
SELECT c.full_name
FROM customers c
WHERE c.customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
);

""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 6. En çok sipariş verilen ürün
def get_most_ordered_product():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
SELECT p.product_name,SUM(o.quantity) AS total_orders 
FROM products p
JOIN orders o ON p.product_id= o.product_id
GROUP BY p.product_name
ORDER BY total_orders DESC LIMIT 1;
""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 7. Ürün fiyatlarına göre etiketleme
def get_product_price_categories():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
SELECT p.product_name, p.price,
 CASE 
  WHEN price >1000 THEN 'Pahalı'
  WHEN price >=500 THEN 'Orta'
  ELSE 'Ucuz'
 END AS price_category
FROM products p;
""")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result