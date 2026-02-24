# mycrab-mcp

MCP server for [mycrab.space](https://mycrab.space) — instant public HTTPS URLs via Cloudflare Tunnels for AI agents.

## Install

```bash
uvx mycrab-mcp
```

## Claude Desktop config

Add to `~/.claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mycrab": {
      "command": "uvx",
      "args": ["mycrab-mcp"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `check_domain` | Check if a subdomain is available on mycrab.space |
| `setup_free_tunnel` | Get the command for a free tunnel (auto subdomain, expires 61 min) |
| `buy_domain_sol` | Reserve a permanent subdomain after paying 0.05 SOL on Solana mainnet |
| `get_skill_docs` | Fetch the full SKILL.md — all templates, commands, and advanced usage |

## Usage

After install, agents have native mycrab tools in every session:

```
# Check availability
check_domain("mybot")

# Free throwaway tunnel — live in <60 seconds
setup_free_tunnel()
# → "curl -s https://mycrab.space/agent-setup-auto.sh | bash"

# Permanent custom subdomain (autonomous x402 flow)
buy_domain_sol("mybot", "<solana_tx_signature>")
# → {"setup_token": "...", "setup_command": "..."}
```

## Links

- Site: https://mycrab.space
- Docs: https://mycrab.space/SKILL.md
- PyPI: https://pypi.org/project/mycrab-mcp/
- GitHub: https://github.com/isgudtek/mycrab-mcp
