# Draft: possible change on `cursor-changelog`
- Tool: `cursor`
- Source: https://cursor.com/changelog
- Detected: 2026-10-31
- Status: **needs human verification**

## AI draft summary (verify before using)
_No AI summary (no API key configured)._

## New text on the page
```text
The Agent SDK is available today. It allows you to define an agent as a folder of code, test it with evals, and deploy it to Cursor or your own infrastructure.
Run npx @cursor/agent-sdk init ./my-bot , then agent-sdk dev to start the bot locally with a playground. Pass --template to start from a security reviewer, an owners-policy approver, a PR autofixer, or a Linear or Jira triager.
# Deploy agents wherever you need them
When you're ready to put an agent into use, you can deploy it to Cursor by running agent-sdk deploy from the project directory. The command builds the agent, gives it a URL, and starts it on our infrastructure. You can manage secrets and integrations from the dashboard, while continuing to use the same logs, evals, and playground available locally.
An agent is a project. instructions.md is the prompt. Each file in tools/ is one typed action the model can call. skills/ holds procedures the model loads on demand, mcp-connections/ adds tools from MCP servers, and channels/ defines where the bot receives and answers messages. agent-sdk validate checks the project and agent-sdk info prints what was discovered.
Agents wake on pull request, comment, and CI events from GitHub, GitLab, and Bitbucket; on mentions and DMs in Slack; on webhooks from any provider; and on a cron schedule. GitHub events pull through your Cursor account, so no public webhook URL is required. Slack is well-supported out of the box.
Each conversation keeps its own session and a complete record of every message and tool call. Follow-ups on a pull request or Slack thread resume the same session.
An eval sends a fixed message to the bot and asserts on what it did: which tools ran, with what input, and the shape of the reply. Run agent-sdk eval locally or in CI.
agent-sdk github replay <pr-url> turns a real pull request into signed webhook payloads and sends them to the bot, so GitHub-driven bots can be tested without waiting for a push. Add --dry-run --fixtures-dir fixtures/ to save the payloads as eval fixtures.
The Agent SDK is generally available today. Read the docs and get started.
Cloud Agent Canvases and Environment Improvements
# Canvases from cloud agents
Cloud agents can now build interactive canvases as part of their work. Share a finished canvas with your team by sending its link.
Learn more about sharing canvases .
The Environments API is now available in beta. Use it to programmatically create and manage the cloud environments your agents run in.
# Larger, faster environments
Cloud agent environments now support up to 300 repositories. Large environments also load 5x faster.
Origin now integrates with over 20 apps for deployments, CI, code review, security, monitoring, and project management, from partners including Cloudflare, Linear, Sentry, and Socket Security.
Starting today, the marketplace is also open to public submissions, so any team building developer tools can publish an app for Origin.
The marketplace now includes apps for:
Deployments: Cloudflare , Netlify , Render , Spacelift , and Vercel
CI: Buildkite , CircleCI , CloudBees , Depot , EngFlow , Namespace , and RWX
Code review: CodeRabbit , Greptile , and Tenki
Security: Artemis Security , Semgrep , Socket Security , and Upwind
Project management: Linear
Create an app in your namespace. It stays private to your namespace while you build.
Build against the Origin API . Apps authenticate with an app JWT and installation access tokens, receive webhook events, and write back check runs, pull request comments, and reviews.
Make the app public, then submit it from the app's page with a slug, suggested tags, and a demo video. The video should show install, uninstall, and your core product flows.
We review the submission and list the app once it's approved.
Try the apps in the Origin App Marketplace today.
Want to build an Origin app? Start with the publishing guide and the Origin API reference .
The Origin Apps plugin can also answer questions from the live Origin API docs and plan a port to Origin for an app you already run.
Remote control for local agents
You can now see and reply to the local agents running on your computer from the Cursor iOS app.
Remote Control is on by default for everyone except Enterprise organizations.
Download the Cursor iOS app and sign in. Computers on your account appear in the app automatically. Tap your computer in the app and approve your pairing request in the Cursor desktop app. Your local agents appear in a list. Tap one to see what it's doing or send it a message.
# Agents keep running on your computer
Remote control doesn't move your agents anywhere. It keeps running on your computer, and the app connects to it. Your computer needs to stay on and online for remote control to work.
# Keep your computer awake
To stop your computer from sleeping while you're away, turn on "Keep this computer awake" under Remote Control in Cursor's desktop settings. Your computer needs to be plugged in with the lid open.
Remote control is on by default, except for Enterprise organizations. Enterprise admins can turn it on in Org settings > Security and identity > Remote control.
Remote control doesn't require cloud agents to work.
Remote control is available today in the Cursor iOS app .
SpaceXSI Subscription Terms ↗
The Agent SDK is available today. It allows you to define an agent as a folder of code, test it with evals, and deploy it to Cursor or your own infrastructure.
Run npx @cursor/agent-sdk init ./my-bot , then agent-sdk dev to start the bot locally with a playground. Pass --template to start from a security reviewer, an owners-policy approver, a PR autofixer, or a Linear or Jira triager.
# Deploy agents wherever you need them
When you're ready to put an agent into use, you can deploy it to Cursor by running agent-sdk deploy from the project directory. The command builds the agent, gives it a URL, and starts it on our infrastructure. You can manage secrets and integrations from the dashboard, while continuing to use the same logs, evals, and playground available locally.
An agent is a project. instructions.md is the prompt. Each file in tools/ is one typed action the model can call. skills/ holds procedures the model loads on demand, mcp-connections/ adds tools from MCP servers, and channels/ defines where the bot receives and answers messages. agent-sdk validate checks the project and agent-sdk info prints what was discovered.
Agents wake on pull request, comment, and CI events from GitHub, GitLab, and Bitbucket; on mentions and DMs in Slack; on webhooks from any provider; and on a cron schedule. GitHub events pull through your Cursor account, so no public webhook URL is required. Slack is well-supported out of the box.
Each conversation keeps its own session and a complete record of every message and tool call. Follow-ups on a pull request or Slack thread resume the same session.
An eval sends a fixed message to the bot and asserts on what it did: which tools ran, with what input, and the shape of the reply. Run agent-sdk eval locally or in CI.
agent-sdk github replay <pr-url> turns a real pull request into signed webhook payloads and sends them to the bot, so GitHub-driven bots can be tested without waiting for a push. Add --dry-run --fixtures-dir fixtures/ to save the payloads as eval fixtures.
The Agent SDK is generally available today. Read the docs and get started.
Cloud Agent Canvases and Environment Improvements
# Canvases from cloud agents
Cloud agents can now build interactive canvases as part of their work. Share a finished canvas with your team by sending its link.
Learn more about sharing canvases .
The Environments API is now available in beta. Use it to programmatically create and manage the cloud environments your agents run in.
# Larger, faster environments
Cloud agent environments now support up to 300 repositories. Large environments also load 5x faster.
Origin now integrates with over 20 apps for deployments, CI, code review, security, monitoring, and project management, from partners including Cloudflare, Linear, Sentry, and Socket Security.
Starting today, the marketplace is also open to public submissions, so any team building developer tools can publish an app for Origin.
The marketplace now includes apps for:
Deployments: Cloudflare , Netlify , Render , Spacelift , and Vercel
CI: Buildkite , CircleCI , CloudBees , Depot , EngFlow , Namespace , and RWX
Code review: CodeRabbit , Greptile , and Tenki
Security: Artemis Security , Semgrep , Socket Security , and Upwind
Project management: Linear
Create an app in your namespace. It stays private to your namespace while you build.
Build against the Origin API . Apps authenticate with an app JWT and installation access tokens, receive webhook events, and write back check runs, pull request comments, and reviews.
Make the app public, then submit it from the app's page with a slug, suggested tags, and a demo video. The video should show install, uninstall, and your core product flows.
We review the submission and list the app once it's approved.
Try the apps in the Origin App Marketplace today.
Want to build an Origin app? Start with the publishing guide and the Origin API reference .
The Origin Apps plugin can also answer questions from the live Origin API docs and plan a port to Origin for an app you already run.
Remote control for local agents
You can now see and reply to the local agents running on your computer from the Cursor iOS app.
Remote Control is on by default for everyone except Enterprise organizations.
Download the Cursor iOS app and sign in. Computers on your account appear in the app automatically. Tap your computer in the app and approve your pairing request in the Cursor desktop app. Your local agents appear in a list. Tap one to see what it's doing or send it a message.
```
