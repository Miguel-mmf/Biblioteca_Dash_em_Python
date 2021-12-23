# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#               Esse arquivo possui algumas modificações em relação ao arquivo apresentado no vídeo do YouTube
#                          Não deixe de assistir o vídeo e estudar pela documentação ofical Dash
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# importando as bibliotecas necessárias
import dash
from dash import dcc, html
# import dash_core_components as dcc
# import dash_html_components as html

# adicionando um estilo externo através do link abaixo
    # esse link é o recomendado pela documentação da biblioteca Dash e ao acessar esse link no seu navegador,
    # você perceberá que ele possui a estrutura de um arquivo CSS

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# criando a aplicação por meio da função Dash do pacote dash e atribuindo a variável app

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

# esse dicionários será utilizado para mudar a cor de fundo além de mudar a cor do texto na aplicação Web
colors = {
    'background':'#8FBC8F',
    'text':'#11111'
}

# criando um layout para a variável app
# adicionando ao layout um componente html.Div que irá conter os demais componentes que dão forma

app.layout = html.Div(children=[

    # inserindo um componente da biblioteca dash HTML components como título/cabeçalho do layout
    html.H1(
        ['Dash - Exemplo de Layout com Gráfico'], style={'textAlign':'center', 'color':colors['text']}
    ),

    # adicionando um novo texto ao layout, porém utilizando um html.Div ("caixa", explicarei no vídeo sobre a biblioteca dash HTML components)
    html.Div(children='''
        Universidade Federal da Paraíba.
        Engenharia Elétrica.
    ''',
        # o parâmetro style define estilos css para o componente
        style={'textAlign':'center', 'color': colors['text'] }
    ),

    # inserindo um gráfico com o a função Graph() do pacote dash core components
    dcc.Graph(
        # identidade/nome do componente
        id='example-graph',
        # o parâmetro figure carrega os dados (data, layout, frames) necessários para a construção do gráfico
        figure={
            'data': [

                # primeiro traço
                {'x':[1,2,3], 'y': [4,1,2],'type': 'bar', 'name': 'primeiro traço'},

                # segundo traço
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'segundo traço'},
                ],

                # modificando o layout
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
    ],
    style= {'background':colors['background']}
)

# servindo a aplicação em dash como versão para teste
if __name__ == '__main__':
    app.run_server(debug=True)