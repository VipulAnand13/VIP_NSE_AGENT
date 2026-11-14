#!/usr/bin/env python3
"""Run from your trading folder after a scan: python3 export_charts.py
Reads trader/watchlist.json, fetches 6 months of daily candles (Yahoo, free) for each
hit and writes trader/charts.json, which the NSE Trader Desk dashboard loads."""
import json, sys, time, urllib.parse, urllib.request

W = json.load(open("trader/watchlist.json"))
syms = [h["symbol"] for h in W.get("hits", [])]
out = {}
for s in syms:
    ys = s if s.endswith((".NS", ".BO")) else s + ".NS"
    url = "https://query2.finance.yahoo.com/v8/finance/chart/%s?range=6mo&interval=1d" % urllib.parse.quote(ys)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        r = json.load(urllib.request.urlopen(req, timeout=20))["chart"]["result"][0]
        q = r["indicators"]["quote"][0]
        rows = [i for i, c in enumerate(q["close"]) if None not in (q["open"][i], q["high"][i], q["low"][i], c)]
        out[s] = {"t": [r["timestamp"][i] for i in rows], **{k: [q[n][i] or 0 for i in rows] for k, n in
                  (("o", "open"), ("h", "high"), ("l", "low"), ("c", "close"), ("v", "volume"))}}
        print("ok  ", s, len(rows), "candles")
    except Exception as e:
        print("skip", s, e)
    time.sleep(0.4)
json.dump(out, open("trader/charts.json", "w"))
print("Wrote trader/charts.json with", len(out), "of", len(syms), "stocks")
