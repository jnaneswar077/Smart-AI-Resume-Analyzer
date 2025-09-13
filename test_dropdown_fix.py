#!/usr/bin/env python3
"""
Test script to verify dropdown visibility fix
Run this to test if the job category dropdown is now visible
"""

import streamlit as st
import sys
import os

# Add the project directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load the CSS
def load_css():
    with open('style/style.css', 'r') as f:
        return f.read()

def main():
    st.set_page_config(
        page_title="Dropdown Fix Test",
        page_icon="🔧",
        layout="wide"
    )
    
    # Load and apply CSS
    css = load_css()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title("🔧 Dropdown Visibility Test")
    st.markdown("This page tests if the job category dropdown options are now visible.")
    
    # Test the job categories from the actual app
    from config.job_roles import JOB_ROLES
    
    st.subheader("Job Category Dropdown Test")
    st.markdown("**Instructions:** Click on the dropdown below. You should see white text on a dark background.")
    
    categories = list(JOB_ROLES.keys())
    selected_category = st.selectbox(
        "Job Category", 
        categories, 
        key="test_category",
        help="This dropdown should show white text on dark background"
    )
    
    if selected_category:
        st.success(f"✅ Selected: {selected_category}")
        
        # Show roles for the selected category
        roles = list(JOB_ROLES[selected_category].keys())
        selected_role = st.selectbox(
            "Specific Role", 
            roles, 
            key="test_role",
            help="This dropdown should also show white text on dark background"
        )
        
        if selected_role:
            st.success(f"✅ Selected Role: {selected_role}")
    
    st.subheader("Visual Test Results")
    st.markdown("""
    **What to check:**
    1. ✅ Dropdown options should have **white text** on **dark background**
    2. ✅ Hover effects should work (darker background on hover)
    3. ✅ Selected option should be highlighted in blue
    4. ✅ Dropdown arrow should be white/visible
    
    **If you still see white text on white background:**
    - Try refreshing the page (Ctrl+F5 or Cmd+Shift+R)
    - Clear browser cache
    - Check browser developer tools for any CSS conflicts
    """)
    
    st.subheader("CSS Variables Used")
    st.code("""
    --bg-light: #2D2D2D (dark background for dropdown)
    --bg-dark: #1E1E1E (darker background for hover)
    --accent-color: #00B4DB (blue for selected option)
    --text-primary: #FFFFFF (white text)
    """, language="css")

if __name__ == "__main__":
    main()
