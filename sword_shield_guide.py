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
    构造文章模板需要的单个内容区块。

    :param section_id: 区块的稳定 HTML 锚点
    :param heading: 区块标题
    :param paragraphs: 正文段落列表
    :param bullets: 可选的要点列表
    :param links: 可选的站内链接列表
    :param table: 可选的表格数据
    :param steps: 可选的步骤列表
    :param image: 可选的配图数据
    :return: dict，包含模板读取的全部区块字段
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


SWORD_SHIELD_GUIDES: Dict[str, Dict[str, Any]] = {
    "en": {
        "slug": "mistfall-hunter-sword-and-shield-build",
        "primary_keyword": "Mistfall Hunter sword and shield build",
        "related_keywords": [
            "Mistfall Hunter mercenary sword and shield build",
            "sword and shield merc Mistfall build",
            "merc sword and shield Mistfall Hunter build",
            "Mistfall Hunter solo sword and shield build",
        ],
        "title": "Mistfall Hunter Sword and Shield Build: 5 Priorities for Safer Solo and Trio Runs",
        "meta_title": "Mistfall Hunter Sword and Shield Build: 5 Priorities",
        "meta_description": "Plan a Mistfall Hunter sword and shield build with clear gear and skill priorities, solo and trio adjustments, and a repeatable test plan without invented stats.",
        "meta_keywords": "Mistfall Hunter sword and shield build, Mistfall Hunter mercenary sword and shield build, sword and shield merc Mistfall build, solo sword and shield build",
        "eyebrow": "Mistfall Hunter weapon build guide",
        "lede": "A sword-and-shield setup is a practical starting point when you want room to read a fight, make a short commitment, and keep a route back open. Build around repeatable decisions rather than an unverified damage ranking: choose one defensive answer, one reliable pressure window, and one way to reset. This guide separates general planning advice from patch-specific values that still need current in-game testing.",
        "checked_label": "Role-based build framework reviewed 24 October 2026; exact item values are not asserted",
        "entry_label": "Read the Mistfall Hunter sword and shield build guide",
        "checked_iso": "2026-10-24",
        "feature_image": {
            "path": _FEATURE_IMAGE,
            "alt": "Editorial fantasy concept art of a hunter carrying a sword and shield, with the short label Sword + Shield",
            "caption": "Original editorial concept art made for this guide; it is not official Mistfall Hunter art or an in-game screenshot.",
            "source_label": "About this independent guide",
            "source_url": "/about/",
            "width": 1024,
            "height": 1024,
        },
        "facts_headers": ["Build decision", "Safe starting point", "Change it when"],
        "facts_rows": [
            ["Role", "Hold space and leave a reset route", "A teammate already owns the anchor role"],
            ["Damage", "Use short, repeatable openings", "A verified patch or test changes the timing"],
            ["Gear", "Keep one survival answer and one pressure option", "The current item descriptions support a clearer trade"],
            ["Solo", "Take loot only while the exit remains readable", "The route or recovery option disappears"],
            ["Trio", "Call the anchor, pressure, and flex jobs", "A squad member is separated or the plan overlaps"],
        ],
        "intro": "For a Mistfall Hunter sword and shield build, start with a stable role instead of chasing a claimed best-in-slot list. Keep enough room to recover from one poor exchange, spend damage only during a clear opening, and decide how you will leave before you commit. The available public material confirms the game's broad extraction loop and equipment focus, but it does not verify one permanent combination of item names, stat values, or talent ranks. Treat the priorities below as a testable setup, then confirm every exact value in your current game version.",
        "sections": [
            _section(
                "build-goal",
                "What this sword and shield build is meant to solve",
                [
                    "The useful question is not whether a shield always beats another weapon. It is whether this setup lets you make a decision, survive its cost, and return to a safe route. A close-range weapon pair naturally invites longer trades, so use the shield side of the setup as a reason to control when you engage, not as proof that every hit can be blocked. The exact input, defense rule, and recovery cost can change; read the current tooltips and test them rather than assuming a genre convention applies.",
                    "Use this guide as a role-based build framework. It works best for a player who prefers controlled contact, wants to learn an encounter, or needs a clear job in a small team. It is not a claim that sword and shield is the highest-damage option, the only viable option, or an official meta build. If your current version uses different class labels or item terminology, keep the decision rules and substitute the names shown in your own loadout screen.",
                ],
                bullets=[
                    "Keep one recovery or disengage option available before committing.",
                    "Choose one offensive window you can recognize without a damage spreadsheet.",
                    "Change one item or skill at a time so the next run teaches you something.",
                ],
                image={
                    "path": _COMBAT_IMAGE,
                    "alt": "Official Steam Store combat screenshot showing a Mistfall Hunter character facing a large forest creature",
                    "caption": "Official Steam Store combat media for general spacing and encounter context; it does not show a tested sword-and-shield build or damage values.",
                    "source_label": "Open the official Steam listing",
                    "source_url": _STEAM_URL,
                    "width": 1200,
                    "height": 675,
                },
            ),
            _section(
                "five-build-priorities",
                "Five priorities for a safer Mistfall Hunter sword and shield build",
                [
                    "Start with these priorities in order. They describe what a build should let you do, not fixed stat names or hidden game formulas. Open your current equipment and skill descriptions, then choose the visible options that serve the same job. If two bonuses appear to help, prefer the one you can test repeatedly over the one that only sounds stronger in isolation.",
                    "A strong first pass is deliberately modest: one answer for survival, one repeatable damage action, and enough flexibility to leave a bad room. After a few runs, review the point where the plan stopped working. If you were safe but too slow, tune pressure. If you dealt damage but lost the exit, tune recovery or decision timing before adding more offense.",
                ],
                table={
                    "headers": ["Priority", "Look for", "Avoid"],
                    "rows": [
                        ["1. Readable defense", "An option whose condition and cost you understand", "Assuming a shield prevents every source of damage"],
                        ["2. Repeatable pressure", "A short attack window you can create on purpose", "A long chase that carries you past the safe route"],
                        ["3. Recovery", "A clear way to regain space or stop an exchange", "Spending every defensive action at the first contact"],
                        ["4. Useful gear", "Bonuses that solve the problem you actually observed", "Copying a stat priority without checking the current item text"],
                        ["5. Team value", "A job that complements the other players", "Three players choosing the same role by default"],
                    ],
                },
                links=[{"target": "builds", "label": "Compare this focused setup with the site's broader build patterns"}],
            ),
            _section(
                "gear-skills",
                "Choose gear, skills, and talents by the job they perform",
                [
                    "Read each item or talent description in the current version and ask what decision it improves. A defensive effect is useful only if it changes a real failure point: being caught during a long trade, losing room to reposition, or having no answer when an encounter changes. A damage effect is useful when you can trigger it in a predictable opening. If a bonus depends on a condition you rarely create, its headline number may not help your actual run.",
                    "Do not copy a `Mistfall Hunter mercenary sword and shield build` string as if it proves that one class label, talent order, or item set is current. Similarweb shows that this wording appears in the query cluster, while public data checked for this brief does not establish a verified class-specific loadout. Match the class name to the current game UI, inspect the prerequisite and resource cost, and test one change. When a source does not state a patch or test method, treat its exact item advice as a lead, not a fact.",
                ],
                bullets=[
                    "Write down the skill's trigger, cost, and recovery before building around it.",
                    "Keep one gear choice that helps you leave danger, not only enter it.",
                    "Use a damage bonus only when you can name the opening that activates it.",
                    "Check whether a talent changes a real decision or only adds an unverified number.",
                ],
            ),
            _section(
                "solo-adjustment",
                "How to adjust the solo sword and shield build",
                [
                    "Solo play removes a teammate who can cover a second angle or confirm a retreat call. Build for information and repeatability: approach one uncertain space at a time, keep a route back in view, and do not treat a safe-looking shield option as permission to stay in a fight indefinitely. If an encounter costs the recovery action you expected to use later, pause and reassess before taking another reward.",
                    "A practical solo loop is to set one objective, check the cost of reaching it, and decide what would make you leave before you move in. The loot can change the value of continuing, but it does not erase the return trip. If you are searching for a `Mistfall Hunter solo sword and shield build`, begin with the same role priorities and remove any choice that only pays off when another player is nearby. For a wider look at extraction decisions, use the site's gameplay and beginner guides.",
                ],
                steps=[
                    "Choose one objective and one route home before the first risky contact.",
                    "Spend only the defensive or offensive action needed for the current opening.",
                    "Recheck health, recovery options, and route visibility after a fight.",
                    "Extract when the remaining reward no longer pays for the route risk.",
                ],
                image={
                    "path": _EXTRACTION_IMAGE,
                    "alt": "Official Steam Store screenshot of a Mistfall Hunter character approaching a glowing chest in a dark chamber",
                    "caption": "Official Steam Store extraction media; it illustrates the reward-and-return decision, not a guaranteed loot route or the recommended weapon set.",
                    "source_label": "Open the official Steam listing",
                    "source_url": _STEAM_URL,
                    "width": 1200,
                    "height": 675,
                },
                links=[{"target": "gameplay-guide", "label": "Review the solo and extraction gameplay loop"}],
            ),
            _section(
                "trio-adjustment",
                "How the build changes in a trio",
                [
                    "In a trio, sword and shield can be a useful anchor job if the player is comfortable holding space and communicating a reset. That is a team recommendation, not a verified class bonus. Agree who will call the retreat, who will take a short pressure window, and who will flex toward scouting or recovery. A `sword and shield merc Mistfall build` should not mean that the player walks ahead alone; the setup works only when teammates know which opening they are waiting for.",
                    "If another player is already anchoring, shift this build toward controlled pressure or a flexible support job instead of duplicating the same responsibility. Keep enough distance to react when the fight moves, but stay close enough to hear a call. If one teammate is separated, the trio should regroup before restarting an engagement. That principle is more stable than claiming a single composition is strongest across every patch, map, and skill level.",
                ],
                table={
                    "headers": ["Situation", "Sword-and-shield job", "Team call"],
                    "rows": [
                        ["Unknown room", "Hold a recoverable position", "Scout one angle before the group pushes"],
                        ["Clear opening", "Commit to one short pressure window", "Call the target and stop after the agreed window"],
                        ["Player separated", "Protect the route to regroup", "Pause the push until the team is together"],
                        ["Exit unclear", "Do not trade away the retreat", "Reset or leave before adding another fight"],
                    ],
                },
                links=[{"target": "trio-builds-guide", "label": "Use the trio roles and fallback checklist"}],
            ),
            _section(
                "repeatable-test",
                "A short test plan for tuning the build",
                [
                    "A build is hard to improve when the class, skills, gear, route, and risk level all change at once. Use a short sequence that holds most choices steady. Before a run, write down the one question you want to answer. Examples: did the defensive choice create time to reposition, did the attack window feel repeatable, or did the planned exit remain usable after the first encounter? These are observations, not a substitute for a controlled damage test.",
                    "After each run, record the result in plain language. Note the decision that cost the most, the resource you wished you still had, and whether the run ended because of combat, route choice, or a team split. Change one relevant part for the next attempt. If you change several things, keep the result as a new build experiment rather than claiming that one item caused the outcome.",
                ],
                steps=[
                    "Lock the class, weapon pairing, route style, and risk level for the first comparison.",
                    "Pick one variable: a gear bonus, skill choice, or timing rule.",
                    "Record the objective, failed decision, recovery option, and extraction result.",
                    "Repeat the same question before calling the change an improvement.",
                    "Recheck patch notes or item text whenever the game changes the relevant system.",
                ],
                links=[{"target": "beginner-guide", "label": "Use the low-risk five-run learning plan"}],
            ),
            _section(
                "mistakes-and-limits",
                "Common mistakes and what this guide cannot prove",
                [
                    "The first mistake is confusing defense with safety. A defensive tool can still have a timing rule, cost, or gap; learn its actual behavior before committing to an extended trade. The second is stacking offensive choices because a build list names them as optimal. If you cannot identify the opening that makes the effect useful, test it before treating it as a priority. The third is following advice with no patch date or clear test conditions as though it were a current ranking.",
                    "The fourth mistake is changing too many parts between runs. A build may feel better because the route or teammate changed, not because one item was stronger. Keep notes and avoid turning a personal success into a universal rule. The current public sources support the game's extraction structure, equipment focus, solo play, and team play; they do not provide a verified sword-and-shield damage formula or a permanent item ranking. Use this framework as a starting point and replace assumptions with repeatable evidence when you have it.",
                ],
            ),
        ],
        "faq_title": "Mistfall Hunter sword and shield build FAQ",
        "faq": [
            {"question": "What is the best Mistfall Hunter sword and shield build?", "answer": "There is no verified universal best setup in the sources used for this guide. Start with a clear defensive answer, one repeatable pressure window, and a way to reset. Then test the current item text and patch rather than trusting an undated meta claim."},
            {"question": "Is a mercenary sword and shield build good for solo?", "answer": "It can be a reasonable role-based starting point if the current class and gear support the pairing, but the Similarweb keyword alone does not verify a current class loadout. For solo, favor choices that keep a route home and do not depend on a teammate to cover your recovery."},
            {"question": "Which stats should I prioritize for a sword and shield build?", "answer": "Use the stat names and effects shown in your current version. First cover the failure you actually observed, then add a damage option you can use in a predictable opening. This guide avoids invented stat names, breakpoints, and exact values."},
            {"question": "Does the sword and shield build work in a trio?", "answer": "It can fit an anchor or controlled-pressure role when the team has agreed who calls a reset and who covers other jobs. If another player already anchors, adjust the role instead of duplicating it. The trio composition should be tested in the current patch."},
            {"question": "Should I copy a Mistfall Hunter sword and shield build code?", "answer": "Use a code as a starting reference only when its source, patch, class, and item requirements are clear. Compare every choice with your own game version and change one variable at a time so you can tell what helped."},
        ],
        "summary_heading": "The short version",
        "summary": "Treat the Mistfall Hunter sword and shield build as a controlled, role-based experiment: protect a reset, use short pressure windows, keep the solo route readable, and assign clear trio jobs. Exact item names and numeric priorities remain patch-sensitive and were not verified here, so validate them in the current game before calling any setup best-in-slot.",
        "related_title": "Continue planning your next run",
        "related_links": [
            {"target": "builds", "label": "Compare broad Mistfall Hunter build patterns"},
            {"target": "classes", "label": "Review the class roles"},
            {"target": "gameplay-guide", "label": "Review the gameplay and extraction loop"},
            {"target": "trio-builds-guide", "label": "Plan a trio composition"},
            {"target": "beginner-guide", "label": "Start with a low-risk learning plan"},
        ],
        "source_title": "Official references and evidence limits",
        "source_note": "The official game website and Steam listing are included for the game's broad identity and equipment context. The existing official Steam screenshots on this page are contextual media only. No current official source was reachable from this workstation to verify a particular sword-and-shield stat line, skill rotation, patch-specific item ranking, or exact best build; recommendations above are explicitly role-based and should be checked in-game.",
        "official_links": [
            {"label": "Official Mistfall Hunter website", "url": _OFFICIAL_URL, "rel": "noopener"},
            {"label": "Official Steam listing and media", "url": _STEAM_URL, "rel": "noopener"},
        ],
    },
    "es": {
        "slug": "mistfall-hunter-sword-and-shield-build",
        "primary_keyword": "build de espada y escudo para Mistfall Hunter",
        "related_keywords": [
            "build de mercenario de Mistfall Hunter",
            "mejor build de espada y escudo para Mistfall Hunter",
            "build de espada y escudo de Mistfall Hunter para jugar en solitario",
            "build de espada y escudo para tríos en Mistfall Hunter",
        ],
        "title": "Build de espada y escudo de Mistfall Hunter: 5 prioridades para sobrevivir en solitario y en trío",
        "meta_title": "Build de espada y escudo de Mistfall Hunter: 5 claves",
        "meta_description": "Prepara un build de espada y escudo de Mistfall Hunter con prioridades de equipo, ajustes para solo y trío y un método de prueba sin estadísticas inventadas.",
        "meta_keywords": "build espada y escudo Mistfall Hunter, build mercenario Mistfall Hunter, build Mistfall Hunter solo",
        "eyebrow": "Guía de build de armas de Mistfall Hunter",
        "lede": "Una configuración de espada y escudo puede servir para controlar el espacio, hacer intercambios cortos y conservar una ruta de salida. La recomendación aquí es un punto de partida basado en roles, no una clasificación de daño verificada. Separamos las decisiones que puedes probar de los valores concretos que deben confirmarse en la versión actual del juego.",
        "checked_label": "Marco de build por funciones revisado el 24 de octubre de 2026; no afirma valores exactos de objetos",
        "entry_label": "Leer la guía de build de espada y escudo de Mistfall Hunter",
        "checked_iso": "2026-10-24",
        "feature_image": {
            "path": _FEATURE_IMAGE,
            "alt": "Ilustración editorial fantástica de un cazador con espada y escudo y el rótulo breve Sword + Shield",
            "caption": "Ilustración conceptual editorial creada para esta guía; no es arte oficial ni una captura del juego.",
            "source_label": "Sobre esta guía independiente",
            "source_url": "/about/",
            "width": 1024,
            "height": 1024,
        },
        "facts_headers": ["Decisión de build", "Punto de partida prudente", "Cámbialo cuando"],
        "facts_rows": [
            ["Rol", "Controlar espacio y conservar una retirada", "Otro compañero ya cumple la función de ancla"],
            ["Daño", "Aprovechar ventanas cortas y repetibles", "Una prueba actual cambia el momento de ataque"],
            ["Equipo", "Combinar una respuesta defensiva con presión", "El texto actual de los objetos muestra una opción mejor"],
            ["Solo", "Recoger botín si aún ves la ruta de vuelta", "Desaparece la ruta o una opción de recuperación"],
            ["Trío", "Asignar ancla, presión y apoyo flexible", "Alguien se separa o dos jugadores repiten el mismo rol"],
        ],
        "intro": "Para un build de espada y escudo para Mistfall Hunter, empieza por una función estable y no por una lista de equipo supuestamente perfecta. Conserva una respuesta para recuperarte de un intercambio malo, gasta daño durante una oportunidad clara y decide cómo saldrás antes de comprometerte. La información pública confirma el ciclo general de extracción y el papel del equipo, pero no verifica una combinación permanente de objetos, estadísticas o talentos. Usa estas prioridades como un plan de prueba y confirma cada valor en tu versión actual.",
        "sections": [
            _section(
                "build-goal",
                "Qué problema resuelve este build de espada y escudo",
                [
                    "La pregunta útil no es si el escudo siempre supera a otra arma. Pregúntate si esta configuración te permite decidir, asumir el coste de un combate y volver a una ruta segura. Las armas de corta distancia invitan a prolongar los intercambios; toma el escudo como una razón para controlar cuándo entras, no como garantía de que puedas bloquear cualquier ataque. La regla, el coste y la recuperación exactos pueden cambiar. Lee las descripciones actuales y prueba su funcionamiento.",
                    "Esta guía es un marco de build por funciones. Puede ayudar a quien prefiere el contacto controlado, quiere aprender un encuentro o necesita un papel claro en un grupo pequeño. No afirma que la espada y el escudo sean la opción con más daño, la única viable o el meta oficial. Si la versión actual usa otros nombres de clase u objeto, conserva el criterio y sustituye los nombres por los que aparecen en tu equipo.",
                ],
                bullets=[
                    "Conserva una opción de recuperación o retirada antes de entrar.",
                    "Elige una ventana de ataque que puedas reconocer sin una hoja de cálculo.",
                    "Cambia un objeto o una habilidad cada vez para aprender algo de la siguiente run.",
                ],
                image={
                    "path": _COMBAT_IMAGE,
                    "alt": "Captura oficial de Steam de un cazador de Mistfall Hunter frente a una criatura grande del bosque",
                    "caption": "Imagen oficial de combate para ilustrar distancia y contexto; no muestra un build probado ni valores de daño.",
                    "source_label": "Abrir la ficha oficial de Steam",
                    "source_url": _STEAM_URL,
                    "width": 1200,
                    "height": 675,
                },
            ),
            _section(
                "five-build-priorities",
                "5 prioridades para un build de espada y escudo más seguro",
                [
                    "Aplica estas prioridades en orden. Describen lo que debe permitirte hacer el build, no nombres fijos de estadísticas ni fórmulas ocultas. Abre el equipo y las habilidades de la versión actual y busca opciones que cumplan la misma función. Si dos bonificaciones parecen útiles, prefiere la que puedas probar de forma repetida en lugar de la que suene más potente fuera de contexto.",
                    "Una primera versión debe ser modesta: una respuesta de supervivencia, una acción ofensiva repetible y flexibilidad para abandonar una sala mala. Después de algunas partidas, revisa cuándo dejó de funcionar el plan. Si estabas a salvo pero tardabas demasiado, ajusta la presión. Si hiciste daño pero perdiste la salida, cambia la recuperación o el momento de decisión antes de añadir más ataque.",
                ],
                table={
                    "headers": ["Prioridad", "Busca", "Evita"],
                    "rows": [
                        ["1. Defensa comprensible", "Una opción cuya condición y coste conoces", "Creer que el escudo bloquea todas las fuentes de daño"],
                        ["2. Presión repetible", "Una ventana corta que puedas provocar", "Perseguir al enemigo más allá de una ruta segura"],
                        ["3. Recuperación", "Una forma clara de recuperar espacio o cortar el intercambio", "Gastar toda la defensa en el primer contacto"],
                        ["4. Equipo útil", "Bonificaciones que resuelven un problema observado", "Copiar una prioridad sin revisar el texto actual"],
                        ["5. Aporte al grupo", "Un trabajo que complemente al resto", "Que todos elijan el mismo rol por defecto"],
                    ],
                },
                links=[{"target": "builds", "label": "Comparar con los patrones de build generales del sitio"}],
            ),
            _section(
                "gear-skills",
                "Elige equipo, habilidades y talentos por la función que cumplen",
                [
                    "Lee la descripción actual de cada objeto o talento y pregúntate qué decisión mejora. Una opción defensiva solo sirve si cambia un fallo real: quedar atrapado en un intercambio largo, perder espacio para recolocarte o no tener respuesta cuando cambia el encuentro. Una bonificación de daño ayuda cuando puedes activarla durante una oportunidad previsible. Si depende de una condición que casi nunca creas, su cifra principal puede no servirte en tus partidas.",
                    "No copies la frase `build de mercenario de espada y escudo de Mistfall Hunter` como prueba de que el nombre de una clase, el orden de talentos o el conjunto de objetos sigan vigentes. Similarweb muestra esa variante en el grupo de consultas, pero la evidencia pública usada aquí no confirma una configuración actual de clase. Comprueba el nombre de tu interfaz, los requisitos y el coste de recursos, y prueba un cambio. Si una guía no indica parche ni método de prueba, úsala como pista, no como hecho.",
                ],
                bullets=[
                    "Anota el activador, el coste y la recuperación de la habilidad antes de basar el build en ella.",
                    "Conserva una elección de equipo que ayude a salir del peligro.",
                    "Usa una bonificación de daño solo si puedes identificar la oportunidad que la activa.",
                    "Comprueba si un talento cambia una decisión real o solo promete una cifra sin verificar.",
                ],
            ),
            _section(
                "solo-adjustment",
                "Cómo ajustar el build de espada y escudo para jugar en solitario",
                [
                    "En solitario no tienes un compañero que cubra otro ángulo o confirme una retirada. Prioriza información y repetibilidad: avanza de una zona incierta a la vez, conserva a la vista una ruta de regreso y no interpretes una opción defensiva como permiso para alargar indefinidamente el combate. Si gastas la recuperación que pensabas usar después, detente y evalúa antes de buscar otra recompensa.",
                    "Un ciclo solo práctico empieza por definir un objetivo, revisar el coste de llegar y decidir de antemano qué te hará salir. El botín puede cambiar el valor de continuar, pero no elimina el viaje de vuelta. Si buscas un `build de espada y escudo de Mistfall Hunter para jugar en solitario`, empieza con las mismas prioridades y elimina cualquier elección que solo funcione cuando otro jugador está cerca. Para el ciclo de extracción completo, consulta las guías de gameplay y principiantes del sitio.",
                ],
                steps=[
                    "Elige un objetivo y una ruta de vuelta antes del primer encuentro de riesgo.",
                    "Usa solo la acción defensiva u ofensiva que pide la oportunidad actual.",
                    "Revisa salud, recuperación y visibilidad de la ruta después de cada combate.",
                    "Extrae cuando la recompensa restante no compense el riesgo de regreso.",
                ],
                image={
                    "path": _EXTRACTION_IMAGE,
                    "alt": "Captura oficial de Steam de un personaje de Mistfall Hunter acercándose a un cofre luminoso",
                    "caption": "Imagen oficial de extracción para explicar la decisión de volver con botín; no garantiza una ruta ni muestra el equipo recomendado.",
                    "source_label": "Abrir la ficha oficial de Steam",
                    "source_url": _STEAM_URL,
                    "width": 1200,
                    "height": 675,
                },
                links=[{"target": "gameplay-guide", "label": "Revisar el ciclo de gameplay y extracción en solitario"}],
            ),
            _section(
                "trio-adjustment",
                "Cómo cambia el build cuando juegas en trío",
                [
                    "En un trío, la espada y el escudo pueden servir para anclar el espacio si quien juega está dispuesto a comunicar cuándo retroceder. Es una recomendación de equipo, no una bonificación de clase verificada. Acuerden quién llama la retirada, quién aprovecha una ventana corta de presión y quién explora o ayuda a recuperar. Un `sword and shield merc Mistfall build` no debería significar que una persona se adelante sola; solo funciona si el equipo entiende qué oportunidad está esperando.",
                    "Si otra persona ya cumple el papel de ancla, orienta este build hacia una presión controlada o un apoyo flexible en lugar de duplicar la misma tarea. Deja distancia para reaccionar, pero mantente lo bastante cerca para escuchar una llamada. Si alguien se separa, reagrúpense antes de empezar otro combate. Esta regla resiste mejor los cambios de parche, mapa y nivel que afirmar que una composición siempre es superior.",
                ],
                table={
                    "headers": ["Situación", "Función con espada y escudo", "Llamada de equipo"],
                    "rows": [
                        ["Sala desconocida", "Mantener una posición recuperable", "Explorar un ángulo antes de avanzar"],
                        ["Apertura clara", "Entrar en una ventana corta de presión", "Anunciar el objetivo y parar al terminar la ventana"],
                        ["Compañero separado", "Proteger la ruta para reagruparse", "Detener el avance hasta estar juntos"],
                        ["Salida incierta", "No sacrificar la retirada por otro intercambio", "Reiniciar o salir antes de buscar otra pelea"],
                    ],
                },
                links=[{"target": "trio-builds-guide", "label": "Usar los roles y la lista de respaldo para tríos"}],
            ),
            _section(
                "repeatable-test",
                "Plan breve para ajustar el build con pruebas repetibles",
                [
                    "Cuesta mejorar una configuración si cambias a la vez de clase, habilidad, equipo, ruta y nivel de riesgo. Sigue una secuencia breve y conserva estables la mayoría de las decisiones. Antes de entrar, anota una pregunta concreta: ¿la opción defensiva me dejó recolocarme?, ¿pude repetir la ventana ofensiva?, ¿seguía disponible la salida después del primer combate? Son observaciones útiles, pero no sustituyen una prueba de daño controlada.",
                    "Después de cada partida, anota el resultado en lenguaje sencillo. Escribe cuál fue la decisión más costosa, qué recurso te habría gustado conservar y si la partida terminó por el combate, la ruta o la separación del equipo. Cambia una parte relacionada para el siguiente intento. Si modificas varias cosas, registra el resultado como otro experimento y no atribuyas el cambio a un objeto concreto.",
                ],
                steps=[
                    "Mantén clase, armas, estilo de ruta y riesgo para la primera comparación.",
                    "Escoge una variable: una bonificación, una habilidad o una regla de tiempo.",
                    "Registra el objetivo, el error, la recuperación y el resultado de extracción.",
                    "Repite la misma pregunta antes de llamar mejora al cambio.",
                    "Revisa las notas del parche y el texto de objetos si cambió el sistema probado.",
                ],
                links=[{"target": "beginner-guide", "label": "Seguir el método de aprendizaje de bajo riesgo"}],
            ),
            _section(
                "mistakes-and-limits",
                "Errores frecuentes y límites de esta recomendación",
                [
                    "El primer error es confundir defensa con seguridad. Una herramienta defensiva puede tener una condición, un coste o una ventana; aprende su comportamiento antes de prolongar el intercambio. El segundo es acumular ataque porque una lista llama óptimo a un conjunto. Si no identificas cuándo sirve ese efecto, pruébalo antes de convertirlo en prioridad. El tercero es seguir una recomendación sin fecha de parche ni condiciones de prueba como si fuera una clasificación actual.",
                    "El cuarto error es cambiar demasiadas partes entre partidas. Un build puede parecer mejor porque cambió la ruta o el compañero, no porque el objeto sea superior. Conserva notas y no conviertas un éxito personal en regla universal. Las fuentes públicas disponibles describen la extracción, el equipo y el juego en solitario o en equipo; no aportan una fórmula de daño verificada para espada y escudo ni un ranking permanente. Usa este marco como inicio y reemplaza los supuestos con pruebas repetibles cuando las tengas.",
                ],
            ),
        ],
        "faq_title": "Preguntas frecuentes sobre el build de espada y escudo de Mistfall Hunter",
        "faq": [
            {"question": "¿Cuál es el mejor build de espada y escudo para Mistfall Hunter?", "answer": "Las fuentes usadas no confirman una configuración universalmente mejor. Empieza con una defensa clara, una ventana de presión repetible y una forma de reiniciar el combate. Comprueba los objetos y el parche actuales antes de confiar en una afirmación de meta sin fecha."},
            {"question": "¿Sirve un build de mercenario con espada y escudo para jugar solo?", "answer": "Puede ser un punto de partida razonable si la clase y el equipo actuales permiten la combinación, pero la consulta de Similarweb no confirma un build vigente. En solo, prioriza una ruta de regreso y una recuperación que no dependan de otro jugador."},
            {"question": "¿Qué estadísticas debo priorizar en el build?", "answer": "Usa los nombres y efectos que aparezcan en tu versión. Primero resuelve el problema que observaste y después añade un efecto de daño que puedas activar en una apertura previsible. Esta guía no inventa nombres, límites ni valores exactos."},
            {"question": "¿Funciona el build de espada y escudo en un trío?", "answer": "Puede encajar como ancla o presión controlada si el equipo acuerda quién llama la retirada y quién cubre las otras tareas. Si otro jugador ya ancla, cambia la función en vez de duplicarla. Prueba la composición en el parche actual."},
            {"question": "¿Conviene copiar un código de build de Mistfall Hunter?", "answer": "Úsalo como referencia inicial solo cuando se conozcan la fuente, el parche, la clase y los requisitos del equipo. Compara cada elección con tu juego y modifica una variable cada vez para saber qué aportó."},
        ],
        "summary_heading": "En resumen",
        "summary": "Trata el build de espada y escudo de Mistfall Hunter como un experimento por roles: conserva una retirada, usa ventanas cortas de presión, mantén visible la ruta en solo y asigna tareas claras en trío. Los objetos y sus valores exactos dependen del parche y no se verificaron aquí; compruébalos en el juego antes de llamar a una configuración la mejor.",
        "related_title": "Prepara la siguiente partida",
        "related_links": [
            {"target": "builds", "label": "Comparar patrones generales de Mistfall Hunter"},
            {"target": "classes", "label": "Revisar las funciones de clase"},
            {"target": "gameplay-guide", "label": "Repasar gameplay y extracción"},
            {"target": "trio-builds-guide", "label": "Planificar una composición de trío"},
            {"target": "beginner-guide", "label": "Empezar con una rutina de bajo riesgo"},
        ],
        "source_title": "Referencias oficiales y límites de la evidencia",
        "source_note": "La web oficial y la ficha de Steam se incluyen para el contexto general del juego y el equipo. Las capturas oficiales son ilustrativas. Desde este equipo no se pudo verificar una línea de estadísticas, rotación, ranking de objetos o build actual de espada y escudo; por eso las recomendaciones se expresan como funciones que deben probarse en el juego.",
        "official_links": [
            {"label": "Web oficial de Mistfall Hunter", "url": _OFFICIAL_URL, "rel": "noopener"},
            {"label": "Ficha oficial de Steam y sus imágenes", "url": _STEAM_URL, "rel": "noopener"},
        ],
    },
    "ja": {
        "slug": "mistfall-hunter-sword-and-shield-build",
        "primary_keyword": "Mistfall Hunter 剣と盾ビルド",
        "related_keywords": [
            "Mistfall Hunter 剣と盾のビルド",
            "Mistfall Hunter 傭兵 剣と盾 ビルド",
            "Mistfall Hunter ソロ 剣と盾 ビルド",
            "Mistfall Hunter 3人パーティー 剣と盾 ビルド",
        ],
        "title": "Mistfall Hunter 剣と盾ビルド：ソロとトリオを支える5つの優先事項",
        "meta_title": "Mistfall Hunter 剣と盾ビルド：5つの要点",
        "meta_description": "Mistfall Hunter 剣と盾ビルドの装備・スキル選び、ソロとトリオの調整、再現できるテスト手順を紹介。未確認の数値は断定しません。",
        "meta_keywords": "Mistfall Hunter 剣と盾ビルド, Mistfall Hunter 傭兵 剣と盾ビルド, ソロ 剣と盾ビルド, トリオ 剣と盾ビルド",
        "eyebrow": "Mistfall Hunter 武器ビルドガイド",
        "lede": "Mistfall Hunter 剣と盾ビルドは、状況を見て短く仕掛け、帰り道を残したい人にとって実用的な出発点です。ここでは検証されていない火力ランキングではなく、役割に基づく組み立て方を紹介します。現在のゲーム内で確認すべきことと、実際に試せる判断を分けて説明します。",
        "checked_label": "役割別ビルドの考え方を2026年10月24日に確認。個別装備の数値は断定しません",
        "entry_label": "Mistfall Hunterの剣と盾ビルドを見る",
        "checked_iso": "2026-10-24",
        "feature_image": {
            "path": _FEATURE_IMAGE,
            "alt": "剣と盾を携えたハンターを描く編集用ファンタジーコンセプトアート。短い文字でSword + Shieldと表示",
            "caption": "この記事用に作成した独立したコンセプトアートです。公式アートやゲーム画面ではありません。",
            "source_label": "この独立ガイドについて",
            "source_url": "/about/",
            "width": 1024,
            "height": 1024,
        },
        "facts_headers": ["ビルドの判断", "安全寄りの出発点", "調整する場面"],
        "facts_rows": [
            ["役割", "空間を保ち、退路を残す", "味方がすでに前衛役を担当している"],
            ["攻撃", "短く再現できる機会を使う", "現行バージョンの検証でタイミングが変わる"],
            ["装備", "生存手段と攻め手を一つずつ選ぶ", "現在の説明文から明確な交換先が分かる"],
            ["ソロ", "帰り道が見える間だけ戦利品を狙う", "退路や立て直し手段を失う"],
            ["トリオ", "前衛、攻撃、柔軟枠を分担する", "味方が離れた、または役割が重複する"],
        ],
        "intro": "Mistfall Hunter 剣と盾ビルドは、最適装備の一覧を追うのではなく、安定した役割から始めましょう。不利な交換の後に立て直せる余地を残し、明確な攻撃機会だけに火力を使い、出撃前に帰り方を決めます。公開情報からゲームの脱出ループと装備重視の方向性は分かりますが、恒久的に最適な装備名、能力値、タレント順までは確認できません。以下の優先事項をテスト計画として使い、具体的な数値は現在のバージョンで確かめてください。",
        "sections": [
            _section(
                "build-goal",
                "Mistfall Hunter 剣と盾ビルドで解決する課題",
                [
                    "大切なのは、盾が常に別の武器より強いかどうかではありません。この構成で状況を判断し、戦闘の代償を抑え、安全な経路へ戻れるかを考えます。近距離の武器は攻防を長引かせやすいため、盾を「すべての攻撃を防げる証拠」ではなく「接敵する瞬間を選ぶ理由」として扱ってください。入力方法、コスト、回復条件は変わる可能性があります。現在の説明を読み、ジャンルの慣習だけで決めつけずに試します。",
                    "この記事は役割ごとの考え方です。交戦を制御したい人、敵の動きを学びたい人、小隊で明確な担当が欲しい人に向いています。最大火力、唯一の正解、公式メタを示すものではありません。ゲーム内のクラス名や装備名が変わっていたら、判断基準を残して、現在のロードアウト画面に表示された名前を使ってください。",
                ],
                bullets=[
                    "仕掛ける前に、立て直しまたは離脱の手段を一つ残す。",
                    "表計算を見なくても判断できる攻撃機会を一つ選ぶ。",
                    "次の出撃から学べるよう、変更する装備やスキルは一つにする。",
                ],
                image={
                    "path": _COMBAT_IMAGE,
                    "alt": "大きな森の敵に向き合うMistfall Hunterのハンターを写したSteam公式ストア画像",
                    "caption": "間合いと戦闘の状況を示すSteam公式画像です。検証済みの剣と盾ビルドやダメージ値を示すものではありません。",
                    "source_label": "Steam公式ページを見る",
                    "source_url": _STEAM_URL,
                    "width": 1200,
                    "height": 675,
                },
            ),
            _section(
                "five-build-priorities",
                "Mistfall Hunter 剣と盾ビルドを整える5つの要点",
                [
                    "次の順番で優先します。これはビルドが可能にする行動の説明であり、固定のステータス名や非公開の計算式ではありません。現在の装備とスキルの説明を読み、同じ役割を果たす選択肢を探してください。二つの効果が有用に見える場合は、説明文の印象だけで決めず、出撃で繰り返し試せる方を選びます。",
                    "最初の構成は控えめにします。生存手段、繰り返せる攻撃、危険な部屋から離れる余地を用意してください。数回の出撃後、計画が破綻した場面を確認します。安全だが時間がかかるなら攻撃機会を調整します。攻撃できても帰り道を失ったなら、火力より立て直し方や判断のタイミングを見直します。",
                ],
                table={
                    "headers": ["優先事項", "探す効果", "避けること"],
                    "rows": [
                        ["1. 分かりやすい防御", "条件とコストを把握できる手段", "盾ですべての攻撃を防げると思う"],
                        ["2. 再現できる攻撃", "自分で作れる短い攻撃機会", "安全な経路を越えて敵を追う"],
                        ["3. 立て直し", "距離を取り、交換を止める方法", "最初の接敵ですべての防御行動を使う"],
                        ["4. 役に立つ装備", "実際に確認した問題を解決する効果", "現在の装備説明を読まず優先度をコピーする"],
                        ["5. チームへの貢献", "味方の役割を補える担当", "全員が同じ役割を選ぶ"],
                    ],
                },
                links=[{"target": "builds", "label": "サイトの汎用ビルド例と比較する"}],
            ),
            _section(
                "gear-skills",
                "装備、スキル、タレントは役割から選ぶ",
                [
                    "装備やタレントの現在の説明を読み、それがどんな判断を改善するのか考えます。防御効果は、長い交換で動けなくなる、再配置の余地がない、状況が変わったときに答えがない、といった失敗を防げる場合に役立ちます。ダメージ効果は、予測できる攻撃機会に発動できる場合に有効です。ほとんど作れない条件に依存しているなら、目立つ数値が実戦に結び付かないことがあります。",
                    "検索語の `Mistfall Hunter 傭兵 剣と盾 ビルド`だけを見て、クラス名、タレント順、装備セットが現在も正しいと判断しないでください。Similarwebでは関連語として見つかりましたが、今回確認できた公開データは現在のクラス別装備を裏付けていません。ゲーム画面に出ているクラス名、装備条件、コストを確認し、一つだけ変更します。更新日や試験条件のない情報は事実ではなく、確認の手掛かりとして扱います。",
                ],
                bullets=[
                    "スキルを軸にする前に、発動条件、コスト、回復時間を記録する。",
                    "危険から離れるのに役立つ装備を一つ残す。",
                    "発動する場面を説明できる場合にダメージ効果を採用する。",
                    "タレントが本当に判断を変えるのか、未確認の数字だけなのか確かめる。",
                ],
            ),
            _section(
                "solo-adjustment",
                "ソロ向け剣と盾ビルドの調整方法",
                [
                    "ソロでは別の角度を見たり撤退を確認したりする味方がいません。情報と再現性を優先し、不確かな場所を一つずつ進み、帰り道を見える状態に保ちます。防御手段があるからといって、戦闘を無期限に続けてよいわけではありません。後のために残していた立て直し手段を使ったなら、追加報酬を探す前に状況を見直します。",
                    "実用的なソロの流れは、目標を決め、到達コストを考え、何が起きたら離脱するかを先に決めることです。戦利品によって続行の価値は変わりますが、帰路そのものはなくなりません。ソロ向けの剣と盾ビルドを探しているなら、同じ優先事項から始め、味方が近くにいる場合だけ働く選択肢を外します。脱出全体の考え方はサイトのゲームプレイガイドと初心者ガイドも参照してください。",
                ],
                steps=[
                    "最初の危険な接敵の前に目標と帰路を決める。",
                    "現在の機会に必要な防御または攻撃だけを使う。",
                    "戦闘の後に体力、立て直し手段、経路の見通しを確認する。",
                    "残りの報酬が帰路の危険に見合わなくなったら脱出する。",
                ],
                image={
                    "path": _EXTRACTION_IMAGE,
                    "alt": "暗い部屋で光る宝箱へ向かうMistfall Hunterのキャラクターを写したSteam公式ストア画像",
                    "caption": "戦利品を持ち帰る判断を説明するSteam公式画像です。特定のルートや推奨装備を示すものではありません。",
                    "source_label": "Steam公式ページを見る",
                    "source_url": _STEAM_URL,
                    "width": 1200,
                    "height": 675,
                },
                links=[{"target": "gameplay-guide", "label": "ソロと脱出の流れを確認する"}],
            ),
            _section(
                "trio-adjustment",
                "トリオではビルドの役割をどう変えるか",
                [
                    "トリオでは、空間を保ち、撤退を伝えるのが得意なら剣と盾を前衛役にできます。これはチーム運用の提案であり、クラス固有の効果が確認されたという意味ではありません。誰が撤退を呼び、誰が短い攻撃機会を担当し、誰が偵察や立て直しを補うか決めましょう。検索されている傭兵の剣と盾ビルドを、単独で先行することと混同しないでください。味方がどの機会を待つのか理解している必要があります。",
                    "別のプレイヤーが前衛なら、同じ役割を重ねず、このビルドを制御した攻撃や柔軟な支援に寄せます。状況に反応できる距離は保ちながら、味方の声が届く範囲を意識してください。誰かが離れたら、次の戦闘を始める前に集合します。単一の編成がどのパッチ、マップ、腕前でも最強だと断言するより、この原則の方が長く使えます。",
                ],
                table={
                    "headers": ["状況", "剣と盾の担当", "チームの連携"],
                    "rows": [
                        ["未知の部屋", "立て直せる位置を保つ", "全員で進む前に一角を偵察する"],
                        ["明確な機会", "短い攻撃時間に集中する", "目標を伝え、時間が終わったら止める"],
                        ["味方が孤立", "集合できる経路を守る", "全員が揃うまで進撃を止める"],
                        ["出口が不明", "撤退を犠牲にして交換しない", "追加戦闘の前に立て直すか離脱する"],
                    ],
                },
                links=[{"target": "trio-builds-guide", "label": "トリオの役割と代替案を確認する"}],
            ),
            _section(
                "repeatable-test",
                "ビルドを調整するための短いテスト手順",
                [
                    "クラス、スキル、装備、経路、リスクを同時に変えると、何を改善すればよいか分かりません。多くの条件を固定した短い手順を使います。出撃前に一つだけ疑問を書きます。例えば、防御手段で再配置できたか、攻撃機会を繰り返せたか、初戦の後も帰路が使えたかです。これは観察の記録であり、管理されたダメージ試験の代わりではありません。",
                    "出撃後は結果を簡潔に残します。最も高くついた判断、残しておきたかった資源、戦闘・経路・分断のどれで失敗したかを記録してください。次の試行では関連する部分を一つだけ変えます。複数を変えた場合は別の実験として保存し、特定の装備が結果を生んだと決めつけないようにします。",
                ],
                steps=[
                    "最初の比較ではクラス、武器、経路の方針、リスクを固定する。",
                    "装備効果、スキル、タイミングのルールから一つだけ選ぶ。",
                    "目的、失敗した判断、立て直し手段、脱出結果を記録する。",
                    "改善と呼ぶ前に同じ疑問を再度確かめる。",
                    "対象システムが変わったらパッチ情報と装備説明を読み直す。",
                ],
                links=[{"target": "beginner-guide", "label": "低リスクで学ぶ5回の手順を使う"}],
            ),
            _section(
                "mistakes-and-limits",
                "よくあるミスと、このガイドで断定できないこと",
                [
                    "一つ目のミスは、防御を安全そのものと考えることです。防御手段には条件やコスト、使える時間があるかもしれません。長い交換に入る前に実際の挙動を確かめます。二つ目は、ガイドに最適と書いてあるからという理由だけで攻撃系の選択肢を積むことです。その効果が役立つ機会を特定できないなら、優先する前に試します。三つ目はパッチ日や試験条件のない情報を現在のランキングとして扱うことです。",
                    "四つ目は出撃ごとに多くの要素を変えることです。経路や味方が変わっただけなのに、装備が強くなったように感じる場合があります。メモを残し、一度の成功を全員に当てはまるルールにしないでください。公開情報は脱出、装備、ソロとチームで遊ぶ構造を説明していますが、剣と盾の検証済みダメージ式や永続的な装備順位は示していません。ここでの考え方を出発点にし、繰り返せる証拠で更新してください。",
                ],
            ),
        ],
        "faq_title": "Mistfall Hunterの剣と盾ビルドに関するFAQ",
        "faq": [
            {"question": "Mistfall Hunterで最強の剣と盾ビルドは何ですか？", "answer": "今回の情報源では、常に最強となる構成は確認できませんでした。分かりやすい防御、再現できる攻撃機会、立て直し手段から始め、日付のないメタ情報を信じる前に現在の装備説明とパッチを確かめてください。"},
            {"question": "傭兵の剣と盾ビルドはソロに向いていますか？", "answer": "現在のクラスと装備で組み合わせられるなら、役割を決める出発点になります。ただしSimilarwebの検索語だけでは現行ビルドを検証できません。ソロでは帰路を保ち、味方に頼らない立て直しを優先します。"},
            {"question": "剣と盾のビルドではどの能力値を優先すべきですか？", "answer": "現在のゲーム内に表示される能力値名と効果を使います。まず実際に起きた失敗を解決し、その後に予測可能な機会で使える攻撃効果を選びます。未確認の名前、閾値、数値はこのガイドでは作っていません。"},
            {"question": "剣と盾ビルドはトリオでも使えますか？", "answer": "誰が撤退を呼び、他の役割を誰が担当するか決めているなら、前衛または制御した攻撃に使えます。他のプレイヤーが前衛なら役割を調整し、現行パッチでチームの組み合わせを試してください。"},
            {"question": "Mistfall Hunterのビルドコードをそのまま使うべきですか？", "answer": "情報源、パッチ、クラス、装備条件が分かる場合に限り、最初の参考として使ってください。自分のバージョンと比べ、効果を判断できるよう一度に一項目だけ変更します。"},
        ],
        "summary_heading": "要点",
        "summary": "Mistfall Hunterの剣と盾ビルドは、役割に基づく実験として扱います。退路を残し、短い攻撃機会を使い、ソロでは帰路を見える状態にし、トリオでは担当を決めてください。個別装備の数値はパッチに依存し、ここでは検証していません。最強装備と断定する前に現在のゲーム内で確認しましょう。",
        "related_title": "次の出撃の準備を続ける",
        "related_links": [
            {"target": "builds", "label": "Mistfall Hunterの汎用ビルド例を比較する"},
            {"target": "classes", "label": "クラスの役割を確認する"},
            {"target": "gameplay-guide", "label": "ゲームプレイと脱出の流れを確認する"},
            {"target": "trio-builds-guide", "label": "トリオ編成を考える"},
            {"target": "beginner-guide", "label": "低リスクの練習方法から始める"},
        ],
        "source_title": "公式の参照先と根拠の範囲",
        "source_note": "公式サイトとSteam掲載ページは、ゲーム全体と装備に関する背景の参照先として掲載しています。公式スクリーンショットも状況説明に限って使用します。この端末から現在の剣と盾の能力値、スキル回し、装備ランキング、最適ビルドを確認できなかったため、本文はゲーム内で試す役割の考え方として記載しています。",
        "official_links": [
            {"label": "Mistfall Hunter公式サイト", "url": _OFFICIAL_URL, "rel": "noopener"},
            {"label": "Steam公式掲載と画像", "url": _STEAM_URL, "rel": "noopener"},
        ],
    },
    "fr": {
        "slug": "mistfall-hunter-sword-and-shield-build",
        "primary_keyword": "build épée et bouclier Mistfall Hunter",
        "related_keywords": ["build mercenaire Mistfall Hunter", "meilleur build épée et bouclier Mistfall Hunter", "build épée et bouclier Mistfall Hunter en solo", "build épée et bouclier Mistfall Hunter en trio"],
        "title": "Build épée et bouclier Mistfall Hunter : 5 priorités pour jouer en solo ou en trio",
        "meta_title": "Build épée et bouclier Mistfall Hunter : 5 priorités",
        "meta_description": "Préparez un build épée et bouclier pour Mistfall Hunter avec des priorités d'équipement et de compétences, des conseils solo et trio et une méthode de test sans statistiques inventées.",
        "meta_keywords": "build épée et bouclier Mistfall Hunter, build mercenaire Mistfall Hunter, build Mistfall Hunter solo épée et bouclier, build Mistfall Hunter trio",
        "eyebrow": "Guide de build d'arme Mistfall Hunter",
        "lede": "L'épée et le bouclier conviennent à une approche qui privilégie la lecture du combat, les engagements courts et une voie de repli claire. Construisez votre équipement autour de décisions répétables plutôt que d'un classement de dégâts non vérifié : prévoyez une réponse défensive, une fenêtre d'attaque fiable et un moyen de reprendre de la distance. Les conseils généraux sont séparés des valeurs propres à une mise à jour, qui doivent encore être testées en jeu.",
        "checked_label": "Cadre de build par rôle vérifié le 24 octobre 2026 ; aucune valeur d'objet exacte n'est affirmée",
        "entry_label": "Lire le guide du build épée et bouclier de Mistfall Hunter",
        "checked_iso": "2026-10-24",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "Illustration éditoriale conceptuelle d'un chasseur avec épée et bouclier, portant le court texte Sword + Shield", "caption": "Illustration conceptuelle créée pour ce guide ; ce n'est ni une image officielle de Mistfall Hunter ni une capture du jeu.", "source_label": "À propos de ce guide indépendant", "source_url": "/fr/about/", "width": 1024, "height": 1024},
        "facts_headers": ["Décision de build", "Point de départ prudent", "Quand l'adapter"],
        "facts_rows": [["Rôle", "Contrôler l'espace et garder une option de repli", "Un équipier tient déjà la ligne"], ["Dégâts", "Privilégier des ouvertures courtes et répétables", "Un test ou une mise à jour vérifiée change le rythme"], ["Équipement", "Garder une réponse de survie et une option offensive", "Les descriptions actuelles justifient un autre compromis"], ["Solo", "Ne prendre du butin que si la sortie reste lisible", "La route ou la récupération n'est plus sûre"], ["Trio", "Répartir ancrage, pression et flexibilité", "Un joueur est isolé ou les rôles se chevauchent"]],
        "intro": "Pour un build épée et bouclier dans Mistfall Hunter, commencez par un rôle stable au lieu de chercher une liste d'équipement soi-disant optimale. Gardez une marge pour vous remettre d'un échange défavorable, n'engagez vos dégâts que lorsqu'une ouverture est claire et décidez comment sortir avant d'avancer. Les informations publiques décrivent la boucle d'extraction et l'équipement, mais ne vérifient pas une combinaison permanente de noms d'objets, de statistiques ou de talents. Utilisez les priorités ci-dessous comme hypothèses à tester et confirmez chaque valeur exacte dans votre version du jeu.",
        "sections": [
            _section("build-goal", "Ce que ce build épée et bouclier doit résoudre", [
                "La bonne question n'est pas de savoir si un bouclier est toujours supérieur à une autre arme. Demandez-vous plutôt si cette configuration vous permet de choisir un échange, d'en supporter le coût et de retrouver une route sûre. Le combat rapproché incite à prolonger les affrontements : le bouclier doit vous aider à contrôler l'engagement, pas vous faire croire que chaque coup peut être bloqué. Les commandes exactes, les règles défensives et le coût de récupération peuvent évoluer ; vérifiez les descriptions et testez-les.",
                "Ce guide propose un cadre de build fondé sur les rôles. Il s'adresse aux joueurs qui préfèrent un contact maîtrisé, veulent apprendre une rencontre ou ont besoin d'une mission claire en petit groupe. Il ne prétend pas que l'épée et le bouclier infligent les meilleurs dégâts, constituent la seule option viable ou forment un build méta officiel. Si votre version emploie d'autres noms de classes ou d'objets, gardez les règles de décision et remplacez les termes par ceux affichés dans votre équipement.",
            ], bullets=["Gardez une option de récupération ou de désengagement avant de vous engager.", "Choisissez une fenêtre offensive que vous pouvez reconnaître sans tableur de dégâts.", "Ne changez qu'un objet ou une compétence à la fois pour apprendre de la partie suivante."], image={"path": _COMBAT_IMAGE, "alt": "Capture officielle Steam montrant un personnage de Mistfall Hunter face à une grande créature dans une forêt", "caption": "Image officielle Steam pour illustrer l'espacement et le contexte d'un combat ; elle ne présente ni un build épée et bouclier testé ni des valeurs de dégâts.", "source_label": "Voir la fiche Steam officielle", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("five-build-priorities", "Cinq priorités pour un build épée et bouclier plus sûr", [
                "Suivez ces priorités dans l'ordre. Elles décrivent ce que l'équipement doit vous permettre de faire, pas des noms de statistiques fixes ni des formules cachées. Ouvrez les descriptions actuelles de vos objets et compétences, puis retenez les options qui remplissent le même rôle. Si deux bonus semblent intéressants, préférez celui que vous pouvez tester de façon répétée à celui dont le chiffre paraît impressionnant hors contexte.",
                "Un premier essai doit rester modeste : une réponse de survie, une action offensive reproductible et assez de souplesse pour quitter une mauvaise salle. Après plusieurs sorties, repérez le moment où le plan a cessé de fonctionner. Si vous êtes resté en vie mais trop lent, augmentez la pression. Si vous avez infligé des dégâts sans garder la sortie, améliorez votre récupération ou votre décision d'abord.",
            ], table={"headers": ["Priorité", "À rechercher", "À éviter"], "rows": [["1. Défense lisible", "Une option dont la condition et le coût sont compris", "Supposer qu'un bouclier bloque toutes les sources de dégâts"], ["2. Pression répétable", "Une courte fenêtre d'attaque que vous provoquez", "Poursuivre au-delà de la route sûre"], ["3. Récupération", "Un moyen clair de reprendre de l'espace", "Dépenser toutes les actions défensives au premier contact"], ["4. Équipement utile", "Des bonus qui corrigent un problème observé", "Copier une priorité sans lire les descriptions actuelles"], ["5. Valeur d'équipe", "Un rôle complémentaire à celui des alliés", "Laisser trois joueurs prendre le même rôle par défaut"]]}, links=[{"target": "builds", "label": "Comparer cette configuration ciblée aux tendances de build du site"}]),
            _section("gear-skills", "Choisir l'équipement, les compétences et les talents par fonction", [
                "Lisez la description de chaque objet ou talent dans la version actuelle et demandez-vous quelle décision il améliore. Un effet défensif n'est utile que s'il corrige un échec réel : rester pris dans un échange trop long, manquer de place pour se repositionner ou ne pas pouvoir réagir quand le combat change. Un effet offensif aide lorsqu'il se déclenche pendant une ouverture prévisible. Si son activation dépend d'une condition que vous créez rarement, son chiffre principal peut ne rien apporter à votre partie.",
                "Ne reprenez pas une formule comme « build mercenaire épée et bouclier Mistfall Hunter » comme preuve qu'un nom de classe, un ordre de talents ou un ensemble est encore valable. Similarweb montre que cette formulation fait partie du groupe de requêtes ; les sources publiques examinées ne confirment pas un build actuel vérifié. Notez les noms visibles, leur coût et les conditions, puis testez une seule pièce avant de reconstruire tout l'équipement.",
            ], bullets=["Une option défensive répond à une erreur que vous avez réellement observée.", "Une compétence offensive a une fenêtre d'utilisation que vous pouvez reproduire.", "Les talents complètent les conditions de l'équipement au lieu de les dupliquer."], links=[{"target": "classes", "label": "Comparer les rôles de classe avant de choisir votre spécialité"}]),
            _section("solo-play", "Adapter le build épée et bouclier aux sorties solo", [
                "En solo, votre trajet de retour est aussi important que la prochaine cible. Avant d'entrer dans une salle, repérez l'espace où reculer, la sortie la plus claire et l'option qui vous permet de récupérer après le premier échange. N'entrez pas au seul motif que le bouclier semble rassurant. S'il n'y a pas d'ouverture nette, contournez la salle ou attendez. Cette approche n'est pas une garantie de survie ; elle limite simplement le nombre de décisions risquées prises sans information.",
                "Après un combat, vérifiez votre état, les ressources de récupération et la lisibilité de l'itinéraire. Comparez la récompense restante au risque de rentrer. Un build solo peut conserver une option offensive, mais il ne doit pas dépendre d'un allié pour attirer un adversaire ou couvrir un repli. Si un élément du plan ne fonctionne que lorsque l'ennemi reste immobile ou que la sortie est libre, considérez-le comme une condition à vérifier, pas comme une certitude.",
            ], steps=["Avant d'engager, repérer l'itinéraire de repli et un endroit où reprendre de l'espace.", "N'utiliser que la défense ou l'attaque utile à l'ouverture présente.", "Après le combat, contrôler l'état, la récupération et la route.", "Quitter la zone quand le butin restant ne justifie plus le trajet retour."], image={"path": _EXTRACTION_IMAGE, "alt": "Capture officielle Steam de Mistfall Hunter montrant un personnage près d'un coffre lumineux dans une pièce sombre", "caption": "Image officielle Steam utilisée pour expliquer le choix de rapporter le butin ; elle ne montre ni une route recommandée ni un équipement précis.", "source_label": "Voir la fiche Steam officielle", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "gameplay-guide", "label": "Revoir la boucle de jeu et d'extraction en solo"}]),
            _section("trio-adjustment", "Adapter le rôle en trio", [
                "En trio, l'épée et le bouclier peuvent tenir la ligne si vous savez préserver l'espace et annoncer le repli. C'est une proposition de coordination, pas la confirmation d'un effet réservé à une classe. Décidez qui appelle la retraite, qui profite d'une courte ouverture et qui repère ou aide à récupérer. Ne confondez pas la recherche d'un build mercenaire avec le fait de partir seul devant : les autres doivent comprendre quelle occasion vous attendez.",
                "Si un autre joueur tient déjà la ligne, évitez de superposer les mêmes fonctions. Orientez plutôt ce build vers une pression contrôlée ou un soutien adaptable, tout en restant assez proche pour réagir aux appels de l'équipe. Si un membre est séparé, rassemblez-vous avant de commencer le prochain combat. Ces principes durent généralement mieux qu'une affirmation selon laquelle une composition serait la meilleure sur chaque carte, mise à jour ou niveau d'expérience.",
            ], table={"headers": ["Situation", "Rôle épée et bouclier", "Coordination"], "rows": [["Salle inconnue", "Garder une position de récupération", "Explorer un angle avant d'avancer"], ["Ouverture claire", "Concentrer une courte attaque", "Annoncer la cible puis arrêter à la fin"], ["Allié isolé", "Protéger un chemin de regroupement", "Suspendre la progression jusqu'au rassemblement"], ["Sortie incertaine", "Ne pas échanger le repli contre des dégâts", "Se regrouper ou quitter avant un autre combat"]]}, links=[{"target": "trio-builds-guide", "label": "Répartir les rôles et prévoir des solutions de remplacement en trio"}]),
            _section("repeatable-test", "Une méthode courte pour tester et régler le build", [
                "Si vous changez de classe, de compétences, d'équipement, d'itinéraire et de niveau de risque à la fois, vous ne saurez pas ce qui a amélioré le résultat. Gardez la plupart des conditions fixes. Avant de partir, notez une question précise : la défense m'a-t-elle permis de me repositionner ? Ai-je pu répéter mon ouverture offensive ? La sortie restait-elle accessible après le premier combat ? Cette observation sert à orienter les essais ; elle ne remplace pas un test de dégâts contrôlé.",
                "Après la sortie, consignez la décision qui a coûté le plus cher, la ressource que vous auriez voulu garder et la cause principale de l'échec : combat, trajet ou séparation de l'équipe. Modifiez un élément pertinent lors de l'essai suivant. Si vous en changez plusieurs, notez-le comme une expérience distincte et n'attribuez pas le résultat à un objet particulier. Relisez les notes de mise à jour et les descriptions si le jeu change.",
            ], steps=["Garder la classe, l'arme, la règle d'itinéraire et le niveau de risque constants au premier essai.", "Choisir une seule question sur l'effet d'un équipement, une compétence ou un timing.", "Noter l'objectif, la décision ratée, la récupération et le résultat de l'extraction.", "Répéter la même question avant de qualifier le changement d'amélioration.", "Relire les notes de mise à jour si le système testé a évolué."], links=[{"target": "beginner-guide", "label": "Utiliser le parcours d'apprentissage à faible risque en cinq sorties"}]),
            _section("mistakes-and-limits", "Erreurs fréquentes et limites de ce guide", [
                "Première erreur : confondre défense et sécurité. Une action défensive peut avoir une condition, un coût ou une durée limitée. Vérifiez son fonctionnement avant de prolonger un échange. Deuxième erreur : ajouter des effets offensifs parce qu'un guide les qualifie d'optimaux. Si vous ne pouvez pas identifier une occasion où ils servent, testez-les avant de les privilégier. Troisième erreur : prendre une liste sans date ni conditions pour le classement actuel.",
                "Une autre erreur consiste à changer trop d'éléments à chaque sortie. Un itinéraire ou un équipier différent peut donner l'impression qu'un objet a rendu le build plus fort. Gardez des notes et ne transformez pas une réussite isolée en règle générale. Les informations publiques décrivent l'extraction, l'équipement et le jeu en solo ou en équipe, mais pas des formules de dégâts épée et bouclier validées ni un classement durable. Utilisez ces décisions comme point de départ et mettez-les à jour avec des essais répétables.",
            ]),
        ],
        "faq_title": "FAQ sur le build épée et bouclier de Mistfall Hunter",
        "faq": [{"question": "Quel est le meilleur build épée et bouclier dans Mistfall Hunter ?", "answer": "Les sources examinées ne confirment pas une configuration toujours optimale. Commencez par une défense compréhensible, une ouverture offensive répétable et un moyen de récupérer. Vérifiez les objets et la mise à jour en cours avant de suivre une liste sans date."}, {"question": "Le build mercenaire épée et bouclier convient-il au solo ?", "answer": "Si la classe et l'équipement actuels permettent cette association, elle peut servir de base à un rôle clair. Une requête Similarweb ne vérifie pas un build actuel. En solo, gardez une route de retour et une récupération qui ne dépend pas d'un allié."}, {"question": "Quelles statistiques prioriser dans un build épée et bouclier ?", "answer": "Utilisez les noms et effets de statistiques affichés dans votre version. Corrigez d'abord un échec observé, puis choisissez un effet offensif utile dans une occasion prévisible. Ce guide n'invente ni nom, ni seuil, ni valeur."}, {"question": "Le build épée et bouclier peut-il fonctionner en trio ?", "answer": "Oui, comme rôle de ligne ou de pression contrôlée si l'équipe sait qui annonce le repli et qui remplit les autres fonctions. Si un allié tient déjà la ligne, adaptez le rôle et testez la composition dans la version actuelle."}, {"question": "Faut-il copier un code de build Mistfall Hunter tel quel ?", "answer": "Seulement comme point de départ lorsque la source, la mise à jour, la classe et les conditions d'équipement sont connues. Comparez-le à votre version et changez un seul élément à la fois pour comprendre son effet."}],
        "summary_heading": "En bref",
        "summary": "Traitez le build épée et bouclier de Mistfall Hunter comme une expérience guidée par le rôle. Gardez un repli, utilisez des ouvertures courtes, rendez la route de retour prioritaire en solo et répartissez les tâches en trio. Les valeurs d'objets dépendent de la mise à jour et ne sont pas vérifiées ici ; consultez le jeu avant d'affirmer qu'un équipement est optimal.",
        "related_title": "Préparer votre prochaine sortie",
        "related_links": [{"target": "builds", "label": "Comparer les builds généraux de Mistfall Hunter"}, {"target": "classes", "label": "Comparer les rôles de classe"}, {"target": "gameplay-guide", "label": "Comprendre le gameplay et l'extraction"}, {"target": "trio-builds-guide", "label": "Préparer la composition du trio"}, {"target": "beginner-guide", "label": "Commencer par les essais à faible risque"}],
        "source_title": "Sources officielles et limites des preuves",
        "source_note": "Le site officiel et la fiche Steam fournissent un contexte sur le jeu et son équipement. Les captures Steam officielles ne servent qu'à illustrer ce contexte. Les valeurs actuelles de l'épée et du bouclier, les rotations de compétences, les classements et le build optimal n'ont pas pu être vérifiés ici ; le texte présente donc des décisions à tester en jeu.",
        "official_links": [{"label": "Site officiel de Mistfall Hunter", "url": _OFFICIAL_URL, "rel": "noopener"}, {"label": "Fiche et images officielles sur Steam", "url": _STEAM_URL, "rel": "noopener"}],
    },
    "de": {
        "slug": "mistfall-hunter-sword-and-shield-build",
        "primary_keyword": "Mistfall Hunter Schwert und Schild Build",
        "related_keywords": ["Mistfall Hunter Söldner Schwert und Schild Build", "bestes Schwert und Schild Build Mistfall Hunter", "Mistfall Hunter Schwert und Schild Build solo", "Mistfall Hunter Schwert und Schild Build Trio"],
        "title": "Mistfall Hunter Schwert und Schild Build: 5 Prioritäten für Solo und Trio",
        "meta_title": "Mistfall Hunter Schwert und Schild Build: 5 Prioritäten",
        "meta_description": "Plane ein Mistfall Hunter Schwert und Schild Build mit Ausrüstungs- und Fertigkeitsprioritäten, Anpassungen für Solo und Trio sowie einem Testplan ohne erfundene Werte.",
        "meta_keywords": "Mistfall Hunter Schwert und Schild Build, Mistfall Hunter Söldner Build, Schwert und Schild Build solo, Schwert und Schild Build Trio",
        "eyebrow": "Mistfall Hunter Waffen-Build-Guide",
        "lede": "Schwert und Schild passen zu einem Ansatz, bei dem du den Kampf lesen, dich kurz festlegen und einen Rückweg offenhalten möchtest. Richte die Ausrüstung nach wiederholbaren Entscheidungen aus, nicht nach einer ungeprüften Schadensrangliste: Plane eine defensive Antwort, ein verlässliches Angriffsfenster und eine Möglichkeit zum Zurücksetzen ein. Allgemeine Empfehlungen sind von versionsabhängigen Werten getrennt, die du im aktuellen Spiel noch prüfen musst.",
        "checked_label": "Rollenbasierter Build-Rahmen, geprüft am 24. Oktober 2026; keine exakten Gegenstandswerte behauptet",
        "entry_label": "Mistfall Hunter Schwert und Schild Build lesen",
        "checked_iso": "2026-10-24",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "Redaktionelles Konzeptbild eines Jägers mit Schwert und Schild und dem kurzen Schriftzug Sword + Shield", "caption": "Originales Konzeptbild für diesen Guide; keine offizielle Mistfall-Hunter-Grafik und kein Screenshot aus dem Spiel.", "source_label": "Über diesen unabhängigen Guide", "source_url": "/de/about/", "width": 1024, "height": 1024},
        "facts_headers": ["Build-Entscheidung", "Sicherer Startpunkt", "Wann anpassen"],
        "facts_rows": [["Rolle", "Raum halten und einen Rückzug ermöglichen", "Ein Teammitglied übernimmt bereits die Ankerrolle"], ["Schaden", "Kurze, wiederholbare Gelegenheiten nutzen", "Ein geprüfter Patch oder Test verändert das Timing"], ["Ausrüstung", "Eine Überlebenshilfe und eine Druckoption behalten", "Aktuelle Beschreibungen sprechen für einen anderen Tausch"], ["Solo", "Beute nur mit lesbarem Rückweg einsammeln", "Route oder Erholung sind nicht mehr klar"], ["Trio", "Anker, Druck und Flexibilität verteilen", "Jemand ist isoliert oder Rollen überschneiden sich"]],
        "intro": "Beginne für ein Mistfall Hunter Schwert und Schild Build mit einer stabilen Aufgabe, statt einer angeblich besten Ausrüstungsliste hinterherzujagen. Behalte genug Spielraum, um einen schlechten Austausch abzufangen, nutze Schaden erst bei einer klaren Gelegenheit und entscheide vor dem Angriff, wie du wieder herauskommst. Öffentliche Informationen bestätigen die allgemeine Extraktionsschleife und Ausrüstung, aber keine dauerhaft beste Kombination aus Gegenstandsnamen, Werten oder Talenträngen. Nutze die Prioritäten als prüfbare Ausgangshypothese und bestätige genaue Werte in deiner Spielversion.",
        "sections": [
            _section("build-goal", "Welches Problem dieses Schwert und Schild Build lösen soll", ["Die nützliche Frage lautet nicht, ob ein Schild immer besser als eine andere Waffe ist. Entscheidend ist, ob du mit dieser Kombination einen Austausch wählen, dessen Kosten tragen und zu einem sicheren Weg zurückkehren kannst. Nahkampf verleitet zu langen Gefechten. Nutze das Schild deshalb, um deinen Einsatz zu kontrollieren, nicht als Beweis, dass jeder Treffer geblockt werden kann. Eingaben, Verteidigungsregeln und Erholungskosten können sich ändern; lies die aktuellen Beschreibungen und teste sie.", "Dieser Guide ist ein rollenbasierter Rahmen für Spieler, die kontrollierten Kontakt bevorzugen, einen Kampf lernen oder im kleinen Team eine klare Aufgabe brauchen. Er behauptet nicht, dass Schwert und Schild den höchsten Schaden verursachen, die einzige sinnvolle Wahl oder ein offizielles Meta-Build sind. Falls deine Version andere Klassen- oder Gegenstandsnamen verwendet, behalte die Entscheidungsregeln bei und ersetze die Begriffe durch das, was dein Ausrüstungsbildschirm zeigt."], bullets=["Vor dem Angriff eine Erholungs- oder Rückzugsoption verfügbar halten.", "Ein offensives Zeitfenster wählen, das du ohne Schadensrechner erkennst.", "Nur einen Gegenstand oder eine Fähigkeit ändern, damit der nächste Lauf etwas aussagt."], image={"path": _COMBAT_IMAGE, "alt": "Offizieller Steam-Store-Screenshot mit einer Mistfall-Hunter-Figur vor einem großen Waldmonster", "caption": "Offizielles Steam-Bild als allgemeiner Kontext für Abstand und Kampf; es zeigt weder ein getestetes Schwert und Schild Build noch Schadenswerte.", "source_label": "Offizielle Steam-Seite öffnen", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("five-build-priorities", "Fünf Prioritäten für ein sichereres Schwert und Schild Build", ["Diese Prioritäten beschreiben, was dein Build ermöglichen soll, nicht feste Stat-Namen oder verborgene Formeln. Öffne die aktuellen Beschreibungen deiner Ausrüstung und Fähigkeiten und wähle sichtbare Optionen nach ihrer Funktion. Wenn zwei Boni nützlich klingen, bevorzuge den, den du wiederholt testen kannst, statt den Wert, der ohne Zusammenhang am größten aussieht. So vergleichst du tatsächliche Entscheidungen, nicht nur einzelne Zahlen.", "Ein guter erster Versuch bleibt bewusst einfach: eine Überlebensantwort, eine verlässliche Schadensaktion und genug Flexibilität, um einen schlechten Raum zu verlassen. Prüfe nach einigen Läufen, an welchem Punkt der Plan scheiterte. Warst du sicher, aber zu langsam, passe den Druck an. Hast du Schaden gemacht, aber den Rückweg verloren, verbessere erst Erholung oder Entscheidungszeitpunkt, bevor du weitere Angriffswerte hinzufügst."], table={"headers": ["Priorität", "Darauf achten", "Vermeiden"], "rows": [["1. Verständliche Verteidigung", "Bekannte Bedingung und Kosten", "Annehmen, ein Schild stoppe jede Schadensquelle"], ["2. Wiederholbarer Druck", "Ein gezielt erzeugtes kurzes Angriffsfenster", "Eine Verfolgung über den sicheren Weg hinaus"], ["3. Erholung", "Ein klarer Weg zu mehr Abstand", "Alle defensiven Aktionen beim ersten Kontakt ausgeben"], ["4. Sinnvolle Ausrüstung", "Boni passend zu einem beobachteten Problem", "Eine Stat-Priorität ohne aktuelle Beschreibung kopieren"], ["5. Teambeitrag", "Eine Aufgabe, die andere Rollen ergänzt", "Drei Spieler wählen dieselbe Aufgabe"]]}, links=[{"target": "builds", "label": "Dieses fokussierte Setup mit allgemeinen Build-Mustern vergleichen"}]),
            _section("gear-skills", "Ausrüstung, Fähigkeiten und Talente nach ihrer Aufgabe wählen", ["Lies die Beschreibung jedes Gegenstands oder Talents in der aktuellen Version und frage, welche Entscheidung dadurch besser wird. Ein defensiver Effekt hilft nur, wenn er einen tatsächlichen Fehlerpunkt verändert: in einem langen Austausch festzuhängen, den Platz zum Neuaufstellen zu verlieren oder auf eine Änderung im Kampf keine Antwort zu haben. Ein Schadenseffekt ist nützlich, wenn du ihn in einer vorhersehbaren Öffnung auslösen kannst. Hängt er von einer seltenen Bedingung ab, hilft sein Spitzenwert deinem Lauf womöglich nicht.", "Verwende „Mistfall Hunter Söldner Schwert und Schild Build“ nicht als Beleg, dass Klassenname, Talentreihenfolge oder Ausrüstung noch aktuell sind. Similarweb zeigt diese Formulierung in der Suchgruppe; öffentliche Quellen bestätigen für diesen Guide jedoch kein verifiziertes aktuelles Build. Notiere sichtbare Namen, Kosten und Bedingungen und teste ein Teil, bevor du alles umstellst. Änderungen an der Ausrüstung sollten ein Problem lösen, das du selbst beobachtet hast."], bullets=["Eine defensive Option antwortet auf einen selbst beobachteten Fehler.", "Eine offensive Fähigkeit hat ein wiederholbares Zeitfenster.", "Talente ergänzen die Ausrüstung, statt ihre Bedingungen zu verdoppeln."], links=[{"target": "classes", "label": "Klassenrollen vergleichen, bevor du dich spezialisierst"}]),
            _section("solo-play", "Das Schwert und Schild Build an Sololäufe anpassen", ["Im Solo ist der Rückweg so wichtig wie das nächste Ziel. Erkenne vor einem Raum, wo du dich zurückziehen kannst, welcher Ausgang am klarsten ist und welche Option dir nach dem ersten Austausch Erholung verschafft. Betritt den Kampf nicht nur, weil sich ein Schild sicher anfühlt. Fehlt eine klare Öffnung, umgehe den Raum oder warte. Das garantiert kein Überleben; es begrenzt riskante Entscheidungen, die du ohne Informationen triffst.", "Prüfe nach einem Kampf deinen Zustand, verfügbare Erholung und die Übersicht über die Route. Vergleiche die übrige Beute mit dem Risiko des Rückwegs. Ein Solo-Build kann eine Angriffsoption behalten, sollte aber nicht darauf angewiesen sein, dass ein Teammitglied Gegner ablenkt oder den Rückzug deckt. Funktioniert ein Teil des Plans nur bei einem stillstehenden Gegner oder freiem Ausgang, behandle das als zu prüfende Bedingung und nicht als Tatsache."], steps=["Vor dem Angriff Rückweg und Platz zum Neuaufstellen erkennen.", "Nur die Verteidigung oder den Angriff nutzen, die zum Zeitfenster passen.", "Nach dem Kampf Zustand, Erholung und Route prüfen.", "Das Gebiet verlassen, wenn die Beute den Rückweg nicht mehr rechtfertigt."], image={"path": _EXTRACTION_IMAGE, "alt": "Offizieller Mistfall-Hunter-Steam-Screenshot mit einer Figur nahe einer leuchtenden Truhe in einem dunklen Raum", "caption": "Offizielles Steam-Bild zur Entscheidung, Beute herauszutragen; es zeigt weder eine empfohlene Route noch eine konkrete Ausrüstung.", "source_label": "Offizielle Steam-Seite öffnen", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "gameplay-guide", "label": "Den Ablauf von Solo-Spiel und Extraktion ansehen"}]),
            _section("trio-adjustment", "Die Rolle im Trio anpassen", ["Im Trio kann Schwert und Schild den Anker bilden, wenn du Raum hältst und den Rückzug ansagst. Das ist ein Vorschlag für Teamabläufe, keine bestätigte Klassenfähigkeit. Legt fest, wer den Rückzug ruft, wer kurze Angriffsfenster nutzt und wer erkundet oder bei der Erholung unterstützt. Ein Söldner-Build ist kein Freibrief, allein vorzurücken; die anderen müssen wissen, auf welche Gelegenheit du wartest.", "Ist ein anderer Spieler bereits der Anker, stapelt nicht dieselbe Funktion doppelt. Richte dieses Build auf kontrollierten Druck oder flexible Unterstützung aus und bleib nah genug, um auf Teamrufe zu reagieren. Wird jemand getrennt, sammelt euch vor dem nächsten Gefecht. Diese Regeln sind nützlicher als die Behauptung, eine Zusammenstellung sei auf jeder Karte, in jedem Patch und für jedes Erfahrungsniveau die beste."], table={"headers": ["Lage", "Schwert und Schild", "Abstimmung"], "rows": [["Unbekannter Raum", "Position mit Erholungsweg halten", "Einen Winkel erkunden"], ["Klare Öffnung", "Kurzen Angriff konzentrieren", "Ziel ansagen und danach stoppen"], ["Mitspieler getrennt", "Weg zum Sammeln sichern", "Bis zum Zusammenschluss nicht vorrücken"], ["Ausgang unklar", "Rückzug nicht für Schaden tauschen", "Vor einem weiteren Kampf sammeln oder gehen"]]}, links=[{"target": "trio-builds-guide", "label": "Trio-Aufgaben und Ausweichpläne vergleichen"}]),
            _section("repeatable-test", "Ein kurzer Testplan zum Anpassen des Builds", ["Wenn du Klasse, Fähigkeiten, Ausrüstung, Route und Risiko zugleich änderst, erfährst du nicht, was das Ergebnis verbessert hat. Halte die meisten Bedingungen konstant. Notiere vor dem Lauf eine Frage: Hat mir die Verteidigung erlaubt, mich neu aufzustellen? Konnte ich mein Angriffsfenster wiederholen? War der Rückweg nach dem ersten Kampf erreichbar? Diese Beobachtung lenkt den nächsten Versuch, ersetzt aber keinen kontrollierten Schadensvergleich.", "Schreibe nach dem Lauf die teuerste Entscheidung, die gern behaltene Ressource und die Hauptursache des Fehlschlags auf: Kampf, Route oder Trennung. Ändere im nächsten Versuch einen passenden Faktor. Änderst du mehrere, führe es als separates Experiment und schreibe den Erfolg nicht einem Gegenstand zu. Lies Patch-Notizen und Beschreibungen neu, wenn sich das getestete System ändert. So lässt sich eine nützliche Hypothese von Zufall unterscheiden."], steps=["Beim ersten Vergleich Klasse, Waffe, Route und Risiko konstant halten.", "Eine Frage zu Ausrüstungseffekt, Fähigkeit oder Timing auswählen.", "Ziel, Fehlentscheidung, Erholung und Extraktion notieren.", "Dieselbe Frage erneut prüfen, bevor du von Verbesserung sprichst.", "Patch-Informationen lesen, wenn sich das System geändert hat."], links=[{"target": "beginner-guide", "label": "Den risikoarmen Lernplan über fünf Läufe nutzen"}]),
            _section("mistakes-and-limits", "Häufige Fehler und Grenzen dieses Guides", ["Verwechsle Verteidigung nicht mit Sicherheit. Eine defensive Aktion kann Bedingungen, Kosten oder eine begrenzte Dauer haben. Prüfe die Wirkung, bevor du einen langen Austausch beginnst. Staple offensive Optionen nicht, weil ein anderer Guide sie optimal nennt; teste sie, wenn du die passende Gelegenheit nicht benennen kannst. Eine Liste ohne Datum und Testbedingungen ist kein aktuelles Ranking.", "Ändere auch nicht in jedem Lauf zu viele Faktoren. Ein anderer Weg oder Mitspieler kann ein Build stärker erscheinen lassen, obwohl der Gegenstand gleich blieb. Notiere deine Läufe und verallgemeinere keinen einzelnen Erfolg. Öffentliche Informationen beschreiben Extraktion, Ausrüstung sowie Solo- und Teamspiel, aber keine geprüfte Schwert-und-Schild-Schadensformel oder dauerhaft gültige Rangfolge. Nutze die Regeln als Ausgangspunkt und aktualisiere sie mit wiederholbaren Beobachtungen."]),
        ],
        "faq_title": "FAQ zum Mistfall Hunter Schwert und Schild Build",
        "faq": [{"question": "Was ist das beste Schwert und Schild Build in Mistfall Hunter?", "answer": "Die geprüften Quellen bestätigen kein dauerhaft bestes Setup. Beginne mit verständlicher Verteidigung, einem wiederholbaren Angriffsfenster und einer Erholungsoption. Prüfe aktuelle Ausrüstung und Patch, bevor du einer undatierten Meta-Liste folgst."}, {"question": "Ist ein Söldner Schwert und Schild Build für Solo geeignet?", "answer": "Falls sich Klasse und Ausrüstung in deiner Version so kombinieren lassen, ist es ein möglicher Startpunkt. Ein Similarweb-Suchbegriff verifiziert kein aktuelles Build. Halte solo den Rückweg offen und plane Erholung ohne Teamhilfe ein."}, {"question": "Welche Werte sollte ich im Schwert und Schild Build priorisieren?", "answer": "Nutze die Wertnamen und Wirkungen deiner Spielversion. Behebe zuerst einen beobachteten Fehler und wähle dann einen Effekt für eine vorhersehbare Gelegenheit. Dieser Guide erfindet keine Namen, Schwellen oder Zahlen."}, {"question": "Funktioniert ein Schwert und Schild Build auch im Trio?", "answer": "Es kann als Anker oder für kontrollierten Druck funktionieren, wenn klar ist, wer den Rückzug ruft und die anderen Aufgaben übernimmt. Ist ein Mitspieler bereits Anker, passe die Rolle an und teste die Teamkombination im aktuellen Patch."}, {"question": "Sollte ich einen Mistfall Hunter Build-Code unverändert kopieren?", "answer": "Nur als Ausgangspunkt, wenn Quelle, Patch, Klasse und Ausrüstungsbedingungen bekannt sind. Vergleiche ihn mit deiner Version und ändere jeweils nur einen Punkt, damit die Wirkung erkennbar bleibt."}],
        "summary_heading": "Kurzfassung",
        "summary": "Behandle das Mistfall Hunter Schwert und Schild Build als rollenbasiertes Experiment. Halte einen Rückweg offen, nutze kurze Angriffsfenster, priorisiere solo den Heimweg und verteile im Trio die Aufgaben. Gegenstandswerte hängen vom Patch ab und sind hier nicht geprüft; bestätige sie im Spiel, bevor du eine Ausrüstung als optimal bezeichnest.",
        "related_title": "Den nächsten Lauf vorbereiten",
        "related_links": [{"target": "builds", "label": "Allgemeine Mistfall-Hunter-Builds vergleichen"}, {"target": "classes", "label": "Klassenrollen prüfen"}, {"target": "gameplay-guide", "label": "Gameplay und Extraktion verstehen"}, {"target": "trio-builds-guide", "label": "Trio-Zusammenstellung planen"}, {"target": "beginner-guide", "label": "Mit risikoarmen Übungen starten"}],
        "source_title": "Offizielle Quellen und Belegumfang",
        "source_note": "Offizielle Website und Steam-Seite liefern Kontext zum Spiel und seiner Ausrüstung. Die offiziellen Steam-Screenshots illustrieren nur diese allgemeinen Aspekte. Aktuelle Werte für Schwert und Schild, Fähigkeitenfolgen, Ranglisten und ein optimales Build konnten hier nicht überprüft werden; der Text enthält daher rollenbasierte Entscheidungen zum Testen im Spiel.",
        "official_links": [{"label": "Offizielle Mistfall-Hunter-Website", "url": _OFFICIAL_URL, "rel": "noopener"}, {"label": "Offizielle Steam-Seite und Bilder", "url": _STEAM_URL, "rel": "noopener"}],
    },
    "pt": {
        "slug": "mistfall-hunter-sword-and-shield-build",
        "primary_keyword": "build de espada e escudo para Mistfall Hunter",
        "related_keywords": ["build de mercenário de Mistfall Hunter", "melhor build de espada e escudo para Mistfall Hunter", "build de espada e escudo de Mistfall Hunter solo", "build de espada e escudo para trio em Mistfall Hunter"],
        "title": "Build de espada e escudo em Mistfall Hunter: 5 prioridades para solo e trio",
        "meta_title": "Build de espada e escudo em Mistfall Hunter: 5 prioridades",
        "meta_description": "Planeje um build de espada e escudo para Mistfall Hunter com prioridades de equipamento e habilidades, ajustes para solo e trio e um método de teste sem números inventados.",
        "meta_keywords": "build de espada e escudo Mistfall Hunter, build de mercenário Mistfall Hunter, build solo espada e escudo, build trio Mistfall Hunter",
        "eyebrow": "Guia de build de arma de Mistfall Hunter",
        "lede": "Espada e escudo combinam com uma abordagem que permite ler a luta, assumir compromissos curtos e manter uma rota de saída. Monte o equipamento com decisões que possam ser repetidas, não com uma classificação de dano sem verificação: tenha uma resposta defensiva, uma janela de ataque confiável e uma forma de recuperar espaço. As orientações gerais estão separadas dos valores específicos de cada atualização, que precisam de confirmação no jogo atual.",
        "checked_label": "Estrutura de build por função revisada em 24 de outubro de 2026; sem alegações de valores exatos",
        "entry_label": "Ler o guia de build de espada e escudo de Mistfall Hunter",
        "checked_iso": "2026-10-24",
        "feature_image": {"path": _FEATURE_IMAGE, "alt": "Arte conceitual editorial de um caçador com espada e escudo e o rótulo curto Sword + Shield", "caption": "Arte conceitual original criada para este guia; não é arte oficial de Mistfall Hunter nem captura do jogo.", "source_label": "Sobre este guia independente", "source_url": "/pt/about/", "width": 1024, "height": 1024},
        "facts_headers": ["Decisão de build", "Ponto de partida seguro", "Quando ajustar"],
        "facts_rows": [["Função", "Controlar espaço e preservar rota de recuo", "Um colega já ocupa a função de âncora"], ["Dano", "Usar aberturas curtas e repetíveis", "Um teste ou atualização verificada muda o ritmo"], ["Equipamento", "Manter sobrevivência e pressão", "Descrições atuais sustentam outra troca"], ["Solo", "Recolher saque enquanto a saída estiver clara", "A rota ou a recuperação deixam de ser legíveis"], ["Trio", "Combinar âncora, pressão e flexibilidade", "Alguém se separa ou as funções se sobrepõem"]],
        "intro": "Para montar um build de espada e escudo em Mistfall Hunter, comece por uma função estável em vez de procurar uma lista supostamente definitiva de melhores equipamentos. Guarde margem para se recuperar de uma troca ruim, use dano quando houver uma abertura clara e decida como sair antes de avançar. As informações públicas confirmam o ciclo geral de extração e equipamento, mas não uma combinação permanente de itens, atributos ou talentos. Trate as prioridades abaixo como hipóteses testáveis e confirme os valores exatos na versão atual do jogo.",
        "sections": [
            _section("build-goal", "O que este build de espada e escudo deve resolver", ["A pergunta útil não é se o escudo sempre supera outra arma. Pergunte se a combinação permite escolher uma troca, suportar o custo dela e voltar a uma rota segura. Armas de curto alcance incentivam confrontos longos; use o escudo para controlar quando entrar, não como prova de que todo golpe pode ser bloqueado. Comandos, regras defensivas e custos de recuperação podem mudar. Leia as descrições atuais e teste o funcionamento em vez de presumir uma regra comum a outros jogos.", "Este guia oferece uma estrutura de build orientada por funções. Ela serve a quem prefere contato controlado, quer aprender um encontro ou precisa de uma tarefa clara em um grupo pequeno. Não afirma que espada e escudo tenham o maior dano, sejam a única opção viável ou formem um meta oficial. Se a versão usa outros nomes para classes ou itens, mantenha os critérios de decisão e use os termos que aparecem na tela de equipamento."], bullets=["Mantenha recuperação ou saída antes de iniciar a luta.", "Escolha uma janela ofensiva reconhecível sem planilha de dano.", "Altere um item ou habilidade por vez para aprender com a próxima partida."], image={"path": _COMBAT_IMAGE, "alt": "Captura oficial da Steam mostrando personagem de Mistfall Hunter diante de uma grande criatura na floresta", "caption": "Imagem oficial da Steam como contexto geral de distância e combate; não mostra build testado nem valores de dano.", "source_label": "Abrir a página oficial na Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}),
            _section("five-build-priorities", "Cinco prioridades para um build mais seguro", ["As prioridades descrevem o que o equipamento deve permitir, não nomes fixos de atributos ou fórmulas ocultas. Leia as descrições atuais e escolha opções visíveis que cumpram a mesma função. Se dois bônus parecem bons, prefira aquele que consegue testar repetidamente ao que só parece forte quando analisado fora de contexto.", "A primeira tentativa deve ser simples: uma resposta de sobrevivência, um ataque repetível e flexibilidade para sair de uma sala ruim. Depois de algumas partidas, procure o momento em que o plano falhou. Se ficou seguro, mas lento, ajuste pressão. Se causou dano e perdeu a saída, trabalhe recuperação ou momento de decisão antes de aumentar o ataque."], table={"headers": ["Prioridade", "Procure", "Evite"], "rows": [["1. Defesa compreensível", "Opção com condição e custo conhecidos", "Achar que o escudo bloqueia todo dano"], ["2. Pressão repetível", "Abertura curta que você consegue criar", "Perseguir além da rota segura"], ["3. Recuperação", "Forma clara de recuperar espaço", "Gastar todas as defesas no primeiro contato"], ["4. Equipamento útil", "Bônus para problema observado", "Copiar prioridade sem ler a descrição atual"], ["5. Valor para o grupo", "Função que complementa os colegas", "Três jogadores com a mesma função"]]}, links=[{"target": "builds", "label": "Comparar esta configuração com os padrões gerais do site"}]),
            _section("gear-skills", "Escolher equipamento, habilidades e talentos pela função", ["Leia cada descrição na versão atual e pergunte qual decisão o item ou talento melhora. Um efeito defensivo só ajuda quando corrige uma falha real: ficar preso a uma troca longa, perder espaço para se reposicionar ou não ter resposta quando o encontro muda. Um efeito de dano é útil quando pode ser ativado numa abertura previsível. Se depende de uma condição rara, o valor em destaque talvez não ajude na sua partida.", "Não use a busca “build de mercenário de Mistfall Hunter com espada e escudo” como prova de que nomes, ordem de talentos ou conjunto continuam válidos. O Similarweb mostra a expressão no grupo de consultas, mas as fontes públicas verificadas não confirmam um build atual. Anote nomes, custos e condições da tela e teste uma peça antes de refazer o conjunto completo."], bullets=["A defesa deve responder a uma falha realmente observada.", "A habilidade ofensiva precisa de uma janela que possa repetir.", "Talentos complementam as condições do equipamento."], links=[{"target": "classes", "label": "Comparar funções das classes antes de escolher uma especialidade"}]),
            _section("solo-play", "Ajustar a build para jogar solo", ["No solo, a rota de volta importa tanto quanto o próximo alvo. Antes de entrar numa sala, identifique onde recuar, a saída mais clara e a opção para recuperar depois da primeira troca. Não comece uma luta só porque o escudo parece seguro. Sem uma abertura nítida, contorne a sala ou espere. Isso não garante sobrevivência; reduz decisões arriscadas tomadas sem informação.", "Depois da luta, confira seu estado, os recursos de recuperação e a clareza do caminho. Compare o saque restante com o risco de voltar. A build pode manter ataque, mas não deve depender de um colega para atrair inimigos ou cobrir a retirada. Se o plano só funciona quando o adversário fica parado ou a saída permanece livre, trate isso como condição a confirmar, não como certeza."], steps=["Antes de lutar, encontre a rota de recuo e um lugar para recuperar distância.", "Use só o ataque ou defesa que serve à abertura atual.", "Depois, confira estado, recuperação e caminho.", "Saia quando o saque restante não justificar o risco da volta."], image={"path": _EXTRACTION_IMAGE, "alt": "Captura oficial da Steam com personagem de Mistfall Hunter perto de um baú iluminado numa sala escura", "caption": "Imagem oficial da Steam para explicar a decisão de extrair com o saque; não mostra rota recomendada nem equipamento específico.", "source_label": "Abrir a página oficial na Steam", "source_url": _STEAM_URL, "width": 1200, "height": 675}, links=[{"target": "gameplay-guide", "label": "Rever o ciclo de jogo solo e extração"}]),
            _section("trio-adjustment", "Ajustar a função no trio", ["No trio, espada e escudo podem assumir a linha de frente se você preserva espaço e avisa quando recuar. É uma proposta de coordenação, não a confirmação de uma habilidade exclusiva de classe. Decidam quem chama a retirada, quem aproveita uma abertura curta e quem explora ou ajuda na recuperação. Buscar uma build de mercenário não significa avançar sozinho; os colegas precisam entender qual oportunidade você espera.", "Se outro jogador já ocupa a linha de frente, evite repetir a mesma função. Oriente o build para pressão controlada ou apoio flexível e fique perto o bastante para responder ao grupo. Se alguém se separar, reúnam-se antes da próxima luta. Esses princípios duram mais do que afirmar que uma composição é a melhor em todo mapa, atualização ou nível de habilidade."], table={"headers": ["Situação", "Função espada e escudo", "Coordenação"], "rows": [["Sala desconhecida", "Manter posição com espaço para recuperação", "Explorar um ângulo antes de avançar"], ["Abertura clara", "Concentrar ataque curto", "Chamar o alvo e parar ao fim da janela"], ["Colega isolado", "Proteger a rota de reencontro", "Pausar o avanço até reunir o grupo"], ["Saída incerta", "Não trocar retirada por dano", "Reagrupar ou sair antes de outra luta"]]}, links=[{"target": "trio-builds-guide", "label": "Distribuir funções e alternativas para o trio"}]),
            _section("repeatable-test", "Um teste curto para ajustar o build", ["Mudar classe, habilidades, equipamento, caminho e risco ao mesmo tempo não mostra o que melhorou o resultado. Mantenha a maioria das condições. Antes da partida, anote uma pergunta: a defesa permitiu reposicionar? A abertura de ataque foi repetível? A saída ainda estava acessível depois da primeira luta? Essa observação orienta o próximo teste, mas não substitui um teste controlado de dano.", "Depois, registre a decisão mais custosa, o recurso que gostaria de ter mantido e a causa da falha: luta, caminho ou separação do grupo. Mude um fator relacionado na partida seguinte. Se mudar vários, trate como experimento separado e não atribua o resultado a um item. Leia as notas de atualização quando o sistema testado mudar."], steps=["No primeiro teste, mantenha classe, arma, rota e risco.", "Escolha uma pergunta sobre equipamento, habilidade ou momento de uso.", "Registre objetivo, erro, recuperação e resultado da extração.", "Repita a pergunta antes de chamar a mudança de melhoria.", "Confira as notas quando o sistema mudar."], links=[{"target": "beginner-guide", "label": "Usar o plano de aprendizado de baixo risco em cinco partidas"}]),
            _section("mistakes-and-limits", "Erros comuns e limites deste guia", ["Não confunda defesa com segurança garantida. Uma ação pode ter condições, custo ou duração limitada; verifique antes de entrar numa troca longa. Não acumule efeitos ofensivos só porque um guia os chama de ideais. Se não consegue apontar quando ajudam, teste-os primeiro. Uma lista sem data e condições de teste não deve ser tratada como classificação atual.", "Mudar muitos fatores em cada partida também confunde os resultados. Outro caminho ou colega pode fazer o equipamento parecer mais forte sem que o item tenha mudado. Anote suas tentativas e não generalize um sucesso isolado. As fontes públicas descrevem extração, equipamento e jogo solo ou em grupo, mas não fornecem uma fórmula verificada de dano de espada e escudo nem uma classificação duradoura. Use o guia como começo e atualize-o com observações repetíveis."]),
        ],
        "faq_title": "Perguntas frequentes sobre build de espada e escudo em Mistfall Hunter",
        "faq": [{"question": "Qual é o melhor build de espada e escudo em Mistfall Hunter?", "answer": "As fontes verificadas não confirmam uma configuração sempre melhor. Comece com defesa compreensível, uma abertura repetível e recuperação. Confira equipamento e atualização antes de seguir uma lista de meta sem data."}, {"question": "O build de mercenário com espada e escudo funciona solo?", "answer": "Se classe e equipamento atuais permitem a combinação, pode ser um ponto de partida com função clara. Uma consulta do Similarweb não verifica um build atual. No solo, preserve a rota de volta e a recuperação independente da equipe."}, {"question": "Quais atributos priorizar no build de espada e escudo?", "answer": "Use os nomes e efeitos exibidos na versão atual. Corrija primeiro uma falha observada e depois escolha um efeito ofensivo para uma abertura previsível. Este guia não inventa nomes, limites ou valores."}, {"question": "O build funciona para trio?", "answer": "Pode servir como âncora ou pressão controlada se a equipe define quem chama a retirada e quem assume as demais tarefas. Se alguém já for a âncora, ajuste a função e teste a composição na atualização atual."}, {"question": "Devo copiar um código de build sem alterar nada?", "answer": "Só como referência inicial quando fonte, atualização, classe e condições de equipamento forem conhecidas. Compare com sua versão e altere um item por vez para entender o efeito."}],
        "summary_heading": "Em resumo",
        "summary": "Trate o build de espada e escudo de Mistfall Hunter como um experimento por função. Preserve a saída, aproveite janelas curtas, priorize a volta no solo e distribua tarefas no trio. Valores dos itens dependem da atualização e não foram verificados aqui; confira o jogo antes de chamar uma configuração de ideal.",
        "related_title": "Prepare a próxima partida",
        "related_links": [{"target": "builds", "label": "Comparar builds gerais de Mistfall Hunter"}, {"target": "classes", "label": "Ver funções das classes"}, {"target": "gameplay-guide", "label": "Entender jogo e extração"}, {"target": "trio-builds-guide", "label": "Planejar o trio"}, {"target": "beginner-guide", "label": "Começar por testes de baixo risco"}],
        "source_title": "Fontes oficiais e alcance das evidências",
        "source_note": "O site oficial e a página da Steam fornecem contexto sobre o jogo e o equipamento. As capturas oficiais da Steam ilustram apenas esse contexto. Valores atuais de espada e escudo, rotações, classificações e build ideal não puderam ser verificados; o texto apresenta decisões por função para testar no jogo.",
        "official_links": [{"label": "Site oficial de Mistfall Hunter", "url": _OFFICIAL_URL, "rel": "noopener"}, {"label": "Página e imagens oficiais na Steam", "url": _STEAM_URL, "rel": "noopener"}],
    },
}

from sword_shield_guide_locales import SWORD_SHIELD_LOCALIZED

SWORD_SHIELD_GUIDES.update(SWORD_SHIELD_LOCALIZED)


def _replace_page_copy(value: Any, replacements: Dict[str, str]) -> Any:
    """
    递归替换本地化文章数据中的指定词项。

    :param value: 当前文章字段、列表或映射
    :param replacements: 旧词项到本地化新词项的映射
    :return: Any，替换后的文章数据
    """
    if isinstance(value, str):
        for original, localized in replacements.items():
            value = value.replace(original, localized)
        return value
    if isinstance(value, list):
        return [_replace_page_copy(item, replacements) for item in value]
    if isinstance(value, dict):
        stable_fields = {"target", "slug", "path", "source_url", "url", "id", "checked_iso"}
        return {
            key: item if key in stable_fields else _replace_page_copy(item, replacements)
            for key, item in value.items()
        }
    return value


_PAGE_TERM_REPLACEMENTS = {
    "es": {"error, la recuperación": "fallo, la recuperación", "primer error es": "primer fallo es", "otro error es": "otro fallo es", "cuarto error es": "cuarto fallo es", "el rótulo breve Sword + Shield": "el rótulo breve en inglés"},
    "ja": {"FAQ": "よくある質問", "Sword + Shieldと表示": "英語の短いラベルを表示"},
    "fr": {"Guide de build d'arme": "Conseils de build d'arme", "guide": "article", "Guide": "Conseils", "FAQ": "Questions fréquentes"},
    "de": {"diesen Guide": "diesen Ratgeber", "dieses Guides": "dieses Ratgebers", "anderer Guide": "anderer Ratgeber", "Guide": "Ratgeber", "FAQ": "Häufige Fragen", "dem kurzen Schriftzug Sword + Shield": "dem kurzen englischen Schriftzug"},
    "pt": {"o rótulo curto Sword + Shield": "um rótulo curto em inglês"},
    "ko": {"FAQ": "자주 묻는 질문", "짧은 Sword + Shield 문구": "짧은 영어 문구"},
    "it": {"FAQ": "Domande frequenti", "la breve scritta Sword + Shield": "la breve scritta in inglese"},
}
for _locale, _replacements in _PAGE_TERM_REPLACEMENTS.items():
    SWORD_SHIELD_GUIDES[_locale] = _replace_page_copy(SWORD_SHIELD_GUIDES[_locale], _replacements)
