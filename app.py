import streamlit as st

st.set_page_config(page_title="Jewel Loan Eligible Calculator", layout="centered")

st.title("Jewel Loan Eligible Calculator")

# Simple password protection for your 5 team members
password = st.text_input("Enter Team Access Password", type="password")

# Change 'bankteam123' to any password you want to share with your 5 members
if password == "bankteam123":
    
    st.markdown("### Inputs")
    col1, col2 = st.columns(2)
    with col1:
        gross_wt = st.number_input("Gross (in grams)", value=35.000, format="%.3f")
    with col2:
        net_wt = st.number_input("Net (in grams)", value=32.200, format="%.3f")

    st.markdown("---")
    
    # Section 1 Rates & Calculations
    st.subheader("Section 1 (Per Gram Rates & Eligibility)")
    c1, c2, c3 = st.columns(3)
    with c1:
        rate_1 = st.number_input("Rate 1", value=9900.0, step=100.0)
    with c2:
        rate_2 = st.number_input("Rate 2", value=9600.0, step=100.0)
    with c3:
        rate_3 = st.number_input("Rate 3", value=8900.0, step=100.0)

    # Calculations (Net weight × Rate)
    smf_12 = net_wt * rate_1
    non_smf_12 = net_wt * rate_2
    jl_12 = net_wt * rate_3

    st.markdown("#### Results")
    st.markdown(f"> **SMF – 12:** &nbsp;&nbsp;&nbsp;&nbsp; **₹ {smf_12:,.2f}**")
    st.markdown(f"> **Non SMF – 12:** &nbsp;&nbsp; **₹ {non_smf_12:,.2f}**")
    st.markdown(f"> **JL – 12:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **₹ {jl_12:,.2f}**")

    st.markdown("---")

    # Section 2 Rates & Calculations
    st.subheader("Section 2 (Per Gram Rates & Eligibility)")
    d1, d2, d3 = st.columns(3)
    with d1:
        rate_4 = st.number_input("Rate 4", value=10700.0, step=100.0)
    with d2:
        rate_5 = st.number_input("Rate 5", value=10000.0, step=100.0)
    with d3:
        rate_6 = st.number_input("Rate 6", value=9400.0, step=100.0)

    # Calculations
    smf_6 = net_wt * rate_4
    non_smf_6 = net_wt * rate_5
    jl_6 = net_wt * rate_6

    st.markdown("#### Results")
    st.markdown(f"> **SMF – 6:** &nbsp;&nbsp;&nbsp;&nbsp; **₹ {smf_6:,.2f}**")
    st.markdown(f"> **Non SMF – 6:** &nbsp;&nbsp; **₹ {non_smf_6:,.2f}**")
    st.markdown(f"> **JL – 6:** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **₹ {jl_6:,.2f}**")

elif password == "":
    st.info("Please enter the team password to view the calculator.")
else:
    st.error("Incorrect password. Please try again.")
