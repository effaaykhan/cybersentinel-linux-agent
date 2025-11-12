# CyberSentinel DLP - Linux Agent Installation Guide

## Quick Start

### Step 1: Install Python Dependencies

```bash
cd cybersentinel-linux-agent
pip3 install -r requirements.txt
```

If you get permission errors:
```bash
pip3 install --user -r requirements.txt
```

### Step 2: Configure the Agent

Edit `agent_config.json`:

```bash
nano agent_config.json
```

Update these important fields:
- `server_url`: Your server IP (e.g., `http://172.23.19.78:8000/api/v1`)
- `agent_id`: Unique ID for this agent (e.g., `LINUX-001`)
- `agent_name`: Name to identify this machine
- `monitored_paths`: Directories to monitor (e.g., `["/home/user/documents"]`)

Example configuration:
```json
{
  "server_url": "http://172.23.19.78:8000/api/v1",
  "agent_id": "LINUX-001",
  "agent_name": "My-Linux-Server",
  "monitored_paths": ["/home/user/documents"]
}
```

### Step 3: Run the Agent

```bash
python3 run_agent.py
```

The agent will start monitoring and send events to the server. Check the log file:
```bash
cat cybersentinel_agent.log
```

## Common Issues

### Issue: "ModuleNotFoundError"
**Fix:** Install dependencies:
```bash
pip3 install requests watchdog python-dateutil
```

### Issue: "Permission denied" when installing
**Fix:** Use `--user` flag:
```bash
pip3 install --user -r requirements.txt
```

### Issue: Agent can't connect to server
**Fix:** 
1. Check server URL in `agent_config.json`
2. Test connectivity: `curl http://YOUR-SERVER-IP:8000/api/v1/agents/`
3. Check firewall: `sudo ufw allow 8000/tcp`

### Issue: No events detected
**Fix:**
1. Verify monitored paths exist: `ls -la /path/to/monitor`
2. Create a test file in monitored directory
3. Check logs: `tail -f cybersentinel_agent.log`

## Running as Background Service (Optional)

To run the agent as a systemd service:

1. Create service file `/etc/systemd/system/cybersentinel-agent.service`:
```ini
[Unit]
Description=CyberSentinel DLP Agent
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /path/to/cybersentinel-linux-agent/run_agent.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

2. Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable cybersentinel-agent
sudo systemctl start cybersentinel-agent
sudo systemctl status cybersentinel-agent
```

3. View logs:
```bash
sudo journalctl -u cybersentinel-agent -f
```

## Verification

After installation:
- [ ] Agent is running (check with `ps aux | grep python`)
- [ ] Agent appears in dashboard
- [ ] Logs show "Agent registered successfully"
- [ ] Test file creation triggers an event in dashboard

