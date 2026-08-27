# SQL Sorguları 3

**Konu:** İleri sorgular

> Kurs alıştırması #3. Soru metni kursa, çözüm bana ait.

## Dosyalar

- `init_db.py` — tabloları oluşturan kurulum betiği
- `question.py` — **çözüm**

---

## Tablolar

### students
| Sütun | Tip |
|-------|-----|
| student_id | SERIAL (PK) |
| first_name | VARCHAR(50) |
| last_name | VARCHAR(50) |
| age | INT |
| city | VARCHAR(50) |

### courses
| Sütun | Tip |
|-------|-----|
| course_id | SERIAL (PK) |
| course_name | VARCHAR(100) |
| category | VARCHAR(50) |

### enrollments
| Sütun | Tip |
|-------|-----|
| enrollment_id | SERIAL (PK) |
| student_id | INT (FK -> students) |
| course_id | INT (FK -> courses) |
| enrollment_date | DATE |

---

## Sorular

### Bölüm 1: Tarih Fonksiyonları

1. `DATE_TRUNC` ile ay bazlı kayıt sayılarını listele. (`month`, `count` — aya göre sıralı)

2. `DATE_PART` ile kayıtların sadece **yıl bilgisini** al. (Tek sütun: `year`)

### Bölüm 2: Aggregate Fonksiyonlar

3. Tüm öğrencilerin yaşlarının **toplamını** döndür. (Tek değer: `SUM`)

4. Toplam **kurs sayısını** bul. (`SELECT COUNT(course_id) ...` — tek satır döner)

5. Yaşı **ortalama yaştan büyük** olan öğrencileri getir. (Tüm sütunlar, `student_id`'ye göre sıralı)

6. Her kursun **en eski kayıt tarihini** bul. (`course_id`, `first_enrollment` — `course_id`'ye göre sıralı)

### Bölüm 3: GROUP BY + JOIN

7. Her kurs için öğrencilerin **ortalama yaşlarını** bul. (`course_name`, `avg_age` — `course_id`'ye göre sıralı)

8. **En genç** öğrencinin yaşını getir. (Tek değer: `MIN`)

9. Her derse kayıt olmuş **öğrenci sayısını** bul. (`course_name`, `student_count` — `course_id`'ye göre sıralı)

10. Kayıt olunmuş derslerin sadece **isimlerini** getir. (Tek sütun: `course_name` — `course_name`'e göre sıralı, tekrarsız)

---
