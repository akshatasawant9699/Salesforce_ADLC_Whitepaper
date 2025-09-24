#!/usr/bin/env python3
"""
Coral Cloud Resorts Agent Demo
Demonstrates the agent's capabilities and conversation flow
"""

import json
import random
from datetime import datetime
from typing import Dict, List, Any

class CoralCloudResortsAgentDemo:
    """
    Demo implementation of the Coral Cloud Resorts Agent
    Shows how the agent would handle different types of requests
    """
    
    def __init__(self):
        """Initialize the demo agent with sample data."""
        self.agent_name = "Coral Cloud Resorts Manager"
        self.company_name = "Coral Cloud Resorts"
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Sample topics and their handling logic
        self.topics = {
            "Customer Complaints": {
                "keywords": ["complaint", "problem", "issue", "unhappy", "disappointed"],
                "response_template": "I sincerely apologize for the inconvenience. Let me address your concern about {issue} immediately.",
                "escalation": "I'm connecting you with our senior management team to ensure this is resolved to your satisfaction."
            },
            "Reservation Management": {
                "keywords": ["booking", "reservation", "cancel", "modify", "check-in", "check-out"],
                "response_template": "I'd be happy to help you with your reservation. Let me access your booking details for {guest_name}.",
                "escalation": "Let me transfer you to our reservations specialist for immediate assistance."
            },
            "Employee Scheduling": {
                "keywords": ["schedule", "shift", "employee", "staff", "coverage", "time-off"],
                "response_template": "I'll help you with the scheduling matter. Let me check the current staff schedule and availability.",
                "escalation": "I'm coordinating with our HR department to resolve this scheduling issue."
            },
            "Resort Operations": {
                "keywords": ["maintenance", "facility", "equipment", "supplies", "operations"],
                "response_template": "I understand the operational concern. Let me coordinate with our facilities team to address {issue}.",
                "escalation": "I'm immediately notifying our operations manager to handle this priority issue."
            },
            "Policy Information": {
                "keywords": ["policy", "rule", "procedure", "guideline", "information"],
                "response_template": "I'd be happy to provide you with information about our {policy_type} policy.",
                "escalation": "Let me connect you with our policy specialist for detailed information."
            },
            "Emergency Response": {
                "keywords": ["emergency", "urgent", "medical", "security", "safety"],
                "response_template": "This is a priority situation. I'm immediately alerting our emergency response team for {emergency_type}.",
                "escalation": "Emergency protocols activated. Security and medical teams have been notified."
            }
        }
    
    def analyze_intent(self, user_input: str) -> str:
        """Analyze user input to determine the appropriate topic."""
        user_input_lower = user_input.lower()
        
        # Score each topic based on keyword matches
        topic_scores = {}
        for topic, config in self.topics.items():
            score = sum(1 for keyword in config["keywords"] if keyword in user_input_lower)
            topic_scores[topic] = score
        
        # Return the topic with the highest score
        if topic_scores:
            best_topic = max(topic_scores, key=topic_scores.get)
            if topic_scores[best_topic] > 0:
                return best_topic
        
        return "General Inquiry"
    
    def generate_response(self, user_input: str, topic: str) -> str:
        """Generate an appropriate response based on the topic."""
        if topic == "General Inquiry":
            return f"Hello! I'm your {self.agent_name}. How can I help make your experience at {self.company_name} more enjoyable today?"
        
        topic_config = self.topics.get(topic, {})
        response_template = topic_config.get("response_template", "I understand your concern. Let me help you with that.")
        
        # Simple template substitution (in a real implementation, this would be more sophisticated)
        if "{issue}" in response_template:
            response_template = response_template.replace("{issue}", "this matter")
        if "{guest_name}" in response_template:
            response_template = response_template.replace("{guest_name}", "your booking")
        if "{policy_type}" in response_template:
            response_template = response_template.replace("{policy_type}", "resort")
        if "{emergency_type}" in response_template:
            response_template = response_template.replace("{emergency_type}", "this situation")
        
        return response_template
    
    def should_escalate(self, topic: str, user_input: str) -> bool:
        """Determine if the request should be escalated."""
        escalation_keywords = ["urgent", "emergency", "manager", "supervisor", "escalate", "complain"]
        return any(keyword in user_input.lower() for keyword in escalation_keywords)
    
    def get_escalation_response(self, topic: str) -> str:
        """Get escalation response for the topic."""
        topic_config = self.topics.get(topic, {})
        return topic_config.get("escalation", "Let me connect you with the appropriate department for immediate assistance.")
    
    def process_request(self, user_input: str) -> Dict[str, Any]:
        """Process a user request and return the agent's response."""
        # Analyze intent
        topic = self.analyze_intent(user_input)
        
        # Generate response
        response = self.generate_response(user_input, topic)
        
        # Check for escalation
        should_escalate = self.should_escalate(topic, user_input)
        if should_escalate:
            escalation_response = self.get_escalation_response(topic)
            response += f" {escalation_response}"
        
        return {
            "timestamp": self.current_time,
            "agent": self.agent_name,
            "topic": topic,
            "user_input": user_input,
            "response": response,
            "escalated": should_escalate
        }

def run_demo():
    """Run the agent demo with sample interactions."""
    agent = CoralCloudResortsAgentDemo()
    
    print("🏝️  Coral Cloud Resorts Agent Demo")
    print("=" * 50)
    print(f"Agent: {agent.agent_name}")
    print(f"Company: {agent.company_name}")
    print(f"Time: {agent.current_time}")
    print()
    
    # Sample user inputs to demonstrate different topics
    sample_inputs = [
        "I have a complaint about my room - the air conditioning isn't working",
        "I need to modify my reservation for next week",
        "Can you help me with the employee schedule for this weekend?",
        "There's a maintenance issue with the pool equipment",
        "What is your pet policy?",
        "This is an emergency - there's a medical situation in the lobby",
        "I'm not happy with the service and want to speak to a manager"
    ]
    
    print("Sample Interactions:")
    print("-" * 30)
    
    for i, user_input in enumerate(sample_inputs, 1):
        print(f"\n{i}. User: {user_input}")
        
        result = agent.process_request(user_input)
        
        print(f"   Topic: {result['topic']}")
        print(f"   Agent: {result['response']}")
        if result['escalated']:
            print("   ⚠️  ESCALATED")
    
    print("\n" + "=" * 50)
    print("Demo completed! The agent successfully handled various types of requests.")
    print("In a real implementation, this would integrate with:")
    print("- Property Management Systems (PMS)")
    print("- Customer Relationship Management (CRM)")
    print("- Human Resources Information System (HRIS)")
    print("- Emergency response protocols")

if __name__ == "__main__":
    run_demo()
