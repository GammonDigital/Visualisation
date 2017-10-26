import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.gridspec import GridSpec


# Pi size
CO2e = [89305,112196,94944,94293]
CO2e_np = np.array(CO2e)

# Create dataframes
xlsx = pd.ExcelFile('CarbonV1-1.xlsx')

CO2_16df = pd.read_excel(xlsx, 'Division 2016').iloc[0::, 0:2].set_index(['Division'])
CO2_15df = pd.read_excel(xlsx, 'Division 2015').iloc[0::, 0:2].set_index(['Division'])
CO2_14df = pd.read_excel(xlsx, 'Division 2014').iloc[0::, 0:2].set_index(['Division'])
CO2_13df = pd.read_excel(xlsx, 'Division 2013').iloc[0::, 0:2].set_index(['Division'])
CO2_df_list = [CO2_16df, CO2_15df, CO2_14df, CO2_13df]
#CO2_df = CO2_16df.join(CO2_15df).join(CO2_14df).join(CO2_13df)

GHG_16df = pd.read_excel(xlsx, 'Division 2016').iloc[0:1, 14::].set_index(['Year']).T
GHG_15df = pd.read_excel(xlsx, 'Division 2015').iloc[0:1, 14::].set_index(['Year']).T
GHG_14df = pd.read_excel(xlsx, 'Division 2014').iloc[0:1, 14::].set_index(['Year']).T
GHG_13df = pd.read_excel(xlsx, 'Division 2013').iloc[0:1, 14::].set_index(['Year']).T
GHG_df_list = [GHG_16df, GHG_15df, GHG_14df, GHG_13df]
#GHG_df = GHG_16df.join(GHG_15df).join(GHG_14df).join(GHG_13df)


# CO2 Plots

# Make square figures and axes
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(11, 11, forward=True)
#fig.tight_layout()
explode = (0,0,0,0.05,0.075,0.1,0.125)
##title = ("Total CO2 {0:.0f}kg".format(CO2_16df.values.sum()), "Total CO2 {0:.0f}kg".format(CO2_15df.values.sum()), "Total CO2 {0:.0f}kg".format(CO2_14df.values.sum()), "Total CO2 {0:.0f}kg".format(CO2_13df.values.sum()))
##radius = (np.array([CO2_16df.values.sum(), CO2_15df.values.sum(), CO2_14df.values.sum(), CO2_13df.values.sum()])/max(CO2_16df.values.sum(), CO2_15df.values.sum(), CO2_14df.values.sum(), CO2_13df.values.sum())).tolist()
##CO2_df.plot.pie(subplots=True,\
##                figsize=(10,10),\
##                layout=(2,2),\
##                explode = explode,\
##                title=title,\
##                autopct='%1.1f%%',\
##                legend=(False,True,False,False),\
##                radius=radius
##                )

for i in range(4):
    gridx = 0 if i < 2 else 1
    gridy = 0 if i%2 == 0 else 1
    legend = False if i == 1 else False #OPTION: change to TRUE to display one legend
    CO2plot = CO2_df_list[i].plot.pie(subplots=True,\
                               title="Yearly CO2 Distribution by Division\n*'Others' include CON, E&M, Head Office, China and SFB",\
                               ax=axes[gridx,gridy], autopct='%1.1f%%',\
                               explode=explode,\
                               legend=legend,\
                               fontsize=9,\
                               radius=CO2e[i]/max(CO2e))
                               #radius=CO2_df_list[i].values.sum()/max(CO2_16df.values.sum(), CO2_15df.values.sum(), CO2_14df.values.sum(), CO2_13df.values.sum()))
plt.subplots_adjust(wspace=0.3)

#GHG Plots
fig2, axes = plt.subplots(nrows=2, ncols=2)
fig2.set_size_inches(11, 11, forward=True)
#fig2.tight_layout()
explode2 = [0,0,0,0,0.1,0.2]

for i in range(4):
    gridx = 0 if i < 2 else 1
    gridy = 0 if i%2 == 0 else 1
    GHGplot = GHG_df_list[i].plot.pie(subplots=True,\
                                      title="Yearly GHG Contribution by Emission Type\n*'Others' include LPG, TownGas, WD40, Septic Tank and Fire Extinguisher",\
                                      ax=axes[gridx, gridy],\
                                      explode=explode2,\
                                      autopct='%1.1f%%',\
                                      legend=False,\
                                      fontsize=9,\
                                      radius=CO2e[i]/max(CO2e))
plt.subplots_adjust(wspace=0.3)

plt.show()