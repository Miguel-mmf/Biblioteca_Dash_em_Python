# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#               Esse arquivo possui algumas modificações em relação ao arquivo apresentado no vídeo do YouTube
#                          Não deixe de assistir o vídeo e estudar pela documentação ofical Dash
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# importando as bibliotecas necessárias
import dash #1.17.0
import dash_core_components as dcc #1.12.1
import dash_html_components as html # 1.1.1

import dash_table #4.11.0

# importando a biblioteca pandas que é indispensável e que fornece ferramentas para análise de dados
import pandas as pd #1.1.4

# lendo um aquivo .csv com a função read_csv da biblioteca pandas
df = pd.read_csv('sousa_geral_anual.csv')

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
df = pd.read_csv('mensal_bi_tri_se_an_sousa_geral.csv')


# criando um layout para a variável app
# adicionando ao layout um componente html.Div que irá conter os demais componentes que dão forma
app.layout = html.Div([

    # inserindo um componente da biblioteca dash HTML components como título/cabeçalho da tabela 
    html.H1('Tabela de dados da cidade de Sousa - PB'),

    # gerando a tabela de dados com a função DataTable() da biblioteca Dash Table
    dash_table.DataTable(

        # dados
        data= df.to_dict('records'),

        # identificação das colunas da planilha
        columns=[
            {
                'name': col,
                'id': col
            }
            for col in df.columns
        ],

    )
])


# servindo a aplicação em dash como versão para teste
if __name__ == '__main__':
    app.run_server(debug=True)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#            Outra forma de gerar uma tabela, sem a utilização da biblioteca Dash Table
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# essa função está gerando a planilha com os dados utilizando componentes da biblioteca dash HTML components
def gera_planilha(dataframe): 

    return html.Table([
        
        # colunas
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),

        # dados
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(len(dataframe))
        ])
    ])