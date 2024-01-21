import streamlit as st
import spacy
import wikipediaapi

def extract_keywords(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    keywords = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    return keywords

def get_wikipedia_data(query):
    user_agent = "chat-bot/1.0 (srivatsavdamaraju2@gmail.com)"
    wiki_wiki = wikipediaapi.Wikipedia('en', extract_format=wikipediaapi.ExtractFormat.WIKI, headers={'User-Agent': user_agent})
    page_py = wiki_wiki.page(query)
    
    if page_py.exists():
        return page_py.text[:500]
    else:
        return "not found in database. Please rephrase your query."

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
