#!/usr/bin/env python3
"""
Create and Deploy REAL Agent from JSON File - Version 2
NO MOCK AGENTS - Creates agent object manually to avoid SDK parsing issues

This version creates the agent object directly instead of using AgentUtils.create_agent_from_file
to avoid the 'scope' field error.
"""

import json
import os
import sys
from datetime import datetime

def create_and_deploy_real_agent():
    """Create and deploy a REAL agent to Salesforce (no mocks)"""
    
    print('=' * 80)
    print('CREATE AND DEPLOY REAL AGENT - V2')
    print('=' * 80)
    print(f'Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('Method: Direct Agent Object Creation (bypasses SDK parser)')
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
        
        # Remove scope if present
        if 'scope' in agent_spec:
            del agent_spec['scope']
        
        print(f'SUCCESS: Loaded {spec_file}')
        print(f'  Agent Name: {agent_spec["name"]}')
        print(f'  Company: {agent_spec["company_name"]}')
        print(f'  Type: {agent_spec["agent_type"]}')
        print(f'  Topics: {len(agent_spec["topics"])}')
        
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
        from agent_sdk import Agentforce
        from agent_sdk.core.agent import Agent, Topic
        
        print('  SUCCESS: Salesforce Agent SDK imported')
        print('  Modules: BasicAuth, Agentforce, Agent, Topic')
        
    except ImportError as e:
        print(f'  ERROR: Failed to import agent_sdk: {e}')
        print('\n  ALTERNATIVE: Use Salesforce CLI:')
        print(f'    sf agent create --spec agentSpec.yaml --target-org {username}')
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
        return False
    
    # Step 6: Create Agent Object Manually
    print('\n[Step 6] Creating Agent Object Manually')
    print('-' * 40)
    print('  Method: Direct instantiation (bypasses JSON parser)')
    
    try:
        # Create topics
        topics = []
        for topic_data in agent_spec['topics']:
            topic = Topic(
                name=topic_data['name'],
                description=topic_data['description']
            )
            topics.append(topic)
        
        print(f'  Created {len(topics)} topics')
        
        # Create agent object directly
        agent = Agent(
            name=agent_spec['name'],
            description=agent_spec['description'],
            agent_type=agent_spec['agent_type'],
            company_name=agent_spec['company_name'],
            company_description=agent_spec['company_description'],
            role=agent_spec['role'],
            tone=agent_spec['tone'],
            topics=topics
        )
        
        print('  SUCCESS: Agent object created manually')
        print(f'  Agent Name: {agent.name}')
        print(f'  Company: {agent.company_name}')
        print(f'  Topics: {len(agent.topics)}')
        print('  Type: REAL AGENT (Not Mock)')
        
    except Exception as e:
        print(f'  ERROR: Failed to create agent object: {e}')
        print(f'  Error Type: {type(e).__name__}')
        
        # Try alternative approach - create minimal agent
        print('\n  Trying minimal agent creation...')
        try:
            agent = Agent(
                name=agent_spec['name'],
                description=agent_spec['description'],
                company_name=agent_spec['company_name']
            )
            print('  SUCCESS: Minimal agent created')
        except Exception as e2:
            print(f'  ERROR: Minimal agent also failed: {e2}')
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
            'method': 'manual_object_creation',
            'status': 'SUCCESS'
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
        print('   App Launcher > Agentforce > Agentforce Builder')
        print('\n3. Find your agent:')
        print(f'   "{agent.name}"')
        print('=' * 80)
        
        return True
        
    except Exception as e:
        print('\n' + '=' * 80)
        print('ERROR: FAILED TO DEPLOY AGENT')
        print('=' * 80)
        print(f'Error: {e}')
        print(f'Error Type: {type(e).__name__}')
        
        # Check if it's an authentication error
        if 'auth' in str(e).lower() or 'login' in str(e).lower():
            print('\nLikely authentication issue:')
            print('  - Verify username and password are correct')
            print('  - Check if security token is needed')
            print('  - Ensure org allows API access')
        
        # Check if it's a feature availability error
        elif 'agentforce' in str(e).lower() or 'feature' in str(e).lower():
            print('\nLikely feature availability issue:')
            print('  - Agentforce may not be enabled in this org')
            print('  - Contact Salesforce to enable Agentforce')
            print('  - Try a different org with Agentforce enabled')
        
        print('\nALTERNATIVE METHODS:')
        print('\n1. Salesforce CLI:')
        print(f'   sf agent create --spec agentSpec.yaml --target-org {username}')
        print('\n2. Agentforce Builder UI:')
        print('   Setup > Agentforce > Agents > New Agent')
        print('=' * 80)
        
        return False


def main():
    """Main entry point"""
    print('\nStarting REAL agent creation and deployment (V2)...')
    print('Method: Manual agent object creation')
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
        print('See error messages above for details.')
        print('\nRECOMMENDATION: Use Salesforce CLI or UI to create agent')
        sys.exit(1)


if __name__ == "__main__":
    main()
