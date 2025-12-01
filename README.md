# 📊 Sales Analysis of Hydrocarbon & Fuel Sector (2010–2025)
Python • SQL • Seaborn • Matplotlib

This project performs a comprehensive analysis of sales made to companies within Argentina’s hydrocarbon and fuel sector.
Using Python, SQL, and data visualization, the analysis reveals market patterns, purchase trends, outliers, and operational insights.

---

## 📁 Dataset

- Source: Argentina’s Energy Secretariat – datos.gob.ar

- Period: 2010–2025

- Rows: 500,000+

- **Includes:**

  - Product

  - Company

  - Province

  - Quantity purchased

  - Unit of measurement

  - Date (month/year)

  - …and other operational attributes

This dataset represents official sales reported by fuel and energy companies across the country.

### 📥 Dataset
This dataset is too large to upload to GitHub.

You can download it from:
[https://drive.google.com/xxxxx](https://drive.google.com/drive/folders/1njJl_u3z1BRBrVhyRU9Rgt4oju3qniPJ?usp=drive_link)

Once downloaded, place it inside:

project/data/ventas-a-empresas-del-sector.csv


---

## 🛠️ Technologies Used

- Programming & Analysis

- Python 3.12

- Pandas

- Seaborn

- Matplotlib

- Database & Backend

- SQLAlchemy

- MariaDB / MySQL

---

## 🗂️ Project Structure

- **project/**
  - **data/**
    - ventas-a-empresas-del-sector.csv — *Raw dataset*
  
  - **functions/**
    - stats_functions.py — *SQL queries & business logic*
    - plot_functions.py — *Visualization functions*
    - db.py — *Database connection*
    - to_excel.py — *Export dataframe to Excel*
  
  - **reports/**
    - figures/ — *Generated charts*
    - excel/ — *Exported Excel summaries*
    - tables/ — *SQL table exports*
 
---

## 🔍 Key Insights Identified

Below are the main insights extracted during the analysis:

### ⭐ 1. Historical Purchase Volume by Province

- Buenos Aires shows 160,000+ units purchased, significantly above any other province.

- Indicates high concentration of demand.

- Suggests greater industrial or energy consumption activity in this region.


  <img width="1200" height="700" alt="ClusterOfProvinces" src="https://github.com/user-attachments/assets/d8d30d51-24d9-4f25-80f4-4346f3463114" />

---

### ⭐ 2. Top Purchasing Companies

- A small group of companies consistently leads the sector's purchases.

- The Top 5 companies account for 51.8% of total historical sales.

- Highlights the presence of a strong market core of major buyers.

  <img width="1200" height="1000" alt="image" src="https://github.com/user-attachments/assets/23d502fb-fb06-44c1-b00e-bdbe2005c0e3" />


### ⭐ 3. Monthly Consumption Trends by Product

- Clear seasonality patterns appear in several fuel types.

- Some products exhibit stable, predictable demand, while others fluctuate sharply.

- Useful for forecasting, logistics, and inventory planning.

  <img width="2000" height="1000" alt="image" src="https://github.com/user-attachments/assets/df7724a8-120b-445b-b844-cf890cb9aca2" />

---

### ⭐ 4. Purchases With Zero Quantity

Some products frequently show recorded purchases with quantity = 0.
This may indicate:

 - Incomplete administrative records

 - Internal reporting anomalies

 - Opportunities for audit or data quality improvement

   <img width="2019" height="600" alt="AmountSoldOfDiesel OilYearlyMonthly" src="https://github.com/user-attachments/assets/a89525bd-c58f-4d87-ab1a-b0b98ab9963d" />

---

## 📈 Areas of Analysis Included in the Project

✔️ Total purchases by company, product, province  
✔️ Monthly and yearly evolution  
✔️ Top N companies and products  
✔️ Seasonal patterns  
✔️ Zero-quantity purchase behavior  
✔️ Exporting full results into Excel and SQL  
✔️ Multiple professional visualizations  

## 🧑‍💻 Author

Manuel Lombardi
Data Analyst & Software Developer

🔗 LinkedIn: https://www.linkedin.com/in/manuel-lombardi-572685341/

🐙 GitHub: https://github.com/ML13-DEV
