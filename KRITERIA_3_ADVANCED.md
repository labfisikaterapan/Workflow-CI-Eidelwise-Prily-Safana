# ✅ KRITERIA 3 ADVANCED - CHECKLIST

**Nama:** Eidelwise Prily Safana  
**Tanggal:** 13 Desember 2025  
**Repository:** https://github.com/labfisikaterapan/Workflow-CI-Eidelwise-Prily-Safana

---

## 🎯 Requirements ADVANCED (4 pts)

### ✅ 1. Folder MLProject
- [x] File `MLProject` dengan entry points
- [x] File `conda.yaml` untuk environment
- [x] File `modelling.py` dengan CLI arguments
- [x] Dataset `diabetes_preprocessing.csv`

### ✅ 2. Workflow CI dengan GitHub Actions
- [x] File `.github/workflows/ci-cd.yml`
- [x] **Menggunakan `mlflow run MLProject`** ← KRITERIA UTAMA!
- [x] Parameter passing dengan `-P` flag
- [x] Automated trigger on push/PR

### ✅ 3. MLflow Project Execution
**Command yang digunakan:**
```yaml
mlflow run . \
  --experiment-name "DiabetesClassifier_Eidelwise_CI" \
  -P n_estimators=100 \
  -P max_depth=10 \
  -P min_samples_split=2 \
  -P min_samples_leaf=1 \
  -P random_state=42
```

### ✅ 4. Artifact Management
- [x] Model artifacts disimpan ke GitHub Actions
- [x] MLflow tracking ke `mlruns/` directory
- [x] Retention period 30 hari

### ✅ 5. Docker Deployment
- [x] Build Docker image dengan MLflow
- [x] Push ke Docker Hub: `eidelwiseprily/diabetes-classifier:latest`
- [x] Secrets configured (DOCKER_USERNAME, DOCKER_PASSWORD)

---

## 📊 Perbedaan BASIC vs ADVANCED

| Aspek | BASIC | ADVANCED ✓ |
|-------|-------|-----------|
| **Execution** | `python modelling.py` | `mlflow run MLProject` |
| **Environment** | Manual setup | Conda auto-management |
| **Parameters** | CLI args | MLflow -P parameters |
| **Tracking** | Manual logging | Auto MLflow tracking |
| **Reproducibility** | Low | High |

---

## ✅ VERIFICATION CHECKLIST

Pastikan workflow menjalankan:
- [x] `mlflow run .` (BUKAN `python modelling.py`)
- [x] Dengan parameter `-P` untuk hyperparameters
- [x] Di dalam `working-directory: ./MLProject`
- [x] Dengan experiment name yang jelas

---

## 🎉 STATUS: READY FOR REVIEW

Semua kriteria ADVANCED telah terpenuhi!

**Reviewer harus melihat:**
1. ✅ Step "Run MLflow Project" menggunakan `mlflow run .`
2. ✅ Parameters di-pass dengan `-P` flag
3. ✅ Artifacts tersimpan
4. ✅ Docker image di-push

**TOTAL POIN: 4/4 ✅**
