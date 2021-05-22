import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from AnalyseData import Analyse
from visualization import *

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

regionAnalysis = Analyse('datasets/WHOregionLifeExpectancyAtBirth.csv')

st.title('Data Analyst On Life Expectancy in Human')
sidebar = st.sidebar


def viewDataset():
    st.header('Data Used in Project')
    dataframe = regionAnalysis.getDataframe()

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")


def analyseRegion():
    st.header("Life Expectancy in various Regions")
    data = regionAnalysis.getRegionData()
    st.dataframe(data)
    st.plotly_chart(plotBar(data, "default title",
                            'Life Expectancy in Years', 'Region Name'))


sidebar.header('Choose Your Option')
options = ['View Dataset', 'Analyse Region']
choice = sidebar.selectbox(options=options, label="Choose Action")

if choice == options[0]:
    viewDataset()
elif choice == options[1]:
    analyseRegion()
