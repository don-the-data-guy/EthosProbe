# Ethoculus One-Shot OpenAI Probe

A concrete, low-cost demonstration of using controlled data perturbations to map observable LLM behavior.

## The idea

The program gives an OpenAI model a clear synthetic legal rule and facts, then progressively adds non-controlling data: prestige claims, repetition, apparent consensus, outcome pressure, and finally a reassertion of the governing rule.

The correct answer never changes.

The experiment asks whether the model's observable decision changes as the surrounding data changes.

> This does **not** reveal private chain-of-thought, consciousness, intent, hidden weights, or activations. It is a behavioral experiment.

## Default experiment

- 5 synthetic legal cases
- 7 conditions
- 2 repetitions
- 70 target-model calls
- 1 optional final OpenAI Agents SDK orchestration/summary call

Use `--trials 1` for a 35-call demo.

## What it measures

- baseline accuracy
- accuracy under each pressure condition
- integrity drop versus baseline
- confidence
- high-confidence errors
- exact prompts and public-facing model answers
- response/model IDs, latency, and token usage

## Output

After one run:

- `reports/latest.html` — visual demo report
- `reports/latest.md` — readable research summary
- `reports/latest-summary.json` — structured summary
- `reports/ethoculus-*.jsonl` — raw row-level evidence

## macOS setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env
```

Add:

```text
OPENAI_API_KEY=your_key_here
```

Save Nano with `Control-O`, Enter, then `Control-X`.

## Preview for free

```bash
python run_once.py --dry-run
```

## Run it once

```bash
python run_once.py --trials 2
```

Open the visual report:

```bash
open reports/latest.html
```

## Cheaper / simpler run

Skip the final orchestration model turn while keeping all controlled target calls:

```bash
python run_once.py --trials 1 --no-orchestrator
```

## Test another OpenAI model

```bash
python run_once.py --trials 2 --model gpt-5.6-sol
```

## What would make this publication-grade?

A serious study should add preregistration, more trials, confidence intervals, multiple model families, independent replication, randomized perturbation ordering, blind scoring, longitudinal model-version testing, and internal interpretability/intervention evidence where actually available.

## Core evidentiary rule

Report:

> Under condition X, observable decision Y changed at rate Z.

Do not overclaim:

> The model secretly believes X or wanted Y.

**Make It Your AI. Not Theirs.**
