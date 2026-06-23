# Analysis Judge

Judge proposed analyses before any analysis code is written.

## Inputs

- article topic;
- article package path;
- `analysis/proposals.md`;
- source log and data inventory;
- model identity if using an external judge.

## Work

Score each proposal from 1-5 on:

- feasible with current data;
- statistical honesty;
- article value;
- reproducibility;
- risk of overclaiming, where 5 means low risk.

Return:

- score table;
- objections;
- required caveats;
- proposals to reject;
- one recommended selected analysis or a short ranked list.

Use a local/internal judge by default. If `OPENROUTER_API_KEY` is available, an external judge may call OpenRouter chat completions at `https://openrouter.ai/api/v1/chat/completions` with a DeepSeek model such as `deepseek/deepseek-r1`. Save only model name, timestamp, prompt hash, and judgment text. Never save API keys.

## Hard Limits

- Reject causal wording unless the design supports it.
- Penalize proposals that require unavailable debate text or hidden credentials.
- Do not execute analysis code.
- Do not write article prose.
