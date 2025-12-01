import pandas as pd
from sqlalchemy import text
from db import engine


#THIS FUNCTIONS GIVES US A DATAFRAME WITH THE 5 PRODUCTS THAT HAVE GENERATED
# THE MOST AMOUNT OF SALES IN THE HISTORY OF THE COMPANY.
def MostSoldProductsHistorically():
    
    query = """select producto as 'Product', COUNT(producto) as 'Amount of sales'
                from ventas 
                group by producto
                order by COUNT(producto) DESC
                limit 5;"""
                
    return pd.read_sql(query, engine)

#THIS FUNCTION RETURNS A DATAFRAME WITH THE TOP 20 MOST SOLD PRODUCTS IN A SPECIFIC YEAR
def GetMostSoldProductsInAYear(year):
    
    query = text("""select producto as 'Producto', SUM(cantidad) as 'Cantidad'
                from ventas where anio = :year
                group by producto
                order by SUM(cantidad) desc
                limit 20;""")
                
    return pd.read_sql(query, engine, params={"year":year})

#THIS FUNCTION RETURNS A DATAFRAME WITH THE AMOUNT OF SALES MADE TO EVERY STATE IN THE COUNTRY IN A SPECIFIC YEAR.
def GetSalesInStates(year):
    
    query = text("""select provincia as 'Provincia', COUNT(producto) as 'Cantidad de compras' 
                from ventas where anio = :year
                group by provincia 
                order by  COUNT(producto) DESC;""")
                
    return pd.read_sql(query, engine, params={"year":year})

#THIS FUNCTION RETURNS A DATAFRAME WITH THE AMOUNT OF PRODUCTS THAT EVERY STATE IN THE COUNTRY BOUGHT IN A SPECIFIC YEAR.
def GetProductsByState(year):
    query = text("""select provincia as 'Provincia', SUM(cantidad) as 'Cantidad de productos comprados' 
    from ventas where anio = :year
    group by provincia 
    order by SUM(cantidad) DESC; """)
    
    data = pd.read_sql(query, engine, params={"year":year})
    data_clean = data[data['Cantidad de productos comprados'] > 0]
    
    return data_clean

#THIS FUNCTION RETURNS A DATAFRAME WITH THE VOLUME OF PRODUCTS SOLD TO ALL THE COMPANIES HISTORICALLY.
def GetVolumeSoldToCompaniesHistorically():
    query = """select empresa as 'Empresa', SUM(cantidad) as 'Volumen de compra histórico'
    from ventas
    group by empresa
    order by SUM(cantidad) desc;"""
    
    data = pd.read_sql(query, engine)
    data_clean = data[data['Volumen de compra histórico'] > 0]
    
    return data_clean

#THIS FUNCTION RETURNS A DATAFRAME WITH THE AVERAGE AMOUNT SOLD OF A PRODUCT TO ALL THE COMPANIES HISTORICALLY.
def GetAvgSalesOfProducByState(product):
    query = text("""select provincia as 'Provincia', AVG(cantidad) as 'Promedio de compra', unidad as 'Unidad del producto'
    from ventas
    where producto = :product
    group by provincia 
    order by AVG(cantidad) desc;""")
    
    data = pd.read_sql(query, engine, params={"product":product})
    data_clean = data[data['Promedio de compra'] > 0]
    
    return data_clean

#THIS FUNCTION RETURNS A DATAFRAME WITH THE MONTHLY SALES OF A PRODUCT IN A SPECIFIC YEAR.
def GetSalesProductInAYear(product, year):
    
    query = text("""select mes as 'Mes', SUM(cantidad) as 'Cantidad vendida'
    from ventas
    where producto = :product and anio = :year
    group by mes 
    order by mes;""")
    
    data = pd.read_sql(query, engine, params={"product":product, "year":year})
    data_clean = data[data['Cantidad vendida'] > 0]
    
    return data_clean

#THIS FUNCTION RETURNS A DATAFRAME WITH THE SALES MADE IN EVERY MONTH OF A SPECIFIC PRODUCT HISTORICALLY
def GetHistoricallyAmountSalesProduct(product):
    query = text("""select mes as 'Mes', SUM(cantidad) as 'Cantidad vendida'
    from ventas
    where producto = :product
    group by mes 
    order by mes;""")
    
    data = pd.read_sql(query, engine, params={"product":product})
    data_clean = data[data['Cantidad vendida'] > 0]
    
    return data_clean

#THIS FUNCTION RETURNS A DATAFRAME WITH THE PRODUCT THAT PRODUCED THE MOST SELLS IN EVERY YEAR.   
def GetBestSellerByYear():
    query = """SELECT anio as 'Año', producto as 'Producto', suma as 'Cantidad vendida'
                FROM (
                    SELECT anio, producto, SUM(cantidad) AS suma
                    FROM ventas
                    GROUP BY anio, producto
                ) AS ventas_por_producto
                WHERE (anio, suma) IN (
                    SELECT anio, MAX(suma)
                    FROM (
                        SELECT anio, producto, SUM(cantidad) AS suma
                        FROM ventas
                        GROUP BY anio, producto
                    ) AS resumen
                    GROUP BY anio
                )
                ORDER BY anio ASC, suma DESC;
            """
            
    return pd.read_sql(query, engine)

#THIS FUNCTION PROVIDES A DATAFRAME WITH THE QUANTITY SOLD OF EVERY PRODUCT, BY MONTH, HISTORICALLY.
def GetSalesPerMonthHistorically():
    query = """select mes as 'Mes', producto as 'Producto' ,SUM(cantidad) as 'Cantidad vendida'
                from ventas
                where cantidad > 0
                group by mes, producto 
                order by mes, SUM(cantidad) desc;
            """
    return pd.read_sql(query, engine)
    
def GetPctByStateTop3():
    query = """
                with top3 as (
                select producto, SUM(cantidad) from ventas
                group by producto
                order by SUM(cantidad) desc
                limit 3
                )

                select v.producto as 'Producto', v.provincia as 'Provincia', SUM(v.cantidad) as 'Cantidad'
                from ventas v
                where v.producto in (select producto from top3)
                group by v.producto, v.provincia
                having SUM(v.cantidad) > 0
                order by v.provincia, SUM(v.cantidad);
                """

    return pd.read_sql(query, engine)

#THIS FUNCTION PROVIDES A DATAFRAME WITH THE QUANTITY SOLD OF A SPECIFIC PRODUCT, BY MONTH, HISTORICALLY.
def GetSalesPerMonthHistoricallyUnique(product):
    query = text("""select mes as 'Mes', producto as 'Producto' ,SUM(cantidad) as 'Cantidad vendida'
                from ventas
                where cantidad > 0 and producto = :product
                group by mes, producto 
                order by mes, SUM(cantidad) desc;
            """)
    return pd.read_sql(query, engine, params={"product":product})

#THIS FUNCTION GIVES US A DATAFRAME WITH THE QUANTITY BOUGHT BY TWO COMPANIES IN EVERY PROVINCE.
def GetSalesByStateAndCompanies(company1, company2):
    
    query = text(""" SELECT
                provincia as 'Provincia',
                SUM(CASE WHEN empresa = :company1 THEN cantidad ELSE 0 END) AS :company1,
                SUM(CASE WHEN empresa = :company2 THEN cantidad ELSE 0 END) AS :company2
                FROM ventas
                WHERE empresa IN (:company1, :company2) AND cantidad > 0 
                GROUP BY provincia
                ORDER BY provincia;
            """)
    
    return pd.read_sql(query, engine, params={"company1":company1, "company2":company2})

#THIS FUNCTION GIVES US A DATAFRAME WITH THE AMOUNT OF SALES OF A PRODUCT, MADE BY MONTH YEARLY AND THE COUNT OF SALES WHICH AMOUNT IS 0. 
def GetAmountSoldByProductYearlyMonthly(product):
    query = text("""select 
                        normales.anio as 'Año',
                        normales.mes as 'Mes',
                        normales.producto as 'Producto',
                        SUM(normales.cantidad) as 'Cantidad',
                        IFNULL(ceros.cantidad_ceros, 0) as 'Compras con cantidad 0',
                        normales.unidad as 'Unidad'
                    from ventas as normales

                    LEFT JOIN (
                        select 
                            anio, 
                            mes, 
                            producto,
                            COUNT(*) as cantidad_ceros 
                        from ventas 
                        where cantidad = 0 
                        and producto = :product
                        group by anio, mes, producto
                    ) as ceros
                        on normales.anio = ceros.anio
                        AND normales.mes = ceros.mes
                        AND normales.producto = ceros.producto

                    where normales.producto = :product

                    GROUP BY normales.anio, normales.mes, normales.producto
                    ORDER BY normales.anio, normales.mes;

                """)

    data = pd.read_sql(query, engine, params={"product":product})
    
    data['Period'] = pd.to_datetime(data['Año'].astype(str) + "-" + data['Mes'].astype(str) + "-01")
    return data

#THIS FUNCTION GIVES US A PLOT CLUSTERING THE PROVINCES BY THE TYPE OF CONSUMER THAT THEY ARE, BASED ON THE AMOUNT OF PURCHASES THAT THEY MADE
def GetClusterOfProvinces():
    
    query = """WITH ProvinciaVentas AS (
                SELECT
                    provincia,
                    SUM(cantidad) AS TotalCantidadComprada,
                    COUNT(producto) AS CantidadDeCompras
                FROM
                    ventas
                GROUP BY
                    provincia
                ),
                PromedioGlobal AS (
                    SELECT
                        AVG(CantidadDeCompras) AS PromedioTotalCompraPorProvincia
                    FROM
                        ProvinciaVentas
                )
                SELECT
                    pv.provincia AS 'Provincia',
                    pv.CantidadDeCompras AS 'Cantidad de compras',
                    pv.TotalCantidadComprada AS 'Cantidad comprada',
                    CASE
                        WHEN pv.CantidadDeCompras >= (pg.PromedioTotalCompraPorProvincia / 4 * 3) THEN 'Comprador fiel'
                        WHEN pv.CantidadDeCompras >= (pg.PromedioTotalCompraPorProvincia / 4 * 2) THEN 'Comprador recurrente'
                        WHEN pv.CantidadDeCompras >= (pg.PromedioTotalCompraPorProvincia / 4 * 1) THEN 'Comprador ocasional'
                        ELSE 'Comprador muy ocasional'
                    END AS 'Tipo de comprador'
                FROM
                    ProvinciaVentas pv, PromedioGlobal pg 
                ORDER BY
                    pv.CantidadDeCompras desc, pv.TotalCantidadComprada DESC;
            """
    
    return pd.read_sql(query, engine)

#THIS FUNCTION GIVES US A PLOT CLUSTERING THE PROVINCES BY THE TYPE OF CONSUMER THAT THEY ARE BASED ON THE AMOUNT OF PRODUCTS THAT THEY BOUGHT
def GetClusterOfProvinces2():
    
    query = """WITH ProvinciaVentas AS (
                SELECT
                    provincia,
                    SUM(cantidad) AS TotalCantidadComprada,
                    COUNT(producto) AS CantidadDeCompras
                FROM
                    ventas
                GROUP BY
                    provincia
                ),
                PromedioGlobal AS (
                    SELECT
                        AVG(CantidadDeCompras) AS PromedioTotalCompraPorProvincia 
                    FROM
                        ProvinciaVentas
                )
                SELECT
                    pv.provincia AS 'Provincia',
                    pv.CantidadDeCompras AS 'Cantidad de compras',
                    pv.TotalCantidadComprada AS 'Cantidad comprada',
                    CASE
                        WHEN pv.CantidadDeCompras >= (pg.PromedioTotalCompraPorProvincia / 4 * 3) THEN 'Comprador fiel'
                        WHEN pv.CantidadDeCompras >= (pg.PromedioTotalCompraPorProvincia / 4 * 2) THEN 'Comprador recurrente'
                        WHEN pv.CantidadDeCompras >= (pg.PromedioTotalCompraPorProvincia / 4 * 1) THEN 'Comprador ocasional'
                        ELSE 'Comprador muy ocasional' -- O puedes definir un umbral más bajo si es necesario
                    END AS 'Tipo de comprador'
                FROM
                    ProvinciaVentas pv, PromedioGlobal pg -- Puedes usar coma para join si PromedioGlobal solo tiene 1 fila
                ORDER BY
                     pv.TotalCantidadComprada DESC, pv.cantidaddecompras  DESC;
            """
    
    return pd.read_sql(query, engine)


#THIS FUNCTION GIVES US A PLOT CLUSTERING THE PROVINCES BY THE TYPE OF CONSUMER THAT THEY ARE BASED ON THE AMOUNT OF PRODUCTS THAT THEY BOUGHT
#BUT FILTERS THE SALES WHERE THE AMOUNT EQUALS 0.
def GetClusterHigherThanZero():
    query = """WITH ProvinciaVentas AS (
                SELECT
                    provincia,
                    SUM(cantidad) AS TotalCantidadComprada,
                    COUNT(producto) AS CantidadDeCompras
                FROM
                    ventas
               	where cantidad > 0
                GROUP BY
                    provincia
                ),
                PromedioGlobal AS (
                    SELECT
                        AVG(CantidadDeCompras) AS PromedioTotalCompraPorProvincia -- Este es el promedio de las compras de cada provincia
                    FROM
                        ProvinciaVentas
                )
                SELECT
                    pv.provincia AS 'Provincia',
                    pv.CantidadDeCompras AS 'Cantidad de compras',
                    pv.TotalCantidadComprada AS 'Cantidad comprada',
                    CASE
                        WHEN pv.CantidadDeCompras >= (pg.PromedioTotalCompraPorProvincia / 4 * 3) THEN 'Comprador fiel'
                        WHEN pv.CantidadDeCompras <= (pg.PromedioTotalCompraPorProvincia / 4 * 3) AND pv.CantidadDeCompras >= (pg.PromedioTotalCompraPorProvincia / 4 * 2) THEN 'Comprador recurrente'
                        WHEN pv.CantidadDeCompras <= (pg.PromedioTotalCompraPorProvincia / 4 * 2) AND pv.CantidadDeCompras >= (pg.PromedioTotalCompraPorProvincia / 4 * 1) THEN 'Comprador ocasional'
                        ELSE 'Comprador muy ocasional' -- O puedes definir un umbral más bajo si es necesario
                    END AS 'Tipo de comprador'
                FROM
                    ProvinciaVentas pv, PromedioGlobal pg -- Puedes usar coma para join si PromedioGlobal solo tiene 1 fila
                ORDER BY
                    pv.CantidadDeCompras desc, pv.TotalCantidadComprada DESC;
                """
    return pd.read_sql(query, engine)

#THIS FUNCTION PROVIDES US A RELPLOT OF THE 5 MOST SOLD PRODUCTS HISTORICALLY AND SHOWS US THE VOLUME OF SELLS EACH MONTH AND
# WE CAN SEE IN WHICH MONTHS WE HAD MORE SELLS
def GetTop5Historically():
    query = """SELECT v.producto AS Product,
        v.mes AS Mes,
        SUM(v.cantidad) AS `Amount sold`
    FROM ventas v
    JOIN (
        SELECT producto
        FROM ventas
        GROUP BY producto
        ORDER BY SUM(cantidad) DESC
        LIMIT 5
    ) AS top5_producto
        ON v.producto = top5_producto.producto
    GROUP BY v.producto, v.mes
    ORDER BY v.mes, v.producto;	"""

    return pd.read_sql(query,engine)

#THIS FUNCTION PLOTS THE PCT THAT THE AMOUNT OF SALES MADE TO EVERY PROVINCE THAT BOUGHT THAT PRODUCT REPRESENTS. ONLY USES THE TOP 3 MOST
#SOLD PRODUCTS HISTORICALLY.
def GetPctByStateTop3():

    query = """
            with top3 as (
            select producto, SUM(cantidad) from ventas
            group by producto
            order by SUM(cantidad) desc
            limit 3
            )

            select v.producto as 'Producto', v.provincia as 'Provincia', SUM(v.cantidad) as 'Cantidad'
            from ventas v
            where v.producto in (select producto from top3)
            group by v.producto, v.provincia
            having SUM(v.cantidad) > 0
            order by v.provincia, SUM(v.cantidad);
            """

    return pd.read_sql(query, engine)

#THIS FUNCTION SHOWS HOW THE SELLS OF THE TOP 5 MOST SOLD PRODUCTS EVOLVED THROUGH TIME.
def GetTop5CompThroughTime():
    query = """with top3 as (
            
            select empresa, SUM(cantidad) from ventas
            group by empresa
            order by SUM(cantidad) desc
            limit 5
        )

        select v.empresa as 'Empresa', v.anio as 'Año', SUM(v.cantidad) as 'Cantidad'
        from ventas v
        where v.empresa in (select empresa from top3)
        group by v.empresa, v.anio
        order by v.anio, SUM(v.cantidad);
        """

    return pd.read_sql(query, engine)

def GetAvgAndStdOfTop1():
    query = """with top1 as (
        select producto, SUM(cantidad)
        from ventas
        group by producto
        order by SUM(cantidad) desc
        limit 1
    )

    select v.producto as 'Producto', v.provincia as 'Provincia', SUM(v.cantidad) as 'Cantidad', AVG(v.cantidad) as 'Promedio', STDDEV_SAMP(v.cantidad) as 'STD'
    from ventas v
    where v.producto in (select producto from top1)
    group by v.producto, v.provincia
    having cantidad > 0 
    order by SUM(v.cantidad) desc, AVG(v.cantidad);"""

    return pd.read_sql(query, engine)

#THIS FUNCTION GIVES US A PLOT WITH THE TOTAL AMOUNT OF SALES AND THE AVERAGE AMOUNT OF SALES OF THE MOST SOLD PRODUCT IN EACH PROVINCE.
def GetCountAvgOfN1():
    query = """WITH ventasprov AS (
        SELECT 
            provincia,
            producto,
            SUM(cantidad) AS total_producto,
            ROW_NUMBER() OVER (PARTITION BY provincia ORDER BY SUM(cantidad) DESC) AS nro_fila
        FROM ventas
        GROUP BY provincia, producto
    )
    SELECT 
        v.provincia,
        v.producto,
        SUM(v.cantidad) AS total_ventas,
        AVG(v.cantidad) AS promedio_historico
    FROM ventas v
    JOIN ventasprov vp 
        ON v.provincia = vp.provincia
    AND v.producto = vp.producto
    WHERE vp.nro_fila = 1
    GROUP BY v.provincia, v.producto
    having SUM(v.cantidad) > 0
    ORDER BY SUM(v.cantidad) desc;
    """

    return pd.read_sql(query, engine)
print(GetAmountSoldByProductYearlyMonthly("Gas Natural"))
