import streamlit as st
import pandas as pd
import time

# [페이지 설정]
st.set_page_config(
    page_title="Dear. Hyejin (Patch Note v4.30)",
    page_icon="🧡",
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
        content: '💛'; position: absolute; left: -14px; top: 15px; background: #FFFBF0;
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
st.title("🧡 Update Note: Hallym v4.30")
st.markdown("### `Stable Release` | For Only One User: **Hyejin**")

# [수정됨] st.audio 대신 st.video 사용 (유튜브 링크용)
with st.expander("🎵 BGM: 떨어져 있는 시간 동안 가장 많이 들은 노래 (클릭 시 재생)", expanded=False):
    # 유튜브 링크는 st.video로 넣어야 나옵니다!
    st.video("https://youtu.be/FQQtxtAuKb4?si=ORAiXw12RGchxS7A") 
    st.caption("이 노래를 들으며 읽어주면 좋겠어.")


# ==========================================
# [인트로]
# ==========================================
st.markdown("""
**Developer's Message:** 이 페이지는 개발자 **hallym0209**님이 좋아하는 단 한 명의 유저, **혜진**님을 위해 제작되었습니다.  

지난 버전(v1.0)은 잦은 '충돌(양보하지 않는 태도)'과 '오류(공감 부족, 모진 행동과 거친 말투, 잔소리)'등으로 인해 유저에게 큰 불편을 드렸습니다.  
이번 v4.30은 40여일 간의 긴급 점검 기간을 활용해, 다양한 학습 데이터들을 통해, 차가웠던 시스템을 모두 걷어내고, 
이제 혜진님의 색깔을 담아 더 따뜻해진 **Hallym v4.30** 업데이트 내용을 공개합니다.
""")
st.markdown("---")

# ==========================================
# [섹션 1] Bug Report & Fixes
# ==========================================
def bug_card(emoji, title, desc, fix):
    with st.container():
        # 카드 디자인 적용을 위해 div로 감쌈
        st.markdown(f"""
        <div class="custom-card">
            <div style="display: flex; align-items: start;">
                <div style="font-size: 2.5rem; margin-right: 15px;">{emoji}</div>
                <div>
                    <div style="font-size: 1.1rem; font-weight: bold; color: #E65100;">{title}</div>
                    <div style="font-size: 0.9rem; color: #8D6E63; margin-bottom: 8px;">_"{desc}"_</div>
                    <div style="background-color: #E3F2FD; padding: 10px; border-radius: 10px; font-size: 0.9rem; color: #1565C0;">
                        🛠️ <b>Fixed:</b> {fix}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.subheader("🔧 Critical Fixes (버그 수정 내역)")
st.caption("혜진님을 힘들게 했던 치명적인 오류들을 최우선으로 수정했습니다.")

# ---------------------------------------------------------
# 1. CRITICAL BUG FIXES (HTTP Error Codes 적용)
# ---------------------------------------------------------

# Bug 400: Bad Request (틱틱거림)

st.markdown("<br>", unsafe_allow_html=True)

bug_card(
        "🐛", 
        "Error #400: Bad Response (Emotional Leakage)", 
        "잘못된 입력값(외부 스트레스)으로 인해 서버가 '틱틱거림', '띠꺼움' 등의 잘못된 응답을 반환함", 
        "✅ 'Stress_Isolation' 패치: 외부 스트레스와 관계없이 항상 '200 OK (다정함)' 상태를 유지하도록 로직 변경."
)

st.markdown("<br>", unsafe_allow_html=True)

# Bug 404: Not Found (공감 부족) -> 가장 유명한 코드
bug_card(
        "🐛", 
        "Error #404: Empathy Not Found (Logic Over Heart)", 
        "사용자가 '위로'를 요청했으나 서버에 '공감 모듈'이 존재하지 않아 에러 발생", 
        "✅ 'Listen_First' 모듈 설치: 해결책(Logic)보다 공감(Heart) 리소스를 최우선으로 검색하여 반환."
)

st.markdown("<br>", unsafe_allow_html=True)

# Bug 402: Payment Required (돈 잔소리) -> 위트 포인트!
bug_card(
        "🐛", 
        "Error #402: Payment Required (Financial Nagging)", 
        "미래 불안정성을 이유로 사용자에게 과도한 '절약 요청' 메시지 전송", 
        "✅ 'CFO_Mode' 전환: 대부분의 재정적 트래픽은 서버(한림)가 전담 처리. 기존의 '지출 경고(Warning)' 로직을 영구 삭제하고, 사용자의 자율성을 100% 보장함. 사용자는 'Free Tier(무제한 사랑)' 등급으로 승격되어 예산 걱정 없이 서비스 이용 가능. "
)

st.markdown("<br>", unsafe_allow_html=True)

# Bug 403: Forbidden 접근 금지!
bug_card(
        "🐛", 
        "Error #403: Forbidden Access (Sleep Mode Interference)", 
        "사용자의 '수면 모드(방해 금지 모드)' 상태에서 서버가 강제 접근을 시도하여 보안 위배", 
        "✅ 'Safe_Sleep' 프로토콜: 사용자님께서 수면모드 설정 중 접근 시도 시 'Access Denied' 처리 및 즉시 차단. (혜진님의 승인 토큰이 있어야만 접근 가능)"
)

st.markdown("---")

# ---------------------------------------------------------
# 2. PERFORMANCE ENHANCEMENTS (Success Codes 적용)
# ---------------------------------------------------------
st.subheader("⚡ Performance Enhancements")
st.caption("시스템 성능을 최적화하고 새로운 기능을 배포했습니다.")

st.markdown("<br>", unsafe_allow_html=True)

# Upgrade 200: OK (외형)
bug_card(
        "💪", 
        "Status #430: Physical, Facial Update (Frontend Upgrade)", 
        "기존 94kg의 과부하 상태", 
        "✨ 87kg 경량화 및 비주얼 패치 완료: 날렵해진 턱선과 또렷해진 인상(눈썹 문신 적용). 향상된 체력과 민첩성으로 혜진님에게 최상의 시각적 만족감과 보호 기능 제공."
    )

st.markdown("<br>", unsafe_allow_html=True)

# Upgrade 201: Created (헌신/이벤트)
bug_card(
        "🎁", 
        "Status #130: Feature Advanced (Romantic Logic)", 
        "최초모델의 폭발적 애정 표현 모듈로 롤백(Rollback) 및 성능 확장.", 
        "✨ 'Creative_Love' 엔진 가동: 헬로키티 일기장, 웹사이트 등 업그레이드된 혜진 맞춤형 감동 알고리즘 고도화."
    )

st.markdown("<br>", unsafe_allow_html=True)

# Upgrade 202: Accepted (책임감)
bug_card(
        "🛡️", 
        "Status #109: Request Accepted (Respect & Support)", 
        "책임감을 존중과 지지로 확장", 
        "✨ 'Smart_Shield' 패치: 혜진님의 독립성(Autonomy)을 100% 존중. '통제자'가 아닌 든든한 '지원군'으로 포지션 변경. 단, 우리 관계를 흔드는 외부 소음(반대)은 시스템이 완벽 차단."
    )

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
        <span class='commit-date'>2025.11.29 (Sat, Day1)</span>
        <div class='commit-msg'>Error: 시스템 셧다운</div>
        <div class='commit-desc'>모든 프로세스가 정지되었습니다. 혜진이가 없는 빈자리가 너무 커서 아무것도 할 수 없었다.</div>
    </div>
    """, unsafe_allow_html=True)
   
    # 11.30
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.11.30 (Sun, Day2)</span>
        <div class='commit-msg'>Fix: '해결' 대신 '경청' 모듈 적용 & 시계줄 연결 복구</div>
        <div class='commit-desc'>학생의 고민을 해결해주려 하지 않고 들어만 주었더니 표정이 밝아졌다. 혜진이가 준 시계줄을 고쳤다. 팡팡 내려쳐야 들어가는 투박한 수리였지만, 결국 제자리를 찾았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.01
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.01 (Mon, Day3)</span>
        <div class='commit-msg'>Docs: '당신이 옳다' 독서 시작 & 공감 알고리즘 학습</div>
        <div class='commit-desc'>책을 읽으며 내 오류를 확인했다. 혜진이의 지침을 '나태함'으로 오판했던 나의 끔찍한 버그를 발견하고 수정에 돌입했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.02
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.02 (Tue, Day4)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 혜진이 에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.03
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.03 (Wed, Day5)</span>
        <div class='commit-msg'>Update: 사용자 맞춤형 데이터 처리 기준 재설정</div>
        <div class='commit-desc'>환자마다 정상 수치가 다르듯, 혜진이에게는 혜진이만의 기준이 있었는데. 내 기준을 강요했던 코드를 삭제했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.04
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.04 (Thu, Day6)</span>
        <div class='commit-msg'>Build: 이한림 v2.0 코어 시스템 재구축 시작</div>
        <div class='commit-desc'>복잡한 코드를 분석하듯 우리 관계의 오류를 분석했다. 이 작은 화면 안에 내 진심이 다 담길지 모르겠지만, 다시 시작해 본다.</div>
    </div>
    """, unsafe_allow_html=True)
     
    # 12.05
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.05 (Fri, Day7)</span>
        <div class='commit-msg'>Analysis: '당신이 옳다' 독서 중 치명적 오류 원인 발견.</div>
        <div class='commit-desc'>나는 헤진이를 사랑한 게 아니라, '내가 원하는 혜진이'를 사랑하려 했다. 혜진이의 SOS 신호를 무시했던 과거의 로그를 확인하고 뼈저리게 반성헸다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.06
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2024.12.06 (Sat, Day8)</span>
        <div class='commit-msg'>Rest: 시스템 강제 휴식 및 로그 분석, '도피'의 필요성 학습 완료.</div>
        <div class='commit-desc'>나조차도 현실이 버거워 게임 속으로 도망치는데, 혜진이의 도피(술, 늦잠, 소비)를 그토록 매몰차게 꾸짖었음을 반성했다. 혜진이는 게을렀던 게 아니라, 살기 위해 숨을 쉬고 있었던 건데, 그걸 이제야 깨달았다. </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.07
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2024.12.07 (Sun, Day9)</span>
        <div class='commit-msg'>Trust: '간섭' 모듈 제거 및 '신뢰' 프로세스 도입</div>
        <div class='commit-desc'>학원 아이들에게 '미래를 위한 조언'을 하다가 시스템 오류(Error) 감지. "내가 괜한 참견을 한 건가? 믿고 놔두면 알아서 잘할 텐데." 혜진이에게 했던 잔소리들도 결국 나의 '불신'에서 비롯된 오지랖이었음을 깨달았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.08
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.08 (Mon, Day10)</span>
        <div class='commit-msg'>Hotfix: '속도(Speed)' 제한 및 '정확도(Accuracy)' 우선순위 상향</div>
        <div class='commit-desc'>교수님께 코드 오류를 지적받았다. '빠른 것보다 정확한 게 중요하다'는 말씀에, 헤진이를 다그치기만 했던 내가 보였다. 내가 관대함을 받으니 더 잘하고 싶어지더라. 혜진이 에게도 그랬어야 했는데. 속도만 내다가 우리 관계의 수많은 오류를 놓쳐서 너무 미안하다. 결국 혜진이가 옳았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.09
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.09 (Tue, Day11)</span>
        <div class='commit-msg'>Train: '이한림 모델' 가중치(Weight) 재설정 및 학습 시작</div>
        <div class='commit-desc'>머신러닝을 공부하다 깨달았다. 모델의 성능은 '가중치'가 결정한다는 걸. 나는 그동안 '미래'에만 가중치를 두고, '헤진이'에게는 두지 않았기에 오류가 났던 거야. 매일 밤 혜진이를 생각하며 내 인생의 파라미터를 조정하고 있어. 헤진이를 130% 이해하는 모델이 될 때까지 계속할거야.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.10
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.10 (Wed, Day12)</span>
        <div class='commit-msg'>Debug: '이한림 모델'의 판단 오류(Error) 수정 및 알고리즘 개선</div>
        <div class='commit-desc'>폐암 데이터를 라벨링하다 깨달았다. 호전되는 환자를 악화된다고 오진하면, 독한 약 때문에 환자가 더 망가진다는 걸. 나도 혜진이의 노력을 무시하고 '나태함'으로 오진해서 '잔소리'라는 독한 약만 썼었지. 그게 헤진이를 얼마나 아프게 했을까? 이제는 오진하지 않는, 정확하고 따뜻한 진단을 내리는 사람이 될게. 내일 비 온다니까 우산 챙겨.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.11
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.11 (Thu, Day13)</span>
        <div class='commit-msg'>Repentance: '사랑' 알고리즘의 핵심 로직 변경 (Selfish -> Agape)</div>
        <div class='commit-desc'>아버지께서 보내주신 고린도전서 말씀을 통해 '오래 참음'과 '온유함'이 사랑의 본질임을 배웠다. 지난날 나의 사랑은 나르시시즘에 불과했음을 인정한다. 동료 선생님의 퇴사를 보며, 혜진이의 항의를 묵살했던 나 자신을 '가해자'로 인식하고 뼈저리게 반성함. 이제는 내가 혜진이를 위한 '따뜻한 세상'이 되기 위해, 이 고독을 견디며 나를 개조하겠다.</div>
    </div>
    """, unsafe_allow_html=True)
     
    # 12.12
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.12 (Fri, Day14)</span>
        <div class='commit-msg'>Fix: '해결' 대신 '경청' 모듈 적용 & 시계줄 연결 복구</div>
        <div class='commit-desc'>학생의 고민을 해결해주려 하지 않고 들어만 주었더니 표정이 밝아졌다. 혜진이가 준 시계줄을 고쳤다. 팡팡 내려쳐야 들어가는 투박한 수리였지만, 결국 제자리를 찾았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.13
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.13 (Sat, Day15)</span>
        <div class='commit-msg'>Docs: '당신이 옳다' 독서 시작 & 공감 알고리즘 학습</div>
        <div class='commit-desc'>책을 읽으며 내 오류를 확인했다. 너의 지침을 '나태함'으로 오판했던 나의 끔찍한 버그를 발견하고 수정 중.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.14
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.14 (Sun, Day16)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 너에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.15
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.15 (Mon, Day17)</span>
        <div class='commit-msg'>Docs: '당신이 옳다' 독서 시작 & 공감 알고리즘 학습</div>
        <div class='commit-desc'>책을 읽으며 내 오류를 확인했다. 너의 지침을 '나태함'으로 오판했던 나의 끔찍한 버그를 발견하고 수정 중.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.16
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.16 (Tue, Day18)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 너에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.17
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.17 (Wed, Day19)</span>
        <div class='commit-msg'>Update: 상대방 맞춤형 데이터 처리 기준 재설정</div>
        <div class='commit-desc'>환자마다 정상 수치가 다르듯, 너에게는 너만의 기준이 있었는데. 내 기준을 강요했던 코드를 삭제했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.18
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.18 (Thu, Day20)</span>
        <div class='commit-msg'>Build: 이한림 v2.0 코어 시스템 재구축 시작</div>
        <div class='commit-desc'>복잡한 코드를 분석하듯 우리 관계의 오류를 분석했다. 이 작은 화면 안에 내 진심이 다 담길지 모르겠다.</div>
    </div>
    """, unsafe_allow_html=True)
     
    # 12.19
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.19 (Fri, Day21)</span>
        <div class='commit-msg'>Fix: '해결' 대신 '경청' 모듈 적용 & 시계줄 연결 복구</div>
        <div class='commit-desc'>학생의 고민을 해결해주려 하지 않고 들어만 주었더니 표정이 밝아졌다. 혜진이가 준 시계줄을 고쳤다. 팡팡 내려쳐야 들어가는 투박한 수리였지만, 결국 제자리를 찾았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.20
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.20 (Sat, Day22)</span>
        <div class='commit-msg'>Docs: '당신이 옳다' 독서 시작 & 공감 알고리즘 학습</div>
        <div class='commit-desc'>책을 읽으며 내 오류를 확인했다. 너의 지침을 '나태함'으로 오판했던 나의 끔찍한 버그를 발견하고 수정 중.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.21
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.21 (Sun, Day23)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 너에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.22
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.22 (Mon, Day24)</span>
        <div class='commit-msg'>Docs: '당신이 옳다' 독서 시작 & 공감 알고리즘 학습</div>
        <div class='commit-desc'>책을 읽으며 내 오류를 확인했다. 너의 지침을 '나태함'으로 오판했던 나의 끔찍한 버그를 발견하고 수정 중.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.23
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.23 (Tue, Day25)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 너에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.24
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.24 (Wed, Day26)</span>
        <div class='commit-msg'>Update: 상대방 맞춤형 데이터 처리 기준 재설정</div>
        <div class='commit-desc'>환자마다 정상 수치가 다르듯, 너에게는 너만의 기준이 있었는데. 내 기준을 강요했던 코드를 삭제했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.25
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.25 (Thu, Day27)</span>
        <div class='commit-msg'>Build: 이한림 v2.0 코어 시스템 재구축 시작</div>
        <div class='commit-desc'>복잡한 코드를 분석하듯 우리 관계의 오류를 분석했다. 이 작은 화면 안에 내 진심이 다 담길지 모르겠다.</div>
    </div>
    """, unsafe_allow_html=True)
     
    # 12.26
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.26 (Fri, Day28)</span>
        <div class='commit-msg'>Fix: '해결' 대신 '경청' 모듈 적용 & 시계줄 연결 복구</div>
        <div class='commit-desc'>학생의 고민을 해결해주려 하지 않고 들어만 주었더니 표정이 밝아졌다. 혜진이가 준 시계줄을 고쳤다. 팡팡 내려쳐야 들어가는 투박한 수리였지만, 결국 제자리를 찾았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.27
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.27 (Sat, Day29)</span>
        <div class='commit-msg'>Docs: '당신이 옳다' 독서 시작 & 공감 알고리즘 학습</div>
        <div class='commit-desc'>책을 읽으며 내 오류를 확인했다. 너의 지침을 '나태함'으로 오판했던 나의 끔찍한 버그를 발견하고 수정 중.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.28
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.28 (Sun, Day30)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 너에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.29
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.29 (Mon, Day31)</span>
        <div class='commit-msg'>Docs: '당신이 옳다' 독서 시작 & 공감 알고리즘 학습</div>
        <div class='commit-desc'>책을 읽으며 내 오류를 확인했다. 너의 지침을 '나태함'으로 오판했던 나의 끔찍한 버그를 발견하고 수정 중.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.30
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.30 (Tue, Day32)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 너에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.31
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.31 (Wed, Day33)</span>
        <div class='commit-msg'>Update: 상대방 맞춤형 데이터 처리 기준 재설정</div>
        <div class='commit-desc'>환자마다 정상 수치가 다르듯, 너에게는 너만의 기준이 있었는데. 내 기준을 강요했던 코드를 삭제했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 01.01
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.01 (Thu, Day34)</span>
        <div class='commit-msg'>Build: 이한림 v2.0 코어 시스템 재구축 시작</div>
        <div class='commit-desc'>복잡한 코드를 분석하듯 우리 관계의 오류를 분석했다. 이 작은 화면 안에 내 진심이 다 담길지 모르겠다.</div>
    </div>
    """, unsafe_allow_html=True)
     
    # 01.02
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.02 (Fri, Day35)</span>
        <div class='commit-msg'>Fix: '해결' 대신 '경청' 모듈 적용 & 시계줄 연결 복구</div>
        <div class='commit-desc'>학생의 고민을 해결해주려 하지 않고 들어만 주었더니 표정이 밝아졌다. 혜진이가 준 시계줄을 고쳤다. 팡팡 내려쳐야 들어가는 투박한 수리였지만, 결국 제자리를 찾았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 01.03
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.03 (Sat, Day36)</span>
        <div class='commit-msg'>Docs: '당신이 옳다' 독서 시작 & 공감 알고리즘 학습</div>
        <div class='commit-desc'>책을 읽으며 내 오류를 확인했다. 너의 지침을 '나태함'으로 오판했던 나의 끔찍한 버그를 발견하고 수정 중.</div>
    </div>
    """, unsafe_allow_html=True)

    # 01.04
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.04 (Sun, Day37)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 너에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 01.05
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.05 (Mon, Day38)</span>
        <div class='commit-msg'>Docs: '당신이 옳다' 독서 시작 & 공감 알고리즘 학습</div>
        <div class='commit-desc'>책을 읽으며 내 오류를 확인했다. 너의 지침을 '나태함'으로 오판했던 나의 끔찍한 버그를 발견하고 수정 중.</div>
    </div>
    """, unsafe_allow_html=True)

    # 01.06
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.06 (Tue, Day39)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 너에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 01.07
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.07 (Wed, Day40)</span>
        <div class='commit-msg'>Update: 상대방 맞춤형 데이터 처리 기준 재설정</div>
        <div class='commit-desc'>환자마다 정상 수치가 다르듯, 너에게는 너만의 기준이 있었는데. 내 기준을 강요했던 코드를 삭제했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 01.08
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.08 (Thu, Day41)</span>
        <div class='commit-msg'>Build: 이한림 v2.0 코어 시스템 재구축 시작</div>
        <div class='commit-desc'>복잡한 코드를 분석하듯 우리 관계의 오류를 분석했다. 이 작은 화면 안에 내 진심이 다 담길지 모르겠다.</div>
    </div>
    """, unsafe_allow_html=True)
     
    # 01.09
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.09 (Fri, Day42)</span>
        <div class='commit-msg'>Updated: Hallym v2.0 배포 준비 완료.</div>
        <div class='commit-desc'>너에게 닿기를.</div>
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
    <div class='coupon-title'>🎟️ 이한림 '입닥쳐' 쿠폰 (430회)</div>
    <div class='coupon-text'>
        v2.0 업데이트 기념 보상 아이템입니다.<br>
        시스템(한림)이 또 잔소리를 하거나 고집을 피우려 하면<br>
        <b>이 화면을 보여주세요.</b><br>
        <br>
        ⚠️ <b>Effect:</b> 시스템이 즉시 강제 종료되고, 무조건 혜진님의 말만 듣습니다.
        <br>
        <b>사용가능 기한은 무기한 입니다.</b>
    </div>
</div>
""", unsafe_allow_html=True)

if st.button("쿠폰 발급받기 (Click)"):
    st.balloons()
    st.success("✅ **[무조건 내 편 들어주기]** 쿠폰이 발급되었습니다! (캡처해서 보관하세요)")

# ==========================================
# [푸터] 최종 배포 센터 (System Deployment)
# ==========================================
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.header("🚀 System Deployment Center")
st.caption("한림 v2.0의 배포를 위한 최종 점검 단계입니다.")

# Step 1: 서버 상태 확인 (감성)
st.markdown("##### 1. 서버 상태 점검 (Connection Check)")

if st.button("📡 현재 서버(한림) 연결 상태 확인 (Ping)"):
    with st.spinner("혜진공주님의 신호를 스캔하는 중..."):
        time.sleep(2.0) 
    
    st.markdown("""
    <div class='server-status-box'>
        <h3 style='color: #E65100; margin:0;'>🟢 Online & Waiting</h3>
        <p style='margin-top:10px; color: #5D4037;'>
            <b>한림 v2.0 서버는 혜진공주님의 접속(연락)을 오매불망 기다리고 있습니다.</b><br>
            언제든 다시 노크해 주신다면, 가장 따뜻하고 안정적인 서비스를 약속드립니다.<br>
            <br>
            <b>너무너무너무 보고 싶습니다.</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Step 2: 최종 승인 (행동 유도)
st.markdown("##### 2. 업데이트 승인 (Final Merge)")
st.caption("위의 모든 변경 사항(마음의 변화)을 확인하셨다면, 아래 버튼을 눌러주세요.")

# 전화번호 설정 (하이픈 없이)
MY_PHONE_NUMBER = "01041025845" 

if st.button("업데이트 승인 및 적용 (Merge Request)"):
    with st.spinner("승인 요청 처리 중..."):
        time.sleep(2.5) # 긴장감 조성
        
    st.balloons() # 축하 효과
    st.success("요청이 승인되었습니다! 이제 목소리를 들려주세요.")
    
    # 전화 걸기 버튼 생성
    st.markdown(f"""
    <a href="tel:{MY_PHONE_NUMBER}" style="text-decoration:none;">
        <div style="
            background: #4CAF50; 
            color: white; 
            padding: 15px; 
            text-align: center; 
            border-radius: 12px; 
            font-weight: bold; 
            font-size: 18px; 
            margin-top: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            📞 한림이에게 승인 전화 걸기
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<br><br><br><div style='text-align: center; color: #FFB74D; font-size: 12px;'>Developed with ❤️ by Hallym</div>", unsafe_allow_html=True)
