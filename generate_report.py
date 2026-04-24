from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ── Colors ──────────────────────────────────────────────────
DARK      = colors.HexColor('#1a1a2e')
ACCENT    = colors.HexColor('#457B9D')
ACCENT2   = colors.HexColor('#2A9D8F')
LIGHT_BG  = colors.HexColor('#f0f4f8')
TARGET    = colors.HexColor('#E63946')
MID_GRAY  = colors.HexColor('#555555')
LIGHT_GRAY= colors.HexColor('#888888')

doc = SimpleDocTemplate(
    'Customer_Segmentation_Report.pdf',
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title', fontSize=24, fontName='Helvetica-Bold',
    textColor=DARK, alignment=TA_CENTER, spaceAfter=6)
subtitle_style = ParagraphStyle('Subtitle', fontSize=13, fontName='Helvetica',
    textColor=ACCENT, alignment=TA_CENTER, spaceAfter=4)
meta_style = ParagraphStyle('Meta', fontSize=10, fontName='Helvetica',
    textColor=LIGHT_GRAY, alignment=TA_CENTER, spaceAfter=20)
h1_style = ParagraphStyle('H1', fontSize=16, fontName='Helvetica-Bold',
    textColor=DARK, spaceBefore=18, spaceAfter=8,
    borderPad=4, leftIndent=0)
h2_style = ParagraphStyle('H2', fontSize=13, fontName='Helvetica-Bold',
    textColor=ACCENT, spaceBefore=12, spaceAfter=6)
body_style = ParagraphStyle('Body', fontSize=10.5, fontName='Helvetica',
    textColor=MID_GRAY, leading=16, alignment=TA_JUSTIFY, spaceAfter=8)
bullet_style = ParagraphStyle('Bullet', fontSize=10.5, fontName='Helvetica',
    textColor=MID_GRAY, leading=16, leftIndent=16, spaceAfter=4,
    bulletIndent=4)

story = []

# ── COVER ────────────────────────────────────────────────────
story.append(Spacer(1, 2*cm))
story.append(Paragraph("Customer Segmentation", title_style))
story.append(Paragraph("Using K-Means &amp; Hierarchical Clustering", subtitle_style))
story.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=12))
story.append(Paragraph("Data Science Internship Project &nbsp;|&nbsp; Arambh Tech", meta_style))
story.append(Paragraph("Author: Ankit &nbsp;|&nbsp; April 2026", meta_style))
story.append(Spacer(1, 1*cm))

# Cover summary box
cover_data = [
    ['Dataset', 'Mall Customers (Kaggle)'],
    ['Records', '200 customers'],
    ['Features', 'Age, Gender, Annual Income, Spending Score'],
    ['Algorithms', 'K-Means Clustering, Hierarchical (Ward)'],
    ['Optimal K', '5 clusters'],
    ['Best Score', 'Silhouette = 0.5547 (K-Means)'],
]
cover_table = Table(cover_data, colWidths=[5*cm, 11*cm])
cover_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,-1), LIGHT_BG),
    ('BACKGROUND', (1,0), (1,-1), colors.white),
    ('TEXTCOLOR', (0,0), (0,-1), DARK),
    ('TEXTCOLOR', (1,0), (1,-1), MID_GRAY),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('PADDING', (0,0), (-1,-1), 8),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [LIGHT_BG, colors.white]),
]))
story.append(cover_table)
story.append(Spacer(1, 1.5*cm))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#dddddd')))
story.append(Spacer(1, 0.5*cm))

# ── 1. OBJECTIVE ─────────────────────────────────────────────
story.append(Paragraph("1. Objective", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "The objective of this project is to segment mall customers into distinct groups based on "
    "their demographic and behavioral attributes — specifically Annual Income and Spending Score. "
    "By identifying these segments, businesses can tailor their marketing strategies, improve "
    "customer engagement, and allocate resources more effectively.",
    body_style))
story.append(Paragraph("Key goals of this project:", body_style))
for point in [
    "Explore and preprocess the Mall Customers dataset",
    "Apply K-Means and Hierarchical clustering algorithms",
    "Determine the optimal number of clusters using the Elbow Method and Silhouette Score",
    "Visualize and interpret each customer segment",
    "Compare the performance of both clustering algorithms",
]:
    story.append(Paragraph(f"• {point}", bullet_style))

# ── 2. DATASET ───────────────────────────────────────────────
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("2. Dataset Overview", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "The dataset used is the Mall Customer Segmentation dataset sourced from Kaggle. "
    "It contains 200 records of mall customers with the following features:",
    body_style))

dataset_data = [
    ['Feature', 'Type', 'Description'],
    ['CustomerID', 'Integer', 'Unique identifier for each customer'],
    ['Gender', 'Categorical', 'Male or Female'],
    ['Age', 'Integer', 'Age of the customer (18–70)'],
    ['Annual Income (k$)', 'Integer', 'Annual income in thousands of dollars'],
    ['Spending Score (1-100)', 'Integer', 'Score assigned by the mall based on spending behavior'],
]
dataset_table = Table(dataset_data, colWidths=[5*cm, 3.5*cm, 8.5*cm])
dataset_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), ACCENT),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('PADDING', (0,0), (-1,-1), 7),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
    ('TEXTCOLOR', (0,1), (-1,-1), MID_GRAY),
]))
story.append(dataset_table)

# ── 3. APPROACH ──────────────────────────────────────────────
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("3. Approach &amp; Methodology", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

story.append(Paragraph("3.1 Data Preprocessing", h2_style))
story.append(Paragraph(
    "The dataset was clean with no missing values. Gender was label-encoded (Female=0, Male=1). "
    "The primary features used for clustering were Annual Income and Spending Score, as they "
    "provide the most discriminative separation between customer groups. Features were scaled "
    "using StandardScaler to normalize the range before applying clustering algorithms.",
    body_style))

story.append(Paragraph("3.2 Determining Optimal K", h2_style))
story.append(Paragraph(
    "Two methods were used to find the optimal number of clusters:",
    body_style))
for point in [
    "Elbow Method: Plots inertia (Within-Cluster Sum of Squares) vs K. The 'elbow' point at K=5 indicates diminishing returns beyond 5 clusters.",
    "Silhouette Score: Measures how similar a point is to its own cluster vs other clusters. A higher score indicates better-defined clusters. The peak score of 0.5547 was achieved at K=5.",
]:
    story.append(Paragraph(f"• {point}", bullet_style))

story.append(Paragraph("3.3 K-Means Clustering", h2_style))
story.append(Paragraph(
    "K-Means was applied with K=5, random_state=42, and n_init=10 to ensure stable results. "
    "The algorithm iteratively assigns customers to the nearest centroid and updates centroids "
    "until convergence. The final cluster centroids were inverse-transformed to interpret results "
    "in original feature space.",
    body_style))

story.append(Paragraph("3.4 Hierarchical Clustering", h2_style))
story.append(Paragraph(
    "Agglomerative Hierarchical Clustering was applied using Ward linkage, which minimizes "
    "the total within-cluster variance. A dendrogram was plotted to visually confirm the "
    "optimal cut point at 5 clusters. The same feature set and scaling were used for "
    "a fair comparison with K-Means.",
    body_style))

# ── 4. RESULTS ───────────────────────────────────────────────
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("4. Results &amp; Analysis", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

story.append(Paragraph("4.1 Customer Segment Profiles", h2_style))

seg_data = [
    ['Segment', 'Count', 'Avg Age', 'Avg Income', 'Avg Spending', 'Female %'],
    ['Target Customers', '39', '32.7', '$86.5k', '82.1', '53.8%'],
    ['Standard Customers', '81', '42.7', '$55.3k', '49.5', '59.3%'],
    ['Affluent Savers', '35', '41.1', '$88.2k', '17.1', '45.7%'],
    ['Impulsive Spenders', '22', '25.3', '$25.7k', '79.4', '59.1%'],
    ['Careful Spenders', '23', '45.2', '$26.3k', '20.9', '60.9%'],
]
seg_table = Table(seg_data, colWidths=[4.5*cm, 1.8*cm, 2*cm, 2.5*cm, 2.8*cm, 2.4*cm])
seg_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DARK),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('PADDING', (0,0), (-1,-1), 7),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
    ('TEXTCOLOR', (0,1), (-1,-1), MID_GRAY),
    ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#fff0f0')),
    ('TEXTCOLOR', (0,1), (0,1), TARGET),
    ('FONTNAME', (0,1), (0,1), 'Helvetica-Bold'),
]))
story.append(seg_table)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("4.2 Segment Interpretation", h2_style))
segments = [
    ("Target Customers (Priority)", "High income ($86.5k), high spending score (82.1). These 39 customers are the most valuable segment. They are willing to spend and have the financial means to do so. Marketing campaigns, premium products, and loyalty rewards should be focused here."),
    ("Affluent Savers", "High income ($88.2k) but low spending score (17.1). These 35 customers earn well but spend conservatively. They can be converted with targeted promotions, exclusive deals, and value-driven loyalty programs."),
    ("Impulsive Spenders", "Low income ($25.7k) but high spending score (79.4). These 22 customers, mostly younger (avg age 25), spend beyond their means. Retention strategies with budget-friendly offers and discount programs work well here."),
    ("Standard Customers", "Mid income ($55.3k) and mid spending (49.5). The largest group at 81 customers. They represent the average mall visitor. Steady engagement through regular promotions and seasonal offers is recommended."),
    ("Careful Spenders", "Low income ($26.3k) and low spending (20.9). These 23 older customers (avg age 45) are the least engaged segment. Low marketing priority — focus on essential product offerings."),
]
for name, desc in segments:
    story.append(Paragraph(f"<b>{name}:</b> {desc}", bullet_style))

# ── 5. MODEL PERFORMANCE ─────────────────────────────────────
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("5. Model Performance", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

perf_data = [
    ['Metric', 'K-Means (K=5)', 'Hierarchical (K=5)', 'Winner'],
    ['Silhouette Score', '0.5547', '0.5538', 'K-Means'],
    ['Scalability', 'Excellent', 'Moderate', 'K-Means'],
    ['Interpretability', 'High', 'Very High', 'Hierarchical'],
    ['Requires K upfront', 'Yes', 'Flexible', 'Hierarchical'],
    ['Visual Aid', 'Elbow/Silhouette', 'Dendrogram', 'Both'],
]
perf_table = Table(perf_data, colWidths=[4.5*cm, 3.5*cm, 3.5*cm, 4.5*cm])
perf_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), ACCENT2),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('PADDING', (0,0), (-1,-1), 7),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
    ('TEXTCOLOR', (0,1), (-1,-1), MID_GRAY),
]))
story.append(perf_table)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "K-Means achieved a marginally higher silhouette score (0.5547 vs 0.5538) and is more "
    "scalable for larger datasets. Both algorithms agreed on 5 as the optimal number of clusters, "
    "which strongly validates the segmentation. K-Means is recommended as the primary model.",
    body_style))

# ── 6. CONCLUSIONS ───────────────────────────────────────────
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("6. Conclusions", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "This project successfully segmented 200 mall customers into 5 distinct groups using "
    "unsupervised machine learning. The key findings are:",
    body_style))
for point in [
    "K=5 was confirmed as optimal by both the Elbow Method and Silhouette Score analysis",
    "K-Means outperformed Hierarchical Clustering slightly (silhouette: 0.5547 vs 0.5538)",
    "Target Customers (high income, high spending) represent the most valuable segment for marketing investment",
    "Affluent Savers present a significant conversion opportunity — high income but low spending",
    "Both algorithms produced consistent cluster assignments, validating the robustness of the segmentation",
]:
    story.append(Paragraph(f"• {point}", bullet_style))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("Future Improvements", h2_style))
for point in [
    "Apply DBSCAN for density-based clustering to handle outliers",
    "Use PCA for dimensionality reduction on larger feature sets",
    "Build a Streamlit web app for interactive customer segmentation",
    "Incorporate purchase history and visit frequency for richer profiles",
]:
    story.append(Paragraph(f"• {point}", bullet_style))

# ── 7. TOOLS ─────────────────────────────────────────────────
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("7. Tools &amp; Libraries", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))
tools_data = [
    ['Tool / Library', 'Version', 'Purpose'],
    ['Python', '3.13', 'Core programming language'],
    ['pandas', 'latest', 'Data loading and manipulation'],
    ['numpy', 'latest', 'Numerical computations'],
    ['matplotlib', 'latest', 'Data visualization and chart generation'],
    ['seaborn', 'latest', 'Statistical visualization (heatmap)'],
    ['scikit-learn', 'latest', 'K-Means, Agglomerative Clustering, StandardScaler'],
    ['scipy', 'latest', 'Hierarchical linkage and dendrogram'],
    ['Jupyter Notebook', 'latest', 'Interactive development environment'],
]
tools_table = Table(tools_data, colWidths=[5*cm, 3*cm, 8*cm])
tools_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DARK),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('PADDING', (0,0), (-1,-1), 7),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
    ('TEXTCOLOR', (0,1), (-1,-1), MID_GRAY),
]))
story.append(tools_table)

# ── FOOTER ───────────────────────────────────────────────────
story.append(Spacer(1, 1*cm))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#dddddd')))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "Customer Segmentation Project &nbsp;|&nbsp; Arambh Tech Data Science Internship &nbsp;|&nbsp; Ankit &nbsp;|&nbsp; April 2026",
    ParagraphStyle('Footer', fontSize=9, textColor=LIGHT_GRAY, alignment=TA_CENTER)
))

doc.build(story)
print("PDF report generated: Customer_Segmentation_Report.pdf")
