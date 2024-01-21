import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import wikipediaapi

# Download the necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_keywords(sentence):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)

    # Perform part-of-speech tagging
    pos_tags = pos_tag(tokens)

    # Extracting nouns and proper nouns as main keywords
    keywords = [word for word, pos in pos_tags if pos in ['NN', 'NNS', 'NNP', 'NNPS']]

    return keywords

def get_wikipedia_data(query):
    # Specify a user agent
    user_agent = "chat-bot/1.0 (srivatsavdamaraju2@gmail.com)"
    wiki_wiki = wikipediaapi.Wikipedia('en', extract_format=wikipediaapi.ExtractFormat.WIKI, headers={'User-Agent': user_agent})
    page_py = wiki_wiki.page(query)

    if page_py.exists():
        return page_py.text[:500]  # Return first 500 characters of the page text
    else:
        return "not found in database .please rephrase your query "

def main():
    st.title("Wikipedia Chatbot")

    user_input = st.text_input("User:")
    
    if user_input.lower() == 'exit':
        st.write("Chatbot exiting.")
    else:
        keywords = extract_keywords(user_input)
        if keywords:
            main_keyword = keywords[0]
            result = get_wikipedia_data(main_keyword)
            st.write("Chatbot:", result)
        else:
            st.write("No significant keywords found.")

if __name__ == "__main__":
    main()
