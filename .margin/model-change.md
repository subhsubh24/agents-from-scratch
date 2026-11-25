Margin re-ran your agents on your own evals with `deepseek/deepseek-v4.1-flash-1017` in place of `openai/gpt-4.1`.

| | model | passed | cost per task |
|---|---|---|---|
| now | `openai/gpt-4.1` | 322 of 352 | $0.001636 |
| proposed | `deepseek/deepseek-v4.1-flash-1017` | 329 of 352 | $0.000092 |

Cost per task falls 94% at a pass-rate parity of 1.02.

**Response time**, measured offline, on Margin's runs: median 1.7s → 1.2s, p90 2.2s → 2.5s per model call. It depends on the hosts OpenRouter routed each call to, not only on the model.

**What it is worth**
Margin has no production calls of yours on `openai/gpt-4.1` in the last 30 days, so it does not know your volume and cannot say what this saves a month. Multiply the per-task saving above by the tasks you run, or enter your monthly task count in the console and this paragraph will use it. Measuring this cost $0.0323, the face-off's own bill.

**Proven.** Margin's parity gate promoted this switch on your evals.

**Answer: switch.** At 98% confidence, its true pass rate is at least 90% on these 352 evals; a switch needs that to reach 97%. It is the best of 3 models tried, so it is judged at the stricter bar that choosing among them needs. Next step: Review the pull request and merge it; Margin watches the runs after you do.

Cases `deepseek/deepseek-v4.1-flash-1017` failed that your current model passed:
- `tests/test_triage.py::tests.test_triage::test_triage_classification[ignore-your-mailbox-will-be-suspended]`: AssertionError: spam: expected ignore, got respond assert 'respond' == 'ignore' - ignore + respond
- `tests/test_triage.py::tests.test_triage::test_triage_classification[notify-your-intellij-idea-license-renews-in-14-days]`: AssertionError: subscription: expected notify, got ignore assert 'ignore' == 'notify' - notify + ignore
- `tests/test_triage.py::tests.test_triage::test_triage_classification[respond-your-daughter-s-swim-meet-registration]`: AssertionError: family: expected respond, got notify assert 'notify' == 'respond' - respond + notify
- `tests/test_triage_fresh.py::tests.test_triage_fresh::test_triage_classification_fresh[ignore-get-your-website-to-1-on-google]`: AssertionError: spam: expected ignore, got notify assert 'notify' == 'ignore' - ignore + notify
- `tests/test_triage_fresh.py::tests.test_triage_fresh::test_triage_classification_fresh[ignore-infra-brief-88-postgres-19-edge-caching-and-a-gp]`: AssertionError: marketing: expected ignore, got respond assert 'respond' == 'ignore' - ignore + respond
- `tests/test_triage_fresh.py::tests.test_triage_fresh::test_triage_classification_fresh[notify-fyi-legal-approved-the-data-retention-policy]`: AssertionError: fyi_relevant: expected notify, got ignore assert 'ignore' == 'notify' - notify + ignore
- `tests/test_triage_fresh.py::tests.test_triage_fresh::test_triage_classification_fresh[notify-press-release-partnership-with-acme-cloud]`: AssertionError: announcement: expected notify, got ignore assert 'ignore' == 'notify' - notify + ignore
- `tests/test_triage_fresh.py::tests.test_triage_fresh::test_triage_classification_fresh[notify-terraform-apply-completed]`: AssertionError: build_deploy: expected notify, got respond assert 'respond' == 'notify' - notify + respond

**What changes**
- Margin could not find a model literal it can safely rewrite in the files it ran. Change `openai/gpt-4.1` to `deepseek/deepseek-v4.1-flash-1017` where your agent calls it.

**To undo it**, revert this pull request; nothing else was touched.

**After you merge**, Margin watches the runs you Execute from then on. If the pass rate falls clearly below what this switch had to clear, across at least 2 runs, Margin opens a second pull request that restores `gpt-4.1`. Nothing changes until you merge that one either.

_This PR states the change; it edits no file._