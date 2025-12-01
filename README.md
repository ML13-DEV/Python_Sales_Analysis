📊 Sales Analysis of Hydrocarbon & Fuel Sector (2010–2025)
Python • SQL • Seaborn • Matplotlib

This project performs a comprehensive analysis of sales made to companies within Argentina’s hydrocarbon and fuel sector.
Using Python, SQL, and data visualization, the analysis reveals market patterns, purchase trends, outliers, and operational insights.

📁 Dataset

Source: Argentina’s Energy Secretariat – datos.gob.ar

Period: 2010–2025

Rows: 500,000+

Includes:

Product

Company

Province

Quantity purchased

Unit of measurement

Date (month/year)

…and other operational attributes

This dataset represents official sales reported by fuel and energy companies across the country.

🛠️ Technologies Used

Programming & Analysis

Python 3.12

Pandas

Seaborn

Matplotlib

Database & Backend

SQLAlchemy

MariaDB / MySQL

🗂️ Project Structure  
1project/  
1.1 data/  
   1.1.1 ventas-a-empresas-del-sector.csv     # Raw dataset  

1.2 functions/  
   1.2.1 stats_functions.py                   # SQL queries + business logic  
   1.2.2 plot_functions.py                    # Visualization functions  
   1.2.3 db.py                            # Connection to the database  
   1.2.3 db.py                            # Function to export a dataframe to an excel file  

1.3 reports/  
   1.3.1 figures/                             # Generated charts  
   1.3.2 excel/                              # Exported Excel summaries  
   1.3.3 sql_tables/                          # SQL table exports  


🔍 Key Insights Identified

Below are the main insights extracted during the analysis (you can insert your images here later):

⭐ 1. Historical Purchase Volume by Province

Buenos Aires shows 160,000+ units purchased, significantly above any other province.

Indicates high concentration of demand.

Suggests greater industrial or energy consumption activity in this region.

⭐ 2. Top Purchasing Companies

A small group of companies consistently leads the sector's purchases.

The Top 5 companies account for 51.8% of total historical sales.

Highlights the presence of a strong market core of major buyers.

⭐ 3. Monthly Consumption Trends by Product

Clear seasonality patterns appear in several fuel types.

Some products exhibit stable, predictable demand, while others fluctuate sharply.

Useful for forecasting, logistics, and inventory planning.

⭐ 4. Purchases With Zero Quantity

Some products frequently show recorded purchases with quantity = 0.
This may indicate:

Incomplete administrative records

Internal reporting anomalies

Opportunities for audit or data quality improvement

📈 Areas of Analysis Included in the Project

✔️ Total purchases by company, product, province
✔️ Monthly and yearly evolution
✔️ Top N companies and products
✔️ Seasonal patterns
✔️ Zero-quantity purchase behavior
✔️ Exporting full results into Excel and SQL
✔️ Multiple professional visualizations

🧑‍💻 Author

Manuel Lombardi
Data Analyst & Software Developer

🔗 LinkedIn: https://www.linkedin.com/in/manuel-lombardi-572685341/

🐙 GitHub: https://github.com/ML13-DEV
