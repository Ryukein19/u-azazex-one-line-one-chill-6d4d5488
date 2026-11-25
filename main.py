import os
# One-liner entry (200 chars max): the line below is the entire submission.
# Writes the line to /output/entry.txt.
LINE = "She checked the baby monitor twice. The third time, it was already looking back at her."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
