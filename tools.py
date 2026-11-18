"""Deterministic tools used by the researcher agent."""

import math

CITIES = {"delhi": (28.61, 77.21), "jaipur": (26.91, 75.79), "agra": (27.18, 78.01), "chandigarh": (30.73, 76.78)}


def distance_km(a: str, b: str) -> float:
    (la1, lo1), (la2, lo2) = CITIES[a.lower()], CITIES[b.lower()]
    p1, p2, dp, dl = map(math.radians, (la1, la2, la2 - la1, lo2 - lo1))
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return round(2 * 6371 * math.asin(math.sqrt(h)), 1)


def split_budget(total: float, days: int) -> dict[str, float]:
    per_day = total / days
    return {"stay": round(per_day * 0.5, 2), "food": round(per_day * 0.3, 2), "travel": round(per_day * 0.2, 2)}
