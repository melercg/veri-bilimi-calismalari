# Veri Bilimi Çalışmaları

Nisan–Temmuz 2026 arasında aldığım veri bilimi kursunda çözdüğüm **16 alıştırma** —
SQL'den istatistiğe, konu konu.

> Alıştırma soruları kursa aittir, **çözümler bana ait.**
> Her klasörde sorunun kendisi ve benim çözümüm birlikte duruyor.

---

## Konu haritası

| Klasör | Konu | Alıştırma | Çözüm |
|---|---|---|---|
| `01-sql/` | SELECT, JOIN, VIEW, CASE, alt sorgu, veri temizleme | 5 | 700 satır |
| `02-python-temelleri/` | Değişken, koşul, döngü, fonksiyon | 2 | 135 satır |
| `03-numpy/` | Vektör/matris işlemleri, string işleme, API | 2 | 239 satır |
| `04-pandas/` | Series, DataFrame, `apply`, filtreleme | 2 | 134 satır |
| `05-gorsellestirme/` | Grafik türleri ve kullanımı | 1 | 170 satır |
| `06-istatistik/` | Betimsel istatistik, aykırı değer, olasılık dağılımları | 4 | 424 satır |
| | **Toplam** | **16** | **1.802 satır** |

---

## Sıra neden böyle

İlerleme, veriyle çalışmanın doğal sırasını takip ediyor:

**Veriye eriş** (SQL) → **veriyi işle** (Python) → **araçları öğren** (NumPy, Pandas)
→ **göster** (görselleştirme) → **yorumla** (istatistik).

Önce SQL geliyor çünkü veri çoğu zaman bir veritabanında duruyor; ona ulaşamadan
analiz edecek bir şey yok. En sona istatistik kalıyor çünkü bir sayının ne anlama
geldiğini sormadan önce o sayıyı üretebilmek gerekiyor.

---

## Öne çıkan teknikler

Çözümlerde fiilen kullanılanlar:

**SQL (5 alıştırma)**
- `JOIN` ile çok tablolu sorgular — 4 alıştırmada
- `CASE WHEN` ile koşullu sütun üretimi — 4 alıştırmada
- `GROUP BY` ile toplulaştırma — 3 alıştırmada
- `VIEW` ve alt sorgu (subquery) ile karmaşık sorguyu parçalara bölmek
- `psycopg2` ile Python'dan veritabanına bağlanma — 10 dosyada

**Python & NumPy**
- `collections.defaultdict` ve `deque` ile veri yapısı seçimi
- `np.array` ile vektör/matris işlemleri
- `requests` ile API'den veri çekme
- `typing.List` ile tip ipuçları

**Pandas**
- `apply` ile satır bazlı dönüşüm — döngü yazmadan tüm sütunu çevirmek
- `nlargest` ile sıralama + kesme tek adımda — 2 alıştırmada
- `lambda` ile tek satırlık dönüşümler
- Boolean maskeleme ile filtreleme

**İstatistik**
- `quantile` ve `std` ile aykırı değer tespiti (IQR ve z-skoru)
- `scipy.stats` ile binom ve Poisson dağılımları
- `statistics.mean` / `median` ile merkezi eğilim
- `matplotlib` ile dağılım görselleştirme

---

## Çalıştırma

Alıştırmalar birbirinden bağımsız, ortak bir kurulum yok.

**SQL alıştırmaları (`01-sql/`)** — PostgreSQL gerekir:

```bash
python init_db.py     # tabloları oluşturur
python question.py    # çözümleri çalıştırır
```

> Veritabanı şifresi dosyalarda `postgres` placeholder'ı olarak duruyor,
> kendi kurulumuna göre değiştir.

**Diğerleri** — `pandas`, `numpy`, `matplotlib`, `scipy` kurulu bir ortam yeterli:

```bash
python task_manager.py
```

---

## Not

Bu alıştırmalar başlangıçta 16 ayrı repoda duruyordu; okunabilirlik için tek repoda
konu konu toplandı. Kursun test altyapısı (`watch.py`, `tests/`, CI dosyaları)
dahil edilmedi — burada olan şey **soru ve çözüm**.
