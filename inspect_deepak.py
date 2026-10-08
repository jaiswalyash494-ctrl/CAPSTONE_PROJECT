import docx
import os

doc = docx.Document("DEEPAK CAPSTONE.docx")

print(f"Total paragraphs: {len(doc.paragraphs)}")
print(f"Total tables: {len(doc.tables)}")

headings = []
for p in doc.paragraphs:
    if p.style.name.startswith("Heading"):
        if p.text.strip():
            headings.append((p.style.name, p.text.strip()))
    elif any(run.bold for run in p.runs) and 3 < len(p.text.strip()) < 80:
        if p.text.strip():
            headings.append(("BoldLine", p.text.strip()))

print("Sample Headings in DEEPAK CAPSTONE.docx:")
for h in headings[:50]:
    print(h)

# Check text of first 100 paragraphs
with open("deepak_text_dump.txt", "w", encoding="utf-8") as f:
    for i, p in enumerate(doc.paragraphs[:150]):
        if p.text.strip():
            f.write(f"[{i}] {p.text}\n")
    f.write("\n--- TABLES ---\n")
    for t_idx, table in enumerate(doc.tables[:5]):
        f.write(f"\nTable {t_idx}:\n")
        for row in table.rows:
            f.write(" | ".join(cell.text.strip().replace("\n", " ") for cell in row.cells) + "\n")

print("Saved deepak_text_dump.txt")
