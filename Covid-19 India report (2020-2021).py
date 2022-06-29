
# The program fetches data from a CSV file containing various details about COVID-19 in India. It plots three graphs showing the confirmed cases, death toll, and total patients cured in four of the major states which were mostly effected by the pandemic; from 2020 to 2021. The four states are: Maharashtra, Kerela, Karnataka, and Tamil Nadu. 

# There is a fourth graph which is a bar graph, showing the report of the entire country and not just a state.


import pandas as pd
import matplotlib.pyplot as plt


# Reading the data:
    
data = pd.read_csv('Covid-19 India Report (2020-2021).csv')


# Assigning the informations to a variable:

#### Setting Date As Index:
data['Date'] = data['Date'].astype('datetime64')
data = data.set_index('Date')

#### Assigning:
states_name = data['State/UnionTerritory']
confirmed_cases = data['Confirmed']
cured = data['Cured']
deaths = data['Deaths']


# Deriving content for the four plots: 

#### Covid_19 Details Of The Entire Country:        
total_confirmed_cases = data['Confirmed'].sum()
total_cured = data['Cured'].sum()
total_deaths = data['Deaths'].sum()

# ...Getting Confirmed Cases, Death Toll & Number Of Paitents Cured Of The Four Major-Hit States... #

#### Kerela:
# >>> Confirmed Cases:
kerela_data = data[states_name == 'Kerala']
kerela_confirmed_cases_column = kerela_data['Confirmed']
# >>> Deaths:
kerela_deaths_column = kerela_data['Deaths']
# >>> Cured Patients:
cured_in_kerela_column = kerela_data['Cured']

#### Maharashtra:
# >>> Confirmed Cases:
maharashtra_data= data[states_name == 'Maharashtra']
maharashtra_confirmed_cases_column = maharashtra_data['Confirmed']
# >>> Deaths:
maharashtra_deaths_column = maharashtra_data['Deaths'] 
# >>> Cured Patients:
cured_in_maharashtra_column = maharashtra_data['Cured']
    
#### Karnataka: 
# >>> Confirmed Cases:
karnataka_data  = data[states_name == 'Karnataka']
karnataka_confirmed_cases_column = karnataka_data['Confirmed']
# >>> Deaths:
karnataka_deaths_column = karnataka_data['Deaths']
# >>> Cured Patients:
cured_in_karnataka_column = karnataka_data['Cured']
    
#### Tamil Nadu:
# >>> Confirmed Cases:
tamilnadu_data = data[states_name == 'Tamil Nadu']
tamilnadu_confirmed_cases_column = tamilnadu_data['Confirmed']
# >>> Deaths:
tamilnadu_deaths_column = tamilnadu_data['Deaths']
# >>> Cured Patients:
cured_in_tamilnadu_column = tamilnadu_data['Cured']


# Using a matplotlib custom style -- 'Ggplot': 

plt.style.use('ggplot')


# Creating four axes:
    
fig, axes = plt.subplots( nrows= 2, 
                          ncols= 2, 
                          sharex= False, 
                          constrained_layout= True
                          )


# Creating a class to plot the data:
    
class plot():    
    def __init__(self,axis,x_axis):
        self.axis = axis
        self.x_axis = x_axis 

#### Creating A Function To Plot The Three Line Graphs:
    def line_plot(self): 
# >>> For Customisation: 
        colors = [ 'Green', 
                   'Orange', 
                   'Red', 
                   'Yellow'
                    ]
        labels = [ 'Kerela', 
                   'Maharashtra', 
                   'Karnataka', 
                   'Tamil Nadu'
                    ]
# >>> Plotting:
        for x_axis,color,label in zip(self.x_axis,colors,labels):
            self.axis.plot( x_axis, 
                            color= color, 
                            label= label
                            )
# >>> Labeling (Using A Function Created Bellow):
            self.labelling()

#### Creating A Class Method To Plot The Last Graph:
    @classmethod   
    def bar_plot(cls,axis,x_axis,y_axis):
        cls.axis = axis
        cls.x_axis = x_axis
        cls.y_axis = y_axis
# >>> For Customisation:
        colors = [ 'Purple', 
                   'Green', 
                   'Red'
                    ]
# >>> Plotting:
        for color,x_axis,y_axis in zip(colors,cls.x_axis, cls.y_axis):
            cls.axis.bar( x_axis,y_axis,
                          color= color
                          )
# >>> Labeling (Using A Function Bellow):
            cls.labelling

#### Creating A Function To Label & Customize All The Plots:
    def labelling(self):                   
        axis = [ axes[0,0], 
                 axes[0,1], 
                 axes[1,0], 
                 axes[1,1] 
                 ]
        ylabels = [ 'Cases >', 
                    'Deaths >', 
                    'Cured >', 
                    'Total >' 
                     ] 
        titles = [ 'Confirmed Cases (Top 4 States)', 
                   'Death Toll (Top 4 States)',
                   'Cured Patients (Top 4 States)', 
                   'All India Report' 
                    ]
        for  ax,ylabel,title in zip(axis,ylabels,titles):                              
            ax.legend( loc= 'upper left',
                       prop= { 'weight': 'bold',
                               'size': 4
                                }
                       )        
            ax.set_title( title, 
                          fontsize= 6, 
                          fontweight= 'bold'
                          ) 
            ax.set_ylabel( ylabel, 
                           fontsize= 6, 
                           fontweight= 'bold'
                           )   
            ax.tick_params( axis= 'x', 
                            labelrotation= 30, 
                            labelsize= 6
                            )
            ax.tick_params( axis= 'y', 
                            labelsize= 6
                            )
# >>> Some More Customisation To The Bar Graph:
            axis[-1].tick_params( axis= 'both',
                                  bottom= False,
                                  labelrotation= False,
                                  labelsize= 6,
                                  ) 
            axis[-1].set_yscale('log')
# >>> Labeling The X-Ticks Of The Bar Graph:
            ticklabels = [ 'Confirmed Cases', 
                           'Cured Patients',
                           'Death Toll'
                            ]
            axis[-1].set_xticklabels( ticklabels,
                                      fontweight= 'bold'
                                      )
# >>> Giving A Title To The Entire Figure:            
            fig.suptitle( 'Covid-19 India Report (2020-2021):',
                           fontsize= 9, 
                           fontweight='bold'
                           ) 
            

# Creating the plots & plotting them:
 
#### Confirmed Cases:
plot( axis= axes[0,0], 
      x_axis= [ kerela_confirmed_cases_column, 
                maharashtra_confirmed_cases_column, 
                karnataka_confirmed_cases_column, 
                tamilnadu_confirmed_cases_column 
                ]
      ).line_plot()

#### Death Toll:
plot( axis= axes[0,1], 
      x_axis= [ kerela_deaths_column, 
                maharashtra_deaths_column, 
                karnataka_deaths_column, 
                tamilnadu_deaths_column
                ]
      ).line_plot()

#### Cured Patients:
plot( axis= axes[1,0], 
      x_axis= [ cured_in_kerela_column, 
                cured_in_maharashtra_column, 
                cured_in_karnataka_column, 
                cured_in_tamilnadu_column
                ]
      ).line_plot()

#### All India Report:
plot.bar_plot( axis= axes[1,1],
               x_axis= [ 'a','b','c'
                          ],
               y_axis= [ total_confirmed_cases,
                         total_cured,
                         total_deaths
                         ]
              )


# Showing the plots:

plt.show()


''' Created By Sourin Das '''