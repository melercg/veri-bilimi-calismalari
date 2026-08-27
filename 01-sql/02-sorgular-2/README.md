# SQL Sorguları 2

**Konu:** Gruplama ve birleştirme

> Kurs alıştırması #2. Soru metni kursa, çözüm bana ait.

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
| email | VARCHAR(100) |
| age | INT |

### courses
| Sütun | Tip |
|-------|-----|
| course_id | SERIAL (PK) |
| course_name | VARCHAR(100) |
| category | VARCHAR(50) |

### instructors
| Sütun | Tip |
|-------|-----|
| instructor_id | SERIAL (PK) |
| name | VARCHAR(100) |
| expertise | VARCHAR(100) |

### enrollments
| Sütun | Tip |
|-------|-----|
| enrollment_id | SERIAL (PK) |
| student_id | INT (FK -> students) |
| course_id | INT (FK -> courses) |
| enrollment_date | DATE |

### course_instructors
| Sütun | Tip |
|-------|-----|
| id | SERIAL (PK) |
| course_id | INT (FK -> courses) |
| instructor_id | INT (FK -> instructors) |

---

## Sorular

### Bölüm 1: WHERE Sorguları

1. **students** tablosundan yaşı **22'den büyük** öğrencileri listele. (Tüm sütunlar)

2. **courses** tablosundan kategorisi **'Veritabanı'** olan kursları getir. (Tüm sütunlar)

3. **students** tablosundan ismi **'A' harfi ile başlayan** öğrencileri bul. (Tüm sütunlar)

4. **courses** tablosundan kurs ismi içinde **'SQL' geçenleri** listele. (Tüm sütunlar)

5. **students** tablosundan yaşı **22 ile 24 arasında** (dahil) olan öğrencileri getir. (Tüm sütunlar)

### Bölüm 2: JOIN Sorguları

6. Kursa **kayıtlı olan** öğrencilerin isimlerini listele. (`first_name`, `last_name` — tekrar etmeyen, `student_id`'ye göre sıralı)

7. **Veritabanı** kategorisindeki kurslara kayıtlı öğrenci sayısını bul. (`course_name`, `student_count` — `course_id`'ye göre sıralı)

8. Her kursun adını ve bu kursu veren **öğretmenin adını** getir. (`course_name`, `instructor_name` — `course_id`'ye göre sıralı)

9. Hiçbir kursa **kayıtlı olmayan** öğrencileri listele. (Tüm sütunlar)

10. Kurslara göre **ortalama öğrenci yaşı** nedir? (`course_name`, `avg_age` — `course_name`'e göre alfabetik sıralı)

### Bölüm 3: İleri JOIN ve GROUP BY

11. Öğrenci başına toplam kaç kursa kayıtlı olduklarını listele. (`first_name`, `last_name`, `total_courses` — `student_id`'ye göre sıralı)

12. **Birden fazla** kurs veren öğretmenleri listele. (`instructor_name`, `total_courses`)

13. Kurslara göre kaç **farklı** öğrenci kayıtlı? (`course_name`, `unique_students` — `course_name`'e göre alfabetik sıralı)

14. Hem **'SQL Temelleri'** hem de **'İleri SQL'** kursuna kayıtlı öğrencileri bul. (`first_name`, `last_name`)

15. Kurs, öğretmen ve öğrenciyi birleştirerek kayıt tarihlerini listele. (`first_name`, `last_name`, `course_name`, `instructor_name`, `enrollment_date` — `enrollment_id`'ye göre sıralı)

---
