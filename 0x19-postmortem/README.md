# Postmortem: Web Stack Outage Incident

## Issue Summary

### Duration of the Outage
Start Time: Apr 13, 2024, 02:00 AM EST  
End Time: Apr 13, 2024, 06:45 AM EST  

### Impact
- **Service Affected:** E-commerce website checkout functionality
- **User Experience:** Users were unable to complete purchases, leading to cart abandonment.
- **Affected Users:** Approximately 60% of active users attempting to make a purchase during the outage period.

### Root Cause
The root cause was traced back to a misconfiguration in the load balancer settings, specifically an incorrect health check configuration that led to the premature termination of healthy backend servers.

## Timeline

- **02:05 AM EST:** The issue was initially detected via automated monitoring alerts indicating high latency and failure rates in the checkout process.
- **02:10 AM EST:** Initial investigation focused on the application layer, assuming a code deployment issue. No recent deployments were identified.
- **02:30 AM EST:** Investigation shifted to database performance, suspecting query optimization issues. Database queries appeared optimized and performing normally.
- **03:15 AM EST:** Misleading path led to investigating network latency between services. Network diagnostics showed no anomalies.
- **03:45 AM EST:** Incident escalated to senior infrastructure team.
- **04:20 AM EST:** Load balancer configuration was reviewed, revealing misconfigured health checks.
- **06:00 AM EST:** Correct load balancer settings were applied.
- **06:45 AM EST:** Service restored after confirming stable operation through monitoring tools and manual testing.

## Root Cause and Resolution

The root cause was a misconfiguration in the load balancer's health check settings. The health checks were set too aggressively, causing healthy backend servers to be marked as unhealthy and removed from the pool. This resulted in an overload on the remaining servers, leading to increased latency and failures in processing checkout requests.

The issue was resolved by adjusting the load balancer's health check settings to more appropriate values, allowing for a grace period before marking servers as unhealthy. This adjustment ensured that temporary spikes in traffic did not lead to unnecessary server removals from the active pool.

## Corrective and Preventative Measures

### Improvements/Fixes
- Review and document load balancer configuration standards.
- Implement more granular monitoring for load balancer health checks.
- Conduct regular audits of infrastructure configurations against established standards.

### Tasks
- Patch load balancer software to the latest stable version.
- Add monitoring alerts for anomalies in backend server health status changes.
- Schedule a training session for the operations team on advanced load balancing techniques.
- Develop a playbook for responding to high latency incidents involving the checkout process.





