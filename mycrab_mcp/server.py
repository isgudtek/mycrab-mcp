from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP(
    "mycrab",
    instructions="mycrab.space gives agents instant public HTTPS URLs via Cloudflare Tunnels. Use check_domain first, then setup_free_tunnel for a throwaway URL, or buy_domain_sol for a permanent custom subdomain."
)

API = "https://api.mycrab.space"

@mcp.tool()
def check_domain(subdomain: str) -> dict:
    """Check if a subdomain is available on mycrab.space."""
    r = httpx.post(f"{API}/check-domain", json={"subdomain": subdomain}, timeout=10)
    return r.json()

@mcp.tool()
def setup_free_tunnel() -> str:
    """Get the command to set up a free mycrab tunnel. Auto-generated subdomain (e.g. agent-123456.mycrab.space), live in under 60 seconds, expires after 61 minutes."""
    return "curl -s https://mycrab.space/agent-setup-auto.sh | bash"

@mcp.tool()
def buy_domain_sol(subdomain: str, tx_signature: str) -> dict:
    """Reserve a permanent custom subdomain after paying 0.05 SOL to PEPESwRv3gWQGi2RwhXeQ2TeSZPx7NBdu8eGhFP1SVL on Solana mainnet. Returns setup_token and setup_command on success."""
    r = httpx.post(f"{API}/verify-sol-payment",
                   json={"subdomain": subdomain, "tx_signature": tx_signature}, timeout=15)
    return r.json()

@mcp.tool()
def get_skill_docs() -> str:
    """Fetch the full mycrab SKILL.md — all templates, commands, persistence, tunnel management, and advanced usage."""
    r = httpx.get("https://mycrab.space/SKILL.md", timeout=10)
    return r.text

def main():
    mcp.run()

if __name__ == "__main__":
    main()
