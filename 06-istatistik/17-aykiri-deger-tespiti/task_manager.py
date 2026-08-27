def five_number_summary(data: list) -> dict:
    """
    Min, Q1, Median, Q3, Max değerlerini içeren sözlük döndür.
    Output örneği: {'min': ..., 'Q1': ..., 'median': ..., 'Q3': ..., 'max': ...}
    """

def detect_outliers(data: list) -> list:
    """
    IQR metoduyla aykırı değerleri tespit et.
    Output: [list of outliers]
    """

def draw_boxplot(data: list) -> None:
    """
    Verinin boxplot'unu çiz.
    Output: matplotlib görseli
    """

def draw_histogram(data: list, title: str = "Histogram") -> None:
    """
    Histogramı çiz.
    """

#Input: [1, 2, 3, 4, 100]
#Output: skewness değeri, > 0 ise sağa çarpık
def calculate_skewness(data: list) -> float:
    """
    Veri setinin skewness (çarpıklık) değerini hesapla.
    """

#Input: [1, 2, 3, 4, 100]
#skewness değerini hesaplamalısın. bu değere göre 'left', 'right' veya 'symmetric' değerini döndür
def is_skewed(data: list) -> str:
    """
    Skewness değerine göre 'left', 'right' veya 'symmetric' döndür.
    """

def calculate_covariance(x: list, y: list) -> float:
    """
    İki veri seti arasındaki kovaryansı hesapla.
    """

def calculate_correlation(x: list, y: list) -> float:
    """
    Pearson correlation coefficient hesapla.
    """

def is_positive_correlation(x: list, y: list) -> bool:
    """
    Korelasyon pozitif mi kontrol et.
    """

def compare_variables(x: list, y: list) -> dict:
    """
    Hem kovaryans hem de korelasyonu döndür.
    Output: {'covariance': ..., 'correlation': ...}
    """