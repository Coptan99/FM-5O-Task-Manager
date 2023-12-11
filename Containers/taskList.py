import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import numpy as np


np.random.seed(42)
num_tasks = 10
data = {
    'No.': np.arange(1, num_tasks + 1),
    'Task Name': [f'Task {i}' for i in range(1, num_tasks + 1)],
    'runtime_type': np.random.choice([0, 1], num_tasks)
}


df = pd.DataFrame(data)


def handle_button_click(task_name):
    print(f"Button clicked for {task_name}")


if 'runtime_type' in df.columns and (df['runtime_type'] == 1).any():
    df['Notes'] = df.apply(lambda row: widgets.Button(description=f'Add Note for {row["Task Name"]}'), axis=1)

    def on_button_click(b):
        task_name = b.description.split()[-1]
        handle_button_click(task_name)

    for button in df['Notes']:
        button.on_click(on_button_click)


display(df)
