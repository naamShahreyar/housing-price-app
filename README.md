#  House Price Prediction – End-to-End MLOps Project

##  Overview

This project demonstrates a **production-ready Machine Learning system** for predicting house prices using the California Housing dataset.

It implements a **full-stack ML application**, including:

* Data pipeline
* Model training
* API serving (FastAPI)
* Interactive UI (Streamlit)
* Containerized deployment (Docker)

---

##  System Architecture

```
User → Streamlit UI → FastAPI Backend → Model → Prediction
```

---

##  Key Features

* End-to-end ML pipeline (ingestion → preprocessing → training)
* Config-driven architecture (YAML-based)
* Centralized structured logging
* Feature-safe inference
* REST API using FastAPI
* Interactive UI using Streamlit
* Fully containerized using Docker
* Separation of training and inference environments

---

##  Project Structure

```
house-price-app/
│
├── backend/
│   ├── main.py
│   ├── schema.py
│   ├── service.py
│
├── frontend/
│   └── app.py
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
│   ├── model/
│   ├── raw/
│   ├── processed/
│   └── logs/
│
├── docker-compose.yml
├── requirements.txt
├── requirements-prod.txt
└── README.md
```

---

##  Setup Instructions (Local)

### 1️ Clone the repository

```
git clone <your-repo-url>
cd house-price-app
```

---

### 2️ Create environment

```
conda create -p venv python=3.11
conda activate ./venv
```

---

### 3️ Install dependencies

```
pip install -r requirements.txt
```

---

##  Run Training Pipeline

```
python -m src.pipeline.training_pipeline
```

This will:

* Ingest data
* Process data
* Train model
* Save model artifacts

---

##  Run Application (Without Docker)

### Start Backend

```
uvicorn backend.main:app --reload
```

### Start Frontend

```
streamlit run frontend/app.py
```

---

##  Run with Docker (Recommended)

### Build and run

```
docker-compose up --build
```

---

### Access services

* UI → http://localhost:8501
* API → http://localhost:8000/docs

---

##  Prediction API

### Endpoint

```
POST /predict
```

---

### Sample Request

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

---

### Response

```json
{
  "prediction": 2.45
}
```

---

##  Design Decisions

### ✔ Feature Consistency

* Ensured via schema validation (Pydantic)
* Prevents training–inference mismatch

### ✔ Config-Driven System

* YAML-based configuration
* No hardcoded paths

### ✔ Service Layer

* Separates API from business logic
* Improves maintainability

### ✔ Logging

* Centralized logging
* Useful for debugging and monitoring

### ✔ Containerization

* Separate frontend & backend containers
* Lightweight production dependencies
* Reproducible environment

---

##  Model Details

* Algorithm: Random Forest Regressor
* Metric: RMSE
* Dataset: California Housing Dataset

---

##  Future Improvements

* Experiment tracking (MLflow)
* Data & model versioning (DVC)
* Cloud deployment (Azure / AWS)
* CI/CD pipeline
* Monitoring & alerting

---

##  Learnings

* Building end-to-end ML systems
* Structuring production-ready code
* API-based model serving
* Containerization with Docker
* Handling real-world deployment issues

---

##  Demo

*Add screenshots or demo video here*

---

##  License

MIT License
