# How Claude Code Works Remotely

Claude Code provides multiple ways to work remotely, letting you write code, run commands, and debug applications from anywhere.

## Remote Development Options

### 1. Claude Code on the Web (Cloud VMs)

Runs Claude Code on Anthropic-managed virtual machines in the cloud.

**How it works:**

1. Visit [claude.ai/code](https://claude.ai/code) or use the mobile app
2. Connect your GitHub account and install the Claude GitHub app
3. Submit a coding task (e.g., "Fix the authentication bug in login.py")
4. Claude clones your repo to a cloud VM, analyzes the code, makes changes, and runs tests
5. Review the diff and create a PR when satisfied

**Key features:**

- Tasks run asynchronously — close your browser and come back later
- Run multiple tasks in parallel across different repos
- Pre-installed tools: Python, Node.js, Go, Rust, Java, Ruby, PHP, PostgreSQL, Redis, and more
- Configurable network access (limited allowlist by default, full, or no internet)
- Works from any browser or the mobile app (iOS/Android)

**Best for:** Parallel bug fixes, long-running refactors, working from mobile, cloud-only repos.

### 2. Remote Control (Local Session via Web/Mobile)

Extends a local Claude Code terminal session to your browser or phone while keeping execution on your machine.

**How to use:**

```bash
# Start a new Remote Control session
claude remote-control

# Or convert an existing session
/remote-control
```

Then open the provided URL or scan the QR code from your phone.

**Key features:**

- Full access to your local filesystem, MCP servers, and tools
- Automatic reconnection if interrupted
- Works across multiple devices simultaneously
- No inbound ports opened on your machine — outbound HTTPS only

**Best for:** Continuing local work from another device, surviving network interruptions, using full local environment remotely.

### 3. SSH Sessions

Run Claude Code directly on a remote machine via SSH.

**How to use:**

```bash
# From CLI
claude --ssh user@hostname
claude --ssh user@hostname:2222  # custom port
```

Or in the Desktop app: click the environment dropdown, select **+ Add SSH connection**, and provide the host details.

**Key features:**

- Works with cloud VMs, dev containers, or your own servers
- Full access to the remote machine's environment
- Permission modes and MCP servers work the same as local

**Best for:** Specific hardware requirements, shared team servers, CI/CD debugging.

## Comparison Table

| Feature | Web Sessions | Remote Control | SSH Sessions |
|---------|-------------|----------------|--------------|
| **Execution location** | Cloud VM | Local machine | Remote machine |
| **Terminal must stay open** | No | Yes | No |
| **Access to local tools** | No | Yes | Yes (remote) |
| **Multiple parallel tasks** | Yes | No | No |
| **Mobile/browser access** | Yes | Yes | No |
| **Setup complexity** | Low | Low | Medium |

## Setting Up for Remote Sessions

### SessionStart Hooks

Install dependencies automatically when a remote session starts by adding a hook to `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/setup.sh"
          }
        ]
      }
    ]
  }
}
```

Example `scripts/setup.sh`:

```bash
#!/bin/bash
# Only run in remote environments
if [ "$CLAUDE_CODE_REMOTE" != "true" ]; then
  exit 0
fi

npm install
pip install -r requirements.txt
exit 0
```

### CLAUDE.md for Context

Add a `CLAUDE.md` file to your repo so Claude understands your project in remote sessions:

```markdown
# Project Setup
- Run `npm install` for dependencies
- Tests: `npm test`
- Lint: `npm run lint`
```

### Network Access (Web Sessions)

By default, web sessions have access to common development domains:

- **Version control:** GitHub, GitLab, Bitbucket
- **Package managers:** npm, PyPI, RubyGems, crates.io, Maven
- **Cloud platforms:** AWS, Azure, Google Cloud

Configure custom network access when creating or editing your cloud environment.

## Security

- **Web sessions:** Isolated VMs, scoped git credentials via secure proxy, HTTPS proxy for outbound traffic
- **Remote Control:** No inbound ports, outbound HTTPS only, TLS encryption, short-lived credentials
- **SSH:** Standard SSH security, Claude runs natively on remote machine

**Best practices:**
- Don't commit secrets to repositories — use environment variables
- Limit network access to required domains
- Review SessionStart hooks for security implications

## Further Reading

- [Claude Code on the Web](https://docs.anthropic.com/en/docs/claude-code/claude-code-on-the-web)
- [Remote Control](https://docs.anthropic.com/en/docs/claude-code/remote-control)
- [Desktop SSH Sessions](https://docs.anthropic.com/en/docs/claude-code/desktop)
- [Security](https://docs.anthropic.com/en/docs/claude-code/security)
