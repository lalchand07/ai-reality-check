# Draft: possible change on `cursor-changelog`
- Tool: `cursor`
- Source: https://cursor.com/changelog
- Detected: 2026-11-07
- Status: **needs human verification**

## AI draft summary (verify before using)
_No AI summary (no API key configured)._

## New text on the page
```text
You can now talk with your agents in a realtime voice call. Describe a change out loud, ask what an agent is working on, and hear updates as the work moves forward.
Voice chat works in the Agents Window, the IDE, on web, and in Cursor for iOS.
When the agent is idle and the chat input is empty, click the waveform button labeled Start voice chat . It sits where Send usually is, next to the microphone button for dictation.
On iOS, you can also say "Hey Siri, call Cursor" to start a call with a new agent, and mute or hang up from the Lock Screen with a Live Activity.
# Talk while the agent works
The voice agent listens, replies, and hands coding work to the agent in your chat. While that agent runs, you can keep the conversation going. Ask what changed in a diff, check on a run, search earlier messages and calls with this agent, or switch between workers in a Project that has them.
The coding agent speaks for itself too. It shares short progress notes while it works and a brief answer when it's done, so you usually hear a short update instead of the full written reply.
Voice chat runs on Grok Voice. Pick from many voices in Voice settings, including Ara, Eve, Leo, Rex, and Sal. With Privacy Mode on, voice chat runs with zero data retention.
# Voice chat and dictation
Voice chat is separate from dictation, which earlier releases called Voice Mode. Dictation still turns your speech into text in the chat input, and Cmd+Shift+Space still toggles it in the IDE. Voice chat is a two-way conversation where the agent answers out loud.
Update Cursor to try voice chat. Learn more in our docs .
Build Live Apps in Cursor
Agents have lowered the cost of writing code, but most apps and tools that users build never make it off of localhost.
Now, you can build live apps directly in Cursor and share them with a link. Describe what you want to create and Cursor will handle the rest: build the app, set up a database, configure auth, and deploy it.
With this release, anyone in your org can now build useful tools for their work and share them with teammates. Update Cursor to try it out.
To get started, kick off a cloud agent and tell it explicitly that you want to build an app.
Cursor will scaffold the web app, spin up a Postgres database if needed, set up authentication behind Cursor SSO, and provision hosting. If the app needs to connect to your systems, like a data warehouse, Cursor will ask for the secrets it needs.
When you go to publish your app, you pick a unique domain and Cursor gets you back a live link.
At Cursor, users across sales, operations, legal, finance, and engineering are building internal apps. Some of the most useful ones are:
Internal ops tools for event registration, account assignments, and desk seating
Multimedia presentations for customers that combine slides, videos, and interactive demos
Training, enablement, and onboarding experiences for new hires
Live dashboards and tools for sales teams to understand their pipeline and opportunities
Portals to manage engineering services
Cursor can deploy apps from new or existing repos across Cursor Origin and GitHub. Support for other git providers like GitLab is coming soon.
# Controls and guardrails
When you publish an app, Cursor will run deterministic and agentic security checks to catch common issues, like secrets written in app files or exposed credentials. If a check fails, the agent tells you what it needs to fix. Nothing goes live until the checks pass and you explicitly publish the app.
Team admins can see every app and secret on the team. They can also add their own rules to the security review, approve publishes the review blocked, and unpublish any app.
Once the checks pass, Cursor deploys the app to the URL you chose. You can then share your app with specific people, groups, or your entire team, all behind Cursor sign-in. On individual plans, you can also share apps publicly.
You can also provision a Cursor API key if you want a script or Grok Bot to use your app.
This capability is now available on all paid plans with cloud agents enabled. Learn more by reading our docs .
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
SpaceXSI Subscription Terms ↗
You can now talk with your agents in a realtime voice call. Describe a change out loud, ask what an agent is working on, and hear updates as the work moves forward.
Voice chat works in the Agents Window, the IDE, on web, and in Cursor for iOS.
When the agent is idle and the chat input is empty, click the waveform button labeled Start voice chat . It sits where Send usually is, next to the microphone button for dictation.
On iOS, you can also say "Hey Siri, call Cursor" to start a call with a new agent, and mute or hang up from the Lock Screen with a Live Activity.
# Talk while the agent works
The voice agent listens, replies, and hands coding work to the agent in your chat. While that agent runs, you can keep the conversation going. Ask what changed in a diff, check on a run, search earlier messages and calls with this agent, or switch between workers in a Project that has them.
The coding agent speaks for itself too. It shares short progress notes while it works and a brief answer when it's done, so you usually hear a short update instead of the full written reply.
Voice chat runs on Grok Voice. Pick from many voices in Voice settings, including Ara, Eve, Leo, Rex, and Sal. With Privacy Mode on, voice chat runs with zero data retention.
# Voice chat and dictation
Voice chat is separate from dictation, which earlier releases called Voice Mode. Dictation still turns your speech into text in the chat input, and Cmd+Shift+Space still toggles it in the IDE. Voice chat is a two-way conversation where the agent answers out loud.
Update Cursor to try voice chat. Learn more in our docs .
Build Live Apps in Cursor
Agents have lowered the cost of writing code, but most apps and tools that users build never make it off of localhost.
Now, you can build live apps directly in Cursor and share them with a link. Describe what you want to create and Cursor will handle the rest: build the app, set up a database, configure auth, and deploy it.
With this release, anyone in your org can now build useful tools for their work and share them with teammates. Update Cursor to try it out.
To get started, kick off a cloud agent and tell it explicitly that you want to build an app.
```
