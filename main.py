import os

LINE = "I unplugged the toaster to save power. It now judges me from the counter, cold, dark, and somehow still disappointed."
# Verified count: 117 characters (117 bytes UTF-8), 1-280 range, not whitespace only.

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
out_path = os.path.join(out_dir, 'entry.txt')

os.makedirs(out_dir, exist_ok=True)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(f"Wrote {len(LINE.encode('utf-8'))} bytes to {out_path}")
