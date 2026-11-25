Margin re-ran your agents on your own evals with `deepseek/deepseek-v4.1-flash-1017` in place of `openai/gpt-4.1`.

| | model | passed | cost per task |
|---|---|---|---|
| now | `openai/gpt-4.1` | 138 of 152 | $0.001687 |
| proposed | `deepseek/deepseek-v4.1-flash-1017` | 137 of 152 | $0.000084 |

Cost per task falls 95% at a pass-rate parity of 0.99.

**Response time**, measured offline, on Margin's runs: median 1.4s → 1.4s, p90 1.8s → 2.3s per model call. It depends on the hosts OpenRouter routed each call to, not only on the model.

**What it is worth**
Margin has no production calls of yours on `openai/gpt-4.1` in the last 30 days, so it does not know your volume and cannot say what this saves a month. Multiply the per-task saving above by the tasks you run, or enter your monthly task count in the console and this paragraph will use it. Measuring this cost $0.0128, the face-off's own bill.

**Not provable, so this is a draft.** Measured 0.8 points behind your current model on the same 129 cases (another 23 are held back to confirm a switch); at 97% confidence no more than 7.0 points behind, and a switch needs that within 2.8: 2.3 points is how much your evals move when nothing changes, so this is not yet a loss.

**A decision model advised holding this.** `typesafe/jev-1.14-20261014` read the numbers and which rubric checks only the new model failed, and said hold (51% sure).

**Answer: keep current.** Measured 0.8 points behind your current model on the same 129 cases (another 23 are held back to confirm a switch); at 97% confidence no more than 7.0 points behind, and a switch needs that within 2.8: 2.3 points is how much your evals move when nothing changes, so this is not yet a loss. Next step: Stay on your current model: this is the safe action, not proof the candidate is worse. Re-run with more evals, or with a candidate that is cheaper and passes at least as many.

Cases `deepseek/deepseek-v4.1-flash-1017` failed that your current model passed:
- `tests/test_triage.py::tests.test_triage::test_triage_classification[ignore-bring-a-friend-for-free-this-month]`: AssertionError: marketing: expected ignore, got notify assert 'notify' == 'ignore' - ignore + notify
- `tests/test_triage.py::tests.test_triage::test_triage_classification[ignore-double-miles-on-all-summer-bookings]`: AssertionError: marketing: expected ignore, got respond assert 'respond' == 'ignore' - ignore + respond
- `tests/test_triage.py::tests.test_triage::test_triage_classification[ignore-lose-20-pounds-in-a-week-doctors-hate-this]`: AssertionError: spam: expected ignore, got respond assert 'respond' == 'ignore' - ignore + respond
- `tests/test_triage.py::tests.test_triage::test_triage_classification[ignore-new-episodes-you-might-like]`: AssertionError: marketing: expected ignore, got notify assert 'notify' == 'ignore' - ignore + notify
- `tests/test_triage.py::tests.test_triage::test_triage_classification[notify-course-production-update]`: AssertionError: status_update: expected notify, got respond assert 'respond' == 'notify' - notify + respond
- `tests/test_triage.py::tests.test_triage::test_triage_classification[notify-rollout-to-100-complete-for-search-service]`: AssertionError: build_deploy: expected notify, got ignore assert 'ignore' == 'notify' - notify + ignore

**What changes**
- Margin could not find a model literal it can safely rewrite in the files it ran. Change `openai/gpt-4.1` to `deepseek/deepseek-v4.1-flash-1017` where your agent calls it.

**To undo it**, revert this pull request; nothing else was touched.

**After you merge**, Margin watches the runs you Execute from then on. If the pass rate falls clearly below what this switch had to clear, across at least 2 runs, Margin opens a second pull request that restores `gpt-4.1`. Nothing changes until you merge that one either.

_This PR states the change; it edits no file._