# 🏋️ Fitness AI: Intelligent Workout & Calorie Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-16.0-black.svg)](https://nextjs.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange.svg)](https://scikit-learn.org/)
[![Flask](https://img.shields.io/badge/Flask-Latest-green.svg)](https://flask.palletsprojects.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue.svg)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A comprehensive machine learning solution for personalized fitness recommendations, calorie prediction, and weight management with a modern Next.js frontend interface.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Machine Learning Models](#-machine-learning-models)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Results](#-results)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**Fitness AI** is an end-to-end machine learning system designed to revolutionize personal fitness management. The platform combines advanced ML algorithms with an intuitive web interface to provide:

- **Accurate Calorie Burn Prediction**: Predict calories burned based on workout parameters and user physiology
- **Weight Management Forecasting**: Estimate future weight based on workout plans and dietary habits
- **Intelligent Workout Recommendations**: ML-powered workout suggestions tailored to individual goals
- **Dynamic Weekly Planning**: Generate personalized weekly workout schedules with exercise details

### Problem Statement

Modern fitness apps lack personalization and data-driven insights. Users need:
- Accurate calorie burn predictions based on their unique physiology
- Personalized workout recommendations aligned with their fitness goals
- Scientific weight management forecasting
- Real-time predictions with interpretable results

### Solution Impact

- **80%+ accuracy** in workout recommendations
- **R² > 0.7** for calorie prediction models
- **Real-time predictions** (< 500ms response time)
- **Interpretable models** for user trust and transparency

---

## ✨ Features

### Machine Learning Capabilities

- **🔥 Calorie Prediction**
  - Multiple regression models (Gradient Boosting, Linear Regression, SVM)
  - Feature engineering with BMI, heart rate metrics, and workout parameters
  - Hyperparameter optimization for maximum accuracy

- **📊 Weight Forecasting**
  - Physics-based calculations combined with ML predictions
  - Time-series weight trajectory modeling
  - Accounts for workout effects and caloric deficit/surplus

- **💪 Workout Recommendations**
  - ML-based classification for optimal workout selection
  - Considers user goals (weight loss, muscle gain, maintenance)
  - Factors in experience level, gender, and body composition

### Frontend Features

- **📱 Modern Responsive UI**
  - Built with Next.js 16 and Tailwind CSS
  - Mobile-first design approach
  - Dark mode support

- **📈 Interactive Dashboards**
  - Model performance comparison visualizations
  - Real-time prediction interfaces
  - Weekly workout plan generator with PDF export

- **🎨 User-Friendly Forms**
  - Intuitive input forms for user metrics
  - Instant feedback and validation
  - Progress tracking and history

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Frontend (Next.js)                  │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │  Prediction  │  │   Dashboard  │  │  Weekly   │ │
│  │  Interface   │  │   Analytics  │  │  Planner  │ │
│  └──────┬───────┘  └──────┬───────┘  └─────┬─────┘ │
└─────────┼──────────────────┼────────────────┼───────┘
          │                  │                │
          └──────────────────┼────────────────┘
                             │
                    ┌────────▼────────┐
                    │   Flask API     │
                    │  (Port 5000)    │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
    ┌─────▼─────┐     ┌─────▼──────┐    ┌─────▼──────┐
    │  Calorie  │     │   Weight   │    │  Workout   │
    │Prediction │     │ Prediction │    │Recommender │
    │   Model   │     │   Model    │    │   Model    │
    └───────────┘     └────────────┘    └────────────┘
```

### Data Flow

1. **User Input** → Frontend form submission
2. **API Request** → Next.js sends data to Flask backend
3. **Preprocessing** → Feature engineering and data transformation
4. **Model Inference** → Trained models generate predictions
5. **Response** → Results returned to frontend
6. **Visualization** → Interactive charts and recommendations displayed

---

## 🤖 Machine Learning Models

### 1. Calorie Prediction Model

**Objective**: Predict calories burned during workout sessions

**Features**:
- Age, Weight, Height, BMI
- Heart Rate Metrics (Avg BPM, Resting BPM, Max BPM)
- Session Duration
- Fat Percentage
- Workout Frequency
- Experience Level
- Workout Type (Categorical)

**Models Evaluated**:
- ✅ **Gradient Boosting Regressor** (Best Performance)
  - R² Score: 0.9872
  - RMSE: 45.23
  - MAE: 32.15
- Linear Regression
  - R² Score: 0.8543
  - RMSE: 152.34
  - MAE: 118.67
- Support Vector Regression (SVM)
  - R² Score: 0.8921
  - RMSE: 131.45
  - MAE: 98.32

**Pipeline**:
```
OneHotEncoder (Workout_Type) → Feature Scaling → Gradient Boosting → Prediction
```

### 2. Weight Prediction Model

**Objective**: Forecast future weight based on workout plans

**Methodology**:
- Physics-based caloric deficit calculations
- Integration of workout effects over time
- Step count impact modeling
- Workout type-specific adjustments

**Features**:
- Current weight and target weight
- Days ahead for prediction
- Daily step count
- Workout type and frequency
- Caloric burn rate

### 3. Workout Recommendation Model

**Objective**: Recommend optimal workout type based on user profile

**Models**: 
- Gradient Boosting Classifier
- Random Forest Classifier
- Logistic Regression
- Support Vector Classifier

**Features**:
- User goal (lose weight, gain muscle, maintain)
- Gender
- BMI and body composition
- Experience level
- Available workout duration

**Output**: Ranked workout recommendations with confidence scores

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask**: REST API framework
- **scikit-learn**: Machine learning library
- **pandas & numpy**: Data manipulation
- **joblib**: Model serialization
- **matplotlib & seaborn**: Data visualization

### Frontend
- **Next.js 16**: React framework for production
- **React 19**: UI library
- **TypeScript**: Type-safe development
- **Tailwind CSS 4**: Utility-first styling
- **jsPDF**: PDF generation for workout plans

### Data & Models
- **Datasets**: Synthetic gym member exercise tracking data (1800+ entries)
- **Model Storage**: Pickle files (.pkl) for trained models
- **Data Processing**: Comprehensive cleaning and feature engineering pipeline

---

## 📁 Project Structure

```
ML_Fitness_Project/
│
├── 📊 datasets/
│   ├── gym_members_exercise_tracking_synthetic_data.csv
│   ├── fitness_dataset.csv
│   ├── GYM.csv
│   └── weightlifting_721_workouts.csv
│
├── 📓 notebook/
│   ├── fitness_ai_project.ipynb         # Main ML notebook
│   │
│   ├── deployment/
│   │   └── api.py                        # Flask API server
│   │
│   ├── saved_models/
│   │   ├── calories_gradient_boosting.pkl
│   │   ├── weight_prediction.pkl
│   │   ├── recommendation_ml.pkl
│   │   └── cleaned_dataset.pkl
│   │
│   ├── latex_tables/
│   │   └── model_comparison.tex
│   │
│   └── report_images/
│
├── 🎨 frontend-nextjs/
│   ├── app/
│   │   ├── page.tsx                      # Home page
│   │   ├── predict/page.tsx              # Calorie prediction
│   │   ├── weight/page.tsx               # Weight forecasting
│   │   ├── recommend/page.tsx            # Rule-based recommendations
│   │   ├── recommend-ml/page.tsx         # ML recommendations
│   │   ├── weeklyworkout/page.tsx        # Weekly planner
│   │   └── ml-results/page.tsx           # Model comparison
│   │
│   ├── components/
│   │   ├── FitnessApp.tsx                # Main app component
│   │   ├── CaloriesForm.tsx              # Prediction form
│   │   ├── WeightForm.tsx                # Weight prediction form
│   │   ├── ModelResults.tsx              # Model analytics
│   │   ├── DynamicWeeklyPlan.tsx         # Weekly plan generator
│   │   └── ...
│   │
│   ├── lib/
│   │   └── api.ts                        # API client utilities
│   │
│   ├── package.json
│   └── next.config.ts
│
└── 📄 README.md
```

---

## 🚀 Installation

### Prerequisites

- **Python 3.8+** installed
- **Node.js 18+** and npm/yarn
- **Git** for cloning the repository

### Step 1: Clone the Repository

```bash
git clone https://github.com/akramnemri/ML_Fitness_Project.git
cd ML_Fitness_Project
```

### Step 2: Backend Setup

#### 2.1 Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 2.2 Install Python Dependencies

```bash
pip install flask pandas numpy scikit-learn joblib matplotlib seaborn
```

#### 2.3 Verify Models Exist

Ensure trained models are in `notebook/saved_models/`:
- `calories_gradient_boosting.pkl`
- `weight_prediction.pkl`
- `recommendation_ml.pkl`

If models are missing, run the Jupyter notebook:
```bash
cd notebook
jupyter notebook fitness_ai_project.ipynb
# Execute all cells to train and save models
```

### Step 3: Frontend Setup

```bash
cd frontend-nextjs

# Install dependencies
npm install
# or
yarn install
```

---

## 💻 Usage

### Running the Backend API

```bash
cd notebook/deployment
python api.py
```

The Flask API will start on `http://localhost:5000`

### Running the Frontend

In a new terminal:

```bash
cd frontend-nextjs

# Development mode
npm run dev
# or
yarn dev

# Production build
npm run build
npm start
```

The Next.js app will be available at `http://localhost:3000`

### Accessing the Application

1. **Home Dashboard**: `http://localhost:3000`
2. **Calorie Prediction**: Navigate to `/predict`
3. **Weight Forecasting**: Navigate to `/weight`
4. **ML Recommendations**: Navigate to `/recommend-ml`
5. **Weekly Planner**: Navigate to `/weeklyworkout`
6. **Model Analytics**: Navigate to `/ml-results`

---

## 📡 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Calorie Prediction
```http
POST /api/predict
Content-Type: application/json

{
  "Age": 25,
  "Weight (kg)": 70,
  "Height (m)": 1.75,
  "Avg_BPM": 140,
  "Resting_BPM": 65,
  "Session_Duration (hours)": 1.5,
  "Fat_Percentage": 18,
  "Workout_Frequency (days/week)": 4,
  "Experience_Level": 2,
  "BMI": 22.86,
  "Workout_Type": "Cardio"
}

Response:
{
  "prediction": 523.45,
  "model": "Gradient Boosting"
}
```

#### 2. Weight Prediction
```http
POST /api/predict-weight
Content-Type: application/json

{
  "current_weight": 75,
  "target_weight": 70,
  "days_ahead": 90,
  "avg_calories": 450,
  "steps": 8000,
  "workout_type": "HIIT"
}

Response:
{
  "predicted_weight": 71.2,
  "days_to_goal": 85,
  "trajectory": [75, 74.5, 74, ...]
}
```

#### 3. ML Workout Recommendation
```http
POST /api/recommend-ml
Content-Type: application/json

{
  "goal": "lose_weight",
  "gender": "Male",
  "current_weight": 80,
  "height": 1.78,
  "age": 30,
  "experience_level": 2
}

Response:
{
  "recommendations": [
    {
      "recommended_workout": "HIIT",
      "confidence": 0.87,
      "duration_hours": 1.0,
      "explanation": "Best for weight loss goals..."
    }
  ]
}
```

#### 4. Weekly Plan Generation
```http
POST /api/plan-week
Content-Type: application/json

{
  "user_id": "user123",
  "goal": "lose_weight",
  "ai_recommended": "HIIT"
}

Response:
{
  "plans": [{
    "week_plan": [
      {"day": "Monday", "workout": "HIIT", "duration": 1.0},
      {"day": "Tuesday", "workout": "Strength", "duration": 1.5},
      ...
    ],
    "daily_calorie_shift": -500
  }]
}
```

---

## 📊 Results

### Model Performance Comparison

| Model | R² Score | RMSE | MAE | Training Time |
|-------|----------|------|-----|---------------|
| **Gradient Boosting** | **0.9872** | **45.23** | **32.15** | 3.2s |
| Linear Regression | 0.8543 | 152.34 | 118.67 | 0.1s |
| SVM | 0.8921 | 131.45 | 98.32 | 8.7s |

### Key Insights

- **Gradient Boosting** achieved the highest accuracy with R² = 0.9872
- Model can predict calories within ±32 calories on average
- Feature importance analysis reveals:
  - Session Duration (28%)
  - Avg BPM (23%)
  - Weight (19%)
  - Workout Type (15%)
  - Other features (15%)

### Visualization Highlights

The notebook includes comprehensive visualizations:
- Univariate analysis of all features
- Multivariate correlation heatmaps
- Model comparison bar charts
- Residual plots and prediction accuracy
- Feature importance rankings

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint and Prettier for TypeScript/React code
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Team ML Fitness Project** - [akramnemri](https://github.com/akramnemri)

---

## 🙏 Acknowledgments

- Dataset inspired by synthetic gym member tracking data
- Built with scikit-learn machine learning library
- UI components powered by Next.js and Tailwind CSS
- Special thanks to the open-source community

---

## 📧 Contact

For questions, suggestions, or collaboration opportunities:

- **GitHub Issues**: [Create an issue](https://github.com/akramnemri/ML_Fitness_Project/issues)
- **Email**: Contact via GitHub profile

---

## 🔮 Future Enhancements

- [ ] Real-time exercise form detection using computer vision
- [ ] Integration with wearable fitness devices (Fitbit, Apple Watch)
- [ ] Social features for workout sharing and challenges
- [ ] Nutrition tracking and meal recommendations
- [ ] Mobile app development (React Native)
- [ ] Advanced time-series forecasting for progress tracking
- [ ] Deep learning models for image-based body composition analysis

---

<div align="center">

**⭐ Star this repository if you find it helpful! ⭐**

Made with ❤️ and 💪 by the ML Fitness Team

</div>