import random
from typing import List
import numpy as np
from scipy.stats import binom, poisson

# Açıklama:
# Bir Witcher'ın karşılaştığı canavarı öldürme şansı probability ile verilir.
# Bu olay bir Bernoulli deneyidir. Fonksiyon True (öldürdü) ya da False (ölmedi) döndürmelidir.
# Input: probability=0.7
# Output: True veya False
def is_monster_killed(probability: float) -> bool:
    pass


# Açıklama:
# Witcher 100 kez ava çıktıysa ve her avda canavarı öldürme şansı p ise,
# kaç canavar öldürüldüğünü Binom dağılımı ile simüle edin.
# Input: n=100, p=0.65
# Output: 68 (örnek)
def simulate_monster_hunts(n: int, p: float) -> int:
    pass


# Açıklama:
# Zehirli Ghoul'lar bir saat içinde ortalama lmbda kez saldırır.
# time saatlik süre için Poisson dağılımı ile toplam saldırı sayısını üretin.
# Input: lmbda=2.5, time=4
# Output: 10 (örnek)
def expected_poison_attacks(lmbda: float, time: int) -> int:
    pass


# Açıklama:
# Bir Witcher'ın 10 avdan k tanesini öldürme olasılığını Binom formülüyle hesaplayın.
# Input: k=7, n=10, p=0.6
# Output: 0.215 (örnek)
def probability_k_monsters_killed(k: int, n: int, p: float) -> float:
    pass


# Açıklama:
# Bir Ghoul’un k defa saldırma ihtimali lmbda ortalamasıyla nedir?
# Poisson olasılığı hesaplanmalı.
# Input: k=3, lmbda=2.5
# Output: 0.213 (örnek)
def poisson_probability(k: int, lmbda: float) -> float:
    pass


# Açıklama:
# Witcher’ın 1000 denemede ortalama öldürme oranını simüle et.
# Input: trials=1000, p=0.5
# Output: 0.501 (örnek)
def average_kill_rate(trials: int, p: float) -> float:
    pass


# Açıklama:
# İki Witcher’ın canavar öldürme olasılıkları farklıysa, 1000 denemede kim daha başarılı?
# Input: p1=0.6, p2=0.7, trials=1000
# Output: 'Witcher 2'
def compare_two_witchers(p1: float, p2: float, trials: int) -> str:
    pass


# Açıklama:
# Ghoul’lar gün boyu saldırıyor. Her saat için saldırı sayısını liste olarak döndürün.
# Input: hours=24, lmbda=3.0
# Output: [2, 3, 1, 5, ...]
def simulate_poison_attacks_day(hours: int, lmbda: float) -> List[int]:
    pass