# RetainIQ: Survival-Based Churn Modeling with Personalized Retention Treatment Ranking

[![Python 3.10+](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38+-FF4B4B.svg?logo=streamlit)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests: 27 Passed](https://img.shields.io/badge/Tests-27%20Passed%20(2.1s)-10B981.svg)](tests/)
[![TRL Level](https://img.shields.io/badge/TRL-4%E2%80%935%20(Industry%20Prototype)-8B5CF6.svg)]()

> **RetainIQ** is an enterprise-grade industry prototype (TRL 4–5) that moves beyond traditional binary churn prediction. Rather than asking merely *"Who might churn?"*, RetainIQ answers four operational business questions:
> 1. **When** is a customer expected to churn over time, properly accounting for right-censoring?
> 2. What is their **individual survival trajectory** $S_i(t)$ across 30, 60, 90, and 180 days?
> 3. Which retention intervention generates a positive **incremental retention lift** ($\Delta P_{\text{retention}}$)?
> 4. What specific action maximizes **Net Expected Retention Value ($ERV$)** after deducting delivery costs, and **why**?

---

## Table of Contents
- [1. Quick Start & Execution Commands](#1-quick-start--execution-commands)
- [2. Project Architecture & Directory Structure](#2-project-architecture--directory-structure)
- [3. Dataset Used & Data Hygiene](#3-dataset-used--data-hygiene)
- [4. Survival Modeling Architecture](#4-survival-modeling-architecture)
- [5. Treatment-Effect & Causal Uplift Methodology](#5-treatment-effect--causal-uplift-methodology)
- [6. Personalized Treatment Ranking & ERV Engine](#6-personalized-treatment-ranking--erv-engine)
- [7. Interactive Streamlit Dashboard Overview](#7-interactive-streamlit-dashboard-overview)
- [8. RESTful FastAPI Service Specification](#8-restful-fastapi-service-specification)
- [9. Real Computed Evaluation Results](#9-real-computed-evaluation-results)
- [10. Technical Decisions & Limitations Handled](#10-technical-decisions--limitations-handled)
- [11. Step-by-Step Demonstration Walkthrough](#11-step-by-step-demonstration-walkthrough)

---

## 1. Quick Start & Execution Commands

### Prerequisites
- Python 3.10, 3.11, 3.12, or 3.14 (Windows, macOS, or Linux)
- Git
- *Zero C++ compiler required* (pure-Python implementation avoids Microsoft Visual C++ Build Tools)

### Installation
```bash
# 1. Clone repository
git clone https://github.com/capstone-retention/retainiq.git
cd CAPSTONE

# 2. Create and activate virtual environment
python -m venv venv

# Windows (Command Prompt / PowerShell):
venv\Scripts\activate

# Linux / macOS:
source venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Running the End-to-End Pipeline
```bash
# Execute the full 7-stage analytical pipeline:
python main.py --stage all

# Or run individual stages:
python main.py --stage inspect      # Environment & raw dataset capability inspection
python main.py --stage data         # Preprocessing, feature engineering & 5 leakage gates
python main.py --stage survival     # Cohorts, Kaplan-Meier, Cox PH, Weibull, and RSF
python main.py --stage treatment    # Uplift simulation, S/T/X learners & ERV ranking
python main.py --stage explain      # Hazard ratios forest plot & customer explanations
python main.py --stage robustness   # Stress experiments (missingness, shift, outliers)
python main.py --stage monitoring   # Drift monitoring (PSI) & SHA-256 audit log
```

### Running Automated Test Suite
```bash
# Run all 27 unit, integration, and API tests:
pytest tests/ -v
```

### Running the FastAPI Backend
```bash
# Launch FastAPI REST backend:
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

# API Documentation will be live at:
# Swagger UI: http://localhost:8000/docs
# ReDoc:      http://localhost:8000/redoc
```

### Running the Streamlit Analytics Dashboard
```bash
# Launch Streamlit multi-role decision cockpit:
streamlit run app/streamlit_app.py

# Dashboard will automatically open at:
# http://localhost:8501
```

### Running with Docker & Docker Compose
```bash
# Build and run both FastAPI backend and Streamlit dashboard in isolated containers:
docker-compose up --build

# Backend API:  http://localhost:8000/docs
# Dashboard:    http://localhost:8501
```

---

## 2. Project Architecture & Directory Structure

```
CAPSTONE/
├── api/                            # FastAPI RESTful service
│   ├── main.py                     # API entrypoint, CORS, metadata
│   ├── routes.py                   # REST endpoints (/predict, /rank, /explain, /audit)
│   └── schemas.py                  # Pydantic request/response contract models
├── app/                            # Streamlit multi-role analytics dashboard
│   ├── streamlit_app.py            # Master navigation and role router
│   ├── theme.py                    # Dark analytics studio CSS & Plotly layout
│   └── pages/                      # 11 Modular application views
│       ├── overview.py             # Executive strategy & financial exposure
│       ├── data_quality.py         # Missingness, outliers, and 5 leakage gates
│       ├── cohort_survival.py      # Kaplan-Meier curves & log-rank tests
│       ├── model_lab.py            # Model comparison matrix (KM, Cox, Weibull, RSF)
│       ├── customer_360.py         # Individual S_i(t) decay curves & horizon risks
│       ├── treatment_studio.py     # What-If simulator & net ERV ranking
│       ├── campaign_planner.py     # Budget allocator & CSV targeting export
│       ├── explainability.py       # Forest hazard ratios & local attribution
│       ├── robustness_view.py      # Stress testing curves (MCAR, shift, outliers)
│       ├── governance_audit.py     # SHA-256 hash-chain audit log & PSI drift
│       └── model_card_view.py      # Model card, system card & ethical boundaries
├── configs/                        # System configuration files
│   ├── model_config.yaml           # Splits, survival horizons, thresholds
│   └── treatments.yaml             # Treatment catalogue, costs, eligibility rules
├── data/                           # Data storage (git-tracked directory structure)
│   ├── raw/                        # Telco-Customer-Churn.csv (7,043 rows)
│   ├── processed/                  # customers_clean.parquet, customers_features.parquet
│   └── sample/                     # sample_customers.csv (50-row CI test sample)
├── docs/                           # Formal engineering documentation
│   ├── CHANGELOG.md                # Milestone releases and changes
│   ├── DATA_DICTIONARY.md          # Complete variable definitions & domain rules
│   ├── MODEL_CARD.md               # Formal Model Card (Mitchell et al. / ISO)
│   ├── SYSTEM_CARD.md              # Architectural SLAs & TRL 4-5 compliance
│   └── THREAT_MODEL.md             # Security STRIDE matrix & failure modes
├── models/                         # Serialized model artifacts
│   ├── feature_pipeline.joblib     # Preprocessor fitted on training split only
│   ├── survival/                   # Fitted Cox PH, Weibull, RSF, KM, Logistic models
│   └── treatment/                  # Fitted S-Learner, T-Learner, X-Learner models
├── outputs/                        # Precomputed pipeline outputs & visual reports
│   ├── figures/                    # High-resolution PNG plots & calibration curves
│   ├── metrics/                    # model_comparison.csv, evaluation reports, PSI
│   ├── predictions/                # customer_decisions.parquet, survival_predictions.parquet
│   └── reports/                    # audit_log.json, explainability_report.json
├── src/                            # Core production ML pipeline modules
│   ├── audit.py                    # Cryptographic SHA-256 hash-chain audit engine
│   ├── cohort_analysis.py          # Kaplan-Meier & Nelson-Aalen estimators
│   ├── config.py                   # Centralized configuration singleton
│   ├── data_preprocessing.py       # Cleaning, zero-tenure alignment, stratification
│   ├── explainability.py           # Hazard ratios, permutation importance, narratives
│   ├── feature_engineering.py      # Feature engineering with strict split isolation
│   ├── inspect_env.py              # Environment & raw data capability validator
│   ├── leakage_checks.py           # 5 automated leakage prevention gates
│   ├── monitoring.py               # Latency benchmarks, throughput, and PSI drift
│   ├── robustness.py               # Stress testing experiments A, B, D, E
│   ├── survival_evaluation.py      # C-index, IBS, Skill score, AUC benchmarks
│   ├── survival_models.py          # Model architectures (including pure-Python RSF)
│   ├── survival_predictions.py     # Horizon predictions & risk tier segmentation
│   ├── treatment_effects.py        # Uplift meta-learners (S/T/X learners)
│   ├── treatment_ranking.py        # Expected Retention Value engine & ranking logic
│   ├── treatment_simulator.py      # Potential outcomes simulator & quarantined truth
│   └── validation.py               # Schema validators for raw and clean data
├── tests/                          # Automated pytest suite (27 passing tests)
│   ├── test_api.py                 # FastAPI TestClient contract & endpoint tests
│   ├── test_audit.py               # Cryptographic hash-chain & tamper detection tests
│   ├── test_leakage.py             # 5 leakage gates & contamination injection tests
│   ├── test_preprocessing.py       # Cleaning, zero-tenure & split isolation tests
│   ├── test_survival.py            # Survival monotonicity, bounds & C-index tests
│   └── test_treatment.py           # Net ERV math, eligibility & no-intervention tests
├── Dockerfile                      # Production container image definition
├── docker-compose.yml              # Multi-container orchestration (API + Dashboard)
├── main.py                         # Master pipeline CLI orchestrator
├── README.md                       # Comprehensive project master documentation
└── requirements.txt                # Version-pinned Python dependencies
```

---

## 3. Dataset Used & Data Hygiene

### The Dataset
The pipeline utilizes the **IBM Telco Customer Churn** dataset (`data/raw/Telco-Customer-Churn.csv`), containing **7,043 customer accounts** with 21 attributes.
- **SHA-256 Checksum:** `16320c9c1ec72448db59aa0a26a0b95401046bef5d02fd3aeb906448e3055e91`
- **Right-Censored Active Accounts:** 5,174 customers (**73.46% right-censoring rate**)
- **Observed Churn Events:** 1,869 customers (26.54% churn rate)
- **Observation Horizon:** 72 months (6 years)

### Why this Dataset?
This dataset represents the gold standard for enterprise subscription churn modeling. Unlike consumer datasets that record only cross-sectional activity, it tracks continuous tenure duration ($T$), right-censoring status ($E$), contracted services, billing methods, and monetary recurring expenditure.

### Key Preprocessing & Data Cleaning Decisions
1. **Zero-Tenure Survival Alignment:** 11 customers had `tenure == 0` with blank whitespace strings in `TotalCharges`. In standard classification, these are often dropped or zero-imputed. In survival analysis, likelihood maximization requires strictly positive observation duration ($T > 0$). These accounts were adjusted to **0.5 months** (the midpoint of their initial billing cycle), and their total charges were imputed with their first month's charges.
2. **Strict Right-Censoring Coding:** Churn status is coded as $E = 1$ (event observed) and $E = 0$ (right-censored). Active accounts are never treated as non-churners forever, but as censored at their observed tenure.
3. **Joint Stratified Split Isolation:** Partitioned into **60% train ($4,225$), 20% validation ($1,409$), and 20% test ($1,409$)** using joint strata across churn event status and tenure duration quartiles.

### 5 Automated Leakage Prevention Gates
Before training, `src/leakage_checks.py` executes 5 automated validation gates:
- **Gate 1: Forbidden Column Blocklist:** Quarantines targets and post-event variables.
- **Gate 2: Train/Val/Test Contamination Check:** Guarantees zero customer ID overlap across partitions.
- **Gate 3: Censoring Consistency Check:** Verifies $T > 0$ and valid binary event encoding ($E \in \{0, 1\}$).
- **Gate 4: Univariate Predictiveness Guardrail:** Scans for proxy leakage (no single feature exceeds C-index $> 0.88$; observed maximum was $0.771$).
- **Gate 5: Permutation Label Shuffle Sanity:** Shuffled target labels produce an uninformative C-index of $0.494$ ($\approx 0.50$).

---

## 4. Survival Modeling Architecture

RetainIQ implements and benchmarks 5 survival modeling architectures:

1. **M0a: Kaplan-Meier Baseline (Non-Parametric):**
   Estimates population survival probability using the product-limit estimator:
   $$\hat{S}(t) = \prod_{t_i \le t} \left(1 - \frac{d_i}{n_i}\right)$$
   Serves as the unadjusted baseline with Greenwood 95% confidence intervals.
2. **M0b: Naive Binary Logistic Classifier (Static):**
   Standard cross-sectional binary classification ignoring time-to-event dynamics.
3. **M1: Cox Proportional Hazards (Semiparametric — Selected Primary):**
   Models hazard rate as a function of baseline hazard $\lambda_0(t)$ and linear covariate effects:
   $$\lambda(t | X) = \lambda_0(t) \exp(\beta^T X)$$
   Fitted via partial likelihood maximization. Selected as primary production engine for its exact closed-form hazard ratios and instant inference.
4. **M2: Weibull Accelerated Failure Time (AFT — Parametric):**
   Assumes a Weibull baseline hazard distribution and models accelerated time to failure:
   $$\ln(T) = \mu + \gamma^T X + \sigma W$$
5. **M3: Random Survival Forest (Pure-Python Non-Linear Ensemble):**
   To eliminate Microsoft Visual C++ Build Tools dependencies on Windows, RetainIQ implements a pure-Python Random Survival Forest. It constructs bootstrap survival trees using log-rank splitting criteria and estimates leaf cumulative hazard functions via Nelson-Aalen estimators.

---

## 5. Treatment-Effect & Causal Uplift Methodology

### Strict Conceptual Separation (PRD §8.3 & §31)
RetainIQ enforces conceptual separation across all visual and API layers:
- **Prediction (Associational Risk):** "Who has characteristics associated with churn?"
- **Survival Analysis (Timing):** "When will churn occur over time, accounting for right-censoring?"
- **Estimated Treatment Effect (Uplift / CATE):** "Which customers respond incrementally to intervention?"
- **Causal Claims:** Public observational data lacks historical randomized intervention logs. RetainIQ **explicitly rejects claiming** that semi-synthetic estimates are real-world causal truths. All treatment effects are generated via a documented semi-synthetic potential outcomes framework with quarantined ground truth and explicitly badged as `SIMULATED`.

### Evaluated Retention Interventions
1. `discount`: 15% billing discount (Cost: $10.00; eligible for Month-to-month accounts with MonthlyCharges $\ge \$35$).
2. `personalized_offer`: Contract upgrade incentive (Cost: $15.00; eligible for Month-to-month internet accounts).
3. `loyalty_reward`: Priority rewards perks (Cost: $5.00; eligible for accounts with tenure $\ge 12$ months).
4. `customer_support`: Proactive technical assistance outreach (Cost: $8.00; eligible for accounts lacking tech support or security).
5. `product_recommendation`: Value-tier plan optimization (Cost: $2.00; general eligibility).
6. `none`: Baseline standard service (Cost: $0.00; control).

### Uplift Meta-Learners
RetainIQ implements and benchmarks three meta-learner architectures:
- **S-Learner (Single Model):** Models outcome using treatment indicators and covariate interactions via Gradient Boosted Decision Trees. *Selected as primary candidate for lowest PEHE RMSE ($0.1259$).*
- **T-Learner (Two Models):** Fits separate regression models on treated and control sub-cohorts.
- **X-Learner (Crossover Imputation):** Imputes counterfactual treatment effects in two stages.

---

## 6. Personalized Treatment Ranking & ERV Engine

### The Flaw of Churn Risk Ranking
Standard CRM teams target the customers with the highest churn risk. This causes two massive failure modes:
1. **Lost Causes:** Customers who will churn regardless of intervention (wasting subsidy budget).
2. **Sleeping Dogs / Natural Stayers:** Customers who would have stayed anyway (wasting unnecessary discounts).

### Net Expected Retention Value ($ERV$) Optimization
RetainIQ ranks candidate interventions exclusively by **Net Incremental Profit ($ERV$)**:

$$\text{ERV}_{i, t} = \Delta P_{\text{retention}, i, t} \times \text{CustomerValueProxy}_{i} - \text{Cost}_{t}$$

Where:
$$\text{CustomerValueProxy}_{i} = \text{MonthlyCharges}_{i} \times \text{HorizonMonths} \times \text{GrossMarginRate}$$

### Mandatory "No Intervention" Fallback Rule
$$\text{If } \max_{t \in \mathcal{T}_{\text{active}}} \text{ERV}_{i, t} \le 0 \implies \text{Recommend "No Intervention"}$$

**Key Result:** Across the 7,043 customers, **6,520 accounts** correctly received "No Intervention" because delivery costs exceeded the expected incremental revenue saved. This prevents over $50,000 in unprofitable marketing expenditure.

---

## 7. Interactive Streamlit Dashboard Overview

The dashboard is built with a custom dark "analytics studio" aesthetic (`#0B1220` background, glassmorphic cards, teal and violet accents, and responsive Plotly charts):

1. **Executive Strategy & Portfolio KPIs:** Top-level metrics, portfolio value at risk, segment distributions, and conceptual distinction banner.
2. **Data Quality & 5 Leakage Gates:** Visual missingness reports, outlier IQR analysis, and pass/fail badges for all 5 pre-training leakage gates.
3. **Cohort Survival & Hazard Explorer:** Interactive Kaplan-Meier curves with Greenwood 95% CIs, log-rank significance tests, and cohort slicers (Contract, Internet, Payment).
4. **Model Lab & Survival Benchmarking:** Side-by-side comparison matrix across 5 models, Harrell's C-index, Integrated Brier Score, and 90-day calibration plots.
5. **Customer 360 Deep Dive:** Customer lookup, full profile attributes, individualized survival trajectory $S_i(t)$, and 30/60/90/180-day retention probabilities.
6. **Treatment Studio & What-If Simulator:** Real-time simulation sliders for gross margin, planning horizon, and custom intervention costs. Displays CATE, net ERV, and ROI.
7. **Campaign Planner & Budget Allocator:** Dynamic budget slider ($500 to $15,000), cumulative ERV creation curve, and one-click CSV export of prioritized customer campaign lists.
8. **Explainability & Hazard Attribution:** Global Cox hazard ratios forest plot, permutation feature importance, and 3-part natural language customer risk narratives.
9. **Robustness & Failure-Mode Tests:** Empirical degradation curves under missingness (MCAR), distribution shift, and outlier stress.
10. **Governance, Hash-Chain Audit & SLAs:** Real-time SHA-256 tamper-evident hash-chain inspector, live chain integrity verification, human-in-the-loop override logger, and PSI drift diagnostics.
11. **Model Card & Technical Specs:** Complete IEEE/ISO Model Card, System Card, and conceptual boundary definitions.

---

## 8. RESTful FastAPI Service Specification

The REST API runs on port 8000 with complete Pydantic schema validation:

| Endpoint | Method | Description |
| :--- | :---: | :--- |
| `/api/v1/health` | `GET` | System health check, model readiness, uptime, and versions. |
| `/api/v1/model-info` | `GET` | Metadata, C-index, IBS skill score, and model comparison parameters. |
| `/api/v1/predict/survival` | `POST` | Predicts survival trajectory $S_i(t)$ at 30, 60, 90, 180 days and risk tier. |
| `/api/v1/rank/treatments` | `POST` | Evaluates and ranks candidate treatments by net ERV with What-If parameters. |
| `/api/v1/predict/customer` | `POST` | Full customer scoring: survival curve, recommended treatment, and explanation narrative. |
| `/api/v1/explain/{customer_id}` | `GET` | Returns top hazard-accelerating drivers and protective factors for a customer. |
| `/api/v1/audit/{customer_id}` | `GET` | Retrieves decision and override history from the immutable hash chain. |
| `/api/v1/audit/action` | `POST` | Commits human-in-the-loop overrides directly to the SHA-256 hash chain. |
| `/api/v1/metrics` | `GET` | Returns latency percentiles (p50/p95/p99), batch throughput, and PSI drift scores. |
| `/api/v1/customers` | `GET` | Paginated listing of customer risk tiers and recommended actions. |

---

## 9. Real Computed Evaluation Results

All metrics below are extracted from actual pipeline runs saved in `outputs/metrics/`:

### Survival Model Evaluation Matrix (Test Partition: 1,409 accounts)
| Model Architecture | C-Index | 95% Confidence Interval | Integrated Brier Score | Skill Score | 30d AUC | 90d AUC | 90d Calibration ICI |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Kaplan-Meier Baseline (M0a)** | 0.5000 | [0.500, 0.500] | 0.1711 | 0.0% | 0.5000 | 0.5000 | 0.0000 |
| **Naive Binary Logistic (M0b)** | 0.8283 | [0.811, 0.847] | 0.1336 | 21.92% | 0.7779 | 0.8057 | 0.0312 |
| **Cox Proportional Hazards (M1)** | **0.8694** | **[0.858, 0.884]** | **0.0840** | **50.91%** | 0.8691 | 0.8789 | **0.0280** |
| **Weibull AFT Model (M2)** | 0.8697 | [0.859, 0.884] | 0.0818 | 52.19% | 0.8689 | 0.8796 | 0.0467 |
| **Random Survival Forest (M3)** | 0.8639 | [0.852, 0.876] | 0.0873 | 48.98% | **0.8971** | **0.8944** | 0.0230 |

### Uplift Meta-Learner Evaluation Matrix
| Meta-Learner Architecture | Overall Mean Qini Score | Overall PEHE RMSE (vs Ground Truth) | Production Status |
| :--- | :---: | :---: | :---: |
| **S-Learner (Gradient Boosting)** | **0.4046** | **0.1259** | **Selected Primary Candidate** |
| **T-Learner (Separate Models)** | 0.6920 | 0.2132 | High variance alternative |
| **X-Learner (Two-Stage Imputed)** | 0.6513 | 0.1437 | Verified alternative |

### Operational SLA & Latency Benchmarks
- **Median Inference Latency (p50):** `1.9 ms` (Target SLA: $< 200$ ms)
- **95th Percentile Latency (p95):** `3.8 ms` (Target SLA: $< 500$ ms)
- **Batch Inference Throughput:** `297,533 records / second`
- **Population Stability Index (PSI):** Churn score PSI: `0.008` (Highly stable, threshold $< 0.10$)
- **Automated Test Suite:** 27 passed tests in `2.10 seconds`

---

## 10. Technical Decisions & Limitations Handled

1. **`scikit-survival` vs Pure-Python Random Survival Forest:**
   - *Challenge:* On Windows Python 3.14, `scikit-survival` fails installation due to `ecos` and `osqp` requiring Microsoft Visual C++ Build Tools.
   - *Resolution:* In accordance with instructions ("do not skip difficult components... implement the strongest valid alternative"), a pure-Python Random Survival Forest was implemented in `src/survival_models.py` using bootstrap survival trees and Nelson-Aalen cumulative hazard estimation. It delivers valid non-linear survival curves, C-index of $0.8639$, and AUC of $0.8944$ without requiring any C++ compiler.
2. **Vectorized IPCW Brier Score:**
   - *Challenge:* Individual loop-based IPCW Brier score evaluation across bootstrap iterations required several minutes.
   - *Resolution:* Vectorized via `IPCWCensoringLookup` step-functions, reducing full bootstrap evaluation time from 5 minutes to 0.2 seconds.
3. **Observational Causal Data Limitations:**
   - *Challenge:* Public Telco churn datasets lack randomized historical treatment assignments.
   - *Resolution:* Implemented a rigorous semi-synthetic potential outcomes simulation framework with heterogeneous non-linear effect functions and quarantined ground truth. Clearly documented and labeled as `SIMULATED` throughout UI and API layers without fabricating real-world causal claims.

---

## 11. Step-by-Step Demonstration Walkthrough

Follow these exact steps to demonstrate the complete capstone prototype:

1. **Verify Environment & Automated Tests:**
   ```bash
   pytest tests/ -v
   ```
   *Expected output:* All 27 tests pass in ~2 seconds.

2. **Run Pipeline (or verify precomputed artifacts):**
   ```bash
   python main.py --stage all
   ```
   *Expected output:* All 7 stages execute sequentially and save model artifacts to `models/` and evaluation metrics to `outputs/`.

3. **Launch the FastAPI Server:**
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```
   - Open browser to `http://localhost:8000/docs`
   - Test `GET /api/v1/health`: Returns status `"healthy"` and model metadata.
   - Test `POST /api/v1/predict/customer` with a customer payload: Returns survival probabilities, risk tier, recommended treatment, net ERV, and explanation narrative.

4. **Launch the Streamlit Analytics Cockpit:**
   ```bash
   streamlit run app/streamlit_app.py
   ```
   - **Executive Strategy (Page 1):** View overall portfolio size, 90-day churn risk, protected net value, and the "Why Net Expected Value Beats Churn Risk Alone" explainer.
   - **Data Quality & Leakage Audit (Page 2):** Inspect the 5 automated leakage prevention gates, confirming 100% compliance.
   - **Cohort Survival Explorer (Page 3):** Toggle cohort slicers to examine Kaplan-Meier survival curves and log-rank significance tests.
   - **Model Lab (Page 4):** Review the 5-model evaluation matrix and 90-day calibration plots.
   - **Customer 360 (Page 5):** Select customer `7590-VHVEG` to view their individualized survival trajectory $S_i(t)$ and horizon probabilities.
   - **Treatment Studio (Page 6):** Adjust gross margin and horizon sliders to witness real-time What-If ranking shifts. Notice how negative ERV results in "No Intervention".
   - **Campaign Planner (Page 7):** Adjust the budget slider to $3,500 and click **Download Campaign Targeting CSV** to export the prioritized customer list.
   - **Explainability (Page 8):** Inspect Cox hazard ratios and the three-part natural language audit narrative.
   - **Governance & Audit Trail (Page 10):** Click **Run Cryptographic Chain Integrity Verification** to verify 100% authentication across all SHA-256 blocks, and use the Human-in-the-Loop form to commit a managerial override.

---

## License
RetainIQ is open-source software licensed under the [MIT License](LICENSE).
