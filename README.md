## Strands Agents (Personal Study Project)

A small sandbox to learn and experiment with building tool-using agents with `strands-agents`.

### Repo layout
- `my_agent/`: the quick start example from the strands-agents documentation
- `countries/`: agent that calls a public REST API to fetch country data

### Prerequisites
- Python 3.10+ (macOS: `python3 --version`)

### Quick start

Run the simple `my_agent` example:

```bash
cd my_agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python agent.py
```

Run the `countries` example:

```bash
cd countries
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python agent.py
```

### Upgrading dependencies
From within either example directory:

```bash
pip install -U -r requirements.txt
```

### Notes
- Virtual environments are per example folder above for isolation. Use `deactivate` to exit.

### Why this project exists
This is purely for personal study—quick, isolated examples I can iterate on as I learn.


