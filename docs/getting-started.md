# Getting Started

This short guide helps you preview and publish the docs.

## Prerequisites

- Python 3.8+
- pip (or pipx)

## Install locally

```bash
# (optional) create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Upgrade pip and install mkdocs-material
python -m pip install --upgrade pip
pip install mkdocs-material
```

## Run locally

```bash
mkdocs serve
```

Open http://127.0.0.1:8000 to preview. Edits in the docs/ folder hot-reload.

## Deploy with GitHub Pages

A workflow is set up to build and deploy on every push to `main`.

One-time in GitHub (repository Settings → Pages):
- Set Source to "GitHub Actions".

Then push changes to `docs/` or `mkdocs.yml` on `main`. The site will publish automatically.