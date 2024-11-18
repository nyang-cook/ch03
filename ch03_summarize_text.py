#### 기본 정보 입력 ####
# 스트림릿 패키지  설치
import streamlit as st
# OpenAI 패키지 추가
import openai

#### 기능 구현 함수 정리####
def askGpt(prompt, apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        message=[{"role":"user", "content":prompt}]
    )
    gptResponse = response.choices[0].message.content
    return gptResponse

#### 메인 함수 ####
def main():
    st.set_page_config(page_title="요약 프로그램")
    # sesstion state 초기화
    if "OPENAI_API" not in st.seesion_state:
        st.session_state["OPENAI_API"] = ""

    # 사이드바
    with st.sidebar:
        # Open AI API 키 입력받기
        openai_apikey = st.text_input(label="OPENAI API 키", placeholder="Enter your API Key", value='', type='password')
        # 세션 스테이트에 저장
        if openai_apikey:
            st.session_state["OPENAI_API"] = openai_apikey
        st.markdown('---')
        # 메인 공간
        st.header("문서 요약 프로그램")
        st.markdown("---")

        text = st.text_area("요약 할 글을 입력하세요")
        if st.button("요약"):
            prompt = f'''
            **instruction**  :
            - plz ...