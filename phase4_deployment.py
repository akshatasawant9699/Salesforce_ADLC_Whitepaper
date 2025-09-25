#!/usr/bin/env python3
"""
Phase 4: Deployment & Release - Comprehensive Implementation

This module orchestrates the complete Phase 4 implementation including:
- Agent metadata deployment
- Custom objects deployment
- Production environment setup
- Release management
- Version control integration
"""

import subprocess
import json
import sys
import os
from typing import Dict, List, Any, Optional
from datetime import datetime
import time

from deploy_agent import AgentDeployment
from release_management import ReleaseManager

class Phase4Orchestrator:
    """Orchestrates complete Phase 4: Deployment & Release"""
    
    def __init__(self, source_org: str = "resorts-demo", target_org: str = "production"):
        self.source_org = source_org
        self.target_org = target_org
        self.phase4_results = {}
        
    def run_phase4(self) -> Dict[str, Any]:
        """Run complete Phase 4: Deployment & Release"""
        print("🚀 Phase 4: Deployment & Release - Complete Implementation")
        print("=" * 70)
        
        # Step 1: Agent Deployment
        print("\n📦 Step 1: Agent Deployment")
        print("-" * 40)
        deployment = AgentDeployment(target_org=self.source_org)
        deployment_result = deployment.deploy_all()
        self.phase4_results["agent_deployment"] = deployment_result
        
        # Step 2: Release Management
        print("\n📋 Step 2: Release Management")
        print("-" * 40)
        release_manager = ReleaseManager(
            source_org=self.source_org,
            target_org=self.target_org
        )
        release_result = release_manager.manage_release()
        self.phase4_results["release_management"] = release_result
        
        # Step 3: Production Validation
        print("\n🧪 Step 3: Production Validation")
        print("-" * 40)
        validation_result = self._run_production_validation()
        self.phase4_results["production_validation"] = validation_result
        
        # Step 4: Version Control Integration
        print("\n📚 Step 4: Version Control Integration")
        print("-" * 40)
        vc_result = self._integrate_version_control()
        self.phase4_results["version_control"] = vc_result
        
        # Generate comprehensive report
        report = self._generate_phase4_report()
        
        # Print final summary
        self._print_phase4_summary(report)
        
        return report
    
    def _run_production_validation(self) -> Dict[str, Any]:
        """Run production validation tests"""
        print("🔍 Running production validation...")
        
        try:
            # Run comprehensive test suite
            result = subprocess.run([
                'python3', 'test_runner.py'
            ], capture_output=True, text=True, check=True)
            
            print("✅ Production validation completed successfully")
            return {
                "status": "success",
                "output": result.stdout,
                "timestamp": datetime.now().isoformat()
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Production validation failed: {e.stderr}")
            return {
                "status": "error",
                "error": e.stderr,
                "timestamp": datetime.now().isoformat()
            }
    
    def _integrate_version_control(self) -> Dict[str, Any]:
        """Integrate with version control system"""
        print("📚 Integrating with version control...")
        
        try:
            # Create deployment branch
            subprocess.run(['git', 'checkout', '-b', 'phase4-deployment'], check=True)
            
            # Add deployment files
            subprocess.run(['git', 'add', 'deploy_agent.py'], check=True)
            subprocess.run(['git', 'add', 'release_management.py'], check=True)
            subprocess.run(['git', 'add', 'manifests/'], check=True)
            
            # Commit deployment changes
            subprocess.run([
                'git', 'commit', '-m', 
                'Phase 4: Add deployment and release management capabilities\n\n- Added comprehensive agent deployment framework\n- Added release management with version control\n- Added production validation and testing\n- Added deployment manifests and orchestration'
            ], check=True)
            
            # Create deployment tag
            subprocess.run([
                'git', 'tag', '-a', 'v1.0.0-deployment', 
                '-m', 'Phase 4: Deployment & Release - Version 1.0.0'
            ], check=True)
            
            print("✅ Version control integration completed")
            return {
                "status": "success",
                "branch": "phase4-deployment",
                "tag": "v1.0.0-deployment",
                "timestamp": datetime.now().isoformat()
            }
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Version control integration failed: {e.stderr}")
            return {
                "status": "error",
                "error": e.stderr,
                "timestamp": datetime.now().isoformat()
            }
    
    def _generate_phase4_report(self) -> Dict[str, Any]:
        """Generate comprehensive Phase 4 report"""
        report = {
            "phase4_summary": {
                "phase": "Deployment & Release",
                "version": "1.0.0",
                "completion_date": datetime.now().isoformat(),
                "source_org": self.source_org,
                "target_org": self.target_org,
                "status": "completed" if all(
                    r.get("status") == "success" or r.get("deployment_summary", {}).get("status") == "completed"
                    for r in self.phase4_results.values()
                ) else "failed"
            },
            "phase4_results": self.phase4_results,
            "deployment_artifacts": [
                "deploy_agent.py - Agent deployment framework",
                "release_management.py - Release management system",
                "manifests/Agents.package.xml - Agent metadata manifest",
                "manifests/AgentTests.package.xml - Agent tests manifest",
                "deployment_report.json - Deployment results",
                "release_report.json - Release management results"
            ],
            "production_readiness": {
                "agent_deployed": self.phase4_results.get("agent_deployment", {}).get("deployment_summary", {}).get("status") == "completed",
                "release_managed": self.phase4_results.get("release_management", {}).get("release_summary", {}).get("status") == "completed",
                "validation_passed": self.phase4_results.get("production_validation", {}).get("status") == "success",
                "version_controlled": self.phase4_results.get("version_control", {}).get("status") == "success"
            }
        }
        
        return report
    
    def _print_phase4_summary(self, report: Dict[str, Any]):
        """Print Phase 4 summary"""
        print("\n" + "=" * 70)
        print("📊 PHASE 4: DEPLOYMENT & RELEASE - SUMMARY")
        print("=" * 70)
        
        summary = report["phase4_summary"]
        print(f"Phase: {summary['phase']}")
        print(f"Version: {summary['version']}")
        print(f"Completion Date: {summary['completion_date']}")
        print(f"Source Org: {summary['source_org']}")
        print(f"Target Org: {summary['target_org']}")
        print(f"Overall Status: {summary['status'].upper()}")
        
        print(f"\n📋 PHASE 4 COMPONENTS:")
        for component, result in self.phase4_results.items():
            if isinstance(result, dict) and "status" in result:
                status = result.get("status", "unknown")
            elif isinstance(result, dict) and "deployment_summary" in result:
                status = result.get("deployment_summary", {}).get("status", "unknown")
            else:
                status = "completed"
            
            if status == "success" or status == "completed":
                print(f"   {component.replace('_', ' ').title()}: ✅ Success")
            else:
                print(f"   {component.replace('_', ' ').title()}: ❌ Failed")
        
        print(f"\n🚀 PRODUCTION READINESS:")
        readiness = report["production_readiness"]
        for check, status in readiness.items():
            status_icon = "✅" if status else "❌"
            print(f"   {check.replace('_', ' ').title()}: {status_icon}")
        
        print(f"\n📦 DEPLOYMENT ARTIFACTS:")
        for artifact in report["deployment_artifacts"]:
            print(f"   • {artifact}")
        
        print("=" * 70)


def main():
    """Main Phase 4 orchestration function"""
    print("🏨 Resort Manager Agent - Phase 4: Deployment & Release")
    print("=" * 60)
    
    # Initialize Phase 4 orchestrator
    orchestrator = Phase4Orchestrator(
        source_org="resorts-demo",
        target_org="production"
    )
    
    # Run complete Phase 4
    report = orchestrator.run_phase4()
    
    # Save Phase 4 report
    with open("phase4_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"\n💾 Phase 4 report saved to: phase4_report.json")
    
    # Return exit code based on Phase 4 status
    if report["phase4_summary"]["status"] == "completed":
        print("\n🎉 Phase 4: Deployment & Release completed successfully!")
        print("🚀 Resort Manager Agent is ready for production deployment!")
        return 0
    else:
        print("\n⚠️  Phase 4 completed with issues. Please review the report.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
