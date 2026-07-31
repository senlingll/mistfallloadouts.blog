(function () {
  const form = document.querySelector("[data-planner]");
  if (!form) return;

  const copyButton = form.querySelector("[data-copy]");
  const output = {
    summary: document.querySelector("[data-summary]"),
    tags: document.querySelector("[data-tags]"),
    stats: document.querySelector("[data-stats]"),
    route: document.querySelector("[data-route]"),
    tip: document.querySelector("[data-tip]"),
  };

  const classNotes = {
    vanguard: ["Anchor the fight", "guard a reset lane", "armor uptime, stagger control, sustain"],
    seeker: ["Scout first, fight second", "mark exit choices early", "mobility, detection, disengage"],
    arcanist: ["Build around burst windows", "avoid long messy trades", "cooldown uptime, burst timing, recovery"],
    warden: ["Keep the run stable", "cover mistakes and revive windows", "support utility, durability, team recovery"],
  };

  function value(name) {
    return new FormData(form).get(name);
  }

  function render() {
    const classFocus = value("classFocus");
    const role = value("role");
    const risk = value("risk");
    const weapon = value("weapon");
    const phase = value("phase");
    const notes = classNotes[classFocus];
    const roleText = {
      solo: "solo extraction",
      team: "team support",
      boss: "boss pressure",
    }[role];
    const riskText = {
      safe: "safe exits before extra loot",
      balanced: "one objective, one backup exit",
      greedy: "high-value fights only after scouting an escape",
    }[risk];
    const weaponText = {
      melee: "melee control with a ranged answer",
      ranged: "ranged pressure with a close-range panic tool",
      hybrid: "hybrid pressure so you are not locked into one range",
    }[weapon];
    const phaseText = {
      early: "early-game reliability",
      mid: "mid-game flexibility",
      late: "late-game specialization",
    }[phase];

    output.summary.textContent = `${notes[0]} for ${roleText}: choose ${weaponText} and plan around ${riskText}.`;
    output.tags.textContent = `${classFocus}, ${role}, ${risk}, ${weapon}, ${phase}`;
    output.stats.textContent = `${notes[2]}; favor ${phaseText} over untested maximum damage.`;
    output.route.textContent = notes[1];
    output.tip.textContent = "If a new patch changes class values, keep the same role logic and update the exact gear choices after reliable tests appear.";
  }

  form.addEventListener("change", render);
  form.addEventListener("reset", () => setTimeout(render, 0));
  copyButton.addEventListener("click", async () => {
    const text = [output.summary.textContent, output.tags.textContent, output.stats.textContent, output.route.textContent].join("\n");
    try {
      await navigator.clipboard.writeText(text);
      copyButton.textContent = "Copied";
      setTimeout(() => { copyButton.textContent = "Copy"; }, 1200);
    } catch (error) {
      output.tip.textContent = `${output.tip.textContent} Copy is unavailable in this browser.`;
    }
  });
  render();
})();
