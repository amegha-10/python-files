
import re

def clean_text(text):
    
    text = re.sub(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', '', text)  
    text = re.sub(r'\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b', '', text)    
    text = re.sub(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}\b', '', text, flags=re.IGNORECASE)

    
    text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '', text)

    
    text = re.sub(r'\s+', ' ', text)

    
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    
    text = re.sub(r'[.!?,]{2,}', '', text)

   
    return text.strip()


text = '''
Hello!!! Contact me at test.email@example.com on July 12, 2023 or 12/07/2023 😊😊
This is    a test... Are you coming??
'''

cleaned = clean_text(text)
print(cleaned)
