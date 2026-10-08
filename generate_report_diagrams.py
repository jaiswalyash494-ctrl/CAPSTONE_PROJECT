"""RetainIQ - Generate High-Resolution System Design & Architecture Diagrams.

Generates:
1. System Architecture Diagram
2. Project Implementation Timeline (Gantt Chart)
3. Data Flow Diagrams (Level 0 Context & Level 1 Decomposition)
4. UML Class Diagram
5. UML Sequence Diagram (Customer Scoring & Ranking Flow)
6. UML State Chart Diagram (Decision & Override Lifecycle)
7. UML Use-Case Diagram
8. Model Comparison Benchmarks Bar Chart (C-Index & IBS)
9. Portfolio ERV Cumulative Value Optimization Curve
10. Dashboard Multi-Module Overview Graphic
"""

import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

figures_dir = Path("outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

# Set global matplotlib styling for professional publication quality
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 1.0

# -------------------------------------------------------------
# 1. SYSTEM ARCHITECTURE DIAGRAM
# -------------------------------------------------------------
def make_architecture_diagram():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    # Title
    ax.text(6.0, 7.6, "RetainIQ: End-to-End Enterprise Architecture", ha='center', va='center',
            fontsize=16, fontweight='bold', color='#0F172A')
    ax.text(6.0, 7.3, "Survival-Based Churn Modeling & Personalized Retention Treatment Ranking (TRL 4–5)",
            ha='center', va='center', fontsize=11, color='#475569')

    # Layers
    layers = [
        ("Data Layer", 0.5, 5.8, 11.0, 1.1, '#E0F2FE', '#0284C7',
         ["Raw Telco Subscription Data (7,043 Accounts, 73.46% Censored)",
          "Data Cleaning & Zero-Tenure Survival Alignment (0.5m)",
          "5 Automated Pre-Training Leakage Prevention Gates",
          "Feature Engineering Pipeline (Fitted on Train Split Only)"]),
        
        ("Analytical Modeling Layer", 0.5, 4.0, 11.0, 1.4, '#F0FDF4', '#16A34A',
         ["Survival Modeling Suite: Kaplan-Meier (M0a), Naive Logistic (M0b), Cox PH (M1), Weibull AFT (M2), RSF (M3)",
          "Semi-Synthetic Potential Outcomes Treatment Simulator (Quarantined Ground Truth)",
          "Causal Uplift Meta-Learners: S-Learner (Selected), T-Learner, X-Learner",
          "Individual Horizon Forecasting: S_i(t) @ 30d, 60d, 90d, 180d & Documented Risk Tiers"]),
        
        ("Decision & Governance Layer", 0.5, 2.3, 11.0, 1.3, '#FAF5FF', '#9333EA',
         ["Net Expected Retention Value (ERV) Engine: ERV = ΔP * ValueProxy - Cost",
          "Eligibility Constraints & Mandatory 'No Intervention' Fallback for ERV ≤ 0",
          "Three-Part Natural Language Audit Narratives & Cox Hazard Ratios",
          "Cryptographic SHA-256 Tamper-Evident Hash-Chain Audit Log"]),
        
        ("Serving & Production Interface Layer", 0.5, 0.6, 11.0, 1.3, '#FFF7ED', '#EA580C',
         ["RESTful FastAPI Backend: Sub-4ms p95 Latency, Pydantic Schema Contracts",
          "Streamlit Multi-Role Decision Cockpit: 11 Interactive Analytical Modules",
          "Interactive What-If Scenario Simulator & Portfolio Campaign Budget Allocator",
          "Operational Drift Monitoring: Population Stability Index (PSI) & Latency Benchmarks"])
    ]

    for title, x, y, w, h, bg_color, border_color, bullets in layers:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.15",
                                      facecolor=bg_color, edgecolor=border_color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + 0.3, y + h - 0.22, title.upper(), fontsize=11, fontweight='bold', color=border_color)
        
        for idx, bullet in enumerate(bullets):
            by = y + h - 0.45 - (idx * 0.22)
            ax.text(x + 0.5, by, f"•  {bullet}", fontsize=9, color='#1E293B', va='center')

    # Connecting arrows
    arrow_props = dict(facecolor='#64748B', edgecolor='#475569', width=1.5, headwidth=6, headlength=6)
    ax.annotate('', xy=(6.0, 5.8), xytext=(6.0, 5.5), arrowprops=arrow_props)
    ax.annotate('', xy=(6.0, 4.0), xytext=(6.0, 3.7), arrowprops=arrow_props)
    ax.annotate('', xy=(6.0, 2.3), xytext=(6.0, 2.0), arrowprops=arrow_props)

    plt.tight_layout()
    plt.savefig(figures_dir / "architecture_diagram.png", bbox_inches='tight')
    plt.close()
    print("Saved architecture_diagram.png")

# -------------------------------------------------------------
# 2. GANTT CHART
# -------------------------------------------------------------
def make_gantt_chart():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    tasks = [
        "1. Requirement Analysis & PRD Specifications",
        "2. Dataset Capability Audit & Environment Inspection",
        "3. Data Preprocessing & Zero-Tenure Survival Alignment",
        "4. Feature Engineering & 5 Leakage Prevention Gates",
        "5. Cohort Analysis & Kaplan-Meier Estimation",
        "6. Survival Modeling Suite (Cox PH, Weibull, RSF)",
        "7. Potential Outcomes Simulation & Quarantined Truth",
        "8. Uplift Meta-Learning (S/T/X-Learners) & Qini Analysis",
        "9. Net ERV Engine & Personalized Treatment Ranking",
        "10. Explainability, Hazard Ratios & Narrative Engine",
        "11. Robustness, Positivity & Failure-Mode Experiments",
        "12. SHA-256 Hash-Chain Audit & PSI Drift Monitoring",
        "13. FastAPI REST Service & Schema Implementation",
        "14. Streamlit Multi-Role Analytics Studio (11 Pages)",
        "15. Verification Test Suite & Final Project Packaging"
    ]

    start_weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    durations =   [2, 1, 2, 2, 2, 3, 2, 2, 2,  2,  2,  2,  2,  3,  2]

    y_pos = np.arange(len(tasks))
    ax.barh(y_pos, durations, left=start_weeks, height=0.6, align='center',
            color=['#0284C7', '#0284C7', '#0D9488', '#0D9488', '#16A34A',
                   '#16A34A', '#7C3AED', '#7C3AED', '#9333EA', '#D97706',
                   '#D97706', '#DC2626', '#2563EB', '#0D9488', '#059669'],
            edgecolor='#0F172A', linewidth=0.5)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=9, fontweight='500', color='#0F172A')
    ax.invert_yaxis()
    ax.set_xlabel("Project Timeline (Weeks 1 to 16)", fontsize=11, fontweight='bold', color='#1E293B')
    ax.set_xlim(0, 18)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    ax.set_title("Figure 3.2: RetainIQ Project Implementation Gantt Chart", fontsize=13, fontweight='bold', pad=15)

    plt.tight_layout()
    plt.savefig(figures_dir / "gantt_chart.png", bbox_inches='tight')
    plt.close()
    print("Saved gantt_chart.png")

# -------------------------------------------------------------
# 3. DFD LEVEL 0 AND LEVEL 1
# -------------------------------------------------------------
def make_dfd_diagram():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 9), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')

    # DFD Level 0
    ax1.set_facecolor('#F8FAFC')
    ax1.axis('off')
    ax1.text(0.5, 0.95, "Figure 3.3a: Level 0 Context Data Flow Diagram", ha='center', fontsize=12, fontweight='bold')

    # External Entity Left
    rect_ent1 = patches.FancyBboxPatch((0.05, 0.35), 0.22, 0.3, boxstyle="square,pad=0.05",
                                      facecolor='#E2E8F0', edgecolor='#475569', linewidth=1.5)
    ax1.add_patch(rect_ent1)
    ax1.text(0.16, 0.5, "Telecom CRM\n& Billing Database", ha='center', va='center', fontsize=9, fontweight='bold')

    # Central Process
    circle_proc = patches.Circle((0.5, 0.5), 0.18, facecolor='#E0F2FE', edgecolor='#0284C7', linewidth=2.0)
    ax1.add_patch(circle_proc)
    ax1.text(0.5, 0.5, "0.0\nRetainIQ\nDecision System", ha='center', va='center', fontsize=10, fontweight='bold', color='#0369A1')

    # External Entity Right
    rect_ent2 = patches.FancyBboxPatch((0.73, 0.35), 0.22, 0.3, boxstyle="square,pad=0.05",
                                      facecolor='#E2E8F0', edgecolor='#475569', linewidth=1.5)
    ax1.add_patch(rect_ent2)
    ax1.text(0.84, 0.5, "Retention Strategist\n& Campaign Ops", ha='center', va='center', fontsize=9, fontweight='bold')

    # Arrows Level 0
    ax1.annotate('Customer Profiles & Tenures', xy=(0.32, 0.55), xytext=(0.27, 0.55),
                 arrowprops=dict(facecolor='#0284C7', width=1.5, headwidth=6, headlength=6), fontsize=8, ha='center', va='bottom')
    ax1.annotate('Personalized Treatment Rankings\n& Net ERV Decisions', xy=(0.73, 0.55), xytext=(0.68, 0.55),
                 arrowprops=dict(facecolor='#16A34A', width=1.5, headwidth=6, headlength=6), fontsize=8, ha='center', va='bottom')
    ax1.annotate('Managerial Overrides\n& Campaign Budget', xy=(0.68, 0.45), xytext=(0.73, 0.45),
                 arrowprops=dict(facecolor='#9333EA', width=1.5, headwidth=6, headlength=6), fontsize=8, ha='center', va='top')
    ax1.annotate('Audit Confirmation Receipts', xy=(0.27, 0.45), xytext=(0.32, 0.45),
                 arrowprops=dict(facecolor='#EA580C', width=1.5, headwidth=6, headlength=6), fontsize=8, ha='center', va='top')

    # DFD Level 1
    ax2.set_facecolor('#F8FAFC')
    ax2.axis('off')
    ax2.text(0.5, 0.95, "Figure 3.3b: Level 1 Decomposed Data Flow Diagram", ha='center', fontsize=12, fontweight='bold')

    processes = [
        ("1.0 Ingest & Clean", 0.08, 0.45, '#E0F2FE', '#0284C7'),
        ("2.0 Survival Forecast", 0.32, 0.45, '#F0FDF4', '#16A34A'),
        ("3.0 Uplift Meta-Learning", 0.56, 0.45, '#FAF5FF', '#9333EA'),
        ("4.0 ERV Ranking Engine", 0.80, 0.45, '#FFF7ED', '#EA580C')
    ]

    for name, cx, cy, bg, border in processes:
        circ = patches.Circle((cx, cy), 0.09, facecolor=bg, edgecolor=border, linewidth=1.8)
        ax2.add_patch(circ)
        ax2.text(cx, cy, name.replace(" ", "\n"), ha='center', va='center', fontsize=8, fontweight='bold', color=border)

    # Connecting flow arrows
    ax2.annotate('Clean Parquet', xy=(0.23, 0.45), xytext=(0.17, 0.45),
                 arrowprops=dict(facecolor='#0284C7', width=1.2, headwidth=5, headlength=5), fontsize=7, ha='center', va='bottom')
    ax2.annotate('Survival S(t)', xy=(0.47, 0.45), xytext=(0.41, 0.45),
                 arrowprops=dict(facecolor='#16A34A', width=1.2, headwidth=5, headlength=5), fontsize=7, ha='center', va='bottom')
    ax2.annotate('CATE Lift (ΔP)', xy=(0.71, 0.45), xytext=(0.65, 0.45),
                 arrowprops=dict(facecolor='#9333EA', width=1.2, headwidth=5, headlength=5), fontsize=7, ha='center', va='bottom')

    # Bottom Data Store
    rect_ds = patches.FancyBboxPatch((0.25, 0.12), 0.5, 0.14, boxstyle="round,pad=0.03,rounding_size=0.05",
                                      facecolor='#FEF3C7', edgecolor='#D97706', linewidth=1.5)
    ax2.add_patch(rect_ds)
    ax2.text(0.5, 0.19, "D1: SHA-256 Tamper-Evident Hash Chain Audit Store", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#B45309')

    # Arrow to datastore
    ax2.annotate('Append Event Hash', xy=(0.5, 0.26), xytext=(0.80, 0.36),
                 arrowprops=dict(facecolor='#D97706', width=1.2, headwidth=5, headlength=5), fontsize=7, ha='center')

    plt.tight_layout()
    plt.savefig(figures_dir / "dfd_level0_level1.png", bbox_inches='tight')
    plt.close()
    print("Saved dfd_level0_level1.png")

# -------------------------------------------------------------
# 4. UML CLASS DIAGRAM
# -------------------------------------------------------------
def make_uml_class_diagram():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    ax.text(6.0, 7.6, "Figure 3.4: RetainIQ Object-Oriented UML Class Architecture", ha='center', va='center',
            fontsize=14, fontweight='bold', color='#0F172A')

    classes = [
        ("FeaturePipeline", 0.5, 4.8, 3.2, 2.2, '#E0F2FE', '#0284C7',
         ["+ continuous_cols: List[str]", "+ scaler: StandardScaler", "+ fitted: bool"],
         ["+ fit(X_train: DataFrame)", "+ transform(X: DataFrame)", "+ get_survival_feature_names()"]),
        
        ("CoxPHModel", 4.3, 4.8, 3.4, 2.2, '#F0FDF4', '#16A34A',
         ["+ penalizer: float = 0.01", "+ cph: CoxPHFitter", "+ baseline_hazard_: DataFrame"],
         ["+ fit(X, duration, event)", "+ predict_survival_function(X, t)", "+ compute_hazard_ratios()"]),
        
        ("SLearnerUplift", 8.2, 4.8, 3.3, 2.2, '#FAF5FF', '#9333EA',
         ["+ estimator: GradientBoosting", "+ treatment_cols: List[str]"],
         ["+ fit(X, treatment, y)", "+ predict_cate(X, treatment)", "+ evaluate_qini(test_df)"]),
        
        ("ExpectedRetentionValueEngine", 2.2, 1.6, 3.6, 2.4, '#FFF7ED', '#EA580C',
         ["+ margin_rate: float = 0.70", "+ horizon_months: int = 3", "+ cost_map: Dict[str, float]"],
         ["+ check_eligibility(customer, treat)", "+ compute_erv(cate, proxy, cost)", "+ rank_all_treatments(customer)", "+ fallback_no_intervention()"]),
        
        ("AuditTrail", 6.8, 1.6, 3.8, 2.4, '#FEF2F2', '#DC2626',
         ["+ log_path: Path", "+ records: List[Dict]", "+ genesis_hash: str"],
         ["+ log_decision_event(...) -> Dict", "+ verify_integrity() -> (bool, str)", "+ get_latest_hash() -> str", "+ _compute_hash(payload, prev)"])
    ]

    for name, x, y, w, h, bg, border, attrs, meths in classes:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0.05", facecolor='#FFFFFF', edgecolor=border, linewidth=1.5)
        ax.add_patch(rect)
        # Header banner
        hdr = patches.Rectangle((x, y + h - 0.45), w, 0.45, facecolor=bg, edgecolor=border, linewidth=1.0)
        ax.add_patch(hdr)
        ax.text(x + w/2, y + h - 0.22, name, ha='center', va='center', fontsize=9.5, fontweight='bold', color=border)
        
        # Attributes
        ay = y + h - 0.65
        for a in attrs:
            ax.text(x + 0.15, ay, a, fontsize=7.5, color='#334155', fontfamily='monospace')
            ay -= 0.22
            
        # Divider line
        ax.plot([x, x + w], [ay + 0.1, ay + 0.1], color=border, linewidth=0.8)
        ay -= 0.15
        
        # Methods
        for m in meths:
            ax.text(x + 0.15, ay, m, fontsize=7.5, color='#0F172A', fontfamily='monospace')
            ay -= 0.22

    # Relationship arrows
    ax.annotate('', xy=(4.3, 5.8), xytext=(3.7, 5.8), arrowprops=dict(facecolor='#0284C7', width=1.2, headwidth=5, headlength=5))
    ax.annotate('', xy=(8.2, 5.8), xytext=(7.7, 5.8), arrowprops=dict(facecolor='#16A34A', width=1.2, headwidth=5, headlength=5))
    ax.annotate('', xy=(4.0, 4.0), xytext=(5.0, 4.8), arrowprops=dict(facecolor='#EA580C', width=1.2, headwidth=5, headlength=5))
    ax.annotate('', xy=(7.5, 4.0), xytext=(9.0, 4.8), arrowprops=dict(facecolor='#9333EA', width=1.2, headwidth=5, headlength=5))
    ax.annotate('', xy=(6.8, 2.8), xytext=(5.8, 2.8), arrowprops=dict(facecolor='#DC2626', width=1.2, headwidth=5, headlength=5))

    plt.tight_layout()
    plt.savefig(figures_dir / "uml_class_diagram.png", bbox_inches='tight')
    plt.close()
    print("Saved uml_class_diagram.png")

# -------------------------------------------------------------
# 5. UML SEQUENCE DIAGRAM
# -------------------------------------------------------------
def make_uml_sequence_diagram():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    ax.text(5.5, 6.7, "Figure 3.5: UML Sequence Diagram — Customer Scoring & Ranking Workflow",
            ha='center', va='center', fontsize=13, fontweight='bold', color='#0F172A')

    actors = ["Client / UI", "FastAPI Route", "Survival Engine", "Uplift Engine", "ERV Ranker", "Audit Chain"]
    x_coords = [0.8, 2.6, 4.5, 6.4, 8.3, 10.1]

    # Draw vertical lifelines
    for idx, (name, x) in enumerate(zip(actors, x_coords)):
        rect = patches.FancyBboxPatch((x - 0.7, 5.9), 1.4, 0.45, boxstyle="round,pad=0.05",
                                      facecolor='#E2E8F0', edgecolor='#475569', linewidth=1.2)
        ax.add_patch(rect)
        ax.text(x, 6.12, name, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1E293B')
        ax.plot([x, x], [0.6, 5.9], color='#94A3B8', linestyle='--', linewidth=1.0)

    # Sequence calls
    messages = [
        (0, 1, 5.3, "1. POST /predict/customer", '#0284C7'),
        (1, 2, 4.7, "2. predict_survival_function(X)", '#16A34A'),
        (2, 1, 4.2, "3. Return S(t) horizons & Churn Risk", '#16A34A', True),
        (1, 3, 3.6, "4. predict_cate(X, treatments)", '#9333EA'),
        (3, 1, 3.1, "5. Return CATE treatment effects", '#9333EA', True),
        (1, 4, 2.5, "6. rank_by_net_erv(CATE, ValueProxy)", '#EA580C'),
        (4, 1, 2.0, "7. Return Ranked Options & Top Action", '#EA580C', True),
        (1, 5, 1.4, "8. log_decision_event(SHA-256)", '#DC2626'),
        (1, 0, 0.8, "9. Return CustomerScoringResponse JSON", '#0284C7', True)
    ]

    for item in messages:
        src_idx, dst_idx, y, text, col = item[0], item[1], item[2], item[3], item[4]
        is_ret = len(item) > 5 and item[5]
        x1, x2 = x_coords[src_idx], x_coords[dst_idx]
        
        style = '->' if not is_ret else '->'
        ls = '-' if not is_ret else '--'
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(facecolor=col, edgecolor=col, arrowstyle=style, linestyle=ls, linewidth=1.5))
        ax.text((x1 + x2)/2, y + 0.12, text, ha='center', va='bottom', fontsize=7.5, fontweight='600', color=col)

    plt.tight_layout()
    plt.savefig(figures_dir / "uml_sequence_diagram.png", bbox_inches='tight')
    plt.close()
    print("Saved uml_sequence_diagram.png")

# -------------------------------------------------------------
# 6. UML STATE CHART & USE CASE DIAGRAMS
# -------------------------------------------------------------
def make_uml_state_and_usecase():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')

    # State Chart
    ax1.set_facecolor('#F8FAFC')
    ax1.axis('off')
    ax1.text(0.5, 0.95, "Figure 3.6: UML Statechart Diagram\n(Retention Decision Lifecycle)", ha='center', fontsize=11, fontweight='bold')

    states = [
        ("Account Ingested", 0.1, 0.7, '#E0F2FE', '#0284C7'),
        ("Scored & Forecasted", 0.5, 0.7, '#F0FDF4', '#16A34A'),
        ("Intervention Ranked", 0.5, 0.4, '#FAF5FF', '#9333EA'),
        ("Committed to Audit", 0.1, 0.4, '#FEF3C7', '#D97706'),
        ("Action Executed", 0.1, 0.12, '#F0FDF4', '#059669'),
        ("Exception Override", 0.5, 0.12, '#FEF2F2', '#DC2626')
    ]

    for name, x, y, bg, border in states:
        rect = patches.FancyBboxPatch((x, y), 0.35, 0.14, boxstyle="round,pad=0.03,rounding_size=0.04",
                                      facecolor=bg, edgecolor=border, linewidth=1.5)
        ax1.add_patch(rect)
        ax1.text(x + 0.175, y + 0.07, name, ha='center', va='center', fontsize=8, fontweight='bold', color=border)

    # State arrows
    ax1.annotate('Preprocess & Align', xy=(0.5, 0.77), xytext=(0.45, 0.77),
                 arrowprops=dict(facecolor='#0284C7', width=1.0, headwidth=4, headlength=4), fontsize=6.5, ha='center')
    ax1.annotate('Uplift & ERV Calc', xy=(0.675, 0.54), xytext=(0.675, 0.70),
                 arrowprops=dict(facecolor='#16A34A', width=1.0, headwidth=4, headlength=4), fontsize=6.5, ha='center')
    ax1.annotate('Automated Select', xy=(0.45, 0.47), xytext=(0.5, 0.47),
                 arrowprops=dict(facecolor='#9333EA', width=1.0, headwidth=4, headlength=4), fontsize=6.5, ha='center')
    ax1.annotate('Approve Offer', xy=(0.275, 0.26), xytext=(0.275, 0.40),
                 arrowprops=dict(facecolor='#059669', width=1.0, headwidth=4, headlength=4), fontsize=6.5, ha='center')
    ax1.annotate('Managerial Override', xy=(0.675, 0.26), xytext=(0.675, 0.40),
                 arrowprops=dict(facecolor='#DC2626', width=1.0, headwidth=4, headlength=4), fontsize=6.5, ha='center')

    # Use Case Diagram
    ax2.set_facecolor('#F8FAFC')
    ax2.axis('off')
    ax2.text(0.5, 0.95, "Figure 3.7: UML Use-Case Diagram\n(Role-Based Interactions)", ha='center', fontsize=11, fontweight='bold')

    actors = [("Retention Strategist", 0.05, 0.75), ("Data Scientist", 0.05, 0.45), ("Governance Admin", 0.05, 0.15)]
    for aname, ax_pos, ay_pos in actors:
        ax2.plot(ax_pos + 0.05, ay_pos + 0.05, marker='o', markersize=10, color='#1E293B')
        ax2.plot([ax_pos + 0.05, ax_pos + 0.05], [ay_pos - 0.04, ay_pos + 0.05], color='#1E293B', linewidth=2)
        ax2.text(ax_pos + 0.05, ay_pos - 0.09, aname, ha='center', fontsize=7.5, fontweight='bold')

    use_cases = [
        ("Simulate Treatment What-If", 0.55, 0.8),
        ("Allocate Campaign Budget", 0.55, 0.65),
        ("Inspect 5 Leakage Gates", 0.55, 0.5),
        ("Benchmark Survival Models", 0.55, 0.35),
        ("Verify SHA-256 Audit Chain", 0.55, 0.2),
        ("Monitor Population Drift (PSI)", 0.55, 0.05)
    ]

    for uname, ux, uy in use_cases:
        ellipse = patches.Ellipse((ux + 0.2, uy + 0.04), 0.42, 0.1, facecolor='#FFFFFF', edgecolor='#0284C7', linewidth=1.2)
        ax2.add_patch(ellipse)
        ax2.text(ux + 0.2, uy + 0.04, uname, ha='center', va='center', fontsize=7.5, color='#0F172A')

    # Association lines
    ax2.plot([0.15, 0.55], [0.75, 0.84], color='#64748B', linestyle=':', linewidth=1.0)
    ax2.plot([0.15, 0.55], [0.75, 0.69], color='#64748B', linestyle=':', linewidth=1.0)
    ax2.plot([0.15, 0.55], [0.45, 0.54], color='#64748B', linestyle=':', linewidth=1.0)
    ax2.plot([0.15, 0.55], [0.45, 0.39], color='#64748B', linestyle=':', linewidth=1.0)
    ax2.plot([0.15, 0.55], [0.15, 0.24], color='#64748B', linestyle=':', linewidth=1.0)
    ax2.plot([0.15, 0.55], [0.15, 0.09], color='#64748B', linestyle=':', linewidth=1.0)

    plt.tight_layout()
    plt.savefig(figures_dir / "uml_state_and_usecase.png", bbox_inches='tight')
    plt.close()
    print("Saved uml_state_and_usecase.png")

# -------------------------------------------------------------
# 7. MODEL COMPARISON BENCHMARK BAR CHART
# -------------------------------------------------------------
def make_model_comparison_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')

    comp_df = pd.read_csv("outputs/metrics/model_comparison.csv")
    models = ["KM (M0a)", "Logistic (M0b)", "Cox PH (M1)", "Weibull (M2)", "RSF (M3)"]
    c_indices = comp_df['c_index'].values
    ibs_scores = comp_df['integrated_brier_score'].values

    # C-Index plot
    bars1 = ax1.bar(models, c_indices, color=['#94A3B8', '#64748B', '#0D9488', '#0284C7', '#8B5CF6'], width=0.55, edgecolor='#0F172A', linewidth=0.5)
    ax1.set_ylim(0.45, 0.95)
    ax1.set_ylabel("Harrell's C-Index (Higher is Better)", fontsize=9.5, fontweight='bold', color='#1E293B')
    ax1.set_title("Survival Discrimination (C-Index)", fontsize=11, fontweight='bold', pad=10)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 0.01, f"{yval:.4f}", ha='center', va='bottom', fontsize=8, fontweight='bold')

    # IBS plot
    bars2 = ax2.bar(models, ibs_scores, color=['#EF4444', '#F59E0B', '#10B981', '#10B981', '#10B981'], width=0.55, edgecolor='#0F172A', linewidth=0.5)
    ax2.set_ylim(0.0, 0.20)
    ax2.set_ylabel("Integrated Brier Score (Lower is Better)", fontsize=9.5, fontweight='bold', color='#1E293B')
    ax2.set_title("Calibration Accuracy (IBS)", fontsize=11, fontweight='bold', pad=10)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.004, f"{yval:.4f}", ha='center', va='bottom', fontsize=8, fontweight='bold')

    plt.tight_layout()
    plt.savefig(figures_dir / "model_comparison_chart.png", bbox_inches='tight')
    plt.close()
    print("Saved model_comparison_chart.png")

# -------------------------------------------------------------
# 8. PORTFOLIO ERV CUMULATIVE OPTIMIZATION CURVE
# -------------------------------------------------------------
def make_erv_optimization_curve():
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=300)
    fig.patch.set_facecolor('#FFFFFF')

    df_dec = pd.read_parquet("outputs/predictions/customer_decisions.parquet")
    active_df = df_dec[df_dec["expected_value"] > 0].copy()
    active_df = active_df.sort_values(by="expected_value", ascending=False).reset_index(drop=True)
    active_df["cum_cost"] = active_df["treatment_cost"].cumsum()
    active_df["cum_erv"] = active_df["expected_value"].cumsum()

    x = np.arange(1, len(active_df) + 1)
    ax.plot(x, active_df["cum_erv"], color='#10B981', linewidth=2.5, label='Cumulative Net Expected Value (ERV $)')
    ax.plot(x, active_df["cum_cost"], color='#F59E0B', linewidth=2.0, linestyle='--', label='Cumulative Intervention Spend ($)')

    # Add vertical line for optimal budget cutoff
    ax.axvline(x=len(active_df), color='#0284C7', linestyle=':', linewidth=1.5, label=f'Marginal ERV Cutoff (n={len(active_df):,})')

    ax.set_title("Figure 5.4: Cumulative Net Expected Retention Value vs Capital Spend", fontsize=11.5, fontweight='bold', pad=10)
    ax.set_xlabel("Targeted Customer Accounts (Ranked Descending by Net ERV)", fontsize=9.5, fontweight='bold', color='#1E293B')
    ax.set_ylabel("Dollars ($)", fontsize=9.5, fontweight='bold', color='#1E293B')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8.5)

    plt.tight_layout()
    plt.savefig(figures_dir / "erv_optimization_curve.png", bbox_inches='tight')
    plt.close()
    print("Saved erv_optimization_curve.png")

if __name__ == "__main__":
    make_architecture_diagram()
    make_gantt_chart()
    make_dfd_diagram()
    make_uml_class_diagram()
    make_uml_sequence_diagram()
    make_uml_state_and_usecase()
    make_model_comparison_chart()
    make_erv_optimization_curve()
    print("All report diagrams generated successfully!")
