# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#               Esse arquivo possui algumas modificações em relação ao arquivo apresentado no vídeo do YouTube
#                          Não deixe de assistir o vídeo e estudar pela documentação ofical Dash
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# importando as bibliotecas necessárias
import dash
import dash_core_components as dcc
import dash_html_components as html

# importando as funções que auxiliam no funcionamento das callbacks do subpacote dependencies do pacote dash 
from dash.dependencies import Input, Output

# importando o módulo graph_objects da biblioteca plotly
import plotly.graph_objects as go

# adicionando um estilo externo através do link abaixo
    # esse link é o recomendado pela documentação da biblioteca Dash e ao acessar esse link no seu navegador,
    # você perceberá que ele possui a estrutura de um arquivo CSS

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# criando a aplicação por meio da função Dash do pacote dash e atribuindo a variável app

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

# criando uma função para gerar um gráfico com a biblioteca plotly.graph_objects
def gera_grafico(tipo):

    # criando uma figura
    # caso você faça print(fig), um dicionário será apresentado uma vez que as figuras podem ser representadas dessa forma, necessitando de módulos da biblioteca plotly para trabalhar com as informações
    fig = go.Figure()
    # https://plotly.com/python/creating-and-updating-figures/

    # adicionando um traço a figura
    fig.add_trace(
        go.Scatter(
            x=[0,1,2,3,4,5,6],
            y=[0,1,2,3,4,5,6],
            mode=tipo,
            name='Reta',
            )
        )

    fig.add_trace(
        go.Scatter(
            x=[0,1,2,3,4,5,6],
            y=[0,1,4,9,16,25,36],
            mode=tipo,
            name='Parábola',
            )
        )
    
    # adicionando um título ao gráfico
    fig.update_layout(title='Gráfico Exemplo')

    # variável retornada pela função gera_grafico(tipo)
    return fig


# criando um layout para a variável app
# adicionando ao layout um componente html.Div que irá conter os demais componentes que dão forma 

app.layout = html.Div([

    # inserindo um componente da biblioteca dash HTML components como título/cabeçalho do layout
    html.H2(
        ['Painel de Visualização de Gráficos'],
        
         # o parâmetro style define estilos css para o componente
        style={
            'textAlign':'center', # texto alinhado
            'font-weight':'bold' # texto em negrito
        }
    ),

    # adicionando uma linha horizontal no layout
    html.Hr(),

    # criando abas pai dentro do layout
    dcc.Tabs(

        # identidade/nome do componente
        id='tabs',

        # criando as abas filhas dentro do parâmetro children da função Tabs()
        children=[
            dcc.Tab(label='Gráfico de linha',value='tab-1'),
            dcc.Tab(label='Gráfico de Barra',value='tab-2'),
            dcc.Tab(label='Gráfico de Linha e Pontos',value='tab-3')
        ]
    ),

    # onde será apresentado o conteúdo das abas logo após a callback ser ativada
    html.Div(id='tabs-content'),

    html.Hr(),
])

# Callback

# estruturando a callback com as entradas (input) e saídas (output)
@app.callback(
    # Output(component_id,component_property)
    Output('tabs-content','children'),
    [
        # Input(component_id,component_property)
        Input('tabs','value')
    ]
)

# função que será chamada pela callback
def update_tab(tab):

    # quando a aba com valor igual a 'tab-1' for selecionada, a propriedade children do componente 'tabs-content'
    # receberá o gráfico de linha retornado abaixo pela função gera_gráfico(tipo='lines')
    if tab == 'tab-1':
        return html.Div([
            dcc.Graph(figure = gera_grafico('lines'))
        ])


    # quando a aba com valor igual a 'tab-2' for selecionada, a propriedade children do componente 'tabs-content'
    # receberá o gráfico de barras construído e retornado abaixo
    elif tab == 'tab-2':
        fig_bar = go.Figure()

        fig_bar.add_trace(
            go.Bar(
                x=[0,1,2,3,4,5,6],
                y=[0,1,2,3,4,5,6],
                )
            )

        fig_bar.add_trace(
            go.Bar(
                x=[0,1,2,3,4,5,6],
                y=[0,1,4,9,16,25,36],
                )
            )

        fig_bar.update_layout(title='Gráfico em Barras Exemplo')
        
        return html.Div([
            dcc.Graph(figure = fig_bar)
        ])

    # quando a aba com valor igual a 'tab-3' for selecionada, a propriedade children do componente 'tabs-content'
    # receberá o gráfico de linha retornado abaixo pela função gera_gráfico(tipo='lines+markers')
    elif tab == 'tab-3':
        return html.Div([
            dcc.Graph(figure = gera_grafico('lines+markers'))
        ])
    
    # caso nenhuma das condições acima sejam aceitas, significa que existe um erro, e assim, retornamos a mensagem de erro
    else:
        return html.Div(['Erro!'])


# servindo a aplicação em dash como versão para teste
if __name__ == "__main__":
    app.run_server(debug=True)