# 1. Görev listesine görev ekle ve task listesini geri dön(bu işlem için metotlarda nasıl değer dönülür incelemen gerekebilir.) (return keyword araştır)
def add_task(task_list: list, task: str) -> list:
    task_list.append(task)
    return task_list

# 2. Görev listesinde bir görevi sil ve task listesini geri dön(bu işlem için metotlarda nasıl değer dönülür incelemen gerekbilir)
def remove_task(task_list: list, task: str) -> list:
    task_list.remove(task)
    return task_list

# 3. Uzunluğu 10 karakterden fazla olan görevleri filtrele ve bu görevleri geri dön.
def filter_long_tasks(task_list: list) -> list:
    return [task for task in task_list if len (task) >10]


# 4. Görev sayısı çift mi kontrol et ve bu değeri geri dön
def is_even_task_count(task_list: list) -> bool:
    return len(task_list) %2==0

# 5. Görev listesindeki tüm görevleri büyük harfe çevir
def uppercase_tasks(task_list: list) -> list:
    return [task.upper()for task in task_list]

# 6. Görev listesindeki görevleri ters sırala
def reverse_tasks(task_list: list) -> list:
    return task_list[::-1]

# 7. Görev listesinde geçen belirli bir kelimeyi arayıp dönen fonksiyon
def find_task_with_keyword(task_list: list, keyword: str) -> list:
    return [task for task in task_list if keyword.lower() in task.lower()]

# 8. Görev listesinde en uzun görevi döndür
def get_longest_task(task_list: list) -> str:
    return max(task_list,key=len)

# 9. Görevleri sıralı bir şekilde döndür (alfabetik)
def sort_tasks(task_list: list) -> list:
    return sorted(task_list)

# 10. Görev listesindeki toplam karakter sayısını döndür
def total_character_count(task_list: list) -> int:
    return sum(len(task)for task in task_list)