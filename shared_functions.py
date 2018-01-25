
################################################################
# __      ___                 _ _          _   _             
# \ \    / (_)               | (_)        | | (_)            
#  \ \  / / _ ___ _   _  __ _| |_ ______ _| |_ _  ___  _ __  
#   \ \/ / | / __| | | |/ _` | | |_  / _` | __| |/ _ \| '_ \ 
#    \  /  | \__ \ |_| | (_| | | |/ / (_| | |_| | (_) | | | |
#     \/   |_|___/\__,_|\__,_|_|_/___\__,_|\__|_|\___/|_| |_|
################################################################

# plotly part
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import plotly.plotly as py
import plotly.graph_objs as go


def make_plotly_graph(traces, labels, title, mode='scatter', xtitle='', ytitle=''):
    if(len(traces)!=len(labels)):
        print ("ERROR in make_plotly_graph: len(traces)!=len(labels)")
        return
    
    if(mode=='scatter'):
        barmode='overlay'
    elif(mode=='stack'):
        barmode='stack'

    plotly_traces = []
    for trace, label in zip(traces, labels):
        if(mode=='scatter'):
            plotly_trace = go.Scatter(
                x= trace.index,
                y= trace,
                name = label,
                #mode = 'lines+markers',
                mode = 'lines',
                #fill='tozeroy'
            )
        elif(mode=='stack'):
            plotly_trace = go.Bar(
                x= trace.index,
                y= trace,
                name = label)
        else:
            print("ERROR: unknown mode")
            return
        plotly_traces.append(plotly_trace)
    

    layout = go.Layout(title=title,
                       barmode=barmode,
                       legend=dict(orientation="h", x=-.1, y=1.1),
                       xaxis=dict(title=xtitle),
                       yaxis=dict(title=ytitle, rangemode='tozero',
                                  #range=[0., ymax*1.10] 
                                  ),
                       )

    fig = go.Figure(data=plotly_traces, layout=layout)
    iplot(fig)



################################################################
#  ______         _                    ______             _                      _             
# |  ____|       | |                  |  ____|           (_)                    (_)            
# | |__ ___  __ _| |_ _   _ _ __ ___  | |__   _ __   __ _ _ _ __   ___  ___ _ __ _ _ __   __ _ 
# |  __/ _ \/ _` | __| | | | '__/ _ \ |  __| | '_ \ / _` | | '_ \ / _ \/ _ \ '__| | '_ \ / _` |
# | | |  __/ (_| | |_| |_| | | |  __/ | |____| | | | (_| | | | | |  __/  __/ |  | | | | | (_| |
# |_|  \___|\__,_|\__|\__,_|_|  \___| |______|_| |_|\__, |_|_| |_|\___|\___|_|  |_|_| |_|\__, |
#                                                    __/ |                                __/ |
#                                                   |___/                                |___/ 
################################################################






################################################################
#  __  __           _      _     
# |  \/  |         | |    | |    
# | \  / | ___   __| | ___| |___ 
# | |\/| |/ _ \ / _` |/ _ \ / __|
# | |  | | (_) | (_| |  __/ \__ \
# |_|  |_|\___/ \__,_|\___|_|___/
################################################################                                
                                
