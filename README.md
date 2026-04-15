#  House Price Prediction – End-to-End MLOps Project

##  Overview

This project demonstrates a **production-style Machine Learning pipeline** for predicting house prices using the California Housing dataset.

It covers the **complete ML lifecycle**:

* Data ingestion
* Data processing
* Model training
* Model serving via FastAPI

The system is designed with **modularity, reproducibility, and scalability** in mind, following real-world MLOps practices.

---

##  Key Features

*  Modular pipeline (ingestion → preprocessing → training)
*  Config-driven architecture (YAML-based)
*  Structured logging for observability
*  Feature-safe inference using `features.json`
*  FastAPI backend for real-time predictions
*  Clean separation of concerns (API vs business logic)

---

##  Project Structure

```
house-price-app/
│
├── backend/
│   ├── main.py            # FastAPI app
│   ├── schema.py          # Request/response schema
│   ├── service.py         # Prediction logic
│   └── model/
│       ├── model.pkl
│       └── features.json
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_preprocessing.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py
│   │
│   ├── constants/
│   │   ├── config.py
│   │   └── config.yaml
│   │
│   └── logger.py
│
├── artifacts/
│   ├── raw/
│   ├── processed/
│   └── logs/
│
└── notebooks/
```

---

##  Setup Instructions

### 1️ Clone the repository

```bash
git clone <your-repo-url>
cd house-price-app
```

---

### 2️ Create environment

```bash
conda create -p venv python=3.11
conda activate ./venv
```

---

### 3️ Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Run Training Pipeline

```bash
python -m src.pipeline.training_pipeline
```

This will:

* Ingest data
* Process data
* Train model
* Save model + features

---

##  Run FastAPI Server

```bash
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

##  Prediction API

### Endpoint:

```
POST /predict
```

### Sample Request:

```json
{
  "MedInc": 5.0,
  "HouseAge": 20,
  "AveRooms": 6,
  "AveBedrms": 1,
  "Population": 1000,
  "AveOccup": 3,
  "Latitude": 34,
  "Longitude": -118
}
```

### Response:

```json
{
  "prediction": 2.45
}
```

---

##  Design Decisions

### ✔ Feature Ordering

* Stored in `features.json`
* Ensures training–inference consistency

### ✔ Config-Driven System

* All paths and parameters defined in YAML
* No hardcoding

### ✔ Service Layer

* Business logic separated from API
* Easier to maintain and scale

### ✔ Logging

* Centralized logging across pipeline and API
* Useful for debugging and monitoring

---

##  Model Details

* Algorithm: Random Forest Regressor
* Metric: RMSE
* Dataset: California Housing Dataset

---

##  Future Improvements

* Add Streamlit UI
* Dockerize the application
* Integrate experiment tracking (MLflow)
* Add data & model versioning (DVC)
* Deploy on cloud (Azure / AWS)

---

##  Learnings

This project helped in understanding:

* Building end-to-end ML systems
* Structuring production-ready code
* Designing APIs for ML models
* Handling feature consistency
* Importance of logging and configuration

---


##  License

This project is open-source and available under the MIT License.
