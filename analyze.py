import re


# This script analyze
path_of_clean_txt="martin_clean.txt"
output_path="result/martin_clean.xml"



#we open the clean text
text = open(path_of_clean_txt, encoding="utf-8").read()

text = re.sub(r'^(SCÈNE\s[IVXLCDM]{1,6})', r'<head>\1</head>\n', text, flags=re.MULTILINE)

text = re.sub(r'\(_(.*?)_\)', r'<stage>\1</stage>\n', text, flags= re.MULTILINE | re.DOTALL)

text = re.sub(r'_(.*?)_', r'<cue>\1</cue>\n', text, flags= re.MULTILINE | re.DOTALL)
text = re.sub(r'--(.*?)--', r'<l>\1</l>\n', text, flags= re.MULTILINE | re.DOTALL)

# insert 
text = re.sub(r'^([A-ZÉÈÀÙÂÊÎÔÛÄËÏÖÜÇ]+)\.\n', r'<sp><speaker>\1</speaker><p>\n', text, flags=re.MULTILINE)

text = re.sub(r'\n(?=[A-ZÉÈÀÙÂÊÎÔÛÄËÏÖÜÇ]+\.\n)', r'</p></sp>\n', text)

# Add XML header and root tag (optional, for proper XML structure)
text = '<?xml version="1.0" encoding="UTF-8"?>\n<body>\n' + text + '\n</body>'

# Export to XML file
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(text)
