import docx2txt
import re
from collections import Counter


orignal = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\old\393040521_TM_HS\Orignals\ORIGNAL_merge.docx"
orignal_text = docx2txt.process(orignal)

translation = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\old\393040521_TM_HS\Translation\Perfectit\PERFECTIT_merge.docx"
translation_text = docx2txt.process(translation)

orignal_names = set(re.findall("[A-Z][a-z]+ [A-Z][a-z]+" , orignal_text))
translation_names = set(re.findall("[A-Z][a-z]+ [A-Z][a-z]+" , translation_text))

combo = list(orignal_names) + list(translation_names)
counts = Counter(combo)
sorted(counts.items())
