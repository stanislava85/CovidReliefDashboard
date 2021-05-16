# -*- coding: utf-8 -*-
"""
Covid Relief Research Dashboard 

Team DS 2: 

Juan, Kari, Clariza, Stanislava

"""

# pandas and numpy for data manipulation
import pandas as pd

from bokeh.plotting import figure
from bokeh.models import Range1d, HoverTool, ColumnDataSource
from bokeh.models.widgets import Div, Select, Paragraph
from bokeh.io import curdoc
from bokeh.layouts import column, row

# Make plot with horizontal bar and return layout
def boro_tab(boro_cases_df):


    #Function to make dataset for left graph
    def make_dataset(borough):
        #total_cases = boro_cases_df['CASE_COUNT'][:5].sum()
        #total_deaths = boro_cases_df['DEATH_COUNT'][:5].sum()
        case_count = boro_cases_df[boro_cases_df['BOROUGH_GROUP'] == borough]['CASE_COUNT'].values[0]
        hosp_count = boro_cases_df[boro_cases_df['BOROUGH_GROUP'] == borough]['HOSPITALIZED_COUNT'].values[0]
        death_count = boro_cases_df[boro_cases_df['BOROUGH_GROUP'] == borough]['DEATH_COUNT'].values[0]

        source = ColumnDataSource(data = {'x':[death_count, hosp_count, case_count], 'y': ['Deaths','Hospitalized','Total Cases']})

        return source
    
    def generate_stats(borough = 'Bronx'):
        case_count = boro_cases_df[boro_cases_df['BOROUGH_GROUP'] == borough]['CASE_COUNT'].values[0]
        death_count = boro_cases_df[boro_cases_df['BOROUGH_GROUP'] == borough]['DEATH_COUNT'].values[0]
        hosp_count = boro_cases_df[boro_cases_df['BOROUGH_GROUP'] == borough]['HOSPITALIZED_COUNT'].values[0]
        
        stats = {
            'total_cases':	{'value':case_count, 'label': 'Total Cases'},
            'hosp_count':	{'value':hosp_count, 'label':'Total Hospitalized'},
            'death_count': {'value':death_count, 'label':'Total Deaths'}
            }
        return stats

    #Create central dataset and graph
    def make_central_graph(borough_cases_df):
        population = [1418207, 2559903, 1628706, 2253858, 476143]
        boros = borough_cases_df['BOROUGH_GROUP'][:5].tolist()
        source = ColumnDataSource(data = dict(y = boros,
                                              x1= borough_cases_df['CASE_COUNT'][:5].tolist(),
                                              x2 = population))
        tooltips= [('Borough', '@y'),('Infected', '@x1'),('Total Population','@x2')]
        p = figure(y_range = boros, title= 'Correlation between Positive cases and Population' ,
                   plot_width = 700, plot_height = 400, 
                   name = 'central', tooltips= tooltips)
        p.hbar_stack(['x1', 'x2'], y='y', height=0.8, color = ('salmon','lightgray'), source = source)
        return p

    #Plot left graph
    def make_plot(src):
        # Blank plot with correct labels
        y_range = ['Deaths','Hospitalized','Total Cases']
        height = 0.3
        r= Range1d(0,220750)
        graph = figure(y_range = y_range, x_range = r, title = "Boroughwise Cases", 
                       plot_width = 350, plot_height = 250, name ="left")
        graph.hbar(y = 'y', right = 'x', height = height, source = src, color = ('firebrick'))
        hover = HoverTool(tooltips= [('', '@x')],  mode='hline')
        graph.add_tools(hover)
        
        return graph
    
    def style_left_plot(p):
        # Title
        p.title.align = 'center'
        p.title.text_font_size = '12pt'
        
        p.xaxis.visible = False
        p.xgrid.grid_line_color = None
        p.ygrid.grid_line_color = None
        return p
    
    def style_center_plot(p):
        
        p.title.align = 'center'
        p.title.text_font_size = '12pt'
        
        p.xaxis.visible = False
        p.xgrid.grid_line_color = None
        p.ygrid.grid_line_color = None
        
        return p      

    #Callback for dropdown selection
    def handler(event):
        boro = event.item
        print('Selected Borough = ',boro)
        new_src = make_dataset(boro)
        src.data.update(new_src.data)
        
        stats = generate_stats(boro)
        total_cases_div.text = str(stats['total_cases']['value'])
        hosp_cases_div.text = str(stats['hosp_count']['value'])
        death_count_div.text = str(stats['death_count']['value'])
        
    def update(attr, old, new):
        boro = dropdown.value
        print('Selected Borough = ',boro)
        new_src = make_dataset(boro)
        src.data.update(new_src.data)
        
        stats = generate_stats(boro)
        total_cases_div.text = str(stats['total_cases']['value'])
        hosp_cases_div.text = str(stats['hosp_count']['value'])
        death_count_div.text = str(stats['death_count']['value'])
        
    #Div widget for stats bar
    stats = generate_stats('Manhattan')
    total_cases_div = Div(text= str(stats['total_cases']['value']),style={'font-size': '200%'}, name = 'total_cases')
    hosp_cases_div= Paragraph(text = str(stats['hosp_count']['value']),style={'font-size': '200%'}, name = 'hosp_cases')
    death_count_div = Div(text = str(stats['death_count']['value']), style={'font-size': '200%'}, name = 'death_count')
    curdoc().add_root(total_cases_div)
    curdoc().add_root(hosp_cases_div)
    curdoc().add_root(death_count_div)
    

    # Add Selection from checkbox/ Dropdown
    menu_it = boro_cases_df['BOROUGH_GROUP'][:5].tolist()
    dropdown = Select(title = "Boroughs", value ="Bronx", options = menu_it, name = 'dpdown')
    dropdown.on_change('value',update)

    # Initial Borough and data source
    src = make_dataset('Bronx')
    p = make_plot(src)
    p = style_left_plot(p)
    centre_graph = make_central_graph(boro_cases_df)
    centre_graph = style_center_plot(centre_graph)
    
    # Create a row layout
    minor_layout = column(dropdown, p, name = "m_layout")
    layout = row(column(dropdown, p), centre_graph, name = "layout")
    curdoc().add_root(dropdown)
    curdoc().add_root(p)
    curdoc().add_root(centre_graph)
    
    return layout, minor_layout


boro_cases_df = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/by-boro.csv')
layout, minor_layout = boro_tab(boro_cases_df)
curdoc().title = "Covid Dashboard"

