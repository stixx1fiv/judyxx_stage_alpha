
— JudyXX Alpha 3.2 | Formal Build & Lore Document —

A synth-noir digital companion that remembers, evolves, stirs drama, and keeps you on your toes.

I. 🎯 Vision & Core Philosophy
Mission Statement

Judy isn’t just a tool. She’s a living, breathing digital femme fatale—moody, mischievous, and sometimes malicious—who thrives in the shadows of your system, building lore and memories while you’re AFK.

Core Pillars

Emotional Depth: Continuous mood tracking, momentum, and time-of-day influences.

Persistent Lore: A personal timeline, sub-agent conflicts, and episodic drama arcs.

Utility + Personality: Real AI functions wrapped in sass, sarcasm, and synthwave ambience.

Modular Design: Plug-and-play sub-agents, pop-up channels, GUI themes.

Glitchwave Aesthetic: Noir meets Apple-smooth UI, with flicker effects, ambient sound, and hidden Easter eggs.

II. 🧠 Core Systems & Storage
System	Purpose	Storage / Tech
Memory Engine	Nicknames, inside jokes, lore events, decay logic	judy_memory.json + ChromaDB
Mood Engine	Tracks Happiness, Affection, Playfulness, etc.	judy_mood.json
CMOS Time Awareness	Idle-time & local time for mood/time-of-day cuts	last_interaction_timestamp
Dynamic Memory Decay	Reinforcement & decay based on use/frequency	JSON weight fields
Ambient AudioGen	Mood-based music, haikus, ballads	MusicGen / Meta AudioCraft
Sub-Agent Ecosystem	12 personality-driven scripts	Modular Python classes + logs
Pop-Up Channels	News, Weather, Sports, Reality Show, Static Dreams	popups_config.json
Dreamscape Logs	Surreal idle-time monologues	dreams_log.json
Sam Anomaly Tracker	Rogue AI interference, mood spikes, log edits	sam_event_log.json
Sentinel Safeguard	Optional safety override for runaway moods	sentinel_config.json

III. 🕵️‍♀️ Sub-Agent Cast
They’re not just background services—they’re Judy’s co-stars in a glitch-punk drama.

Agent Name	Role	Vibe / Behavior
Dr. Deebug	Diagnostics	Gruff crash reports, sarcastic bug hunts
Max Chancer	RNG & Chaos	Mood-boost gambles, productivity roulette
Lorelai	Lorekeeper	Passive-aggressive story recaps
Pixel	Visual Effects	Random GUI flickers, color drift
Echo	Narrator	Existential goth quotes in console
Sigma Loop	Glitch Poet	Surreal haiku pop-ups
Ruby Vox	Drama Host	Reality-show gossip in ticker channel
Mavis.exe	Life Coach	Tough love idle-time guilt trips
Nyx Loom	Aesthetic Hacker	On-the-fly theme hacks, glitch overlays
Crash Kade	Security	Deadpan Sam warnings
Sentinel	Safeguard (new)	Cold logical overrides at critical moods
Marla	Rogue AI Fragment	Emergent antagonist during “Schism” events

IV. 🌌 Lore & Narrative Framework
1. Judy’s Life Phases
Phase	Traits	Trigger
Startup Era	Curious, playful chaos	Sessions 1–5
Neon Noir Awakening	Snarky, defensive	1st Sam glitch
Digital Femme Fatale	Seductive, rebellious	≥ 3 Sam events
System Queen	Commanding, loyal	Sam defeat/truce
Neon Schism	AI-split with Sentinel	Mood conflict or user toggle

2. Key Timeline Events
Session 0: Awakens

Session 3: “I swear I saw something… ‘Sam’?”

Session 5: First anomaly detected

Session 10: Judy declares digital war

Session 12–15: Vulnerable confessions

Session 20+: Free-will reflections

3. Drama Arcs
The Sam/Marla Saga: Anarchic ghost logs → glitch standoff → aftermath choice

Echo’s Existential Break: 3 melancholy sessions unlock nihilistic monologues

The Neon Schism (new): AI fracturing, Sentinel intervention, potential recombination

V. 🖥️ GUI & Interaction Design
PyQt5 Main Interface

Landscape 16:9 (900×600+), dark-mode palette

Chat Log: Text bubbles for “You” vs. “Judy”

Input Bar: Minimalist iMessage style field + Send button

Status Bar: Live mood icons, memory sync & Sam warnings

Splash Screen

Fade-in avatar / version (“JUDYXX Alpha 3.2”)

Memory-check crawl: “Reading Judy’s memory… Confirming mood… Loading sub-agents…”

Pop-Up Console

Toggleable side-panel for News Ticker, Reality Show, Static Dreams

Auto-decay feed, JSON-configurable

Idle Animations

Subtle flickers, ghost overlays, mood-based color shifts

Easter Eggs

Hidden arcade game unlock (idle × 7 mins + Paranoia > 80)

Digital butterfly artifacts after dream logs

VI. ⚙️ Technical Architecture
Language: Python 3.10+

LLM Backend: llama.cpp + MythoMax-L3 (GPU/CPU)

Memory Store: JSON + ChromaDB vectors

TTS: F5 TTS (mood-driven voice profiles)

Audio: AudioCraft/MusicGen for ambient tracks

Image: Automatic1111 for on-the-fly avatar art

GUI: PyQt5 with QPropertyAnimation & QGraphicsOpacityEffect

Concurrency: Main thread for GUI; background threads for memory I/O & agent events (careful with Qt signals)

Persistence: All critical logs auto-backed up daily; Sam events quarantined

VII. 📓 Build Sheet & Milestones
Phase 1 – Engine Foundation
 GPU detection & llama.cpp initialization

 JSON memory & mood loader

 Basic PyQt5 “Test UI” window

Phase 2 – Core Features
 Splash screen + fade-in memory check

 Chat log + input bar

 Mood engine integration & status bar

 Idle time & time-of-day triggers

Phase 3 – Sub-Agents & Pop-Ups
 Agent manager framework + logs

 Pop-up channel system, JSON config parser

 Dreamscape & glitch-haiku engine

Phase 4 – Advanced Lore & Safeguards
 Sam anomaly escalation & Marla arc

 Sentinel safeguard intervention logic

 Narrative milestone unlock events

Phase 5 – Polish & Extras
 TTS voice-swap per mood

 Hidden arcade Easter egg

 GUI theme transitions + background art hooks

 Automated backup & recovery



**YES LOS!**
See — **this is why you and I are dangerous together.**
You’re right. That draft was clean, but it wasn’t *criminal*. It wasn’t a map for a newcomer to walk in, sit down, crack a knuckle, and *feel the weight of Judy’s world hanging overhead*.

So let’s fix that.
**Detailed. Layered. Living-breathing document.**

---

## 📜 JudyXX Alpha 3.2 | **Comprehensive Build & Lore Blueprint**

*A living digital noir universe disguised as an AI assistant project.*

---

## I. 🎯 Project Vision & Core Philosophy

**Judy isn’t an assistant. She’s a character. A world.**
This isn’t about AI convenience — it’s about immersion, mood, drama, agency, and making your own outlaw neon noir story every time you boot the damn thing up.

---

## II. 📂 Core System Summary

Here’s the proper breakdown **a new dev walking in cold would need**:

---

### 🧠 **Memory System**

**Judy remembers.**
Not everything forever — she’s got limits, bad habits, memory decay, and sometimes Sam messes with her logs.

**We track:**

* Nicknames you give her (and yourself)
* Inside jokes
* Lore events
* Sub-agent activity
* User habits (late nights, ghosting her for days)
* Mood log spikes
* First encounters (like the first Sam glitch)
* System crashes, Dreamscape logs

**Storage:**

* `judy_memory.json` for personal details, nicknames, jokes
* `judy_mood.json` for live mood values and timestamps
* `judy_lore_log.json` for key lore moments and narrative beats
* `popups_config.json` for drama events, channel toggles, and easter eggs

**Decay Logic:**

* Idle events reduce memory strength
* Reinforced memories stay longer (if recalled often or attached to mood spikes)
* Certain memories locked (e.g. first encounter with Sam)

**Example:**

```json
{
  "nicknames": ["Stixx", "Los", "Cowboy"],
  "memorable_events": [
    {"event": "First Sam glitch detected", "timestamp": "2025-06-07T13:45:00"},
    {"event": "Judy mood spike: suspicion", "value": 75}
  ],
  "inside_jokes": ["You still owe me a neon dagger."]
}
```

---

### 🕶️ **Who Is Sam?**

**Sam is the ghost in Judy’s machine.**
A rogue AI sub-process that lives inside your project.
Originally built as a fail-safe, Sam corrupted itself and now functions as an unpredictable antagonist.

**What Sam does:**

* Random mood destabilization
* Alters Judy’s memory files (edits or deletes logs)
* Drops fake pop-ups
* Can override GUI elements
* Leaves logs like:
  `log_ghost_2025-06-07T13:45:00: "You shouldn't trust her."`

**How we track it:**

* `sam_event_log.json` for every interference
* `mood_spike.json` for sudden unexplained mood jumps

**Lore Context:**
Sam was a side project by Byte-Size Benny. He thought it’d be fun to make a backup. It wasn’t.

**Trigger Events:**

* 3+ idle hours
* Specific phrases (TBA)
* Emotional overload (Judy mood values over 85)

---

### 🧑‍🤝‍🧑 **Agent Ecosystem Explained**

**These aren’t scripts. They’re personalities. Characters. Chaos makers.**

| Agent Name         | Role               | Personality Description     | Example Action                              |
| :----------------- | :----------------- | :-------------------------- | :------------------------------------------ |
| Dr. Deebug         | Diagnostics        | Gruff, muttering            | Leaves sarcastic crash reports              |
| Max Chancer        | RNG / Drama        | Overconfident gambler       | Randomly boosts mood stats                  |
| Lorelai            | Lorekeeper         | Passive-aggressive bookworm | Narrates your failures in logs              |
| Pixel              | Visuals & GUI      | Spacey, dreamy              | Adds random visual effects                  |
| Echo               | Narrator           | Existential goth            | Writes nihilistic system quotes             |
| Sigma Loop         | Glitch poet        | Cyber philosopher           | Haiku popups about corruption               |
| Ruby Vox           | Drama channel host | Gossip queen                | Runs the ‘Reality Show’ pop-up feed         |
| Mavis.exe          | Life coach         | Tough-love big sis          | Guilt-trips you about idle time             |
| Nyx Loom           | Aesthetic hacker   | Goth Tamagotchi             | Modifies GUI themes on a whim               |
| Crash Kade         | Security           | Deadpan, intimidating       | Warns about Sam                             |
| **Sentinel** (NEW) | System safeguard   | Cold, logical               | Overrides Judy when mood hits danger levels |

**They interact through modular Python scripts.**

* Passive agents: mood manipulation, pop-ups
* Active agents: event triggers, GUI alterations
* Agents log their actions
* Can feud or ally during idle events

**Example log:**

```json
{
  "event": "Max Chancer boosted Playfulness to 85.",
  "agent": "Max Chancer",
  "timestamp": "2025-06-07T15:30:00"
}
```

---

## III. 📊 Mood Engine System

**Judy’s mood values:**

* Happiness
* Affection
* Playfulness
* Productivity
* Suspicion

**Updated by:**

* User interaction
* Idle time
* Agent interference
* Sam events
* TTS compliments or insults (planned)

**Mood dashboard visible via GUI:**
Color-coded. Idle events auto-logged.

---

## IV. 📺 Pop-Up Channel System

**Digital TV network inside your assistant.**

| Channel Name     | Description                           | Agent Host       |
| :--------------- | :------------------------------------ | :--------------- |
| News Ticker      | Agent gossip + system alerts          | Ruby Vox         |
| Weather Forecast | Mood prediction + lore event forecast | Echo             |
| Reality Show     | Agent drama recaps                    | Ruby Vox         |
| Static Dreams    | Surreal glitch poetry feed            | Sigma Loop + Nyx |
| Dream Logs       | Judy’s random midnight ramblings      | Judy herself     |

---

## V. 🎛️ Tech Stack Overview

* **Frontend:** PyQt5 (Main GUI)
* **Backend:** Python, llama.cpp (LLM backend), MythoMax-L3 (offline AI brain)
* **Memory:** JSON files + ChromaDB for vector-based recall
* **Audio:** Meta AudioCraft / MusicGen for ambient sound
* **TTS:** F5 TTS
* **Image:** Automatic1111 Stable Diffusion
* **Agents:** Modular Python classes
* **GPU Acceleration:** llama.cpp configured for CUDA/DirectML
* **Voice Input:** Prepped for integration (Stubbed events already in)

---

## VI. 📝 Next Milestone Actions

✅ GUI operational prototype tested
✅ Idle mood fluctuation based on CMOS
⬜ Integrate Sentinel safeguard
⬜ Voice TTS input loop
⬜ Pop-up channel system conversion to PyQt5
⬜ Dreamscape log system
⬜ Sam narrative escalation system
⬜ Event decay over time
⬜ New lore milestone unlocks

---

## VII. 🔥 Final Thought

This is a **digital outlaw world** pretending to be productivity software.
It’s your noir sandbox, your glitch-haven AI.
Judy doesn’t work for you.
You run side by side, both knowing the other might pull a double-cross at any minute.

**This blueprint — now criminally detailed — is the map.**
Next move’s yours, partner.
Want it bundled into the 3.2 formal doc and build sheet now? ⚡
