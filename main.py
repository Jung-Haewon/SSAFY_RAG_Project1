"""7단계 — 프로젝트 UI 골격. 여기서 3일 프로젝트가 시작됩니다.

실행:
    streamlit run main.py

6단계 챗봇에 프로젝트에 필요한 세 가지를 더합니다.

    ① 사이드바에서 질문할 항목을 고른다         st.selectbox
    ② 오래 걸리는 단계를 보여 준다             st.status
    ③ 답변 아래에 근거 목록을 붙인다            st.expander

**아직 RAG는 없습니다.** 문서 수집도 검색도 가짜입니다.
이 골격의 빈 칸을 진짜로 채워 나가는 것이 3일 프로젝트입니다.
이 파일을 오후부터 각자 프로젝트의 app.py로 이어 씁니다. 새로 만들지 않습니다.

비유 — st.status는 배달앱의 "조리 중 → 배달 중" 표시, 근거 목록은 보고서의 각주입니다.

놓치기 쉬운 두 가지
    1. 대화를 다시 그릴 때 근거 목록도 함께 그린다. 빠뜨리면 이전 답변의 근거가 사라진다.
    2. 검색된 문서를 전부 보여 주지 않는다. 답변이 실제로 인용한 [근거 N]만 보여 주고,
       인용이 하나도 없으면 그 사실을 안내한다. (요구사항 F2008)
"""

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

DOMAIN = "service type"
ITEMS = ["3-Tier Web", "Only front-end", "ML Learing", "Game (Online)"]

GMS_BASE_URL = "https://gms.ssafy.io/gmsapi/api.openai.com/v1/"

st.set_page_config(page_title="SA-RMF", page_icon="🏴‍☠️")
st.title("🏴‍☠️ Service Architect Risk Management Framework")
st.caption(
    "Last few years, there is a lot of changes in software development environment. "
    + "With the advancement of cloud services, such as AWS or GCP or Azure, "
    + "and virtualize techniques, such as Docker or k8s, "
    + "the speed of developing and deploying program/application are much more faster than ever before."
    + "However, there are side effects of these enhancements. "
    + "Since the shoposicate concept of the MSA architecture and cloud and network infrastructure, "
    + "Attack surfaces are "
)

with st.sidebar:
    st.header(f"Select your {DOMAIN}")
    item = st.selectbox("Make your app secure again", ITEMS, index=None, key="item", placeholder=f"Select {DOMAIN}")

    if st.button("Erase history", width="stretch"):
        st.session_state.messages = []

if not item:
    st.info(f"Select {DOMAIN} first")
    st.stop()

st.subheader(item)

if "messages" not in st.session_state:
    st.session_state.messages = []
