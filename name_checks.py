import spacy
import docx2txt
import re

nlp = spacy.load("en_core_web_lg")

orignal = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\old\393040521_TM_HS\Orignals\ORIGNAL_merge.docx"
translation = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\old\393040521_TM_HS\Translation\Perfectit\PERFECTIT_merge.docx"

    
def find_persons_docx_spacy_regex(orignal, translation):
    
    orignal_text = docx2txt.process(orignal)
    orignal_text = orignal_text.replace('\n', ' ').replace('\t', ' ')
    translation_text = docx2txt.process(translation)
    translation_text = translation_text.replace('\n', ' ').replace('\t', ' ')
    
    doc1 = nlp(orignal_text)
    doc2 = nlp(translation_text)
    
    persons_orignal_sp = [ent.text for ent in doc1.ents if ent.label_ == 'PERSON']
    persons_translation_sp = [ent.text for ent in doc2.ents if ent.label_ == 'PERSON']
    spacy_names = sorted(set([n for n in persons_translation_sp if n not in persons_orignal_sp]))

    
    print('SPACY RESULTS')
    print('\n')
    
    for n in spacy_names:
        print(n)
