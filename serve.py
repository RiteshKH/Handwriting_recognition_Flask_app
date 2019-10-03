from cursive.main import main

# Function that takes loads in our pickled word processor
# and defines a function for using it. This makes it easy
# to do these steps together when serving our model.
def get_cursive_api():
    
    # read in pickled word processor. You could also load in
    # other models as this step.
#    keyword_processor = pickle.load(open("processor.pkl", "rb"))
    
    # Function to apply our model & extract keywords from a 
    # provided bit of text
    def cursive_api(path): 
#        keywords_found = keywordProcessor.extract_keywords(text, span_info=True)  
        rec_char = []
        rec_char = main(path)
        return rec_char
    
    # return the function we just defined
    return cursive_api