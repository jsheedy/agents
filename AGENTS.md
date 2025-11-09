## agents — purpose and how to use this repo

This repository is a workspace for authoring lightweight "agent" projects (prompts, small pipelines, media generators, etc.).

This directory will be used to develop projects for Velotron Heavy Industries, including:
- Videos
- Music
- Essays# Agents

This document contains information about the agents in this workspace.

## Agent Configuration

### Development Commands
- **Lint**: `npm run lint` (if available)
- **Type Check**: `npm run typecheck` (if available)
- **Test**: `npm test` (if available)

### Agent Guidelines
- Follow existing code conventions and patterns
- Use established libraries and frameworks already present in the codebase
- Maintain security best practices
- Never commit secrets or sensitive information

## Project Structure
```
agents/
├── README.md          # Project overview
├── AGENTS.md          # This file - agent documentation
```

## Notes
This is a working space for all agents. Update this file as new agents and configurations are added.
=======
Current state
- `AGENTS.md`: this file (index and guidance)
- `templates/`: starter files and minimal project templates (README, agent_spec, project.json, LICENSE, .gitignore)

When to add a new project
- Create a new folder under `projects/<project-name>/` (or `projects/` if you prefer flat listing).
- Populate `project.json` with minimal metadata and add an `agent_spec.md` describing goals and prompts.

Recommended project scaffold

- projects/<project-name>/
	- README.md            # human-friendly overview and quick start
	- agent_spec.md        # goals, prompts, data sources, tests
	- project.json         # metadata (name, owner, license, type)
	- src/                 # optional code
	- assets/              # images, audio, examples
	- LICENSE
	- .gitignore

Templates
- See `templates/` for starter files you can copy into new projects.

Quick start
1. Copy `templates/project.json` into `projects/<project-name>/project.json` and update fields.
2. Edit `projects/<project-name>/agent_spec.md` to describe the agent's goals, prompts, inputs, and constraints.
3. Add source code to `src/` and assets to `assets/` as needed.

Example metadata (project.json keys)
- name, description, owner, created, license (SPDX), type (video|music|essay|agent|tool), entry (agent_spec.md)

## Inspiration and Style

### Coding Projects

The owner's past projects show a strong focus on Python, C++, and JavaScript, with many repositories related to DIY electronics, graphics, and data science. Key themes include:
- **Rendering and Graphics:** `PUNYTY` (Python rendering engine), `tinyraytracer`, `CUBE-GL`.
- **DIY Electronics & LEDs:** `MATRIX-DISPLAY`, `BIOFEEDBACK-CUBE`, `DOTSTAR`, `neopixel-framebuffer`.
- **Data Science & AI:** `XION` (AI), `dask-sql`, `zarr-python`.
- **Audio/Music:** `python-osc`.

### Music Style: "Lecture Wave"

The "Lecture Wave" style, as seen on the Velotron SoundCloud, is characterized by:
- **Thematic Focus:** Human technological singularity, science, technology, and evolution.
- **Sonic Characteristics:** Glitching, processing of acoustic instruments (like saxophones) to create an "uncanny valley" effect, blurring the lines between synthetic and analog sounds. This suggests a style that is intellectually driven, exploring futuristic and scientific themes through experimental and boundary-pushing sound design.

The overall goal is to "go singularity," suggesting an ambition to create highly advanced, self-improving, and impactful projects.

If you'd like, I can create an example project in `projects/` next (e.g., `projects/velotron-video`) using the templates.
