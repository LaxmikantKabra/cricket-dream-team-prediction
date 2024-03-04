from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import viridis

df = pd.read_csv("Combined.csv")
duration_mins_secs = [
    str(f"{i}:{j}")
    for i, j in zip(
        [int(i // 1) for i in list(df["Duration"])],
        [int(round((i % 1) * 60, 2)) for i in list(df["Duration"])],
    )
]
df["Track Duration"] = duration_mins_secs

p1 = pd.read_csv("Playlist1.csv")
p1 = pd.DataFrame(
    p1[
        [
            "Acousticness",
            "Danceability",
            "Energy",
            "Instrumentalness",
            "Speechiness",
            "Valence",
        ]
    ].mean()
).T
p2 = pd.read_csv("Playlist2.csv")
p2 = pd.DataFrame(
    p2[
        [
            "Acousticness",
            "Danceability",
            "Energy",
            "Instrumentalness",
            "Speechiness",
            "Valence",
        ]
    ].mean()
).T
p = pd.concat([p1, p2], ignore_index=True)

artists = pd.read_csv("All Artists.csv")
artists["Index"] = artists.index

genres = pd.read_csv("Genres.csv")
genres["Index"] = genres.index

collabs = pd.read_csv("All Collaborations.csv")

artists_songs = pd.read_csv("Common Artist Songs.csv")

genre_songs = pd.read_csv("Common Genre Songs.csv")

new_songs = pd.read_csv("New Playlist.csv")
duration_mins_secs = [
    str(f"{i}:{j}")
    for i, j in zip(
        [int(i // 1) for i in list(new_songs["Duration"])],
        [int(round((i % 1) * 60, 2)) for i in list(new_songs["Duration"])],
    )
]
new_songs["Track Duration"] = duration_mins_secs

cols = ["Popularity", "Tempo", "Danceability", "Energy", "Acousticness", "Valence"]
scatter_cols = ["Acousticness", "Danceability", "Energy", "Tempo", "Valence"]
hist_cols = [
    "Popularity",
    "Tempo",
    "Danceability",
    "Energy",
    "Loudness",
    "Speechiness",
    "Acousticness",
    "Instrumentalness",
    "Liveliness",
    "Valence",
]


# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
app.title = "Visual Tunes"


# Define the layout and callbacks for page 1
page1_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="left",
                    children=[
                        dbc.Label("Comparing Playlists - CDF Plots"),
                        dcc.Graph(id="viz-1"),
                    ],
                ),
                dbc.Col(
                    width=2,
                    align="right",
                    children=[
                        html.Div(
                            [
                                html.Label("Field"),
                                dcc.Dropdown(
                                    id="field",
                                    value=hist_cols[0],
                                    options=[
                                        {"label": col, "value": col}
                                        for col in hist_cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Bins"),
                                dcc.Slider(
                                    id="nbins",
                                    min=5,
                                    max=200,
                                    marks=None,
                                    step=1,
                                    value=10,
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Alpha"),
                                dcc.Slider(
                                    id="opacity", min=0, max=1, marks=None, value=0.5
                                ),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("viz-1", "figure"),
    [Input("field", "value"), Input("nbins", "value"), Input("opacity", "value")],
)
def update_chart(field, nbins, opacity):
    fig = px.histogram(
        df,
        x=field,
        histfunc="count",
        nbins=nbins,
        color="Playlist",
        color_discrete_sequence=["limegreen", "fuchsia"],
        opacity=opacity,
        cumulative=True,
        width=1400,
        height=600,
    )
    fig.update_layout(
        barmode="overlay",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        yaxis={"showgrid": False},
        xaxis={"showgrid": False},
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )
    return fig


page2_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="center",
                    children=[
                        dbc.Label("Comparing Playlists - Scatterplot"),
                        dcc.Graph(id="viz-2"),
                    ],
                ),
                dbc.Col(
                    width=2,
                    align="center",
                    children=[
                        html.Div(
                            [
                                html.Label("X-Axis"),
                                dcc.Dropdown(
                                    id="xax",
                                    value=scatter_cols[0],
                                    options=[
                                        {"label": col, "value": col}
                                        for col in scatter_cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Y-Axis"),
                                dcc.Dropdown(
                                    id="yax",
                                    value=scatter_cols[1],
                                    options=[
                                        {"label": col, "value": col}
                                        for col in scatter_cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Size"),
                                dcc.Dropdown(
                                    id="size",
                                    value=scatter_cols[2],
                                    options=[
                                        {"label": col, "value": col}
                                        for col in scatter_cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Alpha"),
                                dcc.Slider(id="opacity", min=0, max=1, value=0.5),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("viz-2", "figure"),
    [
        Input("xax", "value"),
        Input("yax", "value"),
        Input("size", "value"),
        Input("opacity", "value"),
    ],
)
def update_figure(xax, yax, size, opacity):
    hover_dict = {
        xax: False,
        yax: False,
        size: False,
        "Playlist": False,
        "Album": True,
        "Artist(s)": True,
        "Track Duration": True,
        "Popularity": True,
    }
    fig = px.scatter(
        df,
        x=xax,
        y=yax,
        size=size,
        color="Playlist",
        trendline="ols",
        color_discrete_sequence=["limegreen", "fuchsia"],
        hover_name="Track_Name",
        hover_data=hover_dict,
        size_max=25,
        opacity=opacity,
        width=1400,
        height=600,
    )
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        yaxis={"showgrid": False},
        xaxis={"showgrid": False},
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )
    fig.update_traces(opacity=opacity)
    return fig


page3_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="center",
                    children=[
                        dbc.Label("Comparing Playlists - Radar Plot"),
                        dcc.Graph(id="viz-3"),
                    ],
                ),
                dbc.Col(
                    width=2,
                    align="center",
                    children=[
                        html.Div(
                            [
                                html.Label("Alpha"),
                                dcc.Slider(
                                    id="opacity",
                                    min=0,
                                    max=1,
                                    value=0.5,
                                    marks=None,
                                    step=None,
                                ),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(Output("viz-3", "figure"), Input("opacity", "value"))
def update_figure1(opacity):
    trace1 = go.Scatterpolar(
        r=list(p.iloc[0, :]),
        theta=list(p.columns),
        fill="toself",
        fillcolor="limegreen",
        line=dict(color="black", width=1),
        name="Playlist 1",
    )
    trace2 = go.Scatterpolar(
        r=list(p.iloc[1, :]),
        theta=list(p.columns),
        fill="toself",
        fillcolor="fuchsia",
        line=dict(color="black", width=1),
        name="Playlist 2",
    )
    layout = go.Layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        height=600,
        width=1400,
        plot_bgcolor="rgba(0, 0, 0, 0)",
    )
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    fig.update_layout(
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell")
    )
    fig.update_traces(opacity=opacity)
    return fig


page4_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="center",
                    children=[dbc.Label("Top Artists"), dcc.Graph(id="viz-4")],
                ),
                dbc.Col(
                    width=2,
                    align="center",
                    children=[
                        html.Div(
                            [
                                html.Label("Measure"),
                                dcc.Dropdown(
                                    id="measure",
                                    value="Followers",
                                    options=[
                                        {"label": col, "value": col}
                                        for col in ["Followers", "Popularity"]
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Top N"),
                                dcc.Slider(
                                    id="topn",
                                    min=5,
                                    max=25,
                                    marks=None,
                                    step=1,
                                    value=15,
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Alpha"),
                                dcc.Slider(id="opacity", min=0, max=1, value=0.5),
                            ]
                        ),
                    ],
                ),
            ]
        )
    ],
    fluid=True,
)


@app.callback(
    Output("viz-4", "figure"),
    [Input("measure", "value"), Input("topn", "value"), Input("opacity", "value")],
)
def update_figure2(measure, topn, opacity):
    hover_dict = {
        measure: False,
        "Index": False,
        "Name": False,
        "Playlist": False,
        "Genres": True,
        "Popularity": True,
        "Followers": True,
        "Total Count": False,
    }
    fig = px.scatter(
        artists.sort_values(by=measure, ascending=False).head(topn),
        x="Index",
        y=measure,
        text="Name",
        size="Total Count",
        size_max=100,
        color="Playlist",
        color_discrete_map={
            "Playlist 1": "limegreen",
            "Playlist 2": "fuchsia",
            "Both": "yellow",
        },
        hover_name="Name",
        hover_data=hover_dict,
        opacity=opacity,
        width=1400,
        height=600,
    )
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        yaxis={"showgrid": False},
        xaxis={"showgrid": False},
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )
    return fig


page5_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="center",
                    children=[dbc.Label("Top Genres"), dcc.Graph(id="viz-5")],
                ),
                dbc.Col(
                    width=2,
                    align="center",
                    children=[
                        html.Div(
                            [
                                html.Label("Top N"),
                                dcc.Slider(
                                    id="topn",
                                    min=5,
                                    max=25,
                                    marks=None,
                                    step=1,
                                    value=15,
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Alpha"),
                                dcc.Slider(id="opacity", min=0, max=1, value=0.5),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("viz-5", "figure"), [Input("topn", "value"), Input("opacity", "value")]
)
def update_figure(topn, opacity):
    hover_dict = {
        "Index": False,
        "Genre": False,
        "Playlist": False,
        "Total Count": True,
    }
    fig = px.scatter(
        genres.sort_values(by="Total Count", ascending=False).head(topn),
        x="Total Count",
        y="Index",
        text="Genre",
        size="Total Count",
        size_max=100,
        color="Playlist",
        color_discrete_map={
            "Playlist 1": "limegreen",
            "Playlist 2": "fuchsia",
            "Both": "yellow",
        },
        hover_name="Genre",
        hover_data=hover_dict,
        opacity=opacity,
        width=1400,
        height=600,
    )
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        yaxis={"showgrid": False},
        xaxis={"showgrid": False},
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )
    return fig


page6_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="center",
                    children=[
                        dbc.Label("Collaboration Network"),
                        dcc.Graph(id="viz-6"),
                    ],
                ),
                dbc.Col(
                    width=2,
                    align="center",
                    children=[
                        html.Div(
                            [
                                html.Label("Alpha"),
                                dcc.Slider(id="opacity", min=0, max=1, value=0.5),
                            ]
                        )
                    ],
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(Output("viz-6", "figure"), Input("opacity", "value"))
def update_figure3(opacity):
    G = nx.Graph()
    for i, j, k, l, m in zip(
        list(artists["Name"]),
        list(artists["Genres"]),
        list(artists["Popularity"]),
        list(artists["Followers"]),
        list(artists["Playlist"]),
    ):
        G.add_node(i)
        G.nodes[i]["Genres"] = j
        G.nodes[i]["Popularity"] = k
        G.nodes[i]["Followers"] = l
        G.nodes[i]["Playlist"] = m
    for i, j, k, l, m in zip(
        list(collabs["Artist 1"]),
        list(collabs["Artist 2"]),
        list(collabs["Popular Collab"]),
        list(collabs["Popularity"]),
        list(collabs["Artist From"]),
    ):
        G.add_edge(i, j)
        G.edges[(i, j)]["Popular Collab"] = k
        G.edges[(i, j)]["Popularity"] = l
        G.edges[(i, j)]["Artist From"] = m
    # nx.write_gexf(G, 'Collaboration Graph.gexf')

    pos = nx.spring_layout(G, k=0.99)
    pos = nx.rescale_layout_dict(pos, 1000)
    for n in G.nodes:
        G.nodes[n]["pos"] = pos[n]

    edge_x = []
    edge_y = []
    xtext = []
    ytext = []
    edgetext = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]["pos"]
        x1, y1 = G.nodes[edge[1]]["pos"]
        xtext.append((x0 + x1) / 2)
        ytext.append((y0 + y1) / 2)
        edgetext.append(
            f"Artist 1: {edge[0]}, \nArtist 2: {edge[1]},\n Collaboration: {G.edges[edge]['Popular Collab']}"
        )
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1, color="#888"),
        hoverinfo="text",
        mode="lines",
    )
    edge_trace.text = edgetext

    eweights_trace = go.Scatter(
        x=xtext,
        y=ytext,
        mode="markers",
        marker=dict(
            size=5,
            color="#888",
        ),
        text=edgetext,
        hoverinfo="text",
    )

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = G.nodes[node]["pos"]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        hoverinfo="text",
        marker=dict(color=[], size=[], line_width=0.5),
    )

    pd1 = {"Playlist 1": "limegreen", "Playlist 2": "fuchsia", "Both": "yellow"}

    node_size = []
    node_color = []
    node_text = []
    for n in G.nodes:
        node_size.append((nx.degree_centrality(G)[n] * 500) + 10)
        node_color.append(pd1[G.nodes[n]["Playlist"]])
        node_text.append(f"Name: {n},\nGenres: {G.nodes[n]['Genres']}")

    node_trace.marker.size = node_size
    node_trace.marker.color = node_color
    node_trace.text = node_text

    layout = go.Layout(
        showlegend=False,
        hovermode="closest",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=600,
        width=1400,
        plot_bgcolor="rgba(0, 0, 0, 0)",
    )

    fig = go.Figure(data=[edge_trace, eweights_trace, node_trace], layout=layout)
    fig.update_layout(
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell")
    )
    fig.update_traces(opacity=opacity)
    return fig


page7_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="center",
                    children=[
                        dbc.Label("Wall of Recommendations - Common Genres"),
                        dcc.Graph(id="viz-7"),
                    ],
                ),
                dbc.Col(
                    width=2,
                    align="center",
                    children=[
                        html.Div(
                            [
                                html.Label("Measure"),
                                dcc.Dropdown(
                                    id="measure",
                                    value=cols[0],
                                    options=[
                                        {"label": col, "value": col} for col in cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Top N"),
                                dcc.Slider(
                                    id="topn",
                                    min=5,
                                    max=25,
                                    marks=None,
                                    step=1,
                                    value=15,
                                ),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("viz-7", "figure"), [Input("measure", "value"), Input("topn", "value")]
)
def update_figure4(measure, topn):
    hover_dict = {"Artist(s)": True, measure: False, "Track_Name": False}
    fig = px.treemap(
        genre_songs.sort_values(by=measure, ascending=False).head(topn),
        path=["Common Genre", "Track_Name"],
        values=measure,
        color=measure,
        color_continuous_scale=px.colors.sequential.Purp,
        hover_name="Track_Name",
        hover_data=hover_dict,
    )
    fig.update_layout(
        width=1400,
        height=600,
        plot_bgcolor="rgba(0, 0, 0, 0)",
        yaxis={"showgrid": False},
        xaxis={"showgrid": False},
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )
    return fig


page8_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="center",
                    children=[
                        dbc.Label("Wall of Recommendations - Common Artists"),
                        dcc.Graph(id="viz-8"),
                    ],
                ),
                dbc.Col(
                    width=2,
                    align="center",
                    children=[
                        html.Div(
                            [
                                html.Label("Measure"),
                                dcc.Dropdown(
                                    id="measure",
                                    value=cols[0],
                                    options=[
                                        {"label": col, "value": col} for col in cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Top N"),
                                dcc.Slider(
                                    id="topn",
                                    min=5,
                                    max=25,
                                    marks=None,
                                    step=1,
                                    value=15,
                                ),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("viz-8", "figure"), [Input("measure", "value"), Input("topn", "value")]
)
def update_figure5(measure, topn):
    hover_dict = {"Artist(s)": True, measure: False, "Track_Name": False}
    fig = px.treemap(
        artists_songs.sort_values(by=measure, ascending=False).head(topn),
        path=["Common Artist", "Track_Name"],
        values=measure,
        color=measure,
        color_continuous_scale=px.colors.sequential.Purp,
        hover_name="Track_Name",
        hover_data=hover_dict,
    )
    fig.update_layout(
        width=1400,
        height=600,
        plot_bgcolor="rgba(0, 0, 0, 0)",
        yaxis={"showgrid": False},
        xaxis={"showgrid": False},
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )
    return fig


page9_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="center",
                    children=[
                        dbc.Label("Comparing Playlists - Scatterplot"),
                        dcc.Graph(id="viz-9"),
                    ],
                ),
                dbc.Col(
                    width=2,
                    align="center",
                    children=[
                        html.Div(
                            [
                                html.Label("X-Axis"),
                                dcc.Dropdown(
                                    id="xax",
                                    value=cols[0],
                                    options=[
                                        {"label": col, "value": col} for col in cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Y-Axis"),
                                dcc.Dropdown(
                                    id="yax",
                                    value=cols[1],
                                    options=[
                                        {"label": col, "value": col} for col in cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Size"),
                                dcc.Dropdown(
                                    id="size",
                                    value=cols[2],
                                    options=[
                                        {"label": col, "value": col} for col in cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Color"),
                                dcc.Dropdown(
                                    id="color",
                                    value=cols[3],
                                    options=[
                                        {"label": col, "value": col} for col in cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Alpha"),
                                dcc.Slider(
                                    id="opacity",
                                    min=0,
                                    max=1,
                                    value=0.5,
                                    step=None,
                                    marks=None,
                                ),
                            ]
                        ),
                    ],
                ),
            ]
        )
    ],
    fluid=True,
)


@app.callback(
    Output("viz-9", "figure"),
    [
        Input("xax", "value"),
        Input("yax", "value"),
        Input("size", "value"),
        Input("color", "value"),
        Input("opacity", "value"),
    ],
)
def update_figure6(xax, yax, size, color, opacity):
    hover_dict = {
        xax: False,
        yax: False,
        size: False,
        color: False,
        "Album": True,
        "Artist(s)": True,
        "Track Duration": True,
        "Popularity": True,
    }
    fig = px.scatter(
        new_songs,
        x=xax,
        y=yax,
        size=size,
        color=color,
        trendline="ols",
        color_continuous_scale="Purp",
        hover_name="Track_Name",
        hover_data=hover_dict,
        size_max=15,
        opacity=opacity,
        width=1400,
        height=600,
    )
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        yaxis={"showgrid": False},
        xaxis={"showgrid": False},
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )
    fig.update_traces(opacity=opacity)
    return fig


page10_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    width=10,
                    align="left",
                    children=[
                        dbc.Label("New Playlist - CDF Plot"),
                        dcc.Graph(id="viz-10"),
                    ],
                ),
                dbc.Col(
                    width=2,
                    align="right",
                    children=[
                        html.Div(
                            [
                                html.Label("Field"),
                                dcc.Dropdown(
                                    id="field",
                                    value=hist_cols[0],
                                    options=[
                                        {"label": col, "value": col}
                                        for col in hist_cols
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Bins"),
                                dcc.Slider(
                                    id="nbins",
                                    min=5,
                                    max=200,
                                    marks=None,
                                    step=1,
                                    value=10,
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Alpha"),
                                dcc.Slider(
                                    id="opacity", min=0, max=1, marks=None, value=0.5
                                ),
                            ]
                        ),
                    ],
                ),
            ]
        )
    ],
    fluid=True,
)


@app.callback(
    Output("viz-10", "figure"),
    [Input("field", "value"), Input("nbins", "value"), Input("opacity", "value")],
)
def update_chart1(field, nbins, opacity):
    fig = px.histogram(
        new_songs,
        x=field,
        histfunc="count",
        nbins=nbins,
        opacity=opacity,
        cumulative=True,
        width=1400,
        height=600,
    )
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        yaxis={"showgrid": False},
        xaxis={"showgrid": False},
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    )
    return fig


viz_titles = {
    1: "Comparing Playlists - CDF Plots",
    2: "Comparing Playlists - Scatterplot",
    3: "Comparing Playlists - Radar Plot",
    4: "Top Artists",
    5: "Top Genres",
    6: "Collaboration Network",
    7: "Wall of Recommendations - Common Genres",
    8: "Wall of Recommendations - Common Artists",
    9: "Comparing Playlists - Scatterplot 2",
    10: "New Playlist - CDF Plot",
}


# Define the common top header
common_top_header = dbc.NavbarSimple(
    children=[dbc.NavItem(dbc.NavLink("", href="/"))],
    brand_href="/",
    color="primary",
    dark=True,
)


welcome_page = html.Div(
    [
        html.H2("Welcome to Visual Tunes!"),
        html.P("Explore various visualizations related to music playlists."),
        html.P(
            "Click on the tabs above to navigate to different visualizations and explore insights into your music playlists."
        ),
        html.H3("Featured Visualizations:"),
        html.Ul(
            [
                html.Li(f"{viz_titles[1]} - Overview"),
                html.Li(f"{viz_titles[2]} - Scatterplot"),
                html.Li(f"{viz_titles[4]} - Top Genres"),
                html.Li(f"{viz_titles[6]} - Collaboration Network"),
            ]
        ),
        html.H3("Data Features"),
        html.Ul(
            [
                html.Li("Track_Name: Song name"),
                html.Li("Track_ID: Spotify ID for the song, used for search purposes"),
                html.Li("URL: Web URL for the son"),
                html.Li("Artist(s): All artists associated with the Song"),
                html.Li("Genres: Genres associated with the artists"),
                html.Li("Album: Album name that includes a Song"),
                html.Li(
                    "Song Popularity: song popularity score (0-100), based on no. of streams"
                ),
                html.Li(
                    "Artist Popularity: artist popularity score (0-100), based on no. of streams"
                ),
                html.Li("Duration: Song runtime"),
                html.Li("Tempo: Approx. beats per minute"),
                html.Li(
                    "Loudness: How loud a song is (dB). Key: 0-11, one of the 12 notes on a musical scale"
                ),
                html.Li("Mode: Major or minor"),
                html.Li(
                    "Danceability: A probabilistic measure of how danceable is a Song"
                ),
                html.Li(
                    "Instrumentalness: A probabilistic measure of the amount of vocals in a Song"
                ),
                html.Li(
                    "Liveliness: A probabilistic measure of the presence of a live audience"
                ),
                html.Li("Valence: A probabilistic measure of how positive is a Song"),
                html.Li(
                    "Time_Signature: The time signature (beats in a measure) of a Song"
                ),
            ]
        ),
    ]
)


main_page_layout = dbc.Container(
    [
        dbc.NavbarSimple(
            children=[common_top_header],
            brand="Visual Tunes",
            brand_href="/",
            color="primary",
            dark=True,
        ),
        dcc.Tabs(
            id="tabs",
            value="/",
            children=[
                dcc.Tab(label="Home", value="/home"),
                *[
                    dcc.Tab(label=f"{viz_titles[i]}", value=f"/viz-{i}")
                    for i in range(1, 11)
                ],
            ],
        ),
    ],
    fluid=True,
    style={"backgroundColor": "#f8f9fa"},
)


# Callback to update the content based on the selected tab
@app.callback(Output("page-content", "children"), [Input("tabs", "value")])
def display_tab(tab_value):
    if tab_value == "/viz-1":
        return html.Div([html.H2("Visualization 1"), page1_layout])
    elif tab_value == "/viz-2":
        return html.Div([html.H2("Visualization 2"), page2_layout])
    elif tab_value == "/viz-3":
        return html.Div([html.H2("Visualization 3"), page3_layout])
    elif tab_value == "/viz-4":
        return html.Div([html.H2("Visualization 4"), page4_layout])
    elif tab_value == "/viz-5":
        return html.Div([html.H2("Visualization 5"), page5_layout])
    elif tab_value == "/viz-6":
        return html.Div([html.H2("Visualization 6"), page6_layout])
    elif tab_value == "/viz-7":
        return html.Div([html.H2("Visualization 7"), page7_layout])
    elif tab_value == "/viz-8":
        return html.Div([html.H2("Visualization 8"), page8_layout])
    elif tab_value == "/viz-9":
        return html.Div([html.H2("Visualization 9"), page9_layout])
    elif tab_value == "/viz-10":
        return html.Div([html.H2("Visualization 10"), page10_layout])
    else:
        return welcome_page


# Define the overall layout
app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh=False),
        main_page_layout,
        html.Div(id="page-content"),
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(port=8080, debug=True)
