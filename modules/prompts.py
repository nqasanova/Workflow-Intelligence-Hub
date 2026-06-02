def requirement_prompt(business_text):
    return f"""
Analyze this customer or business input.

Return:
## Business Objectives
## Technical Requirements
## Constraints
## Risks
## Open Questions

Input:
{business_text}
"""


def stakeholder_prompt(business_text):
    return f"""
Identify likely stakeholders from this business input.

Return:
## Decision Makers
## Technical Stakeholders
## End Users
## Internal Teams
## Questions for Each Stakeholder Group

Input:
{business_text}
"""


def proposal_prompt(business_text):
    return f"""
Create a professional proposal draft from this business input.

Return:
## Executive Summary
## Customer Needs
## Recommended Approach
## Expected Benefits
## Implementation Notes
## Next Steps

Input:
{business_text}
"""


def workflow_prompt(business_text):
    return f"""
Create a workflow plan from this business input.

Return:
## Suggested Workflow
## Automation Opportunities
## Bottlenecks
## Recommended Tools or Processes
## Success Metrics

Input:
{business_text}
"""