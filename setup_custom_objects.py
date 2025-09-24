#!/usr/bin/env python3
"""
Custom Objects Setup Script for Resort Manager Agent
Creates Reservation__c, Activity__c, and Employee__c objects in Salesforce
"""

import os
import subprocess
import json
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(f"✅ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:")
        print(f"   Command: {command}")
        print(f"   Error: {e.stderr}")
        return None

def check_prerequisites():
    """Check if required tools are available"""
    print("🔍 Checking prerequisites...")
    
    # Check Python version
    if sys.version_info < (3, 9):
        print("❌ Python 3.9+ required")
        return False
    
    # Check Salesforce CLI
    result = run_command("sf --version", "Checking Salesforce CLI")
    if not result:
        print("❌ Salesforce CLI not found. Please install it first.")
        return False
    
    # Check org connection
    result = run_command("sf org list", "Checking Salesforce org connection")
    if not result:
        print("❌ No Salesforce org connected. Please run 'sf org login web' first.")
        return False
    
    print("✅ All prerequisites met")
    return True

def create_metadata_directories():
    """Create required directory structure"""
    print("📁 Creating metadata directories...")
    
    directories = [
        "force-app/main/default/objects",
        "force-app/main/default/objects/Reservation__c",
        "force-app/main/default/objects/Activity__c", 
        "force-app/main/default/objects/Employee__c"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   Created: {directory}")
    
    print("✅ Directory structure created")

def create_reservation_metadata():
    """Create Reservation__c object metadata"""
    print("📝 Creating Reservation__c metadata...")
    
    metadata = '''<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Reservation__c</fullName>
    <description>Reservation object for Resort Manager Agent</description>
    <label>Reservation</label>
    <pluralLabel>Reservations</pluralLabel>
    <nameField>
        <displayFormat>RES-{0000}</displayFormat>
        <label>Reservation Name</label>
        <type>AutoNumber</type>
    </nameField>
    <deploymentStatus>Deployed</deploymentStatus>
    <enableActivities>true</enableActivities>
    <enableBulkApi>true</enableBulkApi>
    <enableFeeds>true</enableFeeds>
    <enableHistory>true</enableHistory>
    <enableLicensing>false</enableLicensing>
    <enableReports>true</enableReports>
    <enableSearch>true</enableSearch>
    <enableSharing>true</enableSharing>
    <enableStreamingApi>true</enableStreamingApi>
    <externalSharingModel>Private</externalSharingModel>
    <sharingModel>ReadWrite</sharingModel>
    <visibility>Public</visibility>
    <fields>
        <fullName>Guest_Name__c</fullName>
        <label>Guest Name</label>
        <type>Text</type>
        <length>100</length>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
    </fields>
    <fields>
        <fullName>Check_In_Date__c</fullName>
        <label>Check In Date</label>
        <type>Date</type>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
    </fields>
    <fields>
        <fullName>Check_Out_Date__c</fullName>
        <label>Check Out Date</label>
        <type>Date</type>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
    </fields>
    <fields>
        <fullName>Room_Number__c</fullName>
        <label>Room Number</label>
        <type>Text</type>
        <length>10</length>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
    </fields>
    <fields>
        <fullName>Status__c</fullName>
        <label>Status</label>
        <type>Picklist</type>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
        <valueSet>
            <restricted>true</restricted>
            <valueSetDefinition>
                <sorted>false</sorted>
                <value>
                    <fullName>Confirmed</fullName>
                    <default>false</default>
                    <label>Confirmed</label>
                </value>
                <value>
                    <fullName>Checked-in</fullName>
                    <default>false</default>
                    <label>Checked-in</label>
                </value>
                <value>
                    <fullName>Checked-out</fullName>
                    <default>false</default>
                    <label>Checked-out</label>
                </value>
                <value>
                    <fullName>Cancelled</fullName>
                    <default>false</default>
                    <label>Cancelled</label>
                </value>
            </valueSetDefinition>
        </valueSet>
    </fields>
</CustomObject>'''
    
    with open("force-app/main/default/objects/Reservation__c.object-meta.xml", "w") as f:
        f.write(metadata)
    print("✅ Reservation__c metadata created")

def create_activity_metadata():
    """Create Activity__c object metadata"""
    print("📝 Creating Activity__c metadata...")
    
    metadata = '''<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Activity__c</fullName>
    <description>Activity object for Resort Manager Agent</description>
    <label>Activity</label>
    <pluralLabel>Activities</pluralLabel>
    <nameField>
        <displayFormat>ACT-{0000}</displayFormat>
        <label>Activity Name</label>
        <type>AutoNumber</type>
    </nameField>
    <deploymentStatus>Deployed</deploymentStatus>
    <enableActivities>true</enableActivities>
    <enableBulkApi>true</enableBulkApi>
    <enableFeeds>true</enableFeeds>
    <enableHistory>true</enableHistory>
    <enableLicensing>false</enableLicensing>
    <enableReports>true</enableReports>
    <enableSearch>true</enableSearch>
    <enableSharing>true</enableSharing>
    <enableStreamingApi>true</enableStreamingApi>
    <externalSharingModel>Private</externalSharingModel>
    <sharingModel>ReadWrite</sharingModel>
    <visibility>Public</visibility>
    <fields>
        <fullName>Description__c</fullName>
        <label>Description</label>
        <type>LongTextArea</type>
        <length>1000</length>
        <visibleLines>3</visibleLines>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
    </fields>
    <fields>
        <fullName>Category__c</fullName>
        <label>Category</label>
        <type>Text</type>
        <length>50</length>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
    </fields>
</CustomObject>'''
    
    with open("force-app/main/default/objects/Activity__c.object-meta.xml", "w") as f:
        f.write(metadata)
    print("✅ Activity__c metadata created")

def create_employee_metadata():
    """Create Employee__c object metadata"""
    print("📝 Creating Employee__c metadata...")
    
    metadata = '''<?xml version="1.0" encoding="UTF-8"?>
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">
    <fullName>Employee__c</fullName>
    <description>Employee object for Resort Manager Agent</description>
    <label>Employee</label>
    <pluralLabel>Employees</pluralLabel>
    <nameField>
        <displayFormat>EMP-{0000}</displayFormat>
        <label>Employee Name</label>
        <type>AutoNumber</type>
    </nameField>
    <deploymentStatus>Deployed</deploymentStatus>
    <enableActivities>true</enableActivities>
    <enableBulkApi>true</enableBulkApi>
    <enableFeeds>true</enableFeeds>
    <enableHistory>true</enableHistory>
    <enableLicensing>false</enableLicensing>
    <enableReports>true</enableReports>
    <enableSearch>true</enableSearch>
    <enableSharing>true</enableSharing>
    <enableStreamingApi>true</enableStreamingApi>
    <externalSharingModel>Private</externalSharingModel>
    <sharingModel>ReadWrite</sharingModel>
    <visibility>Public</visibility>
    <fields>
        <fullName>Shift_Type__c</fullName>
        <label>Shift Type</label>
        <type>Text</type>
        <length>50</length>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
    </fields>
    <fields>
        <fullName>Scheduled_Date__c</fullName>
        <label>Scheduled Date</label>
        <type>Date</type>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
    </fields>
    <fields>
        <fullName>Status__c</fullName>
        <label>Status</label>
        <type>Picklist</type>
        <required>false</required>
        <trackFeedHistory>false</trackFeedHistory>
        <trackHistory>false</trackHistory>
        <trackTrending>false</trackTrending>
        <unique>false</unique>
        <valueSet>
            <restricted>true</restricted>
            <valueSetDefinition>
                <sorted>false</sorted>
                <value>
                    <fullName>Scheduled</fullName>
                    <default>false</default>
                    <label>Scheduled</label>
                </value>
                <value>
                    <fullName>Completed</fullName>
                    <default>false</default>
                    <label>Completed</label>
                </value>
                <value>
                    <fullName>Cancelled</fullName>
                    <default>false</default>
                    <label>Cancelled</label>
                </value>
            </valueSetDefinition>
        </valueSet>
    </fields>
</CustomObject>'''
    
    with open("force-app/main/default/objects/Employee__c.object-meta.xml", "w") as f:
        f.write(metadata)
    print("✅ Employee__c metadata created")

def deploy_to_salesforce():
    """Deploy custom objects to Salesforce"""
    print("🚀 Deploying custom objects to Salesforce...")
    
    result = run_command("sf project deploy start --target-org resorts-demo", "Deploying custom objects")
    if result:
        print("✅ Custom objects deployed successfully")
        return True
    else:
        print("❌ Deployment failed")
        return False

def verify_deployment():
    """Verify that custom objects were created successfully"""
    print("🔍 Verifying custom objects creation...")
    
    objects_to_verify = ["Reservation__c", "Activity__c", "Employee__c"]
    
    for obj in objects_to_verify:
        result = run_command(f'sf data query --query "SELECT Id, Name FROM {obj} LIMIT 1" --target-org resorts-demo', f"Verifying {obj}")
        if result:
            print(f"✅ {obj} is accessible")
        else:
            print(f"❌ {obj} verification failed")
            return False
    
    print("✅ All custom objects verified successfully")
    return True

def insert_sample_data():
    """Insert sample data for testing"""
    print("📊 Inserting sample data...")
    
    sample_data = [
        {
            "object": "Reservation__c",
            "values": "Name=RES-0001"
        },
        {
            "object": "Activity__c", 
            "values": "Name=ACT-0001"
        },
        {
            "object": "Employee__c",
            "values": "Name=EMP-0001"
        }
    ]
    
    for data in sample_data:
        result = run_command(f'sf data create record --sobject {data["object"]} --values "{data["values"]}" --target-org resorts-demo', f"Creating sample {data['object']}")
        if result:
            print(f"✅ Sample {data['object']} created")
        else:
            print(f"⚠️  Sample {data['object']} creation failed (this is optional)")
    
    print("✅ Sample data insertion completed")

def main():
    """Main execution function"""
    print("🏨 Resort Manager Agent - Custom Objects Setup")
    print("=" * 50)
    
    # Check prerequisites
    if not check_prerequisites():
        print("❌ Prerequisites not met. Please fix the issues above and try again.")
        return False
    
    # Create directory structure
    create_metadata_directories()
    
    # Create metadata files
    create_reservation_metadata()
    create_activity_metadata()
    create_employee_metadata()
    
    # Deploy to Salesforce
    if not deploy_to_salesforce():
        print("❌ Deployment failed. Please check your Salesforce org connection and permissions.")
        return False
    
    # Verify deployment
    if not verify_deployment():
        print("❌ Verification failed. Please check the deployment logs.")
        return False
    
    # Insert sample data
    insert_sample_data()
    
    print("\n🎉 Custom Objects Setup Complete!")
    print("=" * 50)
    print("✅ Reservation__c object created")
    print("✅ Activity__c object created") 
    print("✅ Employee__c object created")
    print("✅ All objects verified and accessible")
    print("\n🚀 Your Resort Manager Agent is ready for Phase 3!")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
