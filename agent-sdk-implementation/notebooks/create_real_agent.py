#!/usr/bin/env python3
"""
Create and Deploy REAL Agent from JSON File
NO MOCK AGENTS - This creates an actual agent in Salesforce

Based on: deploy_agent.py and SCOPE_FIELD_FIX.md
"""

import json
import os
import sys
from datetime import datetime

def create_and_deploy_real_agent():
    """Create and deploy a REAL agent to Salesforce (no mocks)"""
    
    print('=' * 80)
    print('CREATE AND DEPLOY REAL AGENT')
    print('=' * 80)
    print(f'Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('Type: REAL AGENT (Not Mock)')
    print('=' * 80)
    
    # Step 1: Load agent specification
    print('\n[Step 1] Loading Agent Specification')
    print('-' * 40)
    
    # Use SDK-compatible version (without 'scope' field)
    spec_file = 'agent_spec_sdk.json'
    if not os.path.exists(spec_file):
        print(f'WARNING: {spec_file} not found, using agent_spec.json')
        spec_file = 'agent_spec.json'
    
    try:
        with open(spec_file, 'r') as f:
            agent_spec = json.load(f)
        
        print(f'SUCCESS: Loaded {spec_file}')
        print(f'  Agent Name: {agent_spec["name"]}')
        print(f'  Company: {agent_spec["company_name"]}')
        print(f'  Type: {agent_spec["agent_type"]}')
        print(f'  Topics: {len(agent_spec["topics"])}')
        
        # Check for scope field
        if 'scope' in agent_spec:
            print(f'  WARNING: Found scope field, removing for SDK compatibility')
            agent_spec_sdk = {k: v for k, v in agent_spec.items() if k != 'scope'}
            # Save SDK version
            with open('agent_spec_sdk.json', 'w') as f:
                json.dump(agent_spec_sdk, f, indent=2)
            spec_file = 'agent_spec_sdk.json'
            print(f'  Created: agent_spec_sdk.json (without scope)')
        
    except FileNotFoundError:
        print(f'ERROR: Agent specification file not found')
        print('Please ensure agent_spec.json or agent_spec_sdk.json exists')
        return False
    except json.JSONDecodeError as e:
        print(f'ERROR: Invalid JSON in specification file: {e}')
        return False
    
    # Step 2: Setup Authentication
    print('\n[Step 2] Salesforce Authentication')
    print('-' * 40)
    
    username = "your_username@example.com"
    password = "your_password"
    security_token = ""
    
    print(f'  Username: {username}')
    print(f'  Org: Developer Edition')
    
    # Step 3: Import Salesforce SDK
    print('\n[Step 3] Importing Salesforce Agent SDK')
    print('-' * 40)
    
    try:
        from agent_sdk.core.auth import BasicAuth
        from agent_sdk import Agentforce, AgentUtils
        
        print('  SUCCESS: Salesforce Agent SDK imported')
        print('  Modules: BasicAuth, Agentforce, AgentUtils')
        sdk_available = True
        
    except ImportError as e:
        print(f'  ERROR: Failed to import agent_sdk: {e}')
        print('\n  The Salesforce Agent SDK is not installed or not available.')
        print('  To install: pip install agentforce-sdk')
        print('\n  ALTERNATIVE: Use Salesforce CLI instead:')
        print(f'    sf agent create --spec {spec_file} --target-org {username}')
        sdk_available = False
        return False
    
    # Step 4: Initialize Authentication
    print('\n[Step 4] Initializing Authentication')
    print('-' * 40)
    
    try:
        auth = BasicAuth(
            username=username,
            password=password,
            security_token=security_token
        )
        print('  SUCCESS: Authentication object created')
        
    except Exception as e:
        print(f'  ERROR: Failed to create authentication: {e}')
        return False
    
    # Step 5: Initialize Agentforce Client
    print('\n[Step 5] Initializing Agentforce Client')
    print('-' * 40)
    
    try:
        agentforce = Agentforce(auth=auth)
        print('  SUCCESS: Agentforce client initialized')
        print('  Ready to create REAL agent')
        
    except Exception as e:
        print(f'  ERROR: Failed to initialize Agentforce: {e}')
        print('  Check your credentials and network connection')
        return False
    
    # Step 6: Create Agent from JSON
    print('\n[Step 6] Creating Agent from JSON Specification')
    print('-' * 40)
    
    try:
        agent = AgentUtils.create_agent_from_file(spec_file)
        
        print('  SUCCESS: Agent object created')
        print(f'  Agent Name: {agent.name}')
        print(f'  Description: {agent.description}')
        print(f'  Company: {agent.company_name}')
        print(f'  Topics: {len(agent.topics) if hasattr(agent, "topics") else "N/A"}')
        print('  Type: REAL AGENT (Not Mock)')
        
    except Exception as e:
        print(f'  ERROR: Failed to create agent from JSON: {e}')
        print(f'  File: {spec_file}')
        print('  Check that the JSON file has all required fields')
        return False
    
    # Step 7: Deploy Agent to Salesforce
    print('\n[Step 7] Deploying REAL Agent to Salesforce')
    print('-' * 40)
    print('  Connecting to Salesforce org...')
    
    try:
        result = agentforce.create(agent)
        
        print('\n' + '=' * 80)
        print('SUCCESS: REAL AGENT DEPLOYED TO SALESFORCE!')
        print('=' * 80)
        print(f'Agent ID: {result.id if hasattr(result, "id") else "N/A"}')
        print(f'Agent Name: {agent.name}')
        print(f'Company: {agent.company_name}')
        print(f'Org: {username}')
        print(f'Deployment Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'Type: REAL AGENT (Not Mock)')
        print('=' * 80)
        
        # Save deployment metadata
        deployment_data = {
            'agent_id': result.id if hasattr(result, 'id') else 'N/A',
            'agent_name': agent.name,
            'company': agent.company_name,
            'org': username,
            'deployment_time': datetime.now().isoformat(),
            'type': 'REAL_AGENT',
            'status': 'SUCCESS'
        }
        
        with open('real_agent_deployment.json', 'w') as f:
            json.dump(deployment_data, f, indent=2)
        
        print('\nDeployment metadata saved to: real_agent_deployment.json')
        
        # Instructions for accessing the agent
        print('\n' + '=' * 80)
        print('HOW TO ACCESS YOUR REAL AGENT')
        print('=' * 80)
        print('\n1. Log into your Salesforce org:')
        print(f'   https://your-org.salesforce.com')
        print('\n2. Navigate to Agentforce Builder:')
        print('   - Click the App Launcher (9 dots icon)')
        print('   - Search for "Agentforce" or "Einstein"')
        print('   - Click on "Agentforce Builder"')
        print('\n3. Find your agent:')
        print(f'   - Look for: "{agent.name}"')
        print('   - Click to open and configure')
        print('\n4. Test your agent:')
        print('   - Use the preview/test feature in Agentforce Builder')
        print('   - Try sample conversations')
        print('   - Configure actions and knowledge base')
        print('=' * 80)
        
        return True
        
    except Exception as e:
        print('\n' + '=' * 80)
        print('ERROR: FAILED TO DEPLOY AGENT')
        print('=' * 80)
        print(f'Error: {e}')
        print(f'Error Type: {type(e).__name__}')
        print('\nPossible causes:')
        print('  1. Invalid credentials')
        print('  2. Network connectivity issues')
        print('  3. Agentforce not enabled in org')
        print('  4. Insufficient permissions')
        print('  5. Invalid agent specification')
        print('\nTroubleshooting:')
        print('  - Verify credentials are correct')
        print('  - Check network connection')
        print('  - Ensure Agentforce is enabled in your org')
        print('  - Verify you have Agentforce Admin permissions')
        print('\nALTERNATIVE: Use Salesforce CLI:')
        print(f'  sf agent create --spec agent_spec.json --target-org {username}')
        print('=' * 80)
        
        # Save error metadata
        error_data = {
            'error': str(e),
            'error_type': type(e).__name__,
            'agent_name': agent.name if 'agent' in locals() else 'N/A',
            'org': username,
            'timestamp': datetime.now().isoformat(),
            'type': 'DEPLOYMENT_ERROR'
        }
        
        with open('agent_deployment_error.json', 'w') as f:
            json.dump(error_data, f, indent=2)
        
        print('\nError details saved to: agent_deployment_error.json')
        
        return False


def main():
    """Main entry point"""
    print('\nStarting REAL agent creation and deployment...')
    print('NO MOCK AGENTS will be created\n')
    
    success = create_and_deploy_real_agent()
    
    if success:
        print('\n' + '=' * 80)
        print('DEPLOYMENT COMPLETE - REAL AGENT CREATED')
        print('=' * 80)
        sys.exit(0)
    else:
        print('\n' + '=' * 80)
        print('DEPLOYMENT FAILED')
        print('=' * 80)
        print('Please review the error messages above and try again.')
        sys.exit(1)


if __name__ == "__main__":
    main()
