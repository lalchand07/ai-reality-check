# Setup after you push this repo (5 minutes)

1. **Replace the placeholder.** Find and replace `YOUR_USERNAME` with your GitHub username:
   ```bash
   grep -rl YOUR_USERNAME . | xargs sed -i 's/YOUR_USERNAME/your-name/g'   # macOS: sed -i ''
   ```
2. **Enable the website.** Settings → Pages → Source: *Deploy from a branch* → Branch `main`, folder `/docs`.
3. **Let the bot open PRs.** Settings → Actions → General → Workflow permissions → *Read and write*, and tick *Allow GitHub Actions to create and approve pull requests*.
4. **Create labels** (optional, the workflows fall back without them): `bot`, `needs-verification`, `stale`, `change`, `new-tool`, `reality-check`.
5. **AI summaries (optional).** Settings → Secrets and variables → Actions → New secret `ANTHROPIC_API_KEY`. Without it the bot still works; drafts just contain the raw new text.
6. **Run the watcher once by hand.** Actions → *Watch official sources* → *Run workflow*. The first run only stores snapshots; real change detection starts from the second run.
7. **Repo polish.** Add a description, the website URL, and topics: `ai`, `ai-tools`, `developer-tools`, `copilot`, `cursor`, `claude`, `gemini`, `fact-check`, `awesome`.
