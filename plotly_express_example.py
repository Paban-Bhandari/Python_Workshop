import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Time': [1, 2, 3, 4, 5],
    'Value': [10, 15, 7, 12, 9]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a line plot with Plotly Express
fig = px.line(df, x='Time', y='Value', title='Line Plot Example')

# Show the plot
fig.show()