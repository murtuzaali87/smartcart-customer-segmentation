# SmartCart Customer Segmentation

## Files
- `smartcart_customer_segmentation.ipynb`: your original notebook workflow with targeted fixes and export cells added at the end.
- `smartcart_customers.csv`: source dataset.
- `app.py`: Streamlit dashboard that reads the notebook's exported customer segmentation results.
- `requirements.txt`: Python dependencies.

## Run the notebook first
1. Keep `smartcart_customer_segmentation.ipynb` and `smartcart_customers.csv` in the same folder.
2. Open the notebook and run all cells from top to bottom.
3. The final cells create `smartcart_segmented_customers.csv` and `cluster_summary.csv`.

## Run Streamlit locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
Push `app.py`, `requirements.txt`, `smartcart_segmented_customers.csv`, and optionally `cluster_summary.csv` to a GitHub repository. In Streamlit Community Cloud, select that repository and set the main file path to `app.py`.

Note: the exported CSVs are produced by the notebook; they must be generated before deployment and included in the repository. `Response` is excluded from the clustering input and used only for post-clustering campaign analysis.
