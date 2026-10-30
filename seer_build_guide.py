from typing import Any, Dict, List, Optional


_STEAM_URL = "https://store.steampowered.com/app/3282300/Mistfall_Hunter/"
_OFFICIAL_URL = "https://mistfallhunter.com/"
_FEATURE_IMAGE = "images/mistfall-hunter-solo-exploration.webp"
_COMBAT_IMAGE = "images/mistfall-hunter-steam-store-combat.webp"
_EXTRACTION_IMAGE = "images/mistfall-hunter-steam-store-extraction.webp"

_OFFICIAL_LINK_LABELS = {
    "en": ["Mistfall Hunter on Steam", "Mistfall Hunter official website"],
    "es": ["Mistfall Hunter en Steam", "Sitio oficial de Mistfall Hunter"],
    "ja": ["Mistfall HunterのSteamページ", "Mistfall Hunter公式サイト"],
    "fr": ["Mistfall Hunter sur Steam", "Site officiel de Mistfall Hunter"],
    "de": ["Mistfall Hunter auf Steam", "Offizielle Mistfall-Hunter-Website"],
    "pt": ["Mistfall Hunter na Steam", "Site oficial de Mistfall Hunter"],
    "ko": ["Mistfall Hunter Steam 페이지", "Mistfall Hunter 공식 사이트"],
    "it": ["Mistfall Hunter su Steam", "Sito ufficiale di Mistfall Hunter"],
}

_VISIBLE_TERM_REPLACEMENTS = {
    "es": {"FAQ": "Preguntas frecuentes"},
    "ja": {"FAQ": "よくある質問"},
    "fr": {"Reset-Call": "appel de réinitialisation", "Reset": "réinitialisation", "reset": "réinitialisation", "Guide": "Conseil", "FAQ": "Questions fréquentes"},
    "de": {"Reset-Call": "Rücksetz-Ansage", "Reset": "Rücksetzung", "Guide": "Ratgeber", "FAQ": "Häufige Fragen"},
    "pt": {"reset": "reinício", "Reset": "Reinício", "FAQ": "Perguntas frequentes"},
    "ko": {"FAQ": "자주 묻는 질문"},
    "it": {"reset": "ripristino", "Reset": "Ripristino", "FAQ": "Domande frequenti"},
}

_NON_VISIBLE_KEYS = {
    "primary_keyword",
    "related_keywords",
    "meta_keywords",
    "path",
    "target",
    "source_url",
    "slug",
    "locale",
    "checked_iso",
}


def _localize_visible_terms(value: Any, replacements: Dict[str, str], key: str = "") -> Any:
    """
    仅替换页面可见文案中的通用英文短词，保留关键词、路由和素材路径。

    :param value: 待处理的页面数据节点
    :param replacements: 当前语言的替换词典
    :param key: 当前节点的字段名
    :return: 处理后的页面数据节点
    """
    if isinstance(value, dict):
        return {
            child_key: _localize_visible_terms(child, replacements, child_key)
            for child_key, child in value.items()
        }
    if isinstance(value, list):
        return [_localize_visible_terms(child, replacements, key) for child in value]
    if isinstance(value, str) and key not in _NON_VISIBLE_KEYS:
        for source, target in replacements.items():
            value = value.replace(source, target)
    return value


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
    构造 Seer build 文章的单个内容区块。

    :param section_id: 区块的稳定 HTML 锚点
    :param heading: 区块标题
    :param paragraphs: 正文段落列表
    :param bullets: 可选要点列表
    :param links: 可选站内链接列表
    :param table: 可选表格数据
    :param steps: 可选步骤列表
    :param image: 可选配图数据
    :return: dict，模板可直接渲染的区块
    """
    if image and image.get("path") == _FEATURE_IMAGE:
        image = None
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


def _guide(locale: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    补齐指定语言文章的通用元数据和来源字段。

    :param locale: 语言代码
    :param data: 语言专属文章字段
    :return: dict，完整文章数据
    """
    guide = _localize_visible_terms(dict(data), _VISIBLE_TERM_REPLACEMENTS.get(locale, {}))
    guide.setdefault("slug", "mistfall-hunter-seer-build")
    guide.setdefault("checked_iso", "2026-10-30")
    guide["locale"] = locale
    guide.setdefault("official_links", [
        {"label": _OFFICIAL_LINK_LABELS[locale][0], "url": _STEAM_URL, "rel": "noopener"},
        {"label": _OFFICIAL_LINK_LABELS[locale][1], "url": _OFFICIAL_URL, "rel": "noopener"},
    ])
    return guide


SEER_BUILD_GUIDES: Dict[str, Dict[str, Any]] = {
    "en": _guide("en", {
        "primary_keyword": "Mistfall Hunter Seer build",
        "related_keywords": [
            "best Seer build Mistfall Hunter",
            "best Seer abilities and talent build Mistfall Hunter",
            "melee Seer build Mistfall Hunter",
            "Mistfall Hunter Seer healer build",
        ],
        "title": "Mistfall Hunter Seer Build: Abilities, Talents, and Safer Solo Routes",
        "meta_title": "Mistfall Hunter Seer Build: Abilities & Talents",
        "meta_description": "Build a practical Mistfall Hunter Seer setup around ability timing, talent jobs, melee or healer paths, solo routes, and trio communication without invented stats.",
        "meta_keywords": "Mistfall Hunter Seer build, best Seer build Mistfall Hunter, Seer abilities and talent build, melee Seer build, Seer healer build",
        "eyebrow": "Mistfall Hunter class build guide",
        "lede": "A useful Mistfall Hunter Seer build starts with a job you can repeat: create information, protect a recovery window, or add controlled pressure. This guide turns the current Seer search cluster into a testable setup for solo and trio runs without pretending that a patch-sensitive talent value is permanent.",
        "checked_label": "Role-based Seer framework reviewed 30 October 2026; exact item values remain version-sensitive",
        "entry_label": "Read the Mistfall Hunter Seer build guide",
        "feature_image": {
            "path": _FEATURE_IMAGE,
            "alt": "Official Steam Store screenshot of a Mistfall Hunter hunter exploring a dark chamber alone",
            "caption": "Official Steam Store exploration media used to frame the Seer build's information and reset decisions; it is not a Seer stat test.",
            "source_label": "Open the official Steam listing",
            "source_url": _STEAM_URL,
            "width": 1200,
            "height": 675,
        },
        "facts_headers": ["Build question", "Safe starting answer", "Change it when"],
        "facts_rows": [
            ["Role", "Information plus a recoverable reset", "A teammate already owns scouting or recovery"],
            ["Ability", "Use one repeatable trigger before adding a second", "The current tooltip or cooldown changes"],
            ["Talent", "Choose the talent that fixes your observed failure", "The bonus cannot be activated in your normal route"],
            ["Melee path", "Short contact, then return to space", "The encounter denies a safe exit"],
            ["Healer path", "Support only while the group can regroup", "Healing costs the route or leaves you exposed"],
        ],
        "intro": "For a Mistfall Hunter Seer build, choose the problem you want the class to solve before you choose a talent order. The most reliable first setup is not a universal meta list: it is one that lets you read a room, create a short pressure window, and keep one recovery answer unused. Similarweb shows strong demand for Seer build wording, but the public sources checked for this page do not verify hidden damage, cooldown, or rank values. Treat the framework below as a build brief you can test in the current client.",
        "sections": [
            _section(
                "seer-job",
                "What a Seer build should solve first",
                [
                    "Seer queries often use the word build as if there were one fixed answer. An extraction run needs a more useful definition. Your build should help the team see the next decision, survive the cost of taking it, and leave when the route stops paying. That can mean scouting an uncertain room, covering a revive, or applying pressure after an enemy commits. It does not mean every Seer must be a healer or that one talent row is always best.",
                    "Write the job in one sentence before loading in: ‘I reveal the next safe angle’, ‘I keep one teammate alive through a reset’, or ‘I create a short opening and stop.’ If the sentence contains three jobs, the build is too broad. Start with one primary job and one fallback. This keeps the page useful even when the current version uses different class labels, item names, or ability values than a community post.",
                ],
                bullets=[
                    "Keep one movement, recovery, or information option available after the first contact.",
                    "Use a talent because it changes a real decision, not because a screenshot calls it meta.",
                    "Change one variable per run so the result is explainable.",
                ],
                links=[
                    {"target": "classes", "label": "Compare Seer with the site's other class roles"},
                    {"target": "tier-list-guide", "label": "Use the tier list as a role comparison, not a permanent ranking"},
                ],
            ),
            _section(
                "ability-talent-priority",
                "Best Seer abilities and talent priorities",
                [
                    "The best Seer ability is the one whose trigger, cost, and recovery you can name before the fight. Read the current tooltip and test it in a low-value route. If the effect requires a condition you rarely create, its headline value may not help your actual run. Prefer a smaller effect that you can activate on purpose over a larger effect that only appears in an ideal clip.",
                    "For talents, begin with the failure that ended your last run. If the team lacked information, choose the option that makes the next angle or threat easier to read. If the team reached the objective but could not leave, choose recovery or space. If the group was safe but slow, add pressure only after the first two problems are stable. This is the evidence-based boundary behind searches for a best Seer build: the best choice depends on the failure you are fixing.",
                ],
                table={
                    "headers": ["Priority", "Look for in the current client", "Avoid"],
                    "rows": [
                        ["1. Information", "A repeatable way to reveal or read danger", "Assuming a visual effect proves hidden range or damage"],
                        ["2. Reset", "A tool that buys space, time, or a regroup", "Spending every defensive option on first contact"],
                        ["3. Support", "A heal or utility window with a safe exit", "Healing while both players are still being chased"],
                        ["4. Pressure", "A short opening after the target commits", "Chasing damage into an unknown room"],
                        ["5. Flex", "A fallback that still works when the plan changes", "Taking five conditional bonuses no one can call"],
                    ],
                },
                image={
                    "path": _COMBAT_IMAGE,
                    "alt": "Official Steam Store combat screenshot showing a Mistfall Hunter hunter facing a large forest creature",
                    "caption": "Official Steam Store combat media for timing and spacing context; it does not show a verified Seer talent or damage result.",
                    "source_label": "Open the official Steam listing",
                    "source_url": _STEAM_URL,
                    "width": 1200,
                    "height": 675,
                },
            ),
            _section(
                "melee-healer-paths",
                "Melee Seer build or healer Seer build?",
                [
                    "The phrase ‘melee Seer build’ points to a close-range branch, but it should not be read as permission to stay in every trade. Choose a weapon or skill pattern that creates one short contact window, then return to a position where the next attack is readable. The Seer value is the information and reset around that contact. If the route disappears when you commit, the build needs more space or a lower-risk trigger before it needs more damage.",
                    "A healer or support branch has a similar boundary. Support is useful when it keeps a teammate in the fight without deleting the escape plan. Agree where the heal happens, who calls the reset, and which resource is reserved for the route home. If the party asks the Seer to heal while everyone is split, reduce the objective first. A safe regroup is a better result than a perfect heal followed by a lost extraction.",
                ],
                table={
                    "headers": ["Path", "Good first test", "Switch away when"],
                    "rows": [
                        ["Melee Seer", "One short opening after the target commits", "You cannot see a retreat before contact"],
                        ["Healer Seer", "A planned heal during a protected regroup", "The heal locks you in the open"],
                        ["Information Seer", "Reveal one unknown angle before the push", "The effect is saved so long that it never changes a decision"],
                        ["Flex Seer", "One primary job plus one emergency fallback", "The group cannot say which job is yours"],
                    ],
                },
                links=[
                    {"target": "sword-shield-guide", "label": "Pair a controlled close-range plan with the sword-and-shield guide"},
                    {"target": "gameplay-guide", "label": "Review the site's extraction loop before adding risk"},
                ],
            ),
            _section(
                "solo-route",
                "How to run the Seer build solo",
                [
                    "Solo Seer play has no teammate to confirm an angle or cover a revive. Build for information first: approach one uncertain space, keep the route behind you visible, and spend only the action needed to understand the next threat. If the first fight consumes the recovery option you planned for the exit, pause before taking another reward. A solo build is successful when it preserves choices, not when it forces every encounter.",
                    "Use a short loop for the first tests. Choose one objective, name the condition that ends the run, and record the point where the Seer job stopped helping. That note is more useful than copying a class screenshot without a patch, mode, or test method. The same logic supports searches for a solo class: choose the class that lets you read, reset, and leave under your actual control scheme.",
                ],
                steps=[
                    "Pick one objective and one route home before the first risky room.",
                    "Use the information or support action only when it changes the next decision.",
                    "Recheck health, remaining recovery, and route visibility after contact.",
                    "Extract when the remaining reward no longer pays for the route risk.",
                ],
                image={
                    "path": _EXTRACTION_IMAGE,
                    "alt": "Official Steam Store screenshot of a Mistfall Hunter hunter approaching a glowing chest in a dark chamber",
                    "caption": "Official Steam Store extraction media; it illustrates the reward-versus-route decision behind a solo Seer test.",
                    "source_label": "Open the official Steam listing",
                    "source_url": _STEAM_URL,
                    "width": 1200,
                    "height": 675,
                },
                links=[{"target": "beginner-guide", "label": "Use the beginner guide for first-run and extraction fundamentals"}],
            ),
            _section(
                "trio-communication",
                "How the Seer build fits a trio",
                [
                    "In a trio, Seer is strongest when the team knows which information or recovery job is reserved for the class. Name an anchor, a pressure player, and a flex player before the queue. The Seer can fill flex or support, but the label matters less than the call: who protects the reset, who takes the short opening, and who watches the route? If two players expect the Seer to solve the same problem, the build will feel weak even when its tools are working.",
                    "When a teammate is separated, stop the original plan. A healer Seer should not cross an open room alone to rescue a player who has lost the route, and a melee Seer should not chase a target beyond the anchor's space. Regroup, lower the objective, and restart the role contract. This is the practical link between a single-class build and the site's trio builds guide: the loadout only works when the group can describe its boundaries.",
                ],
                table={
                    "headers": ["Trio moment", "Seer call", "Team response"],
                    "rows": [
                        ["Unknown room", "Hold the information action", "Let the flex player check one angle"],
                        ["Clear opening", "Call one pressure window", "Stop when the window closes"],
                        ["Player split", "Protect the regroup route", "Pause instead of forcing a rescue"],
                        ["Exit unclear", "Reserve support for the retreat", "Lower the reward target or extract"],
                    ],
                },
                image={
                    "path": _FEATURE_IMAGE,
                    "alt": "Official Steam Store exploration screenshot of a Mistfall Hunter hunter moving through a dark room",
                    "caption": "Official Steam Store exploration media used as a reminder that a trio build still needs a readable route and regroup point.",
                    "source_label": "Open the official Steam listing",
                    "source_url": _STEAM_URL,
                    "width": 1200,
                    "height": 675,
                },
                links=[{"target": "trio-builds-guide", "label": "Use the trio roles and duo fallback checklist"}],
            ),
            _section(
                "test-and-mistakes",
                "A five-run test plan and common mistakes",
                [
                    "Do not judge the Seer build from one lucky extraction or one failed boss room. Run the same low-risk route five times, keep the class job stable, and change only one talent, weapon pattern, or support choice between tests. Record the trigger you used, the resource it cost, the point where the route became unsafe, and whether the team understood the call. The result is a small experiment, not proof of a universal tier ranking.",
                    "The most common mistake is building around an unverified number. Another is saving the Seer tool so carefully that it never affects a decision. A third is asking the class to cover scouting, healing, damage, and rescue at the same time. Fix the first visible failure, keep one fallback, and update the page's assumptions when an official patch or repeatable test changes the input.",
                ],
                bullets=[
                    "Record patch, mode, team size, and the exact ability or talent tested.",
                    "Compare the same route and risk level before changing the conclusion.",
                    "Treat a community screenshot as a lead unless its source and conditions are clear.",
                    "Stop a test when the remaining reward no longer pays for the route home.",
                ],
                links=[{"target": "maps-guide", "label": "Check map and route context before comparing runs"}],
            ),
        ],
        "faq_title": "Mistfall Hunter Seer build FAQ",
        "faq": [
            {"question": "What is the best Seer build in Mistfall Hunter?", "answer": "There is no verified permanent best build in the public sources checked for this guide. Start with one job: information, reset, support, or short pressure. Choose the current ability and talent that fixes your observed failure, then test it on the same route before calling it a best build."},
            {"question": "What are the best Seer abilities and talents?", "answer": "Prioritize a repeatable information trigger, a safe reset, and a support window with a route home. Exact names, values, and ranks are version-sensitive, so confirm the current tooltip and record the patch or mode when you test them."},
            {"question": "Is a melee Seer build viable?", "answer": "A melee Seer can work when the build creates one short contact window and still leaves a readable retreat. Do not treat close range as permission to chase. If you cannot see the reset before contact, lower the risk or choose more space first."},
            {"question": "Can Seer work as a healer or support build?", "answer": "Yes, when the team agrees where the heal happens and who calls the regroup. Support should preserve the escape plan. If the group is split in an open room, reduce the objective instead of spending every resource on a rescue."},
            {"question": "What is a good solo Seer build?", "answer": "Use one information action, one recovery answer, and a modest pressure option. Test the setup on a known route, keep the exit visible, and leave when the reward no longer covers the remaining risk. Solo success is choice preservation, not forced fights."},
            {"question": "Should a trio copy a Seer build code?", "answer": "Only when the code has a clear source, patch, mode, and assumptions. A copied code cannot tell your team who owns scouting, pressure, or the retreat. Use the role contract first and verify every current value in the client."},
        ],
        "summary_heading": "Seer build summary",
        "summary": "Build Seer around one repeatable job, one fallback, and a route home. Start with information and reset, add support or melee pressure only when you can call the window, and test one change at a time. The official Steam and game pages confirm the broad extraction and equipment context; they do not verify hidden numbers, so keep exact claims tied to current tooltips or repeatable tests.",
        "related_title": "Continue planning Mistfall Hunter runs",
        "related_links": [
            {"target": "classes", "label": "Compare Mistfall Hunter classes"},
            {"target": "tier-list-guide", "label": "Read the Mistfall Hunter tier list"},
            {"target": "trio-builds-guide", "label": "Plan trio roles and duo fallbacks"},
            {"target": "sword-shield-guide", "label": "Review a controlled sword-and-shield build"},
            {"target": "gameplay-guide", "label": "Review solo gameplay and extraction decisions"},
        ],
        "source_title": "Sources and scope",
        "source_note": "The page uses official Steam Store media and the official Mistfall Hunter website for broad game context. Similarweb keyword data supports the Seer build topic, while exact class, item, talent, damage, and cooldown values remain unverified and should be checked in the current client.",
    }),
    "es": _guide("es", {
        "primary_keyword": "build de Seer de Mistfall Hunter",
        "related_keywords": ["mejor build de Seer Mistfall Hunter", "habilidades y talentos de Seer Mistfall Hunter", "build cuerpo a cuerpo de Seer Mistfall Hunter", "build de apoyo de Seer Mistfall Hunter"],
        "title": "Build de Seer en Mistfall Hunter: habilidades, talentos y rutas seguras",
        "meta_title": "Build de Seer Mistfall Hunter: habilidades y talentos",
        "meta_description": "Crea un build de Seer para Mistfall Hunter con prioridades de habilidades, talentos, ruta cuerpo a cuerpo o apoyo y ajustes para solo y trios.",
        "meta_keywords": "build de Seer de Mistfall Hunter, mejor build de Seer, habilidades de Seer, build cuerpo a cuerpo de Seer, build de apoyo de Seer",
        "eyebrow": "Guia de builds de Mistfall Hunter",
        "lede": "Un buen build de Seer en Mistfall Hunter empieza por una tarea repetible: obtener informacion, proteger un reinicio o aplicar presion controlada. Esta guia convierte el grupo de busquedas de Seer en una configuracion que puedes probar en solo y trio sin inventar valores de un parche.",
        "checked_label": "Marco de Seer revisado el 30 de octubre de 2026; los valores exactos dependen de la version",
        "entry_label": "Leer la guia del build de Seer de Mistfall Hunter",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "Captura oficial de Steam de un cazador de Mistfall Hunter explorando una sala oscura en solitario", "caption": "Imagen oficial de Steam para explicar informacion y reinicio; no es una prueba de estadisticas de Seer.", "source_label": "Abrir la pagina oficial de Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675},
        "facts_headers": ["Pregunta", "Inicio seguro", "Cambialo cuando"],
        "facts_rows": [["Rol", "Informacion y reinicio seguro", "Otro jugador ya cubre exploracion"], ["Habilidad", "Un disparador repetible", "Cambia el texto o enfriamiento"], ["Talento", "Corrige el fallo observado", "No puedes activarlo en tu ruta"], ["Cuerpo a cuerpo", "Contacto corto y volver al espacio", "No queda salida visible"], ["Apoyo", "Curar durante un reagrupamiento", "La cura te deja expuesto"]],
        "intro": "Para un build de Seer de Mistfall Hunter, define primero el problema que quieres resolver y despues el orden de talentos. El mejor inicio no es una lista meta universal: es una configuracion que permita leer una sala, crear una ventana corta y conservar una respuesta de recuperacion. Los datos publicos revisados no confirman danos, enfriamientos ni rangos ocultos, asi que usa este marco como un brief que debes probar en el cliente actual.",
        "sections": [
            _section("seer-job", "Que debe resolver primero un build de Seer", ["Las busquedas de Seer suelen pedir un unico build, pero una partida de extraccion necesita una definicion mas practica. El build debe mostrar la siguiente decision, pagar el coste de tomarla y dejar una salida cuando la ruta deja de compensar. Puede significar explorar una sala, cubrir una reanimacion o presionar despues de que el enemigo se comprometa. No significa que Seer siempre sea curador ni que una fila de talentos sea definitiva.", "Escribe la tarea en una frase antes de entrar: revelar el siguiente angulo seguro, mantener a un aliado vivo durante un reinicio o crear una ventana corta y parar. Si la frase contiene tres trabajos, es demasiado amplia. Empieza con una tarea principal y una alternativa. Asi el build sigue siendo util aunque cambien los nombres o valores del parche."], bullets=["Guarda una opcion de movimiento, recuperacion o informacion para despues del primer contacto.", "Elige un talento porque cambia una decision real, no porque una captura lo llame meta.", "Cambia una variable por partida para entender el resultado."], links=[{"target": "classes", "label": "Comparar Seer con las otras clases"}, {"target": "tier-list-guide", "label": "Usar la tier list como comparacion de roles"}]),
            _section("ability-talent-priority", "Prioridades de habilidades y talentos de Seer", ["La mejor habilidad de Seer es aquella cuyo disparador, coste y recuperacion puedes explicar antes del combate. Lee la descripcion actual y pruebala en una ruta barata. Si depende de una condicion que casi nunca creas, su numero no ayuda a tu partida. Es mejor un efecto pequeno que activas a voluntad que uno grande que solo aparece en un clip perfecto.", "Empieza por el fallo que termino tu ultima partida. Si falto informacion, elige una opcion que haga visible el siguiente peligro. Si llegaste al objetivo pero no pudiste salir, prioriza espacio o recuperacion. Si el grupo estaba seguro pero lento, anade presion despues. Esa es la frontera practica de la busqueda mejor build de Seer: la mejor opcion depende del problema que estes reparando."], table={"headers": ["Prioridad", "Busca", "Evita"], "rows": [["1. Informacion", "Una forma repetible de leer el peligro", "Tomar un efecto visual como prueba de dano"], ["2. Reinicio", "Espacio, tiempo o reagrupamiento", "Gastar toda la defensa al primer contacto"], ["3. Apoyo", "Curar con una salida segura", "Curar mientras todos siguen perseguidos"], ["4. Presion", "Una ventana corta tras el compromiso", "Perseguir a una sala desconocida"], ["5. Flex", "Una alternativa que siga funcionando", "Bonificaciones condicionales que nadie llama"]]}, image={"path": _COMBAT_IMAGE, "alt": "Captura oficial de combate de Steam con un cazador de Mistfall Hunter frente a una criatura forestal", "caption": "Imagen oficial de Steam para el contexto de tiempo y distancia; no muestra un talento de Seer verificado.", "source_label": "Abrir la pagina oficial de Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("melee-healer-paths", "Build de Seer cuerpo a cuerpo o de apoyo", ["El termino build cuerpo a cuerpo de Seer apunta a una rama cercana, pero no autoriza a mantener todos los intercambios. Elige un patron que cree un contacto corto y vuelve a una posicion legible. El valor de Seer esta en la informacion y el reinicio alrededor del contacto. Si la salida desaparece al entrar, necesitas mas espacio o un disparador de menor riesgo antes que mas dano.", "Un build de apoyo tiene el mismo limite. La curacion sirve cuando mantiene al aliado en la lucha sin borrar la salida. Acuerda donde se cura, quien llama el reinicio y que recurso se guarda para el camino de vuelta. Si el grupo esta separado, baja el objetivo antes de gastar todo en un rescate."], table={"headers": ["Ruta", "Primera prueba", "Cambia cuando"], "rows": [["Cuerpo a cuerpo", "Una ventana corta despues del compromiso", "No ves la retirada"], ["Apoyo", "Curar durante un reagrupamiento protegido", "La cura te fija en abierto"], ["Informacion", "Revelar un angulo antes de avanzar", "La guardas y nunca cambia la decision"], ["Flex", "Una tarea principal y un respaldo", "El grupo no sabe cual es tu trabajo"]]}, links=[{"target": "sword-shield-guide", "label": "Combinarlo con la guia de espada y escudo"}, {"target": "gameplay-guide", "label": "Repasar el ciclo de extraccion"}]),
            _section("solo-route", "Como jugar el build de Seer en solitario", ["En solitario no hay un aliado que confirme un angulo o cubra una reanimacion. Prioriza informacion: entra en una sala incierta, conserva visible la ruta de regreso y gasta solo la accion necesaria para entender el peligro. Si el primer combate consume la recuperacion reservada para salir, para antes de tomar otra recompensa. El exito es conservar opciones, no forzar cada pelea.", "Usa un bucle corto en las primeras pruebas. Elige un objetivo, define la condicion de salida y anota cuando el trabajo de Seer dejo de ayudar. Esa nota es mejor que copiar una captura sin parche, modo ni metodo de prueba."], steps=["Elige un objetivo y una ruta de vuelta antes de la sala de riesgo.", "Usa informacion o apoyo solo cuando cambie la siguiente decision.", "Comprueba vida, recuperacion y visibilidad de la ruta despues del contacto.", "Extrae cuando la recompensa restante no cubra el riesgo."], image={"path": _EXTRACTION_IMAGE, "alt": "Captura oficial de Steam de un cazador de Mistfall Hunter acercandose a un cofre luminoso", "caption": "Imagen oficial de extraccion de Steam para explicar la decision entre recompensa y ruta.", "source_label": "Abrir la pagina oficial de Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "beginner-guide", "label": "Consultar los fundamentos para principiantes"}]),
            _section("trio-communication", "Como encaja Seer en un trio", ["En un trio, Seer funciona mejor cuando todos conocen su tarea de informacion o recuperacion. Nombra un ancla, un jugador de presion y uno flexible antes de la cola. Seer puede cubrir apoyo o flex, pero lo importante es la llamada: quien protege el reinicio, quien toma la ventana y quien mira la ruta. Si dos personas esperan que Seer resuelva lo mismo, el build parecera debil aunque sus herramientas funcionen.", "Cuando un aliado se separa, detened el plan original. Un Seer de apoyo no debe cruzar una sala abierta solo para rescatar a alguien que perdio la ruta, y un Seer cuerpo a cuerpo no debe perseguir mas alla del espacio del ancla. Reagrupaos, reducid el objetivo y retomad el contrato de roles."], table={"headers": ["Momento", "Llamada de Seer", "Respuesta del equipo"], "rows": [["Sala incierta", "Guardar la informacion", "El flex revisa un angulo"], ["Ventana clara", "Llamar un periodo corto", "Parar al cerrarse"], ["Jugador separado", "Proteger el reagrupamiento", "No forzar el rescate"], ["Salida incierta", "Guardar apoyo para retirarse", "Reducir recompensa o extraer"]]}, image={"path": _FEATURE_IMAGE, "alt": "Captura oficial de exploracion de Steam de un cazador de Mistfall Hunter en una sala oscura", "caption": "Imagen oficial de Steam que recuerda que todo trio necesita una ruta legible.", "source_label": "Abrir la pagina oficial de Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "trio-builds-guide", "label": "Usar la lista de roles y respaldo de duo"}]),
            _section("test-and-mistakes", "Plan de cinco partidas y errores comunes", ["No juzgues el build por una extraccion afortunada. Repite la misma ruta de bajo riesgo cinco veces, mantén la tarea de Seer y cambia solo un talento, patron de arma o apoyo. Apunta el disparador, el coste, el momento en que la ruta se volvio peligrosa y si el equipo entendio la llamada. Es un experimento pequeno, no una tier list universal.", "El fallo mas comun es construir alrededor de un numero no verificado. Otro es guardar la herramienta tanto que nunca cambia una decision. El tercero es pedir a Seer que explore, cure, haga dano y rescate a la vez. Corrige el primer fallo visible y actualiza las premisas cuando una nota oficial o una prueba repetible cambie el resultado."], bullets=["Anota parche, modo, tamano del equipo y la habilidad probada.", "Compara la misma ruta y riesgo antes de cambiar la conclusion.", "Trata una captura comunitaria como pista si no muestra fuente y condiciones.", "Deten la prueba cuando la recompensa no pague el camino a casa."], links=[{"target": "maps-guide", "label": "Comprobar el contexto del mapa y la ruta"}]),
        ],
        "faq_title": "Preguntas frecuentes sobre el build de Seer",
        "faq": [{"question": "Cual es el mejor build de Seer en Mistfall Hunter?", "answer": "No hay un mejor build permanente verificado en las fuentes revisadas. Empieza con una tarea: informacion, reinicio, apoyo o presion corta. Elige la opcion actual que corrija tu fallo y pruebala en la misma ruta."}, {"question": "Cuales son las mejores habilidades y talentos de Seer?", "answer": "Prioriza un disparador de informacion repetible, un reinicio seguro y una ventana de apoyo con salida. Confirma nombres y valores en la descripcion actual y anota el parche."}, {"question": "Es viable un Seer cuerpo a cuerpo?", "answer": "Puede funcionar si crea un contacto corto y conserva una retirada legible. No persigas dano cuando la salida no este clara."}, {"question": "Seer puede ser curador o apoyo?", "answer": "Si, cuando el equipo acuerda donde curar y quien llama el reagrupamiento. El apoyo debe conservar el plan de escape."}, {"question": "Cual es un buen build de Seer para solo?", "answer": "Usa una accion de informacion, una respuesta de recuperacion y presion moderada. Mantén visible la salida y extrae cuando el premio no cubra el riesgo."}, {"question": "Debe un trio copiar un codigo de build de Seer?", "answer": "Solo con fuente, parche, modo y supuestos claros. Primero define los roles y verifica los valores en el cliente actual."}],
        "summary_heading": "Resumen del build de Seer",
        "summary": "Construye Seer alrededor de una tarea repetible, un respaldo y una ruta de vuelta. Empieza con informacion y reinicio; anade apoyo o presion cuerpo a cuerpo cuando puedas llamar la ventana. Prueba un cambio por vez y confirma los valores en el cliente actual.",
        "related_title": "Sigue preparando partidas de Mistfall Hunter",
        "related_links": [{"target": "classes", "label": "Comparar clases de Mistfall Hunter"}, {"target": "tier-list-guide", "label": "Leer la tier list de Mistfall Hunter"}, {"target": "trio-builds-guide", "label": "Planificar roles de trio y respaldo de duo"}, {"target": "sword-shield-guide", "label": "Revisar un build de espada y escudo"}, {"target": "gameplay-guide", "label": "Repasar gameplay y extraccion"}],
        "source_title": "Fuentes y alcance",
        "source_note": "La pagina usa imagenes oficiales de Steam y el sitio oficial de Mistfall Hunter para el contexto general. Similarweb respalda el tema del build de Seer; los valores exactos de clase, objetos, talentos, dano y enfriamiento siguen sin verificarse.",
    }),
}


_LOCALE_OVERRIDES = {
    "ja": {
        "primary_keyword": "Mistfall Hunter シーア ビルド",
        "related_keywords": ["Mistfall Hunter シーア 最強ビルド", "シーアのアビリティとタレント", "Mistfall Hunter シーア 近接ビルド", "Mistfall Hunter シーア ヒーラービルド"],
        "title": "Mistfall Hunter シーアビルド：能力・タレント・安全なソロルート",
        "meta_title": "Mistfall Hunter シーアビルド：能力とタレント",
        "meta_description": "Mistfall Hunterのシーアビルドを、能力の使い方、タレント、近接・支援分岐、ソロとトリオの判断で整理します。",
        "meta_keywords": "Mistfall Hunter シーア ビルド, シーア 最強ビルド, シーア アビリティ, シーア 近接ビルド, シーア 支援ビルド",
        "eyebrow": "Mistfall Hunter クラスビルドガイド",
        "lede": "シーアのビルドは、情報を取る、立て直しを守る、短い攻撃機会を作るという一つの仕事から始めます。未確認の数値を断定せず、ソロとトリオで検証できる形にまとめました。",
        "checked_label": "シーアの役割フレームを2026年10月30日に確認。正確な数値はバージョン依存です",
        "entry_label": "Mistfall Hunter シーアビルドガイドを読む",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "暗い部屋を一人で探索するMistfall Hunterの公式Steamスクリーンショット", "caption": "情報と立て直しを説明する公式Steam素材。シーアの数値検証ではありません。", "source_label": "公式Steamページ", "source_url": _STEAM_URL, "width": 1200, "height": 675},
        "facts_headers": ["判断", "安全な開始", "変更する条件"],
        "facts_rows": [["役割", "情報と立て直し", "味方が探索を担当する"], ["能力", "再現できるトリガーを一つ", "説明やクールダウンが変わる"], ["タレント", "実際の失敗を直す", "普段のルートで発動できない"], ["近接", "短く接触して距離を戻す", "退路が見えない"], ["支援", "守られた再集合で回復", "回復中に孤立する"]],
        "intro": "Mistfall Hunter シーア ビルドは、タレントの順番より先に解決したい問題を決めます。情報、立て直し、支援、短い攻撃のどれを主役にするかを一つ選び、現在のツールチップで確かめてください。公開情報は隠れたダメージやクールダウンを保証しないため、以下は検証可能な出発点です。",
        "sections": [
            _section("seer-job", "最初に決めるシーアの仕事", ["シーアの検索では一つの正解が求められがちですが、脱出ゲームでは次の判断を見えるようにし、判断のコストを払い、危険になったら帰れることが重要です。未知の部屋を探る、蘇生を守る、敵の行動後に短く攻める、といった仕事から一つ選びます。シーアが必ずヒーラーになるわけではありません。", "出撃前に「次の安全な角度を知らせる」「再集合まで味方を守る」「短い窓だけ攻めて止める」のように一文で役割を書きます。三つの仕事を同時に選ぶと、どのタレントが効いたのか分からなくなります。"], bullets=["最初の接触後に使える移動・回復・情報手段を残す", "スクリーンショットではなく実際の失敗を直すタレントを選ぶ", "一回の出撃で変える要素を一つにする"], links=[{"target": "classes", "label": "他のクラスの役割と比較する"}, {"target": "tier-list-guide", "label": "ティア表は恒久的な順位ではなく役割比較として読む"}]),
            _section("ability-talent-priority", "シーアの能力とタレントの優先順位", ["最良の能力は、発動条件、コスト、立て直しを戦闘前に説明できるものです。現在の説明を読み、低リスクのルートで試します。ほとんど作れない条件に依存する効果は、数字が大きくても普段の出撃では役に立ちません。", "前回の失敗から始めます。情報が足りなかったなら危険を見えるようにし、帰れなかったなら距離や回復を優先し、安全だが遅いなら最後に攻撃を足します。これが「最強ビルド」を一律に決めない理由です。"], table={"headers": ["優先", "探すもの", "避けること"], "rows": [["1. 情報", "危険を再現可能に読める手段", "見た目だけでダメージを断定する"], ["2. 立て直し", "距離・時間・再集合を作る手段", "最初に防御を全部使う"], ["3. 支援", "退路のある回復窓", "追われながら回復する"], ["4. 攻撃", "敵が動いた後の短い窓", "未知の部屋まで追う"], ["5. 柔軟性", "計画が変わっても使える予備", "誰も呼べない条件付き効果"]]}, image={"path": _COMBAT_IMAGE, "alt": "大きな森の敵と対峙するMistfall Hunterの公式Steam戦闘スクリーンショット", "caption": "距離とタイミングの公式Steam素材。シーアのタレント検証ではありません。", "source_label": "公式Steamページ", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("melee-healer-paths", "近接シーアとヒーラーシーアの分岐", ["近接シーアは、短い接触のあとに読みやすい場所へ戻るパターンから始めます。近距離だからといって戦闘を続けてよいわけではありません。退路が消えるなら、攻撃力より先に距離か低リスクのトリガーを見直します。", "支援型も同じです。回復は味方を残しつつ脱出計画を守れるときに価値があります。どこで回復し、誰が再集合を呼び、帰路用に何を残すかを決めます。味方が分断されているなら、救助より先に目的を下げます。"], table={"headers": ["分岐", "最初のテスト", "切り替える条件"], "rows": [["近接", "敵の行動後に一度だけ接触", "退路を先に見られない"], ["支援", "守られた再集合で回復", "開けた場所で拘束される"], ["情報", "前進前に角度を一つ確認", "保存しすぎて判断が変わらない"], ["柔軟", "主役一つと緊急の予備", "味方が仕事を説明できない"]]}, links=[{"target": "sword-shield-guide", "label": "剣と盾の近接方針も確認する"}, {"target": "gameplay-guide", "label": "脱出の判断ループを読む"}]),
            _section("solo-route", "ソロでシーアビルドを使う方法", ["ソロでは角度を確認する味方も蘇生を守る味方もいません。情報を先に使い、未知の部屋に一つずつ入り、帰路を見える状態にします。最初の戦闘で帰るための回復を使ったなら、次の報酬へ急がず止まります。", "最初のテストは短いループにします。目的、撤退条件、シーアの仕事が効かなくなった地点を記録します。パッチやモードが不明な画面をそのまま最強の根拠にしないことが大切です。"], steps=["危険な部屋の前に目的と帰路を決める", "次の判断を変えるときだけ情報や支援を使う", "接触後に体力・回復・帰路を確認する", "残りの報酬が危険に見合わなければ脱出する"], image={"path": _EXTRACTION_IMAGE, "alt": "光る宝箱へ近づくMistfall Hunterの公式Steam脱出スクリーンショット", "caption": "報酬と帰路を比べるソロ判断を示す公式Steam素材。", "source_label": "公式Steamページ", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "beginner-guide", "label": "初心者向けの脱出基礎を確認する"}]),
            _section("trio-communication", "トリオでのシーアの役割", ["トリオでは、シーアが情報か回復のどちらを担当するかを先に共有します。アンカー、攻撃、フレックスを決め、誰が立て直しを守り、誰が短い窓を取り、誰が帰路を見るかを呼びます。二人が同じ仕事を期待すると、能力が動いていてもビルドは弱く感じます。", "味方が分断されたら元の計画を止めます。支援シーアが開けた部屋を一人で横切ったり、近接シーアがアンカーの範囲を越えて追ったりしないでください。再集合、目的の縮小、役割の再確認を優先します。"], table={"headers": ["場面", "シーアの呼びかけ", "チームの対応"], "rows": [["未知の部屋", "情報手段を温存", "フレックスが角度を一つ見る"], ["明確な窓", "短い攻撃を宣言", "窓が閉じたら止める"], ["味方が分断", "再集合の道を守る", "救助を強行しない"], ["出口が不明", "帰りの支援を残す", "報酬を下げるか脱出"]]}, image={"path": _FEATURE_IMAGE, "alt": "暗い部屋を進むMistfall Hunterの公式Steam探索スクリーンショット", "caption": "トリオにも読みやすい再集合地点が必要だと示す公式Steam素材。", "source_label": "公式Steamページ", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "trio-builds-guide", "label": "トリオの役割とデュオ時のチェックを使う"}]),
            _section("test-and-mistakes", "5回のテスト計画とよくある失敗", ["一度の幸運な脱出でシーアを評価しません。同じ低リスクのルートを5回走り、役割を固定して、タレントや武器の一項目だけを変えます。発動条件、コスト、危険になった地点、呼びかけが伝わったかを記録します。これは小さな実験であり、恒久的な順位ではありません。", "未確認の数字を中心に組む、温存しすぎて能力を使わない、探索・回復・攻撃・救助を一度に求めることが主な失敗です。最初に見えた失敗を直し、予備を一つ残し、公式パッチや再現テストで前提が変わったら更新します。"], bullets=["パッチ、モード、人数、試した能力を記録する", "結論を変える前に同じルートとリスクで比べる", "出典と条件のないコミュニティ画像は手がかりとして扱う", "帰路に見合わない報酬ならテストを止める"], links=[{"target": "maps-guide", "label": "マップとルートの前提を確認する"}]),
        ],
        "faq_title": "Mistfall Hunter シーアビルド よくある質問",
        "faq": [{"question": "Mistfall Hunterで最強のシーアビルドは？", "answer": "今回確認した公開情報には恒久的な最強ビルドを示す根拠がありません。情報、立て直し、支援、短い攻撃の一つを主役にし、現在の説明で失敗を直して同じルートでテストしてください。"}, {"question": "シーアの能力とタレントは何を優先する？", "answer": "再現できる情報手段、安全な立て直し、退路のある支援窓を優先します。名前や数値は現在のツールチップとパッチで確認してください。"}, {"question": "近接シーアは使える？", "answer": "短い接触と読みやすい退路を作れるなら使えます。帰り道が見えない追撃は避けます。"}, {"question": "シーアをヒーラーにできる？", "answer": "どこで回復し、誰が再集合を呼ぶかを共有できれば可能です。支援は脱出計画を残す範囲で使います。"}, {"question": "ソロのシーアビルドは？", "answer": "情報一つ、回復一つ、控えめな攻撃を基本にします。出口を見える状態にして、報酬が危険に見合わなければ脱出します。"}, {"question": "トリオはシーアのビルドコードをコピーすべき？", "answer": "出典、パッチ、モード、前提が明確な場合だけです。まず役割を決め、現在のクライアントで数値を確認します。"}],
        "summary_heading": "シーアビルドのまとめ",
        "summary": "シーアは一つの再現可能な仕事、緊急の予備、帰路を中心に組みます。情報と立て直しから始め、呼びかけられる攻撃や支援を後から足します。正確な数値は現在のクライアントで確認してください。",
        "related_title": "Mistfall Hunterの準備を続ける",
        "related_links": [{"target": "classes", "label": "Mistfall Hunterのクラスを比較"}, {"target": "tier-list-guide", "label": "Mistfall Hunterのティア表を読む"}, {"target": "trio-builds-guide", "label": "トリオとデュオ時の役割を決める"}, {"target": "sword-shield-guide", "label": "剣と盾のビルドを確認する"}, {"target": "gameplay-guide", "label": "ソロと脱出の判断を読む"}],
        "source_title": "出典と範囲",
        "source_note": "公式Steam素材とMistfall Hunter公式サイトをゲームの概要に使用しています。Similarwebはシーアビルドのテーマを支持しますが、クラス、装備、タレント、ダメージ、クールダウンの正確な値は未確認です。",
    },
    "fr": {
        "primary_keyword": "build Seer Mistfall Hunter",
        "related_keywords": ["meilleur build Seer Mistfall Hunter", "capacites et talents de Seer Mistfall Hunter", "build Seer au corps a corps", "build soutien Seer Mistfall Hunter"],
        "title": "Build Seer Mistfall Hunter : capacités, talents et routes sûres",
        "meta_title": "Build Seer Mistfall Hunter : capacités et talents",
        "meta_description": "Préparez un build Seer Mistfall Hunter avec priorités de capacités, talents, variantes mêlée ou soutien et ajustements solo et trio.",
        "meta_keywords": "build Seer Mistfall Hunter, meilleur build Seer, capacités Seer, build mêlée Seer, build soutien Seer",
        "eyebrow": "Présentation de build de classe Mistfall Hunter",
        "lede": "Un build Seer utile commence par une mission répétable : obtenir de l'information, protéger une remise à zéro ou créer une courte fenêtre de pression. Cette page transforme la recherche Seer en plan testable pour le solo et le trio, sans inventer de valeurs de patch.",
        "checked_label": "Cadre Seer vérifié le 30 octobre 2026 ; les valeurs exactes dépendent de la version",
        "entry_label": "Lire la build Seer Mistfall Hunter",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "Capture officielle Steam d'un chasseur de Mistfall Hunter explorant seul une salle sombre", "caption": "Média officiel Steam pour expliquer l'information et la remise à zéro ; ce n'est pas un test de statistiques Seer.", "source_label": "Ouvrir la fiche Steam officielle", "source_url": _STEAM_URL, "width": 1200, "height": 675},
        "facts_headers": ["Question", "Départ prudent", "Changer quand"],
        "facts_rows": [["Rôle", "Information et remise à zéro", "Un allié couvre déjà l'exploration"], ["Capacité", "Un déclencheur répétable", "Le texte ou le temps de recharge change"], ["Talent", "Corriger l'échec observé", "La condition n'arrive jamais"], ["Mêlée", "Contact court puis retour à l'espace", "La sortie n'est plus lisible"], ["Soutien", "Soigner pendant un regroupement", "Le soin vous expose"]],
        "intro": "Pour un build Seer Mistfall Hunter, choisissez le problème à résoudre avant l'ordre des talents. Le meilleur départ n'est pas une liste meta universelle : c'est un setup qui permet de lire une salle, créer une courte ouverture et garder une réponse de récupération. Les sources publiques ne vérifient pas les dégâts, temps de recharge ou rangs cachés ; utilisez donc ce cadre comme un brief à tester dans le client actuel.",
        "sections": [
            _section("seer-job", "Le premier problème d'un build Seer", ["Les recherches Seer demandent souvent une réponse unique, mais une partie d'extraction a besoin d'une définition plus concrète. Le build doit rendre la prochaine décision visible, payer son coût et laisser une sortie lorsque la route ne vaut plus le risque. Il peut explorer une salle, protéger une réanimation ou appliquer une pression après l'engagement ennemi. Seer n'est pas forcément un soigneur.", "Écrivez le rôle en une phrase avant la file : révéler l'angle sûr, maintenir un allié pendant le repli ou créer une ouverture courte puis arrêter. Si la phrase contient trois missions, elle est trop large. Gardez une mission principale et un secours."], bullets=["Garder une option de mouvement, de récupération ou d'information après le premier contact.", "Choisir un talent pour corriger un échec réel, pas une capture qui le dit meta.", "Ne modifier qu'une variable par partie."], links=[{"target": "classes", "label": "Comparer Seer aux autres rôles"}, {"target": "tier-list-guide", "label": "Lire la tier list comme comparaison de rôles"}]),
            _section("ability-talent-priority", "Priorités de capacités et talents Seer", ["La meilleure capacité est celle dont vous connaissez le déclencheur, le coût et la récupération avant le combat. Lisez le texte actuel et testez-la sur une route peu coûteuse. Une condition rare peut rendre un grand nombre inutile. Un petit effet activé à volonté est souvent plus utile qu'un bonus spectaculaire d'un clip.", "Commencez par l'échec qui a terminé la partie. S'il manquait de l'information, prenez une option qui révèle le danger. Si vous ne pouviez pas repartir, prenez de l'espace ou de la récupération. Si le groupe était sûr mais lent, ajoutez la pression en dernier. C'est la limite pratique du meilleur build Seer : il dépend du problème à corriger."], table={"headers": ["Priorité", "Chercher", "Éviter"], "rows": [["1. Information", "Lire le danger de façon répétable", "Déduire les dégâts d'un effet visuel"], ["2. Repli", "Créer espace, temps ou regroupement", "Dépenser toute la défense au contact"], ["3. Soutien", "Une fenêtre de soin avec sortie", "Soigner pendant la poursuite"], ["4. Pression", "Une courte ouverture après l'engagement", "Poursuivre dans une salle inconnue"], ["5. Flex", "Un secours utilisable quand le plan change", "Des bonus conditionnels que personne n'appelle"]]}, image={"path": _COMBAT_IMAGE, "alt": "Capture officielle Steam d'un chasseur de Mistfall Hunter face à une créature forestière", "caption": "Média officiel Steam pour le contexte de distance et de timing ; il ne montre pas un talent Seer vérifié.", "source_label": "Ouvrir la fiche Steam officielle", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("melee-healer-paths", "Seer mêlée ou Seer soutien ?", ["Un build Seer mêlée doit créer un contact court puis revenir à une position lisible. Le corps à corps n'autorise pas à poursuivre chaque échange. Si la sortie disparaît au moment d'entrer, revoyez l'espace ou le déclencheur avant d'ajouter des dégâts.", "Le soutien suit la même limite. Le soin vaut quand il maintient un allié sans supprimer la route de sortie. Décidez où soigner, qui appelle le repli et quelle ressource garder pour rentrer. Si le groupe est séparé, réduisez l'objectif avant de tenter un sauvetage."], table={"headers": ["Branche", "Premier test", "Changer quand"], "rows": [["Mêlée", "Une ouverture courte après l'engagement", "La retraite n'est pas visible"], ["Soutien", "Un soin pendant un regroupement protégé", "Le soin vous bloque à découvert"], ["Information", "Révéler un angle avant d'avancer", "La capacité ne change aucune décision"], ["Flex", "Une mission et un secours", "L'équipe ne sait pas votre rôle"]]}, links=[{"target": "sword-shield-guide", "label": "Voir le plan mêlée épée-bouclier"}, {"target": "gameplay-guide", "label": "Revoir la boucle d'extraction"}]),
            _section("solo-route", "Jouer le build Seer en solo", ["En solo, personne ne confirme l'angle ni ne couvre une réanimation. Priorisez l'information : une salle incertaine à la fois, la route derrière vous visible, et seulement l'action nécessaire pour comprendre le danger. Si le premier combat consomme la récupération prévue pour sortir, arrêtez-vous avant la récompense suivante.", "Pour les premiers tests, choisissez un objectif, une condition de sortie et le point où le rôle Seer cesse d'aider. Cette note vaut mieux qu'une capture sans patch, mode ou méthode."], steps=["Choisir l'objectif et la route de retour avant la salle risquée.", "Utiliser information ou soutien seulement quand la décision suivante change.", "Revoir vie, récupération et visibilité de la route après le contact.", "Extraire quand la récompense ne paie plus le risque."], image={"path": _EXTRACTION_IMAGE, "alt": "Capture officielle Steam d'un chasseur de Mistfall Hunter près d'un coffre lumineux", "caption": "Média officiel Steam pour la décision récompense contre route.", "source_label": "Ouvrir la fiche Steam officielle", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "beginner-guide", "label": "Revoir les bases pour débuter"}]),
            _section("trio-communication", "La place de Seer dans un trio", ["Dans un trio, l'équipe doit savoir si Seer garde l'information ou la récupération. Nommez une ancre, une pression et un rôle flexible : qui protège le repli, qui prend l'ouverture et qui surveille la route ? Deux attentes différentes rendent le build faible même quand les outils fonctionnent.", "Quand un joueur est séparé, arrêtez le plan. Un Seer soutien ne traverse pas seul une salle ouverte pour une cible qui a perdu la route et un Seer mêlée ne poursuit pas au-delà de l'espace de l'ancre. Regroupez-vous, réduisez l'objectif et reformulez les rôles."], table={"headers": ["Moment", "Appel Seer", "Réponse du groupe"], "rows": [["Salle inconnue", "Garder l'information", "Le flex vérifie un angle"], ["Ouverture claire", "Appeler une fenêtre courte", "Arrêter quand elle se ferme"], ["Joueur séparé", "Protéger le regroupement", "Ne pas forcer le sauvetage"], ["Sortie incertaine", "Garder le soutien pour le retour", "Réduire le but ou extraire"]]}, image={"path": _FEATURE_IMAGE, "alt": "Capture officielle Steam d'exploration de Mistfall Hunter dans une salle sombre", "caption": "Média officiel Steam rappelant qu'un trio a besoin d'un point de regroupement lisible.", "source_label": "Ouvrir la fiche Steam officielle", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "trio-builds-guide", "label": "Utiliser la checklist des rôles de trio"}]),
            _section("test-and-mistakes", "Plan de test en cinq parties", ["Ne jugez pas Seer sur une extraction chanceuse. Répétez la même route à faible risque cinq fois, gardez le rôle stable et changez un seul talent ou choix d'arme. Notez le déclencheur, le coût, le point de danger et la compréhension de l'appel. C'est une petite expérience, pas un classement universel.", "Les erreurs fréquentes sont de construire autour d'un nombre non vérifié, de conserver l'outil jusqu'à ne jamais l'utiliser et de demander à Seer d'explorer, soigner, infliger des dégâts et sauver à la fois. Corrigez le premier échec visible et actualisez vos hypothèses après une note officielle ou un test répétable."], bullets=["Noter patch, mode, taille du groupe et capacité testée.", "Comparer même route et risque avant de changer la conclusion.", "Traiter une capture communautaire sans source comme un indice.", "Arrêter quand la récompense ne paie plus le retour."], links=[{"target": "maps-guide", "label": "Vérifier le contexte de la carte"}]),
        ],
        "faq_title": "Questions fréquentes sur le build Seer Mistfall Hunter",
        "faq": [{"question": "Quel est le meilleur build Seer dans Mistfall Hunter ?", "answer": "Aucun meilleur build permanent n'est vérifié dans les sources consultées. Choisissez une mission, corrigez votre échec observé et testez la même route."}, {"question": "Quelles capacités et quels talents Seer choisir ?", "answer": "Priorisez une information répétable, un reset sûr et un soutien avec sortie. Vérifiez noms et valeurs dans le client actuel."}, {"question": "Un build Seer mêlée est-il viable ?", "answer": "Oui si le contact reste court et la retraite lisible. N'ajoutez pas une poursuite lorsque la sortie est inconnue."}, {"question": "Seer peut-il être un soigneur ?", "answer": "Oui si le groupe décide où soigner et qui appelle le regroupement. Le soutien doit conserver la sortie."}, {"question": "Quel build Seer pour jouer en solo ?", "answer": "Une action d'information, une réponse de récupération et une pression modérée. Gardez la sortie visible et partez quand le risque dépasse la récompense."}, {"question": "Faut-il copier un code de build Seer en trio ?", "answer": "Seulement avec source, patch, mode et hypothèses clairs. Définissez d'abord les rôles et vérifiez les valeurs actuelles."}],
        "summary_heading": "Résumé du build Seer",
        "summary": "Construisez Seer autour d'une mission répétable, d'un secours et d'une route de retour. Commencez par information et reset, puis ajoutez soutien ou mêlée quand la fenêtre est appelable. Testez un changement à la fois et vérifiez les valeurs actuelles.",
        "related_title": "Continuer à préparer les parties Mistfall Hunter",
        "related_links": [{"target": "classes", "label": "Comparer les classes Mistfall Hunter"}, {"target": "tier-list-guide", "label": "Lire la tier list Mistfall Hunter"}, {"target": "trio-builds-guide", "label": "Planifier les rôles de trio"}, {"target": "sword-shield-guide", "label": "Voir un build épée-bouclier"}, {"target": "gameplay-guide", "label": "Revoir le gameplay et l'extraction"}],
        "source_title": "Sources et portée",
        "source_note": "La page utilise les médias officiels Steam et le site officiel Mistfall Hunter pour le contexte général. Similarweb justifie le sujet Seer ; les valeurs exactes de classe, équipement, talent, dégâts et recharge restent à vérifier.",
    },
    "de": {
        "primary_keyword": "Mistfall Hunter Seer Build",
        "related_keywords": ["beste Seer Build Mistfall Hunter", "Seer Fähigkeiten und Talente", "Seer Nahkampf Build Mistfall Hunter", "Seer Support Build Mistfall Hunter"],
        "title": "Mistfall Hunter Seer Build: Fähigkeiten, Talente und sichere Routen",
        "meta_title": "Mistfall Hunter Seer Build: Fähigkeiten und Talente",
        "meta_description": "Plane einen Seer Build für Mistfall Hunter mit Fähigkeits- und Talentprioritäten sowie Nahkampf-, Support-, Solo- und Trio-Anpassungen.",
        "meta_keywords": "Mistfall Hunter Seer Build, beste Seer Build, Seer Fähigkeiten, Seer Nahkampf Build, Seer Support Build",
        "eyebrow": "Leitfaden für Mistfall-Hunter-Klassen-Builds",
        "lede": "Ein brauchbarer Seer Build beginnt mit einer wiederholbaren Aufgabe: Informationen schaffen, eine Neuaufstellung schützen oder ein kurzes Druckfenster nutzen. Dieser Leitfaden macht daraus einen testbaren Plan für Solo- und Trio-Runs, ohne patchabhängige Werte zu erfinden.",
        "checked_label": "Seer-Rollenrahmen am 30. Oktober 2026 geprüft; genaue Werte bleiben versionsabhängig",
        "entry_label": "Mistfall Hunter Seer Build lesen",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "Offizieller Steam-Screenshot eines Mistfall-Hunter-Jägers bei der Erkundung eines dunklen Raums", "caption": "Offizielles Steam-Medium für Informations- und Neuaufstellungsentscheidungen; kein Seer-Statistiktest.", "source_label": "Offizielle Steam-Seite öffnen", "source_url": _STEAM_URL, "width": 1200, "height": 675},
        "facts_headers": ["Build-Frage", "Sicherer Start", "Ändern wenn"],
        "facts_rows": [["Rolle", "Information plus sichere Neuaufstellung", "Ein Teammitglied scoutet bereits"], ["Fähigkeit", "Ein wiederholbarer Auslöser", "Tooltip oder Cooldown ändert sich"], ["Talent", "Beobachteten Fehler beheben", "Bedingung tritt auf der Route nicht ein"], ["Nahkampf", "Kurz treffen und Abstand gewinnen", "Kein Rückweg sichtbar"], ["Support", "Während eines geschützten Regroups heilen", "Heilung macht dich offen"]],
        "intro": "Für einen Mistfall Hunter Seer Build legst du zuerst das Problem fest, bevor du eine Talent-Reihenfolge kopierst. Der beste Start ist keine dauerhafte Meta-Liste, sondern ein Setup, das einen Raum lesbar macht, ein kurzes Fenster schafft und eine Erholung zurückhält. Die geprüften Quellen bestätigen keine versteckten Schadens-, Cooldown- oder Rangwerte. Nutze den Rahmen als Brief für den aktuellen Client.",
        "sections": [
            _section("seer-job", "Was ein Seer Build zuerst lösen muss", ["Suchanfragen nach Seer erwarten oft eine feste Antwort. Ein Extraktionslauf braucht aber eine praktischere Definition: Der Build soll die nächste Entscheidung sichtbar machen, ihre Kosten überleben und bei einer schlechten Route einen Rückweg lassen. Das kann Scouting, eine geschützte Wiederbelebung oder kurzer Druck nach einem gegnerischen Commit sein. Seer ist nicht automatisch ein Heiler.", "Schreibe die Aufgabe vor dem Queue in einen Satz: sicheren Winkel zeigen, einen Verbündeten bis zur Neuaufstellung halten oder ein kurzes Fenster öffnen und stoppen. Drei Aufgaben zugleich machen den Build unklar. Wähle eine Hauptaufgabe und eine Notfalloption."], bullets=["Nach dem ersten Kontakt eine Bewegungs-, Erholungs- oder Informationsoption behalten.", "Ein Talent nach dem echten Fehler wählen, nicht nach einem Meta-Screenshot.", "Pro Run nur eine Variable ändern."], links=[{"target": "classes", "label": "Seer mit den anderen Klassen vergleichen"}, {"target": "tier-list-guide", "label": "Die Tier-Liste als Rollenvergleich nutzen"}]),
            _section("ability-talent-priority", "Seer-Fähigkeiten und Talente priorisieren", ["Die beste Fähigkeit ist die, deren Auslöser, Kosten und Erholung du vor dem Kampf erklären kannst. Lies den aktuellen Tooltip und teste sie auf einer günstigen Route. Eine seltene Bedingung kann einen großen Wert nutzlos machen. Ein kleiner, bewusst ausgelöster Effekt ist oft stärker als ein großer Clip-Bonus.", "Beginne mit dem Fehler, der den letzten Run beendet hat. Fehlte Information, nimm eine Option für den nächsten Winkel. Fehlte der Rückweg, nimm Raum oder Erholung. War das Team sicher, aber langsam, kommt Druck erst danach. Der beste Seer Build hängt deshalb vom Problem ab, das du reparierst."], table={"headers": ["Priorität", "Suchen nach", "Vermeiden"], "rows": [["1. Information", "Gefahr wiederholbar lesen", "Schaden aus einem Effektbild ableiten"], ["2. Neuaufstellung", "Raum, Zeit oder Regroup", "Alle Defensivoptionen beim ersten Kontakt"], ["3. Support", "Heilfenster mit Ausgang", "Während der Verfolgung heilen"], ["4. Druck", "Kurzes Fenster nach dem Commit", "In einen unbekannten Raum jagen"], ["5. Flex", "Notfalloption bei Planwechsel", "Boni, die niemand ansagt"]]}, image={"path": _COMBAT_IMAGE, "alt": "Offizieller Steam-Kampfscreenshot eines Mistfall-Hunter-Jägers vor einer Waldkreatur", "caption": "Offizielles Steam-Medium für Abstand und Timing; kein verifizierter Seer-Talenttest.", "source_label": "Offizielle Steam-Seite öffnen", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("melee-healer-paths", "Nahkampf-Seer oder Support-Seer?", ["Ein Nahkampf-Seer braucht ein kurzes Kontaktfenster und danach eine lesbare Position. Nähe ist keine Erlaubnis, jeden Tausch zu verlängern. Wenn der Ausgang beim Einstieg verschwindet, ändere Raum oder Auslöser, bevor du mehr Schaden stapelst.", "Support folgt derselben Grenze. Heilung ist gut, wenn sie den Verbündeten hält und den Fluchtweg offen lässt. Vereinbare Ort, Reset-Call und die Ressource für den Rückweg. Bei einer Trennung soll das Ziel kleiner werden, bevor du rettest."], table={"headers": ["Pfad", "Erster Test", "Wechseln wenn"], "rows": [["Nahkampf", "Ein kurzes Fenster nach dem Commit", "Der Rückweg nicht sichtbar ist"], ["Support", "Heilung im geschützten Regroup", "Die Heilung dich offen festhält"], ["Information", "Vor dem Push einen Winkel zeigen", "Die Fähigkeit keine Entscheidung ändert"], ["Flex", "Eine Aufgabe plus Notfall", "Das Team deinen Job nicht kennt"]]}, links=[{"target": "sword-shield-guide", "label": "Den Schwert-und-Schild-Nahkampfplan prüfen"}, {"target": "gameplay-guide", "label": "Die Extraktionsschleife lesen"}]),
            _section("solo-route", "Seer Build solo spielen", ["Solo gibt es keinen Verbündeten, der einen Winkel bestätigt oder eine Wiederbelebung schützt. Nutze Information zuerst, betrete unsichere Räume einzeln und halte den Rückweg sichtbar. Verbraucht der erste Kampf die Erholung für den Ausgang, halte vor der nächsten Belohnung an.", "Für die ersten Tests reichen ein Ziel, eine Abbruchbedingung und der Punkt, an dem Seers Aufgabe nicht mehr hilft. Diese Notiz ist besser als ein Screenshot ohne Patch, Modus oder Testmethode."], steps=["Ziel und Rückweg vor dem riskanten Raum wählen.", "Information oder Support nur nutzen, wenn sich die nächste Entscheidung ändert.", "Nach Kontakt Leben, Erholung und Weg prüfen.", "Extrahieren, wenn die Belohnung das Risiko nicht mehr trägt."], image={"path": _EXTRACTION_IMAGE, "alt": "Offizieller Steam-Screenshot eines Mistfall-Hunter-Jägers an einer leuchtenden Truhe", "caption": "Offizielles Steam-Medium für die Entscheidung zwischen Belohnung und Rückweg.", "source_label": "Offizielle Steam-Seite öffnen", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "beginner-guide", "label": "Grundlagen für den ersten Run lesen"}]),
            _section("trio-communication", "Seer im Trio", ["Im Trio muss klar sein, ob Seer Information oder Erholung hält. Benenne Anchor, Druck und Flex: Wer schützt den Reset, wer nimmt das Fenster und wer beobachtet den Weg? Wenn zwei Spieler dieselbe Aufgabe erwarten, wirkt der Build schwach, obwohl die Tools funktionieren.", "Bei einer Trennung endet der ursprüngliche Plan. Ein Support-Seer überquert keinen offenen Raum allein für einen Spieler ohne Route, und ein Nahkampf-Seer jagt nicht über den Anchor-Raum hinaus. Regroup, Ziel reduzieren und Rollen neu sagen."], table={"headers": ["Moment", "Seer-Call", "Teamreaktion"], "rows": [["Unbekannter Raum", "Information halten", "Flex prüft einen Winkel"], ["Klares Fenster", "Kurzen Druck ansagen", "Beim Ende stoppen"], ["Spieler getrennt", "Regroup-Weg schützen", "Rettung nicht erzwingen"], ["Ausgang unklar", "Support für Rückweg behalten", "Ziel senken oder gehen"]]}, image={"path": _FEATURE_IMAGE, "alt": "Offizieller Steam-Erkundungsscreenshot eines Mistfall-Hunter-Jägers in einem dunklen Raum", "caption": "Offizielles Steam-Medium: Auch ein Trio braucht einen lesbaren Regroup-Punkt.", "source_label": "Offizielle Steam-Seite öffnen", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "trio-builds-guide", "label": "Trio-Rollen und Duo-Fallback nutzen"}]),
            _section("test-and-mistakes", "Fünf-Runs-Test und typische Fehler", ["Bewerte Seer nicht nach einer glücklichen Extraction. Spiele dieselbe risikoarme Route fünfmal, halte die Rolle gleich und ändere nur ein Talent oder Waffenmuster. Notiere Auslöser, Kosten, Gefahrpunkt und ob der Call verstanden wurde. Das ist ein kleines Experiment, keine dauerhafte Tier-Liste.", "Typische Fehler sind ein Build um eine unbestätigte Zahl, ein Tool, das so lange gespart wird, bis es nie hilft, und vier Aufgaben gleichzeitig. Repariere den ersten sichtbaren Fehler und aktualisiere die Annahmen nach Patchnotes oder wiederholbaren Tests."], bullets=["Patch, Modus, Teamgröße und getestete Fähigkeit notieren.", "Vor einer neuen Schlussfolgerung dieselbe Route und dasselbe Risiko vergleichen.", "Community-Screenshot ohne Quelle als Hinweis behandeln.", "Test stoppen, wenn die Belohnung den Rückweg nicht trägt."], links=[{"target": "maps-guide", "label": "Karten- und Routenkontext prüfen"}]),
        ],
        "faq_title": "Häufige Fragen zum Mistfall Hunter Seer Build",
        "faq": [{"question": "Was ist der beste Seer Build in Mistfall Hunter?", "answer": "Die geprüften Quellen belegen keinen dauerhaft besten Build. Wähle Information, Reset, Support oder kurzen Druck, behebe deinen beobachteten Fehler und teste dieselbe Route."}, {"question": "Welche Seer-Fähigkeiten und Talente sind am besten?", "answer": "Priorisiere wiederholbare Information, einen sicheren Reset und Support mit Ausgang. Werte im aktuellen Tooltip prüfen."}, {"question": "Ist ein Nahkampf-Seer spielbar?", "answer": "Ja, wenn der Kontakt kurz bleibt und der Rückweg lesbar ist. Keine Jagd in unbekannte Räume."}, {"question": "Kann Seer Support oder Heiler sein?", "answer": "Ja, wenn Ort und Reset-Call im Team feststehen. Support darf den Fluchtweg nicht löschen."}, {"question": "Welcher Seer Build passt solo?", "answer": "Eine Informationsaktion, eine Erholung und moderater Druck. Ausgang sichtbar halten und bei zu hohem Risiko gehen."}, {"question": "Soll ein Trio einen Seer-Buildcode kopieren?", "answer": "Nur mit Quelle, Patch, Modus und Annahmen. Erst Rollen klären, dann Werte im Client prüfen."}],
        "summary_heading": "Seer-Build-Zusammenfassung",
        "summary": "Baue Seer um eine wiederholbare Aufgabe, einen Fallback und einen Rückweg. Beginne mit Information und Reset, ergänze Support oder Nahkampfdruck erst nach einem klaren Call und teste eine Änderung nach der anderen.",
        "related_title": "Mistfall-Hunter-Runs weiter planen",
        "related_links": [{"target": "classes", "label": "Mistfall-Hunter-Klassen vergleichen"}, {"target": "tier-list-guide", "label": "Mistfall-Hunter-Tier-Liste lesen"}, {"target": "trio-builds-guide", "label": "Trio-Rollen planen"}, {"target": "sword-shield-guide", "label": "Schwert-und-Schild-Build prüfen"}, {"target": "gameplay-guide", "label": "Gameplay und Extraction lesen"}],
        "source_title": "Quellen und Umfang",
        "source_note": "Offizielle Steam-Medien und die offizielle Mistfall-Hunter-Seite liefern den Spielkontext. Similarweb stützt das Seer-Thema; genaue Klassen-, Item-, Talent-, Schadens- und Cooldownwerte bleiben zu prüfen.",
    },
    "pt": {
        "primary_keyword": "build de Seer do Mistfall Hunter",
        "related_keywords": ["melhor build de Seer Mistfall Hunter", "habilidades e talentos da Seer", "build corpo a corpo de Seer", "build de suporte de Seer Mistfall Hunter"],
        "title": "Build de Seer no Mistfall Hunter: habilidades, talentos e rotas seguras",
        "meta_title": "Build de Seer Mistfall Hunter: habilidades e talentos",
        "meta_description": "Monte um build de Seer para Mistfall Hunter com prioridades de habilidades, talentos, caminhos corpo a corpo ou suporte e ajustes para solo e trio.",
        "meta_keywords": "build de Seer do Mistfall Hunter, melhor build de Seer, habilidades da Seer, build corpo a corpo, build suporte Seer",
        "eyebrow": "Guia de build de classe do Mistfall Hunter",
        "lede": "Um build de Seer útil começa com uma função repetível: criar informação, proteger uma retomada ou abrir uma janela curta de pressão. Este guia transforma o grupo de buscas da Seer em um plano testável para solo e trio sem inventar valores de patch.",
        "checked_label": "Estrutura da Seer revisada em 30 de outubro de 2026; valores exatos dependem da versão",
        "entry_label": "Ler o guia do build de Seer do Mistfall Hunter",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "Captura oficial da Steam de uma caçadora do Mistfall Hunter explorando uma sala escura sozinha", "caption": "Mídia oficial da Steam para explicar informação e retomada; não é um teste de estatísticas da Seer.", "source_label": "Abrir a página oficial da Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675},
        "facts_headers": ["Pergunta", "Início seguro", "Mude quando"],
        "facts_rows": [["Função", "Informação e retomada segura", "Outro jogador já faz o scout"], ["Habilidade", "Um gatilho repetível", "Texto ou recarga muda"], ["Talento", "Corrigir a falha observada", "A condição não aparece"], ["Corpo a corpo", "Contato curto e voltar ao espaço", "A saída não está visível"], ["Suporte", "Curar durante um regroup protegido", "A cura deixa você exposta"]],
        "intro": "Para um build de Seer do Mistfall Hunter, defina o problema antes de copiar uma ordem de talentos. O melhor começo não é uma lista meta permanente, mas uma configuração que permita ler uma sala, criar uma abertura curta e guardar uma resposta de recuperação. As fontes públicas não confirmam dano, recarga ou ranks ocultos; trate este texto como um brief para testar no cliente atual.",
        "sections": [
            _section("seer-job", "O primeiro problema que um build de Seer resolve", ["Buscas por Seer parecem pedir uma resposta única, mas uma partida de extração precisa de uma definição prática. O build deve mostrar a próxima decisão, pagar o custo e deixar uma saída quando a rota ficar ruim. Isso pode ser explorar uma sala, cobrir uma reanimação ou pressionar depois do compromisso do inimigo. Seer não precisa ser sempre curadora.", "Escreva a função em uma frase antes da fila: revelar o ângulo seguro, manter um aliado até a retomada ou abrir uma janela e parar. Três funções juntas deixam o build sem foco. Escolha uma função principal e um fallback."], bullets=["Guarde uma opção de movimento, recuperação ou informação depois do primeiro contato.", "Escolha o talento pelo erro real, não por uma captura que diz meta.", "Mude uma variável por partida."], links=[{"target": "classes", "label": "Comparar Seer com as outras classes"}, {"target": "tier-list-guide", "label": "Usar a tier list como comparação de funções"}]),
            _section("ability-talent-priority", "Prioridades de habilidades e talentos da Seer", ["A melhor habilidade é aquela cujo gatilho, custo e recuperação você consegue explicar antes da luta. Leia o texto atual e teste em uma rota barata. Uma condição rara pode tornar um número alto inútil. Um efeito menor que você ativa de propósito costuma ser mais útil que um bônus de clipe.", "Comece pela falha da última partida. Se faltou informação, escolha uma opção que revele o próximo perigo. Se não houve saída, priorize espaço ou recuperação. Se o grupo estava seguro mas lento, acrescente pressão por último. Esse é o limite prático da melhor build de Seer: ela depende do problema que você está corrigindo."], table={"headers": ["Prioridade", "Procure", "Evite"], "rows": [["1. Informação", "Ler perigo de modo repetível", "Deduzir dano de um efeito visual"], ["2. Retomada", "Espaço, tempo ou regroup", "Gastar toda a defesa no contato"], ["3. Suporte", "Janela de cura com saída", "Curar durante a perseguição"], ["4. Pressão", "Abertura curta após o compromisso", "Perseguir até sala desconhecida"], ["5. Flex", "Fallback que funciona com mudanças", "Bônus condicionais que ninguém chama"]]}, image={"path": _COMBAT_IMAGE, "alt": "Captura oficial de combate da Steam com uma caçadora do Mistfall Hunter diante de uma criatura da floresta", "caption": "Mídia oficial da Steam para contexto de distância e timing; não mostra talento de Seer verificado.", "source_label": "Abrir a página oficial da Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("melee-healer-paths", "Build de Seer corpo a corpo ou de suporte?", ["Um build corpo a corpo de Seer deve criar um contato curto e voltar para uma posição legível. Distância curta não autoriza prolongar a troca. Se a saída some ao entrar, reveja espaço ou gatilho antes de empilhar dano.", "O suporte segue o mesmo limite. Cura é boa quando mantém o aliado sem apagar a rota de fuga. Combine onde curar, quem chama a retomada e qual recurso fica para a volta. Se o grupo se separar, reduza o objetivo antes de tentar resgatar."], table={"headers": ["Caminho", "Primeiro teste", "Mude quando"], "rows": [["Corpo a corpo", "Uma janela curta após o compromisso", "A retirada não está visível"], ["Suporte", "Cura em regroup protegido", "A cura prende você no aberto"], ["Informação", "Revelar um ângulo antes do avanço", "A habilidade não muda decisões"], ["Flex", "Uma função e um fallback", "O time não sabe seu trabalho"]]}, links=[{"target": "sword-shield-guide", "label": "Combinar com o guia de espada e escudo"}, {"target": "gameplay-guide", "label": "Rever o ciclo de extração"}]),
            _section("solo-route", "Como jogar o build de Seer no solo", ["No solo não há aliado para confirmar um ângulo ou cobrir uma reanimação. Use informação primeiro, entre em uma sala incerta por vez e mantenha a rota de volta visível. Se a primeira luta consumir a recuperação para sair, pare antes da próxima recompensa.", "Nos primeiros testes, escolha um objetivo, uma condição de saída e o ponto em que a função da Seer deixou de ajudar. Essa nota vale mais que uma captura sem patch, modo ou método."], steps=["Escolha objetivo e rota de volta antes da sala arriscada.", "Use informação ou suporte apenas quando a próxima decisão mudar.", "Confira vida, recuperação e rota após o contato.", "Extraia quando a recompensa não pagar o risco."], image={"path": _EXTRACTION_IMAGE, "alt": "Captura oficial da Steam de uma caçadora do Mistfall Hunter perto de um baú brilhante", "caption": "Mídia oficial da Steam para a decisão entre recompensa e rota.", "source_label": "Abrir a página oficial da Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "beginner-guide", "label": "Rever os fundamentos para iniciantes"}]),
            _section("trio-communication", "Como a Seer entra em um trio", ["No trio, todos precisam saber se a Seer guarda informação ou recuperação. Defina âncora, pressão e flex: quem protege o reset, quem aproveita a janela e quem olha a rota? Quando duas pessoas esperam a mesma função, o build parece fraco mesmo com as ferramentas funcionando.", "Quando alguém se separa, pare o plano original. Uma Seer de suporte não atravessa uma sala aberta sozinha para resgatar quem perdeu a rota, e uma Seer corpo a corpo não persegue além do espaço da âncora. Reagrupe, reduza o objetivo e repita as funções."], table={"headers": ["Momento", "Chamada da Seer", "Resposta do time"], "rows": [["Sala incerta", "Guardar informação", "Flex verifica um ângulo"], ["Janela clara", "Chamar pressão curta", "Parar quando fechar"], ["Jogador separado", "Proteger regroup", "Não forçar resgate"], ["Saída incerta", "Guardar suporte para voltar", "Reduzir ou extrair"]]}, image={"path": _FEATURE_IMAGE, "alt": "Captura oficial de exploração da Steam com uma caçadora do Mistfall Hunter em uma sala escura", "caption": "Mídia oficial da Steam lembrando que o trio precisa de um ponto de regroup legível.", "source_label": "Abrir a página oficial da Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "trio-builds-guide", "label": "Usar a checklist de funções do trio"}]),
            _section("test-and-mistakes", "Plano de teste em cinco runs", ["Não avalie a Seer por uma extração de sorte. Repita a mesma rota de baixo risco cinco vezes, mantenha a função e mude apenas um talento ou padrão de arma. Anote gatilho, custo, ponto de perigo e se a chamada foi entendida. É um pequeno experimento, não uma tier list universal.", "Os erros mais comuns são montar em torno de um número não verificado, guardar a ferramenta até nunca usá-la e pedir que a Seer explore, cure, cause dano e resgate ao mesmo tempo. Corrija a primeira falha e atualize as premissas após uma nota oficial ou teste repetível."], bullets=["Anote patch, modo, tamanho do grupo e habilidade testada.", "Compare a mesma rota e risco antes de mudar a conclusão.", "Trate captura comunitária sem fonte como pista.", "Pare quando a recompensa não pagar a volta."], links=[{"target": "maps-guide", "label": "Verificar o contexto do mapa"}]),
        ],
        "faq_title": "Perguntas frequentes sobre o build de Seer do Mistfall Hunter",
        "faq": [{"question": "Qual é o melhor build de Seer no Mistfall Hunter?", "answer": "As fontes consultadas não comprovam um melhor build permanente. Escolha informação, reset, suporte ou pressão curta, corrija a falha observada e teste a mesma rota."}, {"question": "Quais habilidades e talentos da Seer priorizar?", "answer": "Priorize informação repetível, reset seguro e suporte com saída. Confirme nomes e valores no cliente atual."}, {"question": "Build de Seer corpo a corpo é viável?", "answer": "Sim, se o contato for curto e a retirada continuar legível. Não persiga em sala desconhecida."}, {"question": "Seer pode ser curadora ou suporte?", "answer": "Sim, quando o time combina onde curar e quem chama o regroup. O suporte deve preservar a fuga."}, {"question": "Qual build de Seer serve para solo?", "answer": "Uma ação de informação, uma resposta de recuperação e pressão moderada. Mantenha a saída visível e extraia quando o risco superar a recompensa."}, {"question": "O trio deve copiar um código de build de Seer?", "answer": "Apenas com fonte, patch, modo e premissas. Defina funções primeiro e confira valores atuais."}],
        "summary_heading": "Resumo do build de Seer",
        "summary": "Monte a Seer em torno de uma função repetível, um fallback e uma rota de volta. Comece com informação e reset, adicione suporte ou pressão corpo a corpo quando a janela puder ser chamada e teste uma mudança por vez.",
        "related_title": "Continue preparando runs do Mistfall Hunter",
        "related_links": [{"target": "classes", "label": "Comparar classes do Mistfall Hunter"}, {"target": "tier-list-guide", "label": "Ler a tier list do Mistfall Hunter"}, {"target": "trio-builds-guide", "label": "Planejar funções de trio"}, {"target": "sword-shield-guide", "label": "Rever um build de espada e escudo"}, {"target": "gameplay-guide", "label": "Rever gameplay e extração"}],
        "source_title": "Fontes e escopo",
        "source_note": "A página usa mídia oficial da Steam e o site oficial do Mistfall Hunter para o contexto geral. Similarweb apoia o tema do build de Seer; valores exatos de classe, item, talento, dano e recarga ainda precisam ser verificados.",
    },
    "ko": {
        "primary_keyword": "Mistfall Hunter 시어 빌드",
        "related_keywords": ["Mistfall Hunter 시어 최고의 빌드", "시어 능력과 특성 빌드", "Mistfall Hunter 시어 근접 빌드", "Mistfall Hunter 시어 지원 빌드"],
        "title": "Mistfall Hunter 시어 빌드: 능력, 특성, 안전한 솔로 루트",
        "meta_title": "Mistfall Hunter 시어 빌드: 능력과 특성",
        "meta_description": "Mistfall Hunter 시어 빌드를 능력 타이밍, 특성 우선순위, 근접·지원 분기, 솔로와 트리오 운영으로 정리합니다.",
        "meta_keywords": "Mistfall Hunter 시어 빌드, 시어 최고의 빌드, 시어 능력, 시어 근접 빌드, 시어 지원 빌드",
        "eyebrow": "Mistfall Hunter 클래스 빌드 가이드",
        "lede": "좋은 시어 빌드는 반복할 수 있는 한 가지 역할에서 시작합니다. 정보를 만들거나, 재정비를 지키거나, 짧은 압박 창을 만드는 방식입니다. 확인되지 않은 수치를 단정하지 않고 솔로와 트리오에서 시험할 수 있는 기준을 제시합니다.",
        "checked_label": "2026년 10월 30일 시어 역할 프레임 검토; 정확한 수치는 버전에 따라 달라질 수 있음",
        "entry_label": "Mistfall Hunter 시어 빌드 가이드 읽기",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "어두운 방을 혼자 탐험하는 Mistfall Hunter 공식 Steam 스크린샷", "caption": "정보와 재정비 판단을 보여 주는 공식 Steam 소재이며 시어 수치 검증 화면은 아닙니다.", "source_label": "공식 Steam 페이지 열기", "source_url": _STEAM_URL, "width": 1200, "height": 675},
        "facts_headers": ["빌드 질문", "안전한 시작", "바꿀 조건"],
        "facts_rows": [["역할", "정보와 재정비", "다른 팀원이 정찰을 맡음"], ["능력", "반복 가능한 발동 하나", "설명이나 쿨다운이 바뀜"], ["특성", "실제 실패를 수정", "경로에서 조건을 만들 수 없음"], ["근접", "짧게 접촉 후 거리 회복", "퇴로가 보이지 않음"], ["지원", "보호된 재집결에서 회복", "회복 중 노출됨"]],
        "intro": "Mistfall Hunter 시어 빌드는 특성 순서를 복사하기 전에 해결할 문제를 정하는 것부터 시작합니다. 정보, 재정비, 지원, 짧은 공격 중 하나를 주역으로 선택하고 현재 툴팁에서 확인하세요. 공개 자료는 숨겨진 피해량이나 쿨다운을 보장하지 않으므로 아래 내용은 현재 클라이언트에서 검증할 출발점입니다.",
        "sections": [
            _section("seer-job", "시어 빌드가 먼저 해결할 문제", ["시어 검색은 하나의 정답을 요구하는 경우가 많지만, 탈출형 런에서는 다음 결정을 보이게 하고 그 비용을 감당하며 위험해지면 돌아갈 수 있어야 합니다. 불확실한 방을 정찰하거나, 부활을 지키거나, 적이 움직인 뒤 짧게 압박하는 역할입니다. 시어가 항상 힐러일 필요는 없습니다.", "출발 전에 역할을 한 문장으로 정하세요. 다음 안전한 각도를 알리기, 재집결까지 아군을 유지하기, 짧은 창만 공격하고 멈추기처럼 적습니다. 세 가지를 동시에 맡으면 무엇이 효과가 있었는지 알 수 없습니다."], bullets=["첫 접촉 뒤에도 이동·회복·정보 수단 하나를 남깁니다.", "메타라는 화면보다 실제 실패를 고치는 특성을 선택합니다.", "한 런에서 한 변수만 바꿉니다."], links=[{"target": "classes", "label": "다른 클래스 역할과 비교하기"}, {"target": "tier-list-guide", "label": "티어표를 역할 비교로 읽기"}]),
            _section("ability-talent-priority", "시어 능력과 특성 우선순위", ["최고의 능력은 발동 조건, 비용, 재정비 방법을 전투 전에 설명할 수 있는 능력입니다. 현재 툴팁을 읽고 낮은 위험의 경로에서 시험하세요. 드물게 만드는 조건에 의존하면 숫자가 커도 실제 런에서 도움이 되지 않습니다.", "지난 런을 끝낸 실패부터 고칩니다. 정보가 부족했다면 다음 위험을 보이게 하고, 탈출하지 못했다면 공간이나 회복을 먼저 선택합니다. 안전하지만 느렸을 때만 압박을 추가하세요. 그래서 최고의 시어 빌드는 고정된 목록이 아니라 문제에 따라 달라집니다."], table={"headers": ["우선순위", "찾을 것", "피할 것"], "rows": [["1. 정보", "위험을 반복해서 읽는 방법", "시각 효과만으로 피해량 단정"], ["2. 재정비", "공간·시간·재집결", "첫 접촉에 방어를 전부 사용"], ["3. 지원", "퇴로가 있는 회복 창", "추격 중 회복"], ["4. 압박", "적이 움직인 뒤 짧은 창", "미지의 방까지 추격"], ["5. 유연성", "계획이 바뀌어도 쓸 백업", "아무도 호출하지 않는 조건부 보너스"]]}, image={"path": _COMBAT_IMAGE, "alt": "큰 숲의 적과 마주한 Mistfall Hunter 공식 Steam 전투 스크린샷", "caption": "거리와 타이밍을 설명하는 공식 Steam 소재이며 시어 특성 검증은 아닙니다.", "source_label": "공식 Steam 페이지 열기", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("melee-healer-paths", "근접 시어와 지원 시어 분기", ["근접 시어는 짧은 접촉을 만든 뒤 읽을 수 있는 위치로 돌아오는 패턴에서 시작합니다. 근거리라고 해서 교전을 계속해도 된다는 뜻은 아닙니다. 들어갈 때 퇴로가 사라지면 피해량보다 공간과 발동 조건을 먼저 바꾸세요.", "지원형도 같은 기준을 가집니다. 회복은 아군을 살리면서 탈출 계획을 남길 때 가치가 있습니다. 어디서 회복할지, 누가 재집결을 부를지, 돌아갈 자원은 무엇인지 합의하세요. 팀이 갈라졌다면 구조보다 목표를 낮춥니다."], table={"headers": ["경로", "첫 시험", "바꿀 조건"], "rows": [["근접", "적이 움직인 뒤 짧은 창 한 번", "퇴로를 먼저 볼 수 없음"], ["지원", "보호된 재집결에서 회복", "노출된 곳에 묶임"], ["정보", "전진 전에 각도 하나 확인", "결정이 바뀌지 않음"], ["유연", "주역 하나와 비상 백업", "팀이 역할을 모름"]]}, links=[{"target": "sword-shield-guide", "label": "검과 방패 근접 가이드 보기"}, {"target": "gameplay-guide", "label": "탈출 판단 루프 확인"}]),
            _section("solo-route", "솔로에서 시어 빌드 운영하기", ["솔로에는 각도를 확인하거나 부활을 지켜 줄 팀원이 없습니다. 정보를 먼저 사용하고, 불확실한 방에 하나씩 들어가며, 뒤의 경로를 보이게 유지하세요. 첫 전투에서 탈출용 회복을 썼다면 다음 보상으로 서두르지 말고 멈춥니다.", "첫 테스트는 짧게 합니다. 목표, 중단 조건, 시어 역할이 더 이상 도움이 되지 않은 지점을 기록하세요. 패치와 모드가 없는 화면을 최고의 근거로 복사하지 않는 것이 중요합니다."], steps=["위험한 방 전에 목표와 귀환 경로를 정합니다.", "다음 결정이 바뀔 때만 정보나 지원을 씁니다.", "접촉 뒤 체력·회복·경로를 확인합니다.", "보상이 위험을 감당하지 못하면 탈출합니다."], image={"path": _EXTRACTION_IMAGE, "alt": "빛나는 상자에 다가가는 Mistfall Hunter 공식 Steam 탈출 스크린샷", "caption": "보상과 귀환 경로를 비교하는 판단을 보여 주는 공식 Steam 소재입니다.", "source_label": "공식 Steam 페이지 열기", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "beginner-guide", "label": "초보자 탈출 기초 보기"}]),
            _section("trio-communication", "트리오에서 시어의 자리", ["트리오에서는 시어가 정보와 회복 중 무엇을 맡는지 모두가 알아야 합니다. 앵커, 압박, 플렉스를 정하고 누가 재정비를 지키며, 누가 창을 사용하고, 누가 경로를 보는지 호출하세요. 두 사람이 같은 역할을 기대하면 도구가 작동해도 빌드가 약하게 느껴집니다.", "팀원이 떨어지면 원래 계획을 멈춥니다. 지원 시어가 경로를 잃은 팀원을 위해 열린 방을 혼자 건너지 말고, 근접 시어가 앵커의 공간 밖으로 추격하지도 마세요. 재집결, 목표 축소, 역할 재확인을 먼저 합니다."], table={"headers": ["상황", "시어 호출", "팀 대응"], "rows": [["불확실한 방", "정보를 아껴 둠", "플렉스가 각도 하나 확인"], ["명확한 창", "짧은 압박 선언", "창이 닫히면 멈춤"], ["팀원 분리", "재집결 경로 보호", "구조를 강행하지 않음"], ["출구 불명", "귀환용 지원 보존", "목표를 낮추거나 탈출"]]}, image={"path": _FEATURE_IMAGE, "alt": "어두운 방을 이동하는 Mistfall Hunter 공식 Steam 탐험 스크린샷", "caption": "트리오에도 읽을 수 있는 재집결 지점이 필요하다는 점을 보여 주는 공식 Steam 소재입니다.", "source_label": "공식 Steam 페이지 열기", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "trio-builds-guide", "label": "트리오 역할과 듀오 점검표 사용"}]),
            _section("test-and-mistakes", "5회 테스트 계획과 흔한 실수", ["운 좋은 탈출 한 번으로 시어를 평가하지 마세요. 같은 낮은 위험 경로를 다섯 번 반복하고 역할을 유지하며 특성이나 무기 패턴 하나만 바꿉니다. 발동, 비용, 위험 지점, 호출이 전달됐는지를 적으세요. 이는 작은 실험이지 영구 티어표가 아닙니다.", "확인되지 않은 숫자에 맞추기, 도구를 아끼다 한 번도 쓰지 않기, 정찰·회복·공격·구조를 동시에 요구하기가 대표적인 실수입니다. 첫 실패를 고치고 공식 패치나 반복 시험에서 전제가 바뀌면 업데이트합니다."], bullets=["패치, 모드, 인원, 시험한 능력을 기록합니다.", "결론을 바꾸기 전에 같은 경로와 위험을 비교합니다.", "출처 없는 커뮤니티 스크린샷은 단서로만 씁니다.", "보상이 귀환 비용을 못 내면 시험을 멈춥니다."], links=[{"target": "maps-guide", "label": "지도와 경로 맥락 확인"}]),
        ],
        "faq_title": "Mistfall Hunter 시어 빌드 자주 묻는 질문",
        "faq": [{"question": "Mistfall Hunter에서 최고의 시어 빌드는?", "answer": "확인한 자료에는 영구적인 최고의 빌드 근거가 없습니다. 정보, 재정비, 지원, 짧은 압박 중 하나를 고르고 같은 경로에서 시험하세요."}, {"question": "시어 능력과 특성은 무엇을 우선하나요?", "answer": "반복 가능한 정보, 안전한 재정비, 퇴로가 있는 지원을 우선합니다. 이름과 수치는 현재 툴팁에서 확인하세요."}, {"question": "근접 시어가 가능한가요?", "answer": "접촉을 짧게 하고 퇴로를 읽을 수 있다면 가능합니다. 미지의 방까지 추격하지 마세요."}, {"question": "시어를 힐러나 지원으로 쓸 수 있나요?", "answer": "어디서 회복하고 누가 재집결을 부를지 합의하면 가능합니다. 지원도 탈출 계획을 남겨야 합니다."}, {"question": "솔로 시어 빌드는 무엇인가요?", "answer": "정보 하나, 회복 하나, 절제된 압박을 기본으로 합니다. 출구를 보이고 위험이 보상보다 커지면 탈출합니다."}, {"question": "트리오가 시어 빌드 코드를 복사해야 하나요?", "answer": "출처, 패치, 모드, 전제가 분명할 때만 가능합니다. 먼저 역할을 정하고 현재 클라이언트에서 값을 확인하세요."}],
        "summary_heading": "시어 빌드 요약",
        "summary": "시어를 반복 가능한 역할 하나, 백업 하나, 귀환 경로 중심으로 구성합니다. 정보와 재정비부터 시작하고, 호출 가능한 지원이나 근접 압박을 나중에 추가하며 한 번에 한 가지를 시험하세요.",
        "related_title": "Mistfall Hunter 런 준비 계속하기",
        "related_links": [{"target": "classes", "label": "Mistfall Hunter 클래스 비교"}, {"target": "tier-list-guide", "label": "Mistfall Hunter 티어표 읽기"}, {"target": "trio-builds-guide", "label": "트리오 역할 계획"}, {"target": "sword-shield-guide", "label": "검과 방패 빌드 확인"}, {"target": "gameplay-guide", "label": "게임플레이와 탈출 판단 확인"}],
        "source_title": "출처와 범위",
        "source_note": "게임의 일반 맥락에는 공식 Steam 미디어와 Mistfall Hunter 공식 사이트를 사용했습니다. Similarweb은 시어 빌드 주제를 뒷받침하지만 클래스, 장비, 특성, 피해량, 쿨다운의 정확한 값은 확인이 필요합니다.",
    },
    "it": {
        "primary_keyword": "build Seer Mistfall Hunter",
        "related_keywords": ["miglior build Seer Mistfall Hunter", "abilità e talenti di Seer", "build Seer da mischia", "build di supporto Seer Mistfall Hunter"],
        "title": "Build Seer di Mistfall Hunter: abilità, talenti e rotte sicure",
        "meta_title": "Build Seer Mistfall Hunter: abilità e talenti",
        "meta_description": "Costruisci una build Seer per Mistfall Hunter con priorità di abilità e talenti, varianti da mischia o supporto e consigli per solo e trio.",
        "meta_keywords": "build Seer Mistfall Hunter, miglior build Seer, abilità Seer, build Seer da mischia, build supporto Seer",
        "eyebrow": "Guida alle build di classe Mistfall Hunter",
        "lede": "Una build Seer utile parte da un compito ripetibile: ottenere informazioni, proteggere un reset o creare una breve finestra di pressione. Questa guida trasforma il gruppo di ricerche su Seer in un piano verificabile per solo e trio senza inventare valori di patch.",
        "checked_label": "Schema di ruolo Seer verificato il 30 ottobre 2026; i valori esatti dipendono dalla versione",
        "entry_label": "Leggi la guida alla build Seer di Mistfall Hunter",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "Screenshot ufficiale Steam di un cacciatore di Mistfall Hunter che esplora una stanza buia da solo", "caption": "Media ufficiale Steam per spiegare informazioni e reset; non è un test dei valori di Seer.", "source_label": "Apri la pagina Steam ufficiale", "source_url": _STEAM_URL, "width": 1200, "height": 675},
        "facts_headers": ["Domanda", "Avvio prudente", "Cambia quando"],
        "facts_rows": [["Ruolo", "Informazioni e reset sicuro", "Un compagno esplora già"], ["Abilità", "Un innesco ripetibile", "Testo o ricarica cambia"], ["Talento", "Correggere l'errore osservato", "La condizione non appare"], ["Mischia", "Contatto breve e ritorno allo spazio", "L'uscita non è leggibile"], ["Supporto", "Curare durante un regroup protetto", "La cura ti espone"]],
        "intro": "Per una build Seer Mistfall Hunter, scegli prima il problema e poi l'ordine dei talenti. L'avvio migliore non è una lista meta permanente, ma una configurazione che permette di leggere una stanza, creare una breve apertura e conservare una risposta di recupero. Le fonti pubbliche non confermano danno, ricariche o gradi nascosti: usa il testo come brief da provare nel client attuale.",
        "sections": [
            _section("seer-job", "Il primo problema da risolvere con Seer", ["Le ricerche su Seer chiedono spesso una risposta unica, ma un'estrazione richiede una definizione concreta. La build deve mostrare la decisione successiva, pagarne il costo e lasciare una via d'uscita quando la rotta non vale più il rischio. Può esplorare una stanza, coprire una rianimazione o applicare pressione dopo l'impegno nemico. Seer non deve essere sempre una guaritrice.", "Scrivi il compito in una frase prima della coda: rivelare l'angolo sicuro, mantenere un alleato fino al reset o aprire una finestra breve e fermarsi. Tre compiti insieme rendono la build vaga. Scegline uno principale e uno di emergenza."], bullets=["Conserva movimento, recupero o informazione dopo il primo contatto.", "Scegli il talento per l'errore reale, non per una schermata che lo chiama meta.", "Cambia una variabile per partita."], links=[{"target": "classes", "label": "Confrontare Seer con gli altri ruoli"}, {"target": "tier-list-guide", "label": "Usare la tier list come confronto di ruoli"}]),
            _section("ability-talent-priority", "Priorità di abilità e talenti Seer", ["La migliore abilità è quella di cui conosci innesco, costo e recupero prima del combattimento. Leggi il testo attuale e provala su una rotta economica. Una condizione rara può rendere inutile un numero alto. Un effetto minore attivato di proposito è spesso più utile di un bonus da clip.", "Parti dall'errore che ha chiuso l'ultima partita. Se mancava informazione, scegli un'opzione per vedere l'angolo successivo. Se mancava la via d'uscita, scegli spazio o recupero. Se la squadra era sicura ma lenta, aggiungi pressione per ultima. La miglior build Seer dipende quindi dal problema che stai correggendo."], table={"headers": ["Priorità", "Cerca", "Evita"], "rows": [["1. Informazione", "Leggere il pericolo in modo ripetibile", "Dedurre il danno da un effetto visivo"], ["2. Reset", "Spazio, tempo o regroup", "Spendere tutta la difesa al contatto"], ["3. Supporto", "Finestra di cura con uscita", "Curare durante l'inseguimento"], ["4. Pressione", "Apertura breve dopo l'impegno", "Inseguire in una stanza sconosciuta"], ["5. Flex", "Fallback utile quando il piano cambia", "Bonus condizionali che nessuno chiama"]]}, image={"path": _COMBAT_IMAGE, "alt": "Screenshot ufficiale Steam di un cacciatore di Mistfall Hunter davanti a una creatura della foresta", "caption": "Media ufficiale Steam per distanza e tempismo; non mostra un talento Seer verificato.", "source_label": "Apri la pagina Steam ufficiale", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("melee-healer-paths", "Build Seer da mischia o di supporto?", ["Una build Seer da mischia deve creare un contatto breve e tornare in una posizione leggibile. La distanza ravvicinata non autorizza a prolungare ogni scambio. Se l'uscita sparisce all'ingresso, rivedi spazio o innesco prima di aggiungere danno.", "Il supporto segue lo stesso limite. La cura è utile quando mantiene l'alleato senza cancellare la via di fuga. Decidi dove curare, chi chiama il reset e quale risorsa tenere per il ritorno. Se il gruppo è diviso, riduci l'obiettivo prima del salvataggio."], table={"headers": ["Percorso", "Primo test", "Cambia quando"], "rows": [["Mischia", "Una finestra breve dopo l'impegno", "La ritirata non è visibile"], ["Supporto", "Cura durante un regroup protetto", "La cura ti blocca allo scoperto"], ["Informazione", "Rivelare un angolo prima di avanzare", "La capacità non cambia decisioni"], ["Flex", "Un compito e un fallback", "La squadra non conosce il ruolo"]]}, links=[{"target": "sword-shield-guide", "label": "Vedere il piano spada e scudo"}, {"target": "gameplay-guide", "label": "Rivedere il ciclo di estrazione"}]),
            _section("solo-route", "Usare la build Seer in solo", ["In solo non c'è un alleato che confermi l'angolo o copra una rianimazione. Usa l'informazione per prima, entra in una stanza incerta alla volta e tieni visibile la rotta dietro di te. Se il primo combattimento consuma il recupero per l'uscita, fermati prima della ricompensa successiva.", "Nei primi test scegli un obiettivo, una condizione di uscita e il punto in cui il ruolo di Seer smette di aiutare. Questa nota vale più di una schermata senza patch, modalità o metodo."], steps=["Scegli obiettivo e ritorno prima della stanza rischiosa.", "Usa informazione o supporto solo quando cambia la decisione successiva.", "Controlla vita, recupero e rotta dopo il contatto.", "Estrai quando la ricompensa non copre più il rischio."], image={"path": _EXTRACTION_IMAGE, "alt": "Screenshot ufficiale Steam di un cacciatore di Mistfall Hunter vicino a una cassa luminosa", "caption": "Media ufficiale Steam per la decisione tra ricompensa e ritorno.", "source_label": "Apri la pagina Steam ufficiale", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "beginner-guide", "label": "Rivedere le basi per principianti"}]),
            _section("trio-communication", "Il ruolo di Seer in un trio", ["Nel trio tutti devono sapere se Seer conserva informazione o recupero. Definisci ancora, pressione e flex: chi protegge il reset, chi sfrutta la finestra e chi guarda la rotta? Due aspettative diverse fanno sembrare debole la build anche quando gli strumenti funzionano.", "Quando un compagno si separa, ferma il piano originale. Una Seer di supporto non attraversa da sola una stanza aperta per un alleato senza rotta e una Seer da mischia non insegue oltre lo spazio dell'ancora. Raggruppa, riduci l'obiettivo e ripeti i ruoli."], table={"headers": ["Momento", "Chiamata Seer", "Risposta del gruppo"], "rows": [["Stanza incerta", "Conservare informazione", "Il flex controlla un angolo"], ["Finestra chiara", "Chiamare pressione breve", "Fermarsi alla chiusura"], ["Giocatore separato", "Proteggere il regroup", "Non forzare il salvataggio"], ["Uscita incerta", "Tenere supporto per il ritorno", "Ridurre o estrarre"]]}, image={"path": _FEATURE_IMAGE, "alt": "Screenshot ufficiale Steam di esplorazione di Mistfall Hunter in una stanza buia", "caption": "Media ufficiale Steam che ricorda che anche un trio ha bisogno di un punto di regroup leggibile.", "source_label": "Apri la pagina Steam ufficiale", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "trio-builds-guide", "label": "Usare la checklist dei ruoli del trio"}]),
            _section("test-and-mistakes", "Piano di test in cinque run", ["Non giudicare Seer da un'estrazione fortunata. Ripeti la stessa rotta a basso rischio cinque volte, mantieni il ruolo e cambia un solo talento o schema d'arma. Segna innesco, costo, punto di pericolo e comprensione della chiamata. È un piccolo esperimento, non una tier list universale.", "Gli errori tipici sono costruire su un numero non verificato, conservare lo strumento fino a non usarlo mai e chiedere a Seer di esplorare, curare, fare danno e salvare insieme. Correggi il primo errore visibile e aggiorna le premesse dopo note ufficiali o test ripetibili."], bullets=["Annota patch, modalità, numero di giocatori e abilità testata.", "Confronta la stessa rotta e lo stesso rischio prima di cambiare conclusione.", "Una schermata della community senza fonte è solo un indizio.", "Ferma il test quando la ricompensa non paga il ritorno."], links=[{"target": "maps-guide", "label": "Controllare il contesto della mappa"}]),
        ],
        "faq_title": "Domande frequenti sulla build Seer di Mistfall Hunter",
        "faq": [{"question": "Qual è la miglior build Seer in Mistfall Hunter?", "answer": "Le fonti controllate non dimostrano una build migliore permanente. Scegli informazione, reset, supporto o pressione breve, correggi l'errore osservato e prova la stessa rotta."}, {"question": "Quali abilità e talenti Seer scegliere?", "answer": "Dai priorità a informazione ripetibile, reset sicuro e supporto con uscita. Verifica nomi e valori nel client attuale."}, {"question": "Una build Seer da mischia è valida?", "answer": "Sì, se il contatto è breve e la ritirata resta leggibile. Non inseguire in una stanza sconosciuta."}, {"question": "Seer può essere supporto o guaritrice?", "answer": "Sì, se il gruppo decide dove curare e chi chiama il regroup. Il supporto deve lasciare la fuga."}, {"question": "Quale build Seer va bene in solo?", "answer": "Un'azione d'informazione, una risposta di recupero e pressione moderata. Tieni visibile l'uscita ed estrai quando il rischio supera la ricompensa."}, {"question": "Il trio deve copiare un codice di build Seer?", "answer": "Solo con fonte, patch, modalità e premesse chiare. Definisci prima i ruoli e verifica i valori correnti."}],
        "summary_heading": "Riepilogo della build Seer",
        "summary": "Costruisci Seer attorno a un compito ripetibile, un fallback e una rotta di ritorno. Parti da informazione e reset, aggiungi supporto o pressione da mischia quando la finestra è chiamabile e prova una modifica alla volta.",
        "related_title": "Continua a preparare i run di Mistfall Hunter",
        "related_links": [{"target": "classes", "label": "Confrontare le classi di Mistfall Hunter"}, {"target": "tier-list-guide", "label": "Leggere la tier list di Mistfall Hunter"}, {"target": "trio-builds-guide", "label": "Pianificare i ruoli del trio"}, {"target": "sword-shield-guide", "label": "Rivedere una build spada e scudo"}, {"target": "gameplay-guide", "label": "Rivedere gameplay ed estrazione"}],
        "source_title": "Fonti e ambito",
        "source_note": "La pagina usa media ufficiali Steam e il sito ufficiale Mistfall Hunter per il contesto generale. Similarweb sostiene il tema Seer; i valori precisi di classe, oggetti, talenti, danni e ricariche restano da verificare.",
    },
}


for _locale, _override in _LOCALE_OVERRIDES.items():
    SEER_BUILD_GUIDES[_locale] = _guide(_locale, _override)
