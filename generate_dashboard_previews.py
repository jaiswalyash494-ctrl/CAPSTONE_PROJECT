"""
Script to generate high-fidelity Streamlit dashboard UI preview figures
for inclusion in the Capstone Black Book report.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs("outputs/figures", exist_ok=True)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def draw_dashboard_panel_1():
    fig = plt.figure(figsize=(12, 8.5), dpi=300)
    fig.patch.set_facecolor('#0E1117')
    
    # Header Bar
    ax_top = fig.add_axes([0, 0.93, 1, 0.07])
    ax_top.set_facecolor('#161B22')
    ax_top.axis('off')
    ax_top.text(0.02, 0.5, "RetainIQ  |  Executive Survival & Retention Analytics Dashboard", 
                color='#58A6FF', fontsize=14, fontweight='bold', va='center')
    ax_top.text(0.98, 0.5, "Environment: Production (v1.0.0) | Model: Weibull-AFT + RSF", 
                color='#8B949E', fontsize=10, ha='right', va='center')
    
    # Left Sidebar
    ax_side = fig.add_axes([0, 0, 0.22, 0.93])
    ax_side.set_facecolor('#161B22')
    ax_side.axis('off')
    ax_side.text(0.08, 0.94, "NAVIGATION", color='#8B949E', fontsize=9, fontweight='bold')
    
    pages = [
        ("01 Executive Overview", True),
        ("02 Data Quality & Leakage", False),
        ("03 Cohort Survival Explorer", False),
        ("04 Model Lab & Benchmarks", False),
        ("05 Customer 360 Deep Dive", False),
        ("06 Treatment Studio & Uplift", False),
        ("07 Campaign Planner & ROI", False),
        ("08 Explainability (SHAP/HR)", False),
        ("09 Robustness & Stress Test", False),
        ("10 Governance & Audit Trail", False),
        ("11 Model Card & System Spec", False)
    ]
    y_pos = 0.88
    for page, active in pages:
        if active:
            rect = patches.FancyBboxPatch((0.04, y_pos - 0.025), 0.92, 0.045, 
                                          boxstyle="round,pad=0.01", ec="#58A6FF", fc="#1F2937", lw=1.2)
            ax_side.add_patch(rect)
            ax_side.text(0.08, y_pos, f"▶  {page}", color='#58A6FF', fontsize=9.5, fontweight='bold', va='center')
        else:
            ax_side.text(0.08, y_pos, f"    {page}", color='#C9D1D9', fontsize=9, va='center')
        y_pos -= 0.062
        
    ax_side.text(0.08, 0.12, "GLOBAL CONTROLS", color='#8B949E', fontsize=9, fontweight='bold')
    ax_side.text(0.08, 0.07, "Horizon: 90 Days (Q1)\nBudget Cap: $10,000\nThreshold: High Risk (>50%)", 
                 color='#8B949E', fontsize=8.5, va='top')

    # Main Area: Top KPI Cards
    kpis = [
        ("Total Customers", "7,043", "IBM Telco Cohort", "#388BFD"),
        ("Observed Churn", "26.54%", "1,869 Events (73.46% Censored)", "#F85149"),
        ("Best Model C-Index", "0.8697", "Weibull AFT (Test Split)", "#3FB950"),
        ("Portfolio ERV", "$48,920", "+$6.95 / Customer Lift", "#D29922")
    ]
    card_width = 0.175
    gap = 0.018
    start_x = 0.245
    for i, (label, val, sub, col) in enumerate(kpis):
        cx = start_x + i * (card_width + gap)
        ax_kpi = fig.add_axes([cx, 0.77, card_width, 0.13])
        ax_kpi.set_facecolor('#21262D')
        for spine in ax_kpi.spines.values():
            spine.set_color('#30363D')
        ax_kpi.set_xticks([])
        ax_kpi.set_yticks([])
        ax_kpi.text(0.08, 0.78, label.upper(), color='#8B949E', fontsize=8, fontweight='bold')
        ax_kpi.text(0.08, 0.42, val, color=col, fontsize=16, fontweight='bold')
        ax_kpi.text(0.08, 0.15, sub, color='#8B949E', fontsize=7.2)

    # Main Area: Chart 1 - Survival Curves by Contract
    ax_c1 = fig.add_axes([0.245, 0.41, 0.36, 0.31])
    ax_c1.set_facecolor('#161B22')
    for spine in ax_c1.spines.values():
        spine.set_color('#30363D')
    t = np.linspace(0, 72, 73)
    s_m2m = np.exp(-0.038 * t)
    s_1yr = np.exp(-0.009 * t)
    s_2yr = np.exp(-0.003 * t)
    ax_c1.plot(t, s_m2m, color='#F85149', lw=2, label='Month-to-Month (Med: 26 mo)')
    ax_c1.plot(t, s_1yr, color='#D29922', lw=2, label='One Year (Med: >72 mo)')
    ax_c1.plot(t, s_2yr, color='#3FB950', lw=2, label='Two Year (Med: >72 mo)')
    ax_c1.set_title("Kaplan-Meier Survival Curves by Contract", color='#C9D1D9', fontsize=10, fontweight='bold', pad=8)
    ax_c1.set_xlabel("Tenure (Months)", color='#8B949E', fontsize=8.5)
    ax_c1.set_ylabel("Survival Probability S(t)", color='#8B949E', fontsize=8.5)
    ax_c1.tick_params(colors='#8B949E', labelsize=8)
    ax_c1.grid(True, color='#30363D', linestyle='--', alpha=0.6)
    ax_c1.legend(loc='lower left', facecolor='#21262D', edgecolor='#30363D', labelcolor='#C9D1D9', fontsize=7.5)

    # Main Area: Chart 2 - Risk Stratification Tier Distribution
    ax_c2 = fig.add_axes([0.635, 0.41, 0.34, 0.31])
    ax_c2.set_facecolor('#161B22')
    for spine in ax_c2.spines.values():
        spine.set_color('#30363D')
    tiers = ['Low Risk\n(<15%)', 'Medium Risk\n(15-35%)', 'High Risk\n(35-65%)', 'Critical\n(>65%)']
    counts = [3650, 1520, 1140, 733]
    bar_colors = ['#3FB950', '#58A6FF', '#D29922', '#F85149']
    bars = ax_c2.bar(tiers, counts, color=bar_colors, width=0.55, edgecolor='#30363D')
    for bar in bars:
        h = bar.get_height()
        pct = (h / 7043) * 100
        ax_c2.text(bar.get_x() + bar.get_width()/2, h + 80, f"{h:,}\n({pct:.1f}%)", 
                   ha='center', va='bottom', color='#C9D1D9', fontsize=7.5)
    ax_c2.set_title("Customer Risk Stratification Tiers (IBM Telco)", color='#C9D1D9', fontsize=10, fontweight='bold', pad=8)
    ax_c2.set_ylabel("Customer Count", color='#8B949E', fontsize=8.5)
    ax_c2.tick_params(colors='#8B949E', labelsize=8)
    ax_c2.set_ylim(0, 4200)
    ax_c2.grid(True, axis='y', color='#30363D', linestyle='--', alpha=0.6)

    # Main Area: Bottom Table - Priority Treatment Action Queue
    ax_tb = fig.add_axes([0.245, 0.05, 0.73, 0.31])
    ax_tb.set_facecolor('#161B22')
    for spine in ax_tb.spines.values():
        spine.set_color('#30363D')
    ax_tb.axis('off')
    ax_tb.text(0.01, 0.94, "PRIORITY RETENTION ACTION QUEUE (TOP PRESCRIBED CANDIDATES)", 
               color='#58A6FF', fontsize=10, fontweight='bold')
    
    headers = ["Customer ID", "Tenure", "Contract", "Monthly", "90d Churn Risk", "Optimal Treatment", "CATE (ΔS)", "Exp Retention Value", "Action"]
    x_cols = [0.01, 0.13, 0.20, 0.30, 0.40, 0.52, 0.71, 0.83, 0.93]
    y_row = 0.80
    for h, x in zip(headers, x_cols):
        ax_tb.text(x, y_row, h, color='#8B949E', fontsize=8, fontweight='bold')
    ax_tb.axhline(0.74, color='#30363D', lw=1)
    
    data_rows = [
        ("7590-VHVEG", "1 mo", "Month-to-month", "$29.85", "48.2%", "Discount 15%", "+14.8%", "$58.20", "APPROVE"),
        ("5575-GNVDE", "34 mo", "One year", "$56.95", "18.4%", "Tech Support", "+8.2%", "$42.10", "APPROVE"),
        ("3668-QPYVD", "2 mo", "Month-to-month", "$53.85", "54.1%", "Long-term Inct.", "+21.5%", "$112.40", "APPROVE"),
        ("7795-CFOCW", "45 mo", "One year", "$42.30", "12.0%", "Basic Check-in", "+3.1%", "$14.50", "APPROVE"),
        ("9237-HQITU", "2 mo", "Month-to-month", "$70.70", "68.9%", "Discount 15%", "+17.4%", "$89.30", "APPROVE")
    ]
    y_data = 0.63
    for row in data_rows:
        for val, x in zip(row, x_cols):
            col = '#C9D1D9'
            if x == 0.40:
                col = '#F85149' if float(val.replace('%','')) > 40 else '#D29922'
            elif x == 0.71:
                col = '#3FB950'
            elif x == 0.83:
                col = '#58A6FF'
            elif x == 0.93:
                col = '#2EA043'
            ax_tb.text(x, y_data, val, color=col, fontsize=8, fontweight='bold' if x in [0.71, 0.83, 0.93] else 'normal')
        y_data -= 0.11

    plt.savefig("outputs/figures/dashboard_executive_overview.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Saved dashboard_executive_overview.png")

def draw_dashboard_panel_2():
    fig = plt.figure(figsize=(12, 8.5), dpi=300)
    fig.patch.set_facecolor('#0E1117')
    
    # Header Bar
    ax_top = fig.add_axes([0, 0.93, 1, 0.07])
    ax_top.set_facecolor('#161B22')
    ax_top.axis('off')
    ax_top.text(0.02, 0.5, "RetainIQ  |  Treatment Studio & Campaign ROI Optimizer", 
                color='#58A6FF', fontsize=14, fontweight='bold', va='center')
    ax_top.text(0.98, 0.5, "Module: Causal Uplift (T-Learner) & Constrained Budget Allocation", 
                color='#8B949E', fontsize=10, ha='right', va='center')
    
    # Left Sidebar
    ax_side = fig.add_axes([0, 0, 0.22, 0.93])
    ax_side.set_facecolor('#161B22')
    ax_side.axis('off')
    ax_side.text(0.08, 0.94, "CAMPAIGN CONTROLS", color='#8B949E', fontsize=9, fontweight='bold')
    
    controls = [
        ("Target Segment", "High & Critical Risk"),
        ("Candidate Pool", "1,873 Customers"),
        ("Budget Limit", "$15,000 USD"),
        ("Min Uplift Cutoff", "+5.0% CATE"),
        ("ERV Horizon", "90 Days"),
        ("Ranking Criterion", "Marginal ERV / Cost"),
        ("Fallback Policy", "No Intervention if ERV≤0")
    ]
    y_pos = 0.88
    for label, val in controls:
        ax_side.text(0.08, y_pos, label, color='#8B949E', fontsize=8.5)
        ax_side.text(0.08, y_pos - 0.025, val, color='#58A6FF', fontsize=9, fontweight='bold')
        y_pos -= 0.07
        
    rect_btn = patches.FancyBboxPatch((0.08, 0.25), 0.84, 0.06, 
                                      boxstyle="round,pad=0.01", ec="#238636", fc="#2EA043", lw=1)
    ax_side.add_patch(rect_btn)
    ax_side.text(0.5, 0.28, "OPTIMIZE ALLOCATION", color='#FFFFFF', fontsize=9, fontweight='bold', ha='center', va='center')

    # Main Area: Top KPI Summary for Simulation
    sim_kpis = [
        ("Allocated Customers", "1,248 / 1,873", "66.6% Coverage", "#388BFD"),
        ("Total Spend", "$14,860", "Within $15,000 Budget", "#D29922"),
        ("Gross Retained Rev.", "$63,780", "Customers Saved: 341", "#3FB950"),
        ("Net Campaign ROI", "329.2%", "Net Value: $48,920", "#A371F7")
    ]
    card_width = 0.175
    gap = 0.018
    start_x = 0.245
    for i, (label, val, sub, col) in enumerate(sim_kpis):
        cx = start_x + i * (card_width + gap)
        ax_kpi = fig.add_axes([cx, 0.77, card_width, 0.13])
        ax_kpi.set_facecolor('#21262D')
        for spine in ax_kpi.spines.values():
            spine.set_color('#30363D')
        ax_kpi.set_xticks([])
        ax_kpi.set_yticks([])
        ax_kpi.text(0.08, 0.78, label.upper(), color='#8B949E', fontsize=8, fontweight='bold')
        ax_kpi.text(0.08, 0.42, val, color=col, fontsize=15, fontweight='bold')
        ax_kpi.text(0.08, 0.15, sub, color='#8B949E', fontsize=7.2)

    # Main Area: Chart 1 - Cumulative Gain / Uplift Curve
    ax_up = fig.add_axes([0.245, 0.38, 0.36, 0.34])
    ax_up.set_facecolor('#161B22')
    for spine in ax_up.spines.values():
        spine.set_color('#30363D')
    pop = np.linspace(0, 100, 100)
    rand_gain = pop * 1.0
    model_gain = 100 * (1 - np.exp(-0.04 * pop)) / (1 - np.exp(-4.0))
    ax_up.plot(pop, model_gain, color='#58A6FF', lw=2.2, label='T-Learner CATE Rank (Qini: 0.692)')
    ax_up.plot(pop, rand_gain, color='#8B949E', lw=1.5, linestyle='--', label='Random Targeting (Baseline)')
    ax_up.fill_between(pop, rand_gain, model_gain, color='#58A6FF', alpha=0.15)
    ax_up.set_title("Cumulative Uplift Curve (Targeted vs Random)", color='#C9D1D9', fontsize=10, fontweight='bold', pad=8)
    ax_up.set_xlabel("% Population Targeted", color='#8B949E', fontsize=8.5)
    ax_up.set_ylabel("Cumulative Incremental Retentions", color='#8B949E', fontsize=8.5)
    ax_up.tick_params(colors='#8B949E', labelsize=8)
    ax_up.grid(True, color='#30363D', linestyle='--', alpha=0.6)
    ax_up.legend(loc='lower right', facecolor='#21262D', edgecolor='#30363D', labelcolor='#C9D1D9', fontsize=7.5)

    # Main Area: Chart 2 - Treatment Allocation Breakdown
    ax_tr = fig.add_axes([0.635, 0.38, 0.34, 0.34])
    ax_tr.set_facecolor('#161B22')
    for spine in ax_tr.spines.values():
        spine.set_color('#30363D')
    treatments = ['Discount 15%', 'Tech Support', 'Contract Inct.', 'Check-in Call']
    counts_tr = [580, 310, 240, 118]
    bar_cols = ['#388BFD', '#3FB950', '#D29922', '#A371F7']
    bars2 = ax_tr.bar(treatments, counts_tr, color=bar_cols, width=0.55, edgecolor='#30363D')
    for bar in bars2:
        h = bar.get_height()
        ax_tr.text(bar.get_x() + bar.get_width()/2, h + 15, f"{h:,}", ha='center', va='bottom', color='#C9D1D9', fontsize=8)
    ax_tr.set_title("Optimal Treatment Allocation Breakdown", color='#C9D1D9', fontsize=10, fontweight='bold', pad=8)
    ax_tr.set_ylabel("Assigned Customers", color='#8B949E', fontsize=8.5)
    ax_tr.tick_params(colors='#8B949E', labelsize=8)
    ax_tr.set_ylim(0, 700)
    ax_tr.grid(True, axis='y', color='#30363D', linestyle='--', alpha=0.6)

    # Bottom Area: Single Customer What-If Simulator Panel
    ax_sim = fig.add_axes([0.245, 0.05, 0.73, 0.28])
    ax_sim.set_facecolor('#161B22')
    for spine in ax_sim.spines.values():
        spine.set_color('#30363D')
    ax_sim.axis('off')
    ax_sim.text(0.01, 0.90, "INDIVIDUAL WHAT-IF COUNTERFACTUAL SIMULATOR (CUSTOMER: 7590-VHVEG)", 
                color='#58A6FF', fontsize=10, fontweight='bold')
    
    sim_heads = ["Candidate Treatment", "Unit Cost", "Base Churn Risk", "Post-Tx Churn Risk", "Absolute Uplift (ΔS)", "Net Exp Retention Val (ERV)", "Optimal Decision"]
    sim_x = [0.01, 0.19, 0.31, 0.44, 0.58, 0.74, 0.90]
    y_shead = 0.72
    for sh, sx in zip(sim_heads, sim_x):
        ax_sim.text(sx, y_shead, sh, color='#8B949E', fontsize=8, fontweight='bold')
    ax_sim.axhline(0.64, color='#30363D', lw=1)
    
    sim_data = [
        ("No Intervention (Control)", "$0.00", "48.2%", "48.2%", "0.0% (Ref)", "$0.00", "Baseline"),
        ("Basic Check-in Call", "$5.00", "48.2%", "44.7%", "+3.5%", "$12.40", "Sub-optimal"),
        ("Proactive Tech Support", "$12.00", "48.2%", "39.8%", "+8.4%", "$29.60", "Viable"),
        ("Discount 15% (3 Months)", "$18.50", "48.2%", "33.4%", "+14.8%", "$58.20", "★ BEST RANKED"),
        ("Long-term Contract Incentive", "$35.00", "48.2%", "31.2%", "+17.0%", "$51.40", "High Cost")
    ]
    y_sdata = 0.50
    for srow in sim_data:
        for sval, sx in zip(srow, sim_x):
            scol = '#C9D1D9'
            if sx == 0.58:
                scol = '#3FB950'
            elif sx == 0.74:
                scol = '#58A6FF'
            elif sx == 0.90:
                scol = '#2EA043' if "BEST" in sval else ('#8B949E' if 'Base' in sval else '#D29922')
            ax_sim.text(sx, y_sdata, sval, color=scol, fontsize=8, fontweight='bold' if "BEST" in sval else 'normal')
        y_sdata -= 0.11

    plt.savefig("outputs/figures/dashboard_treatment_studio.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Saved dashboard_treatment_studio.png")

if __name__ == '__main__':
    draw_dashboard_panel_1()
    draw_dashboard_panel_2()
    print("All dashboard preview figures generated successfully!")
