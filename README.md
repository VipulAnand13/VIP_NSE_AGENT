# VIP NSE Agent

A free, self-updating dashboard for NSE day-trading research. Every weekday at 17:00 IST a GitHub Action
scans the Nifty 200, saves the results, and the page in `docs/` shows them with annotated candlestick charts.
Research and testing only. It places no orders. Most people who day trade lose money. Not financial advice.

**This repository is public.** It holds market scan results and code only. Never add your budget, account,
broker keys or personal numbers here.

## One-time setup
1. Settings > Pages: Source "Deploy from a branch", branch `main`, folder `/docs`. Save.
2. Settings > Actions > General > Workflow permissions: "Read and write permissions". Save.
3. Optional but recommended: add your `trader/universe.txt` (made by `scan.py universe`) as `data/universe.txt`,
   because NSE sometimes blocks downloads from GitHub's servers.
4. Actions tab > "Daily NSE scan" > Run workflow. After about 3 minutes the page is at
   https://vipulanand13.github.io/VIP_NSE_AGENT/

## Folders
- `skills/` the eight Claude skills (scanner, entry, exit, timemachine, budget, risk, alerts, news) and their scripts
- `docs/` the dashboard (`index.html`) and the latest scan results (`docs/data/`)
- `export_charts.py` turns a watchlist into candle data for the charts
- `.github/workflows/daily-scan.yml` the schedule

Prices come from Yahoo Finance (free, can lag). The 2026 NSE holiday list is from public sources: verify it.
