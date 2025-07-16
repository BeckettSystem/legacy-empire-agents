
# Beckett Core Docker Bundle

## Services Deployed:
- n8n (port 5678)
- Redis (port 6379)
- MCP Dispatcher (port 8000)

## Setup Instructions:
1. SSH into your server.
2. Upload this ZIP using SCP or SFTP.
3. Unzip it: `unzip beckett_core_docker_bundle.zip`
4. `cd beckett_core_docker`
5. Run: `docker compose up -d`
6. Visit `http://your_droplet_ip:5678` to access n8n.
