# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#               Esse arquivo possui algumas modificações em relação ao arquivo apresentado no vídeo do YouTube
#                          Não deixe de assistir o vídeo e estudar pela documentação ofical Dash
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# importando as bibliotecas necessárias
import dash #1.17.0
import dash_table #4.11.0
import dash_core_components as dcc #1.13.0
import dash_html_components as html # 1.1.1
from dash.dependencies import Input, Output

# importando a biblioteca pandas que é indispensável e que fornece ferramentas para análise de dados
import pandas as pd #1.1.4

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#            Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# essa função está gerando a planilha com os dados utilizando componentes dash DataTable
def gera_tabela(df):

    return dash_table.DataTable(

            # dados
            data = df.to_dict('records'),

            # colunas
            columns = [
                {
                    'name': col, 
                    'id': col,
                } 
                for col in df.columns
            ], 
            
            style_cell={
                'textAlign': 'center',
                'border': '1px solid grey',
                'minWidth':'90px',
                'width':'125px',
                'maxWidth':'160px',
                'fontSize':'14',
                'font-family':'sans-serif'
                },
                
            style_header={
                'backgroundColor': '#8FBC8F',
                'fontWeight': 'bold'
            },

            page_size = 16,

            style_table = {
                'height':'auto',
                'minWidth': '100%',
                'overflowX': 'auto',
                'border': '2px solid lightgreen',
            }
        )

# essa função está renomeando as colunas de um dataframe pelos nomes presentes na lista
def gera_dados_selec(df):
    list_colunas = [
        'Tempo','Precipitação Média','Umidade a 2m','Umidade Relativa a 2m (%)','Pressão na Superfície (kPa)',
        'Média das Temp. a 2m (°C)','Média das Temp. Mínimas a 2m (°C)','Média das Temp. Máximas a 2m (°C)',
        'Média das Vel. Mínimas do Vento a 50m (m/s)','Média das Vel. Mínimas do Vento a 10m (m/s)',
        'Média das Vel. Máximas do Vento a 50m (m/s)','Média das Vel. Máximas do Vento a 10m (m/s)',
        'Média das Vel. do Vento a 50m (m/s)','Média das Vel. do Vento a 10m (m/s)','Temp. Máxima a 2m (°C)',
        'Média das Vel. do Vento a 50m (m/s)','Vel. Máxima do Vento a 10m (m/s)','Temp. Mínima a 2m (°C)',
         'Vel. Mínima do Vento a 50m (m/s)','Vel. Mínima do Vento a 10m (m/s)','Precipitação Acumulada'
    ]
    df.columns = map(lambda x: x.title(),list_colunas)

    return df

# criando o cabeçalho para facilitar na construção do layout
def div_topo():
    return html.Div(children=[

                html.H2('Informações da Cidade de Sousa-PB', style={'font-weight':'bold',}),

                html.H4('Dados de 1983 até 2018')
                ],
                style={
                    'textAlign':'center',
                    'font-weight':'bold',
                    'border': '2px solid lightgreen',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)',
                    'background-color':'#8FBC8F',
                    }
            )

# criando o rodapé para facilitar na construção do layout
def div_base():
    return html.Div(children=[
                dcc.Markdown(''' ### **Sousa, Paraíba - 2020**'''),

                dcc.Markdown('''#### Site: [Cidade Sousa](https://www.sousa.pb.gov.br/)''')

                ],
                style={
                    'textAlign':'center',
                    'font-weight':'bold',
                    'border': '2px solid lightgreen',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)',
                    'background-color':'#8FBC8F',
                    }
            )

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# adicionando um estilo externo através do link abaixo
    # esse link é o recomendado pela documentação da biblioteca Dash e ao acessar esse link no seu navegador,
    # você perceberá que ele possui a estrutura de um arquivo CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# criando a aplicação por meio da função Dash do pacote dash e atribuindo a variável app
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

# lendo um aquivo .csv com a função read_csv da biblioteca pandas
df = gera_dados_selec(pd.read_csv('sousa_geral_anual.csv'))

# podemos fazer da seguinte forma:
    # df = pd.read_csv('mensal_bi_tri_se_an_sousa_geral.csv')
    # modificando o nome das colunas
    # df = gera_dados_selec(df)


# Armazenando as colunas do dataframe na variável coluna
colunas = list(df.columns)

# criando um layout para a variável app
# adicionando ao layout um componente html.Div que irá conter os demais componentes que dão forma
app.layout = html.Div([

    # inserindo o cabeçalho
    div_topo(),

    # inserindo uma frase acima da dropdown
    html.H4(
        ['Selecione os Dados:'],style={'textAlign':'justify','text-indent': '50px','line-height': '3'}
    ),

    # parte central do layout
    html.Div([

        # bloco esquerdo da parte central do layout
        html.Div([

            # Criando a componente drowpdown contendo a lista com as colunas de df
            dcc.Dropdown(
                # nome do componente
                id='columns',
                # lista de opções
                options=[
                    {
                        'label': i,
                        'value': i
                    }
                    for i in colunas[1:]
                ],
                value='Precipitação Média'
            ),

            # adicionando uma linha horizontal no layout
            html.Hr(),

            # inserindo um gráfico com o a função Graph() do pacote dash core components
            dcc.Graph(
                id='indicator-graphic',
                style={'border': '2px solid lightgreen','background-color':'#ADD8E6'}
            ),
        ],
        style={'margin-left': '15px','width':'48%', 'display':'inline-block'}
        ),

        # bloco direito da parte central do layout
        html.Div([

            gera_tabela(df),
            
        ],
        style={'margin-right': '15px','width':'48%', 'float': 'right', 'display':'inline-block'}
        )
    ]),

    html.Hr(),

    # inserindo o rodapé
    div_base()

    ],

    # inserindo um estilo ao redor de toda a página
    style={
        'border': '2px solid lightgreen'
        ,'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
        ,'background-color':'#90EE90'
    }
)


# Callback

@app.callback(
    # parâmetro de saída que irá ser modificado quando a função update_graph() for chamada
    Output('indicator-graphic','figure'),
    [
        # parâmetro modificador (dropdown com as colunas)
        Input('columns','value'),
    ]
)
def update_graph(coluna):

    # teste para verificar se o dataframe foi gerado perfeitamente
    print(df.head())

    # retorno da função update_graph()
    return{
        # dados (uma chave contendum dicionário com informações do gráfico)
        'data':[
            dict(
                x=df['Tempo'],
                y=df[str(coluna)],
                mode='lines+markers',
                text=str(coluna),
                opacity=0.8
            )
        ],
        'layout': dict(
            # modificando o eixo x do gráfico
            xaxis={
                'title':'Anual',
                'type':'date',
                'rangeslider': 'dict(visible=True)'
            },
            # modificando o eixo y do gráfico
            yaxis={
                'title':coluna,
                'type':'linear'
            },
            # modificando as margens e legendas do gráfico
            margin={'l': 100, 'b': 40, 't': 40, 'r': 100},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }

# servindo a aplicação em dash como versão para teste
if __name__ == '__main__':
    app.run_server(debug=True)