from __future__ import annotations

from datetime import date
from typing import Any, Dict, List

from flask import Flask, abort, render_template

from crossplay_guide import CROSSPLAY_GUIDES
from gameplay_guide import GAMEPLAY_GUIDES
from price_guide import PRICE_GUIDES

app = Flask(__name__)

BASE_URL = "https://mistfallloadouts.blog"
SUPPORTED_LANGUAGES = ["en", "es", "ja", "fr", "de", "pt", "ko", "it"]
DEFAULT_LANGUAGE = "en"
LAST_UPDATED = date(2026, 7, 31).isoformat()


LOCALE_LABELS = {
    "en": "English",
    "es": "Espa\u00f1ol",
    "ja": "\u65e5\u672c\u8a9e",
    "fr": "Fran\u00e7ais",
    "de": "Deutsch",
    "pt": "Portugu\u00eas",
    "ko": "\ud55c\uad6d\uc5b4",
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
        "signal_volume": "Similarweb 28d main-term window",
        "signal_kd": "Low-difficulty launch query",
        "signal_date": "Research window",
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
        "table_class": "Class",
        "table_fit": "Best fit",
        "table_strength": "Strength",
        "table_watch": "Watch out",
        "card_best": "Best for",
        "card_priorities": "Priorities",
        "card_avoid": "Avoid",
        "deep_title": "Loadout decision method",
        "site_scope": "Site scope",
        "data_handling": "Data handling",
        "accuracy_affiliation": "Accuracy and affiliation",
        "contact_heading": "Contact",
        "advertising_cookies": "Advertising and cookies",
        "user_choices": "User choices",
    },
    "es": {
        "title": "Planificador de loadouts de Mistfall Hunter",
        "meta_title": "Loadouts y builds de Mistfall Hunter",
        "meta_description": "Planifica loadouts de Mistfall Hunter por clase, rol, riesgo y arma con supuestos claros de la semana de lanzamiento.",
        "meta_keywords": "loadouts Mistfall Hunter, builds Mistfall Hunter, clases Mistfall Hunter",
        "nav_tool": "Planificador",
        "nav_classes": "Clases",
        "nav_builds": "Builds",
        "nav_guide": "Gu\u00eda",
        "nav_faq": "Preguntas frecuentes",
        "hero_eyebrow": "Planificaci\u00f3n de lanzamiento",
        "hero_title": "Loadouts de Mistfall Hunter para clases, riesgo y extracci\u00f3n",
        "hero_lede": "Elige rol, arma y nivel de riesgo para obtener una direcci\u00f3n pr\u00e1ctica de loadout antes de entrar a una partida.",
        "hero_note": "El planificador usa supuestos p\u00fablicos de lanzamiento. No afirma conocer valores ocultos de da\u00f1o.",
        "signal_volume": "Ventana de 28 d\u00edas del t\u00e9rmino principal en Similarweb",
        "signal_kd": "Consulta de lanzamiento con baja dificultad",
        "signal_date": "Ventana de investigaci\u00f3n",
        "tool_title": "Planificador de loadout",
        "tool_intro": "Ajusta los campos y revisa la recomendaci\u00f3n. El resultado prioriza estilo, supervivencia y valor para el equipo.",
        "class_label": "Clase",
        "role_label": "Rol",
        "risk_label": "Riesgo",
        "weapon_label": "Arma",
        "phase_label": "Progreso",
        "class_vanguard": "Vanguardia",
        "class_seeker": "Explorador",
        "class_arcanist": "Arcanista",
        "class_warden": "Guardi\u00e1n",
        "role_solo": "Extracci\u00f3n solo",
        "role_team": "Apoyo de equipo",
        "role_boss": "Presi\u00f3n a jefes",
        "risk_safe": "Seguro",
        "risk_balanced": "Equilibrado",
        "risk_greedy": "Agresivo",
        "weapon_melee": "Cuerpo a cuerpo",
        "weapon_ranged": "A distancia",
        "weapon_hybrid": "H\u00edbrido",
        "phase_early": "Inicio",
        "phase_mid": "Mitad",
        "phase_late": "Avanzado",
        "result_title": "Direcci\u00f3n recomendada",
        "result_tags": "Etiquetas prioritarias",
        "result_stats": "Prioridades de estad\u00edsticas",
        "result_route": "Ruta de extracci\u00f3n",
        "result_tip": "Consejo de run",
        "reset": "Restablecer",
        "copy": "Copiar",
        "copied": "Copiado",
        "classes_title": "Clases de Mistfall Hunter de un vistazo",
        "classes_intro": "Usa la tabla para decidir si tu loadout debe proteger la run, explorar con seguridad, hacer burst o mantener estable al grupo.",
        "builds_title": "Patrones de build que evitan errores de lanzamiento",
        "builds_intro": "Muchas builds iniciales fallan por acumular da\u00f1o sin resolver escape, roles repetidos o presi\u00f3n de recursos.",
        "guide_title": "C\u00f3mo usar el planificador antes de una run",
        "guide_intro": "Funciona como lista de decisi\u00f3n. Elige el estilo m\u00e1s cercano, lee los costes y ajusta cuando haya parches o pruebas fiables.",
        "data_title": "Datos y vigencia",
        "data_text": "Sitio creado para la ventana de b\u00fasqueda del 31 de julio de 2026. Google Trends mostr\u00f3 demanda activa en EE. UU. y Similarweb report\u00f3 demanda fuerte de 28 d\u00edas.",
        "faq_title": "Preguntas frecuentes sobre loadouts de Mistfall Hunter",
        "about_title": "Sobre Mistfall Loadouts",
        "about_text": "Mistfall Loadouts es un sitio independiente para planificar builds, comparar clases y preparar rutas con supuestos claros.",
        "privacy_title": "Pol\u00edtica de privacidad",
        "terms_title": "T\u00e9rminos de servicio",
        "contact_title": "Contacto de Mistfall Loadouts",
        "contact_text": "Env\u00eda correcciones, fuentes nuevas, problemas de accesibilidad o preguntas de pol\u00edtica a hello@mistfallloadouts.blog. Incluye la URL y el tema.",
        "legal_text": "Este recurso independiente no recopila inicios de sesi\u00f3n, no vende datos y no afirma afiliaci\u00f3n oficial.",
        "footer_disclaimer": "Planificador independiente creado por fans.",
        "table_class": "Clase",
        "table_fit": "Mejor uso",
        "table_strength": "Fortaleza",
        "table_watch": "Cuidado",
        "card_best": "Ideal para",
        "card_priorities": "Prioridades",
        "card_avoid": "Evita",
        "deep_title": "M\u00e9todo para decidir el loadout",
        "site_scope": "Alcance del sitio",
        "data_handling": "Tratamiento de datos",
        "accuracy_affiliation": "Precisi\u00f3n y afiliaci\u00f3n",
        "contact_heading": "Contacto",
        "advertising_cookies": "Publicidad y cookies",
        "user_choices": "Opciones del usuario",
    },
    "ja": {
        "title": "Mistfall Hunter \u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u30d7\u30e9\u30f3\u30ca\u30fc",
        "meta_title": "Mistfall Hunter \u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u3068\u30d3\u30eb\u30c9",
        "meta_description": "\u30af\u30e9\u30b9\u3001\u5f79\u5272\u3001\u30ea\u30b9\u30af\u3001\u6b66\u5668\u50be\u5411\u304b\u3089 Mistfall Hunter \u306e\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u65b9\u91dd\u3092\u6574\u7406\u3057\u307e\u3059\u3002",
        "meta_keywords": "Mistfall Hunter \u30ed\u30fc\u30c9\u30a2\u30a6\u30c8, Mistfall Hunter \u30d3\u30eb\u30c9, Mistfall Hunter \u30af\u30e9\u30b9",
        "nav_tool": "\u30d7\u30e9\u30f3\u30ca\u30fc",
        "nav_classes": "\u30af\u30e9\u30b9",
        "nav_builds": "\u30d3\u30eb\u30c9",
        "nav_guide": "\u30ac\u30a4\u30c9",
        "nav_faq": "よくある質問",
        "hero_eyebrow": "\u30ed\u30fc\u30f3\u30c1\u9031\u306e\u30d3\u30eb\u30c9\u8a08\u753b",
        "hero_title": "\u30af\u30e9\u30b9\u3001\u30ea\u30b9\u30af\u3001\u62bd\u51fa\u76ee\u6a19\u3067\u9078\u3076 Mistfall Hunter \u30ed\u30fc\u30c9\u30a2\u30a6\u30c8",
        "hero_lede": "\u5f79\u5272\u3001\u6b66\u5668\u50be\u5411\u3001\u30ea\u30b9\u30af\u3092\u9078\u3073\u3001\u51fa\u6483\u524d\u306b\u5b9f\u7528\u7684\u306a\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u65b9\u91dd\u3092\u78ba\u8a8d\u3067\u304d\u307e\u3059\u3002",
        "hero_note": "\u516c\u958b\u60c5\u5831\u306b\u57fa\u3065\u304f\u4eee\u8aac\u578b\u30d7\u30e9\u30f3\u30ca\u30fc\u3067\u3059\u3002\u672a\u516c\u958b\u306e\u30c0\u30e1\u30fc\u30b8\u5024\u306f\u65ad\u5b9a\u3057\u307e\u305b\u3093\u3002",
        "signal_volume": "Similarweb 28\u65e5\u9593\u306e\u4e3b\u8981\u30ad\u30fc\u30ef\u30fc\u30c9\u7a93",
        "signal_kd": "\u96e3\u6613\u5ea6\u306e\u4f4e\u3044\u30ed\u30fc\u30f3\u30c1\u691c\u7d22",
        "signal_date": "\u8abf\u67fb\u5bfe\u8c61\u671f\u9593",
        "tool_title": "\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u30d7\u30e9\u30f3\u30ca\u30fc",
        "tool_intro": "\u5165\u529b\u3092\u8abf\u6574\u3057\u3001\u63a8\u5968\u30ab\u30fc\u30c9\u3092\u78ba\u8a8d\u3057\u3066\u304f\u3060\u3055\u3044\u3002\u6b63\u78ba\u306a\u96a0\u3057\u6570\u5024\u3088\u308a\u3082\u3001\u751f\u5b58\u6027\u3068\u5f79\u5272\u9069\u5408\u3092\u91cd\u8996\u3057\u307e\u3059\u3002",
        "class_label": "\u30af\u30e9\u30b9",
        "role_label": "\u5f79\u5272",
        "risk_label": "\u30ea\u30b9\u30af",
        "weapon_label": "\u6b66\u5668",
        "phase_label": "\u9032\u884c\u5ea6",
        "class_vanguard": "\u30f4\u30a1\u30f3\u30ac\u30fc\u30c9",
        "class_seeker": "\u30b7\u30fc\u30ab\u30fc",
        "class_arcanist": "\u30a2\u30eb\u30ab\u30cb\u30b9\u30c8",
        "class_warden": "\u30a6\u30a9\u30fc\u30c7\u30f3",
        "role_solo": "\u30bd\u30ed\u62bd\u51fa",
        "role_team": "\u30c1\u30fc\u30e0\u652f\u63f4",
        "role_boss": "\u30dc\u30b9\u5727\u529b",
        "risk_safe": "\u5b89\u5168",
        "risk_balanced": "\u30d0\u30e9\u30f3\u30b9",
        "risk_greedy": "\u653b\u3081\u91cd\u8996",
        "weapon_melee": "\u8fd1\u63a5",
        "weapon_ranged": "\u9060\u8ddd\u96e2",
        "weapon_hybrid": "\u30cf\u30a4\u30d6\u30ea\u30c3\u30c9",
        "phase_early": "\u5e8f\u76e4",
        "phase_mid": "\u4e2d\u76e4",
        "phase_late": "\u7d42\u76e4",
        "result_title": "\u63a8\u5968\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u65b9\u91dd",
        "result_tags": "\u512a\u5148\u30bf\u30b0",
        "result_stats": "\u512a\u5148\u30b9\u30c6\u30fc\u30bf\u30b9",
        "result_route": "\u62bd\u51fa\u30eb\u30fc\u30c8",
        "result_tip": "\u5b9f\u8df5\u30e1\u30e2",
        "reset": "\u30ea\u30bb\u30c3\u30c8",
        "copy": "\u30b3\u30d4\u30fc",
        "copied": "\u30b3\u30d4\u30fc\u6e08\u307f",
        "classes_title": "Mistfall Hunter \u30af\u30e9\u30b9\u65e9\u898b\u8868",
        "classes_intro": "\u5b88\u308a\u3001\u7d22\u6575\u3001\u77ac\u9593\u706b\u529b\u3001\u5b89\u5b9a\u652f\u63f4\u306e\u3069\u308c\u3092\u91cd\u8996\u3059\u308b\u304b\u3067\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u65b9\u91dd\u304c\u5909\u308f\u308a\u307e\u3059\u3002",
        "builds_title": "\u30ed\u30fc\u30f3\u30c1\u9031\u306b\u907f\u3051\u305f\u3044\u30d3\u30eb\u30c9\u306e\u5931\u6557",
        "builds_intro": "\u706b\u529b\u3060\u3051\u3092\u7a4d\u3080\u3068\u3001\u8131\u51fa\u30bf\u30a4\u30df\u30f3\u30b0\u3001\u5f79\u5272\u91cd\u8907\u3001\u8cc7\u6e90\u7ba1\u7406\u3067\u5931\u6557\u3057\u3084\u3059\u304f\u306a\u308a\u307e\u3059\u3002",
        "guide_title": "\u51fa\u6483\u524d\u306e\u4f7f\u3044\u65b9",
        "guide_intro": "\u307e\u305a\u8fd1\u3044\u30b9\u30bf\u30a4\u30eb\u3092\u9078\u3073\u3001\u30c8\u30ec\u30fc\u30c9\u30aa\u30d5\u3092\u8aad\u307f\u3001\u30d1\u30c3\u30c1\u3084\u691c\u8a3c\u30c7\u30fc\u30bf\u306b\u5408\u308f\u305b\u3066\u8abf\u6574\u3057\u307e\u3059\u3002",
        "data_title": "\u30c7\u30fc\u30bf\u3068\u9bae\u5ea6\u30e1\u30e2",
        "data_text": "2026\u5e747\u670831\u65e5\u306e\u691c\u7d22\u72b6\u6cc1\u3092\u3082\u3068\u306b\u4f5c\u6210\u3057\u307e\u3057\u305f\u3002\u30c8\u30ec\u30f3\u30c9\u8abf\u67fb\u3068 Similarweb \u306e\u9700\u8981\u3092\u78ba\u8a8d\u3057\u3001\u6b63\u78ba\u306a\u30b2\u30fc\u30e0\u5185\u6570\u5024\u304c\u78ba\u8a8d\u3055\u308c\u308b\u307e\u3067\u306f\u65b9\u91dd\u3068\u3057\u3066\u6271\u3044\u307e\u3059\u3002",
        "faq_title": "Mistfall Hunter \u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u306e\u3088\u304f\u3042\u308b\u8cea\u554f",
        "about_title": "Mistfall Loadouts \u306b\u3064\u3044\u3066",
        "about_text": "Mistfall Hunter \u306e\u30d3\u30eb\u30c9\u5224\u65ad\u3001\u30af\u30e9\u30b9\u6bd4\u8f03\u3001\u30eb\u30fc\u30c8\u6e96\u5099\u3092\u652f\u63f4\u3059\u308b\u72ec\u7acb\u30d5\u30a1\u30f3\u30b5\u30a4\u30c8\u3067\u3059\u3002",
        "privacy_title": "\u30d7\u30e9\u30a4\u30d0\u30b7\u30fc\u30dd\u30ea\u30b7\u30fc",
        "terms_title": "\u5229\u7528\u898f\u7d04",
        "contact_title": "Mistfall Loadouts \u3078\u306e\u9023\u7d61",
        "contact_text": "\u4fee\u6b63\u3001\u60c5\u5831\u66f4\u65b0\u3001\u30a2\u30af\u30bb\u30b7\u30d3\u30ea\u30c6\u30a3\u3001\u30dd\u30ea\u30b7\u30fc\u306b\u95a2\u3059\u308b\u8cea\u554f\u306f hello@mistfallloadouts.blog \u307e\u3067\u304a\u9001\u308a\u304f\u3060\u3055\u3044\u3002",
        "legal_text": "\u672c\u30b5\u30a4\u30c8\u306f\u30ed\u30b0\u30a4\u30f3\u60c5\u5831\u3092\u53ce\u96c6\u305b\u305a\u3001\u30c7\u30fc\u30bf\u3092\u8ca9\u58f2\u305b\u305a\u3001\u516c\u5f0f\u904b\u55b6\u3068\u306e\u63d0\u643a\u3092\u4e3b\u5f35\u3057\u307e\u305b\u3093\u3002",
        "footer_disclaimer": "\u30d5\u30a1\u30f3\u5236\u4f5c\u306e\u72ec\u7acb\u30d7\u30e9\u30f3\u30ca\u30fc\u3067\u3059\u3002",
        "table_class": "\u30af\u30e9\u30b9",
        "table_fit": "\u5411\u3044\u3066\u3044\u308b\u5f79\u5272",
        "table_strength": "\u5f37\u307f",
        "table_watch": "\u6ce8\u610f\u70b9",
        "card_best": "\u5411\u3044\u3066\u3044\u308b\u5834\u9762",
        "card_priorities": "\u512a\u5148\u9805\u76ee",
        "card_avoid": "\u907f\u3051\u308b\u70b9",
        "deep_title": "\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u5224\u65ad\u65b9\u6cd5",
        "site_scope": "\u30b5\u30a4\u30c8\u306e\u7bc4\u56f2",
        "data_handling": "\u30c7\u30fc\u30bf\u306e\u6271\u3044",
        "accuracy_affiliation": "\u6b63\u78ba\u6027\u3068\u63d0\u643a\u95a2\u4fc2",
        "contact_heading": "\u9023\u7d61\u5148",
        "advertising_cookies": "\u5e83\u544a\u3068 Cookie",
        "user_choices": "\u30e6\u30fc\u30b6\u30fc\u306e\u9078\u629e",
    },
}

for locale in ["fr", "de", "pt", "ko", "it"]:
    TRANSLATIONS[locale] = TRANSLATIONS["en"] | {
        "fr": {
            "title": "Planificateur de loadouts Mistfall Hunter",
            "meta_title": "Loadouts et builds Mistfall Hunter",
            "meta_description": "Planifiez les loadouts Mistfall Hunter par classe, r\u00f4le, risque et arme avec des hypoth\u00e8ses claires.",
            "nav_tool": "Planificateur",
            "nav_classes": "Classes",
            "nav_builds": "Builds",
            "nav_guide": "Conseils",
            "nav_faq": "Questions fréquentes",
            "hero_eyebrow": "Planification de la semaine de lancement",
            "hero_title": "Loadouts Mistfall Hunter par classe, risque et extraction",
            "hero_lede": "Choisissez le r\u00f4le, l'arme et le niveau de risque pour obtenir une direction pratique avant la sortie.",
            "hero_note": "Le planificateur utilise des hypoth\u00e8ses publiques et ne pr\u00e9tend pas conna\u00eetre les valeurs cach\u00e9es.",
            "signal_volume": "Fen\u00eatre Similarweb de 28 jours",
            "signal_kd": "Requ\u00eate de lancement peu difficile",
            "signal_date": "Fen\u00eatre de recherche",
            "tool_title": "Planificateur de loadout",
            "tool_intro": "Ajustez les champs et lisez la carte de recommandation. Le r\u00e9sultat privil\u00e9gie la survie et l'utilit\u00e9 d'\u00e9quipe.",
            "class_label": "Classe",
            "role_label": "R\u00f4le",
            "risk_label": "Risque",
            "weapon_label": "Arme",
            "phase_label": "Progression",
            "class_vanguard": "Avant-garde",
            "class_seeker": "\u00c9claireur",
            "class_arcanist": "Arcaniste",
            "class_warden": "Gardien",
            "role_solo": "Extraction solo",
            "role_team": "Soutien d'\u00e9quipe",
            "role_boss": "Pression sur boss",
            "risk_safe": "S\u00fbr",
            "risk_balanced": "\u00c9quilibr\u00e9",
            "risk_greedy": "Agressif",
            "weapon_melee": "M\u00eal\u00e9e",
            "weapon_ranged": "Distance",
            "weapon_hybrid": "Hybride",
            "phase_early": "D\u00e9but",
            "phase_mid": "Milieu",
            "phase_late": "Fin",
            "result_title": "Direction de loadout recommand\u00e9e",
            "result_tags": "Tags prioritaires",
            "result_stats": "Statistiques prioritaires",
            "result_route": "Route d'extraction",
            "result_tip": "Conseil de run",
            "reset": "R\u00e9initialiser",
            "copy": "Copier",
            "copied": "Copi\u00e9",
            "classes_title": "Classes Mistfall Hunter en un coup d'oeil",
            "classes_intro": "Utilisez ce tableau pour savoir si votre loadout doit prot\u00e9ger, \u00e9clairer, burst ou stabiliser l'\u00e9quipe.",
            "builds_title": "Mod\u00e8les de build qui \u00e9vitent les erreurs de lancement",
            "builds_intro": "Les premiers builds \u00e9chouent souvent quand ils empilent les d\u00e9g\u00e2ts sans pr\u00e9voir l'\u00e9vasion, les r\u00f4les ou les ressources.",
            "guide_title": "Comment utiliser le planificateur avant une run",
            "guide_intro": "Choisissez le style le plus proche, lisez les compromis, puis ajustez avec les notes de patch ou les tests fiables.",
            "data_title": "Donn\u00e9es et fra\u00eecheur",
            "data_text": "Ce site suit la fen\u00eatre de recherche du 31 juillet 2026 et pr\u00e9sente les conseils comme des orientations tant que les valeurs exactes restent \u00e0 confirmer.",
            "faq_title": "Questions fréquentes sur les loadouts Mistfall Hunter",
            "about_title": "\u00c0 propos de Mistfall Loadouts",
            "about_text": "Mistfall Loadouts est un site ind\u00e9pendant pour planifier les builds, comparer les classes et pr\u00e9parer les routes.",
            "privacy_title": "Politique de confidentialit\u00e9",
            "terms_title": "Conditions d'utilisation",
            "contact_title": "Contacter Mistfall Loadouts",
            "contact_text": "Envoyez corrections, sources ou questions \u00e0 hello@mistfallloadouts.blog avec l'URL concern\u00e9e.",
            "legal_text": "Cette ressource ind\u00e9pendante ne collecte pas de connexions et ne revendique aucune affiliation officielle.",
            "footer_disclaimer": "Planificateur ind\u00e9pendant cr\u00e9\u00e9 par des fans.",
            "table_class": "Classe",
            "table_fit": "Meilleur usage",
            "table_strength": "Force",
            "table_watch": "Attention",
            "card_best": "Id\u00e9al pour",
            "card_priorities": "Priorit\u00e9s",
            "card_avoid": "\u00c0 \u00e9viter",
            "deep_title": "M\u00e9thode de d\u00e9cision du loadout",
            "site_scope": "Port\u00e9e du site",
            "data_handling": "Gestion des donn\u00e9es",
            "accuracy_affiliation": "Exactitude et affiliation",
            "contact_heading": "Contact",
            "advertising_cookies": "Publicit\u00e9 et cookies",
            "user_choices": "Choix utilisateur",
        },
        "de": {
            "title": "Mistfall Hunter Loadout-Planer",
            "meta_title": "Mistfall Hunter Loadouts und Builds",
            "meta_description": "Plane Mistfall Hunter Loadouts nach Klasse, Rolle, Risiko und Waffe mit klaren Annahmen.",
            "nav_tool": "Planer",
            "nav_classes": "Klassen",
            "nav_builds": "Builds",
            "nav_guide": "Anleitung",
            "nav_faq": "Häufige Fragen",
            "hero_eyebrow": "Build-Planung zur Startwoche",
            "hero_title": "Mistfall Hunter Loadouts f\u00fcr Klassen, Risiko und Extraktion",
            "hero_lede": "W\u00e4hle Rolle, Waffenstil und Risiko, um vor dem Run eine brauchbare Loadout-Richtung zu erhalten.",
            "hero_note": "Der Planer nutzt \u00f6ffentliche Annahmen und behauptet keine versteckten Schadenswerte.",
            "signal_volume": "Similarweb 28-Tage-Fenster",
            "signal_kd": "Launch-Suche mit geringer Schwierigkeit",
            "signal_date": "Recherchefenster",
            "tool_title": "Loadout-Planer",
            "tool_intro": "Passe die Eingaben an und lies die Empfehlung. Der Fokus liegt auf \u00dcberleben, Rolle und Teamnutzen.",
            "class_label": "Klasse",
            "role_label": "Rolle",
            "risk_label": "Risiko",
            "weapon_label": "Waffe",
            "phase_label": "Fortschritt",
            "class_vanguard": "Vorhut",
            "class_seeker": "Sucher",
            "class_arcanist": "Arkanist",
            "class_warden": "H\u00fcter",
            "role_solo": "Solo-Extraktion",
            "role_team": "Teamunterst\u00fctzung",
            "role_boss": "Bossdruck",
            "risk_safe": "Sicher",
            "risk_balanced": "Ausgewogen",
            "risk_greedy": "Riskant",
            "weapon_melee": "Nahkampf",
            "weapon_ranged": "Fernkampf",
            "weapon_hybrid": "Hybrid",
            "phase_early": "Fr\u00fch",
            "phase_mid": "Mitte",
            "phase_late": "Sp\u00e4t",
            "result_title": "Empfohlene Loadout-Richtung",
            "result_tags": "Priorit\u00e4ts-Tags",
            "result_stats": "Priorisierte Werte",
            "result_route": "Extraktionsroute",
            "result_tip": "Run-Tipp",
            "reset": "Zur\u00fccksetzen",
            "copy": "Kopieren",
            "copied": "Kopiert",
            "classes_title": "Mistfall Hunter Klassen im \u00dcberblick",
            "classes_intro": "Die Tabelle zeigt, ob dein Loadout Schutz, Aufkl\u00e4rung, Burst oder Stabilit\u00e4t liefern sollte.",
            "builds_title": "Build-Muster gegen typische Startfehler",
            "builds_intro": "Fr\u00fche Builds scheitern oft, wenn sie Schaden stapeln, aber Flucht, Rollen und Ressourcen ignorieren.",
            "guide_title": "So nutzt du den Planer vor dem Run",
            "guide_intro": "W\u00e4hle den n\u00e4chsten Stil, lies die Kompromisse und passe nach Patches oder verl\u00e4sslichen Tests an.",
            "data_title": "Daten und Aktualit\u00e4t",
            "data_text": "Der Stand bezieht sich auf das Suchfenster vom 31. Juli 2026. Die Hinweise bleiben Richtungen, bis exakte Werte best\u00e4tigt sind.",
            "faq_title": "Häufige Fragen zu Mistfall-Hunter-Loadouts",
            "about_title": "\u00dcber Mistfall Loadouts",
            "about_text": "Mistfall Loadouts ist eine unabh\u00e4ngige Planungsseite f\u00fcr Builds, Klassenvergleiche und Routen.",
            "privacy_title": "Datenschutzrichtlinie",
            "terms_title": "Nutzungsbedingungen",
            "contact_title": "Kontakt zu Mistfall Loadouts",
            "contact_text": "Sende Korrekturen, Quellen oder Fragen mit URL an hello@mistfallloadouts.blog.",
            "legal_text": "Diese unabh\u00e4ngige Fan-Ressource sammelt keine Logins und behauptet keine offizielle Verbindung.",
            "footer_disclaimer": "Unabh\u00e4ngiger, von Fans erstellter Planer.",
            "table_class": "Klasse",
            "table_fit": "Beste Rolle",
            "table_strength": "St\u00e4rke",
            "table_watch": "Achtung",
            "card_best": "Geeignet f\u00fcr",
            "card_priorities": "Priorit\u00e4ten",
            "card_avoid": "Vermeiden",
            "deep_title": "Methode zur Loadout-Entscheidung",
            "site_scope": "Umfang der Seite",
            "data_handling": "Datenverarbeitung",
            "accuracy_affiliation": "Genauigkeit und Zugeh\u00f6rigkeit",
            "contact_heading": "Kontakt",
            "advertising_cookies": "Werbung und Cookies",
            "user_choices": "Nutzerauswahl",
        },
        "pt": {
            "title": "Planejador de loadouts de Mistfall Hunter",
            "meta_title": "Loadouts e builds de Mistfall Hunter",
            "meta_description": "Planeje loadouts de Mistfall Hunter por classe, fun\u00e7\u00e3o, risco e arma com premissas claras.",
            "nav_tool": "Planejador",
            "nav_classes": "Classes",
            "nav_builds": "Builds",
            "nav_guide": "Guia",
            "nav_faq": "Perguntas frequentes",
            "hero_eyebrow": "Planejamento da semana de lan\u00e7amento",
            "hero_title": "Loadouts de Mistfall Hunter para classes, risco e extra\u00e7\u00e3o",
            "hero_lede": "Escolha fun\u00e7\u00e3o, arma e risco para receber uma dire\u00e7\u00e3o pr\u00e1tica antes da run.",
            "hero_note": "O planejador usa premissas p\u00fablicas e n\u00e3o afirma conhecer valores ocultos.",
            "signal_volume": "Janela Similarweb de 28 dias",
            "signal_kd": "Consulta de lan\u00e7amento com baixa dificuldade",
            "signal_date": "Janela de pesquisa",
            "tool_title": "Planejador de loadout",
            "tool_intro": "Ajuste os campos e leia a recomenda\u00e7\u00e3o. O resultado prioriza sobreviv\u00eancia, fun\u00e7\u00e3o e valor para o time.",
            "class_label": "Classe",
            "role_label": "Fun\u00e7\u00e3o",
            "risk_label": "Risco",
            "weapon_label": "Arma",
            "phase_label": "Progresso",
            "class_vanguard": "Vanguarda",
            "class_seeker": "Batedor",
            "class_arcanist": "Arcanista",
            "class_warden": "Guard\u00e3o",
            "role_solo": "Extra\u00e7\u00e3o solo",
            "role_team": "Suporte de equipe",
            "role_boss": "Press\u00e3o em chefe",
            "risk_safe": "Seguro",
            "risk_balanced": "Equilibrado",
            "risk_greedy": "Arriscado",
            "weapon_melee": "Corpo a corpo",
            "weapon_ranged": "Dist\u00e2ncia",
            "weapon_hybrid": "H\u00edbrido",
            "phase_early": "In\u00edcio",
            "phase_mid": "Meio",
            "phase_late": "Final",
            "result_title": "Dire\u00e7\u00e3o de loadout recomendada",
            "result_tags": "Tags priorit\u00e1rias",
            "result_stats": "Prioridades de atributos",
            "result_route": "Rota de extra\u00e7\u00e3o",
            "result_tip": "Dica de run",
            "reset": "Redefinir",
            "copy": "Copiar",
            "copied": "Copiado",
            "classes_title": "Classes de Mistfall Hunter em resumo",
            "classes_intro": "Use a tabela para decidir se o loadout deve proteger, explorar, causar burst ou estabilizar a equipe.",
            "builds_title": "Padr\u00f5es de build que evitam erros do lan\u00e7amento",
            "builds_intro": "Builds iniciais falham quando acumulam dano sem resolver fuga, fun\u00e7\u00f5es repetidas ou recursos.",
            "guide_title": "Como usar o planejador antes da run",
            "guide_intro": "Escolha o estilo mais pr\u00f3ximo, leia os custos e ajuste depois de patches ou testes confi\u00e1veis.",
            "data_title": "Dados e atualidade",
            "data_text": "Este site foi criado para a janela de pesquisa de 31 de julho de 2026 e trata as recomenda\u00e7\u00f5es como dire\u00e7\u00f5es at\u00e9 os valores exatos serem confirmados.",
            "faq_title": "Perguntas frequentes sobre loadouts de Mistfall Hunter",
            "about_title": "Sobre Mistfall Loadouts",
            "about_text": "Mistfall Loadouts \u00e9 um site independente para planejar builds, comparar classes e preparar rotas.",
            "privacy_title": "Pol\u00edtica de privacidade",
            "terms_title": "Termos de servi\u00e7o",
            "contact_title": "Contato do Mistfall Loadouts",
            "contact_text": "Envie corre\u00e7\u00f5es, fontes ou perguntas com a URL para hello@mistfallloadouts.blog.",
            "legal_text": "Este recurso independente n\u00e3o coleta logins e n\u00e3o afirma afilia\u00e7\u00e3o oficial.",
            "footer_disclaimer": "Planejador independente feito por f\u00e3s.",
            "table_class": "Classe",
            "table_fit": "Melhor uso",
            "table_strength": "For\u00e7a",
            "table_watch": "Cuidado",
            "card_best": "Ideal para",
            "card_priorities": "Prioridades",
            "card_avoid": "Evite",
            "deep_title": "M\u00e9todo de decis\u00e3o do loadout",
            "site_scope": "Escopo do site",
            "data_handling": "Tratamento de dados",
            "accuracy_affiliation": "Precis\u00e3o e afilia\u00e7\u00e3o",
            "contact_heading": "Contato",
            "advertising_cookies": "Publicidade e cookies",
            "user_choices": "Escolhas do usu\u00e1rio",
        },
        "ko": {
            "title": "Mistfall Hunter \ub85c\ub4dc\uc544\uc6c3 \ud50c\ub798\ub108",
            "meta_title": "Mistfall Hunter \ub85c\ub4dc\uc544\uc6c3\uacfc \ube4c\ub4dc",
            "meta_description": "\ud074\ub798\uc2a4, \uc5ed\ud560, \uc704\ud5d8\ub3c4, \ubb34\uae30 \uc131\ud5a5\uc73c\ub85c Mistfall Hunter \ub85c\ub4dc\uc544\uc6c3\uc744 \uacc4\ud68d\ud569\ub2c8\ub2e4.",
            "nav_tool": "\ud50c\ub798\ub108",
            "nav_classes": "\ud074\ub798\uc2a4",
            "nav_builds": "\ube4c\ub4dc",
            "nav_guide": "\uac00\uc774\ub4dc",
            "nav_faq": "\uc790\uc8fc \ubb3b\ub294 \uc9c8\ubb38",
            "hero_eyebrow": "\ucd9c\uc2dc \uc8fc\uac04 \ube4c\ub4dc \uacc4\ud68d",
            "hero_title": "\ud074\ub798\uc2a4, \uc704\ud5d8\ub3c4, \ud0c8\ucd9c \ubaa9\ud45c\ub85c \uc120\ud0dd\ud558\ub294 Mistfall Hunter \ub85c\ub4dc\uc544\uc6c3",
            "hero_lede": "\uc5ed\ud560, \ubb34\uae30, \uc704\ud5d8\ub3c4\ub97c \uc120\ud0dd\ud574 \ub7f0 \uc804\uc5d0 \uc2e4\uc6a9\uc801\uc778 \ub85c\ub4dc\uc544\uc6c3 \ubc29\ud5a5\uc744 \ud655\uc778\ud558\uc138\uc694.",
            "hero_note": "\uacf5\uac1c \uc815\ubcf4\uc5d0 \uae30\ubc18\ud55c \uac00\uc124\ud615 \ud50c\ub798\ub108\uc774\uba70 \uc228\uaca8\uc9c4 \ud53c\ud574\ub7c9\uc744 \ub2e8\uc815\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.",
            "signal_volume": "Similarweb 28\uc77c \uc8fc\uc694 \ud0a4\uc6cc\ub4dc \uad6c\uac04",
            "signal_kd": "\ub09c\uc774\ub3c4\uac00 \ub0ae\uc740 \ucd9c\uc2dc \uac80\uc0c9\uc5b4",
            "signal_date": "\uc870\uc0ac \uae30\uac04",
            "tool_title": "\ub85c\ub4dc\uc544\uc6c3 \ud50c\ub798\ub108",
            "tool_intro": "\uc785\ub825\uac12\uc744 \uc870\uc815\ud558\uace0 \ucd94\ucc9c \uce74\ub4dc\ub97c \ud655\uc778\ud558\uc138\uc694. \uc0dd\uc874\uc131\uacfc \uc5ed\ud560 \uc801\ud569\uc744 \uc6b0\uc120\ud569\ub2c8\ub2e4.",
            "class_label": "\ud074\ub798\uc2a4",
            "role_label": "\uc5ed\ud560",
            "risk_label": "\uc704\ud5d8\ub3c4",
            "weapon_label": "\ubb34\uae30",
            "phase_label": "\uc9c4\ud589\ub3c4",
            "class_vanguard": "\ubc45\uac00\ub4dc",
            "class_seeker": "\uc2dc\ucee4",
            "class_arcanist": "\uc544\uce74\ub2c8\uc2a4\ud2b8",
            "class_warden": "\uc6cc\ub4e0",
            "role_solo": "\uc194\ub85c \ud0c8\ucd9c",
            "role_team": "\ud300 \uc9c0\uc6d0",
            "role_boss": "\ubcf4\uc2a4 \uc555\ubc15",
            "risk_safe": "\uc548\uc804",
            "risk_balanced": "\uade0\ud615",
            "risk_greedy": "\uacf5\uaca9\uc801",
            "weapon_melee": "\uadfc\uc811",
            "weapon_ranged": "\uc6d0\uac70\ub9ac",
            "weapon_hybrid": "\ud558\uc774\ube0c\ub9ac\ub4dc",
            "phase_early": "\ucd08\ubc18",
            "phase_mid": "\uc911\ubc18",
            "phase_late": "\ud6c4\ubc18",
            "result_title": "\ucd94\ucc9c \ub85c\ub4dc\uc544\uc6c3 \ubc29\ud5a5",
            "result_tags": "\uc6b0\uc120 \ud0dc\uadf8",
            "result_stats": "\uc6b0\uc120 \ub2a5\ub825\uce58",
            "result_route": "\ud0c8\ucd9c \uacbd\ub85c",
            "result_tip": "\ub7f0 \ud301",
            "reset": "\ucd08\uae30\ud654",
            "copy": "\ubcf5\uc0ac",
            "copied": "\ubcf5\uc0ac\ub428",
            "classes_title": "Mistfall Hunter \ud074\ub798\uc2a4 \ud55c\ub208\uc5d0 \ubcf4\uae30",
            "classes_intro": "\ub85c\ub4dc\uc544\uc6c3\uc774 \ubcf4\ud638, \uc815\ucc30, \uc21c\uac04 \ud654\ub825, \ud300 \uc548\uc815 \uc911 \ubb34\uc5c7\uc744 \ub9e1\uc544\uc57c \ud558\ub294\uc9c0 \ud655\uc778\ud558\uc138\uc694.",
            "builds_title": "\ucd9c\uc2dc \uc8fc\uac04\uc5d0 \ud53c\ud574\uc57c \ud560 \ube4c\ub4dc \uc2e4\uc218",
            "builds_intro": "\ucd08\uae30 \ube4c\ub4dc\ub294 \ub3c4\uc8fc, \uc5ed\ud560 \uc911\ubcf5, \uc790\uc6d0 \uad00\ub9ac\ub97c \ud480\uc9c0 \uc54a\uace0 \ud654\ub825\ub9cc \uc313\uc744 \ub54c \uc2e4\ud328\ud558\uae30 \uc27d\uc2b5\ub2c8\ub2e4.",
            "guide_title": "\ub7f0 \uc804 \ud50c\ub798\ub108 \uc0ac\uc6a9\ubc95",
            "guide_intro": "\uac00\uc7a5 \uac00\uae4c\uc6b4 \uc2a4\ud0c0\uc77c\uc744 \uace0\ub974\uace0 \ud2b8\ub808\uc774\ub4dc\uc624\ud504\ub97c \uc77d\uc740 \ub4a4 \ud328\uce58\uc640 \uc2e0\ub8b0\ud560 \uc218 \uc788\ub294 \ud14c\uc2a4\ud2b8\uc5d0 \ub9de\ucdb0 \uc870\uc815\ud558\uc138\uc694.",
            "data_title": "\ub370\uc774\ud130\uc640 \uc2e0\uc120\ub3c4 \uba54\ubaa8",
            "data_text": "2026\ub144 7\uc6d4 31\uc77c \uac80\uc0c9 \uad6c\uac04\uc744 \uae30\uc900\uc73c\ub85c \uc791\uc131\ub418\uc5c8\uc73c\uba70, \uc815\ud655\ud55c \uac8c\uc784 \uc218\uce58\uac00 \ud655\uc778\ub420 \ub54c\uae4c\uc9c0\ub294 \ubc29\ud5a5\uc73c\ub85c \uc81c\uc2dc\ud569\ub2c8\ub2e4.",
            "faq_title": "Mistfall Hunter \ub85c\ub4dc\uc544\uc6c3 \uc790\uc8fc \ubb3b\ub294 \uc9c8\ubb38",
            "about_title": "Mistfall Loadouts \uc18c\uac1c",
            "about_text": "Mistfall Hunter \ube4c\ub4dc \ud310\ub2e8, \ud074\ub798\uc2a4 \ube44\uad50, \ub8e8\ud2b8 \uc900\ube44\ub97c \ub3d5\ub294 \ub3c5\ub9bd \ud32c \uc0ac\uc774\ud2b8\uc785\ub2c8\ub2e4.",
            "privacy_title": "\uac1c\uc778\uc815\ubcf4 \ucc98\ub9ac\ubc29\uce68",
            "terms_title": "\uc774\uc6a9 \uc57d\uad00",
            "contact_title": "Mistfall Loadouts \uc5f0\ub77d\ucc98",
            "contact_text": "\uc218\uc815, \ucd9c\ucc98 \uc5c5\ub370\uc774\ud2b8, \uc811\uadfc\uc131 \ubb38\uc81c\ub294 hello@mistfallloadouts.blog \ub85c URL\uacfc \ud568\uaed8 \ubcf4\ub0b4 \uc8fc\uc138\uc694.",
            "legal_text": "\uc774 \ub3c5\ub9bd \ud32c \uc790\ub8cc\ub294 \ub85c\uadf8\uc778\uc744 \uc218\uc9d1\ud558\uc9c0 \uc54a\uace0 \uacf5\uc2dd \uc81c\ud734\ub97c \uc8fc\uc7a5\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.",
            "footer_disclaimer": "\ud32c\uc774 \ub9cc\ub4e0 \ub3c5\ub9bd \ud50c\ub798\ub108\uc785\ub2c8\ub2e4.",
            "table_class": "\ud074\ub798\uc2a4",
            "table_fit": "\uc801\ud569\ud55c \uc5ed\ud560",
            "table_strength": "\uac15\uc810",
            "table_watch": "\uc8fc\uc758",
            "card_best": "\uc801\ud569\ud55c \uc0c1\ud669",
            "card_priorities": "\uc6b0\uc120\uc21c\uc704",
            "card_avoid": "\ud53c\ud560 \uc810",
            "deep_title": "\ub85c\ub4dc\uc544\uc6c3 \uacb0\uc815 \ubc29\ubc95",
            "site_scope": "\uc0ac\uc774\ud2b8 \ubc94\uc704",
            "data_handling": "\ub370\uc774\ud130 \ucc98\ub9ac",
            "accuracy_affiliation": "\uc815\ud655\uc131\uacfc \uad00\uacc4",
            "contact_heading": "\uc5f0\ub77d\ucc98",
            "advertising_cookies": "\uad11\uace0\uc640 \ucfe0\ud0a4",
            "user_choices": "\uc0ac\uc6a9\uc790 \uc120\ud0dd",
        },
        "it": {
            "title": "Pianificatore loadout Mistfall Hunter",
            "meta_title": "Loadout e build di Mistfall Hunter",
            "meta_description": "Pianifica loadout di Mistfall Hunter per classe, ruolo, rischio e arma con ipotesi chiare.",
            "nav_tool": "Planner",
            "nav_classes": "Classi",
            "nav_builds": "Build",
            "nav_guide": "Guida",
            "nav_faq": "Domande frequenti",
            "hero_eyebrow": "Pianificazione della settimana di lancio",
            "hero_title": "Loadout Mistfall Hunter per classi, rischio ed estrazione",
            "hero_lede": "Scegli ruolo, arma e rischio per ottenere una direzione pratica prima della run.",
            "hero_note": "Il planner usa ipotesi pubbliche e non pretende di conoscere valori nascosti.",
            "signal_volume": "Finestra Similarweb di 28 giorni",
            "signal_kd": "Query di lancio a bassa difficolt\u00e0",
            "signal_date": "Finestra di ricerca",
            "tool_title": "Planner loadout",
            "tool_intro": "Regola gli input e leggi la raccomandazione. Il risultato privilegia sopravvivenza, ruolo e valore per il team.",
            "class_label": "Classe",
            "role_label": "Ruolo",
            "risk_label": "Rischio",
            "weapon_label": "Arma",
            "phase_label": "Progresso",
            "class_vanguard": "Avanguardia",
            "class_seeker": "Esploratore",
            "class_arcanist": "Arcanista",
            "class_warden": "Custode",
            "role_solo": "Estrazione solo",
            "role_team": "Supporto team",
            "role_boss": "Pressione boss",
            "risk_safe": "Sicuro",
            "risk_balanced": "Bilanciato",
            "risk_greedy": "Avido",
            "weapon_melee": "Mischia",
            "weapon_ranged": "Distanza",
            "weapon_hybrid": "Ibrido",
            "phase_early": "Inizio",
            "phase_mid": "Met\u00e0",
            "phase_late": "Finale",
            "result_title": "Direzione loadout consigliata",
            "result_tags": "Tag prioritari",
            "result_stats": "Statistiche prioritarie",
            "result_route": "Rotta di estrazione",
            "result_tip": "Consiglio run",
            "reset": "Reimposta",
            "copy": "Copia",
            "copied": "Copiato",
            "classes_title": "Classi di Mistfall Hunter in sintesi",
            "classes_intro": "Usa la tabella per capire se il loadout deve proteggere, esplorare, fare burst o stabilizzare il gruppo.",
            "builds_title": "Schemi di build che evitano errori di lancio",
            "builds_intro": "Le prime build falliscono quando accumulano danni senza risolvere fuga, ruoli duplicati o risorse.",
            "guide_title": "Come usare il planner prima di una run",
            "guide_intro": "Scegli lo stile pi\u00f9 vicino, leggi i compromessi e aggiorna dopo patch o test affidabili.",
            "data_title": "Dati e freschezza",
            "data_text": "Il sito segue la finestra di ricerca del 31 luglio 2026 e presenta i consigli come direzioni finch\u00e9 i valori esatti non sono confermati.",
            "faq_title": "Domande frequenti sui loadout di Mistfall Hunter",
            "about_title": "Informazioni su Mistfall Loadouts",
            "about_text": "Mistfall Loadouts \u00e8 un sito indipendente per pianificare build, confrontare classi e preparare rotte.",
            "privacy_title": "Informativa sulla privacy",
            "terms_title": "Termini di servizio",
            "contact_title": "Contatta Mistfall Loadouts",
            "contact_text": "Invia correzioni, fonti o domande con l'URL a hello@mistfallloadouts.blog.",
            "legal_text": "Questa risorsa indipendente non raccoglie login e non rivendica affiliazione ufficiale.",
            "footer_disclaimer": "Planner indipendente creato dai fan.",
            "table_class": "Classe",
            "table_fit": "Uso migliore",
            "table_strength": "Forza",
            "table_watch": "Attenzione",
            "card_best": "Ideale per",
            "card_priorities": "Priorit\u00e0",
            "card_avoid": "Evita",
            "deep_title": "Metodo di decisione del loadout",
            "site_scope": "Ambito del sito",
            "data_handling": "Gestione dei dati",
            "accuracy_affiliation": "Accuratezza e affiliazione",
            "contact_heading": "Contatto",
            "advertising_cookies": "Pubblicit\u00e0 e cookie",
            "user_choices": "Scelte utente",
        },
    }[locale]


LOCALIZED_CLASS_ROWS: Dict[str, List[Dict[str, str]]] = {
    "en": [
        {"name": "Vanguard", "fit": "Frontline control", "strength": "Safer trades and room entry", "watch": "Can overcommit when greedy"},
        {"name": "Seeker", "fit": "Scouting and mobility", "strength": "Information, repositioning, extraction timing", "watch": "Needs discipline in boss fights"},
        {"name": "Arcanist", "fit": "Burst windows", "strength": "High pressure when cooldowns align", "watch": "Punished by messy escapes"},
        {"name": "Warden", "fit": "Team stability", "strength": "Keeps runs recoverable", "watch": "Lower solo tempo"},
    ],
    "es": [
        {"name": "Vanguardia", "fit": "Control frontal", "strength": "Intercambios y entradas m\u00e1s seguros", "watch": "Puede comprometerse demasiado si juega agresivo"},
        {"name": "Explorador", "fit": "Exploraci\u00f3n y movilidad", "strength": "Informaci\u00f3n, reposicionamiento y tiempo de extracci\u00f3n", "watch": "Necesita disciplina contra jefes"},
        {"name": "Arcanista", "fit": "Ventanas de burst", "strength": "Alta presi\u00f3n cuando coinciden los enfriamientos", "watch": "Sufre en huidas desordenadas"},
        {"name": "Guardi\u00e1n", "fit": "Estabilidad del equipo", "strength": "Mantiene la run recuperable", "watch": "Menor ritmo en solo"},
    ],
    "ja": [
        {"name": "\u30f4\u30a1\u30f3\u30ac\u30fc\u30c9", "fit": "\u524d\u7dda\u5236\u5fa1", "strength": "\u90e8\u5c4b\u5165\u308a\u3068\u4ea4\u6226\u304c\u5b89\u5b9a", "watch": "\u653b\u3081\u3059\u304e\u308b\u3068\u6df1\u8ffd\u3044\u3057\u3084\u3059\u3044"},
        {"name": "\u30b7\u30fc\u30ab\u30fc", "fit": "\u7d22\u6575\u3068\u6a5f\u52d5\u529b", "strength": "\u60c5\u5831\u3001\u4f4d\u7f6e\u53d6\u308a\u3001\u62bd\u51fa\u30bf\u30a4\u30df\u30f3\u30b0", "watch": "\u30dc\u30b9\u6226\u3067\u306f\u5224\u65ad\u529b\u304c\u5fc5\u8981"},
        {"name": "\u30a2\u30eb\u30ab\u30cb\u30b9\u30c8", "fit": "\u77ac\u9593\u706b\u529b", "strength": "\u30af\u30fc\u30eb\u30c0\u30a6\u30f3\u304c\u5408\u3046\u3068\u9ad8\u5727\u529b", "watch": "\u9000\u907f\u304c\u4e71\u308c\u308b\u3068\u5f31\u3044"},
        {"name": "\u30a6\u30a9\u30fc\u30c7\u30f3", "fit": "\u30c1\u30fc\u30e0\u5b89\u5b9a", "strength": "\u30df\u30b9\u3092\u53d6\u308a\u623b\u3057\u3084\u3059\u3044", "watch": "\u30bd\u30ed\u306e\u30c6\u30f3\u30dd\u306f\u4f4e\u3081"},
    ],
}
LOCALIZED_CLASS_ROWS["fr"] = [
    {"name": "Avant-garde", "fit": "Contr\u00f4le de front", "strength": "\u00c9changes et entr\u00e9es plus s\u00fbrs", "watch": "Peut trop s'engager"},
    {"name": "\u00c9claireur", "fit": "Reconnaissance et mobilit\u00e9", "strength": "Information, repositionnement, timing d'extraction", "watch": "Demande de la discipline sur les boss"},
    {"name": "Arcaniste", "fit": "Fen\u00eatres de burst", "strength": "Forte pression quand les temps de recharge s'alignent", "watch": "Puni par les retraites confuses"},
    {"name": "Gardien", "fit": "Stabilit\u00e9 d'\u00e9quipe", "strength": "Garde la run r\u00e9cup\u00e9rable", "watch": "Tempo solo plus faible"},
]
LOCALIZED_CLASS_ROWS["de"] = [
    {"name": "Vorhut", "fit": "Frontkontrolle", "strength": "Sicherere Trades und Raumeinstiege", "watch": "Kann bei hohem Risiko \u00fcberziehen"},
    {"name": "Sucher", "fit": "Aufkl\u00e4rung und Mobilit\u00e4t", "strength": "Information, Positionswechsel, Extraktionszeit", "watch": "Braucht Disziplin bei Bossen"},
    {"name": "Arkanist", "fit": "Burst-Fenster", "strength": "Hoher Druck bei passenden Abklingzeiten", "watch": "Wird bei chaotischer Flucht bestraft"},
    {"name": "H\u00fcter", "fit": "Teamstabilit\u00e4t", "strength": "H\u00e4lt Runs rettbar", "watch": "Langsameres Solo-Tempo"},
]
LOCALIZED_CLASS_ROWS["pt"] = [
    {"name": "Vanguarda", "fit": "Controle da linha de frente", "strength": "Trocas e entradas mais seguras", "watch": "Pode avan\u00e7ar demais quando arriscado"},
    {"name": "Batedor", "fit": "Explora\u00e7\u00e3o e mobilidade", "strength": "Informa\u00e7\u00e3o, reposicionamento e tempo de extra\u00e7\u00e3o", "watch": "Exige disciplina contra chefes"},
    {"name": "Arcanista", "fit": "Janelas de burst", "strength": "Alta press\u00e3o quando recargas alinham", "watch": "Sofre em fugas confusas"},
    {"name": "Guard\u00e3o", "fit": "Estabilidade da equipe", "strength": "Mant\u00e9m a run recuper\u00e1vel", "watch": "Ritmo solo mais baixo"},
]
LOCALIZED_CLASS_ROWS["ko"] = [
    {"name": "\ubc45\uac00\ub4dc", "fit": "\uc804\uc120 \uc81c\uc5b4", "strength": "\uc548\uc815\uc801\uc778 \uad50\uc804\uacfc \ubc29 \uc9c4\uc785", "watch": "\uacf5\uaca9\uc801\uc77c \ub54c \ubb34\ub9ac\ud558\uae30 \uc26c\uc6c0"},
    {"name": "\uc2dc\ucee4", "fit": "\uc815\ucc30\uacfc \uae30\ub3d9\uc131", "strength": "\uc815\ubcf4, \uc7ac\ubc30\uce58, \ud0c8\ucd9c \ud0c0\uc774\ubc0d", "watch": "\ubcf4\uc2a4\uc804\uc5d0\uc11c \uc790\uc81c\uac00 \ud544\uc694"},
    {"name": "\uc544\uce74\ub2c8\uc2a4\ud2b8", "fit": "\uc21c\uac04 \ud654\ub825", "strength": "\ucfe8\ub2e4\uc6b4\uc774 \ub9de\uc744 \ub54c \ub192\uc740 \uc555\ubc15", "watch": "\ud0c8\ucd9c\uc774 \uc5c9\ud0a4\uba74 \ucde8\uc57d"},
    {"name": "\uc6cc\ub4e0", "fit": "\ud300 \uc548\uc815", "strength": "\ub7f0\uc744 \ubcf5\uad6c \uac00\ub2a5\ud558\uac8c \uc720\uc9c0", "watch": "\uc194\ub85c \ud15c\ud3ec\uac00 \ub0ae\uc74c"},
]
LOCALIZED_CLASS_ROWS["it"] = [
    {"name": "Avanguardia", "fit": "Controllo frontale", "strength": "Scambi e ingressi pi\u00f9 sicuri", "watch": "Pu\u00f2 esporsi troppo se gioca avido"},
    {"name": "Esploratore", "fit": "Ricognizione e mobilit\u00e0", "strength": "Informazioni, riposizionamento, timing di estrazione", "watch": "Richiede disciplina contro i boss"},
    {"name": "Arcanista", "fit": "Finestre di burst", "strength": "Alta pressione quando i cooldown coincidono", "watch": "Punito dalle fughe confuse"},
    {"name": "Custode", "fit": "Stabilit\u00e0 del team", "strength": "Mantiene recuperabile la run", "watch": "Ritmo solo pi\u00f9 basso"},
]


LOCALIZED_BUILD_PATTERNS: Dict[str, List[Dict[str, str]]] = {
    "en": [
        {"name": "Safe Extractor", "best": "Solo, early game, cautious players", "priorities": "Mobility, sustain, escape utility", "mistake": "Skipping exit tools for damage"},
        {"name": "Balanced Raider", "best": "Most mixed groups", "priorities": "Reliable weapon, one defensive layer, flexible utility", "mistake": "Duplicating the same team role"},
        {"name": "Boss Breaker", "best": "Planned boss pressure", "priorities": "Burst window, uptime, recovery option", "mistake": "Entering without a reset route"},
        {"name": "Scout Caller", "best": "Teams that need information", "priorities": "Vision, mobility, low-noise disengage", "mistake": "Fighting every contact"},
    ],
    "es": [
        {"name": "Extractor seguro", "best": "Solo, inicio, jugadores cautos", "priorities": "Movilidad, sost\u00e9n, herramientas de escape", "mistake": "Cambiar escape por da\u00f1o"},
        {"name": "Asaltante equilibrado", "best": "Grupos mixtos", "priorities": "Arma fiable, defensa y utilidad flexible", "mistake": "Duplicar el mismo rol"},
        {"name": "Rompejefes", "best": "Presi\u00f3n planificada a jefes", "priorities": "Ventana de burst, actividad, recuperaci\u00f3n", "mistake": "Entrar sin ruta de reinicio"},
        {"name": "L\u00edder explorador", "best": "Equipos que necesitan informaci\u00f3n", "priorities": "Visi\u00f3n, movilidad, retirada silenciosa", "mistake": "Pelear cada contacto"},
    ],
    "ja": [
        {"name": "\u5b89\u5168\u62bd\u51fa\u578b", "best": "\u30bd\u30ed\u3001\u5e8f\u76e4\u3001\u614e\u91cd\u306a\u30d7\u30ec\u30a4\u30e4\u30fc", "priorities": "\u6a5f\u52d5\u529b\u3001\u7dad\u6301\u529b\u3001\u9003\u8d70\u624b\u6bb5", "mistake": "\u706b\u529b\u306e\u305f\u3081\u306b\u8131\u51fa\u624b\u6bb5\u3092\u6368\u3066\u308b"},
        {"name": "\u30d0\u30e9\u30f3\u30b9\u30ec\u30a4\u30c0\u30fc", "best": "\u591a\u304f\u306e\u6df7\u6210\u30c1\u30fc\u30e0", "priorities": "\u4fe1\u983c\u3067\u304d\u308b\u6b66\u5668\u3001\u9632\u5fa1\u3001\u67d4\u8edf\u306a\u30e6\u30fc\u30c6\u30a3\u30ea\u30c6\u30a3", "mistake": "\u540c\u3058\u5f79\u5272\u3092\u91cd\u8907\u3055\u305b\u308b"},
        {"name": "\u30dc\u30b9\u30d6\u30ec\u30a4\u30ab\u30fc", "best": "\u8a08\u753b\u7684\u306a\u30dc\u30b9\u5727\u529b", "priorities": "\u77ac\u9593\u706b\u529b\u3001\u7d99\u6226\u3001\u56de\u5fa9\u624b\u6bb5", "mistake": "\u30ea\u30bb\u30c3\u30c8\u30eb\u30fc\u30c8\u306a\u3057\u3067\u5165\u308b"},
        {"name": "\u30b9\u30ab\u30a6\u30c8\u6307\u63ee", "best": "\u60c5\u5831\u304c\u5fc5\u8981\u306a\u30c1\u30fc\u30e0", "priorities": "\u8996\u754c\u3001\u6a5f\u52d5\u529b\u3001\u4f4e\u30ce\u30a4\u30ba\u96e2\u8131", "mistake": "\u63a5\u89e6\u3059\u3079\u3066\u3068\u6226\u3046"},
    ],
}
LOCALIZED_BUILD_PATTERNS["fr"] = [
    {"name": "Extracteur s\u00fbr", "best": "Solo, d\u00e9but, joueurs prudents", "priorities": "Mobilit\u00e9, sustain, outils d'\u00e9vasion", "mistake": "Sacrifier l'\u00e9vasion pour les d\u00e9g\u00e2ts"},
    {"name": "Raider \u00e9quilibr\u00e9", "best": "Groupes mixtes", "priorities": "Arme fiable, couche d\u00e9fensive, utilit\u00e9 flexible", "mistake": "Dupliquer le m\u00eame r\u00f4le"},
    {"name": "Briseur de boss", "best": "Pression planifi\u00e9e sur boss", "priorities": "Burst, uptime, option de r\u00e9cup\u00e9ration", "mistake": "Entrer sans route de r\u00e9cup\u00e9ration"},
    {"name": "Appel d'\u00e9claireur", "best": "\u00c9quipes qui ont besoin d'information", "priorities": "Vision, mobilit\u00e9, d\u00e9sengagement discret", "mistake": "Combattre chaque contact"},
]
LOCALIZED_BUILD_PATTERNS["de"] = [
    {"name": "Sicherer Extraktor", "best": "Solo, fr\u00fches Spiel, vorsichtige Spieler", "priorities": "Mobilit\u00e4t, Sustain, Fluchtwerkzeuge", "mistake": "Fluchtwerkzeuge f\u00fcr Schaden opfern"},
    {"name": "Ausgewogener Raider", "best": "Die meisten gemischten Gruppen", "priorities": "Zuverl\u00e4ssige Waffe, Verteidigung, flexible N\u00fctzlichkeit", "mistake": "Dieselbe Teamrolle doppeln"},
    {"name": "Bossbrecher", "best": "Geplanter Bossdruck", "priorities": "Burst-Fenster, Uptime, Erholung", "mistake": "Ohne Ausweichroute starten"},
    {"name": "Scout-Rufer", "best": "Teams mit Informationsbedarf", "priorities": "Sicht, Mobilit\u00e4t, leiser R\u00fcckzug", "mistake": "Jeden Kontakt bek\u00e4mpfen"},
]
LOCALIZED_BUILD_PATTERNS["pt"] = [
    {"name": "Extrator seguro", "best": "Solo, in\u00edcio, jogadores cautelosos", "priorities": "Mobilidade, sustenta\u00e7\u00e3o, fuga", "mistake": "Trocar ferramentas de sa\u00edda por dano"},
    {"name": "Raider equilibrado", "best": "Grupos mistos", "priorities": "Arma confi\u00e1vel, defesa, utilidade flex\u00edvel", "mistake": "Duplicar a mesma fun\u00e7\u00e3o"},
    {"name": "Quebra-chefe", "best": "Press\u00e3o planejada em chefe", "priorities": "Janela de burst, atividade, recupera\u00e7\u00e3o", "mistake": "Entrar sem rota de rein\u00edcio"},
    {"name": "Chamador batedor", "best": "Equipes que precisam de informa\u00e7\u00e3o", "priorities": "Vis\u00e3o, mobilidade, retirada discreta", "mistake": "Lutar contra todo contato"},
]
LOCALIZED_BUILD_PATTERNS["ko"] = [
    {"name": "\uc548\uc804 \ud0c8\ucd9c\ud615", "best": "\uc194\ub85c, \ucd08\ubc18, \uc2e0\uc911\ud55c \ud50c\ub808\uc774\uc5b4", "priorities": "\uae30\ub3d9\uc131, \uc720\uc9c0\ub825, \ud0c8\ucd9c \ub3c4\uad6c", "mistake": "\ud654\ub825\uc744 \uc704\ud574 \ud0c8\ucd9c \ub3c4\uad6c\ub97c \ud3ec\uae30"},
    {"name": "\uade0\ud615 \ub808\uc774\ub354", "best": "\ub300\ubd80\ubd84\uc758 \ud63c\ud569 \ud300", "priorities": "\uc2e0\ub8b0\ud560 \ubb34\uae30, \ubc29\uc5b4, \uc720\uc5f0\ud55c \uc720\ud2f8", "mistake": "\uac19\uc740 \ud300 \uc5ed\ud560 \uc911\ubcf5"},
    {"name": "\ubcf4\uc2a4 \ube0c\ub808\uc774\ucee4", "best": "\uacc4\ud68d\ub41c \ubcf4\uc2a4 \uc555\ubc15", "priorities": "\uc21c\uac04 \ud654\ub825, \uc9c0\uc18d\uc131, \ud68c\ubcf5 \uc218\ub2e8", "mistake": "\ub9ac\uc14b \uacbd\ub85c \uc5c6\uc774 \uc9c4\uc785"},
    {"name": "\uc2a4\uce74\uc6b0\ud2b8 \ucf5c\ub7ec", "best": "\uc815\ubcf4\uac00 \ud544\uc694\ud55c \ud300", "priorities": "\uc2dc\uc57c, \uae30\ub3d9\uc131, \uc800\uc18c\uc74c \uc774\ud0c8", "mistake": "\ubaa8\ub4e0 \uc811\ucd09\uacfc \uc804\ud22c"},
]
LOCALIZED_BUILD_PATTERNS["it"] = [
    {"name": "Estrattore sicuro", "best": "Solo, inizio, giocatori cauti", "priorities": "Mobilit\u00e0, sustain, fuga", "mistake": "Saltare strumenti di uscita per danni"},
    {"name": "Raider bilanciato", "best": "Gruppi misti", "priorities": "Arma affidabile, difesa, utilit\u00e0 flessibile", "mistake": "Duplicare lo stesso ruolo"},
    {"name": "Spezzaboss", "best": "Pressione boss pianificata", "priorities": "Finestra burst, uptime, recupero", "mistake": "Entrare senza rotta di recupero"},
    {"name": "Chiamata scout", "best": "Team che hanno bisogno di informazioni", "priorities": "Visione, mobilit\u00e0, disengage discreto", "mistake": "Combattere ogni contatto"},
]


STEPS = {
    "en": [
        "Pick the closest class identity before changing weapon style.",
        "Choose the run role that matches the party's actual job split.",
        "Keep risk balanced until your extraction path is repeatable.",
        "Revisit the planner after patch notes, weapon tuning, or new community tests.",
    ],
    "es": [
        "Elige la identidad de clase m\u00e1s cercana antes de cambiar el arma.",
        "Selecciona el rol que coincide con el reparto real del grupo.",
        "Mant\u00e9n el riesgo equilibrado hasta repetir la ruta de extracci\u00f3n.",
        "Revisa el planificador despu\u00e9s de parches, ajustes de armas o pruebas fiables.",
    ],
    "ja": [
        "\u6b66\u5668\u30b9\u30bf\u30a4\u30eb\u3092\u5909\u3048\u308b\u524d\u306b\u8fd1\u3044\u30af\u30e9\u30b9\u50cf\u3092\u9078\u3076\u3002",
        "\u30d1\u30fc\u30c6\u30a3\u306e\u5b9f\u969b\u306e\u5f79\u5272\u5206\u62c5\u306b\u5408\u3046\u30ed\u30fc\u30eb\u3092\u9078\u3076\u3002",
        "\u62bd\u51fa\u30eb\u30fc\u30c8\u3092\u518d\u73fe\u3067\u304d\u308b\u307e\u3067\u30ea\u30b9\u30af\u306f\u30d0\u30e9\u30f3\u30b9\u306b\u3059\u308b\u3002",
        "\u30d1\u30c3\u30c1\u3001\u6b66\u5668\u8abf\u6574\u3001\u65b0\u3057\u3044\u691c\u8a3c\u5f8c\u306b\u518d\u8a55\u4fa1\u3059\u308b\u3002",
    ],
    "fr": [
        "Choisissez l'identit\u00e9 de classe la plus proche avant de changer d'arme.",
        "Choisissez le r\u00f4le qui correspond au vrai partage du groupe.",
        "Gardez un risque \u00e9quilibr\u00e9 tant que la route d'extraction n'est pas r\u00e9p\u00e9table.",
        "Revenez au planificateur apr\u00e8s les patchs, r\u00e9glages d'armes ou tests fiables.",
    ],
    "de": [
        "W\u00e4hle zuerst die passende Klassenidentit\u00e4t, bevor du den Waffenstil \u00e4nderst.",
        "W\u00e4hle die Run-Rolle passend zur echten Aufgabenverteilung.",
        "Halte das Risiko ausgewogen, bis deine Extraktionsroute wiederholbar ist.",
        "Pr\u00fcfe den Planer nach Patches, Waffen-Tuning oder neuen Tests erneut.",
    ],
    "pt": [
        "Escolha a identidade de classe mais pr\u00f3xima antes de trocar o estilo de arma.",
        "Escolha a fun\u00e7\u00e3o que combina com a divis\u00e3o real do grupo.",
        "Mantenha o risco equilibrado at\u00e9 a rota de extra\u00e7\u00e3o ser repet\u00edvel.",
        "Reveja o planejador ap\u00f3s patches, ajustes de armas ou testes confi\u00e1veis.",
    ],
    "ko": [
        "\ubb34\uae30 \uc2a4\ud0c0\uc77c\uc744 \ubc14\uafb8\uae30 \uc804\uc5d0 \uac00\uc7a5 \uac00\uae4c\uc6b4 \ud074\ub798\uc2a4 \uc815\uccb4\uc131\uc744 \uace0\ub974\uc138\uc694.",
        "\ud30c\ud2f0\uc758 \uc2e4\uc81c \uc5ed\ud560 \ubd84\ub2f4\uc5d0 \ub9de\ub294 \ub7f0 \uc5ed\ud560\uc744 \uc120\ud0dd\ud558\uc138\uc694.",
        "\ud0c8\ucd9c \uacbd\ub85c\uac00 \ubc18\ubcf5 \uac00\ub2a5\ud560 \ub54c\uae4c\uc9c0 \uc704\ud5d8\ub3c4\ub294 \uade0\ud615\uc73c\ub85c \uc720\uc9c0\ud558\uc138\uc694.",
        "\ud328\uce58, \ubb34\uae30 \uc870\uc815, \uc2e0\ub8b0\ud560 \ud14c\uc2a4\ud2b8 \ud6c4 \ud50c\ub798\ub108\ub97c \ub2e4\uc2dc \ud655\uc778\ud558\uc138\uc694.",
    ],
    "it": [
        "Scegli prima l'identit\u00e0 di classe pi\u00f9 vicina, poi cambia stile arma.",
        "Scegli il ruolo che corrisponde alla vera divisione del gruppo.",
        "Mantieni il rischio bilanciato finch\u00e9 la rotta di estrazione \u00e8 ripetibile.",
        "Rivedi il planner dopo patch, tuning armi o nuovi test affidabili.",
    ],
}


DEEP_GUIDE = {
    "en": [
        "A useful Mistfall Hunter loadout starts with the job of the run, not with the flashiest weapon. If the goal is a steady extraction, the first question is how the build leaves a bad room, resets a fight, or protects the player who is carrying important loot.",
        "For solo runs, the planner weights mobility and recovery higher because a solo player has no teammate to stabilize a mistake. For team runs, role overlap is the common mistake, so each player should own a clear job.",
        "Risk level should change after evidence, not mood. Safe is best when learning maps, balanced is the default for repeatable farming, and greedy only fits a scouted route with a known exit.",
        "After a few runs, keep a simple note beside each build: class, weapon style, objective, death cause, extraction result, and one change to test next.",
    ],
    "es": [
        "Un loadout \u00fatil empieza por el trabajo de la run, no por el arma m\u00e1s vistosa. Si la meta es extraer de forma estable, pregunta primero c\u00f3mo la build sale de una sala mala o protege el bot\u00edn.",
        "En solo pesan m\u00e1s movilidad y recuperaci\u00f3n porque no hay compa\u00f1ero que corrija errores. En equipo, el fallo com\u00fan es repetir roles, as\u00ed que cada jugador necesita una tarea clara.",
        "El riesgo debe cambiar por evidencia, no por impulso. Seguro sirve para aprender mapas, equilibrado para farmear y agresivo solo para rutas exploradas.",
        "Despu\u00e9s de varias runs, anota clase, arma, objetivo, causa de muerte, resultado de extracci\u00f3n y un cambio para probar.",
    ],
    "ja": [
        "\u5b9f\u7528\u7684\u306a\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u306f\u3001\u76ee\u7acb\u3064\u6b66\u5668\u3067\u306f\u306a\u304f\u30e9\u30f3\u306e\u76ee\u7684\u304b\u3089\u59cb\u307e\u308a\u307e\u3059\u3002\u5b89\u5b9a\u62bd\u51fa\u304c\u76ee\u6a19\u306a\u3089\u3001\u5371\u967a\u306a\u90e8\u5c4b\u304b\u3089\u96e2\u8131\u3067\u304d\u308b\u304b\u3092\u5148\u306b\u898b\u307e\u3059\u3002",
        "\u30bd\u30ed\u3067\u306f\u30df\u30b9\u3092\u30ab\u30d0\u30fc\u3059\u308b\u4ef2\u9593\u304c\u3044\u306a\u3044\u305f\u3081\u3001\u6a5f\u52d5\u529b\u3068\u56de\u5fa9\u529b\u3092\u91cd\u304f\u898b\u307e\u3059\u3002\u30c1\u30fc\u30e0\u3067\u306f\u5f79\u5272\u91cd\u8907\u3092\u907f\u3051\u307e\u3059\u3002",
        "\u30ea\u30b9\u30af\u306f\u6c17\u5206\u3067\u306f\u306a\u304f\u691c\u8a3c\u7d50\u679c\u3067\u5909\u3048\u307e\u3059\u3002\u5b89\u5168\u306f\u5730\u56f3\u5b66\u7fd2\u3001\u30d0\u30e9\u30f3\u30b9\u306f\u5468\u56de\u3001\u653b\u3081\u91cd\u8996\u306f\u5075\u5bdf\u6e08\u307f\u30eb\u30fc\u30c8\u5411\u3051\u3067\u3059\u3002",
        "\u6570\u56de\u30d7\u30ec\u30a4\u3057\u305f\u3089\u3001\u30af\u30e9\u30b9\u3001\u6b66\u5668\u3001\u76ee\u6a19\u3001\u5931\u6557\u539f\u56e0\u3001\u62bd\u51fa\u7d50\u679c\u3001\u6b21\u306b\u8a66\u3059\u5909\u66f4\u3092\u30e1\u30e2\u3057\u307e\u3059\u3002",
    ],
    "fr": [
        "Un loadout utile part du travail de la run, pas de l'arme la plus visible. Pour une extraction stable, demandez d'abord comment quitter une mauvaise salle ou prot\u00e9ger le butin.",
        "En solo, la mobilit\u00e9 et la r\u00e9cup\u00e9ration comptent davantage. En \u00e9quipe, l'erreur courante est le chevauchement des r\u00f4les.",
        "Le risque doit changer avec les preuves, pas avec l'humeur. S\u00fbr pour apprendre, \u00e9quilibr\u00e9 pour farmer, agressif seulement sur une route connue.",
        "Apr\u00e8s quelques runs, notez classe, arme, objectif, cause de mort, r\u00e9sultat d'extraction et prochain test.",
    ],
    "de": [
        "Ein n\u00fctzliches Loadout beginnt mit der Aufgabe des Runs, nicht mit der auff\u00e4lligsten Waffe. F\u00fcr stabile Extraktion z\u00e4hlt zuerst der Ausweg aus schlechten R\u00e4umen.",
        "Solo wiegen Mobilit\u00e4t und Erholung schwerer. Im Team ist doppelte Rollenverteilung der h\u00e4ufige Fehler.",
        "Risiko sollte sich nach Belegen \u00e4ndern, nicht nach Laune. Sicher zum Lernen, ausgewogen zum Farmen, riskant nur auf bekannter Route.",
        "Notiere nach einigen Runs Klasse, Waffe, Ziel, Todesursache, Extraktionsergebnis und den n\u00e4chsten Test.",
    ],
    "pt": [
        "Um loadout \u00fatil come\u00e7a pela fun\u00e7\u00e3o da run, n\u00e3o pela arma mais chamativa. Para extrair com estabilidade, veja primeiro como sair de uma sala ruim ou proteger o loot.",
        "No solo, mobilidade e recupera\u00e7\u00e3o pesam mais. Em equipe, o erro comum \u00e9 repetir fun\u00e7\u00f5es.",
        "O risco deve mudar com evid\u00eancia, n\u00e3o com impulso. Seguro para aprender, equilibrado para farmar, arriscado s\u00f3 em rota conhecida.",
        "Depois de algumas runs, anote classe, arma, objetivo, causa da morte, resultado da extra\u00e7\u00e3o e o pr\u00f3ximo teste.",
    ],
    "ko": [
        "\uc88b\uc740 \ub85c\ub4dc\uc544\uc6c3\uc740 \ud654\ub824\ud55c \ubb34\uae30\uac00 \uc544\ub2c8\ub77c \ub7f0\uc758 \uc784\ubb34\uc5d0\uc11c \uc2dc\uc791\ud569\ub2c8\ub2e4. \uc548\uc815\uc801 \ud0c8\ucd9c\uc774 \ubaa9\ud45c\ub77c\uba74 \uba3c\uc800 \uc704\ud5d8\ud55c \ubc29\uc744 \ub5a0\ub098\ub294 \ubc29\ubc95\uc744 \ubcf4\uc138\uc694.",
        "\uc194\ub85c\uc5d0\uc11c\ub294 \uae30\ub3d9\uc131\uacfc \ud68c\ubcf5\uc774 \ub354 \uc911\uc694\ud569\ub2c8\ub2e4. \ud300\uc5d0\uc11c\ub294 \uc5ed\ud560 \uc911\ubcf5\uc774 \uac00\uc7a5 \ud754\ud55c \uc2e4\uc218\uc785\ub2c8\ub2e4.",
        "\uc704\ud5d8\ub3c4\ub294 \uae30\ubd84\uc774 \uc544\ub2c8\ub77c \uadfc\uac70\uc5d0 \ub530\ub77c \ubc14\uafd4\uc57c \ud569\ub2c8\ub2e4. \uc548\uc804\uc740 \ud559\uc2b5, \uade0\ud615\uc740 \ubc18\ubcf5 \ud30c\ubc0d, \uacf5\uaca9\uc801\uc778 \uc120\ud0dd\uc740 \uc815\ucc30\ub41c \uacbd\ub85c\uc5d0 \ub9de\uc2b5\ub2c8\ub2e4.",
        "\uba87 \ubc88\uc758 \ub7f0 \ud6c4 \ud074\ub798\uc2a4, \ubb34\uae30, \ubaa9\ud45c, \uc0ac\ub9dd \uc6d0\uc778, \ud0c8\ucd9c \uacb0\uacfc, \ub2e4\uc74c \ud14c\uc2a4\ud2b8\ub97c \uba54\ubaa8\ud558\uc138\uc694.",
    ],
    "it": [
        "Un loadout utile parte dal compito della run, non dall'arma pi\u00f9 vistosa. Per un'estrazione stabile conta prima come uscire da una stanza pericolosa.",
        "In solo pesano di pi\u00f9 mobilit\u00e0 e recupero. In team l'errore comune \u00e8 sovrapporre i ruoli.",
        "Il rischio deve cambiare con le prove, non con l'umore. Sicuro per imparare, bilanciato per farmare, avido solo su rotte note.",
        "Dopo alcune run, annota classe, arma, obiettivo, causa della morte, risultato di estrazione e prossimo test.",
    ],
}


FAQ_ITEMS = {
    "en": [
        ("What is the best Mistfall Hunter loadout?", "The safest answer depends on class, team role, and risk level. Start with Balanced Raider, then shift when your goal changes."),
        ("Does this planner use official damage numbers?", "No. It uses public launch-week research and transparent assumptions until official values or reliable tests appear."),
        ("Which Mistfall Hunter class should beginners choose?", "Beginners usually benefit from a safer class plan that protects extraction timing before chasing maximum burst."),
        ("Is Mistfall Hunter better solo or in a team?", "Solo rewards mobility and safe exits. Team play rewards role clarity and support coverage."),
        ("How often should loadouts change?", "Review loadouts after patches, new weapons, class tuning, or a change in party role."),
        ("Can I copy the result?", "Yes. Use the copy button to save a compact loadout note for your next run."),
    ],
    "es": [
        ("\u00bfCu\u00e1l es el mejor loadout de Mistfall Hunter?", "Depende de clase, rol y riesgo. Empieza equilibrado y cambia cuando cambie el objetivo."),
        ("\u00bfUsa n\u00fameros oficiales de da\u00f1o?", "No. Usa investigaci\u00f3n p\u00fablica e hip\u00f3tesis claras hasta que existan valores oficiales o pruebas fiables."),
        ("\u00bfQu\u00e9 clase conviene a principiantes?", "Suele convenir un plan seguro que proteja la extracci\u00f3n antes de buscar burst m\u00e1ximo."),
        ("\u00bfEs mejor jugar solo o en equipo?", "Solo premia movilidad y salidas seguras. En equipo importan roles claros y cobertura."),
        ("\u00bfCada cu\u00e1nto cambiar loadouts?", "Revisa despu\u00e9s de parches, armas nuevas, ajustes de clase o cambios de rol."),
        ("\u00bfPuedo copiar el resultado?", "S\u00ed. Usa el bot\u00f3n de copiar para guardar una nota compacta."),
    ],
    "ja": [
        ("Mistfall Hunter \u306e\u6700\u9069\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u306f\uff1f", "\u30af\u30e9\u30b9\u3001\u5f79\u5272\u3001\u30ea\u30b9\u30af\u3067\u5909\u308f\u308a\u307e\u3059\u3002\u307e\u305a\u30d0\u30e9\u30f3\u30b9\u578b\u304b\u3089\u59cb\u3081\u307e\u3057\u3087\u3046\u3002"),
        ("\u516c\u5f0f\u30c0\u30e1\u30fc\u30b8\u6570\u5024\u3092\u4f7f\u3063\u3066\u3044\u307e\u3059\u304b\uff1f", "\u3044\u3044\u3048\u3002\u516c\u958b\u60c5\u5831\u3068\u900f\u660e\u306a\u4eee\u8aac\u3092\u4f7f\u3044\u307e\u3059\u3002"),
        ("\u521d\u5fc3\u8005\u5411\u3051\u306e\u30af\u30e9\u30b9\u306f\uff1f", "\u62bd\u51fa\u30bf\u30a4\u30df\u30f3\u30b0\u3092\u5b88\u308c\u308b\u5b89\u5168\u578b\u304c\u5411\u3044\u3066\u3044\u307e\u3059\u3002"),
        ("\u30bd\u30ed\u3068\u30c1\u30fc\u30e0\u306f\u3069\u3061\u3089\u304c\u826f\u3044\uff1f", "\u30bd\u30ed\u306f\u6a5f\u52d5\u529b\u3068\u8131\u51fa\u3001\u30c1\u30fc\u30e0\u306f\u5f79\u5272\u5206\u62c5\u304c\u91cd\u8981\u3067\u3059\u3002"),
        ("\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u306f\u3044\u3064\u898b\u76f4\u3059\uff1f", "\u30d1\u30c3\u30c1\u3001\u65b0\u6b66\u5668\u3001\u30af\u30e9\u30b9\u8abf\u6574\u3001\u5f79\u5272\u5909\u66f4\u306e\u5f8c\u3067\u3059\u3002"),
        ("\u7d50\u679c\u3092\u30b3\u30d4\u30fc\u3067\u304d\u307e\u3059\u304b\uff1f", "\u306f\u3044\u3002\u30b3\u30d4\u30fc\u30dc\u30bf\u30f3\u3067\u6b21\u306e\u30e9\u30f3\u7528\u306e\u30e1\u30e2\u3092\u4fdd\u5b58\u3067\u304d\u307e\u3059\u3002"),
    ],
}
FAQ_ITEMS["fr"] = [
    ("Quel est le meilleur loadout Mistfall Hunter ?", "Il d\u00e9pend de la classe, du r\u00f4le et du risque. Commencez \u00e9quilibr\u00e9 puis adaptez."),
    ("Le planificateur utilise-t-il des chiffres officiels ?", "Non. Il utilise des recherches publiques et des hypoth\u00e8ses claires."),
    ("Quelle classe pour d\u00e9buter ?", "Un plan s\u00fbr qui prot\u00e8ge l'extraction est souvent le meilleur d\u00e9part."),
    ("Solo ou \u00e9quipe ?", "Solo r\u00e9compense la mobilit\u00e9. L'\u00e9quipe r\u00e9compense les r\u00f4les clairs."),
    ("Quand changer de loadout ?", "Apr\u00e8s les patchs, nouvelles armes, r\u00e9glages de classe ou changements de r\u00f4le."),
    ("Puis-je copier le r\u00e9sultat ?", "Oui, le bouton de copie enregistre une note compacte."),
]
FAQ_ITEMS["de"] = [
    ("Was ist das beste Mistfall Hunter Loadout?", "Es h\u00e4ngt von Klasse, Rolle und Risiko ab. Starte ausgewogen und passe an."),
    ("Nutzt der Planer offizielle Schadenszahlen?", "Nein. Er nutzt \u00f6ffentliche Recherche und klare Annahmen."),
    ("Welche Klasse ist f\u00fcr Einsteiger gut?", "Ein sicherer Plan, der die Extraktion sch\u00fctzt, ist meist besser als maximaler Burst."),
    ("Solo oder Team?", "Solo belohnt Mobilit\u00e4t, Teamspiel belohnt klare Rollen."),
    ("Wann sollte ein Loadout wechseln?", "Nach Patches, neuen Waffen, Klassen-Tuning oder Rollenwechsel."),
    ("Kann ich das Ergebnis kopieren?", "Ja, die Kopier-Schaltfl\u00e4che speichert eine kurze Notiz."),
]
FAQ_ITEMS["pt"] = [
    ("Qual \u00e9 o melhor loadout de Mistfall Hunter?", "Depende da classe, fun\u00e7\u00e3o e risco. Comece equilibrado e ajuste."),
    ("O planejador usa n\u00fameros oficiais?", "N\u00e3o. Ele usa pesquisa p\u00fablica e premissas transparentes."),
    ("Qual classe \u00e9 melhor para iniciantes?", "Um plano seguro que protege a extra\u00e7\u00e3o costuma ser melhor."),
    ("Solo ou equipe?", "Solo recompensa mobilidade; equipe recompensa fun\u00e7\u00f5es claras."),
    ("Quando mudar loadouts?", "Depois de patches, novas armas, ajustes de classe ou mudan\u00e7a de fun\u00e7\u00e3o."),
    ("Posso copiar o resultado?", "Sim, o bot\u00e3o copia uma nota compacta."),
]
FAQ_ITEMS["ko"] = [
    ("Mistfall Hunter \ucd5c\uace0\uc758 \ub85c\ub4dc\uc544\uc6c3\uc740?", "\ud074\ub798\uc2a4, \uc5ed\ud560, \uc704\ud5d8\ub3c4\uc5d0 \ub530\ub77c \ub2e4\ub985\ub2c8\ub2e4. \uba3c\uc800 \uade0\ud615\ud615\uc73c\ub85c \uc2dc\uc791\ud558\uc138\uc694."),
    ("\uacf5\uc2dd \ud53c\ud574\ub7c9\uc744 \uc0ac\uc6a9\ud558\ub098\uc694?", "\uc544\ub2c8\uc694. \uacf5\uac1c \uc870\uc0ac\uc640 \uba85\ud655\ud55c \uac00\uc815\uc744 \uc0ac\uc6a9\ud569\ub2c8\ub2e4."),
    ("\ucd08\ubcf4\uc790\uc5d0\uac8c \uc88b\uc740 \ud074\ub798\uc2a4\ub294?", "\ud0c8\ucd9c \ud0c0\uc774\ubc0d\uc744 \ubcf4\ud638\ud558\ub294 \uc548\uc804\ud55c \ud074\ub798\uc2a4 \uacc4\ud68d\uc774 \uc88b\uc2b5\ub2c8\ub2e4."),
    ("\uc194\ub85c\uc640 \ud300 \uc911 \ubb34\uc5c7\uc774 \ub354 \uc88b\ub098\uc694?", "\uc194\ub85c\ub294 \uae30\ub3d9\uc131, \ud300\uc740 \uba85\ud655\ud55c \uc5ed\ud560\uc744 \ubcf4\uc0c1\ud569\ub2c8\ub2e4."),
    ("\ub85c\ub4dc\uc544\uc6c3\uc740 \uc5b8\uc81c \ubc14\uafb8\ub098\uc694?", "\ud328\uce58, \uc0c8 \ubb34\uae30, \ud074\ub798\uc2a4 \uc870\uc815, \ud30c\ud2f0 \uc5ed\ud560 \ubcc0\uacbd \ud6c4\uc785\ub2c8\ub2e4."),
    ("\uacb0\uacfc\ub97c \ubcf5\uc0ac\ud560 \uc218 \uc788\ub098\uc694?", "\ub124. \ubcf5\uc0ac \ubc84\ud2bc\uc73c\ub85c \uc9e7\uc740 \uba54\ubaa8\ub97c \uc800\uc7a5\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4."),
]
FAQ_ITEMS["it"] = [
    ("Qual \u00e8 il miglior loadout di Mistfall Hunter?", "Dipende da classe, ruolo e rischio. Inizia bilanciato e poi adatta."),
    ("Il planner usa numeri ufficiali?", "No. Usa ricerca pubblica e ipotesi trasparenti."),
    ("Quale classe per principianti?", "Un piano sicuro che protegge l'estrazione \u00e8 spesso migliore."),
    ("Meglio solo o in team?", "Solo premia mobilit\u00e0 e uscite sicure. Il team premia ruoli chiari."),
    ("Quando cambiare loadout?", "Dopo patch, nuove armi, tuning classe o cambio ruolo."),
    ("Posso copiare il risultato?", "S\u00ec, il pulsante copia una nota compatta."),
]


LEGAL_BODY: Dict[str, Dict[str, str]] = {
    "en": {
        "scope": "Mistfall Loadouts publishes independent planning guidance for Mistfall Hunter loadouts, classes, builds, and route decisions. The site avoids account features and does not ask for passwords, game credentials, payment details, or private profile data.",
        "advertising": "If advertising is enabled in the future, third-party vendors including Google may use cookies, web beacons, IP addresses, browser details, and similar signals to serve, measure, and protect ads. The planner does not request account logins, payment details, or private profile data.",
        "choices": "Visitors can manage cookies in their browser settings. If a consent banner or regional privacy control becomes required for a market, the site should enable that control before serving personalized ads in that market.",
        "data": "The planner runs in the browser and uses only the options selected on the page. No personal account is required. Basic server and CDN logs may exist at hosting providers for security and reliability.",
        "accuracy": "Loadout recommendations are editorial planning aids based on public launch-week research and transparent assumptions. Mistfall Loadouts is not affiliated with the official publisher or developer.",
        "contact": "For corrections, source updates, or policy questions, contact hello@mistfallloadouts.blog.",
    },
    "es": {
        "scope": "Mistfall Loadouts publica orientacion independiente para loadouts, clases, builds y rutas de Mistfall Hunter. El sitio no usa cuentas y no solicita contrasenas, credenciales del juego, pagos ni datos privados de perfil.",
        "advertising": "Si se activan anuncios en el futuro, proveedores externos como Google pueden usar cookies, balizas web, direcciones IP, datos del navegador y senales similares para publicar, medir y proteger anuncios. El planificador no solicita inicios de sesion, pagos ni perfiles privados.",
        "choices": "Los visitantes pueden gestionar cookies desde el navegador. Si un mercado requiere banner de consentimiento o control regional, el sitio debe activarlo antes de mostrar anuncios personalizados alli.",
        "data": "El planificador funciona en el navegador y solo usa las opciones seleccionadas en la pagina. No hace falta cuenta personal. Los proveedores de hosting o CDN pueden conservar registros basicos por seguridad y fiabilidad.",
        "accuracy": "Las recomendaciones de loadout son ayuda editorial basada en investigacion publica de lanzamiento y supuestos transparentes. Mistfall Loadouts no esta afiliado al editor ni al desarrollador oficial.",
        "contact": "Para correcciones, fuentes nuevas o dudas de politica, contacta con hello@mistfallloadouts.blog.",
    },
    "ja": {
        "scope": "Mistfall Loadouts \u306f Mistfall Hunter \u306e\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u3001\u30af\u30e9\u30b9\u3001\u30d3\u30eb\u30c9\u3001\u30eb\u30fc\u30c8\u5224\u65ad\u306b\u95a2\u3059\u308b\u72ec\u7acb\u3057\u305f\u8a08\u753b\u30ac\u30a4\u30c9\u3092\u63b2\u8f09\u3057\u307e\u3059\u3002\u30a2\u30ab\u30a6\u30f3\u30c8\u6a5f\u80fd\u306f\u306a\u304f\u3001\u30d1\u30b9\u30ef\u30fc\u30c9\u3001\u30b2\u30fc\u30e0\u8a8d\u8a3c\u60c5\u5831\u3001\u652f\u6255\u3044\u60c5\u5831\u3001\u975e\u516c\u958b\u30d7\u30ed\u30d5\u30a3\u30fc\u30eb\u60c5\u5831\u306f\u6c42\u3081\u307e\u305b\u3093\u3002",
        "advertising": "\u5c06\u6765\u5e83\u544a\u3092\u6709\u52b9\u306b\u3059\u308b\u5834\u5408\u3001Google \u3092\u542b\u3080\u7b2c\u4e09\u8005\u4e8b\u696d\u8005\u304c Cookie\u3001Web \u30d3\u30fc\u30b3\u30f3\u3001IP \u30a2\u30c9\u30ec\u30b9\u3001\u30d6\u30e9\u30a6\u30b6\u60c5\u5831\u306a\u3069\u3092\u5e83\u544a\u914d\u4fe1\u30fb\u6e2c\u5b9a\u30fb\u4fdd\u8b77\u306b\u4f7f\u3046\u3053\u3068\u304c\u3042\u308a\u307e\u3059\u3002\u30d7\u30e9\u30f3\u30ca\u30fc\u306f\u30ed\u30b0\u30a4\u30f3\u3001\u652f\u6255\u3044\u3001\u975e\u516c\u958b\u30d7\u30ed\u30d5\u30a3\u30fc\u30eb\u3092\u8981\u6c42\u3057\u307e\u305b\u3093\u3002",
        "choices": "\u8a2a\u554f\u8005\u306f\u30d6\u30e9\u30a6\u30b6\u8a2d\u5b9a\u3067 Cookie \u3092\u7ba1\u7406\u3067\u304d\u307e\u3059\u3002\u5730\u57df\u898f\u5236\u306b\u3088\u308a\u540c\u610f\u30d0\u30ca\u30fc\u3084\u30d7\u30e9\u30a4\u30d0\u30b7\u30fc\u5236\u5fa1\u304c\u5fc5\u8981\u306a\u5834\u5408\u306f\u3001\u500b\u5225\u5316\u5e83\u544a\u306e\u524d\u306b\u6709\u52b9\u5316\u3057\u307e\u3059\u3002",
        "data": "\u30d7\u30e9\u30f3\u30ca\u30fc\u306f\u30d6\u30e9\u30a6\u30b6\u5185\u3067\u52d5\u4f5c\u3057\u3001\u30da\u30fc\u30b8\u4e0a\u3067\u9078\u3093\u3060\u9805\u76ee\u3060\u3051\u3092\u4f7f\u3044\u307e\u3059\u3002\u500b\u4eba\u30a2\u30ab\u30a6\u30f3\u30c8\u306f\u4e0d\u8981\u3067\u3059\u3002\u30db\u30b9\u30c6\u30a3\u30f3\u30b0\u3084 CDN \u306b\u306f\u30bb\u30ad\u30e5\u30ea\u30c6\u30a3\u3068\u4fe1\u983c\u6027\u306e\u305f\u3081\u306e\u57fa\u672c\u30ed\u30b0\u304c\u6b8b\u308b\u5834\u5408\u304c\u3042\u308a\u307e\u3059\u3002",
        "accuracy": "\u30ed\u30fc\u30c9\u30a2\u30a6\u30c8\u63a8\u5968\u306f\u3001\u516c\u958b\u3055\u308c\u305f\u30ed\u30fc\u30f3\u30c1\u9031\u7814\u7a76\u3068\u900f\u660e\u306a\u4eee\u8aac\u306b\u57fa\u3065\u304f\u7de8\u96c6\u4e0a\u306e\u8a08\u753b\u652f\u63f4\u3067\u3059\u3002Mistfall Loadouts \u306f\u516c\u5f0f\u30d1\u30d6\u30ea\u30c3\u30b7\u30e3\u30fc\u3084\u958b\u767a\u5143\u3068\u63d0\u643a\u3057\u3066\u3044\u307e\u305b\u3093\u3002",
        "contact": "\u4fee\u6b63\u3001\u60c5\u5831\u66f4\u65b0\u3001\u30dd\u30ea\u30b7\u30fc\u306b\u95a2\u3059\u308b\u9023\u7d61\u306f hello@mistfallloadouts.blog \u307e\u3067\u304a\u9001\u308a\u304f\u3060\u3055\u3044\u3002",
    },
    "fr": {
        "scope": "Mistfall Loadouts publie des conseils independants pour les loadouts, classes, builds et choix de route de Mistfall Hunter. Le site evite les comptes et ne demande pas de mots de passe, identifiants de jeu, donnees de paiement ni profils prives.",
        "advertising": "Si la publicite est activee plus tard, des fournisseurs tiers comme Google peuvent utiliser cookies, balises web, adresses IP, details du navigateur et signaux similaires pour diffuser, mesurer et proteger les annonces. Le planificateur ne demande pas de connexion, paiement ou profil prive.",
        "choices": "Les visiteurs peuvent gerer les cookies dans leur navigateur. Si un marche exige un bandeau de consentement ou un controle regional, le site doit l'activer avant toute publicite personnalisee.",
        "data": "Le planificateur fonctionne dans le navigateur et utilise seulement les options choisies sur la page. Aucun compte personnel n'est requis. Des journaux de serveur ou CDN peuvent exister pour la securite et la fiabilite.",
        "accuracy": "Les recommandations de loadout sont des aides editoriales fondees sur des recherches publiques de lancement et des hypotheses transparentes. Mistfall Loadouts n'est pas affilie a l'editeur ou au developpeur officiel.",
        "contact": "Pour corrections, mises a jour de sources ou questions de politique, contactez hello@mistfallloadouts.blog.",
    },
    "de": {
        "scope": "Mistfall Loadouts veroffentlicht unabhangige Planungshilfen fur Mistfall Hunter Loadouts, Klassen, Builds und Routenentscheidungen. Die Seite nutzt keine Kontofunktionen und fragt nicht nach Passwortern, Spielzugangen, Zahlungsdaten oder privaten Profildaten.",
        "advertising": "Falls spater Werbung aktiviert wird, konnen Drittanbieter wie Google Cookies, Web-Beacons, IP-Adressen, Browserdaten und ahnliche Signale zur Auslieferung, Messung und Absicherung von Anzeigen verwenden. Der Planer fragt keine Logins, Zahlungsdaten oder privaten Profile ab.",
        "choices": "Besucher konnen Cookies in ihren Browsereinstellungen verwalten. Wenn ein Markt ein Zustimmungsbanner oder regionale Datenschutzsteuerung erfordert, sollte die Seite dies vor personalisierter Werbung aktivieren.",
        "data": "Der Planer lauft im Browser und nutzt nur die auf der Seite ausgewahlten Optionen. Ein personliches Konto ist nicht erforderlich. Hosting- und CDN-Anbieter konnen Basisprotokolle fur Sicherheit und Zuverlassigkeit speichern.",
        "accuracy": "Loadout-Empfehlungen sind redaktionelle Planungshilfen auf Basis offentlicher Launch-Recherche und transparenter Annahmen. Mistfall Loadouts ist nicht mit dem offiziellen Publisher oder Entwickler verbunden.",
        "contact": "Fur Korrekturen, Quellenupdates oder Richtlinienfragen: hello@mistfallloadouts.blog.",
    },
    "pt": {
        "scope": "Mistfall Loadouts publica orientacao independente para loadouts, classes, builds e rotas de Mistfall Hunter. O site nao usa contas e nao pede senhas, credenciais do jogo, dados de pagamento ou perfis privados.",
        "advertising": "Se anuncios forem ativados no futuro, fornecedores terceiros como Google podem usar cookies, web beacons, enderecos IP, dados do navegador e sinais semelhantes para veicular, medir e proteger anuncios. O planejador nao solicita login, pagamento ou perfil privado.",
        "choices": "Visitantes podem gerenciar cookies nas configuracoes do navegador. Se um mercado exigir banner de consentimento ou controle regional, o site deve ativar isso antes de anuncios personalizados.",
        "data": "O planejador roda no navegador e usa apenas as opcoes escolhidas na pagina. Nenhuma conta pessoal e necessaria. Provedores de hospedagem e CDN podem manter logs basicos por seguranca e confiabilidade.",
        "accuracy": "As recomendacoes de loadout sao auxilios editoriais baseados em pesquisa publica de lancamento e premissas transparentes. Mistfall Loadouts nao e afiliado ao editor ou desenvolvedor oficial.",
        "contact": "Para correcoes, atualizacoes de fonte ou questoes de politica, contate hello@mistfallloadouts.blog.",
    },
    "ko": {
        "scope": "Mistfall Loadouts\ub294 Mistfall Hunter \ub85c\ub4dc\uc544\uc6c3, \ud074\ub798\uc2a4, \ube4c\ub4dc, \uacbd\ub85c \ud310\ub2e8\uc744 \uc704\ud55c \ub3c5\ub9bd \uacc4\ud68d \uac00\uc774\ub4dc\ub97c \uac8c\uc2dc\ud569\ub2c8\ub2e4. \uc0ac\uc774\ud2b8\ub294 \uacc4\uc815 \uae30\ub2a5\uc744 \uc0ac\uc6a9\ud558\uc9c0 \uc54a\uace0 \ube44\ubc00\ubc88\ud638, \uac8c\uc784 \uc790\uaca9 \uc815\ubcf4, \uacb0\uc81c \uc815\ubcf4, \ube44\uacf5\uac1c \ud504\ub85c\ud544 \ub370\uc774\ud130\ub97c \uc694\uccad\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.",
        "advertising": "\ud5a5\ud6c4 \uad11\uace0\uac00 \ud65c\uc131\ud654\ub418\uba74 Google\uc744 \ud3ec\ud568\ud55c \uc81c3\uc790 \uc0ac\uc5c5\uc790\uac00 Cookie, \uc6f9 \ube44\ucf58, IP \uc8fc\uc18c, \ube0c\ub77c\uc6b0\uc800 \uc815\ubcf4 \ubc0f \uc720\uc0ac \uc2e0\ud638\ub97c \uad11\uace0 \uac8c\uc7ac, \uce21\uc815, \ubcf4\ud638\uc5d0 \uc0ac\uc6a9\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \ud50c\ub798\ub108\ub294 \ub85c\uadf8\uc778, \uacb0\uc81c, \ube44\uacf5\uac1c \ud504\ub85c\ud544\uc744 \uc694\uccad\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.",
        "choices": "\ubc29\ubb38\uc790\ub294 \ube0c\ub77c\uc6b0\uc800 \uc124\uc815\uc5d0\uc11c Cookie\ub97c \uad00\ub9ac\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \uc9c0\uc5ed \uaddc\uc815\uc0c1 \ub3d9\uc758 \ubc30\ub108\ub098 \uac1c\uc778\uc815\ubcf4 \uc81c\uc5b4\uac00 \ud544\uc694\ud558\uba74 \uac1c\uc778\ud654 \uad11\uace0 \uc804\uc5d0 \ud65c\uc131\ud654\ud574\uc57c \ud569\ub2c8\ub2e4.",
        "data": "\ud50c\ub798\ub108\ub294 \ube0c\ub77c\uc6b0\uc800\uc5d0\uc11c \uc2e4\ud589\ub418\uba70 \ud398\uc774\uc9c0\uc5d0\uc11c \uc120\ud0dd\ud55c \uc635\uc158\ub9cc \uc0ac\uc6a9\ud569\ub2c8\ub2e4. \uac1c\uc778 \uacc4\uc815\uc740 \ud544\uc694 \uc5c6\uc2b5\ub2c8\ub2e4. \ud638\uc2a4\ud305 \ubc0f CDN \uc81c\uacf5\uc790\uc5d0 \ubcf4\uc548\uacfc \uc2e0\ub8b0\uc131\uc744 \uc704\ud55c \uae30\ubcf8 \ub85c\uadf8\uac00 \ub0a8\uc744 \uc218 \uc788\uc2b5\ub2c8\ub2e4.",
        "accuracy": "\ub85c\ub4dc\uc544\uc6c3 \ucd94\ucc9c\uc740 \uacf5\uac1c\ub41c \ub860\uce6d \uc8fc\uac04 \uc870\uc0ac\uc640 \ud22c\uba85\ud55c \uac00\uc815\uc744 \ubc14\ud0d5\uc73c\ub85c \ud55c \ud3b8\uc9d1 \uc9c0\uc6d0 \uc790\ub8cc\uc785\ub2c8\ub2e4. Mistfall Loadouts\ub294 \uacf5\uc2dd \ud37c\ube14\ub9ac\uc154\ub098 \uac1c\ubc1c\uc0ac\uc640 \uc81c\ud734\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.",
        "contact": "\uc218\uc815, \ucd9c\ucc98 \uc5c5\ub370\uc774\ud2b8, \uc815\ucc45 \ubb38\uc758\ub294 hello@mistfallloadouts.blog \ub85c \ubcf4\ub0b4\uc8fc\uc138\uc694.",
    },
    "it": {
        "scope": "Mistfall Loadouts pubblica consigli indipendenti per loadout, classi, build e decisioni di rotta di Mistfall Hunter. Il sito evita funzioni account e non chiede password, credenziali di gioco, pagamenti o profili privati.",
        "advertising": "Se la pubblicita sara attivata in futuro, fornitori terzi come Google potranno usare cookie, web beacon, indirizzi IP, dati del browser e segnali simili per mostrare, misurare e proteggere annunci. Il planner non richiede login, pagamenti o profili privati.",
        "choices": "I visitatori possono gestire i cookie nel browser. Se un mercato richiede banner di consenso o controlli regionali, il sito dovrebbe abilitarli prima degli annunci personalizzati.",
        "data": "Il planner funziona nel browser e usa solo le opzioni scelte nella pagina. Non serve un account personale. Hosting e CDN possono conservare log di base per sicurezza e affidabilita.",
        "accuracy": "Le raccomandazioni di loadout sono aiuti editoriali basati su ricerca pubblica di lancio e ipotesi trasparenti. Mistfall Loadouts non e affiliato al publisher o sviluppatore ufficiale.",
        "contact": "Per correzioni, aggiornamenti delle fonti o domande sulle policy, contatta hello@mistfallloadouts.blog.",
    },
}


def legal_sections(page_key: str, locale: str) -> List[Dict[str, str]]:
    """
    生成法律与说明页面的本地化段落列表。

    :param page_key: 页面键名
    :param locale: 语言代码
    :return: list[dict[str, str]]，包含标题和正文的段落列表
    """
    t = tr(locale)
    body = localized_items(LEGAL_BODY, locale)
    sections = [
        {"heading": t["site_scope"], "body": body["scope"]},
    ]
    if page_key == "privacy-policy":
        sections.extend(
            [
                {"heading": t["advertising_cookies"], "body": body["advertising"]},
                {"heading": t["user_choices"], "body": body["choices"]},
            ]
        )
    sections.extend(
        [
            {"heading": t["data_handling"], "body": body["data"]},
            {"heading": t["accuracy_affiliation"], "body": body["accuracy"]},
            {"heading": t["contact_heading"], "body": body["contact"]},
        ]
    )
    return sections


def planner_i18n(locale: str) -> Dict[str, Any]:
    """
    生成浏览器端规划器使用的本地化文案。

    :param locale: 语言代码
    :return: dict[str, Any]，规划器文案和结果模板
    """
    t = tr(locale)
    shared = {
        "classNotes": {
            "vanguard": [t["class_vanguard"], LOCALIZED_CLASS_ROWS[locale][0]["strength"], LOCALIZED_CLASS_ROWS[locale][0]["watch"]],
            "seeker": [t["class_seeker"], LOCALIZED_CLASS_ROWS[locale][1]["strength"], LOCALIZED_CLASS_ROWS[locale][1]["watch"]],
            "arcanist": [t["class_arcanist"], LOCALIZED_CLASS_ROWS[locale][2]["strength"], LOCALIZED_CLASS_ROWS[locale][2]["watch"]],
            "warden": [t["class_warden"], LOCALIZED_CLASS_ROWS[locale][3]["strength"], LOCALIZED_CLASS_ROWS[locale][3]["watch"]],
        },
        "roles": {"solo": t["role_solo"], "team": t["role_team"], "boss": t["role_boss"]},
        "risks": {"safe": t["risk_safe"], "balanced": t["risk_balanced"], "greedy": t["risk_greedy"]},
        "weapons": {"melee": t["weapon_melee"], "ranged": t["weapon_ranged"], "hybrid": t["weapon_hybrid"]},
        "phases": {"early": t["phase_early"], "mid": t["phase_mid"], "late": t["phase_late"]},
    }
    templates = {
        "en": {
            "summary": "{className} plan for {role}: choose {weapon} pressure and keep risk at {risk}.",
            "stats": "{strength}; favor {phase} reliability over untested maximum damage.",
            "route": "Use the class warning as your exit rule: {watch}",
            "tip": "If a new patch changes class values, keep the same role logic and update gear choices after reliable tests appear.",
            "copyUnavailable": "Copy is unavailable in this browser.",
        },
        "es": {
            "summary": "Plan de {className} para {role}: usa presi\u00f3n {weapon} y mant\u00e9n el riesgo en {risk}.",
            "stats": "{strength}; prioriza la fiabilidad de {phase} sobre el da\u00f1o m\u00e1ximo sin probar.",
            "route": "Usa esta advertencia como regla de salida: {watch}",
            "tip": "Si un parche cambia valores de clase, conserva la l\u00f3gica de rol y actualiza equipo con pruebas fiables.",
            "copyUnavailable": "La copia no est\u00e1 disponible en este navegador.",
        },
        "ja": {
            "summary": "{role}\u5411\u3051\u306e{className}\u30d7\u30e9\u30f3\u3067\u3059\u3002{weapon}\u5727\u529b\u3092\u4f7f\u3044\u3001\u30ea\u30b9\u30af\u306f{risk}\u306b\u6291\u3048\u307e\u3059\u3002",
            "stats": "{strength}\u3002\u672a\u691c\u8a3c\u306e\u6700\u5927\u706b\u529b\u3088\u308a{phase}\u306e\u5b89\u5b9a\u6027\u3092\u512a\u5148\u3057\u307e\u3059\u3002",
            "route": "\u8131\u51fa\u5224\u65ad\u306f\u3053\u306e\u6ce8\u610f\u70b9\u3092\u57fa\u6e96\u306b\u3057\u307e\u3059\uff1a{watch}",
            "tip": "\u30d1\u30c3\u30c1\u3067\u30af\u30e9\u30b9\u5024\u304c\u5909\u308f\u3063\u305f\u3089\u3001\u5f79\u5272\u306e\u8003\u3048\u65b9\u306f\u4fdd\u3061\u3001\u691c\u8a3c\u5f8c\u306b\u88c5\u5099\u3092\u66f4\u65b0\u3057\u307e\u3059\u3002",
            "copyUnavailable": "\u3053\u306e\u30d6\u30e9\u30a6\u30b6\u3067\u306f\u30b3\u30d4\u30fc\u3067\u304d\u307e\u305b\u3093\u3002",
        },
        "fr": {
            "summary": "Plan {className} pour {role} : choisissez une pression {weapon} et gardez le risque {risk}.",
            "stats": "{strength}; privil\u00e9giez la fiabilit\u00e9 {phase} plut\u00f4t que des d\u00e9g\u00e2ts non test\u00e9s.",
            "route": "Utilisez cet avertissement comme r\u00e8gle de sortie : {watch}",
            "tip": "Si un patch change les valeurs, gardez la logique de r\u00f4le et mettez l'\u00e9quipement \u00e0 jour apr\u00e8s des tests fiables.",
            "copyUnavailable": "La copie n'est pas disponible dans ce navigateur.",
        },
        "de": {
            "summary": "{className}-Plan f\u00fcr {role}: Nutze {weapon}-Druck und halte das Risiko {risk}.",
            "stats": "{strength}; bevorzuge {phase}-Zuverl\u00e4ssigkeit statt ungetesteten Maximalschaden.",
            "route": "Nutze diese Warnung als Ausstiegsregel: {watch}",
            "tip": "Wenn ein Patch Klassenwerte \u00e4ndert, behalte die Rollenlogik und aktualisiere Ausr\u00fcstung nach Tests.",
            "copyUnavailable": "Kopieren ist in diesem Browser nicht verf\u00fcgbar.",
        },
        "pt": {
            "summary": "Plano de {className} para {role}: use press\u00e3o {weapon} e mantenha risco {risk}.",
            "stats": "{strength}; priorize a confiabilidade de {phase} em vez de dano m\u00e1ximo n\u00e3o testado.",
            "route": "Use este alerta como regra de sa\u00edda: {watch}",
            "tip": "Se um patch mudar valores de classe, mantenha a l\u00f3gica de fun\u00e7\u00e3o e atualize equipamento ap\u00f3s testes.",
            "copyUnavailable": "Copiar n\u00e3o est\u00e1 dispon\u00edvel neste navegador.",
        },
        "ko": {
            "summary": "{role}\uc6a9 {className} \uacc4\ud68d\uc785\ub2c8\ub2e4. {weapon} \uc555\ubc15\uc744 \uc120\ud0dd\ud558\uace0 \uc704\ud5d8\ub3c4\ub294 {risk}\ub85c \uc720\uc9c0\ud558\uc138\uc694.",
            "stats": "{strength}; \uac80\uc99d\ub418\uc9c0 \uc54a\uc740 \ucd5c\ub300 \ud654\ub825\ubcf4\ub2e4 {phase} \uc548\uc815\uc131\uc744 \uc6b0\uc120\ud558\uc138\uc694.",
            "route": "\uc774 \uc8fc\uc758\uc810\uc744 \ud0c8\ucd9c \uaddc\uce59\uc73c\ub85c \uc0ac\uc6a9\ud558\uc138\uc694: {watch}",
            "tip": "\ud328\uce58\ub85c \ud074\ub798\uc2a4 \uc218\uce58\uac00 \ubc14\ub00c\uba74 \uc5ed\ud560 \ub85c\uc9c1\uc744 \uc720\uc9c0\ud558\uace0 \uc2e0\ub8b0\ud560 \ud14c\uc2a4\ud2b8 \ud6c4 \uc7a5\ube44\ub97c \uac31\uc2e0\ud558\uc138\uc694.",
            "copyUnavailable": "\uc774 \ube0c\ub77c\uc6b0\uc800\uc5d0\uc11c\ub294 \ubcf5\uc0ac\ub97c \uc0ac\uc6a9\ud560 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4.",
        },
        "it": {
            "summary": "Piano {className} per {role}: scegli pressione {weapon} e mantieni rischio {risk}.",
            "stats": "{strength}; privilegia l'affidabilit\u00e0 {phase} rispetto al danno massimo non testato.",
            "route": "Usa questo avviso come regola di uscita: {watch}",
            "tip": "Se una patch cambia i valori, conserva la logica di ruolo e aggiorna l'equipaggiamento dopo test affidabili.",
            "copyUnavailable": "La copia non \u00e8 disponibile in questo browser.",
        },
    }
    return shared | templates.get(locale, templates["en"])


PAGES = {
    "index": {"path": "/"},
    "classes": {"path": "/classes/"},
    "builds": {"path": "/builds/"},
    "guide": {"path": "/guide/"},
    "price-guide": {"path": "/mistfall-hunter-price/"},
    "gameplay-guide": {"path": "/mistfall-hunter-gameplay/"},
    "crossplay-guide": {"path": "/mistfall-hunter-crossplay/"},
    "about": {"path": "/about/"},
    "contact": {"path": "/contact/"},
    "privacy-policy": {"path": "/privacy-policy/"},
    "terms-of-service": {"path": "/terms-of-service/"},
}


COMMON_UI_LABELS: Dict[str, Dict[str, str]] = {
    "en": {"language_label": "Language", "primary_nav_label": "Primary navigation", "footer_nav_label": "Footer navigation", "advertisement_label": "Advertisement"},
    "es": {"language_label": "Idioma", "primary_nav_label": "Navegación principal", "footer_nav_label": "Navegación del pie de página", "advertisement_label": "Publicidad"},
    "ja": {"language_label": "言語", "primary_nav_label": "メインナビゲーション", "footer_nav_label": "フッターナビゲーション", "advertisement_label": "広告"},
    "fr": {"language_label": "Langue", "primary_nav_label": "Navigation principale", "footer_nav_label": "Navigation du pied de page", "advertisement_label": "Publicité"},
    "de": {"language_label": "Sprache", "primary_nav_label": "Hauptnavigation", "footer_nav_label": "Footer-Navigation", "advertisement_label": "Werbung"},
    "pt": {"language_label": "Idioma", "primary_nav_label": "Navegação principal", "footer_nav_label": "Navegação do rodapé", "advertisement_label": "Publicidade"},
    "ko": {"language_label": "언어", "primary_nav_label": "주요 탐색", "footer_nav_label": "푸터 탐색", "advertisement_label": "광고"},
    "it": {"language_label": "Lingua", "primary_nav_label": "Navigazione principale", "footer_nav_label": "Navigazione del piè di pagina", "advertisement_label": "Pubblicità"},
}


def tr(locale: str) -> Dict[str, str]:
    """
    返回指定语言的页面文案。

    :param locale: 语言代码
    :return: dict[str, str]，当前语言文案
    """
    base = TRANSLATIONS.get(locale, TRANSLATIONS[DEFAULT_LANGUAGE])
    return base | COMMON_UI_LABELS.get(locale, COMMON_UI_LABELS[DEFAULT_LANGUAGE])


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


def localized_items(mapping: Dict[str, Any], locale: str) -> Any:
    """
    从多语言映射中取出指定语言内容。

    :param mapping: 多语言内容映射
    :param locale: 语言代码
    :return: Any，指定语言内容或英文默认内容
    """
    return mapping.get(locale, mapping[DEFAULT_LANGUAGE])


def common_context(page_key: str, locale: str) -> Dict[str, Any]:
    """
    生成所有模板共享的渲染上下文。

    :param page_key: 页面键名
    :param locale: 语言代码
    :return: dict[str, Any]，模板上下文字典
    """
    source_guide = PRICE_GUIDES[locale]
    price_guide = dict(source_guide)
    price_guide["url"] = localized_path("price-guide", locale)
    price_guide["sections"] = []
    for source_section in source_guide["sections"]:
        section = dict(source_section)
        section_links = []
        for source_link in source_section.get("links", []):
            link = dict(source_link)
            link["url"] = localized_path(source_link["target"], locale)
            section_links.append(link)
        if section_links:
            section["links"] = section_links
        price_guide["sections"].append(section)
    price_guide["related_links"] = [
        dict(link, url=localized_path(link["target"], locale))
        for link in source_guide["related_links"]
    ]
    gameplay_source_guide = GAMEPLAY_GUIDES[locale]
    gameplay_guide = dict(gameplay_source_guide)
    gameplay_guide["url"] = localized_path("gameplay-guide", locale)
    gameplay_guide["sections"] = []
    for source_section in gameplay_source_guide["sections"]:
        section = dict(source_section)
        section_links = []
        for source_link in source_section.get("links", []):
            link = dict(source_link)
            link["url"] = localized_path(source_link["target"], locale)
            section_links.append(link)
        if section_links:
            section["links"] = section_links
        gameplay_guide["sections"].append(section)
    gameplay_guide["related_links"] = [
        dict(link, url=localized_path(link["target"], locale))
        for link in gameplay_source_guide["related_links"]
    ]
    crossplay_source_guide = CROSSPLAY_GUIDES[locale]
    crossplay_guide = dict(crossplay_source_guide)
    crossplay_guide["url"] = localized_path("crossplay-guide", locale)
    crossplay_guide["sections"] = []
    for source_section in crossplay_source_guide["sections"]:
        section = dict(source_section)
        section_links = []
        for source_link in source_section.get("links", []):
            link = dict(source_link)
            link["url"] = localized_path(source_link["target"], locale)
            section_links.append(link)
        if section_links:
            section["links"] = section_links
        crossplay_guide["sections"].append(section)
    crossplay_guide["related_links"] = [
        dict(link, url=localized_path(link["target"], locale))
        for link in crossplay_source_guide["related_links"]
    ]
    price_guide["related_links"].append(
        {"url": localized_path("gameplay-guide", locale), "label": gameplay_source_guide["entry_label"]}
    )
    price_guide["related_links"].append(
        {"url": localized_path("crossplay-guide", locale), "label": crossplay_source_guide["entry_label"]}
    )
    gameplay_guide["related_links"].append(
        {"url": localized_path("crossplay-guide", locale), "label": crossplay_source_guide["entry_label"]}
    )
    article_guide = None
    if page_key == "price-guide":
        article_guide = price_guide
    elif page_key == "gameplay-guide":
        article_guide = gameplay_guide
    elif page_key == "crossplay-guide":
        article_guide = crossplay_guide
    t = tr(locale)
    if article_guide:
        t = t | {
            "title": article_guide["title"],
            "meta_title": article_guide["meta_title"],
            "meta_description": article_guide["meta_description"],
            "meta_keywords": article_guide["meta_keywords"],
        }
    article_schema = None
    if article_guide:
        article_schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": article_guide["title"],
            "description": article_guide["meta_description"],
            "url": canonical_url(page_key, locale),
            "image": [
                f"{BASE_URL}/static/{article_guide['feature_image']['path']}",
                *[
                    f"{BASE_URL}/static/{section['image']['path']}"
                    for section in article_guide["sections"]
                    if section.get("image")
                ],
            ],
            "dateModified": article_guide["checked_iso"],
            "inLanguage": locale,
            "author": {"@type": "Organization", "name": "Mistfall Loadouts"},
            "publisher": {"@type": "Organization", "name": "Mistfall Loadouts", "url": f"{BASE_URL}/"},
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item["question"],
                    "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
                }
                for item in article_guide["faq"]
            ],
        }
    language_links = [
        {"code": code, "label": LOCALE_LABELS[code], "url": localized_path(page_key, code), "active": code == locale}
        for code in SUPPORTED_LANGUAGES
    ]
    return {
        "t": t,
        "locale": locale,
        "locale_label": LOCALE_LABELS[locale],
        "locale_market": LOCALE_MARKETS[locale],
        "languages": language_links,
        "canonical_url": canonical_url(page_key, locale),
        "alternate_urls": alternate_urls(page_key),
        "base_url": BASE_URL,
        "last_updated": LAST_UPDATED,
        "price_guide": article_guide or price_guide,
        "gameplay_guide": gameplay_guide,
        "crossplay_guide": crossplay_guide,
        "page_image": article_guide["feature_image"]["path"] if article_guide else None,
        "page_image_url": f"{BASE_URL}/static/{article_guide['feature_image']['path']}" if article_guide else None,
        "article_schema": article_schema,
        "class_rows": localized_items(LOCALIZED_CLASS_ROWS, locale),
        "build_patterns": localized_items(LOCALIZED_BUILD_PATTERNS, locale),
        "faq_items": localized_items(FAQ_ITEMS, locale),
        "steps": localized_items(STEPS, locale),
        "deep_guide": localized_items(DEEP_GUIDE, locale),
        "legal_sections": legal_sections(page_key, locale),
        "planner_i18n": planner_i18n(locale),
        "nav": [
            ("tool", localized_path("index", locale) + "#planner", t["nav_tool"]),
            ("classes", localized_path("classes", locale), t["nav_classes"]),
            ("builds", localized_path("builds", locale), t["nav_builds"]),
            ("guide", localized_path("guide", locale), t["nav_guide"]),
            ("faq", localized_path("index", locale) + "#faq", t["nav_faq"]),
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


def page_key_from_segment(segment: str) -> str | None:
    """
    将 URL 路径片段解析为内部页面键名。

    :param segment: URL 中不带斜杠的页面片段
    :return: str | None，匹配的页面键名或未找到时的 None
    """
    if segment in PAGES:
        return segment
    target_path = f"/{segment}/"
    for page_key, config in PAGES.items():
        if config["path"] == target_path:
            return page_key
    return None


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
    page_key = page_key_from_segment(segment)
    if page_key:
        return render_page(page_key, DEFAULT_LANGUAGE)
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
    resolved_page_key = page_key_from_segment(page_key)
    if not resolved_page_key:
        abort(404)
    return render_page(resolved_page_key, lang)


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
