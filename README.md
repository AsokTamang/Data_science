# 💼 AI & Data Science Salary Predictor

> An end-to-end Machine Learning web application that predicts salaries for AI and Data Science professionals — built with real-world job market data, a full ML pipeline, and deployed on AWS using Docker and CI/CD automation.

---

## 📌 Table of Contents

- [Description](#-description)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Model Details](#-model-details)
- [Dataset](#-dataset)
- [Installation & Local Setup](#-installation--local-setup)
- [Usage](#-usage)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Deployment](#-deployment)
- [Example Output](#-example-output)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 Description

The **AI & Data Science Salary Predictor** is a full-stack machine learning application that estimates the expected salary of professionals in the Data Science and AI industry. The model is trained on real-world job market data (2020–2026) and considers various factors such as job title, experience level, education, technical skills, company size, location, and hiring trends.

This project was built as an end-to-end ML system — from raw data and EDA all the way to a deployed web application — making it a complete demonstration of both Data Science and MLOps skills.

---

## 🌐 Live Demo

> App deployed on AWS EC2 via Docker container.

```
http://3.133.138.169:8000/prediction_form
```

---

## ✨ Features

- 🔍 **Exploratory Data Analysis (EDA)** — Deep analysis of job market trends, salary distributions, and skill demand patterns
- ⚙️ **Automated ML Pipeline** — Data ingestion → transformation → model training, all automated
- 🏆 **Best Model Selection** — Multiple models trained and compared using R² score with hyperparameter tuning
- 🧹 **Data Transformation Pipeline** — Handles missing values, encoding, and feature scaling automatically
- 🌐 **FastAPI Web Application** — Clean REST API with an interactive HTML/CSS frontend
- 🐳 **Dockerized** — Fully containerized for consistent behavior across all environments
- 🔁 **CI/CD Pipeline** — Automated testing, linting, building, and deployment via GitHub Actions
- ☁️ **AWS Deployment** — Docker image stored in ECR, app running on EC2

---

## 🛠 Technologies Used

### Machine Learning & Data
| Tool | Purpose |
|------|---------|
| Python 3.12 | Core programming language |
| Pandas & NumPy | Data manipulation and analysis |
| Scikit-learn | ML models, pipelines, preprocessing |
| Matplotlib & Seaborn | EDA visualizations |

### Backend & API
| Tool | Purpose |
|------|---------|
| FastAPI | REST API framework |
| Uvicorn | ASGI web server |
| Pydantic | Data validation |

### DevOps & Deployment
| Tool | Purpose |
|------|---------|
| Docker | Containerization |
| GitHub Actions | CI/CD automation |
| AWS ECR | Docker image registry |
| AWS EC2 | Cloud server for running the app |
| Flake8 | Code linting |

---

## 📁 Project Structure

```
salary-predictor/
│
├── .github/
│   └── workflows/
│       └── aws.yml               # CI/CD GitHub Actions workflow
│
├── artifacts/                    # Saved model & preprocessor files
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── src/
│   ├── pipeline/
│   │   ├── predict_pipeline.py   # Prediction pipeline
│   │   ├── train_pipeline.py     # Training pipeline
│   │   └── data_validation_pipeline.py
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── exception.py              # Custom error handling
│   └── logger_file.py            # Logging setup
│
├── statics/
│   ├── index.html                # Prediction form UI
│   └── home.html                 # Landing page
│
├── notebook/
│   └── EDA.ipynb                 # Exploratory Data Analysis
├── main.py                       # FastAPI application entry point
├── Dockerfile                    # Docker build instructions
├── requirements.txt              # Python dependencies
└── README.md
```

---

## ⚙️ How It Works

```
User fills the form (job title, skills, experience, etc.)
            ↓
FastAPI receives JSON payload via POST /predict
            ↓
CustomData class structures the input into a DataFrame
            ↓
Data Transformation Pipeline applies:
  - Imputation (handles missing values)
  - Encoding (categorical → numerical)
  - Scaling (normalizes numerical features)
            ↓
Trained ML Model generates salary prediction
            ↓
Prediction returned as JSON → displayed on frontend
```

---

## 🤖 Model Details

### Training Process
- Multiple regression models were trained and compared
- **Hyperparameter tuning** applied to find the best configuration
- Best model selected based on **R² score** on test data

### Models Evaluated
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

### Input Features

| Feature | Type | Description |
|---------|------|-------------|
| `years_experience` | Numerical | Total years of work experience |
| `experience_level` | Ordinal | Entry / Mid / Senior |
| `education_level` | Ordinal | Bachelor / Master / PhD |
| `job_title` | Categorical | Data Scientist, ML Engineer, etc. |
| `company_industry` | Categorical | Technology, Finance, Healthcare, etc. |
| `country` | Categorical | USA, UK, India, etc. |
| `remote_type` | Categorical | Onsite / Hybrid / Remote |
| `company_size` | Categorical | MNC / Medium / Startup |
| `hiring_urgency` | Categorical | Low / Medium / High |
| `skills_python` | Binary | 1 if Python skill present |
| `skills_sql` | Binary | 1 if SQL skill present |
| `skills_ml` | Binary | 1 if ML skill present |
| `skills_deep_learning` | Binary | 1 if Deep Learning skill present |
| `skills_cloud` | Binary | 1 if Cloud skill present |
| `job_posting_month` | Numerical | Auto-filled from current date |
| `job_posting_year` | Numerical | Auto-filled from current date |
| `job_openings` | Numerical | Auto-imputed by transformer |

### Output
```json
{ "prediction": 95000.0 }
```

---

## 📊 Dataset

- **Source:** [AI and Data Science Job Market Dataset 2020–2026](https://www.kaggle.com/datasets/shree0910/ai-and-data-science-job-market-dataset-20202026)
- **Platform:** Kaggle
- **Coverage:** 2020 – 2026
- **Contents:** Job titles, salaries, skills, education levels, company details, hiring trends, and job posting patterns across global markets

---

## 💻 Installation & Local Setup

### Prerequisites
- Python 3.12+
- Docker (optional, for containerized run)
- Git

### 1. Clone the repository
```bash
git clone https://github.com/AsokTamang/salary-predictor.git
cd salary-predictor
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model (generates artifacts/)
```bash
python src/pipeline/train_pipeline.py
```

### 5. Run the application
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 6. Open in browser
```
http://localhost:8000
```

---

## 🐳 Run with Docker

```bash
# Build the image
docker build -t salary-predictor .

# Run the container
docker run -d -p 8000:8000 --name salary_prediction salary-predictor

# Open in browser
http://localhost:8000
```

---

## 🚀 Usage

1. Navigate to `http://localhost:8000`
2. Fill in your details:
   - Years of experience
   - Education level & experience level
   - Technical skills (Python, SQL, ML, Deep Learning, Cloud)
   - Job title, industry, country, remote type, company size
3. Click **"Predict Salary →"**
4. Your predicted salary is displayed instantly

---

## 🔁 CI/CD Pipeline

The project uses **GitHub Actions** for full automation:

```
Push to main branch
        ↓
✅ Job 1 — Continuous Integration (GitHub Runner)
   → Install dependencies
   → Lint code with Flake8
   → Run tests with Pytest
        ↓
✅ Job 2 — Continuous Delivery (GitHub Runner)
   → Build Docker image
   → Push image to AWS ECR
        ↓
✅ Job 3 — Continuous Deployment (Self-hosted EC2 Runner)
   → Pull latest image from ECR
   → Stop old container
   → Start new container on port 8000
```

Workflow file: `.github/workflows/aws.yml`

---

## ☁️ Deployment

The app is deployed on **AWS** using the following architecture:

```
GitHub Repo
    ↓  (GitHub Actions builds & pushes)
AWS ECR (Docker Image Registry)
    ↓  (Self-hosted runner pulls & runs)
AWS EC2 (Ubuntu, t2.micro or higher)
    ↓
Docker Container → FastAPI App → Port 8000
```

### AWS Services Used
- **ECR** — Stores the Docker image
- **EC2** — Hosts and runs the Docker container
- **IAM** — Manages access credentials for GitHub Actions

---

## 📸 Example Output

**Input:**
```
Experience: 5 years | Level: Senior | Education: Master
Skills: Python ✓, SQL ✓, ML ✓
Job: Data Scientist | Industry: Technology | Country: USA
Remote: Hybrid | Company: MNC
```

**Output:**
```
✦ Predicted Salary
$112,000
```

---



## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Your Name**
- 📧 Email:ashoktmg205@gmail.com
- 💼 LinkedIn: https://www.linkedin.com/in/asok-tamang11/
- 🐙 GitHub: https://github.com/AsokTamang
---

> ⭐ If you found this project useful, please give it a star on GitHub — it helps a lot!
