# Temel SQL Sorguları

**Konu:** SELECT, WHERE, ORDER BY, JOIN

> Kurs alıştırması #1. Soru metni kursa, çözüm bana ait.

## Dosyalar

- `init_db.py` — tabloları oluşturan kurulum betiği
- `questions.py` — **çözüm**

---

## Tablolar

### customers
| Sütun | Tip |
|-------|-----|
| customer_id | SERIAL (PK) |
| customer_name | VARCHAR(100) |
| email | VARCHAR(100) |
| country | VARCHAR(50) |
| signup_date | DATE |

### products
| Sütun | Tip |
|-------|-----|
| product_id | SERIAL (PK) |
| product_name | VARCHAR(100) |
| price | NUMERIC(8,2) |
| stock_quantity | INTEGER |

### orders
| Sütun | Tip |
|-------|-----|
| order_id | SERIAL (PK) |
| customer_id | INTEGER (FK -> customers) |
| order_date | DATE |
| total_amount | NUMERIC(10,2) |

---

## Sorular

1. **customers** tablosundan tüm müşterilerin **adlarını ve ülkelerini** getir.

2. **orders** tablosundaki en yüksek tutarlı **5 siparişi**, tüm sütunlarıyla birlikte listele. (`total_amount`'a göre azalan sırada)

3. **products** tablosundan fiyatı en düşük **3 ürünü**, sadece **adları ve fiyatları** ile getir.

4. **customers** tablosundaki tüm müşterileri `signup_date`'e göre **eskiden yeniye** sırala. (Tüm sütunlar, LIMIT 10)

5. **products** tablosunda en fazla stoğa sahip ürünü, sadece **adı ve stock_quantity** ile getir. (1 kayıt)

6. **orders** tablosundaki **son siparişi** (tarihi en güncel olan) tüm sütunlarıyla listele. (1 kayıt)

7. **products** tablosundan sadece `product_name` sütununu **alfabetik sırada** getir.

8. **customers** tablosundan `customer_id`'ye göre sıralanmış ilk **5 müşteriyi**, sadece `customer_id` ve `email` sütunlarıyla getir.

9. **orders** tablosundaki tutarı en düşük **3 siparişi**, sadece `order_id` ve `total_amount` ile getir. (`total_amount`'a göre artan sırada)

10. **customers** tablosundan sadece **Türkiye'deki** (`country = 'Turkey'`) müşterileri `customer_name`'e göre **alfabetik** sırala. (Tüm sütunlar)

---
