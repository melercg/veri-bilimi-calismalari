import matplotlib.pyplot as plt
import numpy as np

"""
Açıklama: Witcher karakterlerinin farklı yıllardaki can puanlarını içeren data sözlüğünü kullanarak bir line chart (çizgi grafiği) çizer.
Input: Anahtar: yıl (int), Değer: can puanı (int) şeklinde bir sözlük. Örnek: {2010: 80, 2011: 85, 2012: 78}
Output: Hiçbir şey döndürmez. Grafiği matplotlib ile çizip gösterir.
Ek İstek: Grafiğe başlık, x ve y eksen label’ları ekle.
Başlık: Witcher Characters' HP Over Years
x label: Year
Y label: HP
"""
def plot_line_chart(data: dict) -> None:
    plt.plot(data.keys(), data.values())
    plt.title("Witcher Characters' HP Over Years")
    plt.xlabel("Year")
    plt.ylabel("HP")
    plt.show() 



"""
Açıklama: Witcher evrenindeki karakterlerin öldürdükleri düşman sayısını bar chart olarak gösterir.
Input: characters: karakter isimleri listesi (str), kills: her karakterin öldürdüğü düşman sayısı listesi (int). Uzunlukları eşit olmalı.
Örnek Input:
    characters = ['Geralt', 'Yennefer', 'Ciri']
    kills = [120, 50, 80]
Output: Hiçbir şey döndürmez. Bar chart çizer.
Ek İstek: Grafiğe legend ekle.
Başlık: Kills by Witcher Characters
x label: Characters
Y label: Kills
Legend: ['Kills']
"""
def plot_bar_chart(characters: list, kills: list) -> None:
    plt.bar(characters, kills, label='Kills')
    plt.title("Kills by Witcher Characters")
    plt.xlabel("Characters")
    plt.ylabel("Kills")
    plt.legend()
    plt.show()



"""
Açıklama: Witcher evrenindeki farklı fraksiyonların toplam güç oranlarını pasta grafiği olarak gösterir.
Input: Anahtar: fraksiyon ismi (str), Değer: güç puanı (int)
Örnek Input:
    factions = {'Witchers': 40, 'Sorcerers': 35, 'Monsters': 25}
Output: Pasta grafiği gösterir
Ek istek: Virgülden sonra 1 karakter olsun.
title: Power Distribution Among Factions

""" 
def plot_pie_chart(factions: dict) -> None:
    plt.pie(factions.values(), labels=factions.keys(), autopct='%1.1f%%')
    plt.title("Power Distribution Among Factions")
    plt.show()



"""
Açıklama: Witcher karakterlerinin tecrübe yıllarını histogram ile gösterir.
Input: Tecrübe yıllarından oluşan liste (int)
Örnek Input:
    experience_years = [5, 10, 7, 8, 6, 10, 12, 4]
Output: Histogram grafiği gösterir.
Ek İstek: X ve Y eksenlerinde uygun etiketler olsun.
Title: Distribution of Experience
X Label: Years of Experience
Y Label: Number of Characters
"""
def plot_histogram(experience_years: list) -> None:
    plt.hist(experience_years)
    plt.title("Distribution of Experience")
    plt.xlabel("Years of Experience")
    plt.ylabel("Number of Characters")
    plt.show() 
"""
Açıklama: Karakterlerin "güç seviyesi" (x) ve "popülerlik seviyesi" (y) arasındaki ilişkiyi scatterplot ile gösterir.
Input:
x: güç seviyeleri (int list)
y: popülerlik seviyeleri (int list)
labels: karakter isimleri (str list) — her noktaya label olarak gösterilecek.
Örnek Input:
    x = [80, 90, 75]
    y = [70, 85, 60]
    labels = ['Geralt', 'Yennefer', 'Ciri']
Output: Scatterplot grafiği gösterir.
Ek İstek: Noktaların üzerlerine karakter isimleri yazsın.
Title: Power vs Popularity
X Label: Power Level
Y Label: Popularity Level
"""
def plot_scatterplot(x: list, y: list, labels: list) -> None:
    plt.scatter(x,y)
    for i in range(len(x)):
        plt.text(x[i],y[i], labels[i])
    plt.title("Power vs Popularity")
    plt.xlabel("Power Level")
    plt.ylabel("Popularity Level")
    plt.show()



"""
Açıklama: Witcher evrenindeki farklı karakterlerin yıllar içindeki can puanlarını gösteren çoklu line chart çizer.
Input: data sözlüğü, anahtarlar karakter isimleri (str), değerler ise yıl-can puanı sözlükleri.
Örnek Input:
    {
    "Geralt": {2010: 80, 2011: 85, 2012: 78},
    "Ciri": {2010: 70, 2011: 75, 2012: 80}
    }
Output: Çoklu line chart gösterir (her karakter için bir çizgi).
Ek İstek: Grafiğe başlık, eksen etiketleri ve legend ekle.
"""
def plot_multi_line_chart(data: dict) -> None:
   for karakter , yillar in data.items():
       plt.plot(yillar.keys(), yillar.values(), label=karakter)
   plt.title("Witcher Characters' HP Over Years")
   plt.xlabel("Year")
   plt.ylabel("HP")
   plt.legend()
   plt.show()




"""
Açıklama: Witcher evrenindeki karakterlerin farklı düşman türlerine karşı öldürme sayısını stacked bar chart ile gösterir.

Input:
categories: düşman türleri listesi (str) örn: ['Ghoul', 'Wraith', 'Dragon']
values: karakter isimleri (str) anahtar, değer olarak da düşman türlerine göre öldürme sayısı listesi (int list) içeren sözlük.

Örnek Input:
    categories = ['Ghoul', 'Wraith', 'Dragon']
    values = {
        'Geralt': [10, 15, 5],
        'Ciri': [7, 12, 3]
    }
Output: Stacked bar chart gösterir.
"""
def plot_stacked_bar_chart(categories: list, values: dict) -> None:
    plt.bar(categories, values['Geralt'], label='Geralt')
    plt.bar(categories, values['Ciri'], bottom=values['Geralt'], label='Ciri')
    plt.legend()
    plt.show()


"""
Açıklama: Witcher karakterlerinin farklı yetenek puanlarının dağılımını boxplot ile gösterir.

Input:
Anahtar: karakter ismi (str),
Değer: yetenek puanları listesi (int)
Örnek Input:
    {
    'Geralt': [70, 75, 80, 85],
    'Ciri': [60, 65, 70, 75]
    }
Output: Boxplot grafiği gösterir.
Ek İstek: Grafikte karakter isimleri x-tick olarak gözüksün.
"""
def plot_boxplot(data: dict) -> None:
    plt.boxplot(data.values(), tick_labels=data.keys())
    plt.title("Distribution of Skill Levels")
    plt.xlabel("Characters")
    plt.ylabel("Skill Levels")
    plt.show()
