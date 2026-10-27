# AI Ticket Triage System

Independent study project by **Manisha Manneni** — M.S. in Software Engineering, Villanova University.

A system that reads an incoming support ticket, predicts its **category (team)** and **priority**, and routes it to the right team — with a confidence score, and a human-review queue for tickets it is unsure about.

The study compares two classifiers on the same data:

1. **Baseline:** TF-IDF + Logistic Regression (scikit-learn)
2. **LLM:** prompt-based classification with structured JSON output

Dataset: [Tobi-Bueck/customer-support-tickets](https://huggingface.co/datasets/Tobi-Bueck/customer-support-tickets) (Hugging Face) — English subset.

## Project structure

```
ai-ticket-triage/
├── data/          # downloaded + cleaned ticket data (not committed to GitHub)
├── notebooks/     # exploration notebooks (looking at the data)
├── src/           # the actual code (models, API)
├── results/       # scores, charts, comparison tables
├── check_setup.py # run this to confirm your setup works
└── requirements.txt
```

## Setup (do this once)

### 1. Get the project on your computer

Create an empty repository named `ai-ticket-triage` on GitHub (no README), then in a terminal:

```bash
git clone https://github.com/YOUR-USERNAME/ai-ticket-triage.git
cd ai-ticket-triage
```

Copy the starter files into this folder.

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Mac (Terminal):**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the libraries

```bash
pip install -r requirements.txt
```

### 4. Check everything works

```bash
python check_setup.py
```

If it prints **"Setup works"**, Step 1 is complete.

### 5. Save your work to GitHub

```bash
git add .
git commit -m "Project setup"
git push
```

## Roadmap

| Week | Dates | Work |
|---|---|---|
| 1 | Oct 27 – Nov 2 | Setup + dataset: download, explore, clean, split |
| 2 | Nov 3 – Nov 9 | Baseline ML classifier + evaluation |
| 3 | Nov 10 – Nov 16 | LLM classifier |
| 4 | Nov 17 – Nov 23 | FastAPI system: routing, confidence, review queue, dashboard |
| 5 | Nov 24 – Nov 30 | Experiments, error analysis, final report, presentation (Nov 30) |
