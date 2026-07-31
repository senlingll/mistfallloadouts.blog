(function () {
  const form = document.querySelector("[data-planner]");
  if (!form) return;

  const copyButton = form.querySelector("[data-copy]");
  const copyLabel = copyButton?.dataset.copyLabel || "Copy";
  const copiedLabel = copyButton?.dataset.copiedLabel || "Copied";
  const i18nNode = document.getElementById("planner-i18n");
  const fallbackI18n = {
    classNotes: {
      vanguard: ["", "", ""],
      seeker: ["", "", ""],
      arcanist: ["", "", ""],
      warden: ["", "", ""],
    },
    roles: { solo: "", team: "", boss: "" },
    risks: { safe: "", balanced: "", greedy: "" },
    weapons: { melee: "", ranged: "", hybrid: "" },
    phases: { early: "", mid: "", late: "" },
    summary: "{className} {role} {weapon} {risk}",
    stats: "{strength} {phase}",
    route: "{watch}",
    tip: "",
    copyUnavailable: "",
  };
  const i18n = (() => {
    try {
      return i18nNode ? { ...fallbackI18n, ...JSON.parse(i18nNode.textContent) } : fallbackI18n;
    } catch (error) {
      return fallbackI18n;
    }
  })();
  const output = {
    summary: document.querySelector("[data-summary]"),
    tags: document.querySelector("[data-tags]"),
    stats: document.querySelector("[data-stats]"),
    route: document.querySelector("[data-route]"),
    tip: document.querySelector("[data-tip]"),
  };

  function value(name) {
    return new FormData(form).get(name);
  }

  function fill(template, values) {
    return template.replace(/\{(\w+)\}/g, (_, key) => values[key] || "");
  }

  function render() {
    const classFocus = value("classFocus");
    const role = value("role");
    const risk = value("risk");
    const weapon = value("weapon");
    const phase = value("phase");
    const notes = i18n.classNotes[classFocus] || fallbackI18n.classNotes[classFocus];
    const values = {
      className: notes[0],
      strength: notes[1],
      watch: notes[2],
      role: i18n.roles[role],
      risk: i18n.risks[risk],
      weapon: i18n.weapons[weapon],
      phase: i18n.phases[phase],
    };

    output.summary.textContent = fill(i18n.summary, values);
    output.tags.textContent = [values.className, values.role, values.risk, values.weapon, values.phase].join(", ");
    output.stats.textContent = fill(i18n.stats, values);
    output.route.textContent = fill(i18n.route, values);
    output.tip.textContent = i18n.tip;
  }

  form.addEventListener("change", render);
  form.addEventListener("reset", () => setTimeout(render, 0));
  copyButton?.addEventListener("click", async () => {
    const text = [output.summary.textContent, output.tags.textContent, output.stats.textContent, output.route.textContent].join("\n");
    try {
      await navigator.clipboard.writeText(text);
      copyButton.textContent = copiedLabel;
      setTimeout(() => { copyButton.textContent = copyLabel; }, 1200);
    } catch (error) {
      output.tip.textContent = `${output.tip.textContent} ${i18n.copyUnavailable}`;
    }
  });
  render();
})();
