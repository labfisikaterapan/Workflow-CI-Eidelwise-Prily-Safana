"""
Modelling - Diabetes Classification
Nama Siswa: Eidelwise Prily Safana
Kriteria 2: Basic - Menggunakan MLflow Autolog

File ini melatih model machine learning menggunakan MLflow Tracking UI
dengan autolog untuk mencatat parameter, metrik, dan artefak secara otomatis.
"""

import pandas as pd
import numpy as np
import argparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, 
    f1_score, roc_auc_score, confusion_matrix
)
import mlflow
import mlflow.sklearn
import warnings
warnings.filterwarnings('ignore')


def load_preprocessed_data(filepath: str) -> tuple:
    """
    Memuat data yang sudah dipreprocessing.
    
    Args:
        filepath: Path ke file CSV
        
    Returns:
        Tuple (X_train, X_test, y_train, y_test)
    """
    print(f"[INFO] Memuat data dari: {filepath}")
    df = pd.read_csv(filepath)
    
    # Pisahkan fitur dan target
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"[INFO] Training samples: {len(X_train)}")
    print(f"[INFO] Testing samples: {len(X_test)}")
    
    return X_train, X_test, y_train, y_test


def train_model_with_autolog(n_estimators=100, max_depth=10, min_samples_split=2, 
                              min_samples_leaf=1, random_state=42):
    """
    Melatih model RandomForest dengan MLflow autolog.
    
    Args:
        n_estimators: Jumlah trees dalam forest
        max_depth: Kedalaman maksimal tree
        min_samples_split: Min samples untuk split
        min_samples_leaf: Min samples di leaf
        random_state: Random seed
    """
    print("=" * 60)
    print("TRAINING MODEL - MLFLOW AUTOLOG")
    print("Nama Siswa: Eidelwise Prily Safana")
    print("=" * 60)
    print(f"Hyperparameters:")
    print(f"  n_estimators: {n_estimators}")
    print(f"  max_depth: {max_depth}")
    print(f"  min_samples_split: {min_samples_split}")
    print(f"  min_samples_leaf: {min_samples_leaf}")
    print(f"  random_state: {random_state}")
    
    # Load data
    X_train, X_test, y_train, y_test = load_preprocessed_data(
        'diabetes_preprocessing.csv'
    )
    
    # Enable autolog
    mlflow.sklearn.autolog()
    
    # Check if running from mlflow run (MLFLOW_RUN_ID will be set)
    import os
    is_mlflow_run = 'MLFLOW_RUN_ID' in os.environ
    
    if is_mlflow_run:
        # Running from mlflow run - don't create new run, use existing context
        from contextlib import nullcontext
        run_context = nullcontext()
        print("[INFO] Running from mlflow run command")
    else:
        # Standalone mode - create our own experiment and run
        mlflow.set_tracking_uri("mlruns")
        mlflow.set_experiment("Diabetes_Classification_Eidelwise")
        run_context = mlflow.start_run(run_name="RandomForest_Autolog")
        print("[INFO] Running in standalone mode")
    
    with run_context:
        print("\n[INFO] Melatih model RandomForestClassifier...")
        
        # Inisialisasi model dengan parameters
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            random_state=random_state,
            n_jobs=-1
        )
        
        # Training
        model.fit(X_train, y_train)
        
        # Prediksi
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        # Hitung metrik
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        print("\n" + "=" * 60)
        print("HASIL EVALUASI MODEL")
        print("=" * 60)
        print(f"Accuracy:  {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        print(f"F1-Score:  {f1:.4f}")
        print(f"ROC-AUC:   {roc_auc:.4f}")
        
        print("\nConfusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        
        print("\n[INFO] Model dan metrik dicatat di MLflow Tracking UI")
        if mlflow.active_run():
            print(f"[INFO] Run ID: {mlflow.active_run().info.run_id}")
        
    return model


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Train Diabetes Classifier')
    parser.add_argument('--n_estimators', type=int, default=100, 
                        help='Number of trees in forest')
    parser.add_argument('--max_depth', type=int, default=10,
                        help='Maximum depth of trees')
    parser.add_argument('--min_samples_split', type=int, default=2,
                        help='Minimum samples required to split')
    parser.add_argument('--min_samples_leaf', type=int, default=1,
                        help='Minimum samples required at leaf')
    parser.add_argument('--random_state', type=int, default=42,
                        help='Random seed for reproducibility')
    
    args = parser.parse_args()
    
    # NOTE: Don't set tracking URI here - let train_model_with_autolog handle it
    # based on whether we're running from mlflow run or standalone
    
    # Jalankan training dengan parameters
    model = train_model_with_autolog(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        min_samples_split=args.min_samples_split,
        min_samples_leaf=args.min_samples_leaf,
        random_state=args.random_state
    )
    
    print("\n" + "=" * 60)
    print("TRAINING SELESAI")
    print("=" * 60)
    print("\nUntuk melihat hasil di MLflow UI, jalankan:")
    print("  mlflow ui --port 5000")
    print("Kemudian buka: http://localhost:5000")
