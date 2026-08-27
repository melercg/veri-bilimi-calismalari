# SQL ile Veri Temizleme

**Konu:** Metin fonksiyonları, NULL yönetimi

> Kurs alıştırması #5. Soru metni kursa, çözüm bana ait.

## Dosyalar

- `init_db.py` — tabloları oluşturan kurulum betiği
- `question.py` — **çözüm**

---

## Tablolar

### customers
| Sütun | Tip |
|-------|-----|
| customer_id | SERIAL (PK) |
| full_name | VARCHAR(100) |
| email | VARCHAR(100) — NULL olabilir |
| signup_date | DATE |

### orders
| Sütun | Tip |
|-------|-----|
| order_id | SERIAL (PK) |
| customer_id | INT (FK -> customers) |
| order_date | DATE |
| total_amount | NUMERIC(10,2) |
| status | VARCHAR(20) |

### products
| Sütun | Tip |
|-------|-----|
| product_id | SERIAL (PK) |
| product_name | VARCHAR(100) |
| price | NUMERIC(10,2) |
| category | VARCHAR(50) — NULL olabilir |

---

## Sorular

### Bölüm 1: String Fonksiyonlar ve COALESCE

1. **customers** tablosundaki `NULL` emailleri `'unknown@example.com'` ile değiştir. (`UPDATE` sorgusu — değer döndürmez)

2. Email adresi içinde **'@' işareti geçmeyen** kayıtları bul. (Tüm sütunlar)

3. **customers** tablosundan müşterinin ismini ve isminin **ilk 3 harfini** `short_name` ismiyle getir. (`full_name`, `short_name`)

4. **customers** tablosundan müşterinin ismini ve emailinin **@ işaretinin sağ tarafını** (domain) getir. (`full_name`, `domain`)

5. Tüm müşterilerin **isim ile emaili** birleştirerek `full_info` ismiyle döndür. Format: `'isim - email'` (`full_info`)

6. **orders** tablosundan tüm tutarları **INTEGER'a** çevirip `order_id` ile birlikte döndür. (`order_id`, `total_amount_int`)

7. Müşterilerin ismini ve emaillerindeki **@ işaretinin kaçıncı indekste** olduğunu `at_position` ismiyle döndür. (`full_name`, `at_position`)

8. **products** tablosundan ürün ismini ve kategorisini `product_category` ismiyle döndür. Eğer kategori **NULL** ise `'Unknown'` ile değiştir. (`product_name`, `product_category`)

### Bölüm 2: Window Functions

9. **orders** tablosundan `customer_id`, `total_amount` ve toplam harcamaya göre sıralamayı (`RANK`) `rank_by_spend` ismiyle döndür. (`customer_id`, `total_amount`, `rank_by_spend`)

10. Siparişlere göre **çalışan toplamı** (Running Total — `SUM OVER`) hesapla. (`order_id`, `customer_id`, `total_amount`, `running_total`)

### Bölüm 3: UNION

11. **Electronics** ve **Appliances** kategorisindeki ürünleri tek listede getir. (`product_name`, `category`)

12. Tüm siparişler ve siparişi olmayan müşterileri birleştir. (`customer_id`, `total_amount` — siparişi olmayanlarda `total_amount` NULL)

---
