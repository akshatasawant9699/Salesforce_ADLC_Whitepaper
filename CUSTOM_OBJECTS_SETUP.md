# Custom Objects Setup for Resort Manager Agent

This document contains the detailed steps for creating custom objects in Salesforce that are required for the Resort Manager Agent.

## Quick Setup (Recommended)

**Use the automated script for one-command setup:**

```bash
python3 setup_custom_objects.py
```

This script will:
- ✅ Check all prerequisites
- ✅ Create required directory structure
- ✅ Generate all metadata files
- ✅ Deploy to Salesforce
- ✅ Verify deployment
- ✅ Insert sample data

## Manual Setup (Alternative)

If you prefer to run the commands manually:

### Prerequisites

- Salesforce org connected via CLI (`sf org list` should show your org)
- Admin permissions in the Salesforce org

### Custom Objects Required

The Resort Manager Agent requires three custom objects:

1. **Reservation__c** - For guest reservations
2. **Activity__c** - For resort activities  
3. **Employee__c** - For employee scheduling

### Manual Setup Steps

#### 1. Create Custom Object Metadata Files

The metadata files are already created in `force-app/main/default/objects/`:

- `Reservation__c.object-meta.xml`
- `Activity__c.object-meta.xml` 
- `Employee__c.object-meta.xml`

#### 2. Deploy Custom Objects to Salesforce

```bash
# Deploy all custom objects and fields to org
sf project deploy start --target-org resorts-demo
```

#### 3. Verify Custom Objects Creation

```bash
# Test that custom objects exist and are accessible
sf data query --query "SELECT Id, Name FROM Reservation__c LIMIT 1" --target-org resorts-demo
sf data query --query "SELECT Id, Name FROM Activity__c LIMIT 1" --target-org resorts-demo
sf data query --query "SELECT Id, Name FROM Employee__c LIMIT 1" --target-org resorts-demo
```

#### 4. Insert Sample Data (Optional)

```bash
# Insert sample data for testing
sf data create record --sobject Reservation__c --values "Name=RES-0001" --target-org resorts-demo
sf data create record --sobject Activity__c --values "Name=ACT-0001" --target-org resorts-demo
sf data create record --sobject Employee__c --values "Name=EMP-0001" --target-org resorts-demo
```

## Object Schema

### Reservation__c Fields
- `Name` (AutoNumber) - RES-{0000}
- `Guest_Name__c` (Text) - Guest name
- `Check_In_Date__c` (Date) - Check-in date
- `Check_Out_Date__c` (Date) - Check-out date
- `Room_Number__c` (Text) - Room number
- `Status__c` (Picklist) - Confirmed, Checked-in, Checked-out, Cancelled

### Activity__c Fields
- `Name` (AutoNumber) - ACT-{0000}
- `Description__c` (LongTextArea) - Activity description
- `Category__c` (Text) - Activity category

### Employee__c Fields
- `Name` (AutoNumber) - EMP-{0000}
- `Shift_Type__c` (Text) - Shift type
- `Scheduled_Date__c` (Date) - Scheduled date
- `Status__c` (Picklist) - Scheduled, Completed, Cancelled

## Troubleshooting

If deployment fails, check:
1. Org permissions - ensure you have admin access
2. Field validation - ensure all required fields are properly defined
3. Picklist values - ensure all picklist values are correctly configured

## Success Criteria

- All three custom objects are created in Salesforce
- Objects are queryable via SOQL
- All custom fields are accessible
- Sample data can be inserted successfully
