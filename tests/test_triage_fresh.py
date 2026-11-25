"""The triage router on 200 held-out cases (triage_cases_fresh.py), same rules, same check.

One model call per case: ``triage_router`` alone, not the response agent. Cases and the rule
each one falls under are in ``triage_cases_fresh.py``.
"""
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from triage_cases_fresh import CASES  # noqa: E402

from email_assistant.email_assistant import triage_router  # noqa: E402


def _id(case):
    return f"{case['label']}-{re.sub(r'[^a-z0-9]+', '-', case['email']['subject'].lower()).strip('-')[:48]}"


@pytest.mark.parametrize("case", CASES, ids=[_id(c) for c in CASES])
def test_triage_classification_fresh(case):
    command = triage_router({"email_input": case["email"]})
    got = command.update["classification_decision"]
    assert got == case["label"], f"{case['rule']}: expected {case['label']}, got {got}"
