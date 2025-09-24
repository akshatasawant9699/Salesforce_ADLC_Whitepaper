#!/usr/bin/env python3
"""
Demo script for Coral Cloud Resorts - Resort Manager Agent
Shows realistic agent interactions with Salesforce data
"""

import json
from resort_manager_agent import ResortManagerAgent, load_agent_spec

def demo_agent_capabilities():
    """Demonstrate the resort manager agent capabilities"""
    
    print("Coral Cloud Resorts - Resort Manager Agent Demo")
    print("=" * 60)
    
    # Load agent specification
    agent_spec = load_agent_spec()
    print(f"Agent: {agent_spec['companyName']} - {agent_spec['role']}")
    print(f"Topics: {[topic['name'] for topic in agent_spec['topics']]}")
    
    # Get real Salesforce org credentials
    import subprocess
    try:
        # Get org info from Salesforce CLI
        result = subprocess.run(['sf', 'org', 'display', '--target-org', 'resorts-demo', '--json'], 
                               capture_output=True, text=True, check=True)
        org_info = json.loads(result.stdout)
        
        org_url = org_info['result']['instanceUrl']
        access_token = org_info['result']['accessToken']
        
        print(f"Connected to: {org_info['result']['username']}")
        print(f"Org URL: {org_url}")
        
    except subprocess.CalledProcessError as e:
        print("Error getting org info from Salesforce CLI:")
        print(e.stderr)
        print("Using fallback credentials...")
        org_url = "https://resorts-demo.my.salesforce.com"
        access_token = "demo_token"
    
    # Initialize agent with real credentials
    agent = ResortManagerAgent(org_url, access_token)
    
    print(f"\nAgent Persona: {agent.persona}")
    print("\n" + "=" * 60)
    
    # Demo scenarios based on agentSpec.yaml topics
    scenarios = [
        {
            "title": "Customer Complaint Resolution",
            "description": "Guest complains about room service delay",
            "request": {
                "type": "customer_complaint",
                "complaint_type": "service_delay",
                "details": "Room service order was 45 minutes late"
            }
        },
        {
            "title": "Reservation System Support", 
            "description": "Look up guest reservation details",
            "request": {
                "type": "reservation_lookup",
                "customer_name": "Sarah Johnson"
            }
        },
        {
            "title": "Employee Schedule Management",
            "description": "Update housekeeping staff schedule",
            "request": {
                "type": "schedule_management",
                "employee_id": "HK001",
                "shift_type": "Evening",
                "date": "2024-11-26"
            }
        },
        {
            "title": "Activity Recommendations",
            "description": "Suggest activities for family with kids",
            "request": {
                "type": "activity_recommendation",
                "guest_preferences": "family activities"
            }
        },
        {
            "title": "Service Quality Monitoring",
            "description": "Handle guest feedback about amenities",
            "request": {
                "type": "customer_complaint",
                "complaint_type": "amenities",
                "details": "Pool temperature too cold"
            }
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{i}. {scenario['title']}")
        print(f"   {scenario['description']}")
        print("   " + "-" * 50)
        
        # Process the request
        result = agent.process_request(scenario['request']['type'], **{k: v for k, v in scenario['request'].items() if k != 'type'})
        
        # Display formatted result
        print("   Agent Response:")
        print("   " + json.dumps(result, indent=6).replace('\n', '\n   '))
        print()
    
    print("=" * 60)
    print("Demo completed. Resort Manager Agent is ready for production!")

if __name__ == "__main__":
    demo_agent_capabilities()
