import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

COLORS = {"primary": "#1f77b4", "accent": "#ff7f0e", "green": "#2ca02c", "red": "#d62728"}

def line_chart(df: pd.DataFrame, x: str, y: str, title: str, y_label: str = "") -> go.Figure:
    fig = px.line(df, x=x, y=y, title=title, labels={y: y_label or y, x: ""})
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="sans-serif", size=13),
        title_font_size=16,
        hovermode="x unified",
        margin=dict(l=40, r=20, t=50, b=40),
    )
    fig.update_traces(line_color=COLORS["primary"], line_width=2)
    return fig

def bar_chart(df: pd.DataFrame, x: str, y: str, title: str, y_label: str = "") -> go.Figure:
    fig = px.bar(df, x=x, y=y, title=title, labels={y: y_label or y, x: ""})
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="sans-serif", size=13),
        title_font_size=16,
        margin=dict(l=40, r=20, t=50, b=40),
    )
    fig.update_traces(marker_color=COLORS["primary"])
    return fig
