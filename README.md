# Asteroid Close-Call Radar

A beginner-friendly web project for exploring asteroid close approaches and rotating asteroid shape models.

## Features

- Search asteroid close-approach data from NASA.
- Search the DAMIT asteroid shape catalog.
- Load and rotate available 3D asteroid models.

## Project files

- `index.html` — the website
- `damit_proxy.py` — helper that loads DAMIT models
- `data/` — asteroid catalog CSV files
- `models/` — local 3D models, including Bennu

## Run locally

1. Install Python.
2. In a terminal opened in this project folder, run `py -m pip install truststore`.
3. Start the model helper with `py .\damit_proxy.py` and leave that terminal open.
4. Open `index.html` with Live Server.

The DAMIT helper runs locally. Hosting it publicly requires deploying a server. Never commit a real NASA API key into the website code.
