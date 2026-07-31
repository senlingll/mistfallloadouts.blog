from __future__ import annotations

from datetime import date
from typing import Any, Dict, List

from flask import Flask, abort, render_template


app = Flask(__name__)

BASE_URL = "https://mistfallloadouts.blog"
SUPPORTED_LANGUAGES = ["en", "es", "ja", "fr", "de", "pt", "ko", "it"]
DEFAULT_LANGUAGE = "en"
LAST_UPDATED = date(2026, 7, 31).isoformat()


LOCALE_LABELS = {
    "en": "English",
    "es": "Español",
    "ja": "日本語",
    "fr": "Français",
    "de": "Deutsch",
    "pt": "Português",
    "ko": "한국어",
    "it": "Italiano",
}


LOCALE_MARKETS = {
    "en": "United States",
    "es": "Mexico and Spanish-speaking players",
    "ja": "Japan",
    "fr": "France",
    "de": "Germany",
    "pt": "Brazil",
    "ko": "South Korea",
    "it": "Italy",
}


TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "en": {
        "title": "Mistfall Hunter Loadouts Planner",
        "meta_title": "Mistfall Hunter Loadouts Planner & Builds",
        "meta_description": "Plan Mistfall Hunter loadouts by class, role, risk, and weapon preference with clear assumptions for launch-week builds.",
        "meta_keywords": "mistfall hunter loadouts, mistfall hunter builds, mistfall hunter classes",
        "nav_tool": "Planner",
        "nav_classes": "Classes",
        "nav_builds": "Builds",
        "nav_guide": "Guide",
        "nav_faq": "FAQ",
        "hero_eyebrow": "Launch-week build planning",
        "hero_title": "Mistfall Hunter loadouts for classes, risk, and extraction goals",
        "hero_lede": "Choose your role, weapon style, and risk level to get a practical Mistfall Hunter loadout direction before you lock in a run.",
        "hero_note": "The planner uses transparent launch-week assumptions from public Steam, official, and guide-page research. It does not claim hidden damage values.",
        "tool_title": "Loadout Planner",
        "tool_intro": "Tune the inputs and read the recommendation card. The result favors playstyle fit, survivability, and team value instead of pretending exact private stats are known.",
        "class_label": "Class focus",
        "role_label": "Run role",
        "risk_label": "Risk level",
        "weapon_label": "Weapon style",
        "phase_label": "Progress",
        "class_vanguard": "Vanguard",
        "class_seeker": "Seeker",
        "class_arcanist": "Arcanist",
        "class_warden": "Warden",
        "role_solo": "Solo extraction",
        "role_team": "Team support",
        "role_boss": "Boss pressure",
        "risk_safe": "Safe",
        "risk_balanced": "Balanced",
        "risk_greedy": "Greedy",
        "weapon_melee": "Melee",
        "weapon_ranged": "Ranged",
        "weapon_hybrid": "Hybrid",
        "phase_early": "Early game",
        "phase_mid": "Mid game",
        "phase_late": "Late game",
        "result_title": "Recommended loadout direction",
        "result_tags": "Priority tags",
        "result_stats": "Stat priorities",
        "result_route": "Extraction route",
        "result_tip": "Run tip",
        "reset": "Reset",
        "copy": "Copy",
        "copied": "Copied",
        "classes_title": "Mistfall Hunter classes at a glance",
        "classes_intro": "Use the class table to decide whether your Mistfall Hunter loadout should protect the run, scout safely, burst targets, or keep the party stable.",
        "builds_title": "Build patterns that avoid common launch-week mistakes",
        "builds_intro": "Most early Mistfall Hunter builds fail because they stack damage without solving escape timing, role overlap, or resource pressure.",
        "guide_title": "How to use the planner before a run",
        "guide_intro": "The planner works best as a decision checklist. Pick the closest style, read the tradeoffs, then adjust once official patch notes or reliable community tests settle exact values.",
        "data_title": "Data and freshness note",
        "data_text": "This site was created for the July 31, 2026 search window. Google Trends showed active US demand for Mistfall Hunter, while Similarweb reported strong 28-day demand for the main term and class queries. Build advice is intentionally framed as guidance until exact game values are verified.",
        "faq_title": "Mistfall Hunter loadouts FAQ",
        "about_title": "About Mistfall Loadouts",
        "about_text": "Mistfall Loadouts is an independent planning site for Mistfall Hunter players. It focuses on build decisions, class comparisons, route planning, and transparent assumptions for launch-week play.",
        "privacy_title": "Privacy Policy",
        "terms_title": "Terms of Service",
        "contact_title": "Contact Mistfall Loadouts",
        "contact_text": "Send corrections, source updates, accessibility issues, or policy questions to hello@mistfallloadouts.blog. Please include the page URL and the Mistfall Hunter topic you want reviewed so updates can be checked against public evidence.",
        "legal_text": "This independent fan resource does not collect account logins, sell user data, or claim affiliation with the official game publisher.",
        "footer_disclaimer": "Independent fan-made planner. Mistfall Hunter names belong to their respective owners.",
    },
    "es": {
        "title": "Planificador de loadouts de Mistfall Hunter",
        "meta_title": "Loadouts y builds de Mistfall Hunter",
        "meta_description": "Planifica loadouts de Mistfall Hunter por clase, rol, riesgo y arma con supuestos claros de la semana de lanzamiento.",
        "meta_keywords": "loadouts Mistfall Hunter, builds Mistfall Hunter, clases Mistfall Hunter",
        "nav_tool": "Planificador",
        "nav_classes": "Clases",
        "nav_builds": "Builds",
        "nav_guide": "Guía",
        "nav_faq": "FAQ",
        "hero_eyebrow": "Planificación de lanzamiento",
        "hero_title": "Loadouts de Mistfall Hunter para clases, riesgo y extracción",
        "hero_lede": "Elige rol, arma y nivel de riesgo para obtener una dirección práctica de loadout antes de entrar a una partida.",
        "hero_note": "El planificador usa supuestos públicos de lanzamiento. No afirma conocer valores ocultos de daño.",
        "tool_title": "Planificador de loadout",
        "tool_intro": "Ajusta los campos y revisa la recomendación. El resultado prioriza estilo, supervivencia y valor para el equipo.",
        "class_label": "Clase",
        "role_label": "Rol",
        "risk_label": "Riesgo",
        "weapon_label": "Arma",
        "phase_label": "Progreso",
        "class_vanguard": "Vanguardia",
        "class_seeker": "Explorador",
        "class_arcanist": "Arcanista",
        "class_warden": "Guardián",
        "role_solo": "Extracción solo",
        "role_team": "Apoyo de equipo",
        "role_boss": "Presión a jefes",
        "risk_safe": "Seguro",
        "risk_balanced": "Equilibrado",
        "risk_greedy": "Agresivo",
        "weapon_melee": "Cuerpo a cuerpo",
        "weapon_ranged": "A distancia",
        "weapon_hybrid": "Híbrido",
        "phase_early": "Inicio",
        "phase_mid": "Mitad",
        "phase_late": "Avanzado",
        "result_title": "Dirección recomendada",
        "result_tags": "Prioridades",
        "result_stats": "Estadísticas clave",
        "result_route": "Ruta de extracción",
        "result_tip": "Consejo",
        "reset": "Restablecer",
        "copy": "Copiar",
        "copied": "Copiado",
        "classes_title": "Clases de Mistfall Hunter",
        "classes_intro": "Usa la tabla para decidir si tu loadout debe proteger, explorar, hacer daño explosivo o estabilizar al grupo.",
        "builds_title": "Patrones de builds que evitan errores comunes",
        "builds_intro": "Muchas builds iniciales fallan por acumular daño sin resolver escape, rol o presión de recursos.",
        "guide_title": "Cómo usar el planificador",
        "guide_intro": "Funciona como lista de decisión. Elige el estilo más cercano y ajusta cuando haya datos oficiales o pruebas fiables.",
        "data_title": "Datos y vigencia",
        "data_text": "Sitio creado para la ventana de búsqueda del 31 de julio de 2026, con demanda activa en Google Trends y volumen reciente en Similarweb.",
        "faq_title": "FAQ de loadouts de Mistfall Hunter",
        "about_title": "Sobre Mistfall Loadouts",
        "about_text": "Mistfall Loadouts es un sitio independiente para planificar builds, comparar clases y preparar rutas.",
        "privacy_title": "Política de privacidad",
        "terms_title": "Términos de servicio",
        "contact_title": "Contacto de Mistfall Loadouts",
        "contact_text": "Envía correcciones, actualizaciones de fuentes, problemas de accesibilidad o preguntas de política a hello@mistfallloadouts.blog. Incluye la URL de la página y el tema de Mistfall Hunter que quieres revisar.",
        "legal_text": "Este recurso independiente no recopila inicios de sesión, no vende datos y no afirma afiliación oficial.",
        "footer_disclaimer": "Planificador independiente creado por fans.",
    },
    "ja": {
        "title": "Mistfall Hunter ロードアウトプランナー",
        "meta_title": "Mistfall Hunter ロードアウトとビルド",
        "meta_description": "クラス、役割、リスク、武器傾向から Mistfall Hunter のロードアウト方針を整理します。",
        "meta_keywords": "Mistfall Hunter ロードアウト, Mistfall Hunter ビルド, Mistfall Hunter クラス",
        "nav_tool": "プランナー",
        "nav_classes": "クラス",
        "nav_builds": "ビルド",
        "nav_guide": "ガイド",
        "nav_faq": "FAQ",
        "hero_eyebrow": "ローンチ週のビルド整理",
        "hero_title": "クラス、リスク、脱出目的で選ぶ Mistfall Hunter ロードアウト",
        "hero_lede": "役割、武器傾向、リスクを選び、出撃前に実用的なロードアウト方針を確認できます。",
        "hero_note": "公開情報にもとづく仮説型プランナーです。未公開のダメージ値を断定しません。",
        "tool_title": "ロードアウトプランナー",
        "tool_intro": "入力を調整し、推奨カードを確認してください。正確な隠し数値よりも、生存性と役割適合を重視します。",
        "class_label": "クラス",
        "role_label": "役割",
        "risk_label": "リスク",
        "weapon_label": "武器",
        "phase_label": "進行度",
        "class_vanguard": "ヴァンガード",
        "class_seeker": "シーカー",
        "class_arcanist": "アルカニスト",
        "class_warden": "ウォーデン",
        "role_solo": "ソロ脱出",
        "role_team": "チーム支援",
        "role_boss": "ボス火力",
        "risk_safe": "安全",
        "risk_balanced": "バランス",
        "risk_greedy": "攻め重視",
        "weapon_melee": "近接",
        "weapon_ranged": "遠距離",
        "weapon_hybrid": "ハイブリッド",
        "phase_early": "序盤",
        "phase_mid": "中盤",
        "phase_late": "終盤",
        "result_title": "推奨ロードアウト方針",
        "result_tags": "優先タグ",
        "result_stats": "優先ステータス",
        "result_route": "脱出ルート",
        "result_tip": "実戦メモ",
        "reset": "リセット",
        "copy": "コピー",
        "copied": "コピー済み",
        "classes_title": "Mistfall Hunter クラス早見表",
        "classes_intro": "守り、索敵、瞬間火力、安定支援のどれを重視するかでロードアウト方針が変わります。",
        "builds_title": "ローンチ週に避けたいビルドの失敗",
        "builds_intro": "火力だけを積むと、脱出タイミング、役割重複、資源管理で失敗しやすくなります。",
        "guide_title": "出撃前の使い方",
        "guide_intro": "まず近いプレイスタイルを選び、公式更新や検証データが出たら細部を調整します。",
        "data_title": "データと更新性",
        "data_text": "2026年7月31日の検索状況をもとに作成。Google Trends と Similarweb の需要を確認しています。",
        "faq_title": "Mistfall Hunter ロードアウト FAQ",
        "about_title": "Mistfall Loadouts について",
        "about_text": "Mistfall Hunter のビルド判断、クラス比較、ルート準備を支援する独立ファンサイトです。",
        "privacy_title": "プライバシーポリシー",
        "terms_title": "利用規約",
        "contact_title": "Mistfall Loadouts への連絡",
        "contact_text": "修正、情報更新、アクセシビリティ、ポリシーに関する質問は hello@mistfallloadouts.blog までお送りください。確認したいページ URL と Mistfall Hunter の話題を含めてください。",
        "legal_text": "本サイトはログイン情報を収集せず、公式運営との提携を主張しません。",
        "footer_disclaimer": "ファン制作の独立プランナーです。",
    },
}

for locale in ["fr", "de", "pt", "ko", "it"]:
    TRANSLATIONS[locale] = TRANSLATIONS["en"] | {
        "title": {
            "fr": "Planificateur de loadouts Mistfall Hunter",
            "de": "Mistfall Hunter Loadout Planer",
            "pt": "Planejador de loadouts de Mistfall Hunter",
            "ko": "Mistfall Hunter 로드아웃 플래너",
            "it": "Pianificatore loadout Mistfall Hunter",
        }[locale],
        "meta_title": {
            "fr": "Loadouts et builds Mistfall Hunter",
            "de": "Mistfall Hunter Loadouts und Builds",
            "pt": "Loadouts e builds de Mistfall Hunter",
            "ko": "Mistfall Hunter 로드아웃과 빌드",
            "it": "Loadout e build di Mistfall Hunter",
        }[locale],
        "hero_title": {
            "fr": "Loadouts Mistfall Hunter pour classes, risque et extraction",
            "de": "Mistfall Hunter Loadouts für Klassen, Risiko und Extraktion",
            "pt": "Loadouts de Mistfall Hunter para classes, risco e extração",
            "ko": "클래스, 위험도, 탈출 목표별 Mistfall Hunter 로드아웃",
            "it": "Loadout Mistfall Hunter per classi, rischio ed estrazione",
        }[locale],
        "footer_disclaimer": {
            "fr": "Planificateur indépendant créé par des fans.",
            "de": "Unabhängiger, von Fans erstellter Planer.",
            "pt": "Planejador independente feito por fãs.",
            "ko": "팬이 만든 독립 플래너입니다.",
            "it": "Planner indipendente creato dai fan.",
        }[locale],
    }


CLASS_ROWS = [
    {"key": "vanguard", "fit": "Frontline control", "strength": "Safer trades and room entry", "watch": "Can overcommit when greedy"},
    {"key": "seeker", "fit": "Scouting and mobility", "strength": "Information, repositioning, extraction timing", "watch": "Needs discipline in boss fights"},
    {"key": "arcanist", "fit": "Burst windows", "strength": "High pressure when cooldowns align", "watch": "Punished by messy escapes"},
    {"key": "warden", "fit": "Team stability", "strength": "Keeps runs recoverable", "watch": "Lower solo tempo"},
]


BUILD_PATTERNS = [
    {"name": "Safe Extractor", "best": "Solo, early game, cautious players", "priorities": "Mobility, sustain, escape utility", "mistake": "Skipping exit tools for damage"},
    {"name": "Balanced Raider", "best": "Most mixed groups", "priorities": "Reliable weapon, one defensive layer, flexible utility", "mistake": "Duplicating the same team role"},
    {"name": "Boss Breaker", "best": "Planned boss pressure", "priorities": "Burst window, uptime, recovery option", "mistake": "Entering without a reset route"},
    {"name": "Scout Caller", "best": "Teams that need information", "priorities": "Vision, mobility, low-noise disengage", "mistake": "Fighting every contact"},
]


FAQ_ITEMS = [
    ("What is the best Mistfall Hunter loadout?", "The safest answer depends on class, team role, and risk level. Start with Balanced Raider, then shift toward Boss Breaker or Safe Extractor when your run goal changes."),
    ("Does this planner use official damage numbers?", "No. It uses public launch-week research and transparent assumptions. Exact values should be updated when official notes or reliable tests are available."),
    ("Which Mistfall Hunter class should beginners choose?", "Beginners usually benefit from a safer class plan that protects extraction timing before chasing maximum burst damage."),
    ("Is Mistfall Hunter better solo or in a team?", "Solo runs reward mobility and safe exits. Team runs reward role clarity, support coverage, and avoiding duplicated loadout jobs."),
    ("How often should loadouts change?", "Review loadouts after patches, new weapons, class tuning, or when your party role changes."),
    ("Can I copy the result?", "Yes. Use the copy button to save a compact loadout note for your next run."),
]


PAGES = {
    "index": {"path": "/"},
    "classes": {"path": "/classes/"},
    "builds": {"path": "/builds/"},
    "guide": {"path": "/guide/"},
    "about": {"path": "/about/"},
    "contact": {"path": "/contact/"},
    "privacy-policy": {"path": "/privacy-policy/"},
    "terms-of-service": {"path": "/terms-of-service/"},
}


def tr(locale: str) -> Dict[str, str]:
    """
    返回指定语言的页面文案。

    :param locale: 语言代码
    :return: dict[str, str]，当前语言文案
    """
    return TRANSLATIONS.get(locale, TRANSLATIONS[DEFAULT_LANGUAGE])


def localized_path(page_key: str, locale: str) -> str:
    """
    生成指定页面和语言的站内路径。

    :param page_key: 页面键名
    :param locale: 语言代码
    :return: str，带语言前缀的路径
    """
    base_path = PAGES[page_key]["path"]
    if locale == DEFAULT_LANGUAGE:
        return base_path
    if base_path == "/":
        return f"/{locale}/"
    return f"/{locale}{base_path}"


def canonical_url(page_key: str, locale: str) -> str:
    """
    生成指定页面的 canonical URL。

    :param page_key: 页面键名
    :param locale: 语言代码
    :return: str，完整 canonical URL
    """
    return f"{BASE_URL}{localized_path(page_key, locale).rstrip('/')}/"


def alternate_urls(page_key: str) -> Dict[str, str]:
    """
    生成页面的 hreflang URL 映射。

    :param page_key: 页面键名
    :return: dict[str, str]，hreflang 到 URL 的映射
    """
    links = {"x-default": canonical_url(page_key, DEFAULT_LANGUAGE)}
    for locale in SUPPORTED_LANGUAGES:
        links[locale] = canonical_url(page_key, locale)
    return links


def common_context(page_key: str, locale: str) -> Dict[str, Any]:
    """
    生成所有模板共享的渲染上下文。

    :param page_key: 页面键名
    :param locale: 语言代码
    :return: dict[str, Any]，模板上下文字典
    """
    language_links = [
        {"code": code, "label": LOCALE_LABELS[code], "url": localized_path(page_key, code), "active": code == locale}
        for code in SUPPORTED_LANGUAGES
    ]
    return {
        "t": tr(locale),
        "locale": locale,
        "locale_label": LOCALE_LABELS[locale],
        "locale_market": LOCALE_MARKETS[locale],
        "languages": language_links,
        "canonical_url": canonical_url(page_key, locale),
        "alternate_urls": alternate_urls(page_key),
        "base_url": BASE_URL,
        "last_updated": LAST_UPDATED,
        "class_rows": CLASS_ROWS,
        "build_patterns": BUILD_PATTERNS,
        "faq_items": FAQ_ITEMS,
        "nav": [
            ("tool", localized_path("index", locale) + "#planner", tr(locale)["nav_tool"]),
            ("classes", localized_path("classes", locale), tr(locale)["nav_classes"]),
            ("builds", localized_path("builds", locale), tr(locale)["nav_builds"]),
            ("guide", localized_path("guide", locale), tr(locale)["nav_guide"]),
            ("faq", localized_path("index", locale) + "#faq", tr(locale)["nav_faq"]),
        ],
        "footer_links": {
            "about": localized_path("about", locale),
            "contact": localized_path("contact", locale),
            "privacy": localized_path("privacy-policy", locale),
            "terms": localized_path("terms-of-service", locale),
        },
    }


def render_page(page_key: str, locale: str = DEFAULT_LANGUAGE) -> str:
    """
    渲染指定页面和语言版本。

    :param page_key: 页面键名
    :param locale: 语言代码
    :return: str，页面 HTML
    """
    if page_key not in PAGES or locale not in SUPPORTED_LANGUAGES:
        abort(404)
    template = "legal.html" if page_key in {"about", "contact", "privacy-policy", "terms-of-service"} else "page.html"
    return render_template(template, page_key=page_key, **common_context(page_key, locale))


@app.route("/")
def index() -> str:
    """
    渲染英文首页。

    :return: str，首页 HTML
    """
    return render_page("index", DEFAULT_LANGUAGE)


@app.route("/<segment>/")
def single_segment_page(segment: str) -> str:
    """
    渲染单段路径对应的语言首页或英文内容页。

    :param segment: 语言代码或页面键名
    :return: str，页面 HTML
    """
    if segment in SUPPORTED_LANGUAGES:
        return render_page("index", segment)
    if segment in PAGES:
        return render_page(segment, DEFAULT_LANGUAGE)
    abort(404)


@app.route("/<page_key>/")
def content_page(page_key: str) -> str:
    """
    渲染英文内容页。

    :param page_key: 页面键名
    :return: str，内容页 HTML
    """
    return render_page(page_key, DEFAULT_LANGUAGE)


@app.route("/<lang>/<page_key>/")
def localized_content_page(lang: str, page_key: str) -> str:
    """
    渲染指定语言内容页。

    :param lang: 语言代码
    :param page_key: 页面键名
    :return: str，内容页 HTML
    """
    return render_page(page_key, lang)


@app.errorhandler(404)
def page_not_found(error: Exception) -> tuple[str, int]:
    """
    渲染 404 页面。

    :param error: Flask 异常对象
    :return: tuple[str, int]，404 HTML 和状态码
    """
    return render_template("404.html", **common_context("index", DEFAULT_LANGUAGE)), 404


if __name__ == "__main__":
    app.run(debug=True, port=5001)
