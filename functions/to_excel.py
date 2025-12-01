import pandas as pd
from queries import GetPctByStateTop3


#THIS FUNCTION CONVERTS THE DATAFRAME TO AN EXCEL FILE TO MAKE A BETTER PRESENTATION
def GetPctByStateToExcelTop3():

    df = GetPctByStateTop3()  
    top3 = df['Producto'].unique()
    try:
        with pd.ExcelWriter('Top3.xlsx', mode='a', if_sheet_exists='overlay', engine='openpyxl') as writer:
            for i,producto in enumerate(top3):
                datos = df[df['Producto'] == producto]
                datos.to_excel(writer, sheet_name="Top3", startrow=0, startcol=(5*i), index=False)
        return "File saved correctly."
    except Exception as e:
        return f"Something went wrong! {e}"