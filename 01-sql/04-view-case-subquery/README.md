# View, CASE ve Alt Sorgu

**Konu:** VIEW, CASE WHEN, subquery

> Kurs alıştırması #4. Soru metni kursa, çözüm bana ait.

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
| email | VARCHAR(100) |
| signup_date | DATE |

### products
| Sütun | Tip |
|-------|-----|
| product_id | SERIAL (PK) |
| product_name | VARCHAR(100) |
| price | NUMERIC(10,2) |
| category | VARCHAR(50) |

### orders
| Sütun | Tip |
|-------|-----|
| order_id | SERIAL (PK) |
| customer_id | INT (FK -> customers) |
| product_id | INT (FK -> products) |
| order_date | DATE |
| quantity | INT |
| status | VARCHAR(20) |

---

## Sorular

### Bölüm 1: VIEW

1. **Completed** (tamamlanmış) siparişlerin listesini gösteren bir VIEW oluştur. (`CREATE OR REPLACE VIEW completed_orders AS ...`)

2. **Electronics** kategorisindeki ürünleri gösteren bir VIEW oluştur. (`CREATE OR REPLACE VIEW electronics_products AS ...`)

### Bölüm 2: WITH (CTE)

3. Her müşterinin toplam harcamasını **WITH** kullanarak hesapla. (`full_name`, `total_spending` — harcamayı `price * quantity` ile hesapla)

4. Sipariş ve ürün detaylarını birleştirerek toplam tutarı (`price * quantity`) **WITH** kullanarak hesapla. (`order_id`, `full_name`, `product_name`, `total_price`)

### Bölüm 3: CASE ve Subquery

5. En pahalı ürünü almış kişinin **full_name** değerini döndür. (Tek sütun)

6. Sipariş durumunu Türkçeleştir: `'completed'` → `'Tamamlandı'`, `'cancelled'` → `'İptal Edildi'`. (`order_id`, `status`, `status_description`)

7. **Ortalama fiyatın üzerindeki** ürünleri bul. (`product_name`, `price`)

8. Alışveriş sayısına göre müşteri kategorisi belirle: **>5** sipariş → `'Sadık Müşteri'`, **2–5** sipariş → `'Orta Seviye'`, diğer → `'Yeni Müşteri'`. (`full_name`, `customer_category`)

9. En son sipariş tarihi **son 30 gün içinde** olan müşterilerin isimlerini getir. (`full_name`)

10. En çok sipariş verilen ürünü bul. (`product_name`, `total_orders`)

### Bölüm 4: Fiyat Etiketleme

11. Ürün fiyatlarına göre etiketle: **>1000** → `'Pahalı'`, **500–1000** → `'Orta'`, diğer → `'Ucuz'`. (`product_name`, `price`, `price_category`)

---
