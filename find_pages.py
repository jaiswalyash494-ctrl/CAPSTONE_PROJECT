import pypdf

reader = pypdf.PdfReader('Ivan_Dsouza_RetainIQ_Blackbook.pdf')
pages_text = [p.extract_text().upper() for p in reader.pages]

headers_to_find = [
    ('CH1', 'CHAPTER 1: INTRODUCTION'),
    ('1.1', '1.1 SIGNIFICANCE'),
    ('1.2', '1.2 PROJECT OBJECTIVES'),
    ('1.3', '1.3 PURPOSE AND SCOPE'),
    ('1.4', '1.4 ENTERPRISE APPLICABILITY'),
    ('1.5', '1.5 TECHNICAL AND EMPIRICAL ACHIEVEMENTS'),
    ('CH2', 'CHAPTER 2: SYSTEM ANALYSIS'),
    ('2.1', '2.1 EXISTING SYSTEM'),
    ('2.2', '2.2 PROPOSED SYSTEM'),
    ('2.3', '2.3 REQUIREMENTS ANALYSIS'),
    ('2.4', '2.4 HARDWARE REQUIREMENTS'),
    ('2.5', '2.5 SOFTWARE REQUIREMENTS'),
    ('2.6', '2.6 SURVEY OF TECHNOLOGY'),
    ('CH3', 'CHAPTER 3: SYSTEM DESIGN'),
    ('3.1', '3.1 MODULE DIVISION'),
    ('3.2', '3.2 SYSTEM ARCHITECTURE'),
    ('3.3', '3.3 PROJECT DEVELOPMENT GANTT'),
    ('3.4', '3.4 DATA FLOW REPRESENTATION'),
    ('3.5', '3.5 UNIFIED MODELING LANGUAGE'),
    ('3.6', '3.6 DATA MODEL AND CONFIGURATION'),
    ('CH4', 'CHAPTER 4: IMPLEMENTATION AND TESTING'),
    ('4.1', '4.1 DATA INGESTION'),
    ('4.2', '4.2 LEAKAGE PREVENTION'),
    ('4.3', '4.3 SURVIVAL MODELING ENGINE'),
    ('4.4', '4.4 CAUSAL UPLIFT'),
    ('4.5', '4.5 PERSONALIZED RANKING'),
    ('4.6', '4.6 REPRESENTATIVE SOURCE CODE'),
    ('4.7', '4.7 TESTING METHODOLOGY'),
    ('4.8', '4.8 AUTOMATED TEST RESULTS MATRIX'),
    ('CH5', 'CHAPTER 5: RESULTS AND DISCUSSIONS'),
    ('5.1', '5.1 DATASET COMPOSITION'),
    ('5.2', '5.2 DATA QUALITY'),
    ('5.3', '5.3 KAPLAN-MEIER'),
    ('5.4', '5.4 SURVIVAL MODEL BENCHMARKING'),
    ('5.5', '5.5 TIME-DEPENDENT PROBABILITY'),
    ('5.6', '5.6 CUSTOMER CHURN RISK'),
    ('5.7', '5.7 TREATMENT EFFECT & UPLIFT'),
    ('5.8', '5.8 PRESCRIPTIVE RANKING & PORTFOLIO'),
    ('5.9', '5.9 MODEL EXPLAINABILITY'),
    ('5.10', '5.10 SYSTEM ROBUSTNESS'),
    ('5.11', '5.11 POPULATION DRIFT'),
    ('5.12', '5.12 INTERACTIVE DASHBOARD'),
    ('CH6', 'CHAPTER 6: CONCLUSION AND FUTURE WORK'),
    ('6.1', '6.1 PROJECT SYNTHESIS'),
    ('6.2', '6.2 FUTURE SCOPE'),
    ('6.3', '6.3 REAL-WORLD OPERATIONAL'),
    ('CH7', 'CHAPTER 7: REFERENCES')
]

print("=== PRELIMINARY PAGES ===")
for i in range(13):
    lines = [l.strip() for l in pages_text[i].split('\n') if l.strip() and 'RETAINIQ:' not in l and 'KES\'' not in l]
    f = lines[0] if lines else "[EMPTY]"
    print(f"Page {i+1:02d}: {f}")

print("\n=== MAIN BODY HEADINGS ===")
for tag, h in headers_to_find:
    found_pg = None
    for i in range(12, len(pages_text)):
        if h in pages_text[i]:
            found_pg = i + 1
            break
    print(f"{tag:5} | {h:45} : Page {found_pg}")
