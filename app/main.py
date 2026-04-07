import pandas as pd
import numpy as np
import random

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# =========================
# 1. Generate Dataset
# =========================
def generate_data(n=1000):
    data = []

    for _ in range(n):
        umur = random.randint(12, 18)

        # distribusi realistis
        setoran = np.clip(int(np.random.normal(5, 3)), 0, 14)
        murojaah = np.clip(int(np.random.normal(4, 2)), 0, 14)
        kehadiran = np.clip(int(np.random.normal(80, 15)), 40, 100)
        nilai = np.clip(int(np.random.normal(75, 10)), 50, 100)

        konsistensi = round(setoran / 7, 2)

        # =========================
        # Labeling (logic realistis)
        # =========================
        if setoran >= 8 and kehadiran >= 90 and nilai >= 85:
            progress = "cepat"
        elif setoran >= 4 and kehadiran >= 70:
            progress = "sedang"
        else:
            progress = "lambat"

        data.append([
            umur,
            setoran,
            murojaah,
            kehadiran,
            nilai,
            konsistensi,
            progress
        ])

    columns = [
        'umur',
        'setoran_per_minggu',
        'murojaah_per_minggu',
        'kehadiran',
        'nilai_ujian',
        'konsistensi',
        'progress'
    ]

    return pd.DataFrame(data, columns=columns)


# generate dataset
df = generate_data(1200)

# simpan ke CSV
df.to_csv("data_santri.csv", index=False)

print("Dataset berhasil dibuat:", df.shape)
print(df.head())


# =========================
# 2. Training Model
# =========================
X = df[['umur', 'setoran_per_minggu', 'murojaah_per_minggu', 'kehadiran', 'nilai_ujian', 'konsistensi']]
y = df['progress']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)


# =========================
# 3. Evaluasi
# =========================
y_pred = model.predict(X_test)

print("\n=== HASIL EVALUASI ===")
print(classification_report(y_test, y_pred))


# =========================
# 4. Simpan Model
# =========================
joblib.dump(model, "model_progress.pkl")
print("\nModel disimpan!")


# =========================
# 5. Load & Prediksi Baru
# =========================
model_loaded = joblib.load("model_progress.pkl")

# contoh data baru
data_baru = [[15, 9, 7, 92, 88, 9/7]]

hasil = model_loaded.predict(data_baru)

print("\n=== PREDIKSI BARU ===")
print("Progress:", hasil[0])