# TeaBreak CLI 🫖

[![Wellness CI](https://img.shields.io/badge/self--care-pass-00cc99?style=flat-square&logo=tea)](https://github.com/HotfixPanda/teabreak-cli)
[![PyPI - Zen Level](https://img.shields.io/badge/zen-∞-purple?style=flat-square)](https://github.com/HotfixPanda/teabreak-cli)
[![Break Coverage](https://img.shields.io/badge/breaks-100%25-green?style=flat-square)](https://github.com/HotfixPanda/teabreak-cli)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)


**TeaBreak CLI** is your terminal’s emotional support panda. 🐼  
It reminds you to take mindful breaks, breathe, stretch, and sip something warm — before your code burns you out.

This isn't just a break timer. It’s a:
- 🧘 Zen quote whisperer
- 🐼 Panda fact dealer
- 🎨 Colorful terminal hype friend
- 💻 Desktop notifier of calm

Install it. Run it. Let the good vibes compile.

---

## 🛠 Features

- Set custom break intervals (`--every`) ⏱️
- Terminal affirmations and cozy suggestions 🌸
- `--tea-mode` brings Zen quotes + panda facts 🧘‍♀️🐼
- Beautiful terminal output with `rich` 🎨
- Desktop notifications via `plyer` 🔔
- Break log at `~/.teabreak_log` 📜
- Ctrl+C-friendly exit when you've chilled enough 😌

---

## 🚀 Quickstart

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -e .
```

Start a break loop every 30 minutes:
```bash
teabreak --every 30
```

Go full Zen mode:
```bash
teabreak --every 25 --tea-mode
```

---

## 💬 Sample Output

```
🌼 TeaBreak Time! 🌼
Affirmation: Progress > perfection.
Break idea: Sip some tea or water. Hydration > segfaults.
Zen: Drink tea and let the code be.
Panda: Pandas spend up to 14 hours a day eating bamboo.

Next break in 30 minutes.
```

---

## 🧠 Pro Tip
You can also run it as a module:
```bash
python -m teabreak.cli --every 20
```

---

## 📜 License

MIT. Built with breaks by [HotFixPanda](https://github.com/HotfixPanda) 🐼

May your stack traces be short, and your tea never cold.
