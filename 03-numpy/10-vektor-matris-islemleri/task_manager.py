import numpy as np

#Input: num_students: int, num_subjects: int
#Output: np.ndarray (boyut: [num_students, num_subjects], 0-100 arası integer değerler)
#Açıklama:
#Öğrencilerin ders puanlarını temsil eden rastgele sayılardan oluşan bir Numpy matrisi oluştur. Bu matris tüm analizlerin temelini oluşturacak.
def create_student_score_matrix(num_students: int, num_subjects: int) -> np.ndarray:
    """
    INPUT: Öğrenci sayısı (int), ders sayısı (int)
    OUTPUT: 0-100 arası random puanlardan oluşan bir numpy array (shape: [num_students, num_subjects])
    """
    return np.random.randint(1,101,size=[num_students, num_subjects])

#Input: scores: np.ndarray
#Output: 1D Numpy dizisi (her dersin ortalama puanı)
#Açıklama:
#Verilen puan matrisinde, her bir ders için tüm öğrencilerin not ortalamasını hesapla.
def calculate_mean_per_subject(scores: np.ndarray) -> np.ndarray:
    """
    INPUT: [öğrenci, ders] formatında puan matrisini alır
    OUTPUT: Her ders için ortalama puan (1D array)
    """
    return np.mean(scores, axis=0)

#Input: scores: np.ndarray
#Output: 1D Numpy dizisi (her öğrencinin not varyansı)
#Açıklama:
#Her öğrencinin notlarının ne kadar değişken olduğunu anlamak için varyans değerlerini hesapla. Varyans, öğrencinin farklı derslerde ne kadar tutarlı olduğunu gösterir.
def calculate_student_variance(scores: np.ndarray) -> np.ndarray:
    """
    INPUT: Puan matrisi
    OUTPUT: Her öğrenci için varyans (1D array)
    """
    return np.var(scores, axis=1)

#Input: scores: np.ndarray
#Output: np.ndarray (puanı %10 artırılmış, 100'ü geçmeyen yeni matris)
#Açıklama:
#Profesör Dumbledore tüm puanlara %10 büyü bonusu verilmesini istedi. Ancak puanlar 100’ü geçemez. Puanları artır ve gerektiğinde 100 ile sınırla.
def apply_magic_curve(scores: np.ndarray) -> np.ndarray:
    """
    INPUT: Puan matrisi
    OUTPUT: Tüm puanları %10 artır (max 100 olacak şekilde clip'le)
    """
    return np.clip(scores*1.1,0,100)


#Input: scores: np.ndarray, threshold: float
#Output: np.ndarray (threshold üzerindeki ortalamaya sahip öğrencilerin index listesi)
#Açıklama:
#Sınıftaki başarılı öğrencileri bul. Ortalama puanı threshold değerinin üstünde olan öğrencilerin sırasını döndür.
def get_top_students(scores: np.ndarray, threshold: float) -> np.ndarray:
    """
    INPUT: Puan matrisi, eşik değeri
    OUTPUT: Ortalama puanı threshold üzerinde olan öğrencilerin index listesi
    """
    return np.where(np.mean(scores,axis=1) > threshold)[0]

#Input: scores: np.ndarray
#Output: 1D Numpy dizisi (her ders için en yüksek puan)
#Açıklama:
#Hangi öğrenci hangi derste parlamış? scores matrisi için en yüksek alınan puanı belirle.
def subject_wise_max_scores(scores: np.ndarray) -> np.ndarray:
    """
    INPUT: Puan matrisi
    OUTPUT: Her ders için alınan en yüksek puan (1D array)
    """
    return np.max(scores,axis=0)

#Input: scores: np.ndarray, start: int, end: int
#Output: np.ndarray (seçilen aralıktaki öğrencilerin puanları)
#Açıklama:
#Verilen başlangıç ve bitiş indexlerine göre öğrenci puanlarını dilimle. Belirli bir grup öğrenciye odaklanmak için kullanılır.
def slice_students_by_index(scores: np.ndarray, start: int, end: int) -> np.ndarray:
    """
    INPUT: Puan matrisi, başlangıç ve bitiş indexi
    OUTPUT: Verilen index aralığındaki öğrencilerin puanları
    """
    return scores[start:end]

#Input: scores: np.ndarray
#Output: 1D Numpy dizisi (her dersin standart sapması)
#Açıklama:
#scores dizisinin ne kadar dağıldığını görmek için standart sapma hesapla. Sapma, öğretim kalitesine dair ipuçları verebilir.
def calculate_subject_std(scores: np.ndarray) -> np.ndarray:
    """
    INPUT: Puan matrisi
    OUTPUT: Her ders için standart sapma
    """
    return np.std(scores, axis=0)

#Input: scores: np.ndarray
#Output: np.ndarray (0 ile 1 arası normalize edilmiş matris)
#Açıklama:
#Tüm puanları 0 ile 1 arasına ölçekle. Böylece büyü gücü açısından karşılaştırmalı analizler yapılabilir.
def normalize_scores(scores: np.ndarray) -> np.ndarray:
    """
    INPUT: Puan matrisi
    OUTPUT: Tüm puanları 0-1 arasında normalize et
    """
    return (scores-np.min(scores,axis=0)) /(np.max(scores,axis=0)-np.min(scores,axis=0))
