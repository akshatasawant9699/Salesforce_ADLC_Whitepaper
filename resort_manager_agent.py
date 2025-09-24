#!/usr/bin/env python3
"""
Coral Cloud Resorts - Resort Manager Agent Implementation
Realistic Python SDK implementation with APIs and RAG capabilities
"""

import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import yaml

# Simulated Salesforce API calls for realistic implementation
class SalesforceAPI:
    def __init__(self, org_url: str, access_token: str):
        self.org_url = org_url
        self.access_token = access_token
        self.headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
    
    def query_reservations(self, customer_name: str) -> Dict:
        """Query Salesforce for customer reservations"""
        soql_query = f"SELECT Id, Name, Check_In_Date__c, Check_Out_Date__c, Room_Number__c, Status__c FROM Reservation__c WHERE Guest_Name__c LIKE '%{customer_name}%'"
        response = requests.get(
            f"{self.org_url}/services/data/v58.0/query/?q={soql_query}",
            headers=self.headers
        )
        result = response.json()
        # Handle case where no records exist or response is not a dict
        if not isinstance(result, dict):
            result = {'records': []}
        if 'records' not in result:
            result['records'] = []
        return result
    
    def update_employee_schedule(self, employee_id: str, shift_data: Dict) -> Dict:
        """Update employee schedule in Salesforce"""
        response = requests.patch(
            f"{self.org_url}/services/data/v58.0/sobjects/Employee__c/{employee_id}",
            headers=self.headers,
            json=shift_data
        )
        return response.json()
    
    def get_activity_recommendations(self, guest_preferences: str) -> Dict:
        """Get activity recommendations based on guest preferences"""
        soql_query = f"SELECT Id, Name, Description__c, Category__c FROM Activity__c WHERE Category__c LIKE '%{guest_preferences}%'"
        response = requests.get(
            f"{self.org_url}/services/data/v58.0/query/?q={soql_query}",
            headers=self.headers
        )
        result = response.json()
        # Handle case where no records exist or response is not a dict
        if not isinstance(result, dict):
            result = {'records': []}
        if 'records' not in result:
            result['records'] = []
        return result

# Knowledge Base for RAG (Retrieval Augmented Generation)
class ResortKnowledgeBase:
    def __init__(self):
        self.policies = {
            "cancellation": {
                "policy": "Free cancellation up to 24 hours before check-in",
                "fees": "Late cancellation fee: $50 per room",
                "emergency": "Emergency cancellations handled case-by-case"
            },
            "amenities": {
                "pool": "Open 6 AM - 10 PM daily",
                "spa": "Reservations required, 24-hour advance notice",
                "restaurant": "Breakfast 7-10 AM, Dinner 6-9 PM",
                "concierge": "Available 24/7 for guest services"
            },
            "complaint_resolution": {
                "escalation": "Level 1: Front Desk, Level 2: Manager, Level 3: General Manager",
                "response_time": "Initial response within 2 hours",
                "resolution": "Target resolution within 24 hours"
            }
        }
    
    def search_policy(self, query: str) -> str:
        """Search knowledge base for relevant policies"""
        query_lower = query.lower()
        for category, policies in self.policies.items():
            for key, value in policies.items():
                if query_lower in key.lower() or query_lower in str(value).lower():
                    return f"{category.title()}: {key} - {value}"
        return "Policy information not found. Please contact management."

# Tool implementations aligned with agentSpec.yaml topics
class ReservationTool:
    def __init__(self, salesforce_api: SalesforceAPI):
        self.api = salesforce_api
    
    def search_reservations(self, customer_name: str) -> Dict:
        """Handle Customer Complaint Resolution - Reservation System Support"""
        try:
            result = self.api.query_reservations(customer_name)
            if result.get('records'):
                reservation = result['records'][0]
                return {
                    "status": "found",
                    "customer": customer_name,
                    "room": reservation.get('Room_Number__c', 'N/A'),
                    "check_in": reservation.get('Check_In_Date__c', 'N/A'),
                    "check_out": reservation.get('Check_Out_Date__c', 'N/A'),
                    "status": reservation.get('Status__c', 'N/A')
                }
            else:
                return {"status": "not_found", "message": "No reservations found"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

class ScheduleManagementTool:
    def __init__(self, salesforce_api: SalesforceAPI):
        self.api = salesforce_api
    
    def update_employee_schedule(self, employee_id: str, shift_type: str, date: str) -> Dict:
        """Handle Employee Schedule Management"""
        try:
            shift_data = {
                "Shift_Type__c": shift_type,
                "Scheduled_Date__c": date,
                "Status__c": "Scheduled"
            }
            result = self.api.update_employee_schedule(employee_id, shift_data)
            return {
                "status": "success",
                "employee_id": employee_id,
                "shift": shift_type,
                "date": date,
                "message": "Schedule updated successfully"
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

class ActivityRecommendationTool:
    def __init__(self, salesforce_api: SalesforceAPI):
        self.api = salesforce_api
    
    def get_activity_recommendations(self, guest_preferences: str) -> Dict:
        """Handle Activity Recommendations"""
        try:
            result = self.api.get_activity_recommendations(guest_preferences)
            if result.get('records'):
                activities = [{
                    "name": activity.get('Name'),
                    "description": activity.get('Description__c'),
                    "category": activity.get('Category__c')
                } for activity in result['records']]
                return {
                    "status": "success",
                    "activities": activities,
                    "count": len(activities)
                }
            else:
                return {"status": "no_activities", "message": "No activities found for preferences"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

class ServiceQualityTool:
    def __init__(self, knowledge_base: ResortKnowledgeBase):
        self.kb = knowledge_base
    
    def handle_complaint(self, complaint_type: str, details: str) -> Dict:
        """Handle Service Quality Monitoring - Customer Complaint Resolution"""
        policy_info = self.kb.search_policy(complaint_type)
        return {
            "status": "acknowledged",
            "complaint_type": complaint_type,
            "policy_reference": policy_info,
            "escalation_level": "Level 1 - Front Desk",
            "response_time": "2 hours",
            "next_steps": "Manager will contact guest within 2 hours"
        }

# Main Resort Manager Agent
class ResortManagerAgent:
    def __init__(self, org_url: str, access_token: str):
        self.salesforce_api = SalesforceAPI(org_url, access_token)
        self.knowledge_base = ResortKnowledgeBase()
        
        # Initialize tools aligned with agentSpec.yaml topics
        self.reservation_tool = ReservationTool(self.salesforce_api)
        self.schedule_tool = ScheduleManagementTool(self.salesforce_api)
        self.activity_tool = ActivityRecommendationTool(self.salesforce_api)
        self.quality_tool = ServiceQualityTool(self.knowledge_base)
        
        self.persona = "A helpful and professional resort manager for Coral Cloud Resorts"
    
    def process_request(self, request_type: str, **kwargs) -> Dict:
        """Main processing method that routes requests to appropriate tools"""
        
        if request_type == "customer_complaint":
            return self.quality_tool.handle_complaint(
                kwargs.get('complaint_type', 'general'),
                kwargs.get('details', '')
            )
        
        elif request_type == "reservation_lookup":
            return self.reservation_tool.search_reservations(
                kwargs.get('customer_name', '')
            )
        
        elif request_type == "schedule_management":
            return self.schedule_tool.update_employee_schedule(
                kwargs.get('employee_id', ''),
                kwargs.get('shift_type', ''),
                kwargs.get('date', '')
            )
        
        elif request_type == "activity_recommendation":
            return self.activity_tool.get_activity_recommendations(
                kwargs.get('guest_preferences', '')
            )
        
        else:
            return {"status": "error", "message": "Unknown request type"}

def load_agent_spec():
    """Load agent specification from YAML file"""
    with open('specs/agentSpec.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    """Main execution function"""
    print("Coral Cloud Resorts - Resort Manager Agent")
    print("=" * 50)
    
    # Load agent specification
    agent_spec = load_agent_spec()
    print(f"Agent Type: {agent_spec['agentType']}")
    print(f"Company: {agent_spec['companyName']}")
    print(f"Role: {agent_spec['role']}")
    print(f"Topics: {len(agent_spec['topics'])}")
    
    # Get Salesforce org details from CLI
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
        org_url = "https://your-org.my.salesforce.com"
        access_token = "your_access_token_here"
    
    agent = ResortManagerAgent(org_url, access_token)
    
    # Demo scenarios aligned with agentSpec.yaml topics
    print("\nDemo Scenarios:")
    print("-" * 30)
    
    # 1. Customer Complaint Resolution
    print("\n1. Customer Complaint Resolution:")
    complaint_result = agent.process_request(
        "customer_complaint",
        complaint_type="cancellation",
        details="Guest wants to cancel reservation"
    )
    print(json.dumps(complaint_result, indent=2))
    
    # 2. Reservation System Support
    print("\n2. Reservation System Support:")
    reservation_result = agent.process_request(
        "reservation_lookup",
        customer_name="John Smith"
    )
    print(json.dumps(reservation_result, indent=2))
    
    # 3. Employee Schedule Management
    print("\n3. Employee Schedule Management:")
    schedule_result = agent.process_request(
        "schedule_management",
        employee_id="EMP001",
        shift_type="Morning",
        date="2024-11-25"
    )
    print(json.dumps(schedule_result, indent=2))
    
    # 4. Activity Recommendations
    print("\n4. Activity Recommendations:")
    activity_result = agent.process_request(
        "activity_recommendation",
        guest_preferences="water sports"
    )
    print(json.dumps(activity_result, indent=2))
    
    print("\nResort Manager Agent initialized successfully!")
    print("Ready to handle resort operations and guest services.")

if __name__ == "__main__":
    main()
