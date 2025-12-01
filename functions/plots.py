import seaborn as sns
from queries import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FIGURES_DIR = BASE_DIR / "reports" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

#THIS FUNCTIONS GIVES US A PLOT WITH THE 5 PRODUCTS THAT HAVE GENERATED
# THE MOST AMOUNT OF SALES IN THE HISTORY OF THE COMPANY.
def PlotTop5Historically():
    
    df = MostSoldProductsHistorically()
    
    plt.figure(figsize=(14,7))
    sns.barplot(data=df, x='Amount of sales', y='Product', palette='viridis')
    plt.title("Top 5 most sold products in our history")
    plt.xlabel("Products")
    plt.ylabel("Amount of sales")
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(FIGURES_DIR / "Top5Historically.png")
    plt.show()
    plt.close()

#THIS FUNCTION PLOTS THE TOP 20 MOST SOLD PRODUCTS IN A SPECIFIC YEAR
# A PLOT WITH 4 SUBPLOTS, EACH ONE INCLUDES 5 PRODUCTS, FIRST PLOT 1-5, SECOND 6-10...
def PlotMostSoldInAYear(year):
    
    data = GetMostSoldProductsInAYear(year)
    
    
    fig, ejees = plt.subplots(2, 2, figsize=(15, 15))
    ejees[0, 0].bar(data["Producto"][0:5],data["Cantidad"][0:5])
    ejees[0, 0].set_title('Products 1-5')
    ejees[0, 0].tick_params(ejeis='x', rotation=45)
    ejees[0, 0].set_ylabel('Amount')
    
    ejees[0, 1].bar(data["Producto"][5:10],data["Cantidad"][5:10])
    ejees[0, 1].set_title('Products 6-10')
    ejees[0, 1].tick_params(ejeis='x', rotation=45)
    ejees[0, 1].set_ylabel('Amount')
    
    ejees[1, 0].bar(data["Producto"][10:15],data["Cantidad"][10:15])
    ejees[1, 0].set_title('Products 11-15')
    ejees[1, 0].tick_params(ejeis='x', rotation=45)
    ejees[1, 0].set_ylabel('Amount')
    
    ejees[1, 1].bar(data["Producto"][15:20], data["Cantidad"][15:20])
    ejees[1, 1].set_title('Products 16-20')
    ejees[1, 1].tick_params(ejeis='x', rotation=45)
    ejees[1, 1].set_ylabel('Amount')
    
    
    
    fig.suptitle(f'Top 20 Most Sold Products In {year}', fontsize=16)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"Top20in{year}.png")
    plt.show()

#THIS FUNCTION PLOTS THE AMOUNT OF SALES MADE TO EVERY STATE IN THE COUNTRY IN A SPECIFIC YEAR.
def PlotSalesInStates(year):
    
    datos = GetSalesInStates(year)
    
    plt.figure(figsize=(14,7))
    sns.barplot(x='Provincia', y='Cantidad de compras', data=datos)
    plt.xlabel("State", labelpad=10)
    plt.ylabel("Total amount", labelpad=10)
    plt.title(f"Sales by state in {year}")
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
    
    # Formatear el eje y para mostrar números sin notación científica y con separador de miles
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    plt.gca().yaxis.set_major_formatter(formatter)
    
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"SalesInStatesIn{year}.png")
    plt.show()

#THIS FUNCTION PLOTS THE AMOUNT OF PRODUCTS THAT EVERY STATE IN THE COUNTRY BOUGHT IN A SPECIFIC YEAR.
def PlotProductsByState(year):
   
    data = GetProductsByState(year)
   
    plt.figure(figsize=(14,7))
    sns.barplot(x='Provincia', y='Cantidad de productos comprados', data=data)
    plt.xlabel("States")
    plt.ylabel("Amount of bought products")
    # Formatear el eje y para mostrar números sin notación científica y con separador de miles
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(FIGURES_DIR / f"ProductsByStateIn{year}.png")
    plt.show()
    
#THIS FUNCTION PLOTS THE VOLUME OF PRODUCTS SOLD TO ALL THE COMPANIES HISTORICALLY.
def PlotVolumeSoldToCompaniesHistorically():
    
    data = GetVolumeSoldToCompaniesHistorically()
    plt.figure(figsize=(25,12))
    sns.barplot(x='Empresa', y='Volumen de compra histórico', data=data)
    plt.xlabel("Companies")
    plt.ylabel("Historical purchase volume")
    # Formatear el eje y para mostrar números sin notación científica y con separador de miles
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(FIGURES_DIR / "HistoricalVolumeByCompany.png")
    plt.show()

#THIS FUNCTION PLOTS THE AVERAGE AMOUNT SOLD OF A PRODUCT TO ALL THE COMPANIES HISTORICALLY.
def PlotAvgSalesOfProducByState(product):

    data = GetAvgSalesOfProducByState(product)
    plt.figure(figsize=(14,7))
    plt.title(f"Average purchases made by every state of the product [{product} {data['Unidad del producto'][0]}]")
    sns.barplot(x='Provincia', y='Promedio de compra', data=data)
    plt.xlabel("Companies")
    plt.ylabel("Average historical purchase volume")
    # Formatear el eje y para mostrar números sin notación científica y con separador de miles
    #formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    #plt.gca().yaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(FIGURES_DIR / f"AvgSoldOf{product}InState.png")
    plt.show()

#THIS FUNCTION GIVES US A PIE CHART OF THE PCT OF SALES THAT EVERY MONTH REPRESENTS OF A PRODUCT IN A SPECIFIC YEAR.
def PlotPctSalesProductInAYear(product, year):
    
    data = GetSalesProductInAYear(product, year)
    
    plt.figure(figsize=(14,7))
    plt.title(f"Monthly sales in {year} of the product [{product}]")
    plt.pie(data['Cantidad vendida'], labels=data['Mes'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis', len(data)))
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"PctPieSalesOf{product}In{year}.png")
    plt.show()
    
#THIS FUNCTION GIVES US A PLOT OF THE AMOUNT SOLD OF A PRODUCT IN A SPECIFIC YEAR BY MONTH.
def PlotSalesProductInAYear(product, year):
    
    data = GetSalesProductInAYear(product, year)
    
    plt.figure(figsize=(14,7))
    sns.barplot(data=data, x='Mes', y='Cantidad vendida')
    plt.title(f"Monthly sales in {year} of the product [{product}]")
    plt.xlabel("Month")
    plt.ylabel("Quantity")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"MonthlyAmountSoldOf{product}In{year}.png")
    plt.show()
      
#THIS FUNCTION PLOTS THE AMOUNT OF SALES MADE IN EVERY MONTH OF A SPECIFIC PRODUCT HISTORICALLY
def PlotHistoricalSalesVolumeProduct(product):
    data = GetHistoricallyAmountSalesProduct(product)
    plt.figure(figsize=(14,7))
    plt.title(f"Historically sales of the product [{product}]")
    sns.barplot(data=data, x='Mes', y='Cantidad vendida')
    plt.xlabel("Months")
    plt.ylabel("Amount sold")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"HistoricalSalesVolume{product}.png")
    plt.grid(True)
    
    plt.show()
  
#THIS FUNCTION GIVES US THE PRODUCT THAT PRODUCED THE MOST SELLS HISTORICALLY.   
def PlotBestSellerByYear():
    
    data = GetBestSellerByYear()
    
    plt.figure(figsize=(14,7))
    plt.title(f"Best sellers in every year")
    sns.lineplot(data=data, x='Año', y='Cantidad vendida', hue='Producto')
    plt.xlabel("Months")
    plt.ylabel("Amount sold")
    plt.xticks(rotation=45, ha='right')
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(FIGURES_DIR / "BestSellerByYear.png")
    plt.show()
    
#THIS FUNCTION PROVIDES A HEATMAP EXPLAINING THE QUANTITY SOLD OF EACH PRODUCT, BY MONTH, HISTORICALLY.
def PlotHistoricalMonthlySalesVolume():
    
    data = GetSalesPerMonthHistorically()
    df = data.pivot_table(index='Producto', columns='Mes', values='Cantidad vendida',aggfunc='sum',fill_value=0)
    plt.figure(figsize=(20, 10))
    sns.heatmap(data=df, annot=True,fmt='0.2f', cmap='YlGnBu',linewidths=0.5, linecolor='gray', xticklabels=True, yticklabels=True)
    plt.title("Historically volume of sells of each product per month")
    plt.xlabel("Month")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "HistoricalMonthlySalesVolume.png")
    plt.show()
    
#THIS FUNCTION PROVIDES A HEATMAP EXPLAINING THE QUANTITY SOLD OF A CERTAIN PRODUCT, BY MONTH, HISTORICALLY.
def PlotSalesPerMonthHistoricallyUnique(product):
    
    data = GetSalesPerMonthHistoricallyUnique(product)
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=data, x='Mes', y='Cantidad vendida', markers=True)
    plt.title(f"Historically volume of sells of '{product}' per month")
    plt.xlabel("Month")
    plt.ylabel("Quantity")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"HistoricalMonthlySalesOf{product}.png")
    plt.show()

#THIS FUNCTION GIVES US A BAR PLOT THAT COMPARES THE AMOUNT BOUGHT BY TWO COMPANIES ACROSS THE PROVINCES IN WHICH THEY WORK.   
def PlotSalesByStateAndCompanies(company1, company2):
    
    data = GetSalesByStateAndCompanies(company1,company2)
    df_melt = data.melt(id_vars='Provincia', var_name='Empresa', value_name='Cantidad')
    plt.figure(figsize=(14,7))
    sns.barplot(data=df_melt, x='Cantidad', y='Provincia', hue='Empresa')
    plt.title(f"Amount sold historically to [{company1} - {company2}] by province")
    plt.xlabel("Province")
    plt.ylabel("Quantity")
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    plt.gca().xejeis.set_major_formatter(formatter)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"{company1}_VS_{company2}.png")
    plt.show()

#THIS FUNCTION GIVES US A PLOT WITH THE AMOUNT OF SALES OF A PRODUCT, MADE BY MONTH YEARLY AND THE COUNT OF SALES WHICH AMOUNT IS 0. 
def PlotAmountSoldByProductYearlyMonthly(product):

    data = GetAmountSoldByProductYearlyMonthly(product)

    data['Period'] = pd.to_datetime(data['Año'].astype(str) + "-" + data['Mes'].astype(str) + "-01")

    df_melt = data.melt(id_vars='Period', value_vars=['Cantidad', 'Compras con cantidad 0'], var_name='Type', value_name='Amount')

    g = sns.relplot(data=df_melt, x='Period', y='Amount', hue='Type', height=6, aspect=3, markers=True, kind='line')

    g.set_xticklabels(rotation=90)

    g.fig.suptitle(f"Monthly Sales Comparison (>0 vs =0) for '{product}'", fontsize=16)


    formatter = ticker.FuncFormatter(lambda x, pos: f"{int(x):,}")
    g.axes[0][0].yaxis.set_major_formatter(formatter)

    g.axes[0][0].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    save_path = FIGURES_DIR / f"AmountSoldOf{product}YearlyMonthly.png"
    g.fig.savefig(save_path, bbox_inches="tight")

    plt.show()
    plt.close()

  
#THIS FUNCTION GIVES US A PLOT CLUSTERING THE PROVINCES BY THE TYPE OF CONSUMER THAT THEY ARE, BASED ON THE AMOUNT OF PURCHASES THAT THEY MADE
def PlotClusterOfProvinces():
    
    data = GetClusterOfProvinces()
    
    plt.figure(figsize=(14,7))
    sns.barplot(data=data, x='Cantidad de compras', y='Provincia', hue='Tipo de comprador')
    plt.title("Clustering of Provinces by the amount of purchases.")
    plt.xlabel("Amount of purchases")
    plt.ylabel("Provinces")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "ClusterOfProvinces.png")
    plt.show()
    
#THIS FUNCTION GIVES US A PLOT CLUSTERING THE PROVINCES BY THE TYPE OF CONSUMER THAT THEY ARE BASED ON THE AMOUNT OF PRODUCTS THAT THEY BOUGHT
def PlotClusterOfProvinces2():
    
    data = GetClusterOfProvinces2()
    
    sns.barplot(data=data, x='Cantidad comprada', y='Provincia', hue='Tipo de comprador')
    plt.title("Purchases by Province: Quantity vs. Total Purchased")
    plt.xlabel("Province")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.legend(title='Métrica')
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "ClusterOfProvinces2.png")
    plt.show()
    
#THIS FUNCTION GIVES US A PLOT CLUSTERING THE PROVINCES BY THE TYPE OF CONSUMER THAT THEY ARE BASED ON THE AMOUNT OF PRODUCTS THAT THEY BOUGHT
#BUT FILTERS THE SALES WHERE THE AMOUNT EQUALS 0.
def PlotClusterHigherThanZero():
    
     
    data = GetClusterHigherThanZero()
    
    plt.figure(figsize=(14,7))
    sns.barplot(data=data, x='Cantidad de compras', y='Provincia', hue='Tipo de comprador')
    plt.title("Purchases by Province with Quantity Greater than 0: Quantity vs. Total Purchased")
    plt.xlabel("Amount of purchases")
    plt.ylabel("Province")
    plt.xticks(rotation=45)
    plt.legend(title='Métrica')
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "ClusterHigherThanZero.png")
    plt.show()

#THIS FUNCTION PROVIDES US A RELPLOT OF THE 5 MOST SOLD PRODUCTS HISTORICALLY AND SHOWS US THE VOLUME OF SELLS EACH MONTH AND
# WE CAN SEE IN WHICH MONTHS WE HAD MORE SELLS  
def PlotTop5HistoricallyMonthly():
    
    df = GetTop5Historically()
    g = sns.relplot(data=df, x='Mes', y='Amount sold', hue='Product', kind='line', height=15, aspect=.75)
    g._legend.set_bbox_to_anchor((1, 0.9))  # x, y en coordenadas relativas
    g._legend.set_frame_on(True) 

    plt.title("Historical Monthly Sales of the Top 5 Products")
    plt.xlabel("Months")
    plt.ylabel("Amount")
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    plt.gca().yaxis.set_major_formatter(formatter)
    
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(FIGURES_DIR / "Top5HistoricallyMonthly.png")
    plt.show()
   
#THIS FUNCTION PLOTS THE PCT THAT THE AMOUNT OF SALES MADE TO EVERY PROVINCE THAT BOUGHT THAT PRODUCT REPRESENTS. ONLY USES THE TOP 3 MOST
#SOLD PRODUCTS HISTORICALLY.
def PlotPctByStateTop3():

    df = GetPctByStateTop3()

    fig, ejes = plt.subplots(1, 3, figsize=(20,10))
    top3 = df['Producto'].unique()
    for i,producto in enumerate(top3):
        datos = df[df['Producto'] == producto]
        eje = ejes[i]
        eje.bar(datos["Provincia"], datos["Cantidad"])

        eje.set_title(producto, fontsize=14)
        eje.set_xlabel("Province")
        if i == 0:
            eje.set_ylabel("Quantity sold")
        
        eje.tick_params(axis="x", rotation=45)
        
        formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
        eje.yaxis.set_major_formatter(formatter)

    plt.suptitle('Sales Distribution by Province for the 3 Best Selling Products', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(FIGURES_DIR / "PctByStateTop3.png")
    plt.show()
    
# PLOTS THE YEARLY PURCHASE VOLUME OF THE TOP 5 COMPANIES WITH THE HIGHEST HISTORICAL TOTAL PURCHASES.
def PlotTop5CompThroughTime():
    
    df = GetTop5CompThroughTime()
    g = sns.relplot(data=df, x='Año', y='Cantidad', hue='Empresa', palette='viridis', kind='line', height=15, aspect=.75)
    plt.title("Yearly Purchase Volume of the Top 5 Highest-Spending Companies")
    plt.xlabel("Year")
    plt.ylabel("Amount sold")
    g._legend.set_bbox_to_anchor((1, 0.9))  # x, y en coordenadas relativas
    g._legend.set_frame_on(True) 
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(FIGURES_DIR / "Top5CompThroughTime.png")
    plt.show()
    
#THIS FUNCTION GIVES US A PLOT WITH THE TOTAL AMOUNT OF SALES AND THE AVERAGE AMOUNT OF SALES OF THE MOST SOLD PRODUCT IN EACH PROVINCE.
def PlotCountAvgOfN1():
    
    df = GetCountAvgOfN1()
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(16, 10))
    sns.barplot(x=df['provincia'][0:10], y=df['total_ventas'], ax=axes[0])
    axes[0].set_title('Total sales amount by province')
    axes[0].set_ylabel('Total quantity sold')
    axes[0].set_xlabel('Province')
    axes[0].tick_params(axis='x', rotation=45)
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    axes[0].yaxis.set_major_formatter(formatter)

    sns.barplot(x=df['provincia'][0:10], y=df['promedio_historico'], ax=axes[1])
    axes[1].set_title('Average sales per province')
    axes[1].set_ylabel('Average sold')
    axes[1].set_xlabel('Province')
    axes[1].tick_params(axis='x', rotation=45)
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x):,}')
    axes[1].yaxis.set_major_formatter(formatter)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "CountAvgOfN1.png")
    plt.show()
#PlotSalesByStateAndCompanies("PETROBRAS ARGENTINA S.A.", "TECPETROL S.A.")
PlotHistoricalMonthlySalesVolume()