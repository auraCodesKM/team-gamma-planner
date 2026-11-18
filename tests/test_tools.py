import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
import tools  # noqa: E402


def test_distance_delhi_jaipur() -> None:
    assert 230 < tools.distance_km("Delhi", "Jaipur") < 250


def test_budget_split_sums_to_daily_total() -> None:
    s = tools.split_budget(15000, 3)
    assert round(sum(s.values()), 2) == 5000
