"""
MLflow Project - Modelling
Nama Siswa: Eidelwise Prily Safana
Kriteria 3: ADVANCE - Workflow CI dengan Docker

File ini melatih model dan dapat dijalankan sebagai MLflow Project.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, 
    f1_score, roc_auc_score, confusion_matrix
)
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
import argparse
import os
import warnings
warnings.filterwarnings('ignore')


def load_data(filepath):
    """Load preprocessed data."""
    print(f"[INFO] Loading data from: {filepath}")
    df = pd.read_csv(filepath)
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


def train_model(n_estimators, max_depth, min_samples_split, data_path):
    """Train RandomForest model with given parameters."""
    
    X_train, X_test, y_train, y_test = load_data(data_path)
    
    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("min_samples_split", min_samples_split)
        
        # Train model
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth if max_depth > 0 else None,
            min_samples_split=min_samples_split,
            random_state=42,
            n_jobs=-1
        )
        model.fit(X_train, y_train)
        
        # Predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)
        mlflow.log_metric("roc_auc", roc_auc)
        
        # Log model
        signature = infer_signature(X_train, y_pred)
        mlflow.sklearn.log_model(
            model, 
            "model",
            signature=signature
        )
        
        print(f"\n{'='*50}")
        print("Model Training Complete")
        print(f"{'='*50}")
        print(f"Accuracy:  {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        print(f"F1-Score:  {f1:.4f}")
        print(f"ROC-AUC:   {roc_auc:.4f}")
        
        return model


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators", type=int, default=100)
    parser.add_argument("--max_depth", type=int, default=10)
    parser.add_argument("--min_samples_split", type=int, default=2)
    parser.add_argument("--data_path", type=str, default="diabetes_preprocessing.csv")
    
    args = parser.parse_args()
    
    train_model(
        args.n_estimators,
        args.max_depth,
        args.min_samples_split,
        args.data_path
    )
