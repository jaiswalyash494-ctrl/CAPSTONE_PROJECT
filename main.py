"""RetainIQ - Master Pipeline Orchestrator.

Implements PRD Section 53:
Coordinates the end-to-end execution flow:
1. Environment & Dataset Inspection
2. Data Preprocessing & Validation
3. Automated Leakage Prevention Audit
4. Feature Engineering Pipeline
5. Cohort Analysis & Exploratory Survival
6. Survival Modeling & Model Comparison (KM, Logistic, Cox PH, Weibull, RSF)
7. Customer Horizon Forecasting & Risk Segmentation
8. Treatment Simulator & Potential Outcomes
9. Causal / Uplift Meta-Learning (S/T/X-Learners)
10. Personalized Treatment Ranking & Expected Retention Value Engine
11. Explainability & Attribution Diagnostics
12. Robustness, Stress Testing, & Failure-Mode Experiments
13. Operational Monitoring, Drift Detection, & Hash-Chain Audit Logging
"""

import argparse
import logging
import sys
import time
from pathlib import Path

from src.config import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("RetainIQ")

def stage_inspect():
    from src.inspect_env import run_inspection
    run_inspection()

def stage_data():
    from src.data_preprocessing import run_preprocessing_pipeline
    from src.feature_engineering import run_feature_engineering_pipeline
    from src.leakage_checks import run_leakage_audit
    
    run_preprocessing_pipeline()
    run_feature_engineering_pipeline()
    run_leakage_audit()

def stage_survival():
    from src.cohort_analysis import run_cohort_analysis
    from src.survival_evaluation import run_survival_pipeline
    from src.survival_predictions import generate_survival_predictions
    
    run_cohort_analysis()
    run_survival_pipeline()
    generate_survival_predictions()

def stage_treatment():
    from src.treatment_simulator import simulate_treatment_dataset
    from src.treatment_effects import run_uplift_pipeline
    from src.treatment_ranking import rank_treatments_for_all_customers
    
    simulate_treatment_dataset(mode=settings.raw_config.get("treatment_modeling", {}).get("mode", "B"))
    run_uplift_pipeline()
    rank_treatments_for_all_customers()

def stage_explain():
    from src.explainability import run_explainability_pipeline
    run_explainability_pipeline()

def stage_robustness():
    from src.robustness import run_robustness_experiments
    run_robustness_experiments()

def stage_monitoring():
    from src.monitoring import run_monitoring_pipeline
    from src.audit import seed_initial_audit_log
    
    seed_initial_audit_log()
    run_monitoring_pipeline()

def run_all_stages():
    """Run complete end-to-end Capstone ML and decision pipeline."""
    start_time = time.time()
    logger.info("=" * 70)
    logger.info("STARTING RETAINIQ CAPSTONE PIPELINE (BDS-11)")
    logger.info("Survival-Based Churn Modeling with Personalized Retention Treatment Ranking")
    logger.info("=" * 70)
    
    logger.info("\n>>> STAGE 1: Environment & Dataset Inspection")
    stage_inspect()
    
    logger.info("\n>>> STAGE 2: Data Cleaning, Feature Engineering & Leakage Gates")
    stage_data()
    
    logger.info("\n>>> STAGE 3: Cohort Analysis & Survival Modeling Suite")
    stage_survival()
    
    logger.info("\n>>> STAGE 4: Treatment Simulator & Causal Uplift Ranking Engine")
    stage_treatment()
    
    logger.info("\n>>> STAGE 5: Explainability & Attribution Layer")
    stage_explain()
    
    logger.info("\n>>> STAGE 6: Robustness, Overlap, & Failure-Mode Experiments")
    stage_robustness()
    
    logger.info("\n>>> STAGE 7: Operational Monitoring & Hash-Chain Audit Logging")
    stage_monitoring()
    
    total_elapsed = time.time() - start_time
    logger.info("=" * 70)
    logger.info(f"RETAINIQ PIPELINE SUCCESSFULLY COMPLETED IN {total_elapsed:.1f} SECONDS.")
    logger.info("All model artifacts saved to models/")
    logger.info("All reports, predictions, and figures saved to outputs/")
    logger.info("=" * 70)

def main():
    parser = argparse.ArgumentParser(
        description="RetainIQ: Survival-Based Churn Modeling with Personalized Retention Treatment Ranking"
    )
    parser.add_argument(
        "--stage",
        type=str,
        default="all",
        choices=["all", "inspect", "data", "survival", "treatment", "explain", "robustness", "monitoring"],
        help="Pipeline stage to execute (default: all)"
    )
    args = parser.parse_args()
    
    if args.stage == "all":
        run_all_stages()
    elif args.stage == "inspect":
        stage_inspect()
    elif args.stage == "data":
        stage_data()
    elif args.stage == "survival":
        stage_survival()
    elif args.stage == "treatment":
        stage_treatment()
    elif args.stage == "explain":
        stage_explain()
    elif args.stage == "robustness":
        stage_robustness()
    elif args.stage == "monitoring":
        stage_monitoring()

if __name__ == "__main__":
    main()
