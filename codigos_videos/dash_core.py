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

app_dash_core_components = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

# criando um layout para a variável app
# adicionando ao layout um componente html.Div que irá conter os demais componentes que dão forma 
app_dash_core_components.layout = html.Div([

    # inserindo um componente da biblioteca dash HTML components como título/cabeçalho do layout 
    html.H1('Dash Core Components',style={'textAlign':'center','font-weight':'bold'}),

    html.Div([

            # inserindo uma linha horizontal no layout
            html.Hr(),

            # inserindo um componente da biblioteca dash HTML components como título/cabeçalho do layout
            html.H2(
                ['Componente Dropdown']
            ),

            # inserindo um componente interativo do pacote dash core components
            dcc.Dropdown(

                # inserindo as opções do dropdown, processo que pode ser feito utilizando uma estrutura de repetição ou múltiplos dicionários
                options=[
                    {
                        'label': f'Opção {value}', 'value': f'{value}'
                    }
                    for value in range(0,10)
                ],
                value='1'
            ),

            html.Hr(),
            html.H2(
                ['Componente Slider']
            ),
    
            dcc.Slider(
                min=-5,
                max=10,
                step=0.5,
                value=-3
            ),

            html.Hr(),
            html.H2(
                ['Componente RangeSlider']
            ),

            dcc.RangeSlider(
                count=1,
                min=-5,
                max=10,
                step=0.5,
                value=[-3, 7]
            ),

            html.Hr(),
            html.H2(
                ['Componente Input']
            ),

            dcc.Input(
                placeholder='Insira uma mensagem...',
                type='text',
                value=''
            ),
            
            html.Hr(),
            html.H2(
                ['Componente Link']
            ),

            # esse componente é utilizado para inserir endereços de outras páginas da sua aplicação
            dcc.Link(),

        ],
        style={
            'margin-left':'10px',
            'margin-right':'10px',
            'width': '48%',
            'display':'inline-block',
            'float':'left',
            'border': '2px solid lightblue'
            }
    ),

    html.Div([

            # inserindo uma linha horizontal no layout
            html.Hr(),

            # inserindo um componente da biblioteca dash HTML components como título/cabeçalho do layout
            html.H2(
                ['Componente Checklist']
            ),

            # inserindo um componente interativo do pacote dash core components
            dcc.Checklist(

                # inserido as opções do dropdown, processo que pode ser feito utilizando uma estrutura de repetição ou múltiplos dicionários
                options=[
                    {
                        'label': f'Opção {value}', 'value': f'{value}'
                    }
                for value in range(1,6)
                ],
                value=['1', '9']
            ),

            html.Hr(),
            html.H2(
                ['Componente RadioItems']
            ),

            # inserindo um componente interativo do pacote dash core components
            dcc.RadioItems(

                # inserido as opções do dropdown, processo que pode ser feito utilizando uma estrutura de repetição ou múltiplos dicionários
                options=[
                    {
                        'label': f'Opção {value}', 'value': f'{value}'
                    }
                    for value in range(1,6)
                ],
                value='MTL'
            ),

            # inserindo uma linha horizontal no layout
            html.Hr(),

            # inserindo um componente da biblioteca dash HTML components como título/cabeçalho do layout
            html.H2(
                ['Componente Graph']
            ),

            # inserindo um gráfico com o a função Graph() do pacote dash core components
            dcc.Graph(
                # identidade/nome do componente
                id='example-graph',
                figure={
                    'data':[
                        # primeiro traço
                        {'x':[0,1,2,3,4,5,6],'y':[0,1,2,3,4,5,6],'type':'line+markers','name':'Reta'},
                        # segundo traço
                        {'x':[0,1,2,3,4,5,6],'y':[0,1,4,9,16,25,36],'type':'line+markers','name':'Parábola'}
                    ],
                    'layout':{
                        'title':'Gráfico Exemplo'
                    }
                }
            ),
        ],
        # o parâmetro style define estilos css para o componente
        style={
            'margin-left':'10px',
            'margin-right':'10px',
            'width': '48%',
            'display':'inline-block',
            'float':'right',
            'border': '2px solid lightblue'
            }
    )

    ],
    style={
        'margin-left':'10px',
        'margin-right':'10px',
        'border': '2px solid lightblue'
    }
)

# servindo a aplicação em dash como versão para teste
if __name__ == "__main__":
    app_dash_core_components.run_server(debug=True)