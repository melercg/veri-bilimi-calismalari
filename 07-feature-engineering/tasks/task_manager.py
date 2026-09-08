import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.utils import resample

# Açıklama: Witcher karakter veri setini CSV'den okur ve bir pandas.DataFrame döndürür.
# Input:filepath: str (CSV dosya yolu)
# Output: pd.DataFrame
def load_witcher_dataset(filepath):
    df=pd.read_csv(filepath)
    return df 

# Açıklama: Hedef sınıf kolonunun dağılımını verir.
# Input: df: pd.DataFrame, target_column: str
# Output: dict (sınıf: adet)
def get_class_distribution(df, target_column):
    return df[target_column].value_counts().to_dict()


# Açıklama: Belirtilen kategorik kolona Label Encoding uygular.
# Input: df: pd.DataFrame, column: str
# Output: pd.DataFrame (kolon Label Encoding yapılmış)
def apply_label_encoding(df, column):
   encoder=LabelEncoder()
   df[column]=encoder.fit_transform(df[column])
   return df

# Açıklama: Belirtilen kategorik kolona One Hot Encoding uygular.
# Input: df: pd.DataFrame, column: str
# Output: pd.DataFrame (kolon OHE yapılmış)
def apply_one_hot_encoding(df, column):
    encoded = pd.get_dummies(df[column], prefix=column)
    df = df.drop(columns=[column])
    df = pd.concat([df, encoded], axis=1)
    return df
# Açıklama: Hedef kolonun dengesiz sınıflarını eşitlemek için down sampling uygular.
# Input: df: pd.DataFrame, target_column: str
# Output: pd.DataFrame (dengelenmiş)
def down_sample(df, target_column):
    class_counts = df[target_column].value_counts()
    majority_class = class_counts.idxmax()
    minority_class = class_counts.idxmin()
    df_majority = df[df[target_column] == majority_class]
    df_minority = df[df[target_column] == minority_class]
    df_majority_downsampled = resample(
    df_majority,
    replace=False,
    n_samples=len(df_minority),
    random_state=42
    ) 
    df_balanced = pd.concat([
    df_majority_downsampled,
    df_minority
    ])
    return df_balanced


# Açıklama: Hedef kolonun dengesiz sınıflarını eşitlemek için up sampling uygular.
# Input: df: pd.DataFrame, target_column: str
# Output: pd.DataFrame
def up_sample(df, target_column):

    class_counts = df[target_column].value_counts()
    majority_class = class_counts.idxmax()
    minority_class = class_counts.idxmin()

    df_majority = df[df[target_column] == majority_class]
    df_minority = df[df[target_column] == minority_class]

    df_minority_upsampled = resample(
        df_minority,
        replace=True,
        n_samples=len(df_majority),
        random_state=42
    )

    df_balanced = pd.concat([
        df_majority,
        df_minority_upsampled
    ])

    return df_balanced



# Açıklama: Girdi verisine SMOTE uygular ve yeni X, y döndürür.
# Input: X: np.ndarray veya pd.DataFrame, y: np.ndarray veya pd.Series
# Output:(X_resampled, y_resampled) (numpy array)
def apply_smote(X, y):
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    return X_resampled, y_resampled
    
# Açıklama: DataFrame'i özellikler (X) ve hedef (y) olarak ayırır.
# Input: df: pd.DataFrame, target_column: str
# Output:(X: pd.DataFrame, y: pd.Series)
def split_features_target(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y

# Açıklama: Veri setinin temel istatistiklerini ve kolon bilgilerini döndürür.
# Input: df: pd.DataFrame
# Output: dict
def summarize_dataset(df):
    summary = {
    "shape": df.shape,
    "columns": df.columns.tolist(),
     "dtypes": df.dtypes.to_dict()
    }

    return summary