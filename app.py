import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="Workflow Intelligence Hub",
    page_icon="🧠",
    layout="wide"
)

st.title("Workflow Intelligence Hub")
st.write(
    "AI-powered platform for turning unstructured business information into "
    "requirements, stakeholder insights, proposal drafts, and workflow recommendations."
)

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
else:
    model = None
    st.warning("Gemini API key not found. App is running in fallback demo mode.")

st.divider()

business_text = st.text_area(
    "Paste customer meeting notes, emails, RFP text, or project requirements:",
    height=220,
    placeholder="Example: A global company wants to provide English and German training to 800 employees..."
)

tab1, tab2, tab3, tab4 = st.tabs([
    "Requirement Analyzer",
    "Stakeholder Mapper",
    "Proposal Generator",
    "Workflow Planner"
])

def run_ai(prompt, fallback):
    if model:
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            return fallback
    return fallback

with tab1:
    st.subheader("Requirement Analyzer")
    if st.button("Analyze Requirements"):
        if not business_text.strip():
            st.warning("Please enter business information first.")
        else:
            prompt = f"""
Analyze this customer/business input.

Return:
## Business Objectives
## Technical Requirements
## Constraints
## Risks
## Open Questions

Input:
{business_text}
"""
            fallback = f"""
## Business Objectives
- Identify customer goals from the provided business information.
- Translate unstructured input into clear requirements.

## Technical Requirements
- SSO integration
- Reporting or analytics needs
- User management
- Scalable platform setup

## Constraints
- Timeline pressure
- Missing technical details
- Multiple stakeholder groups

## Risks
- Integration requirements may be unclear.
- Reporting needs may differ between departments.
- Proposal or demo timeline may be tight.

## Open Questions
- Which systems need integration?
- Who are the main users?
- What reporting KPIs are required?
- What is the expected rollout timeline?

### Source Input
{business_text}
"""
            st.markdown(run_ai(prompt, fallback))

with tab2:
    st.subheader("Stakeholder Mapper")
    if st.button("Map Stakeholders"):
        if not business_text.strip():
            st.warning("Please enter business information first.")
        else:
            prompt = f"""
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
            fallback = f"""
## Decision Makers
- HR / Learning & Development leadership
- Procurement or budget owner

## Technical Stakeholders
- IT team
- SSO or integration owner
- Data/reporting owner

## End Users
- Employees
- Managers
- Department leads

## Internal Teams
- Sales team
- Solution consulting team
- Implementation/customer success team

## Questions for Each Stakeholder Group
- Decision makers: What business outcome should the project achieve?
- Technical stakeholders: Which systems must be integrated?
- End users: What learning or workflow experience is expected?
- Internal teams: What is needed for demo and proposal preparation?
"""
            st.markdown(run_ai(prompt, fallback))

with tab3:
    st.subheader("Proposal Generator")
    if st.button("Generate Proposal Draft"):
        if not business_text.strip():
            st.warning("Please enter business information first.")
        else:
            prompt = f"""
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
            fallback = f"""
## Executive Summary
The customer is looking for a scalable solution to support employee development across multiple teams or regions. The proposed approach should focus on structured rollout, reporting, integration readiness, and clear stakeholder alignment.

## Customer Needs
- Scalable user setup
- Clear reporting and dashboards
- Integration support
- Multi-department rollout
- Timely demo and proposal preparation

## Recommended Approach
- Prepare a tailored demo scenario based on the customer’s key requirements.
- Clarify technical integration needs early.
- Structure the proposal around business value, implementation feasibility, and measurable outcomes.

## Expected Benefits
- Faster requirement clarification
- Better alignment between business and technical teams
- More consistent proposal preparation
- Improved customer-facing communication

## Implementation Notes
- Confirm integration details before final proposal.
- Define user groups and reporting roles.
- Align timeline with customer expectations.

## Next Steps
- Validate requirements with stakeholders.
- Prepare demo environment.
- Draft proposal.
- Collect missing technical details.
"""
            st.markdown(run_ai(prompt, fallback))

with tab4:
    st.subheader("Workflow Planner")
    if st.button("Plan Workflow"):
        if not business_text.strip():
            st.warning("Please enter business information first.")
        else:
            prompt = f"""
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
            fallback = f"""
## Suggested Workflow
1. Collect customer requirements.
2. Identify stakeholders and technical dependencies.
3. Prepare demo scenario.
4. Draft proposal.
5. Review open questions.
6. Align internally before customer follow-up.

## Automation Opportunities
- Requirement extraction from notes or RFPs
- Proposal draft generation
- Stakeholder mapping
- Demo preparation checklist
- Follow-up question generation

## Bottlenecks
- Missing technical integration details
- Unclear decision-making structure
- Tight deadlines
- Manual proposal preparation

## Recommended Tools or Processes
- Shared requirement checklist
- Reusable proposal templates
- Structured demo planning workflow
- Internal review before customer delivery

## Success Metrics
- Faster proposal preparation
- Fewer missing requirements
- Better stakeholder alignment
- More consistent customer communication
"""
            st.markdown(run_ai(prompt, fallback))