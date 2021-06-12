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
lifeExpectancyAnalysis = Analyse('datasets/LifeExpectancyAtBirth.csv')


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
    st.plotly_chart(plotGroupedBar(data, ['Total Life Expectancy', 'Health Life Expectancy'], "Life Expectancy",
                                   'Life Expectancy in Years', 'Region Name'))

    data = regionAnalysis.getGender()
    st.dataframe(data.values)
    col1, col2 = st.beta_columns(2)
    col1.plotly_chart(plotBar(data, "Life Expectancy",
                              'Life Expectancy in Years', 'Region Name'))
    col2.plotly_chart(
        plotPie(['Both Sexes', 'Female', 'Male'], data.values, "Life Expectancy"))

    data = regionAnalysis.getGender()
    col1, col2 = st.beta_columns(2)
    col1.plotly_chart(plotBar(data, "Life Expectancy",
                              'Healthy Life Expectancy in Years', 'Healthy Life Expectancy in Region Name'))
    col2.plotly_chart(
        plotPie(['Both Sexes', 'Female', 'Male'], data.values, "Life Expectancy"))

    selCon = st.selectbox(options=regionHealthAnalysis.getLocations(),
                          label="select Location to Analyse")

    data = regionHealthAnalysis.getExpectancyOverTime(selCon)
    st.dataframe(data)
    # st.plotly_chart(plotLine(data, "Life Expectancy over time",
    #                         ' Life Expactancy (Years)', 'Life Expectancy of Africa over Time'))

    C = "Country"
    st.dataframe(data)
    data = healthAnalysis.getCountryData(C)
    Country = st.plotly_chart(plotBar(data, "Life Expectancy",
                                      'Top 20 life expectancy', ' Life Expactancy in year'))
    st.dataframe(data)
    data = healthAnalysis.getCountryData(C)

    selYear = st.selectbox(
        options=healthAnalysis.getYears(), label="Select Year")
    data = healthAnalysis.getTopCountryData(int(selYear), 20)
    st.plotly_chart(plotBar(data, "Life Expectancy",
                            'Top 20 life expectancy', ' Life Expactancy in year'))

    data = healthAnalysis.getBotCountryData(int(selYear), 20)

    st.plotly_chart(plotBar(data, "Life Expectancy",
                            'Bottom 20 life expectancy', ' Life Expactancy in year'))

    selCon = st.selectbox(options=healthAnalysis. getLifeExpectancydata(
    ), label="select Location in countries to Analyse")

    data = lifeExpectancyAnalysis.getAtBirthData()
    st.plotly_chart(plotBar(data, "Life Expectancy",
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
