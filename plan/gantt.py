# pip install plotly kaleido
import os, sys
from datetime import datetime, timedelta
# https://plot.ly/python/gantt/
import plotly.figure_factory as ff

handy_week_converter = lambda week_n: datetime(2021, 3, 1) + timedelta(weeks=week_n)

# Homebrewed format: Name, starting week, ending week
tasks = [
    ("Write the project", 1, 16),
    ("Benchmark existing Danish NER", 1, 2),
    ("Benchmark English LUKE for NER", 1, 2),
    ("Literature search: KG + NLP", 1, 3),
    ("Literature search: NER", 1, 3),
    ("Get pre-training of daLUKE to work on multiple GPU's", 1, 3),
    ("Get NER fine-tuning and evaluation of daLUKE to work", 1, 3),
    ("Pre-train daBERT for NER on DaNE", 2, 4),
    ("Analyze daBERT predictions", 3, 5),
    ("Analyze English LUKE predictions", 3, 7),
    ("Explore approaches to generate more data", 3, 10),
    ("Search hyper-parameters", 4, 12),
    ("Analyze daLUKE predictions", 9, 15),
    ("Perform final pre-training", 11, 13),
    ("Finetune on DaNE", 13, 14),
    ("Deploy daLUKE for easy open-source use", 13, 16),
]
tasks = reversed(tasks)
fig = ff.create_gantt(
    [{'Task': task[0], 'Start': handy_week_converter(task[1]), 'Finish': handy_week_converter(task[2])} for task in tasks],
    showgrid_y=True, showgrid_x=True, title=None, height=750

)
fig.update_xaxes(
)
fig.update_layout(
    xaxis=dict(tickfont=dict(family='serif',size=10),
        rangeselector=None, dtick=24*60*60*1000*7 #millisecs to weeks
    ),
    yaxis=dict(tickfont=dict(family='serif',size=10)),
)
fig.write_image(os.path.join(sys.path[0], "imgs", "gantt.pdf"))
