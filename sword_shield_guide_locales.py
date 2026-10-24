from typing import Any, Dict, List, Optional


_STEAM_URL = "https://store.steampowered.com/app/3282300/Mistfall_Hunter/"
_OFFICIAL_URL = "https://mistfallhunter.com/"
_FEATURE_IMAGE = "images/mistfall-hunter-sword-shield-build.webp"
_COMBAT_IMAGE = "images/mistfall-hunter-steam-store-combat.webp"
_EXTRACTION_IMAGE = "images/mistfall-hunter-steam-store-extraction.webp"


def _section(
    section_id: str,
    heading: str,
    paragraphs: List[str],
    bullets: Optional[List[str]] = None,
    links: Optional[List[Dict[str, str]]] = None,
    table: Optional[Dict[str, Any]] = None,
    steps: Optional[List[str]] = None,
    image: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    构造本地化文章使用的内容区块。

    :param section_id: 区块的稳定 HTML 锚点
    :param heading: 本地化区块标题
    :param paragraphs: 本地化正文段落
    :param bullets: 可选的要点列表
    :param links: 可选的站内链接列表
    :param table: 可选的表格数据
    :param steps: 可选的步骤列表
    :param image: 可选的图片数据
    :return: dict，包含模板所需的区块字段
    """
    return {
        "id": section_id,
        "heading": heading,
        "paragraphs": paragraphs,
        "bullets": bullets or [],
        "links": links or [],
        "table": table,
        "steps": steps or [],
        "image": image,
        "video": None,
    }


SWORD_SHIELD_LOCALIZED: Dict[str, Dict[str, Any]] = {
    "ko": {
        "slug": "mistfall-hunter-sword-and-shield-build",
        "primary_keyword": "Mistfall Hunter 검과 방패 빌드",
        "related_keywords": ["Mistfall Hunter 용병 검과 방패 빌드", "Mistfall Hunter 검과 방패 추천 빌드", "Mistfall Hunter 솔로 검과 방패 빌드", "Mistfall Hunter 3인 파티 검과 방패 빌드"],
        "title": "Mistfall Hunter 검과 방패 빌드: 솔로와 3인 파티를 위한 5가지 우선순위",
        "meta_title": "Mistfall Hunter 검과 방패 빌드: 5가지 우선순위",
        "meta_description": "Mistfall Hunter 검과 방패 빌드의 장비·기술 우선순위, 솔로와 3인 파티 조정법, 검증되지 않은 수치를 만들지 않는 반복 테스트 방법을 정리합니다.",
        "meta_keywords": "Mistfall Hunter 검과 방패 빌드, Mistfall Hunter 용병 빌드, 솔로 검과 방패 빌드, 3인 파티 검과 방패 빌드",
        "eyebrow": "Mistfall Hunter 무기 빌드 가이드",
        "lede": "검과 방패는 전투를 살피고 짧게 교전하며 빠져나갈 길을 남기는 운영에 어울립니다. 확인되지 않은 피해량 순위보다 반복할 수 있는 판단을 기준으로 장비를 구성하세요. 방어 수단 하나, 안정적으로 활용할 공격 기회 하나, 전열을 다시 정리할 방법 하나를 준비합니다. 일반적인 운영 원칙과 현재 버전에서 추가 확인이 필요한 수치는 구분합니다.",
        "checked_label": "역할 중심 빌드 기준, 2026년 10월 24일 검토; 정확한 아이템 수치는 단정하지 않음",
        "entry_label": "Mistfall Hunter 검과 방패 빌드 가이드 읽기",
        "checked_iso": "2026-10-24",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "검과 방패를 든 사냥꾼과 짧은 Sword + Shield 문구를 담은 편집용 콘셉트 아트", "caption": "이 가이드를 위해 만든 편집용 콘셉트 아트입니다. 공식 Mistfall Hunter 이미지나 실제 게임 화면이 아닙니다.", "source_label": "독립 가이드 소개", "source_url": "/ko/about/", "width": 1024, "height": 1024},
        "facts_headers": ["빌드 판단", "안전한 시작점", "조정할 때"],
        "facts_rows": [["역할", "공간을 지키고 후퇴 경로 남기기", "팀원이 이미 전열 역할을 맡음"], ["공격", "짧고 반복 가능한 기회 활용", "검증된 패치나 테스트로 타이밍이 바뀜"], ["장비", "생존 수단과 압박 선택지 하나씩 확보", "현재 설명을 보면 다른 교환이 더 적절함"], ["솔로", "탈출 경로가 분명할 때만 전리품 추가", "경로나 회복 수단이 불확실해짐"], ["3인 파티", "전열·공격·유연 역할을 나눔", "누군가 고립되거나 역할이 겹침"]],
        "intro": "Mistfall Hunter 검과 방패 빌드는 검증되지 않은 최적 장비 목록을 찾기보다 안정적인 역할부터 정하는 편이 좋습니다. 한 번의 불리한 교전 뒤에도 회복할 여지를 두고, 명확한 기회에서만 공격 자원을 쓰며, 진입하기 전에 빠져나올 방법을 결정하세요. 공개 자료는 게임의 탈출 구조와 장비 중심 진행을 설명하지만 특정 아이템 이름이나 능력치 또는 특성 순서가 계속 최선이라고 확인해 주지는 않습니다. 아래 기준을 시험 가능한 출발점으로 삼고 현재 게임 안에서 수치를 확인하세요.",
        "sections": [
            _section("build-goal", "검과 방패 빌드가 해결해야 할 문제", [
                "핵심 질문은 방패가 항상 다른 무기보다 좋은지가 아닙니다. 이 조합으로 교전을 선택하고 그 비용을 감당하며 안전한 경로로 돌아올 수 있는지를 살펴보세요. 근접 무기는 교전을 길게 끌기 쉽습니다. 방패는 모든 공격을 막아준다는 증거가 아니라 교전 시점을 통제하는 이유로 사용해야 합니다. 입력 방식, 방어 규칙, 회복 비용은 바뀔 수 있으므로 현재 설명을 읽고 직접 확인하세요.",
                "이 글은 역할을 기준으로 빌드를 계획하는 방법입니다. 통제된 교전을 선호하거나 전투를 익히거나 소규모 파티에서 맡을 일을 분명히 하고 싶은 플레이어에게 적합합니다. 검과 방패가 최고 피해량을 낸다거나 유일한 정답 또는 공식 메타라고 주장하지 않습니다. 현재 버전에서 클래스나 장비 이름이 달라졌다면 판단 원칙은 유지하고 실제 장비 화면의 이름을 사용하세요.",
            ], bullets=["교전 전에 회복 또는 이탈 수단 하나를 남깁니다.", "피해량 계산표 없이도 알아볼 수 있는 공격 기회를 고릅니다.", "다음 판에서 배울 수 있도록 아이템이나 기술은 한 번에 하나씩 바꿉니다."], image={"path": _COMBAT_IMAGE, "alt": "숲속의 큰 적과 마주한 Mistfall Hunter 캐릭터가 보이는 Steam 공식 전투 스크린샷", "caption": "간격과 전투 상황을 설명하기 위한 Steam 공식 이미지입니다. 검과 방패 빌드 실험이나 피해량을 보여주는 자료는 아닙니다.", "source_label": "Steam 공식 페이지 보기", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("five-build-priorities", "더 안전한 검과 방패 빌드를 위한 다섯 가지 우선순위", [
                "아래 기준은 고정된 능력치 이름이나 숨겨진 수식이 아니라 빌드로 할 수 있어야 하는 행동을 설명합니다. 현재 장비와 기술 설명을 열고 같은 역할을 하는 선택지를 찾으세요. 두 보너스가 모두 괜찮아 보인다면 숫자가 커 보이는 항목보다 반복해서 시험할 수 있는 항목을 우선합니다. 이렇게 해야 실제 플레이에서 내리는 판단을 비교할 수 있습니다.",
                "첫 시도는 단순해야 합니다. 생존 대응 하나, 재현 가능한 공격 동작 하나, 위험한 방을 빠져나올 여유를 준비하세요. 몇 차례 플레이한 뒤 계획이 무너진 지점을 확인합니다. 안전했지만 느렸다면 압박을 조정하고 피해를 줬지만 탈출로를 잃었다면 공격을 더하기 전에 회복이나 판단 시점을 손보세요.",
            ], table={"headers": ["우선순위", "확인할 내용", "피할 판단"], "rows": [["1. 이해 가능한 방어", "조건과 비용을 아는 선택지", "방패가 모든 피해를 막는다고 가정"], ["2. 반복 가능한 압박", "원하는 때 만들 수 있는 짧은 공격 기회", "안전 경로를 지나치며 추격"], ["3. 회복", "공간을 다시 확보할 분명한 수단", "첫 접촉에 방어 행동을 모두 사용"], ["4. 유효한 장비", "관찰한 문제를 해결하는 보너스", "현재 설명 없이 능력치 순위를 복사"], ["5. 팀 기여", "다른 역할을 보완하는 임무", "세 명이 같은 역할 선택"]]}, links=[{"target": "builds", "label": "세부 구성과 일반 빌드 패턴 비교하기"}]),
            _section("gear-skills", "역할에 맞춰 장비·기술·특성 선택하기", [
                "현재 버전에서 아이템이나 특성 설명을 읽고 어떤 판단을 개선하는지 확인하세요. 방어 효과는 긴 교전에 갇히거나 다시 자리 잡을 공간을 잃거나 전투가 달라졌을 때 대응하지 못하는 실제 실패를 줄일 때 의미가 있습니다. 공격 효과는 예측할 수 있는 기회에 발동시킬 수 있어야 합니다. 자주 만들지 못하는 조건에 의존한다면 표시된 최대 효과가 실제 플레이에 도움을 주지 않을 수 있습니다.",
                "‘Mistfall Hunter 용병 검과 방패 빌드’라는 검색 문구만으로 클래스 명칭, 특성 순서, 장비 조합이 현재도 맞다고 판단하지 마세요. Similarweb은 해당 표현이 검색어 묶음에 있다는 점을 보여주지만 이번 가이드에서 확인한 공개 자료는 현행 구성을 검증하지 못했습니다. 화면에 표시된 이름, 비용, 조건을 기록한 다음 전체를 바꾸기 전에 한 부위만 시험하세요. 바꾸는 요소는 직접 관찰한 문제와 연결해야 합니다.",
            ], bullets=["방어 선택지는 직접 확인한 실패에 대응해야 합니다.", "공격 기술은 재현할 수 있는 발동 기회가 있어야 합니다.", "특성은 장비 조건을 보완하고 불필요하게 반복하지 않습니다."], links=[{"target": "classes", "label": "역할을 정하기 전에 클래스 비교하기"}]),
            _section("solo-play", "솔로 플레이에 맞춰 검과 방패 빌드 조정하기", [
                "솔로에서는 다음 목표만큼 돌아가는 길도 중요합니다. 방에 들어가기 전에 물러날 공간, 분명한 출구, 첫 교전 뒤 회복할 방법을 살펴보세요. 방패가 있으니 안전하겠다는 이유만으로 교전을 시작하지 마세요. 명확한 기회가 없으면 방을 우회하거나 기다릴 수 있습니다. 생존을 보장하진 않지만 정보가 없는 상태에서 위험한 결정을 반복하는 일을 줄여 줍니다.",
                "전투 뒤에는 상태, 회복 자원, 경로의 시야를 확인합니다. 남은 보상과 귀환 위험도 비교하세요. 솔로 빌드가 공격 선택지를 유지하더라도 파티원이 적을 유인하거나 후퇴를 지켜줄 것이라고 기대하면 안 됩니다. 적이 가만히 있거나 출구가 비어 있어야만 계획이 작동한다면 확정 사실이 아니라 확인할 조건으로 다루세요. 귀환을 어렵게 만드는 전투라면 보상을 더 쫓지 않는 판단도 필요합니다.",
            ], steps=["교전 전에 후퇴 경로와 다시 거리를 벌릴 지점을 찾습니다.", "현재 기회에 필요한 공격 또는 방어만 사용합니다.", "전투 후 상태, 회복 수단, 출구를 확인합니다.", "남은 보상보다 귀환 위험이 커지면 지역을 떠납니다."], image={"path": _EXTRACTION_IMAGE, "alt": "어두운 방의 빛나는 상자 근처에 선 Mistfall Hunter 캐릭터가 담긴 Steam 공식 이미지", "caption": "전리품을 가지고 탈출할지 결정하는 맥락을 보여주는 공식 이미지입니다. 특정 경로나 추천 장비를 나타내지는 않습니다.", "source_label": "Steam 공식 페이지 보기", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "gameplay-guide", "label": "솔로 진행과 탈출 흐름 다시 보기"}]),
            _section("trio-adjustment", "3인 파티에서 역할 조정하기", [
                "공간을 지키고 후퇴를 알리는 편이라면 3인 파티에서 검과 방패로 전열을 맡을 수 있습니다. 이는 팀 운영 제안이지 클래스 전용 효과가 확인됐다는 뜻은 아닙니다. 누가 후퇴를 부르고 누가 짧은 공격 기회를 활용하며 누가 정찰과 회복을 돕는지 정하세요. 용병 빌드 검색을 혼자 앞서 나가도 된다는 뜻으로 받아들이지 말고 파티가 기다릴 기회를 이해하고 있는지 확인하세요.",
                "다른 플레이어가 이미 전열이면 같은 기능을 겹치지 말고 통제된 공격이나 유연한 지원으로 조정합니다. 팀의 요청에 반응할 거리 안에 머무르세요. 누군가 떨어져 나갔다면 다음 전투 전에 모입니다. 모든 패치와 맵, 숙련도에서 하나의 조합이 최고라고 단정하기보다 팀이 실제로 수행할 역할과 합류 규칙부터 정하는 편이 유용합니다.",
            ], table={"headers": ["상황", "검과 방패 역할", "팀 조율"], "rows": [["낯선 방", "회복 가능한 위치 유지", "전진 전에 한쪽을 정찰"], ["분명한 기회", "짧은 공격에 집중", "목표를 알리고 기회가 끝나면 중단"], ["팀원 고립", "다시 모일 경로 확보", "전원 합류 전까지 전진 멈춤"], ["출구 불명확", "피해를 위해 후퇴 포기 금지", "추가 전투 전 재정비 또는 이탈"]]}, links=[{"target": "trio-builds-guide", "label": "3인 파티 역할과 대안을 비교하기"}]),
            _section("repeatable-test", "빌드를 조정하는 짧은 반복 테스트", [
                "클래스, 기술, 장비, 경로, 위험도를 한꺼번에 바꾸면 무엇이 결과를 개선했는지 알 수 없습니다. 대부분의 조건은 고정해 두세요. 출발 전 한 가지 질문을 적습니다. 방어 수단으로 재배치할 수 있었나? 공격 기회를 반복할 수 있었나? 첫 전투 뒤에도 탈출로가 열려 있었나? 이 기록은 다음 시도 방향을 정하지만 통제된 피해량 테스트를 대신하지 않습니다.",
                "플레이 후에는 가장 큰 비용을 치른 판단, 남겨두고 싶었던 자원, 실패 원인이 전투·이동 경로·파티 분리 중 무엇이었는지 기록하세요. 다음 시도에서는 관련 요소 한 가지만 바꿉니다. 여러 항목을 바꿨다면 별개의 실험으로 남기고 특정 아이템 덕분이라고 결론내리지 마세요. 테스트한 시스템이 바뀌면 업데이트 노트와 설명을 다시 확인해야 합니다.",
            ], steps=["첫 비교에서는 클래스, 무기, 경로 판단, 위험도를 고정합니다.", "장비 효과·기술·사용 시점 중 질문 하나를 선택합니다.", "목표, 실패한 판단, 회복, 탈출 결과를 기록합니다.", "개선이라고 부르기 전에 같은 질문을 다시 확인합니다.", "대상 시스템이 바뀌면 최신 업데이트 정보를 읽습니다."], links=[{"target": "beginner-guide", "label": "위험이 낮은 다섯 번의 학습 계획 사용하기"}]),
            _section("mistakes-and-limits", "자주 하는 실수와 이 가이드의 한계", [
                "첫 번째 실수는 방어를 안전 자체로 여기는 것입니다. 방어 행동에도 조건, 비용, 지속 시간이 있을 수 있으니 긴 교전을 시작하기 전에 작동 방식을 확인하세요. 두 번째는 다른 가이드가 최선이라고 쓴 공격 효과를 무작정 쌓는 것입니다. 언제 도움이 되는지 설명할 수 없다면 우선순위에 넣기 전에 시험하세요. 세 번째는 날짜와 테스트 조건이 없는 목록을 현행 순위로 받아들이는 것입니다.",
                "매번 많은 요소를 바꾸는 것도 문제입니다. 경로나 파티원이 바뀌어 아이템이 더 강해진 듯 느낄 수 있습니다. 시도 기록을 남기고 한 번의 성공을 일반 규칙으로 만들지 마세요. 공개 정보는 탈출, 장비, 솔로와 팀 플레이를 설명하지만 검증된 검과 방패 피해 공식이나 계속 유효한 장비 순위를 제공하지 않습니다. 이 기준을 출발점으로 삼고 반복 가능한 관찰에 맞춰 업데이트하세요.",
            ]),
        ],
        "faq_title": "Mistfall Hunter 검과 방패 빌드 FAQ",
        "faq": [{"question": "Mistfall Hunter에서 가장 좋은 검과 방패 빌드는 무엇인가요?", "answer": "검토한 자료만으로 항상 최선인 구성을 확인할 수는 없습니다. 이해하기 쉬운 방어, 반복 가능한 공격 기회, 회복 수단부터 시작하세요. 날짜가 없는 메타 목록을 따르기 전에 현재 장비와 패치를 확인하세요."}, {"question": "용병 검과 방패 빌드는 솔로에 적합한가요?", "answer": "현재 클래스와 장비에서 조합할 수 있다면 역할을 정하는 출발점이 될 수 있습니다. Similarweb 검색어만으로 현행 빌드가 검증되지는 않습니다. 솔로에서는 돌아갈 길과 파티원에 의존하지 않는 회복 방법을 남기세요."}, {"question": "검과 방패 빌드에서 어떤 능력치를 우선해야 하나요?", "answer": "현재 게임에 표시된 능력치 이름과 효과를 기준으로 하세요. 실제 실패를 먼저 보완한 다음 예측 가능한 기회에서 쓰는 공격 효과를 선택합니다. 이 글은 확인되지 않은 이름, 기준치, 수치를 만들지 않습니다."}, {"question": "검과 방패 빌드를 3인 파티에서도 쓸 수 있나요?", "answer": "누가 후퇴를 알리고 나머지 역할을 누가 맡을지 정했다면 전열 또는 통제된 공격 역할로 쓸 수 있습니다. 다른 팀원이 전열이면 역할을 조정하고 현재 패치에서 조합을 시험하세요."}, {"question": "Mistfall Hunter 빌드 코드를 그대로 복사해야 하나요?", "answer": "출처, 패치, 클래스, 장비 조건을 알 때만 참고용으로 사용하세요. 현재 버전과 비교하고 한 번에 항목 하나만 바꿔야 영향을 파악할 수 있습니다."}],
        "summary_heading": "핵심 요약",
        "summary": "Mistfall Hunter 검과 방패 빌드는 역할에 기반해 시험하세요. 후퇴 경로를 남기고 짧은 공격 기회를 활용하며 솔로에서는 귀환 경로를, 3인 파티에서는 역할 분담을 우선합니다. 아이템 수치는 패치에 따라 달라지며 여기서 검증되지 않았으니 최선이라고 부르기 전에 게임에서 확인하세요.",
        "related_title": "다음 출전을 준비하세요",
        "related_links": [{"target": "builds", "label": "Mistfall Hunter 일반 빌드 비교"}, {"target": "classes", "label": "클래스별 역할 확인"}, {"target": "gameplay-guide", "label": "게임 진행과 탈출 이해"}, {"target": "trio-builds-guide", "label": "3인 파티 구성 계획"}, {"target": "beginner-guide", "label": "낮은 위험의 연습부터 시작"}],
        "source_title": "공식 출처와 확인 범위",
        "source_note": "공식 사이트와 Steam 페이지는 게임 및 장비에 관한 배경을 제공합니다. Steam 공식 스크린샷은 일반적인 상황 설명에만 사용했습니다. 현재 검과 방패 수치, 기술 순환, 장비 순위, 최적 빌드는 확인하지 못했으므로 본문은 게임 안에서 시험할 역할별 판단을 다룹니다.",
        "official_links": [{"label": "Mistfall Hunter 공식 사이트", "url": _OFFICIAL_URL, "rel": "noopener"}, {"label": "Steam 공식 페이지와 이미지", "url": _STEAM_URL, "rel": "noopener"}],
    },
    "it": {
        "slug": "mistfall-hunter-sword-and-shield-build",
        "primary_keyword": "build spada e scudo Mistfall Hunter",
        "related_keywords": ["build mercenario Mistfall Hunter spada e scudo", "miglior build spada e scudo Mistfall Hunter", "build spada e scudo Mistfall Hunter in solitaria", "build spada e scudo Mistfall Hunter trio"],
        "title": "Build spada e scudo per Mistfall Hunter: 5 priorità per solo e trio",
        "meta_title": "Build spada e scudo Mistfall Hunter: 5 priorità",
        "meta_description": "Pianifica una build spada e scudo per Mistfall Hunter con priorità per equipaggiamento e abilità, modifiche per solo e trio e un metodo di prova senza statistiche inventate.",
        "meta_keywords": "build spada e scudo Mistfall Hunter, build mercenario Mistfall Hunter, build spada e scudo solo, build spada e scudo trio",
        "eyebrow": "Guida alle build con armi di Mistfall Hunter",
        "lede": "Spada e scudo si adattano a un approccio che lascia il tempo di leggere lo scontro, prendere impegni brevi e mantenere una via d'uscita. Organizza l'equipaggiamento intorno a decisioni ripetibili, non a una classifica dei danni non verificata: prevedi una risposta difensiva, un'apertura d'attacco affidabile e un modo per ristabilire la distanza. Le indicazioni generali sono distinte dai valori legati alla versione, che vanno verificati nel gioco attuale.",
        "checked_label": "Schema di build basato sui ruoli verificato il 24 ottobre 2026; nessun valore esatto degli oggetti dichiarato",
        "entry_label": "Leggi la guida alla build spada e scudo di Mistfall Hunter",
        "checked_iso": "2026-10-24",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "Illustrazione concettuale editoriale di un cacciatore con spada e scudo e la breve scritta Sword + Shield", "caption": "Illustrazione concettuale originale realizzata per questa guida; non è un'immagine ufficiale di Mistfall Hunter né uno screenshot di gioco.", "source_label": "Informazioni su questa guida indipendente", "source_url": "/it/about/", "width": 1024, "height": 1024},
        "facts_headers": ["Decisione di build", "Partenza prudente", "Quando adattarla"],
        "facts_rows": [["Ruolo", "Controllare lo spazio e tenere una via di ripiego", "Un compagno copre già il ruolo di ancora"], ["Danni", "Usare aperture brevi e ripetibili", "Una patch o prova verificata cambia i tempi"], ["Equipaggiamento", "Tenere una risposta difensiva e una di pressione", "Le descrizioni attuali indicano uno scambio migliore"], ["Solo", "Raccogliere bottino se l'uscita resta leggibile", "Percorso o recupero diventano incerti"], ["Trio", "Dividere ancora, pressione e flessibilità", "Un compagno è isolato o i ruoli si sovrappongono"]],
        "intro": "Per una build spada e scudo di Mistfall Hunter, parti da un ruolo stabile invece di inseguire una lista di equipaggiamento dichiarata migliore. Mantieni margine per recuperare da uno scambio sfavorevole, usa i danni durante un'apertura chiara e decidi come uscire prima di impegnarti. Le informazioni pubbliche confermano il ciclo generale di estrazione e l'attenzione all'equipaggiamento, ma non una combinazione permanente di nomi, statistiche o gradi dei talenti. Considera le priorità come ipotesi da testare e verifica i valori nella versione attuale.",
        "sections": [
            _section("build-goal", "Quale problema deve risolvere questa build spada e scudo", ["La domanda utile non è se uno scudo sia sempre migliore di un'altra arma. Chiediti se la combinazione ti permette di scegliere uno scambio, sostenerne il costo e tornare su un percorso sicuro. Il combattimento ravvicinato invita a prolungare gli scontri: usa lo scudo per controllare quando ingaggiare, non come prova che ogni colpo possa essere bloccato. Comandi, regole difensive e costi di recupero possono cambiare; consulta le descrizioni correnti e verifica in partita.", "Questa guida propone uno schema basato sui ruoli. È adatto a chi preferisce uno scontro controllato, vuole imparare una battaglia o ha bisogno di un incarico chiaro in una squadra piccola. Non sostiene che spada e scudo offrano i danni più alti, siano l'unica scelta valida o costituiscano una build meta ufficiale. Se la versione usa altri nomi per classi o oggetti, conserva i criteri e sostituisci i termini con quelli visibili nel tuo equipaggiamento."], bullets=["Tieni un'opzione di recupero o disimpegno prima di ingaggiare.", "Scegli una finestra offensiva riconoscibile senza un calcolo dei danni.", "Modifica un solo oggetto o abilità alla volta per imparare dalla partita successiva."], image={"path": _COMBAT_IMAGE, "alt": "Screenshot ufficiale Steam con un personaggio di Mistfall Hunter davanti a una grande creatura nella foresta", "caption": "Immagine ufficiale Steam per il contesto generale su distanza e scontri; non mostra una build testata né valori di danno.", "source_label": "Apri la pagina ufficiale su Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("five-build-priorities", "Cinque priorità per una build spada e scudo più sicura", ["Le priorità descrivono cosa deve permetterti di fare la build, non nomi fissi di statistiche o formule nascoste. Apri le descrizioni aggiornate di equipaggiamento e abilità e scegli le opzioni visibili in base alla funzione. Se due bonus sembrano utili, preferisci quello che puoi provare più volte invece del valore che appare più alto fuori contesto. Così confronti decisioni reali, non numeri isolati.", "Il primo tentativo dovrebbe restare semplice: una risposta per la sopravvivenza, un'azione offensiva ripetibile e abbastanza flessibilità da lasciare una stanza sfavorevole. Dopo alcune partite, individua dove il piano ha smesso di funzionare. Se eri al sicuro ma troppo lento, regola la pressione. Se hai inflitto danni ma perso la via d'uscita, migliora prima il recupero o il momento di decidere."], table={"headers": ["Priorità", "Cerca", "Evita"], "rows": [["1. Difesa leggibile", "Condizioni e costo noti", "Presumere che lo scudo blocchi ogni danno"], ["2. Pressione ripetibile", "Finestra breve che puoi creare", "Inseguire oltre il percorso sicuro"], ["3. Recupero", "Modo chiaro per ristabilire spazio", "Spendere tutte le difese al primo contatto"], ["4. Equipaggiamento utile", "Bonus per un problema osservato", "Copiare priorità senza leggere le descrizioni"], ["5. Valore per la squadra", "Compito che integra gli altri ruoli", "Tre giocatori con lo stesso compito"]]}, links=[{"target": "builds", "label": "Confrontare questa configurazione con i modelli generali del sito"}]),
            _section("gear-skills", "Scegliere equipaggiamento, abilità e talenti in base alla funzione", ["Leggi la descrizione di ogni oggetto o talento nella versione attuale e chiediti quale decisione migliori. Un effetto difensivo serve solo se cambia un problema reale: restare bloccato in uno scambio lungo, perdere spazio per riposizionarti o non avere una risposta quando l'incontro cambia. Un effetto offensivo è utile quando puoi attivarlo durante un'apertura prevedibile. Se dipende da una condizione rara, il suo valore nominale potrebbe non aiutare la tua partita.", "Non trattare la ricerca “build mercenario spada e scudo Mistfall Hunter” come prova che un nome di classe, un ordine di talenti o un set siano attuali. Similarweb indica che la frase compare nel gruppo di query; le fonti pubbliche esaminate non verificano una build corrente. Annota nomi, costi e condizioni visibili, poi prova un singolo pezzo prima di ricostruire tutto l'equipaggiamento. Cambia una scelta per risolvere un problema che hai osservato."], bullets=["La difesa risponde a un errore che hai osservato.", "L'abilità offensiva ha una finestra che riesci a ripetere.", "I talenti completano le condizioni dell'equipaggiamento."], links=[{"target": "classes", "label": "Confrontare i ruoli di classe prima di specializzarti"}]),
            _section("solo-play", "Adattare la build alle partite in solitaria", ["In solitaria, il percorso di ritorno conta quanto il prossimo bersaglio. Prima di entrare in una stanza, individua dove arretrare, l'uscita più chiara e l'opzione per recuperare dopo il primo scambio. Non iniziare solo perché lo scudo sembra rassicurante. Se non c'è un'apertura netta, aggira la stanza o aspetta. Non è una garanzia di sopravvivenza, ma riduce le decisioni rischiose prese senza informazioni.", "Dopo uno scontro, controlla lo stato, le risorse di recupero e la leggibilità della via. Confronta il bottino rimanente con il rischio del ritorno. Una build solo può mantenere un'opzione offensiva, ma non dovrebbe dipendere da un compagno che attira il nemico o copre la ritirata. Se il piano funziona soltanto con un avversario fermo o un'uscita libera, trattalo come requisito da verificare, non come certezza."], steps=["Prima di ingaggiare, individua il ripiego e uno spazio per recuperare distanza.", "Usa soltanto l'attacco o la difesa utili all'apertura presente.", "Dopo lo scontro, controlla stato, recupero e percorso.", "Lascia la zona quando il bottino non giustifica il rischio del ritorno."], image={"path": _EXTRACTION_IMAGE, "alt": "Screenshot ufficiale Steam di Mistfall Hunter con un personaggio vicino a un forziere illuminato in una stanza buia", "caption": "Immagine ufficiale Steam sul contesto della decisione di estrarre con il bottino; non mostra un percorso o equipaggiamento consigliato.", "source_label": "Apri la pagina ufficiale su Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "gameplay-guide", "label": "Rivedere il ciclo di gioco e di estrazione in solo"}]),
            _section("trio-adjustment", "Adattare il ruolo nel trio", ["Nel trio, spada e scudo possono fare da ancora se sai conservare spazio e chiamare la ritirata. È una proposta di coordinamento, non la conferma di un effetto esclusivo di classe. Decidete chi annuncia il ripiego, chi sfrutta una breve apertura e chi esplora o supporta il recupero. La ricerca di una build mercenario non significa procedere da soli: la squadra deve sapere quale occasione aspetti.", "Se un altro giocatore è già l'ancora, evita di sovrapporre lo stesso compito. Sposta la build verso una pressione controllata o un supporto flessibile e resta vicino per reagire alle chiamate. Se qualcuno è isolato, riunitevi prima del prossimo scontro. Questi principi sono più utili dell'affermazione che una composizione sia la migliore su ogni mappa, patch o livello di abilità."], table={"headers": ["Situazione", "Ruolo spada e scudo", "Coordinamento"], "rows": [["Stanza sconosciuta", "Posizione da cui recuperare", "Esplorare un lato prima di avanzare"], ["Apertura chiara", "Concentrare un attacco breve", "Chiamare il bersaglio e fermarsi dopo"], ["Compagno isolato", "Proteggere la via per ritrovarsi", "Fermare l'avanzata fino al ricongiungimento"], ["Uscita incerta", "Non scambiare la ritirata con danni", "Riunirsi o uscire prima di un altro scontro"]]}, links=[{"target": "trio-builds-guide", "label": "Distribuire i ruoli e preparare alternative per il trio"}]),
            _section("repeatable-test", "Un breve piano di prova per regolare la build", ["Cambiare classe, abilità, equipaggiamento, percorso e rischio insieme non mostra cosa abbia migliorato il risultato. Mantieni costanti la maggior parte delle condizioni. Prima della partita annota una domanda: la difesa mi ha permesso di riposizionarmi? Ho ripetuto la finestra offensiva? L'uscita era accessibile dopo il primo scontro? L'osservazione indirizza la prova successiva, ma non sostituisce un test dei danni controllato.", "Dopo la partita, registra la decisione più costosa, la risorsa che avresti voluto tenere e la causa principale del fallimento: scontro, percorso o separazione. Cambia un solo fattore pertinente nel tentativo successivo. Se ne cambi diversi, trattali come esperimento separato e non attribuire il risultato a un solo oggetto. Rileggi le note di aggiornamento se il sistema che stai provando cambia."], steps=["Nel primo confronto mantieni classe, arma, percorso e rischio.", "Scegli una domanda su oggetto, abilità o momento d'uso.", "Registra obiettivo, errore, recupero e risultato dell'estrazione.", "Ripeti la domanda prima di definire il cambiamento un miglioramento.", "Controlla le note della patch se il sistema è cambiato."], links=[{"target": "beginner-guide", "label": "Seguire il piano di apprendimento a basso rischio in cinque partite"}]),
            _section("mistakes-and-limits", "Errori comuni e limiti di questa guida", ["Non considerare la difesa una garanzia di sicurezza. Un'azione può avere condizioni, costi o durata limitata; verifica come funziona prima di iniziare uno scambio lungo. Non accumulare effetti offensivi solo perché una guida li definisce ottimali: se non sai quando sarebbero utili, provali prima. Una lista senza data e condizioni di prova non è una classifica attuale.", "Cambiare troppe cose a ogni partita confonde i risultati. Un percorso o un compagno diverso può far sembrare più forte l'equipaggiamento senza che l'oggetto sia cambiato. Registra i tentativi e non generalizzare un singolo successo. Le fonti pubbliche descrivono estrazione, equipaggiamento e partite solo o in squadra, ma non una formula dei danni spada e scudo verificata né una classifica permanente. Parti da queste decisioni e aggiornatele con osservazioni ripetibili."]),
        ],
        "faq_title": "FAQ sulla build spada e scudo di Mistfall Hunter",
        "faq": [{"question": "Qual è la migliore build spada e scudo in Mistfall Hunter?", "answer": "Le fonti esaminate non confermano una configurazione sempre migliore. Parti da una difesa comprensibile, un'apertura offensiva ripetibile e un'opzione di recupero. Verifica equipaggiamento e patch prima di seguire una lista meta senza data."}, {"question": "La build mercenario spada e scudo è adatta al solo?", "answer": "Se classe ed equipaggiamento correnti permettono la combinazione, può essere un punto di partenza con ruolo chiaro. Una query Similarweb non verifica una build attuale. In solo mantieni la via di ritorno e un recupero indipendente dalla squadra."}, {"question": "Quali statistiche dare priorità nella build spada e scudo?", "answer": "Usa nomi ed effetti mostrati nel gioco corrente. Correggi prima un problema osservato, poi scegli un effetto utile in un'apertura prevedibile. Questa guida non inventa nomi, soglie o valori."}, {"question": "La build spada e scudo può funzionare nel trio?", "answer": "Può coprire l'ancora o una pressione controllata se la squadra decide chi chiama la ritirata e chi svolge gli altri compiti. Se un compagno è già l'ancora, adatta il ruolo e prova la composizione nella patch corrente."}, {"question": "Dovrei copiare un codice build senza modificarlo?", "answer": "Usalo come punto di partenza solo se fonte, patch, classe e condizioni dell'equipaggiamento sono note. Confrontalo con la tua versione e modifica un elemento alla volta per capire l'effetto."}],
        "summary_heading": "In breve",
        "summary": "Considera la build spada e scudo di Mistfall Hunter un esperimento basato sul ruolo. Mantieni una via d'uscita, usa aperture brevi, proteggi il rientro in solo e distribuisci i compiti nel trio. I valori degli oggetti dipendono dalla patch e qui non sono verificati; controllali in gioco prima di definire ottimale un equipaggiamento.",
        "related_title": "Preparati alla prossima partita",
        "related_links": [{"target": "builds", "label": "Confrontare le build generali di Mistfall Hunter"}, {"target": "classes", "label": "Esaminare i ruoli delle classi"}, {"target": "gameplay-guide", "label": "Capire gameplay ed estrazione"}, {"target": "trio-builds-guide", "label": "Pianificare il trio"}, {"target": "beginner-guide", "label": "Iniziare con prove a basso rischio"}],
        "source_title": "Fonti ufficiali e limiti delle prove",
        "source_note": "Il sito ufficiale e la scheda Steam forniscono il contesto del gioco e dell'equipaggiamento. Gli screenshot Steam ufficiali illustrano soltanto questo contesto. Non è stato possibile verificare i valori attuali di spada e scudo, le rotazioni, le classifiche o una build ottimale; il testo presenta quindi scelte basate sul ruolo da provare nel gioco.",
        "official_links": [{"label": "Sito ufficiale di Mistfall Hunter", "url": _OFFICIAL_URL, "rel": "noopener"}, {"label": "Scheda e immagini ufficiali Steam", "url": _STEAM_URL, "rel": "noopener"}],
    },
}
