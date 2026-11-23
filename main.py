import os

JOKE = "My AI agent debugged my code for an hour, then concluded the bug was me."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
