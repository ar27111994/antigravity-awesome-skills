# 🌌 Antigravity Awesome Skills: 257+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More

> **The Ultimate Collection of 257+ Universal Agentic Skills for AI Coding Assistants — Claude Code, Gemini CLI, Codex CLI, Antigravity IDE, GitHub Copilot, Cursor, OpenCode**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Anthropic-purple)](https://claude.ai)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Google-blue)](https://github.com/google-gemini/gemini-cli)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-OpenAI-green)](https://github.com/openai/codex)
[![Cursor](https://img.shields.io/badge/Cursor-AI%20IDE-orange)](https://cursor.sh)
[![Copilot](https://img.shields.io/badge/GitHub%20Copilot-VSCode-lightblue)](https://github.com/features/copilot)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-gray)](https://github.com/opencode-ai/opencode)
[![Antigravity](https://img.shields.io/badge/Antigravity-DeepMind-red)](https://github.com/sickn33/antigravity-awesome-skills)

**Antigravity Awesome Skills** is a curated, battle-tested library of **256 high-performance agentic skills** designed to work seamlessly across all major AI coding assistants:

- 🟣 **Claude Code** (Anthropic CLI)
- 🔵 **Gemini CLI** (Google DeepMind)
- 🟢 **Codex CLI** (OpenAI)
- 🔴 **Antigravity IDE** (Google DeepMind)
- 🩵 **GitHub Copilot** (VSCode Extension)
- 🟠 **Cursor** (AI-native IDE)
- ⚪ **OpenCode** (Open-source CLI)

This repository provides essential skills to transform your AI assistant into a **full-stack digital agency**, including official capabilities from **Anthropic**, **OpenAI**, **Google**, **Supabase**, and **Vercel Labs**.

## Table of Contents

- [🚀 New Here? Start Here!](#new-here-start-here)
- [🔌 Compatibility & Invocation](#compatibility--invocation)
- [📦 Features & Categories](#features--categories)
- [🎁 Curated Collections (Bundles)](#curated-collections)
- [📜 Full Skill Registry](#full-skill-registry-256256)
- [🛠️ Installation](#installation)
- [🤝 How to Contribute](#how-to-contribute)
- [👥 Contributors & Credits](#credits--sources)
- [⚖️ License](#license)
- [👥 Repo Contributors](#repo-contributors)
- [🌟 Star History](#star-history)

---

## New Here? Start Here!

**Welcome to the V3.5.0 Enterprise Edition.** This isn't just a list of scripts; it's a complete operating system for your AI Agent.

### 1. 🐣 Context: What is this?

AI Agents (like Claude Code, Cursor, or Gemini) are smart, but they lack **specific tools**. They don't know your company's "Deployment Protocol" or the specific syntax for "AWS CloudFormation".
**Skills** are small markdown files that teach them how to do these specific tasks perfectly, every time.

### 2. ⚡️ Quick Start (The "Bundle" Way)

Don't install 250+ skills manually. Use our **Starter Packs**:

1.  **Clone the repo**:
    ```bash
    git clone https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills
    ```
2.  **Pick your persona** (See [docs/BUNDLES.md](docs/BUNDLES.md)):
    - **Web Dev?** use the `Web Wizard` pack.
    - **Hacker?** use the `Security Engineer` pack.
    - **Just curious?** start with `Essentials`.

### 3. 🧠 How to use

Once installed, just ask your agent naturally:

> "Use the **@brainstorming** skill to help me plan a SaaS."
> "Run **@lint-and-validate** on this file."

👉 **[Read the Full Getting Started Guide](GETTING_STARTED.md)**

---

## Compatibility & Invocation

These skills follow the universal **SKILL.md** format and work with any AI coding assistant that supports agentic skills.

| Tool            | Type | Invocation Example                | Path              |
| :-------------- | :--- | :-------------------------------- | :---------------- |
| **Claude Code** | CLI  | `>> /skill-name help me...`       | `.claude/skills/` |
| **Gemini CLI**  | CLI  | `(User Prompt) Use skill-name...` | `.gemini/skills/` |
| **Antigravity** | IDE  | `(Agent Mode) Use skill...`       | `.agent/skills/`  |
| **Cursor**      | IDE  | `@skill-name (in Chat)`           | `.cursor/skills/` |
| **Copilot**     | Ext  | `(Paste content manually)`        | N/A               |

> [!TIP]
> **Universal Path**: We recommend cloning to `.agent/skills/`. Most modern tools (Antigravity, recent CLIs) look here by default.

> [!WARNING]
> **Windows Users**: This repository uses **symlinks** for official skills.
> You must enable Developer Mode or run Git as Administrator:
> `git clone -c core.symlinks=true https://github.com/...`

---

Whether you are using **Gemini CLI**, **Claude Code**, **Codex CLI**, **Cursor**, **GitHub Copilot**, **Antigravity**, or **OpenCode**, these skills are designed to drop right in and supercharge your AI agent.

This repository aggregates the best capabilities from across the open-source community, transforming your AI assistant into a full-stack digital agency capable of Engineering, Design, Security, Marketing, and Autonomous Operations.

## Features & Categories

The repository is organized into several key areas of expertise:

| Category                    | Skills Count | Key Skills Included                                                                                                          |
| :-------------------------- | :----------- | :--------------------------------------------------------------------------------------------------------------------------- |
| **🛸 Autonomous & Agentic** | **(13)**     | Loki Mode (Startup-in-a-box), Subagent Driven Dev, Dispatching Parallel Agents, Planning With Files, Skill Creator/Developer |
| **🔌 Integrations & APIs**  | **(35)**     | Stripe, Firebase, Supabase, Vercel, Clerk Auth, Twilio, Discord Bot, Slack Bot, GraphQL, AWS Serverless                      |
| **🛡️ Cybersecurity**        | **(32)**     | Ethical Hacking, Metasploit, Burp Suite, SQLMap, Active Directory, AWS/Cloud Pentesting, OWASP Top 100, Red Team Tools       |
| **🎨 Creative & Design**    | **(21)**     | UI/UX Pro Max, Frontend Design, Canvas, Algorithmic Art, Theme Factory, D3 Viz, Web Artifacts                                |
| **🛠️ Development**          | **(44)**     | TDD, Systematic Debugging, React Patterns, Backend/Frontend Guidelines, Senior Fullstack, Software Architecture              |
| **🏗️ Infrastructure & Git** | **(13)**     | Linux Shell Scripting, Git Worktrees, Git Pushing, Conventional Commits, File Organization, GitHub Workflow Automation       |
| **🤖 AI Agents & LLM**      | **(27)**     | Voice AI Engine, LangGraph, CrewAI, Langfuse, RAG Engineer, Prompt Engineer, Browser Automation, Agent Memory Systems        |
| **🔄 Workflow & Planning**  | **(19)**     | Writing Plans, Executing Plans, Concise Planning, Verification Before Completion, Code Review (Requesting/Receiving)         |
| **📄 Document Processing**  | **(5)**      | DOCX (Official), PDF (Official), PPTX (Official), XLSX (Official)                                                            |
| **🧪 Testing & QA**         | **(8)**      | Webapp Testing, Playwright Automation, Test Fixing, Testing Patterns                                                         |
| **📈 Product & Strategy**   | **(4)**      | Product Manager Toolkit, Content Creator, ASO, Doc Co-authoring, Brainstorming, Internal Comms                               |
| **📣 Marketing & Growth**   | **(26)**     | Page CRO, Copywriting, SEO Audit, Paid Ads, Email Sequence, Pricing Strategy, Referral Program, Launch Strategy              |
| **🚀 Maker Tools**          | **(8)**      | Micro-SaaS Launcher, Browser Extension Builder, Telegram Bot, AI Wrapper Product, Viral Generator, 3D Web Experience         |

## Curated Collections

[Check out our Starter Packs in docs/BUNDLES.md](docs/BUNDLES.md) to find the perfect toolkit for your role.

## Full Skill Registry (257/257)

> [!NOTE] > **Document Skills**: We provide both **community** and **official Anthropic** versions for DOCX, PDF, PPTX, and XLSX. Locally, the official versions are used by default (via symlinks). In the repository, both versions are available for flexibility.

| Skill Name | Risk | Description | Path |
| :--- | :--- | :--- | :--- |
| **2d-games** | ⚪ | 2D game development principles. Sprites, tilemaps, physics, camera. | `skills/game-development/2d-games` |
| **3d-games** | ⚪ | 3D game development principles. Rendering, shaders, physics, cameras. | `skills/game-development/3d-games` |
| **3d-web-experience** | ⚪ | Expert in building 3D experiences for the web - Three.js, React Three Fiber, Spline, WebGL, and interactive 3D scenes. Covers product configurators, 3D portfolios, immersive websites, and bringing depth to web experiences. Use when: 3D website, three.js, WebGL, react three fiber, 3D experience. | `skills/3d-web-experience` |
| **ab-test-setup** | ⚪ | Structured guide for setting up A/B tests with mandatory gates for hypothesis, metrics, and execution readiness. | `skills/ab-test-setup` |
| **Active Directory Attacks** | ⚪ | This skill should be used when the user asks to "attack Active Directory", "exploit AD", "Kerberoasting", "DCSync", "pass-the-hash", "BloodHound enumeration", "Golden Ticket", "Silver Ticket", "AS-REP roasting", "NTLM relay", or needs guidance on Windows domain penetration testing. | `skills/active-directory-attacks` |
| **address-github-comments** | ⚪ | Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI. | `skills/address-github-comments` |
| **agent-evaluation** | ⚪ | Testing and benchmarking LLM agents including behavioral testing, capability assessment, reliability metrics, and production monitoring—where even top agents achieve less than 50% on real-world benchmarks Use when: agent testing, agent evaluation, benchmark agents, agent reliability, test agent. | `skills/agent-evaluation` |
| **agent-manager-skill** | ⚪ | Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling. | `skills/agent-manager-skill` |
| **agent-memory-mcp** | ⚪ | A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions). | `skills/agent-memory-mcp` |
| **agent-memory-systems** | ⚪ | Memory is the cornerstone of intelligent agents. Without it, every interaction starts from zero. This skill covers the architecture of agent memory: short-term (context window), long-term (vector stores), and the cognitive architectures that organize them.  Key insight: Memory isn't just storage - it's retrieval. A million stored facts mean nothing if you can't find the right one. Chunking, embedding, and retrieval strategies determine whether your agent remembers or forgets.  The field is fragm | `skills/agent-memory-systems` |
| **agent-tool-builder** | ⚪ | Tools are how AI agents interact with the world. A well-designed tool is the difference between an agent that works and one that hallucinates, fails silently, or costs 10x more tokens than necessary.  This skill covers tool design from schema to error handling. JSON Schema best practices, description writing that actually helps the LLM, validation, and the emerging MCP standard that's becoming the lingua franca for AI tools.  Key insight: Tool descriptions are more important than tool implementa | `skills/agent-tool-builder` |
| **ai-agents-architect** | ⚪ | Expert in designing and building autonomous AI agents. Masters tool use, memory systems, planning strategies, and multi-agent orchestration. Use when: build agent, AI agent, autonomous agent, tool use, function calling. | `skills/ai-agents-architect` |
| **ai-product** | ⚪ | Every product will be AI-powered. The question is whether you'll build it right or ship a demo that falls apart in production.  This skill covers LLM integration patterns, RAG architecture, prompt engineering that scales, AI UX that users trust, and cost optimization that doesn't bankrupt you. Use when: keywords, file_patterns, code_patterns. | `skills/ai-product` |
| **ai-wrapper-product** | ⚪ | Expert in building products that wrap AI APIs (OpenAI, Anthropic, etc.) into focused tools people will pay for. Not just 'ChatGPT but different' - products that solve specific problems with AI. Covers prompt engineering for products, cost management, rate limiting, and building defensible AI businesses. Use when: AI wrapper, GPT product, AI tool, wrap AI, AI SaaS. | `skills/ai-wrapper-product` |
| **algolia-search** | ⚪ | Expert patterns for Algolia search implementation, indexing strategies, React InstantSearch, and relevance tuning Use when: adding search to, algolia, instantsearch, search api, search functionality. | `skills/algolia-search` |
| **algorithmic-art** | ⚪ | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations. | `skills/algorithmic-art` |
| **analytics-tracking** | ⚪ | Design, audit, and improve analytics tracking systems that produce reliable, decision-ready data. Use when the user wants to set up, fix, or evaluate analytics tracking (GA4, GTM, product analytics, events, conversions, UTMs). This skill focuses on measurement strategy, signal quality, and validation— not just firing events. | `skills/analytics-tracking` |
| **API Fuzzing for Bug Bounty** | ⚪ | This skill should be used when the user asks to "test API security", "fuzz APIs", "find IDOR vulnerabilities", "test REST API", "test GraphQL", "API penetration testing", "bug bounty API testing", or needs guidance on API security assessment techniques. | `skills/api-fuzzing-bug-bounty` |
| **api-documentation-generator** | ⚪ | Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices | `skills/api-documentation-generator` |
| **api-patterns** | ⚪ | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. | `skills/api-patterns` |
| **api-security-best-practices** | ⚪ | Implement secure API design patterns including authentication, authorization, input validation, rate limiting, and protection against common API vulnerabilities | `skills/api-security-best-practices` |
| **app-builder** | ⚪ | Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates agents. | `skills/app-builder` |
| **app-store-optimization** | ⚪ | Complete App Store Optimization (ASO) toolkit for researching, optimizing, and tracking mobile app performance on Apple App Store and Google Play Store | `skills/app-store-optimization` |
| **architecture** | ⚪ | Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design. | `skills/architecture` |
| **autonomous-agent-patterns** | ⚪ | Design patterns for building autonomous coding agents. Covers tool integration, permission systems, browser automation, and human-in-the-loop workflows. Use when building AI agents, designing tool APIs, implementing permission systems, or creating autonomous coding assistants. | `skills/autonomous-agent-patterns` |
| **autonomous-agents** | ⚪ | Autonomous agents are AI systems that can independently decompose goals, plan actions, execute tools, and self-correct without constant human guidance. The challenge isn't making them capable - it's making them reliable. Every extra decision multiplies failure probability.  This skill covers agent loops (ReAct, Plan-Execute), goal decomposition, reflection patterns, and production reliability. Key insight: compounding error rates kill autonomous agents. A 95% success rate per step drops to 60% b | `skills/autonomous-agents` |
| **avalonia-layout-zafiro** | ⚪ | Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing shared styles, generic components, and avoiding XAML redundancy. | `skills/avalonia-layout-zafiro` |
| **avalonia-viewmodels-zafiro** | ⚪ | Optimal ViewModel and Wizard creation patterns for Avalonia using Zafiro and ReactiveUI. | `skills/avalonia-viewmodels-zafiro` |
| **avalonia-zafiro-development** | ⚪ | Mandatory skills, conventions, and behavioral rules for Avalonia UI development using the Zafiro toolkit. | `skills/avalonia-zafiro-development` |
| **AWS Penetration Testing** | ⚪ | This skill should be used when the user asks to "pentest AWS", "test AWS security", "enumerate IAM", "exploit cloud infrastructure", "AWS privilege escalation", "S3 bucket testing", "metadata SSRF", "Lambda exploitation", or needs guidance on Amazon Web Services security assessment. | `skills/aws-penetration-testing` |
| **aws-serverless** | ⚪ | Specialized skill for building production-ready serverless applications on AWS. Covers Lambda functions, API Gateway, DynamoDB, SQS/SNS event-driven patterns, SAM/CDK deployment, and cold start optimization. | `skills/aws-serverless` |
| **azure-functions** | ⚪ | Expert patterns for Azure Functions development including isolated worker model, Durable Functions orchestration, cold start optimization, and production patterns. Covers .NET, Python, and Node.js programming models. Use when: azure function, azure functions, durable functions, azure serverless, function app. | `skills/azure-functions` |
| **backend-dev-guidelines** | ⚪ | Opinionated backend development standards for Node.js + Express + TypeScript microservices. Covers layered architecture, BaseController pattern, dependency injection, Prisma repositories, Zod validation, unifiedConfig, Sentry error tracking, async safety, and testing discipline. | `skills/backend-dev-guidelines` |
| **backend-patterns** | ⚪ | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. | `skills/cc-skill-backend-patterns` |
| **bash-linux** | ⚪ | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems. | `skills/bash-linux` |
| **behavioral-modes** | ⚪ | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type. | `skills/behavioral-modes` |
| **blockrun** | ⚪ | Use when user needs capabilities Claude lacks (image generation, real-time X/Twitter data) or explicitly requests external models ("blockrun", "use grok", "use gpt", "dall-e", "deepseek") | `skills/blockrun` |
| **brainstorming** | ⚪ | Use this skill before any creative or constructive work (features, components, architecture, behavior changes, or functionality). This skill transforms vague ideas into validated designs through disciplined, incremental reasoning and collaboration. | `skills/brainstorming` |
| **brand-guidelines** | ⚪ | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply. | `skills/brand-guidelines-anthropic` |
| **brand-guidelines** | ⚪ | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply. | `skills/brand-guidelines-community` |
| **Broken Authentication Testing** | ⚪ | This skill should be used when the user asks to "test for broken authentication vulnerabilities", "assess session management security", "perform credential stuffing tests", "evaluate password policies", "test for session fixation", or "identify authentication bypass flaws". It provides comprehensive techniques for identifying authentication and session management weaknesses in web applications. | `skills/broken-authentication` |
| **browser-automation** | ⚪ | Browser automation powers web testing, scraping, and AI agent interactions. The difference between a flaky script and a reliable system comes down to understanding selectors, waiting strategies, and anti-detection patterns.  This skill covers Playwright (recommended) and Puppeteer, with patterns for testing, scraping, and agentic browser control. Key insight: Playwright won the framework war. Unless you need Puppeteer's stealth ecosystem or are Chrome-only, Playwright is the better choice in 202 | `skills/browser-automation` |
| **browser-extension-builder** | ⚪ | Expert in building browser extensions that solve real problems - Chrome, Firefox, and cross-browser extensions. Covers extension architecture, manifest v3, content scripts, popup UIs, monetization strategies, and Chrome Web Store publishing. Use when: browser extension, chrome extension, firefox addon, extension, manifest v3. | `skills/browser-extension-builder` |
| **bullmq-specialist** | ⚪ | BullMQ expert for Redis-backed job queues, background processing, and reliable async execution in Node.js/TypeScript applications. Use when: bullmq, bull queue, redis queue, background job, job queue. | `skills/bullmq-specialist` |
| **bun-development** | ⚪ | Modern JavaScript/TypeScript development with Bun runtime. Covers package management, bundling, testing, and migration from Node.js. Use when working with Bun, optimizing JS/TS development speed, or migrating from Node.js to Bun. | `skills/bun-development` |
| **Burp Suite Web Application Testing** | ⚪ | This skill should be used when the user asks to "intercept HTTP traffic", "modify web requests", "use Burp Suite for testing", "perform web vulnerability scanning", "test with Burp Repeater", "analyze HTTP history", or "configure proxy for web testing". It provides comprehensive guidance for using Burp Suite's core features for web application security testing. | `skills/burp-suite-testing` |
| **busybox-on-windows** | ⚪ | How to use a Win32 build of BusyBox to run many of the standard UNIX command line tools on Windows. | `skills/busybox-on-windows` |
| **canvas-design** | ⚪ | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations. | `skills/canvas-design` |
| **cc-skill-continuous-learning** | ⚪ | Development skill from everything-claude-code | `skills/cc-skill-continuous-learning` |
| **cc-skill-project-guidelines-example** | ⚪ | Project Guidelines Skill (Example) | `skills/cc-skill-project-guidelines-example` |
| **cc-skill-strategic-compact** | ⚪ | Development skill from everything-claude-code | `skills/cc-skill-strategic-compact` |
| **Claude Code Guide** | ⚪ | Master guide for using Claude Code effectively. Includes configuration templates, prompting strategies "Thinking" keywords, debugging techniques, and best practices for interacting with the agent. | `skills/claude-code-guide` |
| **clean-code** | ⚪ | Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments | `skills/clean-code` |
| **clerk-auth** | ⚪ | Expert patterns for Clerk auth implementation, middleware, organizations, webhooks, and user sync Use when: adding authentication, clerk auth, user authentication, sign in, sign up. | `skills/clerk-auth` |
| **clickhouse-io** | ⚪ | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. | `skills/cc-skill-clickhouse-io` |
| **Cloud Penetration Testing** | ⚪ | This skill should be used when the user asks to "perform cloud penetration testing", "assess Azure or AWS or GCP security", "enumerate cloud resources", "exploit cloud misconfigurations", "test O365 security", "extract secrets from cloud environments", or "audit cloud infrastructure". It provides comprehensive techniques for security assessment across major cloud platforms. | `skills/cloud-penetration-testing` |
| **code-review-checklist** | ⚪ | Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability | `skills/code-review-checklist` |
| **codex-review** | ⚪ | Professional code review with auto CHANGELOG generation, integrated with Codex AI | `skills/codex-review` |
| **coding-standards** | ⚪ | Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development. | `skills/cc-skill-coding-standards` |
| **competitor-alternatives** | ⚪ | When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when the user mentions 'alternative page,' 'vs page,' 'competitor comparison,' 'comparison page,' '[Product] vs [Product],' '[Product] alternative,' or 'competitive landing pages.' Covers four formats: singular alternative, plural alternatives, you vs competitor, and competitor vs competitor. Emphasizes deep research, modular content architecture, and varied section types beyond feature tables. | `skills/competitor-alternatives` |
| **computer-use-agents** | ⚪ | Build AI agents that interact with computers like humans do - viewing screens, moving cursors, clicking buttons, and typing text. Covers Anthropic's Computer Use, OpenAI's Operator/CUA, and open-source alternatives. Critical focus on sandboxing, security, and handling the unique challenges of vision-based control. Use when: computer use, desktop automation agent, screen control AI, vision-based agent, GUI automation. | `skills/computer-use-agents` |
| **concise-planning** | ⚪ | Use when a user asks for a plan for a coding task, to generate a clear, actionable, and atomic checklist. | `skills/concise-planning` |
| **content-creator** | ⚪ | Create SEO-optimized marketing content with consistent brand voice. Includes brand voice analyzer, SEO optimizer, content frameworks, and social media templates. Use when writing blog posts, creating social media content, analyzing brand voice, optimizing SEO, planning content calendars, or when user mentions content creation, brand voice, SEO optimization, social media marketing, or content strategy. | `skills/content-creator` |
| **context-window-management** | ⚪ | Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rot Use when: context window, token limit, context management, context engineering, long context. | `skills/context-window-management` |
| **context7-auto-research** | ⚪ | Automatically fetch latest library/framework documentation for Claude Code via Context7 API | `skills/context7-auto-research` |
| **conversation-memory** | ⚪ | Persistent memory systems for LLM conversations including short-term, long-term, and entity-based memory Use when: conversation memory, remember, memory persistence, long-term memory, chat history. | `skills/conversation-memory` |
| **copy-editing** | ⚪ | When the user wants to edit, review, or improve existing marketing copy. Also use when the user mentions 'edit this copy,' 'review my copy,' 'copy feedback,' 'proofread,' 'polish this,' 'make this better,' or 'copy sweep.' This skill provides a systematic approach to editing marketing copy through multiple focused passes. | `skills/copy-editing` |
| **copywriting** | ⚪ | Use this skill when writing, rewriting, or improving marketing copy for any page (homepage, landing page, pricing, feature, product, or about page). This skill produces clear, compelling, and testable copy while enforcing alignment, honesty, and conversion best practices. | `skills/copywriting` |
| **core-components** | ⚪ | Core component library and design system patterns. Use when building UI, using design tokens, or working with the component library. | `skills/core-components` |
| **crewai** | ⚪ | Expert in CrewAI - the leading role-based multi-agent framework used by 60% of Fortune 500 companies. Covers agent design with roles and goals, task definition, crew orchestration, process types (sequential, hierarchical, parallel), memory systems, and flows for complex workflows. Essential for building collaborative AI agent teams. Use when: crewai, multi-agent team, agent roles, crew of agents, role-based agents. | `skills/crewai` |
| **Cross-Site Scripting and HTML Injection Testing** | ⚪ | This skill should be used when the user asks to "test for XSS vulnerabilities", "perform cross-site scripting attacks", "identify HTML injection flaws", "exploit client-side injection vulnerabilities", "steal cookies via XSS", or "bypass content security policies". It provides comprehensive techniques for detecting, exploiting, and understanding XSS and HTML injection attack vectors in web applications. | `skills/xss-html-injection` |
| **d3-viz** | ⚪ | Creating interactive data visualisations using d3.js. This skill should be used when creating custom charts, graphs, network diagrams, geographic visualisations, or any complex SVG-based data visualisation that requires fine-grained control over visual elements, transitions, or interactions. Use this for bespoke visualisations beyond standard charting libraries, whether in React, Vue, Svelte, vanilla JavaScript, or any other environment. | `skills/claude-d3js-skill` |
| **daily-news-report** | ⚪ | Scrapes content based on a preset URL list, filters high-quality technical information, and generates daily Markdown reports. | `skills/daily-news-report` |
| **database-design** | ⚪ | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. | `skills/database-design` |
| **deployment-procedures** | ⚪ | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts. | `skills/deployment-procedures` |
| **design-orchestration** | ⚪ | Orchestrates design workflows by routing work through brainstorming, multi-agent review, and execution readiness in the correct order. Prevents premature implementation, skipped validation, and unreviewed high-risk designs. | `skills/design-orchestration` |
| **discord-bot-architect** | ⚪ | Specialized skill for building production-ready Discord bots. Covers Discord.js (JavaScript) and Pycord (Python), gateway intents, slash commands, interactive components, rate limiting, and sharding. | `skills/discord-bot-architect` |
| **dispatching-parallel-agents** | ⚪ | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | `skills/dispatching-parallel-agents` |
| **doc-coauthoring** | ⚪ | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks. | `skills/doc-coauthoring` |
| **docker-expert** | ⚪ | Docker containerization expert with deep knowledge of multi-stage builds, image optimization, container security, Docker Compose orchestration, and production deployment patterns. Use PROACTIVELY for Dockerfile optimization, container issues, image size problems, security hardening, networking, and orchestration challenges. | `skills/docker-expert` |
| **documentation-templates** | ⚪ | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. | `skills/documentation-templates` |
| **docx** | ⚪ | Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction. When Claude needs to work with professional documents (.docx files) for: (1) Creating new documents, (2) Modifying or editing content, (3) Working with tracked changes, (4) Adding comments, or any other document tasks | `skills/docx-official` |
| **email-sequence** | ⚪ | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when the user mentions "email sequence," "drip campaign," "nurture sequence," "onboarding emails," "welcome sequence," "re-engagement emails," "email automation," or "lifecycle emails." For in-app onboarding, see onboarding-cro. | `skills/email-sequence` |
| **email-systems** | ⚪ | Email has the highest ROI of any marketing channel. $36 for every $1 spent. Yet most startups treat it as an afterthought - bulk blasts, no personalization, landing in spam folders.  This skill covers transactional email that works, marketing automation that converts, deliverability that reaches inboxes, and the infrastructure decisions that scale. Use when: keywords, file_patterns, code_patterns. | `skills/email-systems` |
| **environment-setup-guide** | ⚪ | Guide developers through setting up development environments with proper tools, dependencies, and configurations | `skills/environment-setup-guide` |
| **Ethical Hacking Methodology** | ⚪ | This skill should be used when the user asks to "learn ethical hacking", "understand penetration testing lifecycle", "perform reconnaissance", "conduct security scanning", "exploit vulnerabilities", or "write penetration test reports". It provides comprehensive ethical hacking methodology and techniques. | `skills/ethical-hacking-methodology` |
| **exa-search** | ⚪ | Semantic search, similar content discovery, and structured research using Exa API | `skills/exa-search` |
| **executing-plans** | ⚪ | Use when you have a written implementation plan to execute in a separate session with review checkpoints | `skills/executing-plans` |
| **File Path Traversal Testing** | ⚪ | This skill should be used when the user asks to "test for directory traversal", "exploit path traversal vulnerabilities", "read arbitrary files through web applications", "find LFI vulnerabilities", or "access files outside web root". It provides comprehensive file path traversal attack and testing methodologies. | `skills/file-path-traversal` |
| **file-organizer** | ⚪ | Intelligently organizes files and folders by understanding context, finding duplicates, and suggesting better organizational structures. Use when user wants to clean up directories, organize downloads, remove duplicates, or restructure projects. | `skills/file-organizer` |
| **file-uploads** | ⚪ | Expert at handling file uploads and cloud storage. Covers S3, Cloudflare R2, presigned URLs, multipart uploads, and image optimization. Knows how to handle large files without blocking. Use when: file upload, S3, R2, presigned URL, multipart. | `skills/file-uploads` |
| **finishing-a-development-branch** | ⚪ | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup | `skills/finishing-a-development-branch` |
| **firebase** | ⚪ | Firebase gives you a complete backend in minutes - auth, database, storage, functions, hosting. But the ease of setup hides real complexity. Security rules are your last line of defense, and they're often wrong. Firestore queries are limited, and you learn this after you've designed your data model.  This skill covers Firebase Authentication, Firestore, Realtime Database, Cloud Functions, Cloud Storage, and Firebase Hosting. Key insight: Firebase is optimized for read-heavy, denormalized data. I | `skills/firebase` |
| **firecrawl-scraper** | ⚪ | Deep web scraping, screenshots, PDF parsing, and website crawling using Firecrawl API | `skills/firecrawl-scraper` |
| **form-cro** | ⚪ | Optimize any form that is NOT signup or account registration — including lead capture, contact, demo request, application, survey, quote, and checkout forms. Use when the goal is to increase form completion rate, reduce friction, or improve lead quality without breaking compliance or downstream workflows. | `skills/form-cro` |
| **free-tool-strategy** | ⚪ | When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. Also use when the user mentions "engineering as marketing," "free tool," "marketing tool," "calculator," "generator," "interactive tool," "lead gen tool," "build a tool for leads," or "free resource." This skill bridges engineering and marketing — useful for founders and technical marketers. | `skills/free-tool-strategy` |
| **frontend-design** | ⚪ | Create distinctive, production-grade frontend interfaces with intentional aesthetics, high craft, and non-generic visual identity. Use when building or styling web UIs, components, pages, dashboards, or frontend applications. | `skills/frontend-design` |
| **frontend-dev-guidelines** | ⚪ | Opinionated frontend development standards for modern React + TypeScript applications. Covers Suspense-first data fetching, lazy loading, feature-based architecture, MUI v7 styling, TanStack Router, performance optimization, and strict TypeScript practices. | `skills/frontend-dev-guidelines` |
| **frontend-patterns** | ⚪ | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. | `skills/cc-skill-frontend-patterns` |
| **game-art** | ⚪ | Game art principles. Visual style selection, asset pipeline, animation workflow. | `skills/game-development/game-art` |
| **game-audio** | ⚪ | Game audio principles. Sound design, music integration, adaptive audio systems. | `skills/game-development/game-audio` |
| **game-design** | ⚪ | Game design principles. GDD structure, balancing, player psychology, progression. | `skills/game-development/game-design` |
| **game-development** | ⚪ | Game development orchestrator. Routes to platform-specific skills based on project needs. | `skills/game-development` |
| **gcp-cloud-run** | ⚪ | Specialized skill for building production-ready serverless applications on GCP. Covers Cloud Run services (containerized), Cloud Run Functions (event-driven), cold start optimization, and event-driven architecture with Pub/Sub. | `skills/gcp-cloud-run` |
| **geo-fundamentals** | ⚪ | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). | `skills/geo-fundamentals` |
| **git-pushing** | ⚪ | Stage, commit, and push git changes with conventional commit messages. Use when user wants to commit and push changes, mentions pushing to remote, or asks to save and push their work. Also activates when user says "push changes", "commit and push", "push this", "push to github", or similar git workflow requests. | `skills/git-pushing` |
| **github-workflow-automation** | ⚪ | Automate GitHub workflows with AI assistance. Includes PR reviews, issue triage, CI/CD integration, and Git operations. Use when automating GitHub workflows, setting up PR review automation, creating GitHub Actions, or triaging issues. | `skills/github-workflow-automation` |
| **graphql** | ⚪ | GraphQL gives clients exactly the data they need - no more, no less. One endpoint, typed schema, introspection. But the flexibility that makes it powerful also makes it dangerous. Without proper controls, clients can craft queries that bring down your server.  This skill covers schema design, resolvers, DataLoader for N+1 prevention, federation for microservices, and client integration with Apollo/urql. Key insight: GraphQL is a contract. The schema is the API documentation. Design it carefully. | `skills/graphql` |
| **HTML Injection Testing** | ⚪ | This skill should be used when the user asks to "test for HTML injection", "inject HTML into web pages", "perform HTML injection attacks", "deface web applications", or "test content injection vulnerabilities". It provides comprehensive HTML injection attack techniques and testing methodologies. | `skills/html-injection-testing` |
| **hubspot-integration** | ⚪ | Expert patterns for HubSpot CRM integration including OAuth authentication, CRM objects, associations, batch operations, webhooks, and custom objects. Covers Node.js and Python SDKs. Use when: hubspot, hubspot api, hubspot crm, hubspot integration, contacts api. | `skills/hubspot-integration` |
| **i18n-localization** | ⚪ | Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support. | `skills/i18n-localization` |
| **IDOR Vulnerability Testing** | ⚪ | This skill should be used when the user asks to "test for insecure direct object references," "find IDOR vulnerabilities," "exploit broken access control," "enumerate user IDs or object references," or "bypass authorization to access other users' data." It provides comprehensive guidance for detecting, exploiting, and remediating IDOR vulnerabilities in web applications. | `skills/idor-testing` |
| **Infinite Gratitude** | 🔵 | Multi-agent research skill for parallel research execution (10 agents, battle-tested with real case studies). | `skills/infinite-gratitude` |
| **inngest** | ⚪ | Inngest expert for serverless-first background jobs, event-driven workflows, and durable execution without managing queues or workers. Use when: inngest, serverless background job, event-driven workflow, step function, durable execution. | `skills/inngest` |
| **interactive-portfolio** | ⚪ | Expert in building portfolios that actually land jobs and clients - not just showing work, but creating memorable experiences. Covers developer portfolios, designer portfolios, creative portfolios, and portfolios that convert visitors into opportunities. Use when: portfolio, personal website, showcase work, developer portfolio, designer portfolio. | `skills/interactive-portfolio` |
| **internal-comms** | ⚪ | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.). | `skills/internal-comms-anthropic` |
| **internal-comms** | ⚪ | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.). | `skills/internal-comms-community` |
| **javascript-mastery** | ⚪ | Comprehensive JavaScript reference covering 33+ essential concepts every developer should know. From fundamentals like primitives and closures to advanced patterns like async/await and functional programming. Use when explaining JS concepts, debugging JavaScript issues, or teaching JavaScript fundamentals. | `skills/javascript-mastery` |
| **kaizen** | ⚪ | Guide for continuous improvement, error proofing, and standardization. Use this skill when the user wants to improve code quality, refactor, or discuss process improvements. | `skills/kaizen` |
| **langfuse** | ⚪ | Expert in Langfuse - the open-source LLM observability platform. Covers tracing, prompt management, evaluation, datasets, and integration with LangChain, LlamaIndex, and OpenAI. Essential for debugging, monitoring, and improving LLM applications in production. Use when: langfuse, llm observability, llm tracing, prompt management, llm evaluation. | `skills/langfuse` |
| **langgraph** | ⚪ | Expert in LangGraph - the production-grade framework for building stateful, multi-actor AI applications. Covers graph construction, state management, cycles and branches, persistence with checkpointers, human-in-the-loop patterns, and the ReAct agent pattern. Used in production at LinkedIn, Uber, and 400+ companies. This is LangChain's recommended approach for building agents. Use when: langgraph, langchain agent, stateful agent, agent graph, react agent. | `skills/langgraph` |
| **last30days** | ⚪ | Research a topic from the last 30 days on Reddit + X + Web, become an expert, and write copy-paste-ready prompts for the user's target tool. | `skills/last30days` |
| **launch-strategy** | ⚪ | When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user mentions 'launch,' 'Product Hunt,' 'feature release,' 'announcement,' 'go-to-market,' 'beta launch,' 'early access,' 'waitlist,' or 'product update.' This skill covers phased launches, channel strategy, and ongoing launch momentum. | `skills/launch-strategy` |
| **lint-and-validate** | ⚪ | Automatic quality control, linting, and static analysis procedures. Use after every code modification to ensure syntax correctness and project standards. Triggers onKeywords: lint, format, check, validate, types, static analysis. | `skills/lint-and-validate` |
| **Linux Privilege Escalation** | ⚪ | This skill should be used when the user asks to "escalate privileges on Linux", "find privesc vectors on Linux systems", "exploit sudo misconfigurations", "abuse SUID binaries", "exploit cron jobs for root access", "enumerate Linux systems for privilege escalation", or "gain root access from low-privilege shell". It provides comprehensive techniques for identifying and exploiting privilege escalation paths on Linux systems. | `skills/linux-privilege-escalation` |
| **Linux Production Shell Scripts** | ⚪ | This skill should be used when the user asks to "create bash scripts", "automate Linux tasks", "monitor system resources", "backup files", "manage users", or "write production shell scripts". It provides ready-to-use shell script templates for system administration. | `skills/linux-shell-scripting` |
| **llm-app-patterns** | ⚪ | Production-ready patterns for building LLM applications. Covers RAG pipelines, agent architectures, prompt IDEs, and LLMOps monitoring. Use when designing AI applications, implementing RAG, building agents, or setting up LLM observability. | `skills/llm-app-patterns` |
| **loki-mode** | ⚪ | Multi-agent autonomous startup system for Claude Code. Triggers on "Loki Mode". Orchestrates 100+ specialized agents across engineering, QA, DevOps, security, data/ML, business operations, marketing, HR, and customer success. Takes PRD to fully deployed, revenue-generating product with zero human intervention. Features Task tool for subagent dispatch, parallel code review with 3 specialized reviewers, severity-based issue triage, distributed task queue with dead letter handling, automatic deployment to cloud providers, A/B testing, customer feedback loops, incident response, circuit breakers, and self-healing. Handles rate limits via distributed state checkpoints and auto-resume with exponential backoff. Requires --dangerously-skip-permissions flag. | `skills/loki-mode` |
| **marketing-ideas** | ⚪ | Provide proven marketing strategies and growth ideas for SaaS and software products, prioritized using a marketing feasibility scoring system. | `skills/marketing-ideas` |
| **marketing-psychology** | ⚪ | Apply behavioral science and mental models to marketing decisions, prioritized using a psychological leverage and feasibility scoring system. | `skills/marketing-psychology` |
| **mcp-builder** | ⚪ | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). | `skills/mcp-builder` |
| **Metasploit Framework** | ⚪ | This skill should be used when the user asks to "use Metasploit for penetration testing", "exploit vulnerabilities with msfconsole", "create payloads with msfvenom", "perform post-exploitation", "use auxiliary modules for scanning", or "develop custom exploits". It provides comprehensive guidance for leveraging the Metasploit Framework in security assessments. | `skills/metasploit-framework` |
| **micro-saas-launcher** | ⚪ | Expert in launching small, focused SaaS products fast - the indie hacker approach to building profitable software. Covers idea validation, MVP development, pricing, launch strategies, and growing to sustainable revenue. Ship in weeks, not months. Use when: micro saas, indie hacker, small saas, side project, saas mvp. | `skills/micro-saas-launcher` |
| **mobile-design** | ⚪ | Mobile-first design and engineering doctrine for iOS and Android apps. Covers touch interaction, performance, platform conventions, offline behavior, and mobile-specific decision-making. Teaches principles and constraints, not fixed layouts. Use for React Native, Flutter, or native mobile apps. | `skills/mobile-design` |
| **mobile-games** | ⚪ | Mobile game development principles. Touch input, battery, performance, app stores. | `skills/game-development/mobile-games` |
| **moodle-external-api-development** | ⚪ | Create custom external web service APIs for Moodle LMS. Use when implementing web services for course management, user tracking, quiz operations, or custom plugin functionality. Covers parameter validation, database operations, error handling, service registration, and Moodle coding standards. | `skills/moodle-external-api-development` |
| **multi-agent-brainstorming** | ⚪ | Use this skill when a design or idea requires higher confidence, risk reduction, or formal review. This skill orchestrates a structured, sequential multi-agent design review where each agent has a strict, non-overlapping role. It prevents blind spots, false confidence, and premature convergence. | `skills/multi-agent-brainstorming` |
| **multiplayer** | ⚪ | Multiplayer game development principles. Architecture, networking, synchronization. | `skills/game-development/multiplayer` |
| **neon-postgres** | ⚪ | Expert patterns for Neon serverless Postgres, branching, connection pooling, and Prisma/Drizzle integration Use when: neon database, serverless postgres, database branching, neon postgres, postgres serverless. | `skills/neon-postgres` |
| **nestjs-expert** | ⚪ | Nest.js framework expert specializing in module architecture, dependency injection, middleware, guards, interceptors, testing with Jest/Supertest, TypeORM/Mongoose integration, and Passport.js authentication. Use PROACTIVELY for any Nest.js application issues including architecture decisions, testing strategies, performance optimization, or debugging complex dependency injection problems. If a specialized expert is a better fit, I will recommend switching and stop. | `skills/nestjs-expert` |
| **Network 101** | ⚪ | This skill should be used when the user asks to "set up a web server", "configure HTTP or HTTPS", "perform SNMP enumeration", "configure SMB shares", "test network services", or needs guidance on configuring and testing network services for penetration testing labs. | `skills/network-101` |
| **nextjs-best-practices** | ⚪ | Next.js App Router principles. Server Components, data fetching, routing patterns. | `skills/nextjs-best-practices` |
| **nextjs-supabase-auth** | ⚪ | Expert integration of Supabase Auth with Next.js App Router Use when: supabase auth next, authentication next.js, login supabase, auth middleware, protected route. | `skills/nextjs-supabase-auth` |
| **nodejs-best-practices** | ⚪ | Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying. | `skills/nodejs-best-practices` |
| **nosql-expert** | ⚪ | Expert guidance for distributed NoSQL databases (Cassandra, DynamoDB). Focuses on mental models, query-first modeling, single-table design, and avoiding hot partitions in high-scale systems. | `skills/nosql-expert` |
| **notebooklm** | ⚪ | Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automation, library management, persistent auth. Drastically reduced hallucinations through document-only responses. | `skills/notebooklm` |
| **notion-template-business** | ⚪ | Expert in building and selling Notion templates as a business - not just making templates, but building a sustainable digital product business. Covers template design, pricing, marketplaces, marketing, and scaling to real revenue. Use when: notion template, sell templates, digital product, notion business, gumroad. | `skills/notion-template-business` |
| **obsidian-clipper-template-creator** | ⚪ | Guide for creating templates for the Obsidian Web Clipper. Use when you want to create a new clipping template, understand available variables, or format clipped content. | `skills/obsidian-clipper-template-creator` |
| **onboarding-cro** | ⚪ | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also use when the user mentions "onboarding flow," "activation rate," "user activation," "first-run experience," "empty states," "onboarding checklist," "aha moment," or "new user experience." For signup/registration optimization, see signup-flow-cro. For ongoing email sequences, see email-sequence. | `skills/onboarding-cro` |
| **page-cro** | ⚪ | Analyze and optimize individual pages for conversion performance. Use when the user wants to improve conversion rates, diagnose why a page is underperforming, or increase the effectiveness of marketing pages (homepage, landing pages, pricing, feature pages, or blog posts). This skill focuses on diagnosis, prioritization, and testable recommendations— not blind optimization. | `skills/page-cro` |
| **paid-ads** | ⚪ | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. Also use when the user mentions 'PPC,' 'paid media,' 'ad copy,' 'ad creative,' 'ROAS,' 'CPA,' 'ad campaign,' 'retargeting,' or 'audience targeting.' This skill covers campaign strategy, ad creation, audience targeting, and optimization. | `skills/paid-ads` |
| **parallel-agents** | ⚪ | Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis requires multiple perspectives. | `skills/parallel-agents` |
| **paywall-upgrade-cro** | ⚪ | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions "paywall," "upgrade screen," "upgrade modal," "upsell," "feature gate," "convert free to paid," "freemium conversion," "trial expiration screen," "limit reached screen," "plan upgrade prompt," or "in-app pricing." Distinct from public pricing pages (see page-cro) — this skill focuses on in-product upgrade moments where the user has already experienced value. | `skills/paywall-upgrade-cro` |
| **pc-games** | ⚪ | PC and console game development principles. Engine selection, platform features, optimization strategies. | `skills/game-development/pc-games` |
| **pdf** | ⚪ | Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms. When Claude needs to fill in a PDF form or programmatically process, generate, or analyze PDF documents at scale. | `skills/pdf-official` |
| **Pentest Checklist** | ⚪ | This skill should be used when the user asks to "plan a penetration test", "create a security assessment checklist", "prepare for penetration testing", "define pentest scope", "follow security testing best practices", or needs a structured methodology for penetration testing engagements. | `skills/pentest-checklist` |
| **Pentest Commands** | ⚪ | This skill should be used when the user asks to "run pentest commands", "scan with nmap", "use metasploit exploits", "crack passwords with hydra or john", "scan web vulnerabilities with nikto", "enumerate networks", or needs essential penetration testing command references. | `skills/pentest-commands` |
| **performance-profiling** | ⚪ | Performance profiling principles. Measurement, analysis, and optimization techniques. | `skills/performance-profiling` |
| **personal-tool-builder** | ⚪ | Expert in building custom tools that solve your own problems first. The best products often start as personal tools - scratch your own itch, build for yourself, then discover others have the same itch. Covers rapid prototyping, local-first apps, CLI tools, scripts that grow into products, and the art of dogfooding. Use when: build a tool, personal tool, scratch my itch, solve my problem, CLI tool. | `skills/personal-tool-builder` |
| **plaid-fintech** | ⚪ | Expert patterns for Plaid API integration including Link token flows, transactions sync, identity verification, Auth for ACH, balance checks, webhook handling, and fintech compliance best practices. Use when: plaid, bank account linking, bank connection, ach, account aggregation. | `skills/plaid-fintech` |
| **plan-writing** | ⚪ | Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-step work. | `skills/plan-writing` |
| **planning-with-files** | ⚪ | Implements Manus-style file-based planning for complex tasks. Creates task_plan.md, findings.md, and progress.md. Use when starting complex multi-step tasks, research projects, or any task requiring >5 tool calls. | `skills/planning-with-files` |
| **playwright-skill** | ⚪ | Complete browser automation with Playwright. Auto-detects dev servers, writes clean test scripts to /tmp. Test pages, fill forms, take screenshots, check responsive design, validate UX, test login flows, check links, automate any browser task. Use when user wants to test websites, automate browser interactions, validate web functionality, or perform any browser-based testing. | `skills/playwright-skill` |
| **popup-cro** | ⚪ | Create and optimize popups, modals, overlays, slide-ins, and banners to increase conversions without harming user experience or brand trust. | `skills/popup-cro` |
| **powershell-windows** | ⚪ | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. | `skills/powershell-windows` |
| **pptx** | ⚪ | Presentation creation, editing, and analysis. When Claude needs to work with presentations (.pptx files) for: (1) Creating new presentations, (2) Modifying or editing content, (3) Working with layouts, (4) Adding comments or speaker notes, or any other presentation tasks | `skills/pptx-official` |
| **pricing-strategy** | ⚪ | Design pricing, packaging, and monetization strategies based on value, customer willingness to pay, and growth objectives. | `skills/pricing-strategy` |
| **prisma-expert** | ⚪ | Prisma ORM expert for schema design, migrations, query optimization, relations modeling, and database operations. Use PROACTIVELY for Prisma schema issues, migration problems, query performance, relation design, or database connection issues. | `skills/prisma-expert` |
| **Privilege Escalation Methods** | ⚪ | This skill should be used when the user asks to "escalate privileges", "get root access", "become administrator", "privesc techniques", "abuse sudo", "exploit SUID binaries", "Kerberoasting", "pass-the-ticket", "token impersonation", or needs guidance on post-exploitation privilege escalation for Linux or Windows systems. | `skills/privilege-escalation-methods` |
| **product-manager-toolkit** | ⚪ | Comprehensive toolkit for product managers including RICE prioritization, customer interview analysis, PRD templates, discovery frameworks, and go-to-market strategies. Use for feature prioritization, user research synthesis, requirement documentation, and product strategy development. | `skills/product-manager-toolkit` |
| **production-code-audit** | ⚪ | Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically transform it to production-grade, corporate-level professional quality with optimizations | `skills/production-code-audit` |
| **programmatic-seo** | ⚪ | Design and evaluate programmatic SEO strategies for creating SEO-driven pages at scale using templates and structured data. Use when the user mentions programmatic SEO, pages at scale, template pages, directory pages, location pages, comparison pages, integration pages, or keyword-pattern page generation. This skill focuses on feasibility, strategy, and page system design—not execution unless explicitly requested. | `skills/programmatic-seo` |
| **prompt-caching** | ⚪ | Caching strategies for LLM prompts including Anthropic prompt caching, response caching, and CAG (Cache Augmented Generation) Use when: prompt caching, cache prompt, response cache, cag, cache augmented. | `skills/prompt-caching` |
| **prompt-engineer** | ⚪ | Expert in designing effective prompts for LLM-powered applications. Masters prompt structure, context management, output formatting, and prompt evaluation. Use when: prompt engineering, system prompt, few-shot, chain of thought, prompt design. | `skills/prompt-engineer` |
| **prompt-engineering** | ⚪ | Expert guide on prompt engineering patterns, best practices, and optimization techniques. Use when user wants to improve prompts, learn prompting strategies, or debug agent behavior. | `skills/prompt-engineering` |
| **prompt-library** | ⚪ | Curated collection of high-quality prompts for various use cases. Includes role-based prompts, task-specific templates, and prompt refinement techniques. Use when user needs prompt templates, role-play prompts, or ready-to-use prompt examples for coding, writing, analysis, or creative tasks. | `skills/prompt-library` |
| **python-patterns** | ⚪ | Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not copying. | `skills/python-patterns` |
| **rag-engineer** | ⚪ | Expert in building Retrieval-Augmented Generation systems. Masters embedding models, vector databases, chunking strategies, and retrieval optimization for LLM applications. Use when: building RAG, vector search, embeddings, semantic search, document retrieval. | `skills/rag-engineer` |
| **rag-implementation** | ⚪ | Retrieval-Augmented Generation patterns including chunking, embeddings, vector stores, and retrieval optimization Use when: rag, retrieval augmented, vector search, embeddings, semantic search. | `skills/rag-implementation` |
| **react-patterns** | ⚪ | Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices. | `skills/react-patterns` |
| **react-ui-patterns** | ⚪ | Modern React UI patterns for loading states, error handling, and data fetching. Use when building UI components, handling async data, or managing UI states. | `skills/react-ui-patterns` |
| **receiving-code-review** | ⚪ | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation | `skills/receiving-code-review` |
| **Red Team Tools and Methodology** | ⚪ | This skill should be used when the user asks to "follow red team methodology", "perform bug bounty hunting", "automate reconnaissance", "hunt for XSS vulnerabilities", "enumerate subdomains", or needs security researcher techniques and tool configurations from top bug bounty hunters. | `skills/red-team-tools` |
| **red-team-tactics** | ⚪ | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. | `skills/red-team-tactics` |
| **referral-program** | ⚪ | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. Also use when the user mentions 'referral,' 'affiliate,' 'ambassador,' 'word of mouth,' 'viral loop,' 'refer a friend,' or 'partner program.' This skill covers program design, incentive structure, and growth optimization. | `skills/referral-program` |
| **remotion-best-practices** | ⚪ | Best practices for Remotion - Video creation in React | `skills/remotion-best-practices` |
| **requesting-code-review** | ⚪ | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | `skills/requesting-code-review` |
| **research-engineer** | ⚪ | An uncompromising Academic Research Engineer. Operates with absolute scientific rigor, objective criticism, and zero flair. Focuses on theoretical correctness, formal verification, and optimal implementation across any required technology. | `skills/research-engineer` |
| **salesforce-development** | ⚪ | Expert patterns for Salesforce platform development including Lightning Web Components (LWC), Apex triggers and classes, REST/Bulk APIs, Connected Apps, and Salesforce DX with scratch orgs and 2nd generation packages (2GP). Use when: salesforce, sfdc, apex, lwc, lightning web components. | `skills/salesforce-development` |
| **schema-markup** | ⚪ | Design, validate, and optimize schema.org structured data for eligibility, correctness, and measurable SEO impact. Use when the user wants to add, fix, audit, or scale schema markup (JSON-LD) for rich results. This skill evaluates whether schema should be implemented, what types are valid, and how to deploy safely according to Google guidelines. | `skills/schema-markup` |
| **scroll-experience** | ⚪ | Expert in building immersive scroll-driven experiences - parallax storytelling, scroll animations, interactive narratives, and cinematic web experiences. Like NY Times interactives, Apple product pages, and award-winning web experiences. Makes websites feel like experiences, not just pages. Use when: scroll animation, parallax, scroll storytelling, interactive story, cinematic website. | `skills/scroll-experience` |
| **Security Scanning Tools** | ⚪ | This skill should be used when the user asks to "perform vulnerability scanning", "scan networks for open ports", "assess web application security", "scan wireless networks", "detect malware", "check cloud security", or "evaluate system compliance". It provides comprehensive guidance on security scanning tools and methodologies. | `skills/scanning-tools` |
| **security-review** | ⚪ | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. Provides comprehensive security checklist and patterns. | `skills/cc-skill-security-review` |
| **segment-cdp** | ⚪ | Expert patterns for Segment Customer Data Platform including Analytics.js, server-side tracking, tracking plans with Protocols, identity resolution, destinations configuration, and data governance best practices. Use when: segment, analytics.js, customer data platform, cdp, tracking plan. | `skills/segment-cdp` |
| **senior-architect** | ⚪ | Comprehensive software architecture skill for designing scalable, maintainable systems using ReactJS, NextJS, NodeJS, Express, React Native, Swift, Kotlin, Flutter, Postgres, GraphQL, Go, Python. Includes architecture diagram generation, system design patterns, tech stack decision frameworks, and dependency analysis. Use when designing system architecture, making technical decisions, creating architecture diagrams, evaluating trade-offs, or defining integration patterns. | `skills/senior-architect` |
| **senior-fullstack** | ⚪ | Comprehensive fullstack development skill for building complete web applications with React, Next.js, Node.js, GraphQL, and PostgreSQL. Includes project scaffolding, code quality analysis, architecture patterns, and complete tech stack guidance. Use when building new projects, analyzing code quality, implementing design patterns, or setting up development workflows. | `skills/senior-fullstack` |
| **seo-audit** | ⚪ | Diagnose and audit SEO issues affecting crawlability, indexation, rankings, and organic performance. Use when the user asks for an SEO audit, technical SEO review, ranking diagnosis, on-page SEO review, meta tag audit, or SEO health check. This skill identifies issues and prioritizes actions but does not execute changes. For large-scale page creation, use programmatic-seo. For structured data, use schema-markup. | `skills/seo-audit` |
| **seo-fundamentals** | ⚪ | Core principles of SEO including E-E-A-T, Core Web Vitals, technical foundations, content quality, and how modern search engines evaluate pages. This skill explains *why* SEO works, not how to execute specific optimizations. | `skills/seo-fundamentals` |
| **server-management** | ⚪ | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands. | `skills/server-management` |
| **Shodan Reconnaissance and Pentesting** | ⚪ | This skill should be used when the user asks to "search for exposed devices on the internet," "perform Shodan reconnaissance," "find vulnerable services using Shodan," "scan IP ranges with Shodan," or "discover IoT devices and open ports." It provides comprehensive guidance for using Shodan's search engine, CLI, and API for penetration testing reconnaissance. | `skills/shodan-reconnaissance` |
| **shopify-apps** | ⚪ | Expert patterns for Shopify app development including Remix/React Router apps, embedded apps with App Bridge, webhook handling, GraphQL Admin API, Polaris components, billing, and app extensions. Use when: shopify app, shopify, embedded app, polaris, app bridge. | `skills/shopify-apps` |
| **shopify-development** | ⚪ | Build Shopify apps, extensions, themes using GraphQL Admin API, Shopify CLI, Polaris UI, and Liquid. TRIGGER: "shopify", "shopify app", "checkout extension", "admin extension", "POS extension", "shopify theme", "liquid template", "polaris", "shopify graphql", "shopify webhook", "shopify billing", "app subscription", "metafields", "shopify functions" | `skills/shopify-development` |
| **signup-flow-cro** | ⚪ | When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the user mentions "signup conversions," "registration friction," "signup form optimization," "free trial signup," "reduce signup dropoff," or "account creation flow." For post-signup onboarding, see onboarding-cro. For lead capture forms (not account creation), see form-cro. | `skills/signup-flow-cro` |
| **skill-creator** | ⚪ | Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. | `skills/skill-creator` |
| **skill-developer** | ⚪ | Create and manage Claude Code skills following Anthropic best practices. Use when creating new skills, modifying skill-rules.json, understanding trigger patterns, working with hooks, debugging skill activation, or implementing progressive disclosure. Covers skill structure, YAML frontmatter, trigger types (keywords, intent patterns, file paths, content patterns), enforcement levels (block, suggest, warn), hook mechanisms (UserPromptSubmit, PreToolUse), session tracking, and the 500-line rule. | `skills/skill-developer` |
| **slack-bot-builder** | ⚪ | Build Slack apps using the Bolt framework across Python, JavaScript, and Java. Covers Block Kit for rich UIs, interactive components, slash commands, event handling, OAuth installation flows, and Workflow Builder integration. Focus on best practices for production-ready Slack apps. Use when: slack bot, slack app, bolt framework, block kit, slash command. | `skills/slack-bot-builder` |
| **slack-gif-creator** | ⚪ | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack." | `skills/slack-gif-creator` |
| **SMTP Penetration Testing** | ⚪ | This skill should be used when the user asks to "perform SMTP penetration testing", "enumerate email users", "test for open mail relays", "grab SMTP banners", "brute force email credentials", or "assess mail server security". It provides comprehensive techniques for testing SMTP server security. | `skills/smtp-penetration-testing` |
| **social-content** | ⚪ | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or other platforms. Also use when the user mentions 'LinkedIn post,' 'Twitter thread,' 'social media,' 'content calendar,' 'social scheduling,' 'engagement,' or 'viral content.' This skill covers content creation, repurposing, and platform-specific strategies. | `skills/social-content` |
| **software-architecture** | ⚪ | Guide for quality focused software architecture. This skill should be used when users want to write code, design architecture, analyze code, in any case that relates to software development. | `skills/software-architecture` |
| **SQL Injection Testing** | ⚪ | This skill should be used when the user asks to "test for SQL injection vulnerabilities", "perform SQLi attacks", "bypass authentication using SQL injection", "extract database information through injection", "detect SQL injection flaws", or "exploit database query vulnerabilities". It provides comprehensive techniques for identifying, exploiting, and understanding SQL injection attack vectors across different database systems. | `skills/sql-injection-testing` |
| **SQLMap Database Penetration Testing** | ⚪ | This skill should be used when the user asks to "automate SQL injection testing," "enumerate database structure," "extract database credentials using sqlmap," "dump tables and columns from a vulnerable database," or "perform automated database penetration testing." It provides comprehensive guidance for using SQLMap to detect and exploit SQL injection vulnerabilities. | `skills/sqlmap-database-pentesting` |
| **SSH Penetration Testing** | ⚪ | This skill should be used when the user asks to "pentest SSH services", "enumerate SSH configurations", "brute force SSH credentials", "exploit SSH vulnerabilities", "perform SSH tunneling", or "audit SSH security". It provides comprehensive SSH penetration testing methodologies and techniques. | `skills/ssh-penetration-testing` |
| **stripe-integration** | ⚪ | Get paid from day one. Payments, subscriptions, billing portal, webhooks, metered billing, Stripe Connect. The complete guide to implementing Stripe correctly, including all the edge cases that will bite you at 3am.  This isn't just API calls - it's the full payment system: handling failures, managing subscriptions, dealing with dunning, and keeping revenue flowing. Use when: stripe, payments, subscription, billing, checkout. | `skills/stripe-integration` |
| **subagent-driven-development** | ⚪ | Use when executing implementation plans with independent tasks in the current session | `skills/subagent-driven-development` |
| **supabase-postgres-best-practices** | ⚪ | Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configurations. | `skills/postgres-best-practices` |
| **systematic-debugging** | ⚪ | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | `skills/systematic-debugging` |
| **tailwind-patterns** | ⚪ | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. | `skills/tailwind-patterns` |
| **tavily-web** | ⚪ | Web search, content extraction, crawling, and research capabilities using Tavily API | `skills/tavily-web` |
| **tdd-workflow** | ⚪ | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. | `skills/tdd-workflow` |
| **telegram-bot-builder** | ⚪ | Expert in building Telegram bots that solve real problems - from simple automation to complex AI-powered bots. Covers bot architecture, the Telegram Bot API, user experience, monetization strategies, and scaling bots to thousands of users. Use when: telegram bot, bot api, telegram automation, chat bot telegram, tg bot. | `skills/telegram-bot-builder` |
| **telegram-mini-app** | ⚪ | Expert in building Telegram Mini Apps (TWA) - web apps that run inside Telegram with native-like experience. Covers the TON ecosystem, Telegram Web App API, payments, user authentication, and building viral mini apps that monetize. Use when: telegram mini app, TWA, telegram web app, TON app, mini app. | `skills/telegram-mini-app` |
| **templates** | ⚪ | Project scaffolding templates for new applications. Use when creating new projects from scratch. Contains 12 templates for various tech stacks. | `skills/app-builder/templates` |
| **test-driven-development** | ⚪ | Use when implementing any feature or bugfix, before writing implementation code | `skills/test-driven-development` |
| **test-fixing** | ⚪ | Run tests and systematically fix all failing tests using smart error grouping. Use when user asks to fix failing tests, mentions test failures, runs test suite and failures occur, or requests to make tests pass. | `skills/test-fixing` |
| **testing-patterns** | ⚪ | Jest testing patterns, factory functions, mocking strategies, and TDD workflow. Use when writing unit tests, creating test factories, or following TDD red-green-refactor cycle. | `skills/testing-patterns` |
| **theme-factory** | ⚪ | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly. | `skills/theme-factory` |
| **Top 100 Web Vulnerabilities Reference** | ⚪ | This skill should be used when the user asks to "identify web application vulnerabilities", "explain common security flaws", "understand vulnerability categories", "learn about injection attacks", "review access control weaknesses", "analyze API security issues", "assess security misconfigurations", "understand client-side vulnerabilities", "examine mobile and IoT security flaws", or "reference the OWASP-aligned vulnerability taxonomy". Use this skill to provide comprehensive vulnerability definitions, root causes, impacts, and mitigation strategies across all major web security categories. | `skills/top-web-vulnerabilities` |
| **trigger-dev** | ⚪ | Trigger.dev expert for background jobs, AI workflows, and reliable async execution with excellent developer experience and TypeScript-first design. Use when: trigger.dev, trigger dev, background task, ai background job, long running task. | `skills/trigger-dev` |
| **twilio-communications** | ⚪ | Build communication features with Twilio: SMS messaging, voice calls, WhatsApp Business API, and user verification (2FA). Covers the full spectrum from simple notifications to complex IVR systems and multi-channel authentication. Critical focus on compliance, rate limits, and error handling. Use when: twilio, send SMS, text message, voice call, phone verification. | `skills/twilio-communications` |
| **typescript-expert** | ⚪ | TypeScript and JavaScript expert with deep knowledge of type-level programming, performance optimization, monorepo management, migration strategies, and modern tooling. Use PROACTIVELY for any TypeScript/JavaScript issues including complex type gymnastics, build performance, debugging, and architectural decisions. If a specialized expert is a better fit, I will recommend switching and stop. | `skills/typescript-expert` |
| **ui-ux-pro-max** | ⚪ | UI/UX design intelligence. 50 styles, 21 palettes, 50 font pairings, 20 charts, 9 stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui). Actions: plan, build, create, design, implement, review, fix, improve, optimize, enhance, refactor, check UI/UX code. Projects: website, landing page, dashboard, admin panel, e-commerce, SaaS, portfolio, blog, mobile app, .html, .tsx, .vue, .svelte. Elements: button, modal, navbar, sidebar, card, table, form, chart. Styles: glassmorphism, claymorphism, minimalism, brutalism, neumorphism, bento grid, dark mode, responsive, skeuomorphism, flat design. Topics: color palette, accessibility, animation, layout, typography, font pairing, spacing, hover, shadow, gradient. Integrations: shadcn/ui MCP for component search and examples. | `skills/ui-ux-pro-max` |
| **upstash-qstash** | ⚪ | Upstash QStash expert for serverless message queues, scheduled jobs, and reliable HTTP-based task delivery without managing infrastructure. Use when: qstash, upstash queue, serverless cron, scheduled http, message queue serverless. | `skills/upstash-qstash` |
| **using-git-worktrees** | ⚪ | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection and safety verification | `skills/using-git-worktrees` |
| **using-superpowers** | ⚪ | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions | `skills/using-superpowers` |
| **vercel-deployment** | ⚪ | Expert knowledge for deploying to Vercel with Next.js Use when: vercel, deploy, deployment, hosting, production. | `skills/vercel-deployment` |
| **vercel-react-best-practices** | ⚪ | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements. | `skills/react-best-practices` |
| **verification-before-completion** | ⚪ | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always | `skills/verification-before-completion` |
| **viral-generator-builder** | ⚪ | Expert in building shareable generator tools that go viral - name generators, quiz makers, avatar creators, personality tests, and calculator tools. Covers the psychology of sharing, viral mechanics, and building tools people can't resist sharing with friends. Use when: generator tool, quiz maker, name generator, avatar creator, viral tool. | `skills/viral-generator-builder` |
| **voice-agents** | ⚪ | Voice agents represent the frontier of AI interaction - humans speaking naturally with AI systems. The challenge isn't just speech recognition and synthesis, it's achieving natural conversation flow with sub-800ms latency while handling interruptions, background noise, and emotional nuance.  This skill covers two architectures: speech-to-speech (OpenAI Realtime API, lowest latency, most natural) and pipeline (STT→LLM→TTS, more control, easier to debug). Key insight: latency is the constraint. Hu | `skills/voice-agents` |
| **voice-ai-development** | ⚪ | Expert in building voice AI applications - from real-time voice agents to voice-enabled apps. Covers OpenAI Realtime API, Vapi for voice agents, Deepgram for transcription, ElevenLabs for synthesis, LiveKit for real-time infrastructure, and WebRTC fundamentals. Knows how to build low-latency, production-ready voice experiences. Use when: voice ai, voice agent, speech to text, text to speech, realtime voice. | `skills/voice-ai-development` |
| **voice-ai-engine-development** | ⚪ | Build real-time conversational AI voice engines using async worker pipelines, streaming transcription, LLM agents, and TTS synthesis with interrupt handling and multi-provider support | `skills/voice-ai-engine-development` |
| **vr-ar** | ⚪ | VR/AR development principles. Comfort, interaction, performance requirements. | `skills/game-development/vr-ar` |
| **vulnerability-scanner** | ⚪ | Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization. | `skills/vulnerability-scanner` |
| **web-artifacts-builder** | ⚪ | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts. | `skills/web-artifacts-builder` |
| **web-design-guidelines** | ⚪ | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices". | `skills/web-design-guidelines` |
| **web-games** | ⚪ | Web browser game development principles. Framework selection, WebGPU, optimization, PWA. | `skills/game-development/web-games` |
| **web-performance-optimization** | ⚪ | Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance | `skills/web-performance-optimization` |
| **webapp-testing** | ⚪ | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs. | `skills/webapp-testing` |
| **Windows Privilege Escalation** | ⚪ | This skill should be used when the user asks to "escalate privileges on Windows," "find Windows privesc vectors," "enumerate Windows for privilege escalation," "exploit Windows misconfigurations," or "perform post-exploitation privilege escalation." It provides comprehensive guidance for discovering and exploiting privilege escalation vulnerabilities in Windows environments. | `skills/windows-privilege-escalation` |
| **Wireshark Network Traffic Analysis** | ⚪ | This skill should be used when the user asks to "analyze network traffic with Wireshark", "capture packets for troubleshooting", "filter PCAP files", "follow TCP/UDP streams", "detect network anomalies", "investigate suspicious traffic", or "perform protocol analysis". It provides comprehensive techniques for network packet capture, filtering, and analysis using Wireshark. | `skills/wireshark-analysis` |
| **WordPress Penetration Testing** | ⚪ | This skill should be used when the user asks to "pentest WordPress sites", "scan WordPress for vulnerabilities", "enumerate WordPress users, themes, or plugins", "exploit WordPress vulnerabilities", or "use WPScan". It provides comprehensive WordPress security assessment methodologies. | `skills/wordpress-penetration-testing` |
| **workflow-automation** | ⚪ | Workflow automation is the infrastructure that makes AI agents reliable. Without durable execution, a network hiccup during a 10-step payment flow means lost money and angry customers. With it, workflows resume exactly where they left off.  This skill covers the platforms (n8n, Temporal, Inngest) and patterns (sequential, parallel, orchestrator-worker) that turn brittle scripts into production-grade automation.  Key insight: The platforms make different tradeoffs. n8n optimizes for accessibility | `skills/workflow-automation` |
| **writing-plans** | ⚪ | Use when you have a spec or requirements for a multi-step task, before touching code | `skills/writing-plans` |
| **writing-skills** | ⚪ | Use when creating new skills, editing existing skills, or verifying skills work before deployment | `skills/writing-skills` |
| **xlsx** | ⚪ | Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization. When Claude needs to work with spreadsheets (.xlsx, .xlsm, .csv, .tsv, etc) for: (1) Creating new spreadsheets with formulas and formatting, (2) Reading or analyzing data, (3) Modify existing spreadsheets while preserving formulas, (4) Data analysis and visualization in spreadsheets, or (5) Recalculating formulas | `skills/xlsx-official` |
| **zapier-make-patterns** | ⚪ | No-code automation democratizes workflow building. Zapier and Make (formerly Integromat) let non-developers automate business processes without writing code. But no-code doesn't mean no-complexity - these platforms have their own patterns, pitfalls, and breaking points.  This skill covers when to use which platform, how to build reliable automations, and when to graduate to code-based solutions. Key insight: Zapier optimizes for simplicity and integrations (7000+ apps), Make optimizes for power | `skills/zapier-make-patterns` |

## Installation

To use these skills with **Claude Code**, **Gemini CLI**, **Codex CLI**, **Cursor**, **Antigravity**, or **OpenCode**, clone this repository into your agent's skills directory:

```bash
# Universal installation (works with most tools)
git clone https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills

# Claude Code specific
git clone https://github.com/sickn33/antigravity-awesome-skills.git .claude/skills

# Gemini CLI specific
git clone https://github.com/sickn33/antigravity-awesome-skills.git .gemini/skills

# Cursor specific
git clone https://github.com/sickn33/antigravity-awesome-skills.git .cursor/skills
```

---

## How to Contribute

We welcome contributions from the community! To add a new skill:

1. **Fork** the repository.
2. **Create a new directory** inside `skills/` for your skill.
3. **Add a `SKILL.md`** with the required frontmatter (name and description).
4. **Run validation**: `python3 scripts/validate_skills.py`.
5. **Submit a Pull Request**.

Please ensure your skill follows the Antigravity/Claude Code best practices.

---

## Credits & Sources

We stand on the shoulders of giants.

👉 **[View the Full Attribution Ledger](docs/SOURCES.md)**

Key contributors and sources include:

- **HackTricks**
- **OWASP**
- **Anthropic / OpenAI / Google**
- **The Open Source Community**

This collection would not be possible without the incredible work of the Claude Code community and official sources:

### Official Sources

- **[anthropics/skills](https://github.com/anthropics/skills)**: Official Anthropic skills repository - Document manipulation (DOCX, PDF, PPTX, XLSX), Brand Guidelines, Internal Communications.
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)**: Official notebooks and recipes for building with Claude.
- **[remotion-dev/skills](https://github.com/remotion-dev/skills)**: Official Remotion skills - Video creation in React with 28 modular rules.
- **[vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)**: Vercel Labs official skills - React Best Practices, Web Design Guidelines.
- **[openai/skills](https://github.com/openai/skills)**: OpenAI Codex skills catalog - Agent skills, Skill Creator, Concise Planning.
- **[supabase/agent-skills](https://github.com/supabase/agent-skills)**: Supabase official skills - Postgres Best Practices.

### Community Contributors

- **[obra/superpowers](https://github.com/obra/superpowers)**: The original "Superpowers" by Jesse Vincent.
- **[guanyang/antigravity-skills](https://github.com/guanyang/antigravity-skills)**: Core Antigravity extensions.
- **[diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase)**: Infrastructure and Backend/Frontend Guidelines.
- **[ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase)**: React UI patterns and Design Systems.
- **[travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)**: Loki Mode and Playwright integration.
- **[zebbern/claude-code-guide](https://github.com/zebbern/claude-code-guide)**: Comprehensive Security suite & Guide (Source for ~60 new skills).
- **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)**: Senior Engineering and PM toolkit.
- **[karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills)**: A massive list of verified skills for Claude Code.
- **[zircote/.claude](https://github.com/zircote/.claude)**: Shopify development skill reference.
- **[vibeforge1111/vibeship-spawner-skills](https://github.com/vibeforge1111/vibeship-spawner-skills)**: AI Agents, Integrations, Maker Tools (57 skills, Apache 2.0).
- **[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**: Marketing skills for CRO, copywriting, SEO, paid ads, and growth (23 skills, MIT).
- **[vudovn/antigravity-kit](https://github.com/vudovn/antigravity-kit)**: AI Agent templates with Skills, Agents, and Workflows (33 skills, MIT).
- **[affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)**: Complete Claude Code configuration collection from Anthropic hackathon winner - skills only (8 skills, MIT).
- **[webzler/agentMemory](https://github.com/webzler/agentMemory)**: Source for the agent-memory-mcp skill.
- **[sstklen/claude-api-cost-optimization](https://github.com/sstklen/claude-api-cost-optimization)**: Save 50-90% on Claude API costs with smart optimization strategies (MIT).

### Inspirations

- **[f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)**: Inspiration for the Prompt Library.
- **[leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts)**: Inspiration for JavaScript Mastery.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

## Community

- [Community Guidelines](docs/COMMUNITY_GUIDELINES.md)
- [Security Policy](docs/SECURITY_GUARDRAILS.md)

---

---

## GitHub Topics

For repository maintainers, add these topics to maximize discoverability:

```text
claude-code, gemini-cli, codex-cli, antigravity, cursor, github-copilot, opencode,
agentic-skills, ai-coding, llm-tools, ai-agents, autonomous-coding, mcp,
ai-developer-tools, ai-pair-programming, vibe-coding, skill, skills, SKILL.md, rules.md, CLAUDE.md, GEMINI.md, CURSOR.md
```

---

## Repo Contributors

We officially thank the following contributors for their help in making this repository awesome!

- [mvanhorn](https://github.com/mvanhorn)
- [rookie-ricardo](https://github.com/rookie-ricardo)
- [sck_0](https://github.com/sck_0)
- [Munir Abbasi](https://github.com/munirabbasi)
- [Mohammad Faiz](https://github.com/mohdfaiz2k9)
- [Ianj332](https://github.com/Ianj332)
- [sickn33](https://github.com/sickn33)
- [GuppyTheCat](https://github.com/GuppyTheCat)
- [Tiger-Foxx](https://github.com/Tiger-Foxx)
- [arathiesh](https://github.com/arathiesh)
- [1bcMax](https://github.com/1bcMax)
- [Ahmed Rehan](https://github.com/ar27111994)
- [BenedictKing](https://github.com/BenedictKing)
- [Nguyen Huu Loc](https://github.com/LocNguyenSGU)
- [Owen Wu](https://github.com/yubing744)
- [SuperJMN](https://github.com/SuperJMN)
- [Viktor Ferenczi](https://github.com/viktor-ferenczi)
- [krisnasantosa15](https://github.com/krisnasantosa15)
- [raeef1001](https://github.com/raeef1001)
- [taksrules](https://github.com/taksrules)
- [zebbern](https://github.com/zebbern)
- [Đỗ Khắc Gia Khoa](https://github.com/dokhacgiakhoa)
- [vuth-dogo](https://github.com/vuth-dogo)
- [sstklen](https://github.com/sstklen)
- [truongnmt](https://github.com/truongnmt)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sickn33/antigravity-awesome-skills&type=date&legend=top-left)](https://www.star-history.com/#sickn33/antigravity-awesome-skills&type=date&legend=top-left)
