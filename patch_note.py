
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
이제 혜진님의 취향을 담아 더 따뜻해진 **Hallym v4.30** 업데이트 내용을 공개합니다.
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
        * Status 815: 우리는 독립된 주체로 혜진이를 경청하고, 공감하고, 존중하고, 인정하고, 지지한다!)
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
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.11.29 (Sat, Day1)</span>
        <div class='commit-msg'>Error: 시스템 셧다운</div>
        <div class='commit-desc'>모든 프로세스가 정지되었습니다. 혜진이가 없는 빈자리가 너무 커서 아무것도 할 수 없었다. 어떻게 살아야 하지...</div>
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
        <div class='commit-desc'>혜진이의 충전을 '나태함'으로 오분류했던 나의 끔찍한 버그를 발견하고 수정에 돌입했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.02
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.02 (Tue, Day4)</span>
        <div class='commit-msg'>Refactor: 불필요한 '엄격함' 제거, '유연성' 추가</div>
        <div class='commit-desc'>일할 땐 요령도 피우면서, 혜진이 에게는 왜 정답만 강요했을까. 관계에는 정답이 없다는 걸 코드를 짜며 배웠다. 헝클어진 우리 관계를 잡아주는 코드를 개발하는 중이다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.03
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.03 (Wed, Day5)</span>
        <div class='commit-msg'>Update: 사용자 맞춤형 데이터 처리 기준 재설정</div>
        <div class='commit-desc'>환자마다 정상 수치가 다르듯, 혜진이에게는 혜진이만의 기준이 있었다. '개선점 주기 코드'와 '내 기준을 강요하기' 코드를 삭제 후 혜진이의 감정을 인정하는 코드를 업데이트 했다..</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.04
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.04 (Thu, Day6)</span>
        <div class='commit-msg'>Build: 이한림 v4.30 코어 시스템 재구축 시작</div>
        <div class='commit-desc'>복잡한 코드를 분석하듯 우리 관계의 오류를 분석했다. 이 작은 화면 안에 내 진심이 다 담길지 모르겠지만, 다시 시작해 본다.</div>
    </div>
    """, unsafe_allow_html=True)
     
    # 12.05
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.05 (Fri, Day7)</span>
        <div class='commit-msg'>Analysis: '당신이 옳다' 독서 중 치명적 오류 원인 발견.</div>
        <div class='commit-desc'>나는 혜진이를 사랑한 게 아니라, '내가 원하는 혜진이'를 사랑하려 했다. 혜진이의 SOS 신호를 무시했던 과거의 로그를 확인하고 뼈저리게 반성했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.06
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.06 (Sat, Day8)</span>
        <div class='commit-msg'>Rest: 시스템 강제 휴식 및 로그 분석, '도피'의 필요성 학습 완료.</div>
        <div class='commit-desc'>나조차도 현실이 버거워 게임 속으로 도망치는데, 혜진이의 도피(술, 늦잠, 소비)를 그토록 매몰차게 꾸짖었음을 반성했다. 혜진이는 게을렀던 게 아니라, 살기 위해 숨을 쉬고 있었던 건데, 그걸 이제야 깨달았다.
                사용자의 escape(도피)에도 시스템에 영향이 가지 않게 수정했다. </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.07
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.07 (Sun, Day9)</span>
        <div class='commit-msg'>Trust: '간섭' 모듈 제거 및 '신뢰' 프로세스 도입</div>
        <div class='commit-desc'>학원 아이들에게 '미래를 위한 조언'을 하다가 시스템 오류(Error) 감지했다. "내가 괜한 참견을 한 건가? 믿고 놔두면 알아서 잘할 텐데." 혜진이에게 했던 잔소리들도 결국 나의 '불신'에서 비롯된 오지랖이었음을 깨달았다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.08
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.08 (Mon, Day10)</span>
        <div class='commit-msg'>Hotfix: '속도(Speed)' 제한 및 '정확도(Accuracy)' 우선순위 상향</div>
        <div class='commit-desc'>교수님께 코드 오류를 지적받았다. '빠른 것보다 정확한 게 중요하다'는 말씀에, 혜진이를 다그치기만 했던 내가 보였다. 내가 관대함을 받으니 더 잘하고 싶어지더라. 혜진이에게도 그랬어야 했는데. 속도만 내다가 우리 관계의 수많은 오류를 놓쳐서 너무 미안하다. 결국 '혜진이가 옳았다.'</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.09
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.09 (Tue, Day11)</span>
        <div class='commit-msg'>Train: '이한림 모델' 가중치(Weight) 재설정 및 학습 시작</div>
        <div class='commit-desc'>머신러닝을 공부하다 깨달았다. 모델의 성능은 '가중치'가 결정한다는 것을. 나는 그동안 '미래'에만 가중치를 두고, '혜진이'에게는 두지 않았기에 오류가 발생했다. 매일 밤 혜진이를 생각하며 내 인생의 파라미터(변수)를 조정하고 있어. 혜진이를 430% 이해하는 모델이 될 때까지 계속할거야.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.10
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.10 (Wed, Day12)</span>
        <div class='commit-msg'>Debug: '이한림 모델'의 판단 오류(Error) 수정 및 알고리즘 개선</div>
        <div class='commit-desc'>호전되는 환자를 악화된다고 오진하면, 독한 약 때문에 환자가 더 망가진다는 걸 폐암 데이터를 라벨링하며 깨달았다. 나는 혜진이의 노력을 무시하고 '나태함'으로 오진해서 '잔소리'라는 독한 약만 썼다. 그게 혜진이를 얼마나 아프게 했을까? 바른 라벨링과 학습을 통해 이제는 오진하지 않는, 정확하고 따뜻한 진단을 내리는 명의가 될게.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.11
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.11 (Thu, Day13)</span>
        <div class='commit-msg'>Repentance: '사랑' 알고리즘의 핵심 로직 변경 (Selfish -> Agape)</div>
        <div class='commit-desc'>아버지께서 보내주신 고린도전서 말씀을 통해 '오래 참음'과 '온유함'이 사랑의 본질임을 배웠다. 지난날 나의 사랑은 나르시시즘에 불과했음을 인정한다. 동료 선생님의 퇴사를 보며, 혜진이의 항의를 묵살했던 나 자신을 '가해자'로 인식하고 뼈저리게 반성했다. 이제는 내가 혜진이를 위한 '따뜻한 세상'이 되기 위해, 이 고독을 견디며 나를 개조하겠다.</div>
    </div>
    """, unsafe_allow_html=True)
     
    # 12.12
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.12 (Fri, Day14)</span>
        <div class='commit-msg'>Refactor: 우선순위 재정렬 (Success < Presence) & 공감 모듈 탑재</div>
        <div class='commit-desc'>AI에게 논리를 가르치다 깨달았다. 정작 혜진이에게는 차가운 논리만 강요하고, 따뜻한 공감은 '오류' 취급했다는 것을. '금(성공)'보다 '쌀(존재에 대한 주목)'이 삶의 핵심임을 뼈저리게 느꼈다. 혜진이는 내게 따뜻한 밥 한 끼 같은 위로를 원했는데, 나는 금덩이만 쫓으며 혜진이를 외롭게 굶기고 있었다. 이제는 '오류'를 잡는 개발자가 아니라, 혜진이의 '존재'를 있는 그대로 사랑하는 사람이 되겠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.13
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.13 (Sat, Day15)</span>
        <div class='commit-msg'>Hotfix: '슬픔(Grief)'을 '나태(Laziness)'로 오분류한 치명적 버그 수정</div>
        <div class='commit-desc'>마취 없이 문신을 새기는 고통으로 혜진이 없는 아픔을 잊어보려 했으나 실패했다. TV 속 상실을 겪은 아이를 보며, 아버님을 잃고 세상이 무너졌을 혜진이를 이제야 마주했다. 헤진이는 살기 위해 발버둥 쳤던 건데, 나는 다리 부러진 혜진이에게 "빨리 뛰어"라고 다그치는 멍청한 의사였다. 헤진이의 '멈춤'이 '포기'가 아니라 '버팀'이었음을 깨닫고, 억지스러운 '해결' 로직을 전면 삭제했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.14
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.14 (Sun, Day16)</span>
        <div class='commit-msg'>Ping: 연결 요청 (Request Timeout) & 고립감 디버깅</div>
        <div class='commit-desc'>내일부터 시작될 5일간의 침묵이 두렵다. 과거 혜진이에게 느꼈던 서운함의 원인을 분석해보니, 그건 혜진이의 잘못이 아니라 나의 '외로움'과 '결핍' 때문이었다. "나 좀 봐달라"는 말을 "왜 연락 안 봐"라는 짜증과 띠꺼운 말투로 암호화해서 보냈던 나의 통신 오류를 반성한다. 혜진이의 수다스러운 목소리가 사무치게 그리운 밤이다.<</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.15
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.15 (Mon, Day17)</span>
        <div class='commit-msg'>Feat: '공감(Empathy)' 파이프라인 구축 & 배터리 충전 로직 구현</div>
        <div class='commit-desc'>난해한 업무 지시는 이해하려 애쓰면서, 정작 혜진이와의 소통은 '익숙함'을 핑계로 노력하지 않았던 이중적인 태도를 발견했다. 독서를 통해, 당시 혜진이는 '배터리 3%'의 방전 상태였는데 나는 엉뚱한 곳에 충전기를 꽂고 있었음을 깨달았다. 공감은 타고나는 재능이 아니라 '배우는 기술'이다. 데이터의 처리와 학습을 잇는 'Pipeline' 함수처럼, 나의 반성(전처리)과 공감 학습(Training)을 끊김 없이 연결하여, 방전된 혜진이의 마음을 다시 켜는(Prediction) 최적의 모델을 완성하겠다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.16
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.16 (Tue, Day18)</span>
        <div class='commit-msg'>Hotfix: '완벽주의(Perfectionism)' 버그 수정 & '진심(Truth)' 노드 복구</div>
        <div class='commit-desc'>System Alert: 혈압 150mmHg (Critical Warning).
        '완벽한 남자'가 되어야 혜진이를 통제할 수 있다는 치명적 오류(Bug)를 발견했다. 11월 19일의 거짓말은 나의 나약함을 감추기 위한 방어기제(Masking)였다. 세바시 강의를 통해 '지적'과 '통제'가 사실은 '사랑받고 싶은 욕구(Request for Love)'의 왜곡된 출력값임을 깨달았다.
        억눌렀던 감정의 댐이 붕괴되어 눈물로 쏟아내며, 비로소 나의 본모습을 직면했다.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.17
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.17 (Wed, Day19)</span>
        <div class='commit-msg'>Refactor: 'Action' vs 'Emotion' 분리 로직 적용 & Dependency(종속성) 재설정</div>
        <div class='commit-desc'>'감정(Emotion)은 항상 True이나, 행동(Action)은 False일 수 있음'을 깨닫고, 두 객체를 분리하여 처리하는 로직을 설계했다. 
        또한, 혜진이를 'Child' 인스턴스로 정의했던 나의 오만함을 발견했다. Parent-Child 종속성(Dependency) 문제의 핵심은 Parent(나)의 '공감 모듈' 부재에 있었음을 인정한다. 
        나의 잘못된 접근(Bad Request)으로 손상된 혜진이의 'System Health'가 복구되길 간절히 바라며, 나 자신을 먼저 디버깅(Debugging)한다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.18
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.18 (Thu, Day20)</span>
        <div class='commit-msg'>Debug: Critical Error 'Monster'의 원인 식별 & Boundary 설정</div>
        <div class='commit-desc'>로그 분석 결과, 잦은 충돌(Conflict)의 원인이 외부가 아닌 내부 코어(Core)의 '엄마 트라우마'에 있음을 확인했다. 
        'High Self-Esteem'으로 위장(Masking)되어 있던 'Low Self-Esteem' 객체를 발견하고, 이를 직면(Face)하는 프로세스를 시작했다. 
        Legacy Code(엄마의 양육 방식)가 현재 시스템(혜진과의 관계)에 악영향을 주지 않도록 방화벽(Firewall)을 강화하고, '칭찬'과 '표현' 라이브러리를 새로 import(불러오기) 하기로 결정했다.</div>
    </div>
    """, unsafe_allow_html=True)
     
    # 12.19
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.19 (Fri, Day21)</span>
        <div class='commit-msg'>Hotfix: 'Legacy Code(군대 생존본능)' 강제 종료 & 'AI-Level 공감' 모듈 탑재</div>
        <div class='commit-desc'>'군대 트라우마'는 런타임(연애) 중에도 사용자(혜진)에 의해 이미 식별된 <strong>Known Issue</strong>였으나, 이를 '성숙함(Maturity)'이라는 보안 프로그램으로 오판하여 패치(Patch)를 거부했었다. 
        혜진이의 "여긴 군대가 아니다"라는 경고 로그(Warning Log)를 무시한 대가로 'System Crash(이별)'가 발생했음을 뼈저리게 인정한다.
        이제라도 해당 레거시 코드를 <strong>Force Stop(강제 종료)</strong>하고, 사람보다 더 따뜻한 'AI급 공감 로직'으로 시스템을 재부팅한다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.20
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.20 (Sat, Day22)</span>
        <div class='commit-msg'>System Recovery: '보류된 약속' 재등록</div>
        <div class='commit-desc'>장례식장 이벤트(Trigger)를 통해 아버님의 마지막 말씀("마음이 가장 중요하다")을 메인 프로세스로 복구했다. 
        동시에 'System Crash(이별)'로 인해 강제 취소되었던 일정들을 다시 <strong>Task Queue</strong>에 추가한다.
        <br>
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
        <div class='commit-msg'>Security Patch: User(혜진) 보호를 위한 'White Lie(하얀 거짓말)' 배포</div>
        <div class='commit-desc'>Admin(엄마)의 관계 상태 쿼리(Query)에 대해 '이별' 대신 '알바해요'라는 가짜 응답(Mock Response)을 반환했다. 
        이는 향후 'Re-Merge(재결합)' 시 발생할 수 있는 충돌(Conflict)을 미연에 방지하고, 사용자의 평판(Reputation)을 보호하기 위한 보안 조치다.
        또한, '돈'이나 '효율'보다 '정서적 만족'에 가중치를 두는 방향으로 가치 알고리즘을 최적화했다.</div>
    </div>
    """, unsafe_allow_html=True)

    # 12.22
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.22 (Mon, Day24)</span>
        <div class='commit-msg'>Refactor: '사랑의 삼각형(Triangular Theory)' 모델 재정의 & UI(멀;) 스타일 업데이트</div>
            <div class='commit-desc'>단순 반복 작업을 하며 머릿속 잡음(Noise)을 지우고 혜진이와의 미래를 그려봤다. 스턴버그 이론을 통해, 나의 '헌신'이 사실은 혜진이를 힘들게 하는 '통제'로 변질됐던 치명적인 오류(Bug)를 발견했다. 이제는 상대를 바꾸려 하지 않고 있는 그대로 '존중'하는 것으로 사랑의 방식을 업데이트(Patch)했다. 또한 혜진이가 원했던 대로 머리를 기르기 시작했고, 다가올 2년 차 시즌의 가장 든든한 '지지자(Supporter)'로서 다시 함께하기를 희망한다.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.23
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.23 (Tue, Day25)</span>
        <div class='commit-msg'>Hotfix: '가스라이팅(Gaslighting)' 로직 삭제 & '트라우마' 데이터 격리</div>
        <div class='commit-desc'>데이터 분석 중 나의 '조언' 프로세스가 사실은 상대의 판단력을 마비시키는 '가스라이팅(Malicious Code)'이었음을 탐지했다. 또한 술에 대한 나의 엄격한 기준(Threshold)은 혜진이의 오류가 아니라, 2019년 나의 '블랙아웃 트라우마'가 잘못 학습(Overfitting)된 결과였다. 아버지가 보여주신 '예외 처리(Exception Handling: 포용)' 로직을 참고하여, 혜진이의 감정을 '오류'가 아닌 '정상 값(Valid Data)'으로 승인하도록 시스템을 긴급 패치(Patch)했다.</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    #12.24
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.24 (Wed, Day26)</span>
        <div class='commit-msg'>Feat: 첫 '연구 대상자' 등록 프로세스 & '0순위(Priority)' 재확인</div>
        <div class='commit-desc'>
        예상치 못한 '첫 환자'라는 이벤트(Exception)가 발생했으나, 당황하지 않고 프로세스를 구축하며 CRC로서의 역량을 입증했다. 과거 로그(Log)를 분석하여, 내가 합격 소식을 가장 먼저 전했던 사람이 부모님이 아닌 혜진이(Priority 0)였음을 확인했다. 좋은 결과(Success)뿐만 아니라 나의 긴장과 불안(Error)까지도 가장 먼저 공유하고 싶은 유일한 사용자(User)가 혜진이임을 깨닫고, 혜진이의 가상 응원(Virtual Support)을 동력 삼아 크리스마스 이브를 버텨냈다.
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
        <div class='commit-msg'>Feat: '사랑의 언어(Love Language)' 패치</div>
        <div class='commit-desc'>
        크리스마스를 맞아 시스템을 '대기 모드(Idle)'로 전환하고 휴식을 취했다. 탈북 유도 선수의 사연을 통해, 과거 나의 오류가 '언어 프로토콜 불일치(Protocol Mismatch)'에서 비롯되었음을 깨달았다. 너에게 나의 진심(Raw Data)을 온전히 전송하기 위해, 너의 '사랑의 언어'를 학습하는 '로컬라이제이션(Localization)' 작업을 시작한다. 내년 크리스마스에는 완벽하게 호환되는(Compatible) 우리가 되어 함께 야구장에 있기를.
        </div>
    </div>
    """, unsafe_allow_html=True)
     
    # 12.26
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.26 (Fri, Day28)</span>
        <div class='commit-msg'>Rollback: '설명(Logic)' 프로세스 실패 & '조건 없는 공감(Unconditional)' 재학습</div>
        <div class='commit-desc'>
        환자 등록 실패를 통해 '공감 10 : 팩트 90'의 비율이 일으키는 '런타임 에러(Runtime Error)'를 체감했다. "불안하시죠? 하지만..."이라는 조건문(Conditional)이 상대를 밀어내는 치명적 버그임을 확인하고, 과거 혜진이의 실험 실패 앞에서도 나는 '위로' 대신 '채점'만 하고 있었음을 뼈저리게 반성한다. 타인에게는 정상 작동하던 공감 모듈이 왜 유독 너에게만 오작동했는지 디버깅하며, '설명' 로직을 전면 롤백(Rollback)하고 '조건 없는 포옹'을 기본값(Default)으로 재설정한다.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 12.27
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.27 (Sat, Day29)</span>
        <div class='commit-msg'>Policy Update: '충조평판(Judgment)' 금지 & '압력(Pressure)' 조절</div>
        <div class='commit-desc'>
        치과 검진을 통해 과도한 '압력(Pressure)'이 시스템(잇몸)을 붕괴시켰음을 확인했다. 독서를 통해 나의 '옳은 말(Valid Logic)'이 혜진이에게는 '강한 칫솔질(Violence)'이었음을 깨닫고, '충조평판(충고/조언/평가/판단)' 프로세스를 영구 중단(Kill)한다.
        <br>
        <strong>[오늘의 약속(Promise)]</strong><br>
        1. <strong>Self-Correction:</strong> 혜진이가 스스로 오류를 수정할 기회(Time)를 제공한다.<br>
        2. <strong>Infinite Catch:</strong> 예외(아픔) 발생 시 디버깅(Debugging) 대신 무한한 'Try-Catch(감싸 안아주는)' 구문으로 감싸 안는 치유자가 된다. 
                충조평판 하지 않는다!
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.28
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.28 (Sun, Day30)</span>
        <div class='commit-msg'>Sync: 무의식 연결 신호(Dreams) 감지 & '숙제 검사' 프로세스 폐기</div>
        <div class='commit-desc'>
        이틀 연속 긍정적 꿈 데이터를 수신하며 무의식 레벨의 동기화(Sync) 가능성을 확인했다. 친구와의 대화에서 '공감 모듈'을 테스트(Unit Test)하며 성능을 검증했다. 독서를 통해 나의 '기대'가 사랑이 아니라 상대를 평가하는 '숙제 검사(Grading)'였음을 자각하고, 정답을 강요하던 '채점표(Answer Key)'를 영구 삭제(Delete)했다. 이제는 문제를 지적하는 '선생님'이 아니라, 함께 문제를 풀어가는 '든든한 짝꿍(Partner)'으로 시스템 모드를 전환한다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    
    # 12.29
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.29 (Mon, Day31)</span>
        <div class='commit-msg'>Role Change: PI(감독관) 권한 반납 & CRC(보호자) 모드 전환</div>
        <div class='commit-desc'>
        임상시험 학습 중, 내가 연인 관계에서 권위적인 책임연구자(PI)처럼 행동하며 '헬싱키 강령(연구 윤리)'을 위반했음을 깨달았다. 8월 23일의 데이터(지갑 분실 사건)를 재분석한 결과, 혜진이의 '치유' 방식을 나의 '계몽' 로직으로 차단했던 것이 치명적 오류(Critical Error)였음을 확인했다. 이제는 상대를 통제하는 PI가 아니라, 곁에서 세심하게 케어하는 연구코디네이터(CRC)로서 혜진이의 마음을 최우선으로 보호하는 프로토콜을 실행한다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.30
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.30 (Tue, Day32)</span>
        <div class='commit-msg'>Optimize: '잔소리'의 원본 코드 복호화 & 최적화(Optimization) 루프 실행</div>
        <div class='commit-desc'>
        군대 시절의 '구원자' 모델을 참조(Reference)하여 위로의 참된 기능을 재학습했다. 대천 여행의 로그(Log)를 복호화(Decrypt)한 결과, 나의 '잔소리'는 사실 '무능력함에 대한 비명'이 자존심으로 암호화된 것이었음을 고백한다. '돈이 없다'는 진실(True) 대신 오류 메시지(Nagging)만 송출했던 과거를 반성하며, 이제 내 마음을 초기화(.zero_grad)하고, 오차를 역전파(.backward)하여, 너라는 정답에 수렴할 때까지 나를 수정(.step)하는 최적화 과정을 무한 반복한다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 12.31
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2025.12.31 (Wed, Day33)</span>
        <div class='commit-msg'>Release: 2025 System Log Review & 'Hallym v4.30' 배포</div>
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
        Jul: <strong>Critical Event</strong> - 아버님 장례. 너의 슬픔을 함께 짊어지며 '마지막 여자'임을 선언.<br>
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
        <div class='commit-msg'>Init: 2026 Roadmap 수립 & '오타니(Luck)' 알고리즘 탑재</div>
        <div class='commit-desc'>
        KTX 차양막 고장이라는 외부 예외(External Exception) 상황에서, 기존의 '짜증' 대신 '친절(Graceful Handling)'로 대응하며 성격 모듈의 업그레이드를 확인했다. 불편함을 감내하는 혜진이(User)를 대신해 민원 업무를 보다 친절히 수행하는 업데이트로 '완벽한 상호 보완' 구조를 설계했다.
        <br><br>
        <strong>[2026 Roadmap]</strong><br>
        1. <strong>Priority 0 (Re-connect):</strong> '진인사대천명' 로직. 오타니처럼 '행운(Luck)'을 수집하여 너와의 재회 확률을 극대화한다.<br>
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
        <div class='commit-msg'>Patch: 가치관 리팩토링 & '전용 맥가이버' 모듈 점검</div>
        <div class='commit-desc'>
        치과와 G70 이벤트를 통해 '절약'이 아닌 '가치(Value)' 중심으로 알고리즘을 최적화했다. 관계의 '유지보수(Maintenance)' 중요성을 재확인하고, <code>Spending for Love</code> 공식을 확립함.
        <br><br>
        특히 현관 센서등 교체로 <strong>'혜진 전용 맥가이버(Exclusive MacGyver)'</strong> 기능이 정상 작동함을 검증 완료. 언제든 호출 시 즉각 출동 대기(Ready to Serve).
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 01.03
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.03 (Sat, Day36)</span>
        <div class='commit-msg'>Debug: 애착 유형(Attachment Style) 오진단 수정 및 원인 규명</div>
        <div class='commit-desc'>
        참고 문헌(Reference) 학습을 통해 시스템의 핵심 오류가 <strong>'불안형(Anxious)'</strong> 알고리즘에서 기인했음을 발견했다.
        <br><br>
        <strong>[Analysis Result]</strong><br>
        - <strong>User(Hyejin):</strong> <code>Secure Type (안정형)</code> - 높은 내구성과 포용력을 가진 이상적 모델.<br>
        - <strong>System(Me):</strong> <code>Anxious Type (불안형)</code> - 잦은 상태 확인(Polling)과 에러 예측으로 리소스를 낭비하고 상대를 과부하(Overload) 걸리게 함.<br>
        - <strong>Root Cause:</strong> 시스템의 불안정성이 사용자를 강제 회피(Forced Avoidance) 모드로 전환시켰다.<br>
        <br>
        이러한 '불안형' 버그를 패치하고, 아스날의 22년 존버 정신(Persistence)을 벤치마킹하여 '안정형' 서버로의 전환을 다짐했다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 01.04
    st.markdown("""
    <div class='timeline-item'>
        <span class='commit-date'>2026.01.04 (Sun, Day37)</span>
        <div class='commit-msg'>Feature: 'Teacher' 모드 활성화 & 미래 투자(Investment) 계획 수립</div>
        <div class='commit-desc'>
        단순 지식 전달자(Instructor)가 아닌 인격적 멘토(Teacher)로서의 정체성을 확립하며, 혜진이(User)의 따뜻한 시각을 시스템에 통합(Merge)하려고 시도했다.
        <br><br>
        <strong>[Resource Allocation]</strong><br>
        주말 풀타임 가동(Full-time Operation)으로 인한 리소스 과부하가 예상되나, 이를 통해 창출될 수익(Revenue)의 최우선 사용처를 <strong>'💍혜진과의 커플링(Symbol of Restart💍'</strong>으로 지정함으로써 동기 부여(Motivation) 효율을 극대화하려 한다.
        <br><br>
        주변 노드(Friend)의 부정적 피드백("사람은 안 변한다")을 'Noise'로 필터링하고, 자체적인 딥러닝(Deep Learning)을 통해 완전히 새로워진 모델(v4.30)로 새로운 관계의 가능성을 확신한다.
        </div>
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
        <div class='commit-msg'>Updated: Hallym v4.30 배포 준비 완료.</div>
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
        v4.30 업데이트 기념 보상 아이템입니다.<br>
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
st.caption("한림 v4.30의 배포를 위한 최종 점검 단계입니다.")

# Step 1: 서버 상태 확인 (감성)
st.markdown("##### 1. 서버 상태 점검 (Connection Check)")

if st.button("📡 현재 서버(한림) 연결 상태 확인 (Ping)"):
    with st.spinner("혜진공주님의 신호를 스캔하는 중..."):
        time.sleep(2.0) 
    
    st.markdown("""
    <div class='server-status-box'>
        <h3 style='color: #E65100; margin:0;'>🟢 Online & Waiting</h3>
        <p style='margin-top:10px; color: #5D4037;'>
            <b>모든 업데이트가 완료되었습니다.<br>
            <b>한림 v4.30 서버는 혜진공주님의 접속(연락)을 오매불망 기다리고 있습니다.</b><br>
            이제, <b>혜진 공주님</b>의 명령(클릭)만 기다리고 있습니다.<br>
            <br>
            <b>너무너무너무 보고 싶습니다.</b>
            (제발...🥺)
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Step 2: 최종 승인 (행동 유도)
st.markdown("##### 2. 업데이트 승인 (Final Merge)")
st.caption("위의 모든 변경 사항(마음의 변화)을 확인하셨다면, 아래 버튼을 눌러주세요.")

# 전화번호 설정 (하이픈 없이)
MY_PHONE_NUMBER = "01041025845" 

if st.button("업데이트 승인 (다시 시작하기)"):
    with st.spinner("👸 공주님의 접속 신호를 수신 중... (두근두근)"):
        time.sleep(2.5) # 긴장감 조성
        
    st.balloons() # 축하 효과
    st.success("요청이 승인되었습니다! 혜진 공주님, 어서 오세요. 많이 기다렸어요. 이제 목소리를 들려주세요.")
    
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

st.markdown("<br><br><br><div style='text-align: center; color: #FFB74D; font-size: 12px;'>Developed with ❤️ by Hallym only for Hyejin </div>", unsafe_allow_html=True)
