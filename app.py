import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from AnalyseData import Analyse
from visualization import *

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

regionAnalysis = Analyse('datasets/WHOregionLifeExpectancyAtBirth.csv')
healthAnalysis = Analyse('datasets/HALElifeExpectancyAtBirth.csv')
regionHealthAnalysis = Analyse(
    'datasets/HALeWHOregionLifeExpectancyAtBirth.csv')
lifeExpectAnalysis = Analyse('datasets/LifeExpectancyAtBirth.csv')


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
    data = regionAnalysis.getRegionLifeExpectancyData()
    st.dataframe(data)
    st.plotly_chart(plotBar(data, "default title",
                            'Life Expectancy in Years', 'Region Name'))

    data = regionHealthAnalysis.getHealthvsLife()
    st.plotly_chart(plotGroupedBar(data, ['Total Life Expectancy', 'Health Life Expectancy'], "default title",
                                   'Life Expectancy in Years', 'Region Name'))

    data = regionAnalysis.getGender()
    st.plotly_chart(plotBar(data, "default title",
                            'Life Expectancy in Years', 'Region Name'))

    data = regionAnalysis.getGender()
    st.plotly_chart(plotBar(data, "default title",
                            'Healthy Life Expactancy (Years)', 'Healthy Life Expactancy of different region'))

    selCon = st.selectbox(options=healthAnalysis.getLocations(),
                          label="select Location to Analyse")

    data = healthAnalysis.getCountryData(selCon)
    st.plotly_chart(plotBar(data, "default title",
                            ' Life Expactancy (Years)', 'Life Expectancy of Africa over Time'))


    C="Country"
    st.dataframe(data)
    data = healthAnalysis.getCountryData(C)
    Country=st.plotly_chart(plotBar(data, "default title",
                            'Top 20 life expectancy', ' Life Expactancy in year'))
    st.dataframe(data)
    data = healthAnalysis.getCountryData(C)

    selYear = st.selectbox(
        options=healthAnalysis.getYears(), label="Select Year")
    data = healthAnalysis.getTopCountryData(int(selYear), 20)
    st.plotly_chart(plotBar(data, "default title",
                            'Top 20 life expectancy', ' Life Expactancy in year'))

    data = healthAnalysis.getBotCountryData(int(selYear), 20)

    st.plotly_chart(plotBar(data, "default title",
                            'Bottom 20 life expectancy', ' Life Expactancy in year'))

    selCon = st.selectbox(options=healthAnalysis.getlifeExpectancyData(), label="select Location in countries to Analyse")

    data = lifeExpectAnalysis.getAtBirthData()
    st.plotly_chart(plotBar(data, "default title",
                            'Human', ' Life Expactancy in year'))

    # countries=['India', 'China', 'United States of America', 'Germany',
    #  'United Kingdom of Great Britain and Northern Ireland',
    # 'Japan', 'Canada']


sidebar.header('Choose Your Option')
options = ['View Dataset', 'Analyse Region']
choice = sidebar.selectbox(options=options, label="Choose Action")

if choice == options[0]:
    viewDataset()
elif choice == options[1]:
    analyseRegion()
