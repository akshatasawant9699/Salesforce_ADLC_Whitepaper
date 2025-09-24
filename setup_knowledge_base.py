#!/usr/bin/env python3
"""
Knowledge Base Setup for Coral Cloud Resorts Agent
=================================================

This script sets up the knowledge base with resort policies, procedures,
and operational information for the AI agent.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

class ResortKnowledgeBase:
    """Knowledge base for resort policies and procedures"""
    
    def __init__(self):
        self.knowledge_base = {
            "policies": {
                "cancellation": {
                    "title": "Cancellation Policy",
                    "content": "Reservations can be cancelled up to 24 hours before check-in for a full refund. Cancellations within 24 hours are subject to a one-night charge. Group bookings (10+ rooms) require 72-hour notice.",
                    "examples": [
                        "24-hour cancellation window for individual bookings",
                        "One-night penalty for late cancellation",
                        "72-hour notice required for group bookings",
                        "No-show charges apply after 6 PM on arrival day"
                    ],
                    "keywords": ["cancellation", "refund", "penalty", "no-show", "group booking"]
                },
                "check_in_out": {
                    "title": "Check-in and Check-out Policy",
                    "content": "Check-in time is 3:00 PM. Check-out time is 11:00 AM. Early check-in and late check-out may be available based on room availability for an additional fee.",
                    "examples": [
                        "Check-in: 3:00 PM",
                        "Check-out: 11:00 AM", 
                        "Early check-in: $25 fee if available",
                        "Late check-out: $25 fee if available",
                        "Valid ID required for check-in"
                    ],
                    "keywords": ["check-in", "check-out", "early", "late", "ID", "valid"]
                },
                "pets": {
                    "title": "Pet Policy",
                    "content": "Pets are welcome in designated pet-friendly rooms for an additional $25 per night. Maximum 2 pets per room. Pet-friendly rooms are limited and subject to availability.",
                    "examples": [
                        "$25 per night pet fee",
                        "Maximum 2 pets per room",
                        "Limited pet-friendly rooms",
                        "Pets must be leashed in public areas",
                        "Pet damage charges may apply"
                    ],
                    "keywords": ["pet", "dog", "cat", "animal", "fee", "leashed"]
                },
                "amenities": {
                    "title": "Amenity Usage Policy",
                    "content": "Pool hours are 6 AM to 10 PM. Spa services require advance booking. Fitness center is open 24/7 for guests. Tennis courts available 7 AM to 9 PM.",
                    "examples": [
                        "Pool: 6 AM - 10 PM",
                        "Spa: Advance booking required",
                        "Fitness center: 24/7 access",
                        "Tennis courts: 7 AM - 9 PM",
                        "Beach access: Sunrise to sunset"
                    ],
                    "keywords": ["pool", "spa", "fitness", "tennis", "beach", "amenities"]
                },
                "parking": {
                    "title": "Parking Policy",
                    "content": "Complimentary self-parking is available for all guests. Valet parking is available for $15 per night. Oversized vehicles may require special arrangements.",
                    "examples": [
                        "Complimentary self-parking",
                        "Valet parking: $15/night",
                        "Oversized vehicles: Special arrangements",
                        "Parking spaces limited during peak season"
                    ],
                    "keywords": ["parking", "valet", "self-park", "oversized", "complimentary"]
                }
            },
            "procedures": {
                "emergency": {
                    "title": "Emergency Procedures",
                    "content": "For life-threatening emergencies, call 911 immediately. For non-emergency urgent matters, contact front desk at extension 0. Emergency exits are clearly marked throughout the resort.",
                    "examples": [
                        "Life-threatening: Call 911 immediately",
                        "Non-emergency urgent: Front desk extension 0",
                        "Emergency exits clearly marked",
                        "Fire alarm: Follow exit signs",
                        "Medical emergency: Call 911, then notify front desk"
                    ],
                    "keywords": ["emergency", "911", "urgent", "fire", "medical", "exit"]
                },
                "maintenance": {
                    "title": "Maintenance Request Procedure",
                    "content": "Non-emergency maintenance requests should be reported to front desk. Emergency maintenance (plumbing, electrical, HVAC) should be reported immediately. Response times: Emergency (30 min), Urgent (2 hours), Standard (24 hours).",
                    "examples": [
                        "Emergency maintenance: Report immediately",
                        "Standard requests: 24-hour response",
                        "Urgent requests: 2-hour response",
                        "Emergency response: 30 minutes",
                        "After-hours: Contact security at extension 911"
                    ],
                    "keywords": ["maintenance", "repair", "broken", "plumbing", "electrical", "HVAC"]
                },
                "guest_services": {
                    "title": "Guest Services Procedures",
                    "content": "Concierge services available 7 AM to 10 PM. Room service available 6 AM to 11 PM. Housekeeping service available 8 AM to 6 PM. Special requests should be made at least 24 hours in advance.",
                    "examples": [
                        "Concierge: 7 AM - 10 PM",
                        "Room service: 6 AM - 11 PM",
                        "Housekeeping: 8 AM - 6 PM",
                        "Special requests: 24-hour advance notice",
                        "Late check-out: Request by 10 AM"
                    ],
                    "keywords": ["concierge", "room service", "housekeeping", "special request", "late check-out"]
                }
            },
            "facilities": {
                "rooms": {
                    "title": "Room Information",
                    "content": "We offer Standard, Deluxe, Suite, and Presidential Suite accommodations. All rooms include WiFi, mini-fridge, coffee maker, and daily housekeeping. Suites include additional amenities.",
                    "examples": [
                        "Room types: Standard, Deluxe, Suite, Presidential",
                        "All rooms: WiFi, mini-fridge, coffee maker",
                        "Suites: Additional amenities included",
                        "Daily housekeeping service",
                        "Room upgrades available based on availability"
                    ],
                    "keywords": ["room", "suite", "WiFi", "amenities", "housekeeping", "upgrade"]
                },
                "dining": {
                    "title": "Dining Options",
                    "content": "Main restaurant: 7 AM - 10 PM. Poolside bar: 11 AM - 9 PM. Room service: 6 AM - 11 PM. Specialty restaurant: 6 PM - 10 PM (reservations required).",
                    "examples": [
                        "Main restaurant: 7 AM - 10 PM",
                        "Poolside bar: 11 AM - 9 PM",
                        "Room service: 6 AM - 11 PM",
                        "Specialty restaurant: 6 PM - 10 PM",
                        "Reservations required for specialty dining"
                    ],
                    "keywords": ["restaurant", "dining", "room service", "bar", "reservations"]
                },
                "activities": {
                    "title": "Resort Activities",
                    "content": "Beach activities, water sports, tennis, golf, spa services, fitness center, and organized excursions. Activity schedules available at concierge desk. Some activities require advance booking.",
                    "examples": [
                        "Beach activities and water sports",
                        "Tennis and golf facilities",
                        "Spa services and fitness center",
                        "Organized excursions available",
                        "Activity schedules at concierge desk"
                    ],
                    "keywords": ["activities", "beach", "tennis", "golf", "spa", "fitness", "excursions"]
                }
            },
            "contact_info": {
                "front_desk": {
                    "title": "Front Desk Contact",
                    "content": "Main number: (555) 123-RESORT. Extension 0 for general inquiries. Extension 1 for reservations. Extension 2 for concierge services.",
                    "examples": [
                        "Main: (555) 123-RESORT",
                        "General inquiries: Extension 0",
                        "Reservations: Extension 1", 
                        "Concierge: Extension 2",
                        "24/7 availability for urgent matters"
                    ],
                    "keywords": ["front desk", "phone", "extension", "contact", "reservations", "concierge"]
                },
                "departments": {
                    "title": "Department Contacts",
                    "content": "Housekeeping: Extension 3. Maintenance: Extension 4. Security: Extension 911. Management: Extension 5. After-hours emergency: Contact security.",
                    "examples": [
                        "Housekeeping: Extension 3",
                        "Maintenance: Extension 4",
                        "Security: Extension 911",
                        "Management: Extension 5",
                        "After-hours: Contact security"
                    ],
                    "keywords": ["housekeeping", "maintenance", "security", "management", "after-hours"]
                }
            }
        }
    
    def search(self, query: str) -> Dict[str, Any]:
        """Search the knowledge base for relevant information"""
        query_lower = query.lower()
        results = []
        
        # Search through all categories
        for category, items in self.knowledge_base.items():
            for item_id, item_data in items.items():
                # Check title and content
                if (query_lower in item_data["title"].lower() or 
                    query_lower in item_data["content"].lower()):
                    results.append({
                        "category": category,
                        "id": item_id,
                        "title": item_data["title"],
                        "content": item_data["content"],
                        "examples": item_data.get("examples", []),
                        "keywords": item_data.get("keywords", [])
                    })
                # Check examples and keywords
                elif any(query_lower in example.lower() for example in item_data.get("examples", [])):
                    results.append({
                        "category": category,
                        "id": item_id,
                        "title": item_data["title"],
                        "content": item_data["content"],
                        "examples": item_data.get("examples", []),
                        "keywords": item_data.get("keywords", [])
                    })
                elif any(query_lower in keyword.lower() for keyword in item_data.get("keywords", [])):
                    results.append({
                        "category": category,
                        "id": item_id,
                        "title": item_data["title"],
                        "content": item_data["content"],
                        "examples": item_data.get("examples", []),
                        "keywords": item_data.get("keywords", [])
                    })
        
        return {
            "status": "success" if results else "not_found",
            "query": query,
            "results": results,
            "count": len(results),
            "message": f"Found {len(results)} matching entries" if results else "No matching information found"
        }
    
    def get_category(self, category: str) -> Dict[str, Any]:
        """Get all items from a specific category"""
        if category in self.knowledge_base:
            return {
                "status": "success",
                "category": category,
                "items": self.knowledge_base[category],
                "count": len(self.knowledge_base[category])
            }
        else:
            return {
                "status": "error",
                "message": f"Category '{category}' not found"
            }
    
    def save_to_file(self, filename: str = "resort_knowledge_base.json"):
        """Save knowledge base to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.knowledge_base, f, indent=2)
        print(f"Knowledge base saved to {filename}")
    
    def load_from_file(self, filename: str = "resort_knowledge_base.json"):
        """Load knowledge base from JSON file"""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.knowledge_base = json.load(f)
            print(f"Knowledge base loaded from {filename}")
        else:
            print(f"File {filename} not found")

def main():
    """Demo the knowledge base functionality"""
    print("🏝️  Coral Cloud Resorts Knowledge Base Setup")
    print("=" * 50)
    
    # Initialize knowledge base
    kb = ResortKnowledgeBase()
    
    # Save to file
    kb.save_to_file()
    
    # Test search functionality
    test_queries = [
        "cancellation policy",
        "pet policy", 
        "emergency procedures",
        "room service hours",
        "maintenance request",
        "check-in time",
        "amenities"
    ]
    
    print("\n🔍 Testing Knowledge Base Search:")
    print("-" * 40)
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        results = kb.search(query)
        print(f"Status: {results['status']}")
        print(f"Results: {results['count']} found")
        
        if results['results']:
            for result in results['results'][:2]:  # Show first 2 results
                print(f"  • {result['title']} ({result['category']})")
                print(f"    {result['content'][:100]}...")
    
    print("\n📊 Knowledge Base Statistics:")
    print("-" * 30)
    total_items = sum(len(category) for category in kb.knowledge_base.values())
    print(f"Total categories: {len(kb.knowledge_base)}")
    print(f"Total items: {total_items}")
    
    for category, items in kb.knowledge_base.items():
        print(f"  {category}: {len(items)} items")
    
    print("\n✅ Knowledge Base Setup Complete!")
    print("\nFeatures:")
    print("• Comprehensive policy information")
    print("• Emergency procedures")
    print("• Facility information")
    print("• Contact information")
    print("• Search functionality")
    print("• JSON export/import")

if __name__ == "__main__":
    main()
