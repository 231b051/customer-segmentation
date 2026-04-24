# Customer Segmentation
### Data Science Internship Project — Arambh Tech

![Python](https://img.shields.io/badge/Python-3.13-blue)
![sklearn](https://img.shields.io/badge/scikit--learn-latest-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

## Objective
Identify distinct customer segments from mall customer data using unsupervised machine learning — K-Means and Hierarchical Clustering.

## Dataset
- **Source:** [Mall Customer Segmentation Data — Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
- **Records:** 200 customers
- **Features:** Age, Gender, Annual Income (k$), Spending Score (1-100)

## Results — 5 Customer Segments

| Segment | Count | Avg Income | Avg Spending | Strategy |
|---|---|---|---|---|
| 🎯 Target Customers | 39 | $86.5k | 82.1 | Top priority |
| 💰 Affluent Savers | 35 | $88.2k | 17.1 | Convert with loyalty offers |
| 🛍️ Impulsive Spenders | 22 | $25.7k | 79.4 | Retain with discounts |
| 👥 Standard Customers | 81 | $55.3k | 49.5 | Steady engagement |
| 💼 Careful Spenders | 23 | $26.3k | 20.9 | Low priority |

## Model Performance

| Model | Silhouette Score |
|---|---|
| K-Means (K=5) | **0.5547** ✅ |
| Hierarchical/Ward (K=5) | 0.5538 |

## Project Structure
├── Customer_segmentation.ipynb   # Main notebook
├── generate_report.py            # PDF report generator
├── Customer_Segmentation_Report.pdf  # Final report
├── Mall_Customers.csv            # Dataset
├── customer_segments_output.csv  # Clustered output
├── eda_plots.png                 # EDA visualizations
├── elbow_silhouette.png          # Optimal K selection
├── kmeans_clusters.png           # K-Means cluster plot
├── dendrogram.png                # Hierarchical dendrogram
├── hierarchical_clusters.png     # Hierarchical cluster plot
└── cluster_profiles_heatmap.png  # Segment profiles

## Libraries Used
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- scipy

## How to Run
1. Clone this repository
2. Install dependencies: `pip install pandas numpy matplotlib seaborn scikit-learn scipy`
3. Open `Customer_segmentation.ipynb` in Jupyter Notebook
4. Run all cells
