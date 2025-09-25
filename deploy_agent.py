#!/usr/bin/env python3
"""
Phase 4: Deployment & Release for Resort Manager Agent

This module implements comprehensive deployment and release management for the
Resort Manager Agent using Salesforce DX and Agentforce DX capabilities.
"""

import subprocess
import json
import sys
import os
from typing import Dict, List, Any, Optional
from datetime import datetime
import time

class AgentDeployment:
    """Comprehensive agent deployment and release management"""
    
    def __init__(self, target_org: str = "resorts-demo"):
        self.target_org = target_org
        self.deployment_results = {}
        
    def check_prerequisites(self) -> bool:
        """Check deployment prerequisites"""
        print("🔍 Checking deployment prerequisites...")
        
        # Check Salesforce CLI
        try:
            result = subprocess.run(['sf', '--version'], capture_output=True, text=True, check=True)
            print(f"✅ Salesforce CLI: {result.stdout.strip()}")
        except subprocess.CalledProcessError:
            print("❌ Salesforce CLI not found. Please install it first.")
            return False
        
        # Check org connection
        try:
            result = subprocess.run(['sf', 'org', 'display', '--target-org', self.target_org, '--json'], 
                                 capture_output=True, text=True, check=True)
            org_info = json.loads(result.stdout)
            print(f"✅ Connected to org: {org_info['result']['username']}")
        except subprocess.CalledProcessError:
            print(f"❌ Not connected to org '{self.target_org}'. Please connect first.")
            return False
        
        return True
    
    def deploy_agent_metadata(self) -> Dict[str, Any]:
        """Deploy agent metadata to target org"""
        print("\n🚀 Deploying agent metadata...")
        
        try:
            # Deploy agent metadata
            result = subprocess.run([
                'sf', 'project', 'deploy', 'start',
                '--manifest', 'manifests/Agents.package.xml',
                '--target-org', self.target_org,
                '--wait', '10'
            ], capture_output=True, text=True, check=True)
            
            print("✅ Agent metadata deployed successfully")
            return {
                "status": "success",
                "output": result.stdout,
                "timestamp": datetime.now().isoformat()
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Agent metadata deployment failed: {e.stderr}")
            return {
                "status": "error",
                "error": e.stderr,
                "timestamp": datetime.now().isoformat()
            }
    
    def deploy_agent_tests(self) -> Dict[str, Any]:
        """Deploy agent tests to target org"""
        print("\n🧪 Deploying agent tests...")
        
        try:
            # Deploy agent tests
            result = subprocess.run([
                'sf', 'project', 'deploy', 'start',
                '--manifest', 'manifests/AgentTests.package.xml',
                '--target-org', self.target_org,
                '--wait', '10'
            ], capture_output=True, text=True, check=True)
            
            print("✅ Agent tests deployed successfully")
            return {
                "status": "success",
                "output": result.stdout,
                "timestamp": datetime.now().isoformat()
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Agent tests deployment failed: {e.stderr}")
            return {
                "status": "error",
                "error": e.stderr,
                "timestamp": datetime.now().isoformat()
            }
    
    def deploy_custom_objects(self) -> Dict[str, Any]:
        """Deploy custom objects to target org"""
        print("\n📦 Deploying custom objects...")
        
        try:
            # Deploy custom objects
            result = subprocess.run([
                'sf', 'project', 'deploy', 'start',
                '--source-dir', 'force-app/main/default/objects',
                '--target-org', self.target_org,
                '--wait', '10'
            ], capture_output=True, text=True, check=True)
            
            print("✅ Custom objects deployed successfully")
            return {
                "status": "success",
                "output": result.stdout,
                "timestamp": datetime.now().isoformat()
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Custom objects deployment failed: {e.stderr}")
            return {
                "status": "error",
                "error": e.stderr,
                "timestamp": datetime.now().isoformat()
            }
    
    def verify_agent_deployment(self) -> Dict[str, Any]:
        """Verify agent deployment in target org"""
        print("\n🔍 Verifying agent deployment...")
        
        try:
            # Check if agent exists
            result = subprocess.run([
                'sf', 'data', 'query',
                '--query', 'SELECT Id, Name, DeveloperName FROM Bot WHERE DeveloperName = \'Resort_Manager\'',
                '--target-org', self.target_org,
                '--json'
            ], capture_output=True, text=True, check=True)
            
            agent_data = json.loads(result.stdout)
            
            if agent_data['result']['records']:
                agent = agent_data['result']['records'][0]
                print(f"✅ Agent found: {agent['Name']} (ID: {agent['Id']})")
                return {
                    "status": "success",
                    "agent_id": agent['Id'],
                    "agent_name": agent['Name'],
                    "timestamp": datetime.now().isoformat()
                }
            else:
                print("❌ Agent not found in target org")
                return {
                    "status": "error",
                    "message": "Agent not found",
                    "timestamp": datetime.now().isoformat()
                }
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Agent verification failed: {e.stderr}")
            return {
                "status": "error",
                "error": e.stderr,
                "timestamp": datetime.now().isoformat()
            }
    
    def open_agent_builder(self) -> Dict[str, Any]:
        """Open agent in Agentforce Builder UI"""
        print("\n🌐 Opening agent in Agentforce Builder UI...")
        
        try:
            # Open agent in browser
            result = subprocess.run([
                'sf', 'org', 'open', 'agent',
                '--api-name', 'Resort_Manager',
                '--target-org', self.target_org
            ], capture_output=True, text=True, check=True)
            
            print("✅ Agent opened in Agentforce Builder UI")
            return {
                "status": "success",
                "output": result.stdout,
                "timestamp": datetime.now().isoformat()
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to open agent in UI: {e.stderr}")
            return {
                "status": "error",
                "error": e.stderr,
                "timestamp": datetime.now().isoformat()
            }
    
    def run_deployment_tests(self) -> Dict[str, Any]:
        """Run deployment validation tests"""
        print("\n🧪 Running deployment validation tests...")
        
        try:
            # Run Python SDK tests
            result = subprocess.run([
                'python3', 'adversarial_testing.py'
            ], capture_output=True, text=True, check=True)
            
            print("✅ Deployment validation tests passed")
            return {
                "status": "success",
                "output": result.stdout,
                "timestamp": datetime.now().isoformat()
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Deployment validation tests failed: {e.stderr}")
            return {
                "status": "error",
                "error": e.stderr,
                "timestamp": datetime.now().isoformat()
            }
    
    def generate_deployment_report(self) -> Dict[str, Any]:
        """Generate comprehensive deployment report"""
        report = {
            "deployment_summary": {
                "target_org": self.target_org,
                "deployment_time": datetime.now().isoformat(),
                "status": "completed" if all(r.get("status") == "success" for r in self.deployment_results.values()) else "failed"
            },
            "deployment_results": self.deployment_results,
            "recommendations": self._generate_recommendations()
        }
        
        return report
    
    def _generate_recommendations(self) -> List[str]:
        """Generate deployment recommendations"""
        recommendations = []
        
        if self.deployment_results.get("agent_metadata", {}).get("status") == "success":
            recommendations.append("Agent metadata deployed successfully - ready for production use")
        
        if self.deployment_results.get("agent_tests", {}).get("status") == "success":
            recommendations.append("Agent tests deployed - run validation tests before production")
        
        if self.deployment_results.get("custom_objects", {}).get("status") == "success":
            recommendations.append("Custom objects deployed - verify data access permissions")
        
        if self.deployment_results.get("verification", {}).get("status") == "success":
            recommendations.append("Agent verification successful - ready for user testing")
        
        return recommendations
    
    def deploy_all(self) -> Dict[str, Any]:
        """Deploy all components to target org"""
        print("🚀 Starting comprehensive agent deployment")
        print("=" * 50)
        
        # Check prerequisites
        if not self.check_prerequisites():
            return {"status": "failed", "reason": "Prerequisites not met"}
        
        # Deploy components
        self.deployment_results["agent_metadata"] = self.deploy_agent_metadata()
        self.deployment_results["agent_tests"] = self.deploy_agent_tests()
        self.deployment_results["custom_objects"] = self.deploy_custom_objects()
        self.deployment_results["verification"] = self.verify_agent_deployment()
        
        # Run validation tests
        self.deployment_results["validation_tests"] = self.run_deployment_tests()
        
        # Open agent in UI
        self.deployment_results["ui_access"] = self.open_agent_builder()
        
        # Generate report
        report = self.generate_deployment_report()
        
        # Print summary
        self._print_deployment_summary(report)
        
        return report
    
    def _print_deployment_summary(self, report: Dict[str, Any]):
        """Print deployment summary"""
        print("\n" + "=" * 60)
        print("📊 DEPLOYMENT SUMMARY")
        print("=" * 60)
        
        summary = report["deployment_summary"]
        print(f"Target Org: {summary['target_org']}")
        print(f"Deployment Time: {summary['deployment_time']}")
        print(f"Overall Status: {summary['status'].upper()}")
        
        print(f"\n📋 COMPONENT STATUS:")
        for component, result in self.deployment_results.items():
            status = result.get("status", "unknown")
            if status == "success":
                print(f"   {component.replace('_', ' ').title()}: ✅ Success")
            else:
                print(f"   {component.replace('_', ' ').title()}: ❌ Failed")
        
        if report["recommendations"]:
            print(f"\n💡 RECOMMENDATIONS:")
            for i, rec in enumerate(report["recommendations"], 1):
                print(f"   {i}. {rec}")
        
        print("=" * 60)


def main():
    """Main deployment function"""
    print("🏨 Resort Manager Agent - Phase 4: Deployment & Release")
    print("=" * 60)
    
    # Initialize deployment
    deployment = AgentDeployment(target_org="resorts-demo")
    
    # Deploy all components
    report = deployment.deploy_all()
    
    # Save deployment report
    with open("deployment_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"\n💾 Deployment report saved to: deployment_report.json")
    
    # Return exit code based on deployment status
    if report["deployment_summary"]["status"] == "completed":
        print("\n🎉 Deployment completed successfully!")
        print("🚀 Resort Manager Agent is ready for production!")
        return 0
    else:
        print("\n⚠️  Deployment completed with issues. Please review the report.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
