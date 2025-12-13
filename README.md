# Workflow CI - MLflow Project
**Nama:** Eidelwise Prily Safana  
**Dataset:** Pima Indians Diabetes

## 📋 Deskripsi
Repository ini berisi implementasi Workflow CI menggunakan **MLflow Project** untuk automated retraining model machine learning dengan GitHub Actions.

## 📁 Struktur Repository
```
Workflow-CI-Eidelwise-Prily-Safana/
├── .github/
│   └── workflows/
│       └── ci-cd.yml (GitHub Actions workflow)
├── MLProject/ (folder)
│   ├── MLProject (MLflow project config)
│   ├── conda.yaml (environment specification)
│   ├── modelling.py (training script)
│   ├── diabetes_preprocessing.csv (dataset)
│   └── README.md
├── .gitignore
└── README.md
```

## 🚀 Fitur Utama

### 1. MLflow Project
- Automated model training dengan MLflow tracking
- Reproducible experiments dengan conda environment
- Model versioning dan artifact logging

### 2. GitHub Actions CI/CD
- **Trigger:** Push ke main branch atau Pull Request
- **Pipeline:**
  1. Setup Python & Conda environment
  2. Install MLflow dependencies
  3. Run MLflow Project untuk training
  4. Log metrics dan artifacts
  5. Save trained model

### 3. Automated Retraining
Workflow akan otomatis melakukan retraining model ketika:
- Ada perubahan pada dataset preprocessing
- Ada update pada script modelling.py
- Manual trigger via GitHub Actions

## 📊 MLflow Tracking
Semua eksperimen tercatat dengan:
- **Parameters:** Hyperparameters model
- **Metrics:** Accuracy, Precision, Recall, F1, ROC-AUC
- **Artifacts:** Model file, confusion matrix, visualisasi

## 🐳 Docker Hub
Docker image untuk deployment: `[akan diupdate setelah build]`

## 🔧 Cara Menggunakan

### 1. Clone Repository
```bash
git clone https://github.com/labfisikaterapan/Workflow-CI-Eidelwise-Prily-Safana.git
cd Workflow-CI-Eidelwise-Prily-Safana
```

### 2. Install MLflow
```bash
pip install mlflow
conda env create -f MLProject/conda.yaml
conda activate diabetes-env
```

### 3. Run MLflow Project Locally
```bash
mlflow run MLProject --experiment-name DiabetesClassifier_Eidelwise
```

### 4. View MLflow UI
```bash
mlflow ui
# Buka http://localhost:5000
```

## 📈 Workflow CI/CD Pipeline

```mermaid
graph LR
    A[Push/PR] --> B[GitHub Actions Triggered]
    B --> C[Setup Environment]
    C --> D[Install Dependencies]
    D --> E[Run MLflow Project]
    E --> F[Model Training]
    F --> G[Log Metrics & Artifacts]
    G --> H[Save Model]
```

## 📝 MLProject Configuration
```yaml
name: DiabetesClassifier_Eidelwise

conda_env: conda.yaml

entry_points:
  main:
    parameters:
      n_estimators: {type: int, default: 100}
      max_depth: {type: int, default: 10}
      random_state: {type: int, default: 42}
    command: "python modelling.py {n_estimators} {max_depth} {random_state}"
```

## 🎯 Hasil Training
Model RandomForestClassifier dengan performa:
- **Accuracy:** ~85%
- **Precision:** ~82%
- **Recall:** ~78%
- **F1-Score:** ~80%
- **ROC-AUC:** ~88%

## 👤 Author
**Eidelwise Prily Safana**

## 📝 License
Educational purposes only
