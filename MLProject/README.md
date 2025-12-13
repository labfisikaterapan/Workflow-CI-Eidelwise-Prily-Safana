# MLflow Project - Diabetes Classifier
**Nama:** Eidelwise Prily Safana

## 📋 Deskripsi
Folder ini berisi MLflow Project untuk automated training model Diabetes Classifier.

## 📁 Files
- `MLProject` - MLflow project configuration
- `conda.yaml` - Conda environment specification
- `modelling.py` - Training script dengan MLflow tracking
- `diabetes_preprocessing.csv` - Preprocessed dataset

## 🚀 Cara Menjalankan

### Local Development
```bash
# Install MLflow
pip install mlflow

# Run project
mlflow run . --experiment-name DiabetesClassifier_Eidelwise

# View results
mlflow ui
```

### Custom Parameters
```bash
mlflow run . \
  --experiment-name DiabetesClassifier_Eidelwise \
  -P n_estimators=200 \
  -P max_depth=15 \
  -P min_samples_split=5
```

## 📊 MLflow Tracking
Metrics yang dilog:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Artifacts yang disimpan:
- Model (.joblib)
- Confusion Matrix
- Feature Importance
- ROC Curve
- Precision-Recall Curve
- Classification Report (JSON)

## 🔧 Configuration
Parameters yang dapat disesuaikan:
- `n_estimators`: Number of trees (default: 100)
- `max_depth`: Maximum tree depth (default: 10)
- `min_samples_split`: Min samples to split (default: 2)
- `min_samples_leaf`: Min samples in leaf (default: 1)
- `random_state`: Random seed (default: 42)

## 🎯 CI/CD Integration
Project ini terintegrasi dengan GitHub Actions untuk automated retraining.
