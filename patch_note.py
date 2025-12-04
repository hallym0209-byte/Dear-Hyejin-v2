
import streamlit as st
import pandas as pd
import time

# [페이지 설정]
st.set_page_config(
    page_title="To. Hyejin (Patch Note v2.0)",
    page_icon="🍊",
    layout="centered"
)

# [CSS 스타일] 노랑 & 주황 테마 + 쿠폰 디자인 추가
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 */
    .stApp { background-color: #FFFBF0; }
    h1 { color: #FF8C00!important; font-family: 'Helvetica', sans-serif; }
    h2, h3 { color: #FFA500!important; }
    
    /* 본문 글씨색 고정 (다크모드 방지) */
    .stMarkdown, .stText, p, div, span, li { color: #5D4037 !important; }
    
    /* 뱃지 스타일 */
    .highlight-badge {
        background-color: #FFD700; color: #5D4037;
        padding: 5px 12px; border-radius: 20px;
        font-size: 14px; font-weight: bold;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    
    /* 버튼 스타일 */
    div.stButton > button {
        background: linear-gradient(to right, #FF8C00, #FFD700);
        color: white !important; border: none; border-radius: 12px;
        font-weight: bold; transition: 0.3s;
    }
    div.stButton > button:hover { transform: scale(1.02); box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    hr { border-top: 2px solid #FFECB3; }
    
    /* 타임라인 스타일 */
    .timeline-item {
        padding: 20px; border-left: 3px solid #FFB74D;
        margin-left: 20px; position: relative;
        background: white; border-radius: 0 10px 10px 0;
        margin-bottom: 20px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .timeline-item::before {
        content: '🍊'; position: absolute; left: -14px; top: 15px; background: #FFFBF0;
    }
    
    /* 쿠폰 스타일 (종이 질감 효과) */
    .coupon-card {
        background-color: #FFF8E1;
        border: 2px dashed #FFB74D;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
        position: relative;
    }
    .coupon-title {
        color: #E65100 !important;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .coupon-text {
        font-size: 14px;
        color: #5D4037;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# [헤더] 타이틀 & BGM
# ==========================================
st.markdown("<div style='text-align: center;'> <span class='highlight-badge'>New Release</span> </div>", unsafe_allow_html=True)
st.title("🍊 Update Note: Hallym v2.0")
st.markdown("### `Stable Release` | For Only One User: **Hyejin**")

# [수정됨] st.audio 대신 st.video 사용 (유튜브 링크용)
with st.expander("🎵 BGM: 떨어져 있는 시간 동안 가장 많이 들은 노래 (클릭 시 재생)", expanded=False):
    # 유튜브 링크는 st.video로 넣어야 나옵니다!
    st.video("https://youtu.be/FQQtxtAuKb4?si=ORAiXw12RGchxS7A") 
    st.caption("이 노래를 들으며 읽어주면 좋겠어.")

st.markdown("---")

# ==========================================
# [인트로]
# ==========================================
st.markdown("""
**Developer's Message:** 이 페이지는 **노랑**과 **주황**을 좋아하는 단 한 명의 유저, **[혜진]**님을 위해 디자인되었습니다.  

지난 버전(v1.0)은 잦은 '충돌(양보하지 않는 태도)'과 '오류(공감 부족, 모진 행동과 거친 말투, 진소리)'로 인해 유저에게 큰 불편을 드렸습니다.  
40여일 간의 긴급 점검을 통해 차가웠던 시스템을 모두 걷어내고,  
이제 혜진님의 색깔을 담아 더 따뜻해진 **Hallym v2.0** 업데이트 내용을 공개합니다.
""")
st.markdown("---")

# ==========================================
# [섹션 1] Bug Report & Fixes
# ==========================================
st.subheader("🔧 Critical Fixes (버그 수정 내역)")
st.caption("혜진님을 힘들게 했던 치명적인 오류들을 최우선으로 수정했습니다.")

def bug_card(emoji, title, desc, fix):
    with st.container():
        c1, c2 = st.columns([1, 10]) # 컬럼 비율 조정
        with c1: st.markdown(f"<h2>{emoji}</h2>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"**{title}**")
            st.caption(f"_{desc}_")
            st.info(f"🍊 **Fixed:** {fix}")
        st.markdown("<br>", unsafe_allow_html=True)

bug_card("❌", "Bug #401: 공감 프로세스 응답 없음", "해결책부터 제시하여 유저의 마음을 답답하게 함", "'해결' 로직을 조정하고, '무조건 경청' 모듈을 메인 프로세스로 탑재했습니다.")
bug_card("❌", "Bug #503: 감정 제어 장치 오작동", "다툼 시 날카로운 언어로 상처를 입힘", "언어 순화 필터를 이중으로 적용했습니다. 감정이 격해지면 시스템이 잠시 '일시 정지(Pause)' 됩니다.")
bug_card("❌", "Bug #404: 현재(Present) 인식 불가", "미래에 대한 불안으로 현재의 행복을 놓침", "'Future' 클래스 의존성을 대폭 낮추고, '지금 우리'의 우선순위를 최상위로 변경했습니다.")

# ==========================================
# [섹션 2] Data Visualization (감정 분석)
# ==========================================
st.markdown("---")
st.subheader("📊 40 Days Analysis (데이터로 본 변화)")
st.caption("40일 동안 제 머릿속 점유율을 분석해보았습니다.")

# 차트 데이터
chart_data = pd.DataFrame({
    'Day': range(1, 41),
    'Grieving (그리움)': [10 + i * 2 for i in range(40)],  
    'Ego (자존심)': [100 - i * 2.5 for i in range(40)],   
    'Understanding (이해심)': [20 + i * 2 for i in range(40)] 
})

st.line_chart(chart_data.set_index('Day'), color=["#FF9800", "#9E9E9E", "#FFC107"])
st.caption("📉 회색(자존심)은 바닥을 쳤고, 📈 주황색(그리움/이해심)은 우상향 중입니다.")

# ==========================================
# [섹션 3] Commit History (일기 요약)
# ==========================================
st.markdown("---")
st.subheader("📝 Commit History (주요 기록)")
st.caption("매일 혜진님을 생각하며 제 자신을 디버깅한 기록들입니다.")

with st.expander("📂 40일간의 세부 업데이트 로그 열어보기 (Click)", expanded=False):
    st.markdown("""
    <div class='timeline-item'>
        <b>Day 1 (11.29)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>
                    <div class='timeline-item'>
        <b>Day 2 (11.30)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>
    <div class='timeline-item'>
        <b>Day 3 (12.01)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>
    <div class='timeline-item'>
        <b>Day 4 (12.02)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>                
    <div class='timeline-item'>
        <b>Day 5 (12.03)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>
    <div class='timeline-item'>
        <b>Day 6 (12.04)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>
    <div class='timeline-item'>
        <b>Day 7(12.05)</b><br>
        카톡 로그를 처음부터 다시 읽었다. "오빠 말 좀 예쁘게 해"라는 네 메시지에서 멈췄다. (Bug #503 확인)
    </div>
    <div class='timeline-item'>
        <b>Day 8 (12.06)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>
    <div class='timeline-item'>
        <b>Day 9 (12.07)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>                
    <div class='timeline-item'>
        <b>Day 10 (12.08)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>
    <div class='timeline-item'>
        <b>Day 11 (12.09)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>   
    <div class='timeline-item'>
        <b>Day 12 (12.10)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>            
    <div class='timeline-item'>
        <b>Day 13 (12.11)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 14 (12.12)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>                     
    <div class='timeline-item'>
        <b>Day 15 (12.13)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 16 (12.14)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 17 (12.15)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>                     
    <div class='timeline-item'>
        <b>Day 18 (12.16)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 19 (12.17)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>                     
    <div class='timeline-item'>
        <b>Day 20 (12.18)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 21 (12.19)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 22 (12.20)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 23 (12.21)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 24 (12.22)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>                     
    <div class='timeline-item'>
        <b>Day 25 (12.23)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 26 (12.24)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 27 (12.25)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 28 (12.26)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 29 (12.27)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 30 (12.28)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 31 (12.29)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>                     
    <div class='timeline-item'>
        <b>Day 32 (12.30)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>     
    <div class='timeline-item'>
        <b>Day 33 (12.31)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>   
    <div class='timeline-item'>
        <b>Day 34 (01.01)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>   
    <div class='timeline-item'>
        <b>Day 35 (01.02)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>   
    <div class='timeline-item'>
        <b>Day 36 (01.03)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>   
    <div class='timeline-item'>
        <b>Day 37 (01.04)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>   
    <div class='timeline-item'>
        <b>Day 38 (01.05)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>                   
    <div class='timeline-item'>
        <b>Day 39 (01.06)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>   
    <div class='timeline-item'>
        <b>Day 40 (01.07)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>   
    <div class='timeline-item'>
        <b>Day 41 (01.08)</b><br>
        시스템 셧다운. 네가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.
    </div>   
    <div class='timeline-item'>
        <b>Day 42 (01.09)</b><br>
        <b>Hallym v2.0 배포 준비 완료.</b> 너에게 닿기를 기도하며.
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# [섹션 4] 스페셜 쿠폰 (추가된 기능)
# ==========================================
st.markdown("---")
st.subheader("🎁 Special Gift (업데이트 보상)")
st.caption("업데이트를 완료한 유저에게만 드리는 한정판 아이템입니다.")

# 쿠폰 디자인
st.markdown("""
<div class='coupon-card'>
    <div class='coupon-title'>🎟️ 이한림 '입닥쳐' 쿠폰 (430회권)</div>
    <div class='coupon-text'>
        v2.0 업데이트 기념 보상 아이템입니다.<br>
        시스템이 또 잔소리를 하거나 고집을 피우려 하면<br>
        <b>이 화면을 보여주세요.</b><br>
        <b>사용기한은 무기한 입니다.</b><br>    
        <br>
        ⚠️ <b>Effect:</b> 시스템이 강제 종료되고, 무조건 혜진이 말만 듣습니다.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("") # 여백

# 쿠폰 발급 버튼
if st.button("쿠폰 발급받기 (Click)"):
    st.balloons() # 풍선 효과
    st.success("✅ **[무조건 내 편 들어주기]** 쿠폰이 정상적으로 발급되었습니다! (캡처해서 보관하세요)")

# ==========================================
# [푸터] 서버 상태
# ==========================================
st.markdown("---")
st.markdown("### 📡 Server Status")

if st.button("현재 서버 연결 상태 확인"):
    with st.spinner("혜진님의 신호를 기다리는 중..."):
        time.sleep(2.0) 
    
    st.markdown("""
    <div style='background-color: #FFF3E0; padding: 20px; border-radius: 10px; border-left: 5px solid #FF9800;'>
        <h3 style='color: #E65100; margin:0;'>🟢 Online & Waiting</h3>
        <p style='margin-top:10px; color: #5D4037;'>
            <b>한림 v2.0 서버는 혜진님의 접속(연락)을 오매불망 기다리고 있습니다.</b><br>
            언제든 다시 노크해 주신다면, 가장 따뜻하고 안정적인 서비스를 약속드립니다.<br>
            <br>
            <b>보고 싶습니다.</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><div style='text-align: center; color: #FFB74D; font-size: 12px;'>Developed with ❤️ by Hallym</div>", unsafe_allow_html=True)