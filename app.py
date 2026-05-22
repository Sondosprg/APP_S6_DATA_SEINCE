import streamlit as st
import pandas as pd
import numpy as np
import datetime
from data_analysis.analysis import results , analysis , Charts , getNameModules




st.title("DATA SCIENCE APP S6")

#  transpose df for easy processing (col=> row , row => col)
df = pd.read_json("data_analysis/data/s6.json").T

# for immutable 
df_copy = df


# configuration 
data_edited = st.data_editor(
    df_copy,
    column_config={
        "td": st.column_config.NumberColumn(
            "td",
            min_value=0,
            max_value=20,
        ),
        "tp": st.column_config.NumberColumn("tp", min_value=0, max_value=20),
        "exman": st.column_config.NumberColumn("exman", min_value=0, max_value=20),
        "coef": st.column_config.Column(disabled=True),
        "level": st.column_config.Column(disabled=True),
        "field": st.column_config.Column(disabled=True),
        "_index": st.column_config.Column(disabled=True),
    },
)






def displayResult(data_edited):
    
    general_average, data_edited_new  = results(data_edited)
    
    if general_average >=10:
         st.markdown(f" # general average : :green[{general_average:.2f} /20 ( success )] ")
    else:
        st.markdown(f" # general average : :red[ {general_average:.2f} /20  ( failed )]")
    
    
    st.markdown("###### details (sum / average)")
    st.write(data_edited_new)
    
    # show statical infos for each feature  (td , tp , examen)
    describe= analysis(data_edited_new)
    
    st.markdown('###### describe ')
    col1 , col2 , col3 , col4 = st.columns(4)
    with col1 : 
        st.write(describe["td"])
    with col2 : 
        st.write(describe["tp"])
    with col3 : 
        st.write(describe["exman"])
    with col4:
        st.write(describe["level"])

    average_modules , sum_modules , fig_average_level , fig_td , fig_tp , fig_examen = Charts(data_edited_new)
    
    st.markdown('###### top module cause in increasing average ')
    st.write(sum_modules.iloc[0])
    
    st.markdown('###### low  module cause in  decreasing average ')
    st.write(sum_modules.iloc[-1])
    
    st.markdown('###### distribution ')
    tab1_distr , tab2_dist = st.tabs(["distribution of modules averages" ,"distribution of modules sum"])
    
    with tab1_distr :
        st.bar_chart(average_modules)
    with tab2_dist:
        st.bar_chart(sum_modules)
    
    st.markdown('###### average modules by levels  ')
    st.plotly_chart(fig_average_level , use_container_width=True)
    
    st.markdown('###### distribution of td , tp , examen ')
    td_dist , tp_dist , examen_dist = st.tabs(["distribution of td" ,"distribution of  tp" ,"distribution of examen"])
    with td_dist:
        st.plotly_chart(fig_td , use_container_width=True)
    with tp_dist:
        st.plotly_chart(fig_tp , use_container_width=True)
    with examen_dist:
        st.plotly_chart(fig_examen , use_container_width=True)
    


# validate  df before calculations 
def validate(data_edited):
    
    #test if user not edit value of -1 (because is empty)
    if df[df[["td", "tp"]] == -1].equals(data_edited[data_edited[["td", "tp"]] == -1]):
        displayResult(data_edited)
    else:
        st.warning("WARNING : cannot modify -1 values (because is empty)")


def calculate():
    df_edited = data_edited.copy()
    validate(data_edited)
    

def generate_random_data():
    
    df_edited = data_edited.copy()
    
    # filter 
    df_true_not_empty_cell = (df_edited[['td' , 'tp' , 'exman']]!= -1)
    
    random_df = pd.DataFrame(
        np.where( df_true_not_empty_cell ,np.random.uniform(0.0 , 20.0 , size= df_true_not_empty_cell.shape).round(2) , df_true_not_empty_cell),
        columns = df_true_not_empty_cell.columns
    )
    
    # replace 0 by -1 (because it is empty cell)
    random_df= random_df.replace(0 ,-1 )


    # merge 
    contact_df = pd.concat([random_df.reset_index(drop=True) ,data_edited[['coef' , 'field' , 'level']].reset_index(drop=True)  ], axis = 1 )
    # set index by name of modules
    contact_df.index = getNameModules(data_edited)
    
    displayResult(contact_df)



# show main btns 
col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    st.button("calculate ∑", on_click=calculate)
with col3:
    st.button("random ⚄" , on_click = generate_random_data)




# copyRight section
st.markdown(f"&copy; copyright soLogic ` {datetime.date.today().year} ` [github](https://github.com/Sondosprg)")
