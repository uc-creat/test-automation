import nltk
from yake import KeywordExtractor
import spacy

def duplicateOne(text)->list:
  kw_extractor = KeywordExtractor()
  keywords = kw_extractor.extract_keywords(text)
  duplicates = []
  for kw in keywords:
      duplicates.append(kw[0])
  return duplicates

#checks the similarity between texts
def duplicateTwo(text):
   nlp = spacy.load("en_core_web_lg")
  #  ideally check should retrieve data from all the open tickets - through a for loop.
   check = """
      A couple of orgs is unable to add a payment method due to an error mentioned in the audit logs: Bankemoji payment profile was found but is not active.
      The org. is unable to add the card, due to an error.
      Error Message:
      Something went wrong when adding this payment method to your account"""
   text = nlp(str(text))
   check = nlp(str(check))
   return text.similarity(check)












