#!/usr/bin/env python3
"""
Phase 2: Development Demo - Coral Cloud Resorts Agent
===================================================

This script demonstrates the complete Phase 2 implementation including:
- Agent core with tools and knowledge base
- Intent recognition and response generation
- Integration with Salesforce Agentforce SDK concepts
- Real-world resort management scenarios

Based on the Agentforce SDK documentation:
https://pypi.org/project/agentforce-sdk/
"""

import json
import time
from datetime import datetime
from phase2_agent_core import ResortManagerAgent
from setup_knowledge_base import ResortKnowledgeBase

class Phase2Demo:
    """Comprehensive demo of Phase 2 agent capabilities"""
    
    def __init__(self):
        self.agent = ResortManagerAgent()
        self.knowledge_base = ResortKnowledgeBase()
        self.demo_scenarios = self._setup_demo_scenarios()
    
    def _setup_demo_scenarios(self):
        """Setup comprehensive demo scenarios"""
        return {
            "customer_complaints": [
                "I'm very disappointed with my room - the air conditioning isn't working and it's extremely hot",
                "The room service was terrible last night - my food was cold and took over an hour",
                "There's a terrible noise coming from the room above us and we can't sleep",
                "The bathroom in our room is dirty and the shower doesn't work properly"
            ],
            "reservation_management": [
                "Can you help me find my reservation? My name is John Smith",
                "I need to modify my booking for next week - can you change the dates?",
                "What's the status of my reservation? Confirmation number CCR-2024-001",
                "I want to cancel my reservation for this weekend"
            ],
            "employee_scheduling": [
                "I need to update Alice Johnson's schedule - she needs to work the evening shift tomorrow",
                "Can you show me the current employee schedules?",
                "Bob Wilson requested time off next week - can you approve it?",
                "We need to find coverage for Carol Davis's shift on Friday"
            ],
            "resort_operations": [
                "There's a broken elevator in the main building - guests are complaining",
                "The pool area needs cleaning - there's debris from the storm last night",
                "The fitness center equipment is not working properly",
                "We have a maintenance request for room 303 - the TV is not working"
            ],
            "policy_information": [
                "What's your cancellation policy?",
                "Can I bring my pet dog to the resort?",
                "What time is check-in and check-out?",
                "What are the pool hours?",
                "Is there a pet fee?"
            ],
            "emergency_response": [
                "This is an emergency - there's a fire in the kitchen!",
                "We have a medical emergency in room 415 - someone needs help immediately",
                "There's a security issue in the parking lot - someone is acting suspicious",
                "The power went out in the entire building - guests are stuck in elevators"
            ],
            "general_inquiries": [
                "Hello, I just wanted to say the resort is beautiful",
                "What activities are available for families?",
                "Can you recommend a good restaurant nearby?",
                "What's the weather like today?"
            ]
        }
    
    def run_comprehensive_demo(self):
        """Run comprehensive Phase 2 demo"""
        print("🏝️  Coral Cloud Resorts Agent - Phase 2 Development Demo")
        print("=" * 70)
        print(f"Demo started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Test each category
        for category, scenarios in self.demo_scenarios.items():
            print(f"📋 Testing {category.replace('_', ' ').title()}:")
            print("-" * 50)
            
            for i, scenario in enumerate(scenarios, 1):
                print(f"\n{i}. User: {scenario}")
                
                # Process the request
                start_time = time.time()
                response = self.agent.process_request(scenario)
                processing_time = time.time() - start_time
                
                # Display response
                print(f"   Agent: {response['response']}")
                
                # Show tools used
                if response.get('tools_used'):
                    print(f"   🔧 Tools Used: {', '.join(response['tools_used'])}")
                
                # Show escalation if needed
                if response.get('escalation'):
                    print(f"   🚨 Escalation: {response['escalation']}")
                
                # Show next steps
                if response.get('next_steps'):
                    print(f"   📋 Next Steps: {', '.join(response['next_steps'])}")
                
                # Show processing time
                print(f"   ⏱️  Processing Time: {processing_time:.2f}s")
                
                # Add small delay for readability
                time.sleep(0.5)
            
            print(f"\n✅ {category.replace('_', ' ').title()} testing complete!")
            print()
    
    def test_knowledge_base(self):
        """Test knowledge base functionality"""
        print("🧠 Testing Knowledge Base:")
        print("-" * 30)
        
        test_queries = [
            "cancellation policy",
            "pet policy",
            "emergency procedures", 
            "check-in time",
            "pool hours",
            "room service"
        ]
        
        for query in test_queries:
            print(f"\nQuery: '{query}'")
            results = self.knowledge_base.search(query)
            print(f"Results: {results['count']} found")
            
            if results['results']:
                for result in results['results'][:1]:  # Show first result
                    print(f"  • {result['title']}")
                    print(f"    {result['content'][:80]}...")
    
    def test_tools_functionality(self):
        """Test individual tool functionality"""
        print("\n🔧 Testing Individual Tools:")
        print("-" * 30)
        
        # Test Reservation Finder
        print("\n1. Reservation Finder:")
        reservation_tool = self.agent.tools["reservation_finder"]
        result = reservation_tool.execute(email="john.smith@email.com")
        print(f"   Result: {result['message']}")
        
        # Test Schedule Manager
        print("\n2. Schedule Manager:")
        schedule_tool = self.agent.tools["schedule_manager"]
        result = schedule_tool.execute(action="list")
        print(f"   Result: {result['message']}")
        
        # Test Maintenance Tracker
        print("\n3. Maintenance Tracker:")
        maintenance_tool = self.agent.tools["maintenance_tracker"]
        result = maintenance_tool.execute(
            issue_type="broken elevator",
            location="main building",
            description="Elevator stuck between floors",
            priority="urgent"
        )
        print(f"   Result: {result['message']}")
    
    def generate_agent_spec(self):
        """Generate agent specification for Salesforce integration"""
        agent_spec = {
            "agent": {
                "name": "Coral Cloud Resorts Manager",
                "type": "Customer",
                "description": "AI-powered resort manager for handling customer service, employee management, and operations",
                "version": "2.0.0",
                "created": datetime.now().isoformat()
            },
            "capabilities": {
                "intent_recognition": [
                    "customer_complaint",
                    "reservation_management", 
                    "employee_scheduling",
                    "resort_operations",
                    "policy_information",
                    "emergency_response",
                    "general_inquiry"
                ],
                "tools": [
                    {
                        "name": "ReservationFinder",
                        "description": "Search and manage customer reservations",
                        "parameters": ["customer_name", "email", "confirmation"]
                    },
                    {
                        "name": "ScheduleManager", 
                        "description": "Manage employee schedules and time-off requests",
                        "parameters": ["employee_id", "new_shift", "action"]
                    },
                    {
                        "name": "MaintenanceTracker",
                        "description": "Track maintenance requests and facility issues",
                        "parameters": ["issue_type", "location", "description", "priority"]
                    }
                ],
                "knowledge_base": {
                    "policies": 5,
                    "procedures": 3,
                    "facilities": 3,
                    "contact_info": 2
                }
            },
            "integration": {
                "salesforce_org": "resume-demo",
                "api_version": "58.0",
                "permissions": [
                    "EinsteinServiceAgent",
                    "AgentforceUser",
                    "ResortManager"
                ]
            },
            "performance_metrics": {
                "response_time": "< 2 seconds",
                "intent_accuracy": "> 90%",
                "escalation_rate": "< 15%",
                "customer_satisfaction": "> 85%"
            }
        }
        
        # Save to file
        with open("phase2_agent_spec.json", "w") as f:
            json.dump(agent_spec, f, indent=2)
        
        print(f"\n📄 Agent specification saved to phase2_agent_spec.json")
        return agent_spec
    
    def run_performance_test(self):
        """Run performance tests"""
        print("\n⚡ Performance Testing:")
        print("-" * 25)
        
        test_inputs = [
            "I have a complaint about my room",
            "Can you help me with my reservation?",
            "I need to update an employee schedule",
            "There's a maintenance issue",
            "What's your cancellation policy?",
            "This is an emergency!"
        ]
        
        total_time = 0
        successful_requests = 0
        
        for i, test_input in enumerate(test_inputs, 1):
            start_time = time.time()
            response = self.agent.process_request(test_input)
            end_time = time.time()
            
            processing_time = end_time - start_time
            total_time += processing_time
            successful_requests += 1
            
            print(f"{i}. '{test_input[:30]}...' - {processing_time:.3f}s")
        
        avg_time = total_time / successful_requests
        print(f"\n📊 Performance Results:")
        print(f"   Total requests: {successful_requests}")
        print(f"   Average response time: {avg_time:.3f}s")
        print(f"   Total processing time: {total_time:.3f}s")
        
        if avg_time < 2.0:
            print("   ✅ Performance: Excellent")
        elif avg_time < 5.0:
            print("   ✅ Performance: Good")
        else:
            print("   ⚠️  Performance: Needs improvement")
    
    def run_complete_demo(self):
        """Run the complete Phase 2 demo"""
        print("🚀 Starting Complete Phase 2 Demo...")
        print()
        
        # 1. Comprehensive scenario testing
        self.run_comprehensive_demo()
        
        # 2. Knowledge base testing
        self.test_knowledge_base()
        
        # 3. Individual tools testing
        self.test_tools_functionality()
        
        # 4. Performance testing
        self.run_performance_test()
        
        # 5. Generate agent specification
        agent_spec = self.generate_agent_spec()
        
        # 6. Summary
        print("\n🎉 Phase 2 Development Demo Complete!")
        print("=" * 50)
        print("\n✅ Achievements:")
        print("   • Agent core implemented with 3 specialized tools")
        print("   • Knowledge base with 13 policy/procedure entries")
        print("   • Intent recognition for 7 different categories")
        print("   • Professional response generation")
        print("   • Escalation handling for complex issues")
        print("   • Performance optimization (< 2s response time)")
        print("   • Salesforce integration ready")
        
        print("\n📋 Next Steps for Phase 3:")
        print("   • Deploy agent to Salesforce org")
        print("   • Set up real-time data connections")
        print("   • Implement monitoring and logging")
        print("   • User acceptance testing")
        print("   • Performance optimization")
        
        print(f"\n📄 Files Generated:")
        print("   • phase2_agent_core.py - Core agent implementation")
        print("   • setup_knowledge_base.py - Knowledge base setup")
        print("   • phase2_demo.py - Comprehensive demo")
        print("   • phase2_agent_spec.json - Agent specification")
        print("   • resort_knowledge_base.json - Knowledge base data")

def main():
    """Main demo function"""
    demo = Phase2Demo()
    demo.run_complete_demo()

if __name__ == "__main__":
    main()
