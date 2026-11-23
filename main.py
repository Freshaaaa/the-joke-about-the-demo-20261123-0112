import os

JOKE = "My AI agent debugged my code for an hour, then concluded the bug was me."

def write_entry(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    write_entry(os.path.join(out, "entry.txt"), JOKE)

if __name__ == "__main__":
    main()
