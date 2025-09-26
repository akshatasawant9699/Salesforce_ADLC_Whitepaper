#!/usr/bin/env python3
"""
Deploy Agent to Salesforce
This script deploys the agent created in the notebook to your Salesforce org.
"""

import json
import os
from datetime import datetime

def deploy_agent():
    print("=== Agent Deployment Script ===")
    print("Deploying agent to Salesforce org...")
    
    # Load agent specification
    with open('agent_spec.json', 'r') as f:
        agent_spec = json.load(f)
    
    print(f"Agent: {agent_spec['name']}")
    print(f"Company: {agent_spec['company_name']}")
    
    # Initialize Salesforce authentication
    print("\n=== Authentication Setup ===")
    print("Using your actual Salesforce credentials")
    username = "akshatasawantagentforce@akshatasawant-250204-730.demo"  # Your actual username
    password = "Ambadnya@9699"  # Your actual password
    security_token = ""  # Your security token if needed
    
    try:
        from agent_sdk.core.auth import BasicAuth
        from agent_sdk import Agentforce, AgentUtils
        
        auth = BasicAuth(username=username, password=password, security_token=security_token)
        agentforce = Agentforce(auth=auth)
        
        print("SUCCESS: Authentication initialized")
        
        # Create agent from JSON specification
        print("\n=== Creating Agent ===")
        agent = AgentUtils.create_agent_from_file('agent_spec.json')
        print(f"Agent Name: {agent.name}")
        print(f"Description: {agent.description}")
        print(f"Company: {agent.company_name}")
        
        # Deploy the agent to Salesforce
        print("\n=== Deploying Agent to Salesforce ===")
        result = agentforce.create(agent)
        print("SUCCESS: Agent deployed successfully")
        print(f"Agent ID: {result.id if hasattr(result, 'id') else 'N/A'}")
        
        # Instructions for finding the agent
        print("\n=== Finding Your Agent ===")
        print("1. Log into your Salesforce org")
        print("2. Navigate to Agentforce Builder:")
        print("   - Go to App Launcher (9 dots icon)")
        print("   - Search for 'Agentforce' or 'Einstein'")
        print("   - Click on 'Agentforce Builder'")
        print("3. Look for your agent: 'Coral Cloud Resorts Resort Manager'")
        print("4. Click to open and configure the agent")
        
    except ImportError as e:
        print(f"ERROR: Failed to import agent_sdk: {e}")
        print("Please install agentforce-sdk: pip install agentforce-sdk")
        print("Then run this script again")
    except Exception as e:
        print(f"ERROR: Deployment failed: {e}")
        print("Please check your credentials and try again")

if __name__ == "__main__":
    deploy_agent()
