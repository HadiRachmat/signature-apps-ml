# Signature Apps - ML

Repository ini berisi skrip sederhana untuk menghasilkan dataset sintetis, melatih model klasifikasi Random Forest untuk memprediksi "progress" (cepat/sedang/lambat) santri berdasarkan fitur-fitur pembelajaran, dan menyimpan model yang terlatih.

## Ringkasan

- Bahasa: Python
- Tujuan: Demo machine learning end-to-end (generate data → train → evaluate → save/load model)
- Model: RandomForestClassifier (scikit-learn)
- Artefak utama: `data_santri.csv`, `model_progress.pkl`

## Struktur proyek

```
/home/.../signature-apps-ml
├── app/
│   └── main.py                # Skrip utama: generate data, training, evaluasi, simpan model, contoh prediksi
├── data_santri.csv            # Dataset yang dihasilkan oleh main.py
├── model_progress.pkl         # Model yang disimpan setelah training
├── requirements.txt           # Dependensi Python
```

> Catatan: Anda bekerja langsung pada file `app/main.py` — skrip tersebut sudah melakukan semua langkah (generate dataset, training, evaluasi, penyimpanan model, dan contoh prediksi).

## Penjelasan data

Skrip `main.py` menghasilkan dataset sintetis berisi kolom-kolom berikut:

- `umur` : usia peserta (12-18)
- `setoran_per_minggu` : jumlah setoran per minggu (integer, 0-14)
- `murojaah_per_minggu` : jumlah murojaah per minggu (integer, 0-14)
- `kehadiran` : persentase kehadiran (40-100)
- `nilai_ujian` : nilai ujian (50-100)
- `konsistensi` : fitur turunan (setoran_per_minggu / 7)
- `progress` : label target dengan nilai "cepat", "sedang", atau "lambat"

Label dibuat dengan logika heuristik di `main.py`:

- `cepat` jika `setoran >= 8` dan `kehadiran >= 90` dan `nilai >= 85`
- `sedang` jika `setoran >= 4` dan `kehadiran >= 70`
- `lambat` pada kondisi lain

## Cara menyiapkan lingkungan

Pastikan Anda menggunakan Python 3.10+ (skrip inspirasi menunjukkan penggunaan Python 3.12 artefak bytecode, tetapi kode kompatibel dengan 3.10+).

1. Buat virtual environment (direkomendasikan):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependensi:

```bash
pip install -r requirements.txt
```

Jika `requirements.txt` tidak berisi dependensi, tambahkan setidaknya:

```
pandas
numpy
scikit-learn
joblib
```

## Cara menjalankan

Jalankan skrip utama dari direktori proyek:

```bash
python app/main.py
```

Yang dilakukan skrip:

- Menghasilkan dataset sintetis (menyimpan ke `data_santri.csv`)
- Melakukan train/test split
- Melatih `RandomForestClassifier`
- Menampilkan classification report pada data test
- Menyimpan model ke `model_progress.pkl`
- Memuat kembali model dan menjalankan contoh prediksi

Contoh output akhir (ringkasan):

- File `data_santri.csv` berisi dataset yang dibuat
- File `model_progress.pkl` berisi model terlatih
- Teks berisi hasil evaluasi (precision/recall/f1 untuk tiap kelas)

## Contoh penggunaan prediksi (kode)

Anda dapat memuat model yang sudah disimpan dan menjalankan prediksi baru sebagai berikut:

```python
import joblib
model = joblib.load('model_progress.pkl')
# data: [umur, setoran_per_minggu, murojaah_per_minggu, kehadiran, nilai_ujian, konsistensi]
data_baru = [[15, 9, 7, 92, 88, 9/7]]
print(model.predict(data_baru))
```

## Kontrak & asumsi

Inputs

- (opsional) argumen untuk `generate_data(n)` jika Anda memodifikasi skrip

Outputs

- `data_santri.csv` dan `model_progress.pkl`

Asumsi yang diambil dari skrip saat ini

- Data disintesis (bukan data nyata)
- Label dibuat dengan aturan heuristik sederhana
- Tidak ada pipeline preprocessing terpisah; semua fitur numeric sudah siap dipakai

## Edge cases & catatan teknis

- Reproducibility: `random_state=42` pada `train_test_split` dan RandomForest sudah ditetapkan, tetapi fungsi data generator memakai modul `random` dan `numpy.random` tanpa seed global; untuk hasil deterministik, set seed eksplisit (contoh: `random.seed(42); np.random.seed(42)`).
- Skalabilitas: dataset saat ini kecil (1–2k baris); untuk skala lebih besar, pertimbangkan mengubah generator atau gunakan dataset nyata.
- Preprocessing: saat ini semua fitur numeric dan tidak dinormalisasi; jika model lain digunakan (mis. SVM), tambahkan pipeline dengan StandardScaler.

## Saran perbaikan (next steps)

- Pisahkan pipeline: buat modul `data.py`, `train.py`, `predict.py` untuk memisahkan concern.
- Tambahkan argparsing agar skrip dapat menerima mode (`generate`, `train`, `predict`) dan parameter (`--n`, `--model-path`).
- Tambahkan unit tests minimal untuk generator dan fungsi label.
- Tambahkan CI workflow (github actions) untuk linting dan test.

## Quality gates yang disarankan

- Lint: run `flake8` / `ruff`
- Type checking: `mypy` (opsional)
- Tests: pytest (tulis 2-3 test untuk generator dan training pipeline)

## Lisensi

Tambahkan lisensi jika proyek ini akan dipublikasikan (mis. MIT).

## Kontak

############### CONTOH STRUKTUR FOLDER ############################
monitoring-hafalan/
│
├── venv/                      # Virtual Environment Python
│
├── app.py                     # Entry point Streamlit
│
├── pages/                     # Halaman-halaman Streamlit
│   ├── Dashboard.py
│   ├── Data_Santri.py
│   ├── Monitoring_Hafalan.py
│   ├── Prediksi.py
│   └── Tentang.py
│
├── api/                       # Koneksi ke Backend Node.js
│   ├── santri_api.py
│   ├── hafalan_api.py
│   └── prediksi_api.py
│
├── machine_learning/
│   ├── train_model.py         # Melatih Random Forest
│   ├── predict.py             # Fungsi prediksi
│   ├── preprocessing.py       # Pembersihan data
│   └── model.pkl              # Model hasil training
│
├── data/
│   ├── dataset.csv            # Dataset training
│   └── testing.csv
│
├── components/                # Komponen UI yang bisa dipakai ulang
│   ├── sidebar.py
│   ├── navbar.py
│   ├── cards.py
│   └── charts.py
│
├── utils/
│   ├── helper.py
│   ├── config.py
│   └── constants.py
│
├── assets/
│   ├── logo.png
│   └── background.png
│
├── requirements.txt
│
└── .gitignore

Jika Anda ingin bantuan memecah kode menjadi modul, menambahkan argparsing, atau menulis tests/CI, beri tahu saya tugas mana yang mau dikerjakan selanjutnya.
