# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#               Esse arquivo possui algumas modificações em relação ao arquivo apresentado no vídeo do YouTube
#                          Não deixe de assistir o vídeo e estudar pela documentação ofical Dash
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# importando as bibliotecas necessárias
import dash
import dash_core_components as dcc
import dash_html_components as html

# adicionando um estilo externo através do link abaixo
    # esse link é o recomendado pela documentação da biblioteca Dash e ao acessar esse link no seu navegador,
    # você perceberá que ele possui a estrutura de um arquivo CSS

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# criando a aplicação por meio da função Dash do pacote dash e atribuindo a variável app

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

# criando um layout para a variável app
# adicionando ao layout um componente html.Div que irá conter os demais componentes que dão forma
app.layout = html.Div([

    # inserindo uma linha horizontal no layout
    html.Hr(),

    # inserindo um componente da biblioteca dash HTML components como título/cabeçalho do layout
    html.H1('Texto com html.H1',
    style={
        'color':'red'
    }),

    html.Hr(),

    # inserindo um componente interativo do pacote dash HTML components
    html.Button(
        'Botão teste',
        style={
            'width':'100px',
            'height':'30px'
        }
    ),

    html.Hr(),

    # construindo um quadro com funções da biblioteca dash HTML componentes
    html.Table([

        # título das colunas
        html.Tr([
            html.Th('1'),
            html.Th('2'),
            html.Th('3'),
            html.Th('4')
        ]),

        # dados da primeira linha
        html.Tr([
            html.Td('a11'),
            html.Td('a12'),
            html.Td('a13'),
            html.Td('a14')
        ]),

        # dados da segunda linha
        html.Tr([
            html.Td('a21'),
            html.Td('a22'),
            html.Td('a23'),
            html.Td('a24')
        ]),
    ]),

])

# servindo a aplicação em dash como versão para teste
if __name__ == '__main__':
    app.run_server(debug=True)