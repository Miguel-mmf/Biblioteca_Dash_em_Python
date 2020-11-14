# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#               Esse arquivo possui algumas modificações em relação ao arquivo apresentado no vídeo do YouTube
#                          Não deixe de assistir o vídeo e estudar pela documentação ofical Dash
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# importando as bibliotecas necessárias
import dash #1.17.0
import dash_core_components as dcc #1.13.0
import dash_html_components as html # 1.1.1

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

app.layout = html.Div(children=[

    # inserindo um componente da biblioteca dash HTML components como título/cabeçalho do layout                            
    html.H1(
        children='Apresentação da biblioteca Dash!',
        # o parâmetro style define estilos css para o componente
        # caso algum estilo já tenha sido definido, para esse componente o estilo será substituido pelo inserido com o parâmetro style
        style={'textAlign':'center'}
    ),

    # adicionando um novo texto ao layout, porém utilizando um html.Div ("caixa", explicarei no vídeo sobre a biblioteca dash HTML components)
    html.Div(children='''
        Dash: Aplicação na internet em Python.
    '''),


    # inserindo um gráfico com o a função Graph() do pacote dash core components
    dcc.Graph(
        # identidade/nome do componente
        id='example-graph',
        # o parâmetro figure carrega os dados (data, layout, frames) necessários para a construção do gráfico
        figure={
            'data':[

                # primeiro traço
                {
                    'x':[0,1,2,3,4,5,6],
                    'y':[0,1,2,3,4,5,6],
                    'type':'line+markers',
                    'name':'Reta'
                },

                # segundo traço
                {
                    'x':[0,1,2,3,4,5,6],
                    'y':[0,1,4,9,16,25,36],
                    'type':'line+markers',
                    'name':'Parábola'
                }
            ],
            'layout':{'title':'Gráfico (exemplo)'}
        }
    )
    
])

# servindo a aplicação em dash como versão para teste
if __name__ == '__main__':
    app.run_server(debug=True)