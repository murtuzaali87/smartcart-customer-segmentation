import os
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="SmartCart Customer Segmentation", page_icon="🛍️", layout="wide")

st.title("🛍️ SmartCart Customer Segmentation")
st.write("Explore customer groups created by the K-Means clustering workflow in the notebook.")

DATA_FILE = "smartcart_segmented_customers.csv"
SUMMARY_FILE = "cluster_summary.csv"

if not os.path.exists(DATA_FILE):
    st.error(f"Missing `{DATA_FILE}`. Run the notebook from top to bottom and keep the exported CSV beside app.py.")
    st.stop()

customers = pd.read_csv(DATA_FILE)
if "clusters" not in customers.columns:
    st.error("The customer export does not contain a 'clusters' column. Re-run the notebook export cells.")
    st.stop()

customers["clusters"] = customers["clusters"].astype(str)
clusters = sorted(customers["clusters"].unique(), key=lambda x: int(x) if x.isdigit() else x)

with st.sidebar:
    st.header("Filters")
    selected_clusters = st.multiselect("Customer segments", clusters, default=clusters)
    if "Education" in customers.columns:
        education_options = sorted(customers["Education"].dropna().astype(str).unique())
        selected_education = st.multiselect("Education", education_options, default=education_options)
    else:
        selected_education = []
        education_options = []

filtered = customers[customers["clusters"].isin(selected_clusters)].copy()
if education_options and selected_education:
    filtered = filtered[filtered["Education"].astype(str).isin(selected_education)]
elif education_options and not selected_education:
    filtered = filtered.iloc[0:0]

c1, c2, c3 = st.columns(3)
c1.metric("Customers shown", f"{len(filtered):,}")
c2.metric("Segments shown", filtered["clusters"].nunique())
if "total_spending" in filtered.columns:
    c3.metric("Average total spending", f"{filtered['total_spending'].mean():,.0f}" if len(filtered) else "—")
else:
    c3.metric("Average total spending", "—")

st.subheader("Segment size")
size_data = filtered["clusters"].value_counts().sort_index().rename_axis("Segment").reset_index(name="Customers")
if len(size_data):
    st.plotly_chart(px.bar(size_data, x="Segment", y="Customers", color="Segment", title="Customers per segment"), use_container_width=True)
else:
    st.info("No customers match the selected filters.")

if "Income" in filtered.columns and "total_spending" in filtered.columns and len(filtered):
    st.subheader("Income vs. spending")
    st.plotly_chart(px.scatter(filtered, x="total_spending", y="Income", color="clusters", hover_data=[c for c in ["age", "Recency", "total_children"] if c in filtered.columns], title="Customer segments by income and spending"), use_container_width=True)

st.subheader("Segment profiles")
profile_cols = [c for c in ["Income", "age", "total_spending", "Recency", "total_children", "customer_tenure_days", "NumWebPurchases", "NumStorePurchases", "NumWebVisitsMonth"] if c in filtered.columns]
if profile_cols and len(filtered):
    profiles = filtered.groupby("clusters")[profile_cols].mean(numeric_only=True).round(2)
    st.dataframe(profiles, use_container_width=True)
else:
    st.caption("No numeric profile columns are available for the current selection.")

if "Response" in filtered.columns and len(filtered):
    st.subheader("Campaign response by segment")
    response = filtered.groupby("clusters")["Response"].mean().mul(100).round(1).rename("Response rate (%)").reset_index()
    st.plotly_chart(px.bar(response, x="clusters", y="Response rate (%)", color="clusters", title="Campaign response rate (descriptive analysis only)"), use_container_width=True)
    st.caption("Response was excluded from clustering and is shown only to compare campaign outcomes after segments were formed.")

st.subheader("Customer records")
st.dataframe(filtered, use_container_width=True, hide_index=True)
st.download_button("Download filtered customer data (CSV)", filtered.to_csv(index=False).encode("utf-8"), "smartcart_filtered_customers.csv", "text/csv")

if os.path.exists(SUMMARY_FILE):
    with st.expander("Notebook cluster summary export"):
        st.dataframe(pd.read_csv(SUMMARY_FILE), use_container_width=True)

st.caption("Segments are exploratory groups, not ground-truth customer labels. Review the notebook metrics and business context before using them for decisions.")
