import pandas   as pd
import datetime
from datetime import date
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

import locale
locale.setlocale(locale.LC_ALL,  "Portuguese_Brazil.1252")
pd.options.mode.chained_assignment = None  # default='warn'

import requests
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill, Font, Alignment
import numpy as np
import pandas   as pd
import locale
import datetime

from fMovVendas import create_df

dfBr, dfUS, df = create_df()

#
dfBr['Data'] = pd.to_datetime(dfBr['Data'], dayfirst=True)
dfBr['Ano'] = dfBr['Data'].apply(lambda x: str(x.year) + '-' + str(x.month))
dfBr  = dfBr.sort_values(['Ano', 'Corretora'], axis =0, ascending=[False, True])
#
st.title('Vendas Mensais Br')
month = st.sidebar.selectbox('PERIODO Brasil', dfBr['Ano'].unique())
#
df_filteredBr = dfBr[dfBr['Ano'] == month]
df_filteredBr
#
#
#
dfUS['Data'] = pd.to_datetime(dfUS['Data'], dayfirst=True)

dfUS = dfUS.dropna()
dfUS['Ano'] = dfUS['Data'].apply(lambda x: str(x.year) + '-' + str(x.month))
dfUS  = dfUS.sort_values(['Corretora','Ano'], ascending=[True, False])

#
st.title('Vendas Mensais US')

month = st.sidebar.selectbox('PERIODO US', dfUS['Ano'].unique())
#
df_filteredUS = dfUS[dfUS['Ano'] == month]
df_filteredUS
#
#col1, col2 = st.columns(2)
st.title('Vendas Anuais')

st.dataframe(df, width=1500, height=1000)

#  streamlit run C:\Users\lucia\Dev\vendas\pMovVendas.py 