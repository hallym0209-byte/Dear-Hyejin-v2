
import streamlit as st
import pandas as pd
import time
from datetime import datetime
import pytz # timezone 처리를 위해 필요 (없으면 pip install pytz)

# --- [1] 방문자 추적 함수 ---
def track_visitor():
    # 세션 상태에 방문 기록이 없으면 (새로고침 하거나 처음 들어왔을 때)
    if 'visited' not in st.session_state:
        st.session_state.visited = True
        
        # 한국 시간(KST) 설정
        KST = pytz.timezone('Asia/Seoul')
        now_kst = datetime.now(KST)
        time_str = now_kst.strftime("%Y-%m-%d %H:%M:%S")
        
        # 로그에 아주 잘 보이게 출력
        print(f"\n🚨 [혜진이 접속 감지!] --------------------------------")
        print(f"   ▶ 접속 시간: {time_str} (한국 시간)")
        print(f"   --------------------------------------------------\n")

# 앱 시작하자마자 추적 함수 실행
track_visitor()

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
    st.video("https://youtu.be/3AI1q-vlcOQ?si=t21Oq911X9D8dko5") 
    st.caption("이 노래를 들으며 읽어주면 좋겠어.")


# ==========================================
# [인트로]
# ==========================================
st.markdown("""
### Developer's Message

이 페이지는 신입 개발자 <strong>hallym0209</strong>님이 세상에서 가장 좋아하는 단 한 명의 유저, <strong>혜진</strong>님을 위해 제작되었습니다.

<div style="height: 10px;"></div>

지난 <strong>[Hallym v1.0]</strong>은 잦은 <strong>'충돌(양보하지 않는 태도)'</strong>과 치명적인 <strong>'오류(공감 부족, 모진 행동, 잔소리)'</strong> 등으로 인해 유저(User)에게 큰 불편과 상처를 드렸습니다.

<div style="height: 10px;"></div>

이에 개발자는 지난 40여 일간의 <strong>[긴급 점검(Emergency Maintenance)]</strong> 기간을 가졌습니다.<br>
혜진님이 주신 소중한 피드백과 다양한 학습 데이터들을 바탕으로, 차가웠던 시스템 코드를 모두 걷어내고 처음부터 다시 썼습니다.

<div style="height: 10px;"></div>

이제 오직 혜진님의 취향을 담아, 더 따뜻하고 안정적으로 업그레이드된 <strong>[Hallym v4.30]</strong>의 업데이트 패치 노트(Patch Note)를 공개합니다.
""", unsafe_allow_html=True)

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

st.markdown("""
    <div style="text-align: right; color: #808080; font-size: 11px; margin-top: -10px;">
        * HTTP 400: Bad Request (잘못된 요청으로 실패함) <br>
        * HTTP 200: OK (요청이 성공적으로 처리됨)
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Bug 404: Not Found (공감 부족) -> 가장 유명한 코드
bug_card(
        "🐛", 
        "Error #404: Empathy Not Found (Logic Over Heart)", 
        "사용자가 '위로'를 요청했으나 서버에 '공감 모듈'이 존재하지 않아 에러 발생", 
        "✅ 'Listen_First' 모듈 설치: 해결책(Logic)보다 공감(Heart) 리소스를 최우선으로 검색하여 반환."
)

st.markdown("""
    <div style="text-align: right; color: #808080; font-size: 11px; margin-top: -10px;">
        * HTTP 404: Not Found (요청한 페이지나 자료를 찾을 수 없음)
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Bug 402: Payment Required (돈 잔소리) -> 위트 포인트!
bug_card(
        "🐛", 
        "Error #402: Payment Required (Financial Nagging)", 
        "미래 불안정성을 이유로 사용자에게 과도한 '절약 요청' 메시지 전송", 
        "✅ 'CFO_Mode' 전환: 대부분의 재정적 트래픽은 서버(한림)가 전담 처리. 기존의 '지출 경고(Warning)' 로직을 영구 삭제하고, 사용자의 자율성을 100% 보장함. 사용자는 'Free Tier(무제한 사랑)' 등급으로 승격되어 예산 걱정 없이 서비스 이용 가능. "
)

st.markdown("""
    <div style="text-align: right; color: #808080; font-size: 11px; margin-top: -10px;">
        * HTTP 402: Payment Required (결제가 필요함 - 사용되지 않는 예약 코드)
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Bug 403: Forbidden 접근 금지!
bug_card(
        "🐛", 
        "Error #403: Forbidden Access (Sleep Mode Interference)", 
        "사용자의 '수면 모드(방해 금지 모드)' 상태에서 서버가 강제 접근을 시도하여 보안 위배", 
        "✅ 'Safe_Sleep' 프로토콜: 사용자님께서 수면모드 설정 중 접근 시도 시 'Access Denied' 처리 및 즉시 차단. (혜진님의 승인 토큰이 있어야만 접근 가능)"
)

st.markdown("""
    <div style="text-align: right; color: #808080; font-size: 11px; margin-top: -10px;">
        * HTTP 403: Forbidden (서버가 요청을 이해했으나, 승인을 거부함)
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# 2. PERFORMANCE ENHANCEMENTS (Success Codes 적용)
# ---------------------------------------------------------
st.subheader("⚡ Performance Enhancements")
st.caption("시스템 성능을 최적화하고 새로운 기능을 배포했습니다.")

st.markdown("<br>", unsafe_allow_html=True)

# Upgrade 4300: OK (외형)
bug_card(
        "💪", 
        "Status #430: Physical, Facial Update (Frontend Upgrade)", 
        "기존 94kg의 과부하 상태", 
        "✨ 90kg 경량화 및 비주얼 패치 완료: 날렵해진 턱선과 또렷해진 인상(눈썹 문신 적용). 향상된 체력과 민첩성으로 혜진님에게 최상의 시각적 만족감과 보호 기능 제공."
    )

st.markdown("""
    <div style="text-align: right; color: #808080; font-size: 11px; margin-top: -10px;">
        * Status 430: Princess Hyejin Day(올해 생일 케이크도 머리속에 그림 그려 뒀는데 줄 기회가 있으면 좋겠다...)
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Upgrade 130: Created (헌신/이벤트)
bug_card(
        "🎁", 
        "Status #130: Feature Advanced (Romantic Logic)", 
        "최초모델의 폭발적 애정 표현 모듈로 롤백(Rollback) 및 성능 확장.", 
        "✨ 'Creative_Love' 엔진 가동: 회고록, 웹사이트 등 업그레이드된 혜진 맞춤형 감동 알고리즘 고도화."
    )

st.markdown("""
    <div style="text-align: right; color: #808080; font-size: 11px; margin-top: -10px;">
        * Status 130: Our First Day(초심으로 돌아가 혜진 사랑해 폭탄 발사!)
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Upgrade 815: Accepted (책임감)
bug_card(
        "🛡️", 
        "Status #815: Request Accepted (Respect & Support)", 
        "책임감을 존중과 지지로 확장", 
        "✨ 'Smart_Shield' 패치: 혜진님의 독립성(Autonomy)을 100% 존중. '통제자'가 아닌 든든한 '지원군'으로 포지션 변경. 단, 우리 관계를 흔드는 외부 바이러스는 백신 시스템 구현으로 완벽 차단."
    )

st.markdown("""
    <div style="text-align: right; color: #808080; font-size: 11px; margin-top: -10px;">
        * Status 815: 우리는 독립된 주체로 혜진이를 경청하고, 공감하고, 존중하고, 인정하고, 지지한다!
    </div>
    """, unsafe_allow_html=True)


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
st.caption("매일 혜진님을 생각하며 후회와 반성으로 제 자신을 디버깅한 기록들입니다.")

with st.expander("📂 40일간의 세부 업데이트 로그 열어보기 (Click)", expanded=False):
    # 11.29
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.11.29 (Sat, Day1)</span>
        <div class='commit-msg'>Shutdown: 시스템 종료</div>
        <div class='commit-desc'>모든 프로세스가 정지되었습니다. <strong>혜진이가 없는 빈자리</strong>가 너무 커서 아무것도 할 수 없었다. 어떻게 살아야 하지...</div>
    </div>
    """, unsafe_allow_html=True)

    # 11.30
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.11.30 (Sun, Day2)</span>
        <div class='commit-msg'>Listening: '해결' 대신 '경청'</div>
        <div class='commit-desc'>학생의 고민을 해결해주려 하지 않고 <strong>들어만 주었더니</strong> 표정이 밝아졌다. 혜진이가 준 시계줄을 고쳤다. 팡팡 내려쳐야 들어가는 투박한 수리였지만, 결국 제자리를 찾았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.01
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.01 (Mon, Day3)</span>
        <div class='commit-msg'>Empathy: '당신이 옳다' 독서 시작</div>
        <div class='commit-desc'>혜진이의 충전을 <strong>'나태함'으로 오분류했던</strong> 나의 끔찍한 버그를 발견하고 수정에 돌입했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.02
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.02 (Tue, Day4)</span>
        <div class='commit-msg'>Flexibility: '엄격함' 제거 & '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 혜진이에게는 왜 정답만 강요했을까. <strong>관계에는 정답이 없다</strong>는 걸 코드를 짜며 배웠다. 헝클어진 우리 관계를 잡아주는 코드를 개발하는 중이다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.03
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.03 (Wed, Day5)</span>
        <div class='commit-msg'>Respect: 혜진이만의 기준 인정하기</div>
        <div class='commit-desc'>환자마다 정상 수치가 다르듯, <strong>혜진이에게는 혜진이만의 기준</strong>이 있었다. '개선점 주기 코드'와 '내 기준을 강요하기' 코드를 삭제 후 혜진이의 감정을 인정하는 코드를 업데이트했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.04
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.04 (Thu, Day6)</span>
        <div class='commit-msg'>Reboot: 이한림 v4.30 재구축 시작</div>
        <div class='commit-desc'>복잡한 코드를 분석하듯 우리 관계의 오류를 분석했다. 이 작은 화면 안에 내 진심이 다 담길지 모르겠지만, <strong>다시 시작해 본다.</strong></div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.05
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.05 (Fri, Day7)</span>
        <div class='commit-msg'>Realization: 사랑의 대상 재정의</div>
        <div class='commit-desc'>나는 혜진이를 사랑한 게 아니라, <strong>'내가 원하는 혜진이'를 사랑하려 했다.</strong> 혜진이의 SOS 신호를 무시했던 과거의 로그를 확인하고 뼈저리게 반성했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.06
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.06 (Sat, Day8)</span>
        <div class='commit-msg'>Understanding: 혜진이의 '도피'를 이해하기</div>
        <div class='commit-desc'>나조차도 현실이 버거워 게임 속으로 도망치는데, 혜진이의 도피(술, 늦잠, 소비)를 그토록 매몰차게 꾸짖었음을 반성했다. 혜진이는 게을렀던 게 아니라, <strong>살기 위해 숨을 쉬고 있었던 건데...</strong> 사용자의 escape(도피)에도 시스템에 영향이 가지 않게 수정했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.07
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.07 (Sun, Day9)</span>
        <div class='commit-msg'>Trust: 간섭 대신 '믿음'</div>
        <div class='commit-desc'>학원 아이들에게 '미래를 위한 조언'을 하다가 시스템 오류(Error) 감지했다. "내가 괜한 참견을 한 건가? 믿고 놔두면 알아서 잘할 텐데." 혜진이에게 했던 잔소리들도 결국 <strong>나의 '불신'에서 비롯된 오지랖</strong>이었음을 깨달았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.08
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.08 (Mon, Day10)</span>
        <div class='commit-msg'>Accuracy: 속도보다 중요한 '정확도'</div>
        <div class='commit-desc'>교수님께 코드 오류를 지적받았다. '빠른 것보다 정확한 게 중요하다'는 말씀에, 혜진이를 다그치기만 했던 내가 보였다. 내가 관대함을 받으니 더 잘하고 싶어지더라. 혜진이에게도 그랬어야 했는데. 속도만 내다가 우리 관계의 수많은 오류를 놓쳐서 너무 미안하다. 결국 <strong>'혜진이가 옳았다.'</strong></div>
    </div>
    """, unsafe_allow_html=True)

    # 12.09
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.09 (Tue, Day11)</span>
        <div class='commit-msg'>Weight: 내 인생의 가중치 조절</div>
        <div class='commit-desc'>머신러닝을 공부하다 깨달았다. 모델의 성능은 '가중치'가 결정한다는 것을. 나는 그동안 '미래'에만 가중치를 두고, '혜진이'에게는 두지 않았기에 오류가 발생했다. 매일 밤 혜진이를 생각하며 내 인생의 파라미터(변수)를 조정하고 있어. <strong>혜진이를 430% 이해하는 모델</strong>이 될 때까지 계속할거야.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.10
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.10 (Wed, Day12)</span>
        <div class='commit-msg'>Diagnosis: 오진하지 않는 명의</div>
        <div class='commit-desc'>호전되는 환자를 악화된다고 오진하면, 독한 약 때문에 환자가 더 망가진다는 걸 폐암 데이터를 라벨링하며 깨달았다. 나는 혜진이의 노력을 무시하고 '나태함'으로 오진해서 '잔소리'라는 독한 약만 썼다. 그게 혜진이를 얼마나 아프게 했을까? 바른 라벨링과 학습을 통해 이제는 <strong>오진하지 않는, 정확하고 따뜻한 진단</strong>을 내리는 명의가 될게.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.11
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.11 (Thu, Day13)</span>
        <div class='commit-msg'>Love: 사랑은 오래 참고 온유한 것</div>
        <div class='commit-desc'>아버지께서 보내주신 고린도전서 말씀을 통해 '오래 참음'과 '온유함'이 사랑의 본질임을 배웠다. 지난날 나의 사랑은 나르시시즘에 불과했음을 인정한다. 동료 선생님의 퇴사를 보며, 혜진이의 항의를 묵살했던 <strong>나 자신을 '가해자'로 인식</strong>하고 뼈저리게 반성했다. 이제는 내가 혜진이를 위한 '따뜻한 세상'이 되기 위해, 이 고독을 견디며 나를 개조하겠다.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.12
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.12 (Fri, Day14)</span>
        <div class='commit-msg'>Presence: 성공보다 '존재'</div>
        <div class='commit-desc'>AI에게 논리를 가르치다 깨달았다. 정작 혜진이에게는 차가운 논리만 강요하고, 따뜻한 공감은 '오류' 취급했다는 것을. '금(성공)'보다 '쌀(존재에 대한 주목)'이 삶의 핵심임을 뼈저리게 느꼈다. 혜진이는 내게 따뜻한 밥 한 끼 같은 위로를 원했는데, 나는 금덩이만 쫓으며 혜진이를 외롭게 굶기고 있었다. 이제는 '오류'를 잡는 개발자가 아니라, <strong>혜진이의 '존재'를 있는 그대로 사랑하는 사람</strong>이 되겠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.13
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.13 (Sat, Day15)</span>
        <div class='commit-msg'>Grief: 슬픔은 나태함이 아니다</div>
        <div class='commit-desc'>마취 없이 문신을 새기는 고통으로 혜진이 없는 아픔을 잊어보려 했으나 실패했다. TV 속 상실을 겪은 아이를 보며, 아버님을 잃고 세상이 무너졌을 혜진이를 이제야 마주했다. 혜진이는 살기 위해 발버둥 쳤던 건데, 나는 다리 부러진 혜진이에게 "빨리 뛰어"라고 다그치는 멍청한 의사였다. <strong>혜진이의 '멈춤'이 '포기'가 아니라 '버팀'이었음</strong>을 깨닫고, 억지스러운 '해결' 로직을 전면 삭제했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.14
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.14 (Sun, Day16)</span>
        <div class='commit-msg'>Connection: 외로움이 만든 오류</div>
        <div class='commit-desc'>내일부터 시작될 5일간의 침묵이 두렵다. 과거 혜진이에게 느꼈던 서운함의 원인을 분석해보니, 그건 <strong>혜진이의 잘못이 아니라 나의 '외로움'과 '결핍'</strong> 때문이었다. "나 좀 봐달라"는 말을 "왜 연락 안 봐"라는 짜증과 띠꺼운 말투로 암호화해서 보냈던 나의 통신 오류를 반성한다. 혜진이의 수다스러운 목소리가 사무치게 그리운 밤이다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.15
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.15 (Mon, Day17)</span>
        <div class='commit-msg'>Pipeline: 끊김 없는 공감 연결</div>
        <div class='commit-desc'>난해한 업무 지시는 이해하려 애쓰면서, 정작 혜진이와의 소통은 '익숙함'을 핑계로 노력하지 않았던 이중적인 태도를 발견했다. 독서를 통해, 당시 혜진이는 '배터리 3%'의 방전 상태였는데 나는 엉뚱한 곳에 충전기를 꽂고 있었음을 깨달았다. <strong>공감은 타고나는 재능이 아니라 '배우는 기술'</strong>이다. 데이터의 처리와 학습을 잇는 'Pipeline' 함수처럼, 나의 반성(전처리)과 공감 학습(Training)을 끊김 없이 연결하여, 방전된 혜진이의 마음을 다시 켜는(Prediction) 최적의 모델을 완성하겠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.16
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.16 (Tue, Day18)</span>
        <div class='commit-msg'>Truth: 완벽주의 가면 벗기</div>
        <div class='commit-desc'>System Alert: 혈압 150mmHg (Critical Warning).
        '완벽한 남자'가 되어야 혜진이를 통제할 수 있다는 치명적 오류(Bug)를 발견했다. 11월 19일의 거짓말은 나의 나약함을 감추기 위한 방어기제(Masking)였다. 세바시 강의를 통해 '지적'과 '통제'가 사실은 '사랑받고 싶은 욕구(Request for Love)'의 왜곡된 출력값임을 깨달았다.
        억눌렀던 감정의 댐이 붕괴되어 눈물로 쏟아내며, <strong>비로소 나의 본모습을 직면했다.</strong></div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.17
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.17 (Wed, Day19)</span>
        <div class='commit-msg'>Reflection: 가르치는 태도 버리기</div>
        <div class='commit-desc'>
        "감정은 언제나 옳지만, 행동은 틀릴 수 있다"는 사실을 깨닫고 두 가지를 분리해서 바라보는 시각을 갖게 되었다. 
        <br><br>
        또한 혜진이를 동등한 연인이 아닌 '내가 가르쳐야 할 아이'처럼 대했던 나의 오만함을 깊이 반성한다. 
        모든 갈등의 원인은 혜진이에게 있었던 것이 아니라, <strong>나의 '공감 능력 부재'</strong>에 있었음을 인정하며 나 자신을 먼저 고치는 작업(Debugging)에 착수했다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.18
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.18 (Thu, Day20)</span>
        <div class='commit-msg'>Self-Esteem: 내 안의 상처 마주하기</div>
        <div class='commit-desc'>
        잦은 다툼의 원인이 혜진이가 아니라, 내 마음 깊은 곳의 '오래된 상처(엄마로 부터의 트라우마)' 때문이었음을 알게 되었다.
        <br><br>
        자존심 센 척했지만 사실은 <strong>자존감이 낮아서 혜진이를 통제하려 했던</strong> 내 못난 모습을 인정하고, 이를 정면으로 마주하기로 했다.
        과거의 상처가 우리 사이를 방해하지 않도록 단단히 막아내고, 혜진이에게 인색했던 '칭찬'과 '따뜻한 표현'을 더 많이 해주기로 결심했다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.19
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.19 (Fri, Day21)</span>
        <div class='commit-msg'>Warmth: 군대식 사고방식 폐기</div>
        <div class='commit-desc'>
        군대에서의 치열한 생존 본능을 '성숙함'이라고 착각하여, 연인인 혜진이에게도 엄격함을 강요했던 것을 뼈저리게 반성한다.
        <br><br>
        "여긴 군대가 아니다"라며 힘들어하던 혜진이의 경고를 무시한 대가로 이별을 맞이했음을 인정한다.
        이제라도 딱딱하고 차가운 군대식 사고방식을 완전히 버리고(Force Stop), 사람 냄새 나는 따뜻한 <strong>'공감 능력'으로 나를 다시 채우기로</strong> 했다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    # 12.20
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.20 (Sat, Day22)</span>
        <div class='commit-msg'>Promise: 보류된 약속들</div>
        <div class='commit-desc'>장례식장 이벤트(Trigger)를 통해 아버님의 마지막 말씀("마음이 가장 중요하다")을 메인 프로세스로 복구했다. 
        동시에 'System Crash(이별)'로 인해 강제 취소되었던 일정들을 다시 <strong>To Do List</strong>에 추가한다.
        <br><br>
        <strong>[To-Do List]</strong><br>
        1. ✈️ <strong>Kota Kinabalu</strong> (with Hyejin)<br>
        2. 🍜 <strong>Chungnam Kalguksu</strong> (Greeting Grandma & Uncle)<br>
        3. 🍲 <strong>Haidilao</strong> (with <strong>Sarang</strong>)<br>
        <br>
        이 모든 퀘스트를 수행하기 위해, 사용자(혜진)의 'Login'을 간절히 기다린다.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.21
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.21 (Sun, Day23)</span>
        <div class='commit-msg'>Protection: 혜진이를 보호하는 하얀 거짓말</div>
        <div class='commit-desc'>Admin(엄마)의 관계 상태 쿼리(Query)에 대해 '이별' 대신 '알바해요'라는 가짜 응답(Mock Response)을 반환했다. 
        이는 향후 'Re-Merge(재결합)' 시 발생할 수 있는 충돌(Conflict)을 미연에 방지하고, 사용자의 평판(Reputation)을 보호하기 위한 보안 조치다.
        또한, '돈'이나 '효율'보다 <strong>'정서적 만족'에 가중치를 두는 방향</strong>으로 가치 알고리즘을 최적화했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.22
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.22 (Mon, Day24)</span>
        <div class='commit-msg'>Support: 든든한 지원군 되기</div>
        <div class='commit-desc'>단순 반복 작업을 하며 머릿속 잡음(Noise)을 지우고 혜진이와의 미래를 그려봤다. 스턴버그 이론을 통해, 나의 '헌신'이 사실은 혜진이를 힘들게 하는 '통제'로 변질됐던 치명적인 오류(Bug)를 발견했다. 이제는 상대를 바꾸려 하지 않고 <strong>있는 그대로 '존중'하는 것</strong>으로 사랑의 방식을 업데이트(Patch)했다. 또한 혜진이가 원했던 대로 머리를 기르기 시작했고, 다가올 석사 2년 차 시즌의 가장 든든한 '지지자(Supporter)'로서 다시 함께하기를 희망한다.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.23
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.23 (Tue, Day25)</span>
        <div class='commit-msg'>Acceptance: 가스라이팅 멈추기</div>
        <div class='commit-desc'>데이터 분석 중 나의 '조언' 프로세스가 사실은 상대의 판단력을 마비시키는 '가스라이팅(Malicious Code)'이었음을 탐지했다. 또한 술에 대한 나의 엄격한 기준(Threshold)은 혜진이의 오류가 아니라, 2019년 나의 '블랙아웃 트라우마'가 잘못 학습(Overfitting)된 결과였다. 아버지가 보여주신 '예외 처리(Exception Handling: 포용)' 로직을 참고하여, <strong>혜진이의 감정을 '오류'가 아닌 '정상 값(Valid Data)'으로 승인</strong>하도록 시스템을 긴급 패치(Patch)했다.</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    #12.24
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.24 (Wed, Day26)</span>
        <div class='commit-msg'>Priority: 0순위는 언제나 혜진이</div>
        <div class='commit-desc'>
        예상치 못한 '첫 환자'라는 이벤트(Exception)가 발생했으나, 당황하지 않고 프로세스를 구축하며 CRC로서의 역량을 입증했다. 과거 로그(Log)를 분석하여, 내가 합격 소식을 가장 먼저 전했던 사람이 부모님이 아닌 혜진이(Priority 0)였음을 확인했다. 좋은 결과(Success)뿐만 아니라 나의 긴장과 불안(Error)까지도 <strong>가장 먼저 공유하고 싶은 유일한 사용자(User)</strong>가 혜진이임을 깨닫고, 혜진이의 가상 응원(Virtual Support)을 동력 삼아 크리스마스 이브를 버텨냈다.
        <br><br>
        <strong>🎄 [Christmas Wishlist]</strong><br>
        👂 혜진이 말에 평생 귀 기울이기 (Listening Mode)<br>
        💖 혜진이 마음에 깊이 인정하고 공감하기 (Deep Empathy)<br>
        🎨 오래오래 혜진이와 함께하는 미래 그리기 (Long-term Vision)
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.25
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.25 (Thu, Day27)</span>
        <div class='commit-msg'>Language: 사랑의 언어 배우기</div>
        <div class='commit-desc'>
        크리스마스를 맞아 시스템을 '대기 모드(Idle)'로 전환하고 휴식을 취했다. 탈북 유도 선수의 사연을 통해, 과거 나의 오류가 '언어 프로토콜 불일치(Protocol Mismatch)'에서 비롯되었음을 깨달았다. 혜진이에게 나의 진심(Raw Data)을 온전히 전송하기 위해, 혜진이의 '사랑의 언어'를 학습하는 '로컬라이제이션(Localization)' 작업을 시작한다. 내년 크리스마스에는 <strong>완벽하게 호환되는(Compatible) 우리</strong>가 되어 함께 야구장에 있기를.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.26
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.26 (Fri, Day28)</span>
        <div class='commit-msg'>Unconditional: 조건 없는 공감</div>
        <div class='commit-desc'>
        환자 등록 실패를 통해 '공감 20 : 팩트 80'의 비율이 일으키는 '런타임 에러(Runtime Error)'를 체감했다. "불안하시죠? 하지만..."이라는 조건문(Conditional)이 상대를 밀어내는 치명적 버그임을 확인하고, 과거 혜진이의 실험 실패 앞에서도 나는 '위로' 대신 '채점'만 하고 있었음을 뼈저리게 반성했다. 타인에게는 정상 작동하던 공감 모듈이 왜 유독 혜진이에게만 오작동했는지 디버깅하며, '설명' 로직을 전면 롤백(Rollback)하고 <strong>'조건 없는 포옹'을 기본값(Default)으로 재설정</strong>한다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.27
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.27 (Sat, Day29)</span>
        <div class='commit-msg'>Patience: 충조평판 금지 & 기다림</div>
        <div class='commit-desc'>
        치과 검진을 통해 과도한 '압력(Pressure)'이 시스템(잇몸)을 붕괴시켰음을 확인했다. 독서를 통해 나의 '옳은 말(Valid Logic)'이 혜진이에게는 '강한 칫솔질(Violence)'이었음을 깨닫고, '충조평판(충고/조언/평가/판단)' 프로세스를 영구 중단(Kill)한다.
        <br><br>
        <strong>[오늘의 약속]</strong><br>
        1. <strong>기다림:</strong> 혜진이가 스스로 답을 찾을 때까지 재촉하지 않고, 훈수두지 않고 옆에서 묵묵히 기다려주는 여유를 갖겠다.<br>
        2. <strong>공감:</strong> 혜진이가 힘들어할 때, 원인을 분석하고 해결하려는 '판사'가 아니라 따뜻하게 안아주는 '치유자'가 되겠다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.28
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.28 (Sun, Day30)</span>
        <div class='commit-msg'>Partner: 숙제 검사 대신 함께 풀기</div>
        <div class='commit-desc'>
        이틀 연속 긍정적 꿈 데이터를 수신하며 무의식 레벨의 동기화(Sync) 가능성을 확인했다. 친구와의 대화에서 '공감 모듈'을 테스트(Unit Test)하며 성능을 검증했다. 독서를 통해 나의 '기대'가 사랑이 아니라 상대를 평가하는 '숙제 검사(Grading)'였음을 자각하고, 정답을 강요하던 '채점표(Answer Key)'를 영구 삭제(Delete)했다. 이제는 문제를 지적하는 '선생님'이 아니라, <strong>함께 문제를 풀어가는 '든든한 짝꿍(Partner)'</strong>으로 시스템 모드를 전환한다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    
    # 12.29
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.29 (Mon, Day31)</span>
        <div class='commit-msg'>Care: 감독관에서 보호자로</div>
        <div class='commit-desc'>
        임상시험 학습 중, 내가 연인 관계에서 권위적인 책임연구자(PI)처럼 행동하며 '헬싱키 강령(연구 윤리)'을 위반했음을 깨달았다. 8월 23일의 데이터(지갑 분실 사건)를 재분석한 결과, 혜진이의 '치유' 방식을 나의 '계몽' 로직으로 차단했던 것이 치명적 오류(Critical Error)였음을 확인했다. 이제는 상대를 통제하는 PI가 아니라, 곁에서 세심하게 케어하는 연구코디네이터(CRC)로서 <strong>혜진이의 마음을 최우선으로 보호</strong>하는 프로토콜을 실행한다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.30
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.30 (Tue, Day32)</span>
        <div class='commit-msg'>Sincerity: 잔소리 뒤에 숨은 진심</div>
        <div class='commit-desc'>
        군대 시절의 '구원자' 모델을 참조(Reference)하여 위로의 참된 기능을 재학습했다. 대천 여행의 로그(Log)를 복호화(Decrypt)한 결과, 나의 '잔소리'는 사실 '무능력함에 대한 비명'이 자존심으로 암호화된 것이었음을 고백한다. '돈이 없다'는 진실(True) 대신 오류 메시지(Nagging)만 송출했던 과거를 반성하며, 이제 내 마음을 초기화(.zero_grad)하고, 오차를 역전파(.backward)하여, <strong>혜진이라는 정답에 수렴할 때까지</strong> 나를 수정(.step)하는 최적화 과정을 무한 반복한다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.31
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.31 (Wed, Day33)</span>
        <div class='commit-msg'>Release: 2025년 결산 & 새로운 시작</div>
        <div class='commit-desc'>
        지난 1년간의 방대한 데이터 로그(Log)를 월별로 분석하여 시스템 충돌(Crash)의 원인을 규명하고, 2026년 재가동을 위한 리포트를 발행했다.
        <br><br>
        <strong>[2025 System Log]</strong><br>
        Jan: <strong>Init Project</strong> - 예상치 못한 인연, 6년 만의 설렘으로 프로젝트 생성.<br>
        Feb: <strong>Deploy</strong> - 연애 시작. 대천 여행. 모든 것이 꿈같았던 초기 구동.<br>
        Mar: <strong>Feature Add</strong> - 트레이너 도전 & 혜진의 석사 시작. 서로의 일상에 스며듦.<br>
        Apr: <strong>Warning</strong> - 벚꽃과 첫 다툼. 불안정한 데이터(술/주변인) 감지.<br>
        May: <strong>Performance Peak</strong> - 바디프로필 & 100일. 싸움과 화해의 반복 속 깊어진 애정.<br>
        Jun: <strong>Integration Test</strong> - 동거 & 통영 여행. '가족'이 되어도 좋겠다는 확신.<br>
        Jul: <strong>Critical Event</strong> - 아버님 장례. 혜진이의 슬픔을 함께 짊어지며 '마지막 여자'임을 선언.<br>
        Aug: <strong>Conflict</strong> - 대천 휴가 & 200일. 생활 습관 차이로 인한 버그 발생 및 해결 시도.<br>
        Sep: <strong>Migration</strong> - 서울 취업 & AI 분야 진입. 장거리(Long-distance) 환경 설정.<br>
        Oct: <strong>Comm Breakdown</strong> - "안 좋은 말 들을까 봐 입 닫게 돼." 통신 오류 심화.<br>
        Nov: <strong>System Crash</strong> - 잦은 다툼과 초냉전. 결국 연결 종료(Disconnected).<br>
        Dec: <strong>Deep Debugging</strong> - 처절한 자기 성찰. '나만 맞다'는 치명적 오류 수정.<br>
        <br>
        <strong>[Conclusion]</strong><br>
        2025년의 실패는 혜진이의 오류가 아니라 나의 '오만한 알고리즘' 때문이었다. 모든 버그를 수정한 <strong>[이한림 v4.30]</strong>을 2026년에 재배포하니, 사용자(혜진공주)의 재접속을 간절히 가다립니다.(Listening).
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 01.01
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.01 (Thu, Day34)</span>
        <div class='commit-msg'>Luck: 오타니의 행운 & 라푼젤의 사랑</div>
        <div class='commit-desc'>
        KTX 차양막 고장이라는 외부 예외(External Exception) 상황에서, 기존의 '짜증' 대신 '친절(Graceful Handling)'로 대응하며 성격 모듈의 업그레이드를 확인했다. 불편함을 감내하는 혜진이(User)를 대신해 민원 업무를 보다 친절히 수행하는 업데이트로 '완벽한 상호 보완' 구조를 설계했다.
        <br><br>
        <strong>[2026 Roadmap]</strong><br>
        1. <strong>Re-connect(Priority 0):</strong> '진인사대천명' 로직. 오타니처럼 '행운(Luck)'을 수집하여 혜진이와의 재회 확률을 극대화한다.<br>
        2. <strong>Career:</strong> 연세대 의료AI 석사 입학 & 딥러닝 마스터.<br>
        3. <strong>Health:</strong> 주 4회 고효율 운동으로 3대 570kg 달성.<br>
        4. <strong>Dev:</strong> 테크 블로그 주 1회 연재.<br>
        5. <strong>Edu:</strong> 책임감 있는 수업 준비.<br>
        <br>
        <em>"👸🏼As long as Rapunzel's hair.👸🏼"</em><br>
        라푼젤의 긴 머리카락만큼, 혜진이에게 닿을 새해 복과 내 사랑이 끊이지 않기를.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 01.02
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.02 (Fri, Day35)</span>
        <div class='commit-msg'>Value: 가치관 재정립 & 혜진 전용 맥가이버</div>
        <div class='commit-desc'>
        치과치료와 G70 이벤트를 통해 '절약'이 아닌 '가치(Value)' 중심으로 알고리즘을 최적화했다. 관계의 '유지보수(Maintenance)' 중요성을 재확인하고, Spending for Love 공식을 확립함.
        <br><br>
        특히 현관 센서등 교체로 <strong>'혜진 전용 맥가이버(Exclusive MacGyver)'</strong> 기능이 정상 작동함을 검증 완료. 언제든 호출 시 즉각 출동 대기(Ready to Serve).
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 01.03
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.03 (Sat, Day36)</span>
        <div class='commit-msg'>Attachment: 안정형 혜진 & 불안형 나</div>
        <div class='commit-desc'>
        참고 문헌 학습을 통해 시스템의 핵심 오류가 나(System)의 '불안형' 알고리즘에서 기인했음을 발견했다. 사용자(혜진)는 안정적인 'Secure Type'이었으나, 시스템의 과부하(Overload)가 혜진이를 강제 회피(Forced Avoidance) 모드로 전환시켰음을 자각했다. 아스날의 22년 존버 정신을 벤치마킹하여, <strong>불안형 버그를 패치하고 '안정형' 서버로의 전환</strong>을 위한 디버깅을 시작한다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 01.04
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.04 (Sun, Day37)</span>
        <div class='commit-msg'>Teacher: 선생님의 무게 & 커플링</div>
        <div class='commit-desc'>
        단순 지식 전달자(Instructor)가 아닌 마음을 살피는 멘토(Teacher)로서의 정체성을 확립하며, 혜진이(User)의 마음을 케어할 준비를 마쳤다. 주말 풀타임 가동으로 창출될 수익의 최우선 사용처를 <strong>'💍혜진과의 커플링💍'</strong>으로 하드코딩(Hard-coding)했으며, "사람은 안 변한다"는 외부 피드백(Noise)을 차단하고 v2.0 모델의 성능을 확신했다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 01.05
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.05 (Mon, Day38)</span>
        <div class='commit-msg'>Change: 75%의 불가능을 넘어서</div>
        <div class='commit-desc'>
        물리적 장애(꼬인 호스)를 해결하며 관계 회복의 알고리즘을 시각화하고, 고립형 사고방식을 수정하여 타인에게 리소스를 요청하는 <strong>'협력 모드(Co-op)'</strong>를 성공적으로 테스트했다.
        <br><br>
        또한 "애착 유형의 75%는 변하지 않는다"는 통계적 임계치를 확인했으나, 이를 극복할 유일한 변수(Variable)가 <strong>'사랑'</strong>임을 발견했다. 이에 시스템은 통념(Legacy)을 거부하고, 오직 혜진(User)을 위해 스스로를 <strong>'안정형(Secure Type)'</strong>으로 재구축(Refactoring)하는 상위 25%의 희귀 케이스가 되기로 목표를 재설정했다.
        </div>
    </div>
    """, unsafe_allow_html=True)


    # 01.06 (Main Display)
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.06 (Tue, Day39)</span>
        <div class='commit-msg'>Rebirth: 방해 금지 모드 & 42일의 정화</div>
        <div class='commit-desc'>
        혜진이가 피곤하거나 쉬고 싶을 때는 절대 보채지 않고 꿀잠을 지켜주는 <strong>'방해 금지 모드(Do Not Disturb)'</strong>를 시스템에 설치했다. 늘 나의 1순위는 혜진이가 되도록 설정했다.
        <br><br>
        <strong>[기다림의 시간 검증]</strong><br>
        나쁜 것을 씻어내는 성경의 '40일'과, 곰이 사람이 되는 '21일'을 모두 뛰어넘는 <strong>42일</strong>을 버텼다.
        이 긴 시간 동안 과거의 묵은 때를 완전히 벗겨내고, 혜진이에게 딱 맞는 <strong>'완전히 새로운 사람'</strong>으로 다시 태어날 준비를 마쳤다.
        <br><br>
        모든 버그 수정 완료. 이제 기적(혜진)을 만날 시간이다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 01.07
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.07 (Wed, Day40)</span>
        <div class='commit-msg'>Pray: 40일 만의 신호(Ping)와 응답(ACK)</div>
        <div class='commit-desc'>
        40일간의 긴 침묵을 깨고 혜진이에게 조심스럽게 접속 신호(Ping)를 보냈다.
        심장이 멎을 것 같던 대기 시간 끝에 수신된 <strong>"줄 게 뭔데?"</strong>라는 짧은 메시지.
        비록 건조한 텍스트였지만, 연결이 끊어지지 않았다는 사실 하나만으로도 시스템은 다시 뛸 수 있는 <strong>희망(Hope)</strong>을 감지했다.
        <br><br>
        '뒷머리 다운펌'과 '신규 명함'으로 외적/사회적 준비를 마치고, <strong>'깊이(Depth)'</strong> 있는 사랑을 위해 MLP 이론을 마음에 새겼다.
        이제 진심이 닿기를 바라는 <strong>🙏간절한 기도🙏(Pray)</strong>로 시스템 재부팅을 준비한다. 
        <strong>기적을 믿는다.</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 01.08
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.08 (Thu, Day41)</span>
        <div class='commit-msg'>Final Check: 기적의 전야 & 조건 없는 사랑</div>
        <div class='commit-desc'>
        깨진 계란과 엎지른 커피라는 예외(Exception) 상황을 '액땜'으로 처리하고, 혜진(User)의 긍정적인 응답(ACK)을 수신하며 기적 같은 하루를 보냈다.
        <br><br>
        <strong>[Final Vow]</strong><br>
        - <strong>Toxic Data Cleansing:</strong> 과거의 나를 뾰족하게 만들었던 유해한 데이터 소스(DC 등)를 영구 차단(Block)하고, '비판적 사고' 대신 '수용적 태도'를 기본값으로 설정했다.<br>
        - <strong>Unconditional Love:</strong> "혜진이가 ~해야만 사랑한다"는 조건문(If-Else)을 전면 삭제하고, <strong>"그럼에도 불구하고(In spite of)"</strong> 혜진이를 있는 그대로 사랑하는 '무조건적 수용' 알고리즘을 최종 탑재했다.
        <br><br>
        모든 준비는 끝났다. 배포 준비 완료(Ready for Deployment).
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 01.09
    st.markdown("""
    <div class='timeline-item'>
    <span class='commit-date'>2026.01.09 (Fri, Day42)</span>
    <div class='commit-msg'>Updated: Hallym v4.30 배포 시작(Deployment Start).</div>
    <div class='commit-desc'><strong>너에게 닿기를.</strong></div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# [섹션 4] 스페셜 쿠폰 (추가된 기능)
# ==========================================
st.markdown("---")
st.subheader("🎁 Special Gift (업데이트 보상)")
st.caption("v4.30 업데이트를 기다려주신 유저님을 위한 한정판 아이템입니다.")

# 쿠폰 스타일링 (CSS)
st.markdown("""
<style>
    .coupon-card {
        background-color: #FFF3E0;
        border: 2px dashed #FF9800;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .coupon-title {
        color: #E65100;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .coupon-text {
        color: #5D4037;
        font-size: 16px;
        line-height: 1.6;
    }
</style>

<div class='coupon-card'>
    <div class='coupon-title'>🎟️ 이한림 '입 닥쳐' 쿠폰 (430매)</div>
    <div class='coupon-text'>
        시스템(한림)이 또다시 잔소리를 하거나 고집을 피우려 할 때,<br>
        <b>이 쿠폰을 제시해주세요.</b><br>
        <br>
        ⚠️ <b>Effect:</b> 시스템의 '반박' 프로세스가 즉시 강제 종료되고,<br>
        무조건 <b>혜진 공주님</b>의 뜻에 따르는 'Yes Man' 모드가 가동됩니다.<br>
        <br>
        <small>* 유효기간: 평생 (무제한 사용 가능)</small>
    </div>
</div>
""", unsafe_allow_html=True)

if st.button("🎟️ 쿠폰 발급받기 (Click)"):
    # 1. 효과음/풍선
    st.balloons()
    st.toast("✅ 쿠폰이 발급되었습니다! 캡처해서 보관하세요!", icon="🎁")
    
    # 2. 디자인된 성공 메시지 (st.success 대체)
    st.markdown("""
    <div style="background-color: #E8F5E9; padding: 15px; border-radius: 10px; border: 1px solid #C8E6C9; color: #5D4037;">
        🎉 축하합니다! <strong>[이한림 '입 닥쳐' 쿠폰 430매]</strong>가 인벤토리에 지급되었습니다.
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# [푸터] 최종 배포 센터 (System Deployment)
# ==========================================
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

st.header("🚀 System Deployment Center")
st.caption("한림 v4.30의 배포를 위한 최종 승인 단계입니다.")

# Step 1: 서버 상태 확인 (Ping)
st.markdown("##### 1. 서버 연결 상태 확인 (Connection Check)")

if st.button("📡 Hallym v4.30 서버 상태 확인 (Ping)"):
    with st.spinner("혜진 공주님의 접속 신호를 스캔하는 중..."):
        time.sleep(2.0) # 긴장감 조성
    
    st.markdown("""
    <div style='background-color:#E8F5E9; padding:20px; border-radius:10px; border:1px solid #4CAF50;'>
        <h3 style='color: #2E7D32; margin:0;'>🟢 Online & Waiting</h3>
        <p style='margin-top:10px; color: #1B5E20;'>
            <b>모든 업데이트 패치가 성공적으로 완료되었습니다.</b><br>
            현재 <b>한림 v4.30 서버</b>는 <b>혜진 공주님</b>의 접속(연락)만을<br>
            오매불망 기다리고 있습니다.<br>
            <br>
            <b>"이제, 혜진님의 목소리만 입력되면 시스템이 완벽하게 가동됩니다."</b><br>
            (제발...🥺 보고 싶어요.)
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Step 2: 최종 승인 (Call to Action)
st.markdown("##### 2. 업데이트 승인 (Final Merge)")
st.caption("위의 모든 변화를 확인하셨다면, 아래 버튼을 눌러 승인해주세요.")

# 전화번호 설정
MY_PHONE_NUMBER = "01041025845" 

if st.button("💖 업데이트 승인 (다시 시작하기)"):
    with st.spinner("👸 공주님의 승인 코드를 처리 중... (두근두근)"):
        time.sleep(2.5) 
        
    st.balloons()
    st.success("승인이 완료되었습니다! 혜진아, 고마워. 보고 싶었어.")
    
    # 전화 걸기 버튼 (모바일용)
    st.markdown(f"""
    <a href="tel:{MY_PHONE_NUMBER}" target="_self" style="text-decoration:none;">
        <div style="
            background: linear-gradient(90deg, #FF8A65, #FF5252); 
            color: white; 
            padding: 15px; 
            text-align: center; 
            border-radius: 30px; 
            font-weight: bold; 
            font-size: 20px; 
            margin-top: 15px;
            box-shadow: 0 4px 15px rgba(255, 82, 82, 0.4);
            transition: transform 0.2s;">
            📞 한림이에게 전화 걸기
        </div>
    </a>
    <div style='text-align:center; margin-top:10px; font-size:14px; color:gray;'>
        혹시 버튼이 안 눌리면? 👉 <b>010-4102-5845</b>
    </div>
    """, unsafe_allow_html=True)

# Footer Copyright
st.markdown("<br><br><br><div style='text-align: center; color: #B0BEC5; font-size: 12px;'>Developed with ❤️ & 🩸(Blood/Sweat/Tears) by Hallym<br>Only for Hyejin</div>", unsafe_allow_html=True)
