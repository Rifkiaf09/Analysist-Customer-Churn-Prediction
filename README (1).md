
# Telco Customer Churn Prediction

Proyek ini memprediksi apakah pelanggan Telco akan berhenti (churn) atau tidak, berdasarkan data historis pelanggan.

## Fitur Model
- Model: XGBoost Classifier
- Pipeline: Preprocessing (OneHotEncoder) + Model
- Akurasi: ~83%

## Cara Menjalankan (Lokal)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Input yang Diperlukan
- Data pelanggan seperti gender, tenure, jenis layanan, biaya bulanan, dll.

## Output
- Prediksi apakah pelanggan akan churn atau tidak.
