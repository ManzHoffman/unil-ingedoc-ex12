import re
from pathlib import Path

# File paths
input_path = "martin_clean.txt"  # Replace this path
output_path = "result/martin_clean.xml"

# Read input
text = Path(input_path).read_text(encoding="utf-8")

# Tag scene headings like "SCÈNE I"
text = re.sub(r'^(SCÈNE\s[IVXLCDM]{1,6})', r'<head>\1</head>', text, flags=re.MULTILINE)

# Stage directions in (_..._)
text = re.sub(r'\(_(.*?)_\)', r'<stage>\1</stage>', text, flags=re.DOTALL)

# Inline cues: _..._
text = re.sub(r'_(.*?)_', r'<cue>\1</cue>', text, flags=re.DOTALL)

# Inline lines: --...--
text = re.sub(r'--(.*?)--', r'<l>\1</l>', text, flags=re.DOTALL)

# Insert </p></sp> before <head> (except first one)
text = re.sub(r'(?<!^)\n<head>', r'</p></sp>\n<head>', text)

# Insert <sp><p> AFTER each <head>
text = re.sub(r'(<head>.*?</head>)', r'\1\n<sp><p>', text, flags=re.DOTALL)

# Tag speakers: uppercase names
text = re.sub(
    r'(?m)^([A-ZÉÈÀÙÂÊÎÔÛÄËÏÖÜÇ]{4,})(?=(\s*<stage>|\.|:|\s*$))',
    r'</p></sp>\n<sp><speaker>\1</speaker><p>',
    text
)

# Final tag balancing
open_sp = text.count('<sp>')
close_sp = text.count('</sp>')
if open_sp > close_sp:
    text += '</p></sp>\n' * (open_sp - close_sp)

# Wrap entire body
text = '<?xml version="1.0" encoding="UTF-8"?>\n<body>\n' + text.strip() + '\n</body>'

# Write output
Path(output_path).parent.mkdir(parents=True, exist_ok=True)
Path(output_path).write_text(text, encoding="utf-8")

print(f"✅ Fixed XML saved to: {output_path}")
