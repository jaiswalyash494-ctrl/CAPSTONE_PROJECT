"""
Builder for IVAN BLACKBOOK TEST.docx and IVAN BLACKBOOK TEST.pdf.
Replicates the structural organization of 'shubham blackbook.pdf' from page 7 onwards,
tailored exclusively to Ivan Dsouza's RetainIQ Capstone Project.
Outputs:
- IVAN BLACKBOOK TEST.docx
- IVAN BLACKBOOK TEST.pdf
Preserves existing 'Ivan_Dsouza_RetainIQ_Blackbook.docx/pdf' untouched.
"""

import os
import sys
import subprocess
import pypdf
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from shubham_style_helpers import (
    format_paragraph, add_body_p, add_heading_1, add_heading_2, add_heading_3,
    add_figure, add_code_listing, set_cell_background, set_cell_margins, set_table_borders
)

def add_header_footer(doc):
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.1)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = True
        
        # Header (Shubham-style: simple elegant topic header)
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("RetainIQ: Survival Churn Modeling & Personalized Treatment Ranking")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(8.5)
        hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(115, 125, 135)
        
        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("KES' Shroff College  |  B.Sc. Data Science  |  Page ")
        frun.font.name = "Times New Roman"
        frun.font.size = Pt(9)
        frun.font.color.rgb = RGBColor(100, 110, 120)
        fld = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
        fp._p.append(fld)

def build_test_frontmatter(doc, toc_data=None):
    # ==========================================
    # PAGE 1: COVER PAGE
    # ==========================================
    p_inst = doc.add_paragraph()
    format_paragraph(p_inst, space_before=10, space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
    r1 = p_inst.add_run("Kandivli Education Society's\n")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(15, 30, 65)

    r2 = p_inst.add_run("BK Shroff College of Arts & MH Shroff College of Commerce\n")
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(15)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(15, 30, 65)

    r3 = p_inst.add_run("(Autonomous College | NAAC Re-accredited 'A' Grade | ISO 9001:2015 Certified)\nBhulabhai Patel Road, Kandivali (West), Mumbai - 400067")
    r3.font.name = "Times New Roman"
    r3.font.size = Pt(10)
    r3.font.color.rgb = RGBColor(70, 80, 95)

    p_div = doc.add_paragraph()
    format_paragraph(p_div, space_before=15, space_after=15, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_div = p_div.add_run("—" * 38)
    r_div.font.color.rgb = RGBColor(180, 190, 200)

    p_rep = doc.add_paragraph()
    format_paragraph(p_rep, space_before=10, space_after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_rep = p_rep.add_run("A CAPSTONE PROJECT REPORT ON\n")
    r_rep.font.name = "Times New Roman"
    r_rep.font.size = Pt(12)
    r_rep.font.bold = True
    r_rep.font.color.rgb = RGBColor(100, 110, 125)

    p_title = doc.add_paragraph()
    format_paragraph(p_title, space_before=12, space_after=8, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_title = p_title.add_run("SURVIVAL-BASED CHURN MODELING WITH PERSONALIZED RETENTION TREATMENT RANKING")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(18)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(15, 35, 75)

    p_proj = doc.add_paragraph()
    format_paragraph(p_proj, space_before=4, space_after=20, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_proj = p_proj.add_run("(RetainIQ  |  Project ID: BDS-11)")
    r_proj.font.name = "Times New Roman"
    r_proj.font.size = Pt(12)
    r_proj.font.italic = True
    r_proj.font.color.rgb = RGBColor(40, 60, 90)

    p_sub = doc.add_paragraph()
    format_paragraph(p_sub, space_before=10, space_after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_sub = p_sub.add_run("SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENTS\nFOR THE DEGREE OF\n")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(10.5)
    r_sub.font.color.rgb = RGBColor(80, 90, 100)

    r_deg = p_sub.add_run("BACHELOR OF SCIENCE (DATA SCIENCE)")
    r_deg.font.name = "Times New Roman"
    r_deg.font.size = Pt(13)
    r_deg.font.bold = True
    r_deg.font.color.rgb = RGBColor(20, 30, 50)

    p_auth = doc.add_paragraph()
    format_paragraph(p_auth, space_before=25, space_after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_sb = p_auth.add_run("SUBMITTED BY\n")
    r_sb.font.name = "Times New Roman"
    r_sb.font.size = Pt(10.5)
    r_sb.font.bold = True
    r_sb.font.color.rgb = RGBColor(90, 100, 115)

    r_name = p_auth.add_run("MR. IVAN DSOUZA\n")
    r_name.font.name = "Times New Roman"
    r_name.font.size = Pt(14)
    r_name.font.bold = True
    r_name.font.color.rgb = RGBColor(15, 30, 65)

    r_rn = p_auth.add_run("Roll No.: TDDS013A  |  PRN: 2023016401824103\nT.Y. B.Sc. Data Science  |  Semester VI")
    r_rn.font.name = "Times New Roman"
    r_rn.font.size = Pt(11)
    r_rn.font.color.rgb = RGBColor(50, 60, 75)

    p_gui = doc.add_paragraph()
    format_paragraph(p_gui, space_before=22, space_after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_ug = p_gui.add_run("UNDER THE ESTEEMED GUIDANCE OF\n")
    r_ug.font.name = "Times New Roman"
    r_ug.font.size = Pt(10.5)
    r_ug.font.bold = True
    r_ug.font.color.rgb = RGBColor(90, 100, 115)

    r_gname = p_gui.add_run("Mr./Ms. __________________________\nDepartment of Data Science & Information Technology")
    r_gname.font.name = "Times New Roman"
    r_gname.font.size = Pt(12)
    r_gname.font.bold = True
    r_gname.font.color.rgb = RGBColor(20, 30, 50)

    p_yr = doc.add_paragraph()
    format_paragraph(p_yr, space_before=30, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_yr = p_yr.add_run("ACADEMIC YEAR 2025 – 2026")
    r_yr.font.name = "Times New Roman"
    r_yr.font.size = Pt(12)
    r_yr.font.bold = True
    r_yr.font.color.rgb = RGBColor(15, 30, 65)

    doc.add_page_break()

    # ==========================================
    # PAGE 2: CERTIFICATE
    # ==========================================
    p_c1 = doc.add_paragraph()
    format_paragraph(p_c1, space_before=15, space_after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    rc1 = p_c1.add_run("Kandivli Education Society's\nBK Shroff College of Arts & MH Shroff College of Commerce\n")
    rc1.font.name = "Times New Roman"
    rc1.font.size = Pt(13)
    rc1.font.bold = True
    rc1.font.color.rgb = RGBColor(15, 30, 65)

    rc2 = p_c1.add_run("Kandivali (West), Mumbai - 400067\nDEPARTMENT OF DATA SCIENCE")
    rc2.font.name = "Times New Roman"
    rc2.font.size = Pt(11)
    rc2.font.bold = True
    rc2.font.color.rgb = RGBColor(40, 55, 80)

    p_ct = doc.add_paragraph()
    format_paragraph(p_ct, space_before=20, space_after=18, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_ct = p_ct.add_run("CERTIFICATE")
    r_ct.font.name = "Times New Roman"
    r_ct.font.size = Pt(17)
    r_ct.font.bold = True
    r_ct.font.underline = True
    r_ct.font.color.rgb = RGBColor(15, 30, 65)

    cert_text = (
        "This is to certify that Mr. IVAN DSOUZA, a bonafide student of THIRD YEAR Bachelor of Science "
        "in DATA SCIENCE (Semester VI), Division: A, Roll No.: TDDS013A, has successfully completed the "
        "Capstone Project entitled 'SURVIVAL-BASED CHURN MODELING WITH PERSONALIZED RETENTION TREATMENT RANKING' "
        "(RetainIQ, Project ID: BDS-11) during the Academic Year 2025 – 2026, in partial fulfillment of the requirements "
        "for the award of the Degree of Bachelor of Science (Data Science) affiliated with the University of Mumbai, "
        "under the curriculum guidelines of KES' Shroff College of Arts & Commerce (Autonomous)."
    )
    add_body_p(doc, cert_text, space_before=8, space_after=12, line_spacing=1.2)

    cert_text2 = (
        "The project work incorporates original research, empirical survival analysis, heterogeneous treatment effect "
        "estimation, prescriptive decision optimization, cryptographic audit logging, automated unit/integration testing, "
        "and production web microservice deployment carried out under institutional supervision."
    )
    add_body_p(doc, cert_text2, space_before=4, space_after=40, line_spacing=1.2)

    # Signatures Table
    sig_table = doc.add_table(rows=2, cols=3)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    sig_table.autofit = False
    
    col_widths = [Inches(2.1), Inches(2.1), Inches(2.1)]
    for row in sig_table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    c0, c1, c2 = sig_table.cell(0, 0), sig_table.cell(0, 1), sig_table.cell(0, 2)
    c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    c0.paragraphs[0].add_run("_____________________\nMr./Ms. ____________________\nProject Guide\nDept. of Data Science").font.size = Pt(10)

    c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    c1.paragraphs[0].add_run("_____________________\nMs. Sweta Suman\nTeacher In-charge\nCoordinator, B.Sc. DS").font.size = Pt(10)

    c2.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    c2.paragraphs[0].add_run("_____________________\nDr. Lily Bhushan\nPrincipal\nKES' Shroff College").font.size = Pt(10)

    # Row 1: External Examiner & College Seal
    c_ex0, c_ex1, c_ex2 = sig_table.cell(1, 0), sig_table.cell(1, 1), sig_table.cell(1, 2)
    format_paragraph(c_ex0.paragraphs[0], space_before=30, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
    c_ex0.paragraphs[0].add_run("_____________________\nExternal Examiner\nDate: ____ / ____ / 2026").font.size = Pt(10)

    format_paragraph(c_ex1.paragraphs[0], space_before=30, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_seal = c_ex1.paragraphs[0].add_run("COLLEGE SEAL / STAMP")
    r_seal.font.size = Pt(9.5)
    r_seal.font.color.rgb = RGBColor(120, 130, 140)

    format_paragraph(c_ex2.paragraphs[0], space_before=30, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
    c_ex2.paragraphs[0].add_run("_____________________\nInternal Examiner\nDate: ____ / ____ / 2026").font.size = Pt(10)

    doc.add_page_break()

    # ==========================================
    # PAGE 3: PROFORMA FOR APPROVAL
    # ==========================================
    p_phead = doc.add_paragraph()
    format_paragraph(p_phead, space_before=10, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_ph = p_phead.add_run("PROFORMA FOR THE APPROVAL OF PROJECT PROPOSAL\nACADEMIC YEAR 2025 – 2026")
    r_ph.font.name = "Times New Roman"
    r_ph.font.size = Pt(14)
    r_ph.font.bold = True
    r_ph.font.color.rgb = RGBColor(15, 30, 65)

    prof_tbl = doc.add_table(rows=7, cols=2)
    prof_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(prof_tbl, color="90A0B0", sz="6", val="single")

    prof_data = [
        ("Roll No. & Division:", "TDDS013A  |  Division A"),
        ("Student Name:", "IVAN DSOUZA"),
        ("Programme / Class:", "Bachelor of Science (Data Science)  |  T.Y. B.Sc. Semester VI"),
        ("Project Title:", "SURVIVAL-BASED CHURN MODELING WITH PERSONALIZED RETENTION TREATMENT RANKING (RetainIQ)"),
        ("Project Identification ID:", "BDS-11"),
        ("Name of Project Guide:", "Mr./Ms. __________________________"),
        ("Specialization Track:", "Advanced Machine Learning, Causal Inference & Time-to-Event Analytics")
    ]

    for idx, (label, val) in enumerate(prof_data):
        row = prof_tbl.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(4.2)
        set_cell_background(c0, "F0F4F8")
        set_cell_margins(c0, top=90, bottom=90, left=120, right=100)
        set_cell_margins(c1, top=90, bottom=90, left=120, right=100)
        
        c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        r_l = c0.paragraphs[0].add_run(label)
        r_l.font.name = "Times New Roman"
        r_l.font.size = Pt(10.5)
        r_l.font.bold = True

        c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        r_v = c1.paragraphs[0].add_run(val)
        r_v.font.name = "Times New Roman"
        r_v.font.size = Pt(10.5)

    p_spc = doc.add_paragraph()
    format_paragraph(p_spc, space_before=25, space_after=10)

    prof_sig_tbl = doc.add_table(rows=1, cols=3)
    prof_sig_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, width in enumerate([Inches(2.1), Inches(2.1), Inches(2.1)]):
        prof_sig_tbl.rows[0].cells[idx].width = width

    pc0, pc1, pc2 = prof_sig_tbl.rows[0].cells[0], prof_sig_tbl.rows[0].cells[1], prof_sig_tbl.rows[0].cells[2]
    pc0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    pc0.paragraphs[0].add_run("_____________________\nSignature of the Student\nDate: ____ / ____ / 2026").font.size = Pt(10)

    pc1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    pc1.paragraphs[0].add_run("_____________________\nSignature of the Guide\nDate: ____ / ____ / 2026").font.size = Pt(10)

    pc2.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    pc2.paragraphs[0].add_run("_____________________\nSignature of Coordinator\nDate: ____ / ____ / 2026").font.size = Pt(10)

    doc.add_page_break()

    # ==========================================
    # PAGE 4: ABSTRACT
    # ==========================================
    p_absh = doc.add_paragraph()
    format_paragraph(p_absh, space_before=10, space_after=10, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_absh = p_absh.add_run("ABSTRACT")
    r_absh.font.name = "Times New Roman"
    r_absh.font.size = Pt(16)
    r_absh.font.bold = True
    r_absh.font.color.rgb = RGBColor(15, 30, 65)

    add_body_p(
        doc,
        "Customer churn represents an existential financial risk across modern subscription economies, where customer acquisition costs "
        "frequently outstrip retention investments by five- to seven-fold. Conventional industry practices treat churn as a static binary "
        "classification problem, which introduces severe theoretical flaws: survival blindness (ignoring the temporal dimension of attrition) "
        "and right-censoring distortion (penalizing active subscribers as non-events). Furthermore, marketing teams frequently mistarget "
        "interventions toward 'Lost Causes' (customers determined to churn regardless of treatment) while ignoring high-leverage 'Persuadables'.",
        bold_prefix="Problem Statement: "
    )

    add_body_p(
        doc,
        "This project introduces RetainIQ (Project ID: BDS-11), an end-to-end enterprise decision-support ecosystem that unifies continuous-time "
        "statistical survival analysis with causal uplift meta-learning and prescriptive economic optimization. RetainIQ replaces point-in-time "
        "churn probabilities with continuous survival probability curves S(t) = P(T > t) and hazard functions h(t). The system benchmarks "
        "four foundational survival modeling paradigms: non-parametric Kaplan-Meier estimation, semi-parametric Cox Proportional Hazards (M1), "
        "parametric Weibull Accelerated Failure Time (M2), and Random Survival Forests (M3) across 7,043 telecommunications subscribers.",
        bold_prefix="Methodology & Architecture: "
    )

    add_body_p(
        doc,
        "Empirical benchmarks confirm that Weibull AFT and Cox Proportional Hazards achieve peak discriminatory power with test Concordance Indices "
        "(C-Index) of 0.8697 and 0.8694 respectively, vastly outperforming a naive binary baseline (0.8283). At the operational 90-day horizon, "
        "the Weibull AFT model yields an exceptional Integrated Brier Score (IBS) of 0.0818. Deploying T-Learner causal meta-models isolates "
        "individual counterfactual uplift (Delta S) across four treatments, achieving a mean Qini score of 0.6920. Prescriptive knapsack optimization "
        "evaluates Expected Retention Value (ERV = Delta S * LTV - Cost), capturing $48,920 in Net ERV at an outstanding 329.2% ROI under a $15,000 "
        "budget. An immutable SHA-256 cryptographic audit trail and an 11-page dark-themed Streamlit cockpit deliver full enterprise governance.",
        bold_prefix="Results & Practical Value: "
    )

    p_kw = doc.add_paragraph()
    format_paragraph(p_kw, space_before=14, space_after=6)
    r_kw = p_kw.add_run("Keywords: ")
    r_kw.font.name = "Times New Roman"
    r_kw.font.size = Pt(10.5)
    r_kw.font.bold = True
    r_kwt = p_kw.add_run(
        "Survival Analysis, Right Censoring, Kaplan-Meier, Cox Proportional Hazards, Weibull AFT, "
        "Random Survival Forests, Causal Uplift Modeling, T-Learner, Expected Retention Value (ERV), "
        "Prescriptive Optimization, Cryptographic Audit Trail, FastAPI, Streamlit."
    )
    r_kwt.font.name = "Times New Roman"
    r_kwt.font.size = Pt(10)
    r_kwt.font.italic = True

    doc.add_page_break()

    # ==========================================
    # PAGE 5: ACKNOWLEDGEMENT
    # ==========================================
    p_ackh = doc.add_paragraph()
    format_paragraph(p_ackh, space_before=10, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_ah = p_ackh.add_run("ACKNOWLEDGEMENT")
    r_ah.font.name = "Times New Roman"
    r_ah.font.size = Pt(16)
    r_ah.font.bold = True
    r_ah.font.color.rgb = RGBColor(15, 30, 65)

    add_body_p(
        doc,
        "The completion of this Capstone Project, entitled 'SURVIVAL-BASED CHURN MODELING WITH PERSONALIZED "
        "RETENTION TREATMENT RANKING' (RetainIQ, Project ID: BDS-11), has been an enriching academic and technical "
        "endeavor. I take this opportunity to express my profound gratitude to everyone who contributed their invaluable "
        "mentorship, guidance, and encouragement throughout this project."
    )

    add_body_p(
        doc,
        "First and foremost, I express my deepest sense of gratitude to my esteemed Project Guide, Mr./Ms. __________________________, "
        "Department of Data Science, for their intellectual mentorship, constructive criticism, and continuous support throughout the "
        "modeling, implementation, and reporting phases."
    )

    add_body_p(
        doc,
        "I extend my sincere thanks to Ms. Sweta Suman, Teacher In-charge and Course Coordinator of the B.Sc. Data Science programme, "
        "for providing an academically rigorous environment, laboratory infrastructure, and administrative guidance throughout the academic year."
    )

    add_body_p(
        doc,
        "I also convey my deep respect and gratitude to our respected Principal, Dr. Lily Bhushan, whose visionary leadership and "
        "encouragement have continually inspired us to achieve academic and applied technical excellence."
    )

    add_body_p(
        doc,
        "Finally, I am profoundly grateful to my parents and family members for their constant moral and emotional support, and to my "
        "classmates for their thoughtful discussions and collaborative spirit.",
        space_after=40
    )

    p_asig = doc.add_paragraph()
    format_paragraph(p_asig, space_before=15, space_after=0, align=WD_ALIGN_PARAGRAPH.RIGHT)
    ras = p_asig.add_run("MR. IVAN DSOUZA\nRoll No.: TDDS013A\nT.Y. B.Sc. Data Science, Semester VI\nKES' Shroff College, Mumbai")
    ras.font.name = "Times New Roman"
    ras.font.size = Pt(11)
    ras.font.bold = True
    ras.font.color.rgb = RGBColor(15, 30, 65)

    doc.add_page_break()

    # ==========================================
    # PAGE 6: DECLARATION
    # ==========================================
    p_dech = doc.add_paragraph()
    format_paragraph(p_dech, space_before=10, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_dh = p_dech.add_run("DECLARATION")
    r_dh.font.name = "Times New Roman"
    r_dh.font.size = Pt(16)
    r_dh.font.bold = True
    r_dh.font.color.rgb = RGBColor(15, 30, 65)

    add_body_p(
        doc,
        "I, MR. IVAN DSOUZA, student of Third Year Bachelor of Science in Data Science (Semester VI), Division: A, "
        "Roll No.: TDDS013A, studying at Kandivli Education Society's BK Shroff College of Arts & MH Shroff College of "
        "Commerce (Autonomous), Kandivali (West), Mumbai - 400067, hereby declare that the Capstone Project report entitled:",
        space_before=10, space_after=10
    )

    p_dtitle = doc.add_paragraph()
    format_paragraph(p_dtitle, space_before=10, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    rdt = p_dtitle.add_run("“SURVIVAL-BASED CHURN MODELING WITH PERSONALIZED RETENTION TREATMENT RANKING”\n(RetainIQ  |  Project ID: BDS-11)")
    rdt.font.name = "Times New Roman"
    rdt.font.size = Pt(13)
    rdt.font.bold = True
    rdt.font.color.rgb = RGBColor(15, 35, 75)

    add_body_p(
        doc,
        "represents my own authentic, original work carried out under the supervision of my project guide, "
        "Mr./Ms. __________________________, Department of Data Science, KES' Shroff College, during the Academic Year 2025 – 2026."
    )

    add_body_p(
        doc,
        "I further affirm that this project report has been compiled by me in partial fulfillment of the academic requirements "
        "for the degree of Bachelor of Science (Data Science). To the best of my knowledge and belief, this work contains no "
        "material previously published or written by another person, nor has any part of this work been submitted previously "
        "to this or any other university, institute, or examining body for the award of any degree, diploma, or qualification.",
        space_after=45
    )

    p_dsig = doc.add_paragraph()
    format_paragraph(p_dsig, space_before=20, space_after=0, align=WD_ALIGN_PARAGRAPH.RIGHT)
    rds = p_dsig.add_run("_______________________________\nMR. IVAN DSOUZA\nRoll No.: TDDS013A\nDate: ____ / ____ / 2026\nPlace: Mumbai")
    rds.font.name = "Times New Roman"
    rds.font.size = Pt(11)
    rds.font.bold = True
    rds.font.color.rgb = RGBColor(15, 30, 65)

    doc.add_page_break()

    # ==========================================
    # PAGES 7-8: TABLE OF CONTENTS (Shubham-style)
    # ==========================================
    p_toch = doc.add_paragraph()
    format_paragraph(p_toch, space_before=10, space_after=10, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_th = p_toch.add_run("TABLE OF CONTENTS")
    r_th.font.name = "Times New Roman"
    r_th.font.size = Pt(16)
    r_th.font.bold = True
    r_th.font.color.rgb = RGBColor(15, 30, 65)

    toc_table = doc.add_table(rows=1, cols=3)
    toc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(toc_table, color="A0B0C0", sz="4", val="single")

    h0, h1, h2 = toc_table.rows[0].cells[0], toc_table.rows[0].cells[1], toc_table.rows[0].cells[2]
    h0.width, h1.width, h2.width = Inches(1.1), Inches(4.5), Inches(0.9)
    for h, title in [(h0, "SR. NO."), (h1, "TOPIC / CHAPTER TITLE"), (h2, "PAGE NO.")]:
        set_cell_background(h, "152035")
        set_cell_margins(h, top=70, bottom=70, left=90, right=70)
        p = h.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if h != h1 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(title)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    shubham_toc = [
        ("1", "INTRODUCTION", "1–7"),
        ("1.1", "SIGNIFICANCE", "2"),
        ("1.2", "OBJECTIVES", "3"),
        ("1.3", "PURPOSE AND SCOPE", "4"),
        ("1.3.1", "PURPOSE", "4"),
        ("1.3.2", "SCOPE", "5"),
        ("1.4", "APPLICABILITY", "6"),
        ("1.5", "ACHIEVEMENTS", "7"),
        ("", "", ""),
        ("2", "SYSTEM ANALYSIS", "8–16"),
        ("2.1", "EXISTING SYSTEM", "8"),
        ("2.2", "PROPOSED SYSTEM", "9"),
        ("2.3", "REQUIREMENT ANALYSIS", "10"),
        ("2.4", "HARDWARE REQUIREMENTS", "13"),
        ("2.5", "SOFTWARE REQUIREMENTS", "14"),
        ("2.6", "SURVEY OF TECHNOLOGY", "16"),
        ("", "", ""),
        ("3", "SYSTEM DESIGN", "18–26"),
        ("3.1", "MODULE DIVISION", "18"),
        ("3.2", "GANTT CHART", "20"),
        ("3.3", "SYSTEM ARCHITECTURE / E-R DIAGRAM", "21"),
        ("3.4", "DATA FLOW REPRESENTATION", "22"),
        ("3.4.1", "DATA FLOW DIAGRAM", "22"),
        ("3.5", "UML DIAGRAMS", "23"),
        ("3.5.1", "CLASS DIAGRAM", "23"),
        ("3.5.2", "SEQUENCE DIAGRAM", "24"),
        ("3.5.3", "STATE CHART DIAGRAM", "25"),
        ("3.5.4", "USE-CASE DIAGRAM", "26"),
        ("", "", ""),
        ("4", "IMPLEMENTATION AND TESTING", "27–33"),
        ("4.1", "CODE", "27"),
        ("4.2", "TESTING APPROACH", "30"),
        ("", "", ""),
        ("5", "RESULTS AND DISCUSSIONS", "34–39"),
        ("5.1", "FUNCTIONALITY EVALUATION", "34"),
        ("5.2", "USER EXPERIENCE ASSESSMENT & SYSTEM EVALUATION", "38"),
        ("", "", ""),
        ("6", "CONCLUSION AND FUTURE WORK", "40–41"),
        ("6.1", "CONCLUSION", "40"),
        ("6.2", "FUTURE SCOPE", "40"),
        ("6.3", "LIMITATIONS", "41"),
        ("", "", ""),
        ("7", "REFERENCES", "48–49"),
        ("", "", ""),
        ("A", "APPENDIX: REPRODUCIBILITY & ARTIFACT CHECKSUM AUDIT", "50–51")
    ]

    toc_list = toc_data if toc_data is not None else shubham_toc
    for sr, topic, page in toc_list:
        row = toc_table.add_row()
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = Inches(1.1), Inches(4.5), Inches(0.9)
        set_cell_margins(c0, top=26, bottom=26, left=60, right=40)
        set_cell_margins(c1, top=26, bottom=26, left=60, right=40)
        set_cell_margins(c2, top=26, bottom=26, left=60, right=40)

        is_chap = (sr.isdigit() and len(sr) == 1)
        bg_col = "F4F6F9" if is_chap else "FFFFFF"
        for c in [c0, c1, c2]:
            set_cell_background(c, bg_col)

        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.paragraph_format.line_spacing = 1.05
        r0 = p0.add_run(sr)
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(8.5)
        if is_chap:
            r0.font.bold = True

        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p1.paragraph_format.line_spacing = 1.05
        r1 = p1.add_run(topic)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(8.5)
        if is_chap:
            r1.font.bold = True
            r1.font.color.rgb = RGBColor(15, 30, 60)

        p2 = c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.line_spacing = 1.05
        r2 = p2.add_run(page)
        r2.font.name = "Times New Roman"
        r2.font.size = Pt(8.5)
        if is_chap:
            r2.font.bold = True

    doc.add_page_break()
    print("Test front matter generated.")

if __name__ == '__main__':
    print("Test front matter module ready.")
