#!/usr/bin/env python3
"""
Coral Cloud Resorts Agent Setup Script
Phase 1: Ideation & Design Implementation

This script demonstrates the setup and configuration of the Coral Cloud Resorts
agent using the Salesforce Agentforce SDK.
"""

import yaml
import json
from pathlib import Path
from typing import Dict, List, Any

class CoralCloudResortsAgent:
    """
    Coral Cloud Resorts Agent Manager
    
    This class handles the configuration and setup of the resort manager agent
    for Coral Cloud Resorts, including topic management and conversation flow.
    """
    
    def __init__(self, config_path: str = "specs/agentSpec.yaml"):
        """Initialize the agent with configuration from YAML file."""
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.agent_name = self.config['agent']['name']
        self.company_name = self.config['company']['name']
        
    def _load_config(self) -> Dict[str, Any]:
        """Load agent configuration from YAML file."""
        try:
            with open(self.config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Configuration file not found: {self.config_path}")
            return {}
        except yaml.YAMLError as e:
            print(f"Error parsing YAML configuration: {e}")
            return {}
    
    def get_agent_info(self) -> Dict[str, str]:
        """Get basic agent information."""
        return {
            'name': self.config['agent']['name'],
            'type': self.config['agent']['type'],
            'description': self.config['agent']['description'],
            'company': self.config['company']['name'],
            'role': self.config['role']['title']
        }
    
    def get_topics(self) -> List[Dict[str, Any]]:
        """Get all configured topics for the agent."""
        return self.config.get('topics', [])
    
    def get_capabilities(self) -> Dict[str, List[str]]:
        """Get agent capabilities and tools."""
        return self.config.get('capabilities', {})
    
    def generate_topic_summary(self) -> str:
        """Generate a summary of all topics the agent can handle."""
        topics = self.get_topics()
        summary = f"Agent: {self.agent_name}\n"
        summary += f"Company: {self.company_name}\n"
        summary += f"Total Topics: {len(topics)}\n\n"
        
        for topic in topics:
            summary += f"• {topic['name']}: {topic['description']}\n"
            if 'examples' in topic:
                for example in topic['examples'][:2]:  # Show first 2 examples
                    summary += f"  - {example}\n"
            summary += "\n"
        
        return summary
    
    def validate_configuration(self) -> bool:
        """Validate that the agent configuration is complete."""
        required_sections = ['agent', 'company', 'role', 'topics', 'capabilities']
        
        for section in required_sections:
            if section not in self.config:
                print(f"Missing required section: {section}")
                return False
        
        # Check for required agent fields
        agent_fields = ['name', 'type', 'description']
        for field in agent_fields:
            if field not in self.config['agent']:
                print(f"Missing required agent field: {field}")
                return False
        
        # Check for topics
        if not self.config['topics']:
            print("No topics configured")
            return False
        
        print("Configuration validation passed!")
        return True
    
    def export_to_salesforce_format(self) -> Dict[str, Any]:
        """Export configuration in Salesforce-compatible format."""
        return {
            'agentSpec': {
                'agent': self.config['agent'],
                'company': self.config['company'],
                'role': self.config['role'],
                'persona': self.config.get('persona', {}),
                'topics': self.config['topics'],
                'capabilities': self.config['capabilities'],
                'conversation_flow': self.config.get('conversation_flow', {}),
                'integration_requirements': self.config.get('integration_requirements', {}),
                'success_metrics': self.config.get('success_metrics', [])
            }
        }

def main():
    """Main function to demonstrate agent setup."""
    print("🏝️  Coral Cloud Resorts Agent Setup")
    print("=" * 50)
    
    # Initialize the agent
    agent = CoralCloudResortsAgent()
    
    # Validate configuration
    if not agent.validate_configuration():
        print("❌ Configuration validation failed!")
        return
    
    print("✅ Configuration validation passed!")
    print()
    
    # Display agent information
    agent_info = agent.get_agent_info()
    print("Agent Information:")
    for key, value in agent_info.items():
        print(f"  {key.title()}: {value}")
    print()
    
    # Display topic summary
    print("Topic Summary:")
    print(agent.generate_topic_summary())
    
    # Display capabilities
    capabilities = agent.get_capabilities()
    print("Capabilities:")
    for category, items in capabilities.items():
        print(f"  {category.title()}:")
        for item in items:
            print(f"    - {item}")
    print()
    
    # Export to Salesforce format
    salesforce_config = agent.export_to_salesforce_format()
    print("Salesforce Configuration Generated Successfully!")
    print(f"Total topics configured: {len(salesforce_config['agentSpec']['topics'])}")
    
    # Save Salesforce format to file
    output_file = Path("specs/salesforce_agent_config.json")
    with open(output_file, 'w') as f:
        json.dump(salesforce_config, f, indent=2)
    print(f"Salesforce configuration saved to: {output_file}")

if __name__ == "__main__":
    main()
