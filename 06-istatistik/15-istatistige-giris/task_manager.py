import random
from collections import defaultdict, deque

"""
Açıklama: Verilen data listesinden basit rastgele örnekleme ile sample_size kadar örnek seçer.

Input:
data: Elemanları herhangi bir tipte (örnek: karakter isimleri, sayılar vb.) liste
sample_size: örneklem büyüklüğü (int)

Örnek Input:
    data = list(range(100))
    sample_size = 10
Output: Seçilen örneklem listesi.
"""
def simple_random_sampling(data: list, sample_size: int) -> list:
   return random.sample(data, sample_size)


"""
Açıklama: data listesinden, ilk elemanı rastgele seçip, ardından her step adımda bir eleman seçerek sistematik örnekleme yapar.
Input:
data: liste
step: adım sayısı (int)
Örnek Input:
    data = list(range(100))
    step = 3
Output: Seçilen örneklem listesi.
"""
def systematic_sampling(data: list, step: int) -> list:
    start = random.randint(0, step - 1)
    return data[start::step]


"""
Açıklama: data listesini strata_key fonksiyonuna göre katmanlara ayırır ve her katmandan sample_size_per_stratum kadar örnek rastgele seçer.
Input:
    data: liste
    strata_key: her elemana uygulanacak, katman bilgisini döndüren fonksiyon (ör: karakterin mesleği)
    sample_size_per_stratum: her katmandan örnek büyüklüğü (int)
Örnek Input:
    data = [{'name': 'Walt', 'role': 'chemist'},
                {'name': 'Jesse', 'role': 'assistant'},
                {'name': 'Gus', 'role': 'boss'},
                {'name': 'Mike', 'role': 'boss'}]
    strata_key = filter gibi bir fonksiyon olabilir.
    sample_size_per_stratum = 2
Output: Örneklem listesi.
"""
def stratified_sampling(data: list, strata_key: callable, sample_size_per_stratum: int) -> list:
    katmanlar = {}
    for item in data:
        key = strata_key(item)
        if key not in katmanlar:
            katmanlar[key] = []
        katmanlar[key].append(item)
    
    sonuc = []
    for grup in katmanlar.values():
        boyut = min(sample_size_per_stratum, len(grup))
        sonuc.extend(random.sample(grup, boyut))
    
    return sonuc


"""
Açıklama: clusters sözlüğünden belirtilen cluster_ids kümelerindeki tüm elemanları seçerek örneklem oluşturur.
Input:
    clusters: anahtar küme id’si (str veya int), değer kümedeki elemanların listesi
    cluster_ids: seçilecek kümelerin listesi
Örnek Input:
     clusters = {
        'cluster1': [1,2,3],
        'cluster2': [4,5],
        'cluster3': [6,7,8]
    }
    cluster_ids = ['cluster1', 'cluster3']
Output: Seçilen tüm elemanları içeren liste.
"""
def cluster_sampling(clusters: dict, cluster_ids: list) -> list:
    sonuc = []
    for id in cluster_ids:
        sonuc.extend(clusters[id])
    return sonuc

"""
Açıklama: data listesinden, kolay erişilebilir ilk max_samples elemanı seçer.
Input:
    data: liste
    max_samples: maksimum örneklem sayısı
Örnek Input:
    data = list(range(50))
    max_samples = 10
Output: Örneklem listesi.
"""
def convenience_sampling(data: list, max_samples: int) -> list:
    return data[:max_samples]


"""
Açıklama: judge_func fonksiyonuna göre data listesindeki elemanları seçer. Bu fonksiyon True dönen elemanlar seçilir.
Input:
    data: liste
    judge_func: elemana uygulanan ve bool döndüren fonksiyon

Output: Seçilen elemanların listesi.
"""
def judgmental_sampling(data: list, judge_func: callable) -> list:
   sonuc = []
   for item in data:
    if judge_func(item):    
        sonuc.append(item)  
   return sonuc


"""
Açıklama: data listesini strata_key ile katmanlara ayırır, ve her katmandan quotas sözlüğünde belirtilen adet kadar örnek seçer (ilk gelenlerden).

Input:
    data: liste
    strata_key: katman belirleyici fonksiyon
    quotas: anahtar katman ismi, değer o katmandan seçilecek örnek sayısı (int)
Örnek Input:
    data = [{'name': 'Walt', 'role': 'chemist'},
            {'name': 'Jesse', 'role': 'assistant'},
            {'name': 'Gus', 'role': 'boss'},
            {'name': 'Mike', 'role': 'boss'}]
    quotas = {'chemist': 1, 'assistant': 1, 'boss': 1}
Output: Örneklem listesi.
"""
def quota_sampling(data: list, strata_key: callable, quotas: dict) -> list:
    sayilar = {}             
    sonuc = []
    
    for item in data:
        grup = strata_key(item)
        
        if grup not in sayilar:
            sayilar[grup] = 0
        
        if grup in quotas and sayilar[grup] < quotas[grup]:
            sonuc.append(item)
            sayilar[grup] = sayilar[grup] + 1
    
    return sonuc


"""
Açıklama: seed_ids listesinden başlanarak, her elemanın get_neighbors fonksiyonu ile bulunan bağlılarını da örnekleme dahil ederek snowball sampling yapar. Toplam max_samples eleman seçer.

Input:
    data: liste (örneklem havuzu)
    seed_ids: başlanacak örneklerin id listesi
    get_neighbors: bir elemanın bağlantılı olduğu elemanları döndüren fonksiyon
    max_samples: maksimum örneklem sayısı

Output: Seçilen örneklem listesi.

"""
def snowball_sampling(data: list, seed_ids: list, get_neighbors: callable, max_samples: int) -> list:
    sonuc = list(seed_ids)        
    ziyaret_edildi = set(seed_ids)
    bekleyen = list(seed_ids)
    
    while bekleyen and len(sonuc) < max_samples:
        kisi = bekleyen.pop(0)
        komsular = get_neighbors(kisi)
        
        for komsu in komsular:
            if komsu not in ziyaret_edildi and len(sonuc) < max_samples:
                sonuc.append(komsu)
                ziyaret_edildi.add(komsu)
                bekleyen.append(komsu)
    
    return sonuc