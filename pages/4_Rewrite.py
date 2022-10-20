import random

import requests
import streamlit as st

from utils.completion import _full_url
from utils.studio_style import apply_studio_style


# API_KEY = st.secrets['api-keys']['ai21-algo-team-prod']
import os
API_KEY = os.getenv("API_KEY")
DUMMIES_LIST = ["Dummy1", "Dummy2", "Dummy3", "Dummy4"]

@st.cache(show_spinner=False)
def rewrite(text, api_key, intent="general", span_start=0, span_end=None, env="production"):
    url = _full_url(env, model_type='experimental', custom_model='', endpoint='rewrite')
    auth_header = f"Bearer {api_key}"
    resp = requests.post(
        url,
        headers={"Authorization": auth_header},
        json={"text": text,
              "intent": intent,
              "spanStart": span_start,
              "spanEnd": len(text) if span_end is None else span_end}
    )
    return resp.json()


def get_suggestions(text, intent='general', span_start=0, span_end=None):
    rewrite_resp = rewrite(text, intent=intent, span_start=span_start, span_end=span_end, api_key=API_KEY)
    rewritten_texts = [sug['text'] for sug in rewrite_resp['suggestions']]
    st.session_state["rewrite_rewritten_texts"] = rewritten_texts


def show_next():
    # From streamlit docs: "When updating Session state in response to events, a callback function gets executed first, and then the app is executed from top to bottom."
    # This means this function just needs to update the current index. The text itself would be shown since the entire app is executed again
    curr_index = st.session_state["rewrite_curr_index"]
    next_index = (curr_index + 1) % len(DUMMIES_LIST)
    st.session_state["rewrite_curr_index"] = next_index


def show_prev():
    curr_index = st.session_state["rewrite_curr_index"]
    prev_index = (curr_index - 1) % len(DUMMIES_LIST)
    st.session_state["rewrite_curr_index"] = prev_index


if __name__ == '__main__':
    apply_studio_style()

    st.title("Rewrite text")
    text = st.text_input(label="Insert your text here",
                         placeholder="Let's set up a meeting to discuss opportunities using AI21 Studio",
                         value="Let's set up a meeting to discuss opportunities using AI21 Studio").strip()

    intent = st.radio(
        "Set rewrite intent 👉",
        key="intent",
        options=["general", "formal", "casual", "long", "short"],
        horizontal=True
    )

    # col1, *_ = st.columns(4)
    # with col1:
        # intent = st.selectbox(
        #     "Rewrite intent",
        #     ("general", "formal", "casual", "long", "short"),
        # )
    st.button(label="Rewrite", on_click=lambda: get_suggestions(text, intent=intent))
    if "rewrite_rewritten_texts" in st.session_state:
        st.markdown(body='* ' + '\n* '.join(st.session_state["rewrite_rewritten_texts"]))

        ph = st.empty()
        if "rewrite_curr_index" not in st.session_state:
            st.session_state["rewrite_curr_index"] = 0
        curr_index = st.session_state["rewrite_curr_index"]
        ph.text_area(label="", value=DUMMIES_LIST[curr_index])

        col1, col2, col3, col4 = st.columns([0.5, 0.5, 4, 4])
        with col1:
            st.button("<", on_click=lambda: show_prev())
        with col2:
            st.button(">", on_click=lambda: show_next())
        print(st.session_state["rewrite_curr_index"])

