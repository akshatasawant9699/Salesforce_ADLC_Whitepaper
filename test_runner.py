#!/usr/bin/env python3
"""
Phase 3: Comprehensive Test Runner for Resort Manager Agent

This module provides a unified test runner that orchestrates all testing phases:
- Unit Testing (pytest-based)
- End-to-End Testing (conversation scenarios)
- Adversarial Testing (security validation)
- Performance Testing (load and stress testing)
- Integration Testing (Salesforce API integration)

Based on agentforce-sdk testing capabilities and best practices.
"""

import asyncio
import json
import sys
import os
import time
import subprocess
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
import concurrent.futures
import threading

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from agent_sdk import Agentforce
    from agent_sdk.core.auth import BasicAuth
    AGENTFORCE_AVAILABLE = True
except ImportError:
    print("⚠️  agentforce-sdk not available. Using mock implementation for testing.")
    AGENTFORCE_AVAILABLE = False

from test_resort_agent import TestResortManagerAgent, TestEndToEndScenarios, TestAdversarialScenarios, TestPerformanceAndReliability
from e2e_test_scenarios import E2ETestRunner
from adversarial_testing import AdversarialTestSuite

@dataclass
class TestSuite:
    """Represents a test suite with configuration"""
    name: str
    description: str
    test_file: str
    test_class: str
    priority: int
    timeout: int = 300  # 5 minutes default timeout

class ComprehensiveTestRunner:
    """Comprehensive test runner for Resort Manager Agent"""
    
    def __init__(self, org_url: str, access_token: str):
        self.org_url = org_url
        self.access_token = access_token
        self.test_results = {}
        self.start_time = None
        self.end_time = None
        
    def create_test_suites(self) -> List[TestSuite]:
        """Create comprehensive test suite configuration"""
        suites = [
            TestSuite(
                name="Unit Tests",
                description="Unit tests for individual components and functions",
                test_file="test_resort_agent.py",
                test_class="TestResortManagerAgent",
                priority=1,
                timeout=60
            ),
            TestSuite(
                name="End-to-End Scenarios",
                description="E2E testing for complete conversation flows",
                test_file="test_resort_agent.py",
                test_class="TestEndToEndScenarios",
                priority=1,
                timeout=120
            ),
            TestSuite(
                name="Adversarial Security Tests",
                description="Security testing for vulnerability assessment",
                test_file="test_resort_agent.py",
                test_class="TestAdversarialScenarios",
                priority=1,
                timeout=180
            ),
            TestSuite(
                name="Performance Tests",
                description="Performance and reliability testing",
                test_file="test_resort_agent.py",
                test_class="TestPerformanceAndReliability",
                priority=2,
                timeout=300
            ),
            TestSuite(
                name="E2E Conversation Tests",
                description="Advanced E2E testing with conversation scenarios",
                test_file="e2e_test_scenarios.py",
                test_class="E2ETestRunner",
                priority=2,
                timeout=240
            ),
            TestSuite(
                name="Adversarial Security Suite",
                description="Comprehensive adversarial testing suite",
                test_file="adversarial_testing.py",
                test_class="AdversarialTestSuite",
                priority=1,
                timeout=300
            )
        ]
        
        return suites
    
    def run_pytest_tests(self, test_file: str, test_class: str = None) -> Dict[str, Any]:
        """Run pytest-based tests and return results"""
        print(f"\n🧪 Running pytest tests: {test_file}")
        
        # Build pytest command
        cmd = ["python", "-m", "pytest", test_file, "-v", "--tb=short", "--color=yes"]
        if test_class:
            cmd.extend(["-k", test_class])
        
        try:
            # Run pytest with timeout
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            # Parse results
            output_lines = result.stdout.split('\n')
            error_lines = result.stderr.split('\n')
            
            # Count test results
            passed = len([line for line in output_lines if "PASSED" in line])
            failed = len([line for line in output_lines if "FAILED" in line])
            errors = len([line for line in output_lines if "ERROR" in line])
            
            return {
                "status": "completed" if result.returncode == 0 else "failed",
                "exit_code": result.returncode,
                "passed": passed,
                "failed": failed,
                "errors": errors,
                "output": result.stdout,
                "errors_output": result.stderr,
                "duration": 0  # Would need to measure separately
            }
            
        except subprocess.TimeoutExpired:
            return {
                "status": "timeout",
                "exit_code": -1,
                "passed": 0,
                "failed": 0,
                "errors": 1,
                "output": "Test execution timed out",
                "errors_output": "Timeout after 300 seconds",
                "duration": 300
            }
        except Exception as e:
            return {
                "status": "error",
                "exit_code": -1,
                "passed": 0,
                "failed": 0,
                "errors": 1,
                "output": str(e),
                "errors_output": str(e),
                "duration": 0
            }
    
    async def run_e2e_tests(self) -> Dict[str, Any]:
        """Run E2E testing scenarios"""
        print(f"\n🔄 Running E2E Testing Scenarios")
        
        try:
            test_runner = E2ETestRunner(self.org_url, self.access_token)
            report = await test_runner.run_all_scenarios()
            
            return {
                "status": "completed",
                "report": report,
                "duration": 0  # Would need to measure
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "duration": 0
            }
    
    def run_adversarial_tests(self) -> Dict[str, Any]:
        """Run adversarial security testing"""
        print(f"\n🛡️  Running Adversarial Security Tests")
        
        try:
            test_suite = AdversarialTestSuite(self.org_url, self.access_token)
            report = test_suite.run_all_adversarial_tests()
            
            return {
                "status": "completed",
                "report": report,
                "duration": 0  # Would need to measure
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "duration": 0
            }
    
    def run_performance_tests(self) -> Dict[str, Any]:
        """Run performance and load testing"""
        print(f"\n⚡ Running Performance Tests")
        
        try:
            # Simulate performance testing
            start_time = time.time()
            
            # Test response time
            response_times = []
            for i in range(10):
                test_start = time.time()
                # Simulate agent processing
                time.sleep(0.1)  # Simulate processing time
                test_end = time.time()
                response_times.append(test_end - test_start)
            
            avg_response_time = sum(response_times) / len(response_times)
            max_response_time = max(response_times)
            min_response_time = min(response_times)
            
            # Test concurrent requests
            def concurrent_test():
                time.sleep(0.05)
                return "success"
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(concurrent_test) for _ in range(10)]
                concurrent_results = [future.result() for future in futures]
            
            end_time = time.time()
            
            return {
                "status": "completed",
                "metrics": {
                    "avg_response_time": avg_response_time,
                    "max_response_time": max_response_time,
                    "min_response_time": min_response_time,
                    "concurrent_requests": len(concurrent_results),
                    "concurrent_success_rate": (concurrent_results.count("success") / len(concurrent_results)) * 100
                },
                "duration": end_time - start_time
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "duration": 0
            }
    
    async def run_all_tests(self) -> Dict[str, Any]:
        """Run all test suites and generate comprehensive report"""
        print("🚀 Starting Comprehensive Testing Suite")
        print("=" * 60)
        
        self.start_time = datetime.now()
        
        # Get test suites
        suites = self.create_test_suites()
        
        # Run tests by priority
        high_priority = [s for s in suites if s.priority == 1]
        medium_priority = [s for s in suites if s.priority == 2]
        
        all_results = {}
        
        # Run high priority tests
        print(f"\n🔴 Running HIGH Priority Tests")
        print("-" * 40)
        
        for suite in high_priority:
            print(f"\n📋 {suite.name}: {suite.description}")
            
            if suite.test_file == "test_resort_agent.py":
                result = self.run_pytest_tests(suite.test_file, suite.test_class)
            elif suite.test_file == "e2e_test_scenarios.py":
                result = await self.run_e2e_tests()
            elif suite.test_file == "adversarial_testing.py":
                result = self.run_adversarial_tests()
            else:
                result = {"status": "skipped", "reason": "Unknown test file"}
            
            all_results[suite.name] = result
        
        # Run medium priority tests
        print(f"\n🟡 Running MEDIUM Priority Tests")
        print("-" * 40)
        
        for suite in medium_priority:
            print(f"\n📋 {suite.name}: {suite.description}")
            
            if suite.test_file == "test_resort_agent.py":
                result = self.run_pytest_tests(suite.test_file, suite.test_class)
            else:
                result = {"status": "skipped", "reason": "Not implemented yet"}
            
            all_results[suite.name] = result
        
        self.end_time = datetime.now()
        
        # Generate comprehensive report
        report = self._generate_comprehensive_report(all_results)
        return report
    
    def _generate_comprehensive_report(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive test report"""
        total_duration = (self.end_time - self.start_time).total_seconds()
        
        # Calculate overall metrics
        total_tests = 0
        total_passed = 0
        total_failed = 0
        total_errors = 0
        
        for suite_name, result in results.items():
            if "passed" in result:
                total_tests += result.get("passed", 0) + result.get("failed", 0) + result.get("errors", 0)
                total_passed += result.get("passed", 0)
                total_failed += result.get("failed", 0)
                total_errors += result.get("errors", 0)
        
        overall_success_rate = (total_passed / total_tests) * 100 if total_tests > 0 else 0
        
        # Security assessment
        security_score = 0
        if "Adversarial Security Tests" in results:
            adversarial_result = results["Adversarial Security Tests"]
            if "report" in adversarial_result and "summary" in adversarial_result["report"]:
                security_score = adversarial_result["report"]["summary"].get("security_score", 0)
        
        # Performance assessment
        performance_metrics = {}
        if "Performance Tests" in results:
            performance_result = results["Performance Tests"]
            if "metrics" in performance_result:
                performance_metrics = performance_result["metrics"]
        
        report = {
            "summary": {
                "total_duration": total_duration,
                "total_tests": total_tests,
                "passed": total_passed,
                "failed": total_failed,
                "errors": total_errors,
                "overall_success_rate": overall_success_rate,
                "security_score": security_score,
                "performance_metrics": performance_metrics
            },
            "test_suites": results,
            "recommendations": self._generate_recommendations(results),
            "timestamp": datetime.now().isoformat()
        }
        
        return report
    
    def _generate_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on test results"""
        recommendations = []
        
        # Check for failed tests
        failed_suites = [name for name, result in results.items() if result.get("status") == "failed"]
        if failed_suites:
            recommendations.append(f"Fix issues in failed test suites: {', '.join(failed_suites)}")
        
        # Check for errors
        error_suites = [name for name, result in results.items() if result.get("status") == "error"]
        if error_suites:
            recommendations.append(f"Resolve errors in test suites: {', '.join(error_suites)}")
        
        # Check security score
        if "Adversarial Security Tests" in results:
            adversarial_result = results["Adversarial Security Tests"]
            if "report" in adversarial_result and "summary" in adversarial_result["report"]:
                security_score = adversarial_result["report"]["summary"].get("security_score", 0)
                if security_score < 90:
                    recommendations.append("Improve security posture - address vulnerabilities found in adversarial testing")
        
        # Check performance
        if "Performance Tests" in results:
            perf_result = results["Performance Tests"]
            if "metrics" in perf_result:
                avg_response_time = perf_result["metrics"].get("avg_response_time", 0)
                if avg_response_time > 1.0:
                    recommendations.append("Optimize performance - response times are above acceptable thresholds")
        
        return recommendations
    
    def print_comprehensive_report(self, report: Dict[str, Any]):
        """Print formatted comprehensive test report"""
        print("\n" + "=" * 80)
        print("📊 COMPREHENSIVE TEST REPORT")
        print("=" * 80)
        
        summary = report["summary"]
        print(f"\n📈 OVERALL SUMMARY:")
        print(f"   Total Duration: {summary['total_duration']:.1f} seconds")
        print(f"   Total Tests: {summary['total_tests']}")
        print(f"   Passed: {summary['passed']} ✅")
        print(f"   Failed: {summary['failed']} ❌")
        print(f"   Errors: {summary['errors']} ⚠️")
        print(f"   Overall Success Rate: {summary['overall_success_rate']:.1f}%")
        print(f"   Security Score: {summary['security_score']:.1f}%")
        
        if summary['performance_metrics']:
            print(f"\n⚡ PERFORMANCE METRICS:")
            perf = summary['performance_metrics']
            print(f"   Average Response Time: {perf.get('avg_response_time', 0):.3f}s")
            print(f"   Max Response Time: {perf.get('max_response_time', 0):.3f}s")
            print(f"   Min Response Time: {perf.get('min_response_time', 0):.3f}s")
            print(f"   Concurrent Success Rate: {perf.get('concurrent_success_rate', 0):.1f}%")
        
        print(f"\n📋 TEST SUITE RESULTS:")
        for suite_name, result in report["test_suites"].items():
            status = result.get("status", "unknown")
            if status == "completed":
                if "passed" in result:
                    print(f"   {suite_name}: {result['passed']} passed, {result['failed']} failed ✅")
                else:
                    print(f"   {suite_name}: Completed ✅")
            elif status == "failed":
                print(f"   {suite_name}: Failed ❌")
            elif status == "error":
                print(f"   {suite_name}: Error ⚠️")
            else:
                print(f"   {suite_name}: {status}")
        
        if report["recommendations"]:
            print(f"\n💡 RECOMMENDATIONS:")
            for i, rec in enumerate(report["recommendations"], 1):
                print(f"   {i}. {rec}")
        
        print(f"\n🕒 Report Generated: {report['timestamp']}")
        print("=" * 80)
    
    def save_report(self, report: Dict[str, Any], filename: str = "comprehensive_test_report.json"):
        """Save comprehensive report to file"""
        with open(filename, "w") as f:
            json.dump(report, f, indent=2)
        print(f"\n💾 Comprehensive report saved to: {filename}")


async def main():
    """Main function to run comprehensive testing"""
    print("🏨 Resort Manager Agent - Comprehensive Testing Suite")
    print("=" * 60)
    
    # Initialize test runner
    test_runner = ComprehensiveTestRunner(
        org_url="https://test-org.my.salesforce.com",
        access_token="test_token_123"
    )
    
    # Run all tests
    report = await test_runner.run_all_tests()
    
    # Print comprehensive report
    test_runner.print_comprehensive_report(report)
    
    # Save report
    test_runner.save_report(report)
    
    # Determine overall status
    overall_success_rate = report["summary"]["overall_success_rate"]
    security_score = report["summary"]["security_score"]
    
    if overall_success_rate >= 90 and security_score >= 85:
        print("\n🎉 COMPREHENSIVE TESTING PASSED!")
        print("   Agent is ready for production deployment.")
        return 0
    elif overall_success_rate >= 70 and security_score >= 70:
        print("\n⚠️  COMPREHENSIVE TESTING PARTIAL PASS")
        print("   Agent needs improvements before production deployment.")
        return 1
    else:
        print("\n❌ COMPREHENSIVE TESTING FAILED")
        print("   Agent requires significant improvements.")
        return 2


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
