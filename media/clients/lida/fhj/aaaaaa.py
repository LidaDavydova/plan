import pandas as pd

wb = pd.read_excel('mp_fhj_09.23.21.xlsx') # This reads in your excel doc as a pandas DataFrame

wb.to_html('mp_fhj_09.23.21.html')
