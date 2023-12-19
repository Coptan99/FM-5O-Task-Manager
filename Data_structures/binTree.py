import pandas as pd
import ipywidgets as widgets
from anytree import Node, RenderTree, PreOrderIter
import numpy as np

np.random.seed(42)
num_tasks = 10
data = {
    'Task Name': [f'Task {i}' for i in range(1, num_tasks + 1)],
    'Numbering Tasks': np.arange(1, num_tasks + 1),
    'runtime_type': np.random.choice([0, 1], num_tasks)
}

df = pd.DataFrame(data)

root = Node("Root")

def create_binary_tree(parent, tasks):
    if not tasks:
        return

    mid = len(tasks) // 2
    left_child = Node(tasks[mid], parent=parent)
    right_child = Node(tasks[mid - 1], parent=parent)

    create_binary_tree(left_child, tasks[:mid])
    create_binary_tree(right_child, tasks[mid + 1:])

sorted_tasks = sorted(df['Task Name'])
create_binary_tree(root, sorted_tasks)

def handle_button_click(task_name):
    print(f'Button clicked for task: {task_name}')

for node in PreOrderIter(root):
    task_name = node.name
    button = widgets.Button(description=f'Add Note for {task_name}')
    setattr(node, 'button', button)

    def on_button_click(b, task_name=task_name):
        handle_button_click(task_name)

    button.on_click(on_button_click)

tree_container = widgets.VBox()
for pre, _, node in RenderTree(root):
    if hasattr(node, 'button'):
        tree_container.children += (widgets.HBox([widgets.Label(pre + str(node.name)), node.button]),)

#tree_container
