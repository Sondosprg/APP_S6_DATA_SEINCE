import pandas as pd
import plotly.express as px



def getNameModules(df):
    return df.index.tolist()



# calculate
def results(df):
    
    # convert datatype 
    df[["td" , "tp","exman"]] = df[["td" , "tp" , "exman"]].astype(float)
    df["coef"] = df["coef"].astype(int)
    
    
    list_averages = []
    names = getNameModules(df)
    sum_average = 0
    sum_ = 0
    average = 0

    
    for name in names:
        if df.loc[name]["td"] == -1 and df.loc[name]["tp"] == -1:

            sum_ = average = (
                df.loc[name]["exman"] * df.loc[name]["coef"]
            )
        elif df.loc[name]["td"] == -1:
            average = (
                df.loc[name]["tp"] * 0.4 + df.loc[name]["exman"] * 0.6
            )
            sum_ = average * df.loc[name]["coef"]
        elif df.loc[name]["tp"] == -1:
            average = (
                df.loc[name]["td"] * 0.4 + df.loc[name]["exman"] * 0.6
            )
            sum_ = average * df.loc[name]["coef"]
        else:
            average = (
                df.loc[name]["td"] * 0.2
                + df.loc[name]["tp"] * 0.2
                + df.loc[name]["exman"] * 0.6
            )
            sum_ = average * df.loc[name]["coef"]

        print(f"avearge : {average:.2f} ")
        sum_average += sum_
        list_averages.append(average)
    
    
    df["average"] = list_averages
    df["sum"] = df["coef"]*df["average"]
    
    general_average = sum_average / 20
    
    return general_average, df




def names_td_tp(df):
    return list(df[df['td'] != -1].index.values) , list(df[df['tp'] != -1].index.values)

def analysis(df):
    
    names_only_td , names_only_tp = names_td_tp(df)
    
    # constant analysis
    level_count  = df["level"].value_counts() 
    
    return {
        "td":df['td'].loc[names_only_td].describe(),
        "tp":df["tp"].loc[names_only_tp].describe(),
        "exman":df["exman"].describe(),
        "level":level_count
    }
    

def Charts(df):
    # distribution of averages
    average_modules = pd.DataFrame({
        "average" : df["average"]
    } , index = df.index).sort_values(by = "average"  , ascending = False)
    
    # distribution of sum
    sum_modules = pd.DataFrame({
     "sum" : df["sum"]
    } , index = df.index).sort_values(by = "sum"  , ascending = False)


    # level by average 
    average_level = df.groupby("level")["average"].sum()
    average_level_df = pd.DataFrame({
        "level" : average_level.index,
        "average" : average_level.values
    }).sort_values(by = "average"  , ascending = False)
    
    fig_average_level = px.pie(average_level_df , names = "level" , values = "average")
    
    
    # field by average 
    average_field = df.groupby("field")["average"].sum()
    average_field_df = pd.DataFrame({
        "field" : average_field.index,
        "average" : average_field.values
    }).sort_values(by = "average"  , ascending = False)
    
    fig_average_field = px.pie(average_field_df , names = "field" , values = "average")
    
    
    # distribution of td , tp , examen
    names_only_td , names_only_tp = names_td_tp(df)
    
    tds = df['td'].loc[names_only_td] 
    fig_td = px.violin( tds, points="all" , box = True)
    
    
    tps = df['tp'].loc[names_only_tp] 
    fig_tp = px.violin( tps,  points= "all", box=True )
    
        
    examens = df['exman'] 
    fig_examen = px.violin( examens, points= "all", box=True )
    
    return average_modules ,  sum_modules  , fig_average_level ,fig_average_field, fig_td , fig_tp , fig_examen

