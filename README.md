# SmartCart Customer Segmentation

A machine learning project that groups customers based on their purchasing behavior using K-Means clustering. The Streamlit dashboard helps explore customer segments and understand their characteristics.

## Live Demo

[Open the SmartCart Dashboard](https://smartcart-customer-segmentation-ml.streamlit.app/)

## Tech Stack

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- Streamlit

## Project Files

- `smartcart_customer_segmentation.ipynb` — Data analysis and clustering workflow
- `smartcart_customers.csv` — Original customer dataset
- `app.py` — Interactive dashboard
- `smartcart_segmented_customers.csv` — Customer records with cluster labels
- `cluster_summary.csv` — Cluster summary
- `requirements.txt` — Python dependencies

## How It Works

1. Clean and prepare the customer data.
2. Apply K-Means clustering to group similar customers.
3. Analyze the characteristics of each cluster.
4. Explore the results through an interactive Streamlit dashboard.

The project uses `Response` for post-clustering campaign analysis, not as an input feature for clustering.

## Run Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the dashboard:

```bash
streamlit run app.py
```

The exported CSV files must be present in the project folder before running the dashboard. To regenerate them, run the notebook cells from top to bottom.
