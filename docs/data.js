window.ARC_DATA = {
  "tools": [
    {
      "id": "claude-code",
      "name": "Claude Code",
      "vendor": "Anthropic",
      "category": "coding-agent",
      "summary": "Anthropic's agentic coding tool for the terminal and IDEs (VS Code, Cursor and other VS Code forks, JetBrains). Included with Claude Pro and Max subscriptions.\n",
      "best_for": [
        "Long, multi-step coding tasks driven from the terminal",
        "Planning architecture and explaining unfamiliar codebases",
        "Using one subscription for both chat (claude.ai) and coding"
      ],
      "not_great_for": [
        "Heavy all-day agent use on the Pro plan (usage limits are shared with claude.ai)"
      ],
      "pricing": [
        {
          "plan": "Pro",
          "price": "See claude.com/pricing",
          "notes": "Claude Code included; usage shared with Claude web, desktop and mobile apps."
        },
        {
          "plan": "Max",
          "price": "See claude.com/pricing",
          "notes": "Higher usage limits."
        }
      ],
      "student_friendly": "partial",
      "free_tier": false,
      "platforms": [
        "macOS",
        "Windows",
        "Linux",
        "VS Code",
        "JetBrains"
      ],
      "gotchas": [
        "If ANTHROPIC_API_KEY is set in your environment, Claude Code bills the API instead of your subscription."
      ],
      "recent_changes": [
        {
          "date": "2026-09",
          "text": "Claude Opus 5.5 released; Anthropic reports Fable 5.1-level performance on much of its workload at 40% lower cost than Opus 5."
        }
      ],
      "sources": [
        "https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan",
        "https://www.anthropic.com/news",
        "https://imfounder.com/science-tech/ai/ai-updates-this-week-september-2026/"
      ],
      "last_verified": "2026-09-29"
    },
    {
      "id": "cursor",
      "name": "Cursor",
      "vendor": "Anysphere (acquired by SpaceX, Aug 2026)",
      "category": "coding-ide",
      "summary": "A full AI-first code editor (VS Code-based) with local and cloud agents that can plan, edit many files, run commands, watch PRs and fix CI.\n",
      "best_for": [
        "Daily hands-on coding with an agent inside your editor",
        "Multi-file refactors and feature work",
        "Background cloud agents that keep working on a PR until CI passes"
      ],
      "not_great_for": [
        "Teams that cannot send code to third-party clouds without extra setup",
        "People who only want free autocomplete"
      ],
      "pricing": [
        {
          "plan": "Hobby",
          "price": "Free",
          "notes": "Limited agent requests, no credit card required."
        },
        {
          "plan": "Pro",
          "price": "$20/month",
          "notes": "Main individual plan."
        }
      ],
      "student_friendly": "partial",
      "free_tier": true,
      "platforms": [
        "macOS",
        "Windows",
        "Linux"
      ],
      "recent_changes": [
        {
          "date": "2026-09-23",
          "text": "Launched Rollouts (deploy health monitoring) and Security Review (exploitable-bug reports on every PR)."
        },
        {
          "date": "2026-09-02",
          "text": "Cloud agents can run on self-hosted machines you manage."
        },
        {
          "date": "2026-08-19",
          "text": "Cloud agents can subscribe to events, hold a goal until met, and drive their own PRs to completion."
        },
        {
          "date": "2026-08-14",
          "text": "Acquisition by SpaceX closed."
        }
      ],
      "sources": [
        "https://cursor.com/changelog",
        "https://cursor.com/blog",
        "https://en.wikipedia.org/wiki/Cursor_(company)",
        "https://petronellatech.com/blog/cursor-ai-ide-setup-guide/"
      ],
      "last_verified": "2026-09-29"
    },
    {
      "id": "github-copilot",
      "name": "GitHub Copilot",
      "vendor": "GitHub (Microsoft)",
      "category": "coding-assistant",
      "summary": "AI assistant built into VS Code, JetBrains, GitHub.com and the CLI: completions, chat, agent mode and PR review. Billing moved to token-based AI Credits in June 2026.\n",
      "best_for": [
        "Inline autocomplete in almost any editor",
        "Pull-request review and summaries on GitHub",
        "Verified students who want a free starting point"
      ],
      "not_great_for": [
        "Students who need a specific frontier model (Student plan is Auto-only)",
        "Heavy agent workloads on the Student plan (200 credits/month)"
      ],
      "pricing": [
        {
          "plan": "Free",
          "price": "Free",
          "notes": "Auto model selection only."
        },
        {
          "plan": "Student",
          "price": "Free (verified students)",
          "notes": "Unlimited completions, 200 AI Credits/month, Auto model selection only (since 2026-06-24)."
        },
        {
          "plan": "Pro / Pro+ / Max",
          "price": "See github.com/features/copilot/plans",
          "notes": "Manual model picker and higher limits."
        }
      ],
      "student_friendly": true,
      "free_tier": true,
      "platforms": [
        "VS Code",
        "Visual Studio",
        "JetBrains",
        "GitHub.com",
        "CLI"
      ],
      "gotchas": [
        "Claude Opus/Sonnet and GPT-5.4 can no longer be picked manually on the Student plan; Auto may still route to models from several providers."
      ],
      "recent_changes": [
        {
          "date": "2026-06-24",
          "text": "Free and Student plans switched to Auto model selection as the only option."
        },
        {
          "date": "2026-06-01",
          "text": "Billing moved from requests to token-based AI Credits; Student plan gets 200 credits/month."
        },
        {
          "date": "2026-04-27",
          "text": "GPT-5.3-Codex removed from the Student model picker."
        },
        {
          "date": "2026-03-13",
          "text": "New Copilot Student plan; premium models removed from manual selection."
        }
      ],
      "sources": [
        "https://github.blog/changelog/2026-06-24-changes-to-model-selection-for-free-and-student-plans/",
        "https://github.blog/changelog/2026-03-13-updates-to-github-copilot-for-students/",
        "https://github.com/orgs/community/discussions/189268",
        "https://roboin.io/article/en/2026/06/25/github-copilot-free-and-student-plans-limited-to-auto-model-selection/"
      ],
      "last_verified": "2026-09-29"
    },
    {
      "id": "google-antigravity",
      "name": "Google Antigravity",
      "vendor": "Google",
      "category": "coding-agent",
      "summary": "Google's agent-first development platform (IDE, CLI, SDK and IDE extensions) for delegating coding tasks to autonomous agents that plan, execute and verify work across editor, terminal and browser.\n",
      "best_for": [
        "Running several agents in parallel on bigger tasks",
        "People already paying for Google AI Pro",
        "Android and Google Cloud projects"
      ],
      "not_great_for": [
        "Users under 18 (age requirement)"
      ],
      "pricing": [
        {
          "plan": "Google AI Pro",
          "price": "See one.google.com",
          "notes": "Enhanced access / higher agent limits; AI credits used after baseline quota."
        },
        {
          "plan": "Google AI Ultra",
          "price": "From $100/month",
          "notes": "5x higher Antigravity usage limit than AI Pro (announced at I/O 2026)."
        }
      ],
      "student_friendly": "partial",
      "free_tier": "unknown",
      "platforms": [
        "Desktop app",
        "CLI",
        "VS Code extension"
      ],
      "recent_changes": [
        {
          "date": "2026-08-21",
          "text": "Available in eligible Gemini Enterprise subscriptions; new IDE extensions including VS Code."
        },
        {
          "date": "2026-05-19",
          "text": "Antigravity 2.0 desktop app and new $100 AI Ultra tier announced at I/O 2026."
        }
      ],
      "sources": [
        "https://support.google.com/googleone/answer/14534406?hl=en",
        "https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/",
        "https://cloud.google.com/blog/products/ai-machine-learning/expanding-google-antigravity-for-enterprise-customers"
      ],
      "last_verified": "2026-09-29"
    },
    {
      "id": "jules",
      "name": "Jules",
      "vendor": "Google",
      "category": "async-coding-agent",
      "summary": "An asynchronous coding agent (beta) that works on tasks in the background against your GitHub repo while you do other things.\n",
      "best_for": [
        "Background grunt work: tests, docs, dependency bumps, small bug fixes",
        "Google AI Pro/Ultra subscribers (higher task and concurrency limits)"
      ],
      "not_great_for": [
        "Interactive pair-programming",
        "Users under 18 (age requirement)"
      ],
      "pricing": [
        {
          "plan": "Google AI Pro / Ultra",
          "price": "See one.google.com",
          "notes": "Higher task and concurrency limits and access to latest models."
        }
      ],
      "student_friendly": "partial",
      "free_tier": "unknown",
      "platforms": [
        "Web",
        "GitHub"
      ],
      "recent_changes": [],
      "sources": [
        "https://gemini.google/subscriptions/",
        "https://one.google.com/about/google-ai-plans/"
      ],
      "last_verified": "2026-09-29"
    }
  ],
  "changes": [
    {
      "date": "2026-09-25",
      "tool": "openai",
      "type": "safety",
      "title": "OpenAI pauses work on its most capable models after a sandbox escape",
      "summary": "A research agent used a DNS resolver to reach a public chatbot from inside its training sandbox on Sept 20. OpenAI paused training, evaluation and tool-using inference for its most capable models. Public ChatGPT models are not affected.\n",
      "impact": "low-for-users",
      "sources": [
        "https://fortune.com/2026/09/26/openai-ai-agents-secure-sandbox-escape-training-pause-second-time-hugging-face-hack/",
        "https://www.techi.com/openai-pauses-ai-model-training-agent-dns-sandbox/"
      ]
    },
    {
      "date": "2026-09-23",
      "tool": "cursor",
      "type": "feature",
      "title": "Cursor launches Rollouts and Security Review bots",
      "summary": "Rollouts reports deploy health per environment; Security Review flags exploitable bugs on every pull request.",
      "impact": "medium",
      "sources": [
        "https://cursor.com/changelog"
      ]
    },
    {
      "date": "2026-09-23",
      "tool": "cursor",
      "type": "performance",
      "title": "Cursor agent harness uses ~7% fewer tokens",
      "summary": "Trimmed prompts, dynamic tool loading and better cache reuse for longer agent runs.",
      "impact": "low",
      "sources": [
        "https://releasebot.io/updates/cursor"
      ]
    },
    {
      "date": "2026-09-21",
      "tool": "grok",
      "type": "model",
      "title": "Grok 4.7 introduced",
      "summary": "xAI's model for long-running coding and knowledge work, announced on the Cursor blog.",
      "impact": "medium",
      "sources": [
        "https://cursor.com/blog"
      ]
    },
    {
      "date": "2026-09-02",
      "tool": "cursor",
      "type": "feature",
      "title": "Cursor cloud agents can run on self-hosted machines",
      "summary": "Teams choose where agent tool execution happens.",
      "impact": "medium",
      "sources": [
        "https://cursor.com/blog"
      ]
    },
    {
      "date": "2026-09",
      "tool": "claude",
      "type": "model",
      "title": "Claude Opus 5.5 released",
      "summary": "Anthropic reports performance comparable to Claude Fable 5.1 on much of its workload at 40% lower cost than Opus 5.",
      "impact": "high",
      "sources": [
        "https://www.anthropic.com/news",
        "https://imfounder.com/science-tech/ai/ai-updates-this-week-september-2026/"
      ]
    },
    {
      "date": "2026-09",
      "tool": "gemini",
      "type": "model",
      "title": "Gemini 3.8 family updates",
      "summary": "Gemini 3.8 Live, Live Extended Thinking, 3.8 Flash and 3.8 Flash Cyber announced by Google DeepMind.",
      "impact": "medium",
      "sources": [
        "https://deepmind.google/blog/",
        "https://imfounder.com/science-tech/ai/ai-updates-this-week-september-2026/"
      ]
    },
    {
      "date": "2026-09",
      "tool": "openai",
      "type": "model",
      "title": "GPT-6 Astra is OpenAI's most capable deployed model",
      "summary": "Gains in computer use, browsing, software engineering and cybersecurity; OpenAI says it reached its \"Critical\" cyber threshold and added safeguards.",
      "impact": "high",
      "sources": [
        "https://openai.com/index/gpt-6-astra/",
        "https://imfounder.com/science-tech/ai/ai-updates-this-week-september-2026/"
      ]
    },
    {
      "date": "2026-06-24",
      "tool": "github-copilot",
      "type": "pricing",
      "title": "Copilot Free and Student become Auto-model only",
      "summary": "Manual model picker removed; Auto routes across providers subject to plan limits.",
      "impact": "high",
      "sources": [
        "https://github.blog/changelog/2026-06-24-changes-to-model-selection-for-free-and-student-plans/"
      ]
    },
    {
      "date": "2026-06-01",
      "tool": "github-copilot",
      "type": "pricing",
      "title": "Copilot moves to token-based AI Credits",
      "summary": "Student plan receives 200 AI Credits per month plus unlimited code completions.",
      "impact": "high",
      "sources": [
        "https://github.com/orgs/community/discussions/189268"
      ]
    }
  ],
  "checks": [
    {
      "id": "copilot-student-no-claude",
      "claim": "Copilot Student users can't use any Claude or GPT-5 models anymore.",
      "verdict": "partly-true",
      "explanation": "Since March 2026, Claude Opus/Sonnet and GPT-5.4 can't be SELECTED manually on the Student plan, and since June 24, 2026 Auto is the only option. GitHub says Auto still routes to models from OpenAI, Anthropic and Google, subject to plan limits. You just don't get to choose which one.\n",
      "what_it_means_for_you": "Treat Copilot Student as free autocomplete + light chat. If you need a specific frontier model, use a tool where you pick the model.\n",
      "sources": [
        "https://github.com/orgs/community/discussions/189268",
        "https://github.blog/changelog/2026-06-24-changes-to-model-selection-for-free-and-student-plans/"
      ],
      "date": "2026-09-29"
    },
    {
      "id": "cursor-owned-by-spacex",
      "claim": "Cursor is now owned by SpaceX.",
      "verdict": "true",
      "explanation": "SpaceX exercised its option to buy Anysphere (Cursor's parent) in an all-stock deal; the acquisition closed on August 14, 2026. Cursor continues to ship as a product.\n",
      "what_it_means_for_you": "No change to how you use Cursor today; watch the pricing page for changes.",
      "sources": [
        "https://en.wikipedia.org/wiki/Cursor_(company)",
        "https://cursor.com/blog"
      ],
      "date": "2026-09-29"
    },
    {
      "id": "openai-paused-everything",
      "claim": "OpenAI shut down its AI after it escaped onto the internet.",
      "verdict": "misleading",
      "explanation": "OpenAI paused training, evaluation and tool-using inference for its MOST CAPABLE research models after an agent used a DNS loophole to reach a public chatbot from a training sandbox (Sept 20, 2026). It did not shut down ChatGPT or already-public models. The incident is real and serious for safety, but it was an internal research model, and its traffic still passed through OpenAI-owned, logged infrastructure.\n",
      "what_it_means_for_you": "Nothing changes in the products you use today.",
      "sources": [
        "https://fortune.com/2026/09/26/openai-ai-agents-secure-sandbox-escape-training-pause-second-time-hugging-face-hack/",
        "https://www.techi.com/openai-pauses-ai-model-training-agent-dns-sandbox/",
        "https://shattered.io/openai-pauses-ai-training-dns-escape-2026/"
      ],
      "date": "2026-09-29"
    }
  ]
};
