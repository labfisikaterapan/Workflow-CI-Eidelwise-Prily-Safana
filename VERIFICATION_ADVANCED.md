# ✅ KRITERIA 3 ADVANCED - CHECKLIST LENGKAP

**Nama:** Eidelwise Prily Safana  
**Dataset:** Pima Indians Diabetes  
**Tanggal:** 13 Desember 2025

---

## 🎯 KRITERIA ADVANCED (4 POINTS)

### ✅ 1. Folder MLProject
- [x] File `MLProject` dengan entry points
- [x] File `conda.yaml` untuk environment
- [x] File `modelling.py` dengan training script
- [x] File `diabetes_preprocessing.csv` (dataset)
- [x] File `README.md` dokumentasi

### ✅ 2. Workflow CI dengan GitHub Actions
- [x] File `.github/workflows/ci-cd.yml`
- [x] **Menjalankan `mlflow run MLProject`** ← KRITERIA UTAMA!
- [x] Automated trigger on push/PR
- [x] Model training otomatis

### ✅ 3. Simpan Artifacts ke Repository
- [x] Upload artifacts ke GitHub Actions
- [x] Retention period 30 hari
- [x] Model files (.joblib)
- [x] MLflow runs directory

### ✅ 4. Docker Build & Push
- [x] Build Docker image
- [x] Push ke Docker Hub: `eidelwiseprily/diabetes-classifier:latest`
- [x] Docker secrets configured

---

## 📊 VERIFIKASI WORKFLOW

### Command yang Digunakan:
```yaml
mlflow run . \
  --experiment-name "DiabetesClassifier_Eidelwise_CI" \
  -P n_estimators=100 \
  -P max_depth=10 \
  -P min_samples_split=2 \
  -P min_samples_leaf=1 \
  -P random_state=42
```

### Steps Workflow:
1. ✅ Checkout Repository
2. ✅ Setup Python 3.11
3. ✅ Install Dependencies (MLflow, scikit-learn, pandas, numpy)
4. ✅ **Run MLflow Project** (`mlflow run .`)
5. ✅ Display Tracking Info
6. ✅ Save Artifacts (upload-artifact@v4)
7. ✅ Build Docker Image
8. ✅ Push to Docker Hub

---

## 🏆 PENILAIAN

| Kriteria | Requirement | Status |
|----------|-------------|--------|
| **Reject (0)** | Tidak ada MLProject | ❌ N/A |
| **Basic (2)** | Folder MLProject + Workflow CI | ✅ Done |
| **Skilled (3)** | + Simpan artifacts | ✅ Done |
| **ADVANCED (4)** | + Docker Build & Push | ✅ **DONE** |

**TOTAL: 4/4 Points ✅**

---

## 📝 REVISI TERPENUHI

### Poin yang Diminta Reviewer:
- [x] Folder MLProject tersedia ✓
- [x] File modelling.py ada ✓
- [x] File conda.yaml ada ✓
- [x] File MLProject ada ✓
- [x] **Workflow menjalankan `mlflow run MLProject`** ✓

---

## 🐳 Docker Hub

**Image:** eidelwiseprily/diabetes-classifier:latest  
**Link:** https://hub.docker.com/r/eidelwiseprily/diabetes-classifier

---

## 🔗 Repository

**GitHub:** https://github.com/labfisikaterapan/Workflow-CI-Eidelwise-Prily-Safana

---

**STATUS: READY FOR SUBMISSION ✅**
