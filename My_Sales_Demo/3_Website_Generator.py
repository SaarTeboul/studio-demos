import streamlit as st
from constants import WEBSITE_DESCRIPTION_FEW_SHOT, WEBSITE_TESTIMONIAL_FEW_SHOT, DEFAULT_MODEL, WEBSITE_FAQ_FEW_SHOT\
    ,WEBSITE_Email_Template_FEW_SHOT
from utils.completion import complete
from utils.studio_style import apply_studio_style

st.set_page_config(
    page_title="Website Generator",
)


def query(prompt, stopSequences=["##"]):
    config = {
        "numResults": 1,
        #100 tokens (on avg) = 75 words, we want 50-150 words so Min tokens = 67 and max tokens = 200
        "maxTokens": 200,
        "temperature": 0.7,
        "topKReturn": 0,
        "topP":0.98,
        "countPenalty": {
            "scale": 0.4,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
      "stopSequences":stopSequences
    }

    res = complete(model_type=DEFAULT_MODEL,
                   prompt=prompt,
                   **config)

    return res["completions"][0]["data"]["text"]


if __name__ == '__main__':

    apply_studio_style()
    st.title("Saar Teboul - AI21 :blue[_Website Generator_] :sunglasses:")
    st.markdown("###### :red[_Unlock instant, impactful marketing content for your business page! Just share a snippet about your enterprise, and watch our tool craft a captivating description that highlights your unique benefits_]")

    business_name = st.text_input("Enter your business' name:", value="Dance Fusion Studios")
    location = st.text_input("Enter your business' location:", value="Miami, FL")
    services = st.text_area("List your business services here:", value="- Ballet\n- Hip-Hop\n- Contemporary\n- Latin Dance\n- Fitness Classes")
    highlights = st.text_area("Do you want to highlight some benefits of your business?", value="- Certified Instructors\n- Spacious Dance Studios\n- Beginner to Advanced Levels")

    prompt = WEBSITE_DESCRIPTION_FEW_SHOT + f"Name of Business: {business_name}\nLocation: {location}\nServices:\n{services}\n\nImportant Company Highlights:\n{highlights}\n\nDescription:\n"

    if st.button(label="Generate Marketing Content"):
        st.session_state["short-form-save_results_ind"] = []
        with st.spinner("Loading..."):
            st.session_state["short-form-result"] = {
                "completion": query(prompt).strip(),
            }
            result = st.session_state["short-form-result"]["completion"]
            testimonial_prompt = WEBSITE_TESTIMONIAL_FEW_SHOT + f"Name of Business: {business_name}\nLocation: {location}\nServices:\n{services}\n\nImportant Company Highlights:\n{highlights}\n\n"
            st.session_state["testimonial"] = {
                    "completion": query(testimonial_prompt, stopSequences=['##']),}
            faq_prompt = WEBSITE_FAQ_FEW_SHOT + f"Name of Business: {business_name}\nLocation: {location}\nServices:\n{services}\n\nImportant Company Highlights:\n{highlights}\n\n"
            st.session_state["faq"] = {
                "completion": query(faq_prompt, stopSequences=['##']), }
            email_prompt = WEBSITE_Email_Template_FEW_SHOT + f"Name of Business: {business_name}\nLocation: {location}\nServices:\n{services}\n\nImportant Company Highlights:\n{highlights}\n\n"
            st.session_state["email"] = {
                "completion": query(email_prompt, stopSequences=['##']), }

    if "short-form-result" in st.session_state:
        if "headline" in st.session_state:
            st.text_input("Generated Headline", st.session_state['headline']['completion'])
        else:
            st.text("")
        st.text_area("Generated Website Description", st.session_state["short-form-result"]["completion"], height=150)
        if "testimonial" in st.session_state:
            st.text_area("Generated Testimonial", st.session_state['testimonial']['completion'].split('Testimonial:\n')[1], height=200)
        if "faq" in st.session_state:
            st.text_area("Generated FAQ",
                         st.session_state['faq']['completion'].split('FAQ:\n')[1], height=280)
        if "email" in st.session_state:
            st.text_area("Generated Marketing Email",
                         st.session_state['email']['completion'].split('Email:\n')[1], height=300)


# To run: source venv/bin/activate
# streamlit run My_Sales_Demo/3_Website_Generator.py

#(venv) (base) saar.teboul@Saars-MacBook-Pro studio-demos % streamlit run My_Sales_Demo/3_Website_Generator.py
