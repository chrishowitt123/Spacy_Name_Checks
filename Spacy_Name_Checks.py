import spacy
import docx2txt
import re

"""
A program that checks that the names of people match between a source and target document.

"""

# load corpus
nlp = spacy.load("en_core_web_lg")

# define documents
source = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\old\393040521_TM_HS\Orignals\ORIGNAL_merge.docx"
target = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\old\393040521_TM_HS\Translation\Perfectit\PERFECTIT_merge.docx"

    
def find_persons_docx_spacy(source, target):
    
    # clean source and target text
    source_text = docx2txt.process(source)
    source_text = source_text.replace('\n', ' ').replace('\t', ' ')
    target_text = docx2txt.process(target)
    target_text = target_text.replace('\n', ' ').replace('\t', ' ')
    
    # define nlp docs
    doc1 = nlp(source_text)
    doc2 = nlp(target_text)
    
    # add named entities into source and target lists
    persons_source_sp = [ent.text for ent in doc1.ents if ent.label_ == 'PERSON']
    persons_target_sp = [ent.text for ent in doc2.ents if ent.label_ == 'PERSON']
    spacy_names = sorted(set([n for n in persons_target_sp if n not in persons_source_sp]))

    # return results
    print('SPACY RESULTS')
    print('\n')
    
    for n in spacy_names:
        print(n)
