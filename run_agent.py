#!/usr/bin/env python3
"""
Wrapper script to run the Linux agent with local config and log file
"""
import os
import sys
import logging

# Set up logging to use local log file instead of /var/log BEFORE importing agent
log_file = os.path.join(os.path.dirname(__file__), 'cybersentinel_agent.log')

# Remove any existing handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Configure logging with local file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ],
    force=True  # Override any existing config
)

# Now import agent - it will try to set up logging but our config is already set
import agent
# Override the logger in agent module to use our handler
agent.logger = logging.getLogger('CyberSentinelAgent')

# Import DLPAgent
from agent import DLPAgent

if __name__ == "__main__":
    # Use local config file
    config_path = os.path.join(os.path.dirname(__file__), 'agent_config.json')
    print(f"Using config: {config_path}")
    print(f"Log file: {log_file}")
    print()
    
    agent = DLPAgent(config_path=config_path)
    agent.start()

