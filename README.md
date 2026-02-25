# hf_restart_cron

Keeps Hugging Face Spaces alive by automatically restarting them every 48 hours via a scheduled GitHub Actions workflow.

## Why

Free-tier Hugging Face Spaces sleep after 48 hours of inactivity. This repo uses the official [`huggingface_hub`](https://github.com/huggingface/huggingface_hub) Python library to restart them on a schedule — no paid services, no persistent servers.

## How it works

A GitHub Actions cron job runs every 48 hours and calls `restart_space()` for each configured space. GitHub Actions free tier is more than sufficient (~2 runs/week per space).

## Setup

### 1. Fork or clone this repo

### 2. Edit `wake_spaces.py`

Update the `spaces` list with your own space IDs:

```python
spaces = [
    "your-username/your-space-1",
    "your-username/your-space-2",
]
```

### 3. Add your Hugging Face token as a GitHub secret

1. Generate a token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) (Read access is sufficient)
2. In this repo, go to **Settings → Secrets and variables → Actions → New repository secret**
3. Name: `HF_TOKEN` / Value: your token

### 4. Enable GitHub Actions

Go to the **Actions** tab and confirm workflows are enabled. The cron will trigger automatically. You can also run it manually via **Run workflow**.

## Configuration

| File | Purpose |
|------|---------|
| `wake_spaces.py` | List of spaces to restart |
| `.github/workflows/wake-spaces.yml` | Cron schedule and workflow definition |

To change the schedule, edit the `cron` value in the workflow file. The default is every 48 hours (`0 0 */2 * *`). For a safer buffer, consider every 24 hours (`0 0 * * *`).

## Dependencies

- [`huggingface_hub`](https://pypi.org/project/huggingface-hub/) (installed at runtime by the workflow)
