# PRD --- Survival-Based Churn Modeling with Personalized Retention Treatment Ranking

## 1. Project Identification

**Project ID:** BDS-11\
**Project Title:** Survival-Based Churn Modeling with Personalized
Retention Treatment Ranking\
**Programme:** T.Y. B.Sc. Data Science --- Semester V\
**Team Size:** 1--3 students\
**Minimum Effort:** 100 hours per student\
**Target Maturity:** Industry Prototype --- TRL 4--5

This PRD converts the BDS-11 capstone requirements and the supplied
technical prompt into a complete build specification for a runnable,
interactive, stakeholder-testable machine-learning prototype.

------------------------------------------------------------------------

# 2. Executive Summary

The system will go beyond ordinary binary churn prediction.

A conventional churn model answers:

> "Is this customer likely to churn?"

This project must answer four more useful questions:

1.  **When is the customer likely to churn?**
2.  **How does the customer's probability of remaining active change
    over time?**
3.  **Which retention intervention is expected to create incremental
    retention value for this particular customer?**
4.  **What should a customer-success or marketing user do next, and
    why?**

The product therefore combines:

-   customer cohort analysis,
-   data-quality and leakage controls,
-   survival analysis,
-   churn-risk segmentation,
-   individual survival prediction,
-   explainable predictive modeling,
-   treatment-effect/uplift estimation,
-   personalized treatment ranking,
-   expected-value decision logic,
-   interactive dashboard,
-   API/inference layer,
-   audit trail,
-   operational monitoring,
-   robustness/failure testing,
-   reproducible deployment.

The central conceptual separation must remain explicit:

**Prediction ≠ survival probability ≠ treatment effect ≠ causal
effect.**

A high predicted churn risk does not automatically mean that a
particular intervention will work. The treatment-ranking layer must use
estimated incremental treatment effect, not churn probability alone.

------------------------------------------------------------------------

# 3. Problem Statement

Subscription and customer-success teams often use binary churn models
that classify customers as "churn" or "not churn." Such models have
important limitations:

-   they do not estimate *when* churn may occur;
-   active customers are often censored rather than genuinely observed
    until churn;
-   treating censored customers as ordinary non-churners can bias
    analysis;
-   intervention decisions are often based on risk rather than
    incremental treatment impact;
-   historical treatment-response data can contain confounding and
    selection bias;
-   post-churn or post-treatment variables can create severe leakage;
-   a model may identify high-risk customers without identifying the
    best action for each customer.

BDS-11 requires a working prototype that addresses these issues and
demonstrates an end-to-end workflow from data/event intake to
prediction, intervention decision, user action, audit trail, and
operational monitoring.

------------------------------------------------------------------------

# 4. Product Goal

Build an attractive, interactive, production-oriented web application
that allows an authorized user to:

1.  inspect the customer/cohort population;
2.  understand data quality and survival patterns;
3.  compare survival models;
4.  inspect customer-level churn timing and survival probability;
5.  identify risk segments;
6.  simulate or evaluate retention interventions;
7.  rank interventions for a selected customer;
8.  inspect treatment-effect reasoning and confidence;
9.  understand predictive explanations without making unsupported causal
    claims;
10. record/approve a recommended action;
11. inspect model and system monitoring evidence.

------------------------------------------------------------------------

# 5. Target Users and Personas

## 5.1 Customer Success Manager

Needs: - customer risk level; - expected churn timing; - customer
survival curve; - recommended intervention; - expected incremental
value; - explanation that can be communicated to stakeholders.

## 5.2 Marketing/Retention Analyst

Needs: - cohort survival curves; - treatment-effect distributions; -
intervention ranking; - lift/uplift analysis; - segment comparison; -
campaign scenario analysis.

## 5.3 Data Scientist / Model Engineer

Needs: - model comparison; - survival metrics; - calibration; - feature
importance/SHAP; - leakage diagnostics; - treatment-model diagnostics; -
experiment configuration; - reproducible runs.

## 5.4 Project Evaluator / Faculty Reviewer

Needs: - clear methodology; - reproducible execution; - evidence of
engineering work; - baseline comparison; - robustness testing; -
explainability; - system card/model card; - documentation and
limitations.

------------------------------------------------------------------------

# 6. Scope

## In Scope

-   public subscription/customer-churn dataset acquisition;
-   customer-level survival dataset construction;
-   data cleaning and validation;
-   missing-value analysis;
-   outlier analysis;
-   EDA;
-   cohort analysis;
-   feature engineering;
-   temporal/leakage checks;
-   survival modeling;
-   churn-risk prediction;
-   30/60/90/180-day survival estimates;
-   median/expected survival where statistically appropriate;
-   risk segmentation;
-   treatment/intervention framework;
-   uplift/treatment-effect estimation;
-   personalized treatment ranking;
-   expected retention value calculation;
-   explainability;
-   interactive dashboard;
-   prediction API;
-   audit logging;
-   testing;
-   monitoring;
-   reproducible deployment;
-   model/system documentation.

## Out of Scope

-   claiming that simulated treatment effects are real causal effects;
-   automatic deployment of real customer campaigns;
-   using sensitive personal information unnecessarily;
-   pretending that a dataset contains genuine treatment history when it
    does not;
-   treating censored observations as churned;
-   fabricating model performance;
-   fabricating treatment effects;
-   fabricating customer-level predictions;
-   using dashboard visuals as a substitute for model evaluation.

------------------------------------------------------------------------

# 7. Success Criteria

The prototype is successful when it can demonstrate:

### Functional

-   customer data can be loaded and validated;
-   survival data can be generated without obvious leakage;
-   at least one meaningful survival baseline and one advanced survival
    model can be compared;
-   individual survival curves can be generated;
-   30/60/90/180-day survival probabilities can be returned where the
    time scale supports those horizons;
-   customers can be assigned risk segments;
-   treatments can be represented and ranked;
-   ranking uses incremental treatment effect rather than raw churn
    risk;
-   expected retention value is calculated;
-   explanations are available;
-   dashboard interactions update customer/cohort views;
-   recommendation decisions are auditable.

### Evaluation

The system must report, where applicable:

-   concordance index;
-   time-horizon calibration;
-   integrated Brier score;
-   time-dependent AUC;
-   uplift/lift metrics;
-   ranking stability;
-   treatment-effect distribution;
-   subgroup/edge-case results;
-   failure-mode results;
-   latency/resource measurements where practical.

### Engineering

-   clean-machine setup works;
-   fixed random seeds are used;
-   tests pass;
-   no secrets are committed;
-   logs exist;
-   model artifacts are versioned;
-   configuration is separated from code;
-   containerized execution is available;
-   README explains setup and execution.

------------------------------------------------------------------------

# 8. Dataset Strategy

## 8.1 Primary Dataset

Use a suitable public telecom/subscription churn dataset with:

-   customer ID;
-   tenure;
-   churn/event indicator;
-   demographic features;
-   subscription/service features;
-   transaction/billing information;
-   account information.

A practical starting dataset is the **IBM Telco Customer Churn** dataset
because it contains customer identifiers, tenure, churn status,
contract/service variables, billing/payment variables, and customer
attributes.

The project must record:

-   original source;
-   source URL in project documentation;
-   license/usage terms;
-   download date;
-   checksum/version if available;
-   data dictionary;
-   transformation history.

## 8.2 Critical Dataset Limitation

The common Telco churn dataset does **not** provide genuine
intervention/treatment assignment and does not provide a true event
calendar suitable for precise real-world 30/60/90/180-day forecasting.

Therefore the project must **not** claim that it contains genuine
retention treatment effects.

The methodology must explicitly separate:

### Observed information

-   tenure;
-   churn status;
-   customer attributes;
-   services;
-   billing/subscription information.

### Constructed survival information

Tenure can be used as an observed duration from subscription start to
either:

-   churn event, or
-   right-censoring at the observation snapshot.

This is a defensible survival representation for an educational
prototype, but it must be labelled as a limitation because the dataset
does not expose exact churn dates.

### Constructed treatment information

Because genuine randomized retention treatment data are unavailable, the
intervention layer will use a **semi-synthetic treatment framework**.

The semi-synthetic layer must:

1.  retain the real customer's observed pre-treatment features;
2.  define a finite intervention catalogue;
3.  generate treatment assignment using a documented assignment
    mechanism;
4.  use a transparent, pre-specified outcome/treatment-effect simulator;
5.  create known simulated heterogeneous effects;
6.  train/evaluate uplift models against the simulated ground truth;
7.  report simulated results as **method-validation evidence**, not real
    customer causal evidence.

No simulated treatment effect may be presented as a measured effect in
the real telecom dataset.

------------------------------------------------------------------------

# 9. Survival-Time Construction

## 9.1 Event Definition

`event = 1` means the observed customer is labelled as churned.

`event = 0` means the customer remains active in the observed dataset
and is therefore right-censored.

## 9.2 Duration

Use:

`duration = tenure`

when tenure represents months observed from account start to
churn/censoring.

Document clearly that this is a duration-in-months representation rather
than a true event-date timeline.

## 9.3 Censoring Rule

Never convert active customers into churned customers simply because
they have no churn record.

Active customers remain:

`event = 0`

and contribute survival information through their observed duration.

## 9.4 Horizon Conversion

If the source duration is monthly, convert horizons consistently:

-   30 days ≈ 1 month;
-   60 days ≈ 2 months;
-   90 days ≈ 3 months;
-   180 days ≈ 6 months.

The UI must display the actual time unit used by the model.

If the available data cannot validly support a horizon, return `N/A`
with an explanation rather than fabricating a probability.

------------------------------------------------------------------------

# 10. Data Schema

Create a canonical feature table.

## Customer Table

  Field                    Type          Purpose
  ------------------------ ------------- -----------------------
  customer_id              string        unique identifier
  tenure_months            numeric       observed duration
  event_churn              binary        churn/event indicator
  gender                   categorical   demographic feature
  senior_citizen           binary        demographic feature
  partner                  categorical   household feature
  dependents               categorical   household feature
  phone_service            categorical   service feature
  multiple_lines           categorical   service feature
  internet_service         categorical   service feature
  online_security          categorical   service feature
  online_backup            categorical   service feature
  device_protection        categorical   service feature
  tech_support             categorical   service feature
  streaming_tv             categorical   service feature
  streaming_movies         categorical   service feature
  contract                 categorical   subscription feature
  paperless_billing        categorical   billing feature
  payment_method           categorical   billing feature
  monthly_charges          numeric       monetary feature
  total_charges            numeric       monetary feature
  engineered_features...   mixed         derived features

## Treatment Table

For the semi-synthetic module:

  Field                    Purpose
  ------------------------ ----------------------------------------
  customer_id              customer key
  treatment                assigned intervention
  assignment_probability   propensity used for simulation
  observed_outcome         simulated outcome
  counterfactual_outcome   simulator ground truth where available
  treatment_cost           intervention cost
  simulated_effect         known effect used only for validation

------------------------------------------------------------------------

# 11. Data Cleaning Pipeline

Implement the following sequence:

1.  Load raw data.
2.  Normalize column names.
3.  Remove exact duplicate rows.
4.  Check duplicate customer IDs.
5.  Parse numeric fields safely.
6.  Convert blank strings to missing values.
7.  Inspect missingness by column.
8.  Identify impossible values.
9.  Validate tenure ranges.
10. Validate charges.
11. Check churn/event consistency.
12. Encode categorical variables.
13. Impute only within the training pipeline where appropriate.
14. Scale numerical variables only when required.
15. Preserve a clean immutable raw-data copy.
16. Save processed data with version metadata.

------------------------------------------------------------------------

# 12. Missing-Value Analysis

Produce:

-   missing-value count table;
-   missing-value percentage;
-   missingness visualization;
-   treatment strategy for each feature;
-   post-cleaning validation.

Avoid blindly filling every field with a mean.

For categorical variables, use a meaningful `"Unknown"` category where
appropriate.

For numerical variables, use training-only imputation.

------------------------------------------------------------------------

# 13. Outlier Analysis

Inspect:

-   tenure;
-   monthly charges;
-   total charges;
-   engineered monetary features.

Use:

-   IQR diagnostics;
-   percentile analysis;
-   domain validity checks.

Do not automatically delete legitimate high-value customers.

Outlier treatment must be documented.

------------------------------------------------------------------------

# 14. Feature Engineering

Create features that are available before the prediction decision.

Examples:

### Tenure features

-   tenure_months;
-   tenure_bucket;
-   early_lifecycle flag.

### Billing features

-   monthly-to-total-charge ratio where meaningful;
-   average implied monthly charge;
-   billing/payment category.

### Service complexity

-   number of subscribed services;
-   security-service count;
-   streaming-service count;
-   support-service flag.

### Contract features

-   month-to-month flag;
-   long-term contract flag;
-   paperless billing flag.

### Customer profile

-   household indicator;
-   dependent/partner combinations.

Feature engineering must be reviewed for leakage.

------------------------------------------------------------------------

# 15. Leakage Prevention

This is a mandatory project component.

## 15.1 Temporal Leakage

Do not use variables that would only become known after the prediction
point.

## 15.2 Post-Churn Leakage

Do not use information generated after churn.

## 15.3 Treatment Leakage

Do not use treatment assignment or post-treatment response as an input
to the pre-treatment treatment-effect model.

## 15.4 Target Leakage

Do not derive features directly from the churn label.

## 15.5 Train/Test Contamination

Fit:

-   imputers;
-   scalers;
-   encoders;
-   feature selectors;
-   hyperparameter optimizers

only on training data.

## 15.6 Validation Strategy

Prefer temporal/out-of-sample validation when a valid time field exists.

For the supplied tenure-only dataset, document why a true temporal split
is unavailable and use a reproducible stratified/group-safe holdout as
the strongest available alternative.

------------------------------------------------------------------------

# 16. Exploratory Data Analysis

The EDA notebook/module must contain:

1.  class/event distribution;
2.  tenure distribution;
3.  monthly charges distribution;
4.  contract distribution;
5.  churn by contract;
6.  churn by tenure bucket;
7.  churn by payment method;
8.  churn by service combinations;
9.  cohort survival patterns;
10. correlation/association analysis;
11. missingness;
12. outlier diagnostics.

EDA must be descriptive and must not be presented as causal evidence.

------------------------------------------------------------------------

# 17. Cohort Analysis

Create cohorts using available customer lifecycle information.

Suggested cohorts:

-   0--6 months;
-   7--12 months;
-   13--24 months;
-   25--48 months;
-   49+ months.

Also support segmentation by important categorical variables such as:

-   contract;
-   internet service;
-   support status;
-   customer value band.

The dashboard should allow users to select a segment and compare
survival curves.

------------------------------------------------------------------------

# 18. Survival Analysis Architecture

The survival layer must contain at least:

1.  Kaplan--Meier baseline;
2.  Cox Proportional Hazards;
3.  Random Survival Forest.

A neural survival model is optional and should only be added if data
size, complexity, and validation justify it.

------------------------------------------------------------------------

# 19. Kaplan--Meier Model

Purpose:

-   non-parametric population survival baseline;
-   cohort comparison;
-   intuitive visualization.

Outputs:

-   overall survival curve;
-   median survival where estimable;
-   confidence interval;
-   survival curve by selected segments.

Do not interpret Kaplan--Meier curves as causal treatment effects.

------------------------------------------------------------------------

# 20. Cox Proportional Hazards

Use Cox PH as the interpretable model.

Outputs:

-   hazard ratios;
-   individual survival functions;
-   risk score;
-   feature coefficients;
-   confidence intervals where available.

Check the proportional hazards assumption.

If an important feature violates the assumption, document the issue and
consider:

-   stratification;
-   time-varying effect;
-   alternative survival model.

------------------------------------------------------------------------

# 21. Random Survival Forest

Use Random Survival Forest as a non-linear survival baseline/advanced
model.

It can capture:

-   nonlinear relationships;
-   feature interactions;
-   threshold effects.

Compare it against Cox PH rather than assuming it is superior.

------------------------------------------------------------------------

# 22. Optional Neural Survival Model

Only implement if justified by:

-   adequate sample size;
-   meaningful nonlinear structure;
-   measurable validation benefit;
-   manageable project complexity.

Possible implementation:

-   PyTorch-based discrete-time survival model;
-   DeepSurv-style Cox model.

If it does not provide validated additional value, keep it optional and
document why it was excluded.

------------------------------------------------------------------------

# 23. Survival Outputs

For each customer produce:

-   survival probability at 30 days;
-   survival probability at 60 days;
-   survival probability at 90 days;
-   survival probability at 180 days;
-   corresponding churn probability;
-   risk segment;
-   individual survival curve;
-   expected survival time where statistically appropriate;
-   median survival time where estimable.

For each horizon:

`churn_probability(t) = 1 - survival_probability(t)`

Do not report a horizon probability if the model/data cannot support
that horizon.

------------------------------------------------------------------------

# 24. Risk Segmentation

Create understandable segments, for example:

-   Lower observed risk;
-   Moderate risk;
-   Elevated risk;
-   High risk.

Thresholds must be based on documented validation/business criteria
rather than arbitrary visual impressions.

The UI should show the threshold configuration.

Risk segment is a predictive classification and must not be confused
with treatment responsiveness.

------------------------------------------------------------------------

# 25. Survival Model Evaluation

## Required Metrics

### Concordance Index

Measures ranking quality of predicted risk relative to observed event
ordering while accounting for censoring.

### Integrated Brier Score

Measures probabilistic prediction error over a time range and is useful
for evaluating survival probability quality.

### Time-Dependent AUC

Measures discrimination at particular time horizons where appropriate.

### Calibration by Horizon

Compare predicted survival/churn probabilities with observed outcomes
using suitable survival-aware calibration methodology.

Report:

-   30-day calibration;
-   60-day calibration;
-   90-day calibration;
-   180-day calibration

only where supported.

------------------------------------------------------------------------

# 26. Baseline Comparison

The project must include at least one meaningful baseline.

Recommended baselines:

1.  majority/naive churn baseline;
2.  logistic regression churn classifier;
3.  standard tree-based binary churn model.

The purpose is to demonstrate why survival modeling provides additional
information beyond binary classification.

Compare:

-   discrimination;
-   calibration;
-   timing information;
-   interpretability;
-   operational usefulness.

Do not claim that survival models are universally better.

------------------------------------------------------------------------

# 27. Treatment Catalogue

Create a configurable intervention catalogue.

Initial treatments:

1.  Discount / incentive
2.  Personalized offer
3.  Loyalty reward
4.  Customer-support intervention
5.  Product/service recommendation
6.  No intervention

Each treatment must have:

-   treatment name;
-   description;
-   cost;
-   eligibility rules;
-   expected operational constraints;
-   simulated treatment-effect mechanism if using semi-synthetic data.

Example configuration:

``` yaml
treatments:
  discount:
    cost: 10
  personalized_offer:
    cost: 5
  loyalty_reward:
    cost: 8
  customer_support:
    cost: 3
  product_recommendation:
    cost: 1
  no_intervention:
    cost: 0
```

Values are configuration examples only and must not be presented as
observed business costs.

------------------------------------------------------------------------

# 28. Treatment-Data Decision Tree

The application must inspect whether genuine treatment/outcome data are
available.

## Case A --- Genuine Treatment Data Available

Use appropriate causal/uplift methodology.

Candidate methods:

-   S-learner;
-   T-learner;
-   X-learner;
-   causal forest;
-   uplift modeling.

Select based on:

-   treatment structure;
-   sample size;
-   treatment balance;
-   outcome availability;
-   overlap/positivity;
-   model assumptions.

## Case B --- No Genuine Treatment Data

Use the semi-synthetic treatment framework.

The UI and report must clearly label treatment effects as simulated.

Never describe these as real-world causal effects.

------------------------------------------------------------------------

# 29. Semi-Synthetic Treatment Methodology

This is the preferred approach for the likely public churn dataset.

## Step 1 --- Start With Real Pre-Treatment Features

Use only features available before intervention.

## Step 2 --- Estimate Baseline Retention Risk

Use the trained survival model to obtain a baseline retention/survival
signal.

## Step 3 --- Define Heterogeneous Effect Functions

Define transparent treatment-effect functions based on pre-treatment
characteristics.

Example conceptual rule:

-   support intervention effect may be higher for customers with
    support-related service signals;
-   discount effect may vary by price sensitivity;
-   loyalty reward effect may vary by tenure/contract profile.

These rules must be documented before training/evaluation.

## Step 4 --- Simulate Treatment Assignment

Assign treatments using known probabilities with controlled overlap.

Do not make every high-risk customer receive the same treatment.

## Step 5 --- Simulate Potential Outcomes

For each customer, generate potential outcomes under:

-   no intervention;
-   treatment 1;
-   treatment 2;
-   etc.

Keep the simulator's true effects hidden from the learner during model
fitting.

## Step 6 --- Evaluate Uplift

Because the simulator has known counterfactual ground truth, evaluate
whether the uplift model can recover heterogeneous effects.

This makes the innovation layer testable without falsely claiming
real-world causal evidence.

------------------------------------------------------------------------

# 30. Causal/Uplift Modeling

Where genuine randomized or well-designed observational treatment data
exist, estimate:

`ITE_i,t = E[Y_i(t) - Y_i(control) | X_i]`

where `ITE` is the individual treatment effect.

Possible implementation sequence:

### S-Learner

Single model with treatment indicator.

### T-Learner

Separate outcome model per treatment.

### X-Learner

Useful when treatment groups are imbalanced and sample size permits.

### Causal Forest

Use when nonlinear heterogeneous effects are expected and sufficient
data are available.

Do not automatically implement all methods. Compare a simple baseline
against the selected advanced approach.

------------------------------------------------------------------------

# 31. Treatment Evaluation

Required evidence should include:

-   treatment balance;
-   propensity/assignment distribution;
-   overlap/positivity diagnostics;
-   uplift/lift curves;
-   treatment-effect distribution;
-   top-k incremental gain;
-   ranking stability;
-   subgroup performance;
-   sensitivity to simulation assumptions where applicable.

For semi-synthetic data, additionally compare estimated effects against
known simulator effects.

------------------------------------------------------------------------

# 32. Personalized Treatment Ranking

For every customer-treatment pair calculate:

`Expected Retention Value = Incremental Retention Probability × Customer Value − Treatment Cost`

More explicitly:

`ERV(i,t) = ΔP_retention(i,t,H) × CustomerValue(i,H) − Cost(t)`

where:

-   `i` = customer;
-   `t` = treatment;
-   `H` = selected horizon;
-   `ΔP_retention` = estimated incremental retention probability;
-   `CustomerValue` = defined business-value estimate;
-   `Cost` = intervention cost.

The system must not rank treatments using churn probability alone.

------------------------------------------------------------------------

# 33. Customer Value

If reliable customer lifetime value data are unavailable, use a
transparent proxy such as:

-   monthly charges;
-   normalized revenue proxy;
-   configurable value band.

Label this explicitly as a proxy.

Do not call it true CLV unless a validated CLV methodology is actually
implemented.

------------------------------------------------------------------------

# 34. Treatment Ranking Rules

For each customer:

1.  calculate baseline retention;
2.  calculate estimated treatment effect for each eligible treatment;
3.  convert effect to incremental retention probability;
4.  calculate expected customer value;
5.  subtract treatment cost;
6.  calculate confidence/uncertainty;
7.  filter ineligible actions;
8.  rank remaining treatments;
9.  include no-intervention as a valid alternative;
10. return top recommendation plus alternatives.

If all treatments have negative expected value, the system should be
allowed to recommend:

**No intervention**

rather than forcing an action.

------------------------------------------------------------------------

# 35. Confidence and Uncertainty

The final output includes `confidence`.

Confidence must not be an arbitrary score.

Preferred approaches:

-   prediction interval width;
-   bootstrap uncertainty;
-   treatment-model uncertainty;
-   model agreement;
-   sample support/overlap;
-   calibrated probability confidence.

The UI should explain the confidence basis.

Example:

> High confidence because the customer is within strong training-data
> support and the treatment-effect estimate is stable across bootstrap
> samples.

Do not claim statistical certainty when it is not available.

------------------------------------------------------------------------

# 36. Final Customer Output Schema

Required fields:

``` text
customer_id
churn_risk
survival_30d
survival_90d
survival_180d
recommended_treatment
treatment_effect
expected_value
confidence
```

Recommended additional fields:

``` text
survival_60d
risk_segment
median_survival
value_proxy
alternative_treatment_1
alternative_treatment_2
treatment_rank
model_version
prediction_timestamp
explanation_summary
```

------------------------------------------------------------------------

# 37. Customer Decision Explanation

For every recommendation show three separate explanations.

## Predictive explanation

Why does the model consider the customer at elevated risk?

Example:

-   short tenure;
-   month-to-month contract;
-   high monthly charges;
-   limited support services.

## Survival explanation

How does the customer's predicted survival change over time?

## Treatment explanation

Why did treatment A have greater estimated incremental value than
treatment B?

The system must not say:

> "This feature caused the customer to churn."

Instead use:

> "This feature is associated with higher predicted churn risk in the
> predictive model."

For treatment effects, only use causal language when the data/design
support it.

------------------------------------------------------------------------

# 38. Explainability

Implement:

-   SHAP for compatible predictive models;
-   model coefficients/hazard ratios for Cox;
-   permutation/feature importance for survival forest;
-   partial dependence where appropriate;
-   local customer explanation;
-   global feature importance.

Explainability must distinguish:

-   association/prediction;
-   survival relationship;
-   treatment-effect estimate.

------------------------------------------------------------------------

# 39. Dashboard Design

Use **Streamlit** for the primary interactive prototype.

Optional:

-   FastAPI backend;
-   Power BI reporting layer if required separately.

The dashboard should look like a modern analytics product rather than a
notebook.

------------------------------------------------------------------------

# 40. Dashboard Navigation

## Page 1 --- Executive Overview

Show:

-   total customers;
-   churn/event rate;
-   active/censored population;
-   median/summary survival where estimable;
-   high-risk customer count;
-   average predicted survival;
-   treatment opportunity count;
-   model version;
-   last run timestamp.

Charts:

-   overall Kaplan--Meier curve;
-   churn-risk distribution;
-   survival by cohort;
-   risk-segment distribution.

------------------------------------------------------------------------

# 41. Page 2 --- Cohort & Survival Explorer

Controls:

-   cohort selector;
-   contract selector;
-   service selector;
-   risk segment selector;
-   model selector.

Charts:

-   Kaplan--Meier survival curve;
-   confidence bands;
-   segment survival comparison;
-   hazard/risk visualization.

------------------------------------------------------------------------

# 42. Page 3 --- Customer 360

Search by customer ID.

Show:

-   customer profile;
-   subscription details;
-   tenure;
-   charges;
-   services;
-   churn risk;
-   survival probabilities;
-   individual survival curve;
-   risk segment;
-   top predictive factors;
-   recommended treatment;
-   treatment ranking table;
-   expected value;
-   confidence;
-   explanation.

Example treatment table:

  -----------------------------------------------------------------------------
  Rank       Treatment     Incremental          Cost      Expected Confidence
                             Retention                       Value 
  ---------- ----------- ------------- ------------- ------------- ------------
  1          ...                   ...           ...           ... ...

  2          ...                   ...           ...           ... ...

  3          ...                   ...           ...           ... ...
  -----------------------------------------------------------------------------

------------------------------------------------------------------------

# 43. Page 4 --- Treatment Intelligence

Show:

-   treatment-effect distribution;
-   uplift/lift curve;
-   treatment ranking distribution;
-   average simulated incremental effect;
-   expected-value distribution;
-   treatment opportunity by segment;
-   no-intervention rate.

Add warnings when treatment effects are simulated.

------------------------------------------------------------------------

# 44. Page 5 --- Model Evaluation

Show:

-   model comparison;
-   concordance index;
-   integrated Brier score;
-   time-dependent AUC;
-   calibration by horizon;
-   survival prediction error;
-   baseline comparison.

Allow download of evaluation results.

------------------------------------------------------------------------

# 45. Page 6 --- Explainability

Show:

-   global feature importance;
-   SHAP summary;
-   customer-level SHAP;
-   Cox hazard ratios;
-   treatment-effect drivers;
-   uncertainty indicators.

------------------------------------------------------------------------

# 46. Page 7 --- Data Quality & Leakage

Show:

-   missing values;
-   duplicate records;
-   invalid values;
-   outlier diagnostics;
-   feature leakage flags;
-   train/test overlap checks;
-   treatment overlap;
-   censoring summary.

This page is important evidence for the capstone evaluation.

------------------------------------------------------------------------

# 47. Page 8 --- Operations / Audit

Show:

-   model version;
-   dataset version;
-   run ID;
-   timestamp;
-   prediction count;
-   error count;
-   latency summary;
-   audit events;
-   active configuration;
-   application health.

Never expose secrets.

------------------------------------------------------------------------

# 48. Interaction Requirements

The dashboard must be genuinely interactive.

Minimum interactions:

-   customer search;
-   cohort filters;
-   segment filters;
-   model selection;
-   treatment horizon selector;
-   treatment cost/value configuration;
-   survival-curve hover/tooltips;
-   treatment ranking drill-down;
-   downloadable customer prediction;
-   downloadable evaluation report.

UI changes must update dependent visualizations rather than simply
changing labels.

------------------------------------------------------------------------

# 49. Visual Design

Recommended design:

-   clean dark/light professional analytics theme;
-   KPI cards;
-   clear typography;
-   restrained chart palette;
-   consistent treatment colors;
-   risk badges;
-   warning banners;
-   expandable explanation panels;
-   tooltips;
-   responsive layout;
-   minimal clutter.

Avoid excessive decorative charts.

Every chart must answer a business/model question.

------------------------------------------------------------------------

# 50. Architecture

Recommended architecture:

``` text
                 ┌─────────────────────────┐
                 │ Public / Simulated Data │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │ Data Validation & EDA   │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │ Feature Engineering     │
                 │ + Leakage Checks        │
                 └────────────┬────────────┘
                              │
                  ┌───────────┴───────────┐
                  ▼                       ▼
       ┌────────────────────┐   ┌────────────────────┐
       │ Survival Modeling  │   │ Treatment Modeling │
       │ KM / Cox / RSF     │   │ Uplift / Simulator │
       └─────────┬──────────┘   └─────────┬──────────┘
                 │                        │
                 └───────────┬────────────┘
                             ▼
                 ┌─────────────────────────┐
                 │ Treatment Ranking       │
                 │ Expected Value Engine   │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │ Prediction / Audit API  │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │ Streamlit Dashboard     │
                 └─────────────────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │ Logs / Metrics / Models │
                 └─────────────────────────┘
```

------------------------------------------------------------------------

# 51. Recommended Repository Structure

``` text
survival-churn/
│
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── README.md
│
├── notebooks/
│   ├── 01_data_audit.ipynb
│   ├── 02_eda_cohort_analysis.ipynb
│   ├── 03_survival_models.ipynb
│   ├── 04_treatment_simulation.ipynb
│   ├── 05_uplift_models.ipynb
│   └── 06_evaluation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── leakage_checks.py
│   ├── cohort_analysis.py
│   ├── survival_models.py
│   ├── survival_evaluation.py
│   ├── treatment_simulator.py
│   ├── treatment_effects.py
│   ├── treatment_ranking.py
│   ├── explainability.py
│   ├── evaluation.py
│   ├── monitoring.py
│   └── utils.py
│
├── app/
│   ├── streamlit_app.py
│   ├── pages/
│   │   ├── overview.py
│   │   ├── survival.py
│   │   ├── customer_360.py
│   │   ├── treatments.py
│   │   ├── evaluation.py
│   │   ├── explainability.py
│   │   ├── data_quality.py
│   │   └── operations.py
│   └── components/
│
├── api/
│   ├── main.py
│   ├── schemas.py
│   └── routes.py
│
├── models/
│   ├── survival/
│   ├── treatment/
│   └── metadata/
│
├── outputs/
│   ├── figures/
│   ├── predictions/
│   ├── metrics/
│   └── reports/
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_survival.py
│   ├── test_treatment.py
│   ├── test_ranking.py
│   └── test_api.py
│
├── configs/
│   ├── treatments.yaml
│   └── model_config.yaml
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── MODEL_CARD.md
├── SYSTEM_CARD.md
├── THREAT_MODEL.md
├── DATA_DICTIONARY.md
├── CHANGELOG.md
└── main.py
```

------------------------------------------------------------------------

# 52. Python Technology Stack

Core:

-   Python 3.11+
-   pandas
-   numpy
-   scikit-learn
-   lifelines
-   scikit-survival
-   matplotlib
-   seaborn
-   shap

Potential:

-   XGBoost or LightGBM;
-   statsmodels;
-   scipy;
-   Optuna;
-   MLflow;
-   FastAPI;
-   Pydantic;
-   Streamlit;
-   pytest;
-   joblib;
-   Docker.

Use the smallest dependency set that satisfies the validated
architecture.

------------------------------------------------------------------------

# 53. Main Execution Flow

`main.py` should orchestrate:

``` text
1. Load configuration
2. Load raw data
3. Validate data
4. Clean data
5. Run leakage checks
6. Engineer features
7. Build survival dataset
8. Split data
9. Train baseline
10. Train Kaplan–Meier
11. Train Cox PH
12. Train Random Survival Forest
13. Evaluate survival models
14. Select production candidate based on documented criteria
15. Generate individual survival predictions
16. Build treatment simulator if real treatment data unavailable
17. Train/evaluate uplift model
18. Calculate treatment effects
19. Calculate expected retention value
20. Rank treatments
21. Generate explanations
22. Save model artifacts
23. Save predictions
24. Save metrics
25. Launch dashboard/API
```

------------------------------------------------------------------------

# 54. Model Selection Policy

Do not choose a model simply because it produces the highest single
metric.

Selection must consider:

-   discrimination;
-   calibration;
-   Brier score;
-   stability;
-   interpretability;
-   computational cost;
-   edge-case behavior;
-   reproducibility.

The chosen model and selection rationale must be written to the
evaluation report.

------------------------------------------------------------------------

# 55. Reproducibility

Use a fixed seed, for example:

``` python
RANDOM_STATE = 42
```

Record:

-   Python version;
-   package versions;
-   dataset version;
-   preprocessing configuration;
-   model hyperparameters;
-   random seed;
-   training timestamp;
-   model version.

------------------------------------------------------------------------

# 56. Experiment Tracking

Use MLflow if practical.

Track:

-   experiment name;
-   run ID;
-   parameters;
-   model type;
-   metrics;
-   dataset version;
-   artifact paths;
-   feature version;
-   treatment-simulation configuration.

If MLflow is omitted for simplicity, maintain an equivalent structured
experiment log.

------------------------------------------------------------------------

# 57. API Requirements

If FastAPI is used, expose endpoints such as:

``` text
GET  /health
GET  /model-info
POST /predict/survival
POST /predict/customer
POST /rank/treatments
POST /explain/customer
GET  /metrics
GET  /audit/{customer_id}
```

Example customer prediction request:

``` json
{
  "customer_id": "1234",
  "features": {
    "tenure_months": 8,
    "contract": "Month-to-month"
  }
}
```

The API must validate inputs and return structured errors.

------------------------------------------------------------------------

# 58. Security and Privacy

Required:

-   no personal secrets in repository;
-   `.env` excluded from Git;
-   environment variables for credentials;
-   input validation;
-   safe file handling;
-   no arbitrary code execution from user input;
-   de-identified customer identifiers;
-   role-aware access where API deployment supports it;
-   audit logs;
-   dependency scanning.

The application should use synthetic/demo customer identifiers in
screenshots and presentations.

------------------------------------------------------------------------

# 59. Threat Model

Document threats such as:

-   malicious file upload;
-   malformed prediction input;
-   unauthorized prediction access;
-   model artifact tampering;
-   exposure of customer attributes;
-   log leakage;
-   dependency vulnerabilities;
-   denial-of-service through oversized input.

For each threat document:

-   likelihood;
-   impact;
-   mitigation;
-   residual risk.

------------------------------------------------------------------------

# 60. Audit Trail

Every recommendation should have:

``` text
audit_id
customer_id
timestamp
model_version
data_version
risk_score
survival_predictions
treatment_candidates
treatment_effects
expected_values
selected_treatment
selection_reason
user/action status
```

This creates the required operational path:

**data → model → decision → user action → audit**

------------------------------------------------------------------------

# 61. Operational Monitoring

Monitor:

-   input row count;
-   missingness;
-   schema drift;
-   prediction distribution;
-   risk-segment distribution;
-   survival probability distribution;
-   treatment ranking distribution;
-   API latency;
-   API errors;
-   model version;
-   data version.

Where ground truth becomes available later, monitor:

-   calibration drift;
-   discrimination drift;
-   treatment-response drift.

------------------------------------------------------------------------

# 62. Failure Modes

The application must gracefully handle:

-   empty dataset;
-   missing required columns;
-   duplicate IDs;
-   invalid tenure;
-   all customers censored;
-   all customers churned;
-   insufficient event count;
-   horizon beyond supported data;
-   missing customer ID;
-   unknown customer;
-   treatment model without overlap;
-   unsupported treatment;
-   missing model artifact;
-   malformed API request.

Example:

> "180-day survival is unavailable because the training data do not
> contain sufficient support beyond this horizon."

Do not silently fabricate a value.

------------------------------------------------------------------------

# 63. Robustness Experiments

At least one failure-mode/security/robustness experiment is mandatory.

Recommended experiments:

### Experiment A --- Missing Data Stress

Randomly remove selected feature values and measure prediction
degradation.

### Experiment B --- Feature Distribution Shift

Perturb important numerical features and measure survival/ranking
stability.

### Experiment C --- Treatment Imbalance

Simulate unequal treatment assignment and inspect uplift degradation.

### Experiment D --- Overlap Failure

Reduce treatment overlap and demonstrate why causal estimates become
unstable.

### Experiment E --- Outlier Stress

Inject controlled outliers and compare model sensitivity.

Results must be reported rather than hidden.

------------------------------------------------------------------------

# 64. Error Analysis

Review:

-   false high-risk predictions;
-   false low-risk predictions;
-   poorly calibrated horizons;
-   unstable treatment rankings;
-   customers with low training support;
-   unusual feature combinations.

Create a failure-analysis table:

  Case   Expected   Model   Error   Likely Cause   Action
  ------ ---------- ------- ------- -------------- --------

------------------------------------------------------------------------

# 65. Subgroup Analysis

Where meaningful, compare model behavior across groups such as:

-   contract type;
-   tenure bucket;
-   service type;
-   customer-value band.

Avoid unnecessary sensitive-attribute analysis unless required and
ethically justified.

Check:

-   calibration;
-   discrimination;
-   prediction stability;
-   treatment-ranking stability.

Do not claim fairness merely because subgroup metrics were calculated.

------------------------------------------------------------------------

# 66. Evaluation Acceptance Thresholds

Thresholds must be defined before final reporting and may be adjusted
only with documented justification.

Recommended categories:

### Survival model

-   acceptable discrimination;
-   acceptable calibration;
-   stable performance across validation splits;
-   no critical leakage.

### Treatment model

-   treatment overlap adequate;
-   uplift better than a simple baseline where applicable;
-   ranking stable under resampling;
-   simulated-effect recovery documented.

### Product

-   dashboard loads;
-   customer search works;
-   recommendation is reproducible;
-   API responds with validation;
-   logs are generated.

Exact numeric thresholds must be chosen after inspecting dataset size
and baseline performance; they must not be invented as achieved results.

------------------------------------------------------------------------

# 67. No-Fabrication Rule

The project must never hard-code or invent:

-   c-index values;
-   AUC values;
-   Brier scores;
-   treatment effects;
-   uplift gains;
-   customer predictions;
-   business ROI;
-   causal effects.

All numbers shown in the final report must come from actual execution.

Demo screenshots may use clearly labelled example/simulated outputs.

------------------------------------------------------------------------

# 68. Model Card

Create `MODEL_CARD.md` containing:

-   model purpose;
-   intended users;
-   training data;
-   feature description;
-   target/event definition;
-   censoring approach;
-   model architecture;
-   validation method;
-   metrics;
-   limitations;
-   known failure modes;
-   explainability;
-   fairness/subgroup analysis;
-   treatment-data limitations;
-   version.

------------------------------------------------------------------------

# 69. System Card

Create `SYSTEM_CARD.md` containing:

-   system purpose;
-   architecture;
-   components;
-   data flow;
-   APIs;
-   dashboard;
-   user roles;
-   security;
-   privacy;
-   auditability;
-   monitoring;
-   limitations;
-   human oversight.

------------------------------------------------------------------------

# 70. Data Dictionary

Create `DATA_DICTIONARY.md` documenting every feature:

-   name;
-   type;
-   source;
-   meaning;
-   allowed values;
-   missingness;
-   transformation;
-   leakage status;
-   model usage.

------------------------------------------------------------------------

# 71. README Requirements

README must contain:

1.  project overview;
2.  problem statement;
3.  architecture;
4.  dataset source;
5.  dataset limitation;
6.  survival methodology;
7.  treatment methodology;
8.  installation;
9.  execution;
10. dashboard startup;
11. API startup;
12. testing;
13. model evaluation;
14. screenshots;
15. limitations;
16. reproducibility;
17. project structure.

------------------------------------------------------------------------

# 72. Clean-Machine Installation

Example:

``` bash
git clone <repository>
cd survival-churn

python -m venv .venv
```

Windows:

``` bash
.venv\Scripts\activate
```

macOS/Linux:

``` bash
source .venv/bin/activate
```

Then:

``` bash
pip install -r requirements.txt
```

Run the pipeline:

``` bash
python main.py
```

Run Streamlit:

``` bash
streamlit run app/streamlit_app.py
```

Run tests:

``` bash
pytest
```

Run API if implemented:

``` bash
uvicorn api.main:app --reload
```

The final README must use the actual commands that work in the finished
repository.

------------------------------------------------------------------------

# 73. Containerization

Provide a Dockerfile.

Example workflow:

``` bash
docker build -t survival-churn .
docker run -p 8501:8501 survival-churn
```

The exact command must match the final container configuration.

The project should be runnable either:

-   directly in a clean Python environment, or
-   through a reproducible container.

------------------------------------------------------------------------

# 74. CI/CD

A basic CI pipeline should:

1.  install dependencies;
2.  run linting where configured;
3.  run unit tests;
4.  run integration tests;
5.  validate imports;
6.  run a lightweight pipeline smoke test.

Optional:

-   dependency vulnerability scan;
-   Docker build;
-   artifact validation.

------------------------------------------------------------------------

# 75. Testing Strategy

## Unit Tests

Test:

-   cleaning;
-   feature engineering;
-   censoring logic;
-   horizon calculations;
-   treatment-effect calculation;
-   expected-value calculation;
-   ranking logic.

## Integration Tests

Test:

-   raw data → processed data;
-   processed data → model;
-   model → predictions;
-   predictions → treatment ranking;
-   API → prediction response;
-   dashboard → saved artifacts.

## Regression Tests

Ensure future code changes do not alter:

-   schema;
-   ranking logic;
-   prediction format;
-   model artifact loading.

------------------------------------------------------------------------

# 76. Example Ranking Logic

Pseudo-code:

``` python
for customer in customers:

    baseline = predict_survival(customer)

    for treatment in eligible_treatments(customer):

        effect = estimate_treatment_effect(
            customer,
            treatment
        )

        incremental_retention = convert_effect_to_retention_delta(
            effect
        )

        expected_value = (
            incremental_retention
            * customer_value(customer)
            - treatment.cost
        )

        confidence = estimate_confidence(
            customer,
            treatment,
            effect
        )

        store_result(
            customer,
            treatment,
            effect,
            expected_value,
            confidence
        )

    rank = sort_by_expected_value()

    if best_expected_value <= 0:
        recommendation = "No intervention"
    else:
        recommendation = rank[0]
```

The exact statistical implementation must follow the selected
treatment-effect methodology.

------------------------------------------------------------------------

# 77. Recommended Module Responsibilities

## `data_preprocessing.py`

-   load;
-   validate;
-   clean;
-   encode;
-   impute;
-   save processed dataset.

## `feature_engineering.py`

-   create domain features;
-   document transformations;
-   ensure prediction-time availability.

## `leakage_checks.py`

-   identify post-event fields;
-   target leakage;
-   treatment leakage;
-   train/test overlap.

## `survival_models.py`

-   Kaplan--Meier;
-   Cox PH;
-   Random Survival Forest;
-   optional neural model.

## `survival_evaluation.py`

-   c-index;
-   Brier score;
-   time-dependent AUC;
-   calibration.

## `treatment_simulator.py`

-   treatment catalogue;
-   assignment mechanism;
-   potential outcomes;
-   simulator ground truth.

## `treatment_effects.py`

-   S/T/X learner;
-   selected advanced method;
-   effect estimation.

## `treatment_ranking.py`

-   effect-to-retention conversion;
-   expected value;
-   confidence;
-   ranking.

## `explainability.py`

-   SHAP;
-   feature importance;
-   local explanations.

## `monitoring.py`

-   logs;
-   metrics;
-   drift/input checks;
-   operational health.

------------------------------------------------------------------------

# 78. Agile Backlog

## Epic 1 --- Discovery

-   define stakeholders;
-   define personas;
-   define misuse cases;
-   define scope;
-   define success criteria.

## Epic 2 --- Data

-   acquire dataset;
-   document provenance;
-   build data dictionary;
-   clean;
-   validate;
-   EDA.

## Epic 3 --- Survival

-   implement KM;
-   implement Cox;
-   implement RSF;
-   evaluate;
-   generate survival predictions.

## Epic 4 --- Treatment

-   design treatment catalogue;
-   implement simulator;
-   implement uplift baseline;
-   implement advanced uplift;
-   validate treatment effects.

## Epic 5 --- Decision Engine

-   customer value;
-   expected retention value;
-   treatment ranking;
-   confidence;
-   explanation.

## Epic 6 --- Product

-   Streamlit dashboard;
-   customer search;
-   cohort explorer;
-   treatment explorer;
-   model evaluation.

## Epic 7 --- Engineering

-   API;
-   tests;
-   logging;
-   monitoring;
-   Docker;
-   CI. 

## Epic 8 --- Documentation

-   README;
-   model card;
-   system card;
-   threat model;
-   final report;
-   presentation;
-   demo video.

------------------------------------------------------------------------

# 79. Workload Plan

For each student, target at least 100 hours.

Recommended distribution:

  Work                                                         Hours
  -------------------------------------------------------- ---------
  Problem discovery, validation, backlog                          15
  Architecture, UI/data design, technical spike                   15
  Owned module implementation + unit testing                      40
  Integration, security, performance, acceptance testing          15
  Deployment, documentation, demo, viva preparation               15
  **Total**                                                  **100**

For a 3-person team, ownership should be demonstrable rather than merely
dividing slides.

Suggested roles:

### Student 1 --- Data & Survival

-   acquisition;
-   preprocessing;
-   EDA;
-   cohort analysis;
-   survival models.

### Student 2 --- Treatment & ML

-   simulator;
-   uplift;
-   treatment ranking;
-   explainability;
-   evaluation.

### Student 3 --- Product & Engineering

-   Streamlit;
-   API;
-   testing;
-   monitoring;
-   Docker/CI;
-   documentation.

------------------------------------------------------------------------

# 80. Demonstration Flow

The 5--8 minute demonstration should show a complete story.

## 0:00--0:45 --- Problem

Explain why binary churn prediction is insufficient.

## 0:45--1:30 --- Data

Show dataset, cohort structure, censoring, and limitations.

## 1:30--2:30 --- Survival

Show Kaplan--Meier, Cox/RSF comparison, and horizon predictions.

## 2:30--3:30 --- Customer 360

Select a customer and show:

-   risk;
-   survival curve;
-   explanation.

## 3:30--4:30 --- Treatment Ranking

Show multiple interventions and:

-   estimated incremental effect;
-   cost;
-   expected value;
-   confidence;
-   recommendation.

## 4:30--5:30 --- Evaluation

Show:

-   c-index;
-   calibration;
-   Brier score;
-   uplift/lift;
-   robustness.

## 5:30--6:30 --- Engineering

Show:

-   API;
-   audit trail;
-   logs;
-   tests;
-   Docker/CI.

## 6:30--8:00 --- Limitations

Explicitly explain:

-   dataset limitations;
-   simulated treatment limitation;
-   censoring limitations;
-   causal inference limitations;
-   intended human oversight.

------------------------------------------------------------------------

# 81. Key Business Interpretation

The product should help a stakeholder move from:

> "This customer looks risky."

to:

> "This customer has an estimated survival trajectory, and among the
> eligible actions, this intervention has the highest estimated
> incremental retention value under the model assumptions."

The second statement is only a causal claim when the treatment
data/design justify it.

For the semi-synthetic implementation, the wording must instead be:

> "This intervention ranks highest under the simulated
> treatment-response framework."

------------------------------------------------------------------------

# 82. Critical Methodological Rules

1.  Never treat censored customers as churned.
2.  Never use post-churn variables.
3.  Never use post-treatment variables for pre-treatment effect
    estimation.
4.  Never rank treatments using churn probability alone.
5.  Always include no intervention.
6.  Always document treatment-data limitations.
7.  Never call simulated effects real causal effects.
8.  Never fabricate metrics.
9.  Keep predictive and causal reasoning separate.
10. Prefer out-of-sample validation.
11. Use reproducible random seeds.
12. Document all assumptions.
13. Show uncertainty where possible.
14. Provide human-readable explanations.
15. Keep an audit trail.
16. Protect customer data and secrets.

------------------------------------------------------------------------

# 83. Required Visualizations Checklist

The final project must include:

-   [ ] overall Kaplan--Meier survival curve;
-   [ ] survival curves by important customer segments;
-   [ ] feature importance;
-   [ ] churn-risk distribution;
-   [ ] treatment-effect distribution;
-   [ ] treatment-ranking distribution;
-   [ ] customer-level survival curves;
-   [ ] calibration plots;
-   [ ] model comparison;
-   [ ] uplift/lift plot;
-   [ ] missing-value visualization;
-   [ ] cohort analysis;
-   [ ] robustness/error-analysis visualization where useful.

------------------------------------------------------------------------

# 84. Final Deliverables Checklist

## Product

-   [ ] working Streamlit dashboard;
-   [ ] optional FastAPI service;
-   [ ] customer search;
-   [ ] cohort explorer;
-   [ ] treatment ranking;
-   [ ] explainability;
-   [ ] evaluation page;
-   [ ] audit/operations page.

## Data

-   [ ] public dataset;
-   [ ] provenance;
-   [ ] data dictionary;
-   [ ] cleaned data pipeline;
-   [ ] leakage analysis.

## Models

-   [ ] Kaplan--Meier;
-   [ ] Cox PH;
-   [ ] Random Survival Forest;
-   [ ] binary churn baseline;
-   [ ] treatment simulator if necessary;
-   [ ] uplift/treatment-effect model;
-   [ ] treatment ranking engine.

## Evaluation

-   [ ] c-index;
-   [ ] integrated Brier score;
-   [ ] time-dependent AUC where appropriate;
-   [ ] calibration;
-   [ ] uplift/lift;
-   [ ] stability;
-   [ ] robustness;
-   [ ] failure analysis.

## Engineering

-   [ ] tests;
-   [ ] logging;
-   [ ] monitoring;
-   [ ] API validation;
-   [ ] Docker;
-   [ ] CI;
-   [ ] dependency/security checks.

## Documentation

-   [ ] README;
-   [ ] MODEL_CARD.md;
-   [ ] SYSTEM_CARD.md;
-   [ ] THREAT_MODEL.md;
-   [ ] DATA_DICTIONARY.md;
-   [ ] final report;
-   [ ] presentation;
-   [ ] 5--8 minute demo;
-   [ ] individual contribution evidence.

------------------------------------------------------------------------

# 85. Industry Acceptance Gates

The finished project must satisfy the following BDS-11 gates:

### Gate 1 --- Not a Dashboard-Only Project

The system must contain genuine data engineering, survival modeling,
treatment-effect methodology, evaluation, and engineering evidence.

### Gate 2 --- Meaningful Baseline

At least one meaningful baseline comparison must be included.

### Gate 3 --- Failure/Security/Robustness Experiment

At least one documented failure-mode, security, or robustness experiment
must be included.

### Gate 4 --- Reproducibility

The project must run from documented instructions on a clean machine or
reproducible container.

### Gate 5 --- Operational Evidence

Provide appropriate:

-   logs;
-   metrics;
-   traces;
-   monitoring evidence.

### Gate 6 --- AI/Analytics Controls

Include:

-   leakage checks;
-   reproducible splits;
-   baseline models;
-   explainability;
-   error analysis;
-   model/system card.

### Gate 7 --- Original Engineering

The project must not be merely:

-   a copied notebook;
-   a CRUD portal;
-   a dashboard-only submission;
-   an API wrapper with no original modeling/engineering.

------------------------------------------------------------------------

# 86. Recommended Implementation Order

Build in this exact order to reduce project risk.

### Phase 1

Inspect environment and dataset.

### Phase 2

Create raw/processed data pipeline.

### Phase 3

Implement EDA and cohort analysis.

### Phase 4

Implement leakage checks.

### Phase 5

Implement binary churn baseline.

### Phase 6

Implement Kaplan--Meier.

### Phase 7

Implement Cox PH.

### Phase 8

Implement Random Survival Forest.

### Phase 9

Evaluate survival models.

### Phase 10

Generate customer-level survival predictions.

### Phase 11

Build treatment catalogue and simulator.

### Phase 12

Implement simple uplift baseline.

### Phase 13

Implement selected advanced uplift method.

### Phase 14

Validate treatment effects.

### Phase 15

Implement expected-value engine.

### Phase 16

Implement personalized treatment ranking.

### Phase 17

Implement explainability.

### Phase 18

Build Streamlit dashboard.

### Phase 19

Add API, logging, audit trail, monitoring.

### Phase 20

Add tests, Docker, CI, threat model, system/model cards.

### Phase 21

Run final clean-environment validation.

### Phase 22

Generate actual metrics, figures, predictions, and final documentation.

------------------------------------------------------------------------

# 87. Definition of Done

The project is complete only when:

-   the application runs;
-   the dataset pipeline runs;
-   survival models train successfully;
-   model metrics are generated from actual execution;
-   customer survival predictions are generated;
-   treatment ranking works;
-   no-intervention is supported;
-   treatment limitations are visible;
-   explanations work;
-   dashboard interactions work;
-   audit records are produced;
-   tests pass;
-   robustness experiment is complete;
-   documentation is complete;
-   clean-machine execution succeeds;
-   no fabricated results exist.

------------------------------------------------------------------------

# 88. Final Product Principle

The core product is not merely a churn predictor.

It is a decision-support system that connects:

``` text
Customer Data
      ↓
Cohort & Feature Engineering
      ↓
Survival Modeling
      ↓
When Might the Customer Churn?
      ↓
Risk Segmentation
      ↓
Treatment-Effect Estimation
      ↓
Which Action Has Incremental Value?
      ↓
Expected Retention Value
      ↓
Personalized Treatment Ranking
      ↓
Explainable Recommendation
      ↓
Human User Action
      ↓
Audit Trail
      ↓
Monitoring & Evaluation
```

The project must preserve the distinction between **what the model
predicts**, **what survival analysis estimates**, and **what an
intervention is estimated to change**.

For the likely public churn dataset without genuine treatment history,
the survival component may use the observed tenure/churn structure while
the treatment component must remain explicitly
**semi-synthetic/simulated**. The final system must not convert this
limitation into a false causal claim.

This design directly targets the BDS-11 requirement for an
industry-prototype workflow integrating cohort analysis, survival
curves, feature engineering, Cox/survival models, risk segments,
intervention scenarios, dashboarding, and a causal/uplift innovation
layer, while also satisfying the required reproducibility, testing,
security, explainability, robustness, operational monitoring, and
documentation expectations.
