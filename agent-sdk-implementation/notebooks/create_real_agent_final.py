#!/usr/bin/env python3
"""
Create and Deploy REAL Agent from JSON File - FINAL VERSION
NO MOCK AGENTS - Uses correct agent_sdk imports

This version uses the correct imports from agent_sdk:
- Agent, Topic directly from agent_sdk
- AgentUtils.create_agent_from_dict() to avoid 'scope' field issues
"""

import json
import os
import sys
from datetime import datetime

def create_and_deploy_real_agent():
    """Create and deploy a REAL agent to Salesforce (no mocks)"""
    
    print('=' * 80)
    print('CREATE AND DEPLOY REAL AGENT - FINAL VERSION')
    print('=' * 80)
    print(f'Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('Method: AgentUtils.create_agent_from_dict()')
    print('Type: REAL AGENT (Not Mock)')
    print('=' * 80)
    
    # Step 1: Load agent specification
    print('\n[Step 1] Loading Agent Specification')
    print('-' * 40)
    
    spec_file = 'agent_spec_sdk.json'
    if not os.path.exists(spec_file):
        spec_file = 'agent_spec.json'
    
    try:
        with open(spec_file, 'r') as f:
            agent_spec = json.load(f)
        
        # Remove scope if present (SDK doesn't support it)
        if 'scope' in agent_spec:
            print('  Removing scope field for SDK compatibility')
            del agent_spec['scope']
        
        print(f'SUCCESS: Loaded {spec_file}')
        print(f'  Agent Name: {agent_spec["name"]}')
        print(f'  Company: {agent_spec["company_name"]}')
        print(f'  Type: {agent_spec["agent_type"]}')
        print(f'  Topics: {len(agent_spec["topics"])}')
        print(f'  Fields: {list(agent_spec.keys())}')
        
    except FileNotFoundError:
        print(f'ERROR: Agent specification file not found')
        return False
    except json.JSONDecodeError as e:
        print(f'ERROR: Invalid JSON: {e}')
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
        from agent_sdk import Agentforce, AgentUtils, Agent, Topic
        
        print('  SUCCESS: Salesforce Agent SDK imported')
        print('  Classes: BasicAuth, Agentforce, AgentUtils, Agent, Topic')
        
    except ImportError as e:
        print(f'  ERROR: Failed to import agent_sdk: {e}')
        print('\n  Install with: pip install agentforce-sdk')
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
        print(f'  Instance URL: {agentforce.instance_url if hasattr(agentforce, "instance_url") else "N/A"}')
        print('  Ready to create REAL agent')
        
    except Exception as e:
        print(f'  ERROR: Failed to initialize Agentforce: {e}')
        print(f'  Error Type: {type(e).__name__}')
        return False
    
    # Step 6: Create Agent from Dictionary
    print('\n[Step 6] Creating Agent from Specification')
    print('-' * 40)
    print('  Method: AgentUtils.create_agent_from_dict()')
    
    try:
        # Use create_agent_from_dict instead of create_agent_from_file
        # This gives us more control over the data
        agent = AgentUtils.create_agent_from_dict(agent_spec)
        
        print('  SUCCESS: Agent object created')
        print(f'  Agent Name: {agent.name}')
        print(f'  Description: {agent.description[:50]}...')
        print(f'  Company: {agent.company_name}')
        print(f'  Topics: {len(agent.topics) if hasattr(agent, "topics") else 0}')
        print('  Type: REAL AGENT (Not Mock)')
        
    except Exception as e:
        print(f'  ERROR: Failed to create agent: {e}')
        print(f'  Error Type: {type(e).__name__}')
        
        # Try to understand the error
        if 'scope' in str(e):
            print('\n  The SDK is still finding a scope field somewhere.')
            print('  Trying to create agent with minimal fields...')
            
            # Create minimal spec
            minimal_spec = {
                'name': agent_spec['name'],
                'description': agent_spec['description'],
                'company_name': agent_spec['company_name'],
                'company_description': agent_spec['company_description']
            }
            
            try:
                agent = AgentUtils.create_agent_from_dict(minimal_spec)
                print('  SUCCESS: Minimal agent created')
            except Exception as e2:
                print(f'  ERROR: Minimal agent also failed: {e2}')
                return False
        else:
            return False
    
    # Step 7: Deploy Agent to Salesforce
    print('\n[Step 7] Deploying REAL Agent to Salesforce')
    print('-' * 40)
    print('  Connecting to Salesforce org...')
    print('  This may take 30-60 seconds...')
    
    try:
        result = agentforce.create(agent)
        
        print('\n' + '=' * 80)
        print('SUCCESS: REAL AGENT DEPLOYED TO SALESFORCE!')
        print('=' * 80)
        
        # Extract agent ID
        agent_id = None
        if hasattr(result, 'id'):
            agent_id = result.id
        elif isinstance(result, dict) and 'id' in result:
            agent_id = result['id']
        
        print(f'Agent ID: {agent_id if agent_id else "N/A"}')
        print(f'Agent Name: {agent.name}')
        print(f'Company: {agent.company_name}')
        print(f'Org: {username}')
        print(f'Deployment Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'Type: REAL AGENT (Not Mock)')
        print('=' * 80)
        
        # Save deployment metadata
        deployment_data = {
            'agent_id': agent_id if agent_id else 'N/A',
            'agent_name': agent.name,
            'company': agent.company_name,
            'org': username,
            'deployment_time': datetime.now().isoformat(),
            'type': 'REAL_AGENT',
            'method': 'agent_sdk_create_from_dict',
            'status': 'SUCCESS',
            'result': str(result)
        }
        
        with open('real_agent_deployment.json', 'w') as f:
            json.dump(deployment_data, f, indent=2)
        
        print('\nDeployment metadata saved to: real_agent_deployment.json')
        
        # Instructions
        print('\n' + '=' * 80)
        print('HOW TO ACCESS YOUR REAL AGENT')
        print('=' * 80)
        print('\n1. Log into Salesforce:')
        print(f'   https://your-org.salesforce.com')
        print('\n2. Navigate to Agentforce Builder:')
        print('   - Click App Launcher (9 dots)')
        print('   - Search for "Agentforce"')
        print('   - Click "Agentforce Builder"')
        print('\n3. Find your agent:')
        print(f'   - Name: "{agent.name}"')
        if agent_id:
            print(f'   - ID: {agent_id}')
        print('\n4. Configure and test:')
        print('   - Add actions and knowledge base')
        print('   - Test with sample conversations')
        print('   - Activate when ready')
        print('=' * 80)
        
        return True
        
    except Exception as e:
        print('\n' + '=' * 80)
        print('ERROR: FAILED TO DEPLOY AGENT')
        print('=' * 80)
        print(f'Error: {e}')
        print(f'Error Type: {type(e).__name__}')
        
        # Detailed error analysis
        error_str = str(e).lower()
        
        if 'auth' in error_str or 'login' in error_str or 'credential' in error_str:
            print('\nAuthentication Error:')
            print('  - Verify username and password')
            print('  - Check if security token is needed')
            print('  - Ensure org allows API access')
            print('  - Try logging in via web to verify credentials')
            
        elif 'agentforce' in error_str or 'feature' in error_str or 'not enabled' in error_str:
            print('\nFeature Availability Error:')
            print('  - Agentforce may not be enabled in this org')
            print('  - Contact Salesforce to enable Agentforce')
            print('  - Try a different org with Agentforce enabled')
            print('  - Check org edition (requires Enterprise or higher)')
            
        elif 'permission' in error_str or 'access' in error_str:
            print('\nPermission Error:')
            print('  - You may need Agentforce Admin permissions')
            print('  - Go to Setup > Permission Sets')
            print('  - Assign Agentforce Admin to your user')
            
        else:
            print('\nUnknown Error:')
            print('  - Check Salesforce status: status.salesforce.com')
            print('  - Verify network connectivity')
            print('  - Check API limits')
        
        print('\nALTERNATIVE METHODS TO CREATE AGENT:')
        print('\n1. Salesforce CLI (Recommended):')
        print(f'   sf agent create --spec agentSpec.yaml --target-org {username}')
        print('\n2. Agentforce Builder UI:')
        print('   Setup > Agentforce > Agents > New Agent')
        print('   Use details from agent_spec.json')
        print('=' * 80)
        
        # Save error details
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
    print('\n' + '=' * 80)
    print('REAL AGENT CREATION SCRIPT')
    print('=' * 80)
    print('This script will create a REAL agent in Salesforce')
    print('NO MOCK AGENTS will be created')
    print('Using: Salesforce Agent SDK')
    print('=' * 80 + '\n')
    
    success = create_and_deploy_real_agent()
    
    if success:
        print('\n' + '=' * 80)
        print('DEPLOYMENT COMPLETE - REAL AGENT CREATED')
        print('=' * 80)
        print('Your agent is now live in Salesforce!')
        sys.exit(0)
    else:
        print('\n' + '=' * 80)
        print('DEPLOYMENT FAILED')
        print('=' * 80)
        print('Please review the error messages and try alternative methods.')
        sys.exit(1)


if __name__ == "__main__":
    main()
