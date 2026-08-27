
import pandas as pd
import numpy as np
from statistics import mean, median

# Input: [70, 80, 90]
# Output: 80 
def calculate_mean(scores: list) -> float:
    """Öğrencilerin notlarının ortalamasını hesapla."""
    return sum(scores) / len(scores)

#Input: [70, 80, 90, 100] 
# Output: 85.0 
def calculate_median(scores: list) -> float:
    """Öğrencilerin notlarının medyanını hesapla."""
    df= pd.DataFrame({'score':scores})
    return df['score'].median()

#Input: [70, 70, 80, 90] 
# Output: 70
def calculate_mode(scores: list) -> int:
    """En sık görülen notu hesapla (mode)."""
    df=pd.DataFrame({'score': scores})
    return df['score'].mode()[0]

#Input: [10, 20, 30]
#Output: 8.16
def calculate_std(scores: list) -> float:
    """Standart sapmayı hesapla."""
    return round(np.std(scores), 2)   

#Input: [10, 10, 10, 80] ise output median olmalı
#Input: [1,1,1,1] ise output mode
#Input: [10,15,20,25] ise output mean olmalı.
#Hardcoded bir şey olmamalı. Data içeriğine bakarak bu 3 hesaplamadan hangisini yapabileceğine bir kural ile kara vermelisin.
def determine_best_statistic(data: list) -> str:
    """Veri kümesine göre en uygun merkezi eğilim ölçüsünü seç ('mean', 'median' ya da 'mode')."""
    seri = pd.Series(data)
    
    if seri.nunique() == 1:
        return 'mode'
    
    q1 = seri.quantile(0.25)
    q3 = seri.quantile(0.75)
    iqr = q3 - q1
    
    if ((seri < q1 - 1.5*iqr) | (seri > q3 + 1.5*iqr)).any():
        return 'median'
    
    return 'mean'


#Input: ([10, 20, 30, 40, 50], 50) 
#Output: 30
def calculate_percentile(scores: list, percentile: float) -> float:
    """Belirli bir persentil değerini hesapla (örn. 90. persentil)."""
    return np.percentile(scores, percentile)
    

#Input: ([10, 20, 30, 40, 50])
#Output: (20.0, 30.0, 40.0)
def calculate_quartiles(scores: list) -> tuple:
    """Q1, Q2, Q3 çeyrek değerlerini hesapla."""
    q1 = np.percentile(scores, 25)
    q2 = np.percentile(scores, 50)
    q3 = np.percentile(scores, 75)
    return (q1, q2, q3)

#Input: [10, 12, 14, 100]
#Output: [100]
# Bu işlemi yapmak için iqr dediğimiz bir hesaplama kullanmalısın. 
# iqr = q3-q1(q: quartile)
# Daha sonrasonda lower ve upper adında iki tane değişken tanımlamalısın. 
# lower = q1 - 1.5 * iqr, upper = q3 + 1.5 * iqr
# eğer dizideki elemanlar bu lower ve higher değerleri arasındaysa outlier değildirler.
def find_outliers(scores: list) -> list:
    """IQR kullanarak aykırı değerleri tespit et."""
    q1 = np.percentile(scores, 25)
    q3 = np.percentile(scores, 75)
    iqr = q3 - q1
    
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    
    return [x for x in scores if x < lower or x > upper]

#Input: 
    # data = {
    #         'Gryffindor': [80, 85, 90],
    #         'Slytherin': [60, 65, 70]
    # }
#Output: 
    # {
    #   'Gryffindor': 85.0,
    #   'Slytherin': 65.0
    # }
def house_score_summary(house_scores: dict) -> dict:
    """Her bir grup (Gryffindor, Slytherin vb.) için ortalama ve medyan notları döndür."""
    sonuc = {}
    for ev, notlar in house_scores.items():
        sonuc[ev] = {
            'mean': mean(notlar),
            'median': median(notlar)
        }
    return sonuc


#Input:
#  data = {
#         'Gryffindor': [80, 85, 90],
#         'Slytherin': [60, 65, 70]
# }
#Output: 'Gryffindor'
def find_top_house(house_scores: dict) -> str:
    """En yüksek ortalamaya sahip grubu döndür."""
    en_yuksek = 0
    en_iyi_ev = None
    
    for ev, notlar in house_scores.items():
        ortalama = sum(notlar) / len(notlar)
        if ortalama > en_yuksek:
            en_yuksek = ortalama
            en_iyi_ev = ev
    
    return en_iyi_ev