# Workflow-CI - Kriteria 3 ADVANCED
## Nama Siswa: Eidelwise Prily Safana

---

## 📋 Deskripsi

Repository ini berisi workflow CI/CD untuk melatih model machine learning (Diabetes Classification) dan membangun Docker image menggunakan MLflow, kemudian push ke Docker Hub secara otomatis.

---

## 📁 Struktur Folder

```
Workflow-CI/
├── .github/
│   └── workflows/
│       ├── ml-pipeline.yml           # Workflow basic
│       └── ml-pipeline-docker.yml    # Workflow ADVANCED dengan Docker
├── MLProject/
│   ├── modelling.py                  # Script training model
│   ├── MLproject                     # MLflow Project file
│   ├── conda.yaml                    # Conda environment
│   ├── requirements.txt              # Python dependencies
│   ├── Dockerfile                    # Dockerfile untuk build manual
│   ├── diabetes_preprocessing.csv   # Dataset
│   └── DockerHub.txt                 # Link Docker Hub
└── README.md
```

---

## ✅ Kriteria ADVANCED yang Dipenuhi

| Kriteria | Status | Implementasi |
|----------|--------|--------------|
| Workflow CI | ✅ | GitHub Actions di `.github/workflows/` |
| Save Artifacts | ✅ | `actions/upload-artifact@v4` |
| mlflow models build-docker | ✅ | Membangun Docker image dari MLflow model |
| docker/login-action@v2 | ✅ | Login ke Docker Hub |
| docker tag | ✅ | Tag image dengan version |
| docker push | ✅ | Push image ke Docker Hub |

---

## 🚀 Workflow CI/CD Pipeline

### Pipeline Steps:

1. **Train Job**
   - Checkout repository
   - Setup Python 3.10
   - Install dependencies
   - Run MLflow training (`python modelling.py`)
   - Upload training artifacts

2. **Build Docker Job**
   - Download training artifacts
   - Login to Docker Hub (`docker/login-action@v2`)
   - Build Docker image (`mlflow models build-docker`)
   - Tag Docker image (`docker tag`)
   - Push to Docker Hub (`docker push`)

3. **Save Artifacts Job**
   - Download and organize artifacts
   - Create summary
   - Upload final artifacts (retained 90 days)

---

## 🐳 Docker Hub

- **Repository**: https://hub.docker.com/r/eizfisika/diabetes-classifier
- **Image Tags**:
  - `eizfisika/diabetes-classifier:latest`
  - `eizfisika/diabetes-classifier:v1.0.0`

### Pull & Run:
```bash
docker pull eizfisika/diabetes-classifier:latest
docker run -p 5000:5000 eizfisika/diabetes-classifier:latest
```

---

## ⚙️ GitHub Secrets Required

Untuk menjalankan workflow, tambahkan secret berikut di repository settings:

| Secret Name | Description |
|------------|-------------|
| `DOCKER_PASSWORD` | Docker Hub access token |

---

## 📝 Cara Menjalankan Workflow

1. Push ke branch `main` atau `master`
2. Atau trigger manual via "Actions" → "Run workflow"

---

## 🔗 Links

- **GitHub Repository**: https://github.com/labfisikaterapan/Workflow-CI-Eidelwise
- **Docker Hub**: https://hub.docker.com/r/eizfisika/diabetes-classifier
- **DagsHub**: https://dagshub.com/labfisikaterapan/Diabetes_Classification

---

**Author**: Eidelwise Prily Safana  
**Kriteria**: 3 - Membuat Workflow CI (ADVANCED - 4 pts)
