# 🚀 PETUNJUK PUSH KE GITHUB - KRITERIA 3 ADVANCED (REVISI)

## ⚠️ PERBAIKAN PENTING:
Workflow sekarang menggunakan **`mlflow run MLProject`** (BENAR untuk ADVANCED)  
Bukan `python modelling.py` lagi!

## ✅ Yang Sudah Diperbaiki:
1. ✅ Workflow CI/CD menggunakan `mlflow run .` dengan parameters  
2. ✅ Entry point di MLProject file sudah benar
3. ✅ Parameters passing dengan `-P` flag MLflow
4. ✅ Docker build & push ke Docker Hub
5. ✅ Artifact management ke GitHub

---

## 📝 Langkah-Langkah Push ke GitHub:

### 1️⃣ Di Terminal, jalankan perintah berikut satu per satu:

```powershell
cd "C:\Users\mriva\OneDrive\Dokumen\New folder\SMSL_Eidelwise Prily Safana\GitHub_Repos\Workflow-CI-Eidelwise-Prily-Safana"

# Add semua file
git add .

# Commit dengan pesan yang jelas
git commit -m "Fix: Kriteria 3 ADVANCED - Gunakan mlflow run MLProject (bukan direct Python)"

# Pull dulu (jika repository sudah ada)
git pull origin main --allow-unrelated-histories

# Push ke GitHub
git push -u origin main
```

---

## ⚠️ JIKA ADA ERROR:

### Error: "failed to push some refs"
Solusi:
```powershell
git pull origin main --rebase
git push -u origin main
```

### Error: "Please tell me who you are"
Sudah diset, tapi kalau masih error:
```powershell
git config user.email "eidelwise@example.com"
git config user.name "Eidelwise Prily Safana"
```

---

## 🔧 Setup Docker Hub Secrets (PENTING!)

Setelah push ke GitHub, tambahkan secrets:

1. Buka GitHub repository
2. Go to **Settings** → **Secrets and variables** → **Actions**
3. Klik **New repository secret**
4. Tambahkan 2 secrets:
   - Name: `DOCKERHUB_USERNAME` → Value: `eidelwiseprily`
   - Name: `DOCKERHUB_TOKEN` → Value: (Docker Hub token/password)

---

## 🎯 Test Workflow:

### Manual Trigger:
1. Buka repository di GitHub
2. Go to **Actions** tab
3. Klik **Kriteria 3 ADVANCED - ML Pipeline with Docker**
4. Klik **Run workflow** → **Run workflow**

### Auto Trigger:
Workflow akan otomatis jalan saat:
- Push ke branch `main`
- Ada perubahan di folder `MLProject/`

---

## ✅ Verifikasi ADVANCED (4 pts):

Cek bahwa workflow berhasil menjalankan:
- [x] Training model dengan `python modelling.py`
- [x] MLflow tracking metrics
- [x] Save artifacts ke GitHub Actions
- [x] Build Docker image
- [x] Push ke Docker Hub

**Screenshot yang dibutuhkan:**
1. ✅ Workflow success di GitHub Actions
2. ✅ Artifacts tersimpan
3. ✅ Docker image di Docker Hub

---

## 📊 Expected Output:

Workflow akan:
1. ✅ Train model → Output metrics
2. ✅ Log ke MLflow → mlruns/ folder
3. ✅ Save artifacts → GitHub Artifacts (30 hari)
4. ✅ Build Docker → eidelwiseprily/diabetes-classifier:latest
5. ✅ Push ke Docker Hub

**Total: 4 Points ADVANCED ✅**

---

## 🐳 Docker Hub Link:
Update file `Docker_Hub_Link.txt`:
```
https://hub.docker.com/r/eidelwiseprily/diabetes-classifier
```

---

## 📞 Jika Ada Masalah:

1. Cek logs di GitHub Actions
2. Pastikan Docker Hub secrets sudah diset
3. Verify file structure sudah benar
4. Test training local dulu:
   ```bash
   cd MLProject
   python modelling.py --n_estimators 100 --max_depth 10
   ```

---

**READY TO PUSH! 🚀**
