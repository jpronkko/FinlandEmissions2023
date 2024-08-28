# Finland Greenhouse Gas Emissions 2023 (FinlandEmissions2023) project

FinlandEmissions2023 is a small project, in which I investigate through visualizations various aspects of StatFin Finland 2023 greenhouse emission data, which covers years from 1990 to 2023. It includes greenhouse gas emissions from various sectors in a detailed way such as land use, energy and transport. Apart from CO2 emissions, it includes emissions of other greenhouse gasses, such as methane. One can browse the data from https://stat.fi/tilasto/khki. For this project I wrote a simple python code to retrieve a chunk of the data from StatFin public API for further processing in Power BI to create the visualizations.

This git project includes Power BI project files and python code used to make the report shown in the screenshot in Figure 1.

<figure>
  <img src="Screenshots/Emissions_report_2024-08-28.png" width="95%">
  <figcaption>Figure 1. Screenshot of the Power BI report</figcaption>
</figure>
<br />
<br />

# Status

The work so far has involved the following tasks:

- Finding out how to retrieve the data
- Examining what is in the data
- Transforming the data to suit the Power BI visualization (cleaning rows with missing data etc.)
- Writing Power BI measures using DAX filters to use specific data for specific visualizations
- Implementing visualizations, which tell some aspects of the data that I find interesting
- Stylizing the composed report

# Todo

I find the topic quite interesting and I intend to dig further in the data and to continue making additional visualizations.
