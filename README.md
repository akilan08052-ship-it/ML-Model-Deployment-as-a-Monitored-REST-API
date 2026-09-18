
# ML Model Deployment as a Monitored REST API

A production-oriented REST API for Iris flower species classification using a trained machine learning model. The application is developed using FastAPI, containerized with Docker, and integrated with Prometheus-compatible monitoring to track API performance, request counts, response durations, and application health.

## 📌 About the Project

This project focuses on deploying a machine learning model as a monitored REST API. The API predicts the species of an Iris flower based on the sepal and petal measurements provided by the user.

The application supports single and batch predictions, model information retrieval, health monitoring, API documentation, and customized metrics for observing endpoint performance.

The project also includes API key authentication, integration testing, and HTTPX-based load testing to evaluate the reliability and performance of the deployed application.

---

## 🚀 Features

- Iris flower species prediction using a trained machine learning model
- Single flower prediction
- Batch flower prediction
- Model information and accuracy retrieval
- Application and model health monitoring
- Swagger UI for interactive API documentation
- Versioned API endpoints
- API key authentication for protected endpoints
- Prometheus-compatible custom metrics
- Docker containerization
- Integration testing over HTTP
- HTTPX-based load testing
- Centralized application logging
- Request ID and response duration tracking

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| FastAPI | REST API development |
| Uvicorn | ASGI application server |
| Pydantic | Request validation and response schemas |
| Scikit-learn | Machine learning model |
| Joblib / Pickle | Model serialization |
| Swagger UI | API documentation |
| Prometheus | API monitoring and metrics |
| Docker | Application containerization |
| Docker Compose | Local container orchestration |
| Pytest | Automated testing |
| HTTPX | HTTP requests and load testing |
| Git & GitHub | Version control and source management |

---

## 📂 Project Structure

```text
ML-Model-Deployment-as-a-Monitored-REST-API/
│
├── app/
│   ├── logs/
│   │   └── app.log
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── routes/
│   │   ├── v1.py
│   │   └── v2.py
│   │
│   ├── __init__.py
│   ├── config.py
│   ├── dependencies.py
│   ├── logging_config.py
│   ├── main.py
│   └── metrics.py
│
├── ml/
│   ├── saved_model/
│   │   ├── model.pkl
│   │   ├── accuracy.pkl
│   │   └── scaler.pkl
│   │
│   ├── iris.csv
│   └── train.py
│
├── tests/
│   ├── batch_load.py
│   ├── conftest.py
│   ├── predict_load.py
│   ├── security_test.py
│   └── test_integration.py
│
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

> **Note:** Update the structure if your actual filenames or folders differ.

---

## 🔧 API Functionalities

### 1. Single Prediction

Predicts the Iris flower species using four input features:

- Sepal length
- Sepal width
- Petal length
- Petal width

### 2. Batch Prediction

Accepts multiple flower feature records and returns predictions for each input.

### 3. Model Information

Provides information about the loaded machine learning model, including available accuracy information.

### 4. Health Monitoring

Checks the application and model loading status.

### 5. Prometheus Metrics

Provides customized metrics to monitor API activity, including:

- Total number of requests
- Request duration
- Endpoint-level request counts
- Response status information
- Application health-related metrics, where implemented

---

## 🔐 API Authentication

Protected endpoints require an API key in the request header.

Example:

```http
X-API-Key: YOUR_API_KEY
```

Authentication is implemented using FastAPI dependencies.

**Security recommendations:**

- Store API keys in environment variables.
- Do not commit `.env` files containing secrets.
- Configure production secrets through the hosting platform.
- Do not expose private API keys in screenshots or public documentation.

---

## 📥 Installation and Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/akilan08052-ship-it/ML-Model-Deployment-as-a-Monitored-REST-API.git
```

Navigate to the project directory:

```bash
cd ML-Model-Deployment-as-a-Monitored-REST-API
```

### 2. Create a Virtual Environment

```bash
python -m venv env
```

### 3. Activate the Environment

**Windows:**

```bash
env\Scripts\activate
```

**Linux / macOS:**

```bash
source env/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
API_V1_STR=/api/v1
API_V2_STR=/api/v2
MODEL_PKL_PATH=ml/saved_model/model.pkl
ACCURACY_PKL_PATH=ml/saved_model/accuracy.pkl
```

Add any other environment variables required by your application.

### 6. Start the Application

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## 🐳 Docker Deployment

### Build and Run with Docker Compose

Run the following command from the project root:

```bash
docker compose up --build
```

To run the services in the background:

```bash
docker compose up --build -d
```

### Stop the Containers

```bash
docker compose down
```

### View Container Logs

```bash
docker compose logs -f
```

Ensure that the trained model files are included in the Docker image or mounted correctly according to your deployment configuration.

---

## 🧪 Testing

The project includes integration tests, security tests, and HTTPX-based load tests.

> Run the following commands using your actual filenames and test configuration.

### 1. Integration Testing

Tests the API endpoints through HTTP requests.

```bash
python -m pytest tests/test_integration.py -v
```

### 2. Security Testing

Tests API key authentication and unauthorized request handling.

```bash
python -m pytest tests/security_test.py -v
```

### 3. Configuration / Fixture Tests

If you have a separate test file for configuration:

```bash
python -m pytest tests/conf_test.py -v
```

Use `conftest.py` for shared pytest fixtures rather than executing it as a standalone test.

### 4. Single Prediction Load Test

```bash
python -m tests.predict_load
```

### 5. Batch Prediction Load Test

```bash
python -m tests.batch_load
```

### Testing Objectives

- Verify API endpoint functionality.
- Validate request and response schemas.
- Confirm API key authentication.
- Test communication with the running container.
- Measure request processing time.
- Identify errors during concurrent or repeated requests.
- Evaluate API behavior under load.

---

## 📊 Monitoring with Prometheus

Prometheus-compatible metrics are implemented to provide insights into API performance.

### Metrics Include

- Request count
- Request duration
- Endpoint-level monitoring
- HTTP response status tracking
- Custom application metrics

### Access Metrics Locally

```text
http://127.0.0.1:8000/metrics
```

**Note:** Use the actual metrics route configured in your FastAPI application. The standard Prometheus endpoint name is `/metrics`, not `/metrices`.

Prometheus-compatible metrics can be scraped by a Prometheus server for further monitoring and visualization.

---

## 📖 Swagger API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

### Local Swagger URL

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides:

- Available API endpoints
- Request schemas
- Response schemas
- Authentication support, when configured
- Interactive API testing

---

## ☁️ Online Deployment with Render

The FastAPI application can be deployed online using Docker and Render.

### Deployment Steps

1. Push the project to GitHub.
2. Create a Web Service in Render.
3. Connect the GitHub repository.
4. Select Docker as the runtime.
5. Configure the required environment variables.
6. Deploy the application.
7. Verify that the service status is `Live`.
8. Test the deployed API using its public URL.

### Example Production API URL

```text
https://your-service-name.onrender.com
```

### Production Swagger URL

```text
https://your-service-name.onrender.com/docs
```

### Production Health Check

```text
https://your-service-name.onrender.com/health
```

Do not include private API keys or sensitive deployment configuration in the repository.

---

## 📈 Performance Testing

HTTPX-based load testing is used to evaluate API behavior under repeated requests.

The load tests can measure:

- Total requests
- Successful requests
- Failed requests
- Total execution time
- Requests per second
- Response duration

### Example Result Format

```text
Total requests: 200
Successful requests: 200
Failed requests: 0
Total duration: [measured value] seconds
Requests per second: [measured value]
```

> Replace the example values with the actual results from your load test. Do not report sample values as measured performance.

---

## 🐞 Issues and Fixes

During development and deployment, common issues addressed included:

| Issue | Resolution |
|-------|------------|
| Missing API key | Implemented API key dependency validation |
| Docker port configuration | Configured the application to use the deployment environment's port |
| Model file loading | Configured model paths and container file availability |
| Request validation errors | Used Pydantic schemas |
| Integration testing | Tested the running application over HTTP |
| Monitoring | Added custom metrics for API activity |
| Load testing | Used HTTPX to measure request performance |

Update this table with the actual issues and fixes encountered during your project.

---

## 🔒 Security Considerations

- API key authentication is used for protected endpoints.
- Secrets should be managed through environment variables.
- `.env` files should be excluded from Git tracking.
- API keys should be rotated if exposed.
- Production applications should use HTTPS.
- Authentication and authorization requirements should be validated for each protected route.

---

## 🎯 Project Objectives

- Deploy a machine learning model through a REST API.
- Implement scalable API endpoints using FastAPI.
- Containerize the application using Docker.
- Add monitoring and logging for API observability.
- Perform integration and load testing.
- Learn cloud deployment using Render.
- Apply basic API security practices.

---

## 👨‍💻 Author

**Akilan A.**

B.Tech Information Technology Student

GitHub: [akilan08052-ship-it](https://github.com/akilan08052-ship-it)

---

## 📜 License

This project is developed for educational and internship purposes.