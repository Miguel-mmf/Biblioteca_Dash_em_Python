<h1 align="center"> Introdução a Biblioteca Dash em Python</h1>

O objetivo deste material é introduzir e servir como guia rápido para a utilização da biblioteca Dash em Python. Dessa forma, esse material teve como base para a sua construção a documentação para utilização desse _framework_ disponível na internet.

Acesse a site [Dash](https://plotly.com/dash/).

Acesse a documentação completa clicando [aqui](https://dash.plotly.com/introduction).

## **Vídeos sobre a Biblioteca Dash em Python no YouTube**

Esses vídeos foram produzidos com o intuito de auxiliar aqueles que têm interesse em programar em Python e, mais especificamente, utilizar a biblioteca Dash para a construção de aplicações na internet destinadas a visualização e apresentação de dados.

**Assista aos vídeos:**

| 1º Vídeo | 2º Vídeo | 3º Vídeo | 4º Vídeo |
| :---: | :---: | :---: | :---: |
[<img src="introducao.jpg" > <br> <sub> Introdução a Biblioteca Dash </sub>](https://youtu.be/CjhlN4UZc3I) | [<img src="layout.jpg" > <br> <sub> Layout com a Biblioteca Dash </sub>](https://youtu.be/S3xXAKBicPE) | [<img src="page_dash.jpg" > <br> <sub> Exemplo de Página com a Biblioteca Dash </sub>](https://youtu.be/dRgoPuUeQMs) | [<img src="callbacks.jpg" > <br> <sub> CallBacks com a Biblioteca Dash </sub>](https://youtu.be/Xff2GEpcawQ) |
| 5º Vídeo | 6º Vídeo | 7º Vídeo | 8º Vídeo |
[<img src="core_components.jpg" > <br> <sub> Biblioteca Dash Core Components </sub>](https://youtu.be/q_83OeJNv2k) | [<img src="html_components.jpg" > <br> <sub> Biblioteca Dash HTML Components </sub>](https://youtu.be/N49IHkvV9qU) | [<img src="dash_datatable.jpg" > <br> <sub> Biblioteca Dash Table </sub>](https://youtu.be/-6HRKsD36qQ) | [<img src="mini_dashboard.jpg" > <br> <sub> Mini Dashboard com Dash em Python </sub>](https://youtu.be/5mJvsZa6h5s)

**Os exemplos utilizados nos vídeos estão dentro da pasta codigo_videos.**

**Obs.:** _Mesmo com algumas dificuldades, gravei esse material para repassar um pouco do que aprendi ao longo dos meses de junho, julho e agosto de 2020, em que trabalhei com a biblioteca Dash em Python._

## Sumário

* ### [Instalação](#Instalação)
    * ### [Pacotes Instalados Automaticamente](#pacotes)
    * ### [Versões dos Pacotes](#versoes)
    * ### [Instalação da Biblioteca Dash](#installdash)
    * ### [Verificação da Versão Instalada](#versaoinstalada)
        * #### [Interpretador Python](#interpython)
        * #### [Pip Freeze ou Pip List](#piplist)
* ### [Links de Apoio](#links)


### **Instalação**

* Para o processo de instalação é necessário que você tenha o Python 3.8 instalado em sua máquina e que siga os passos abaixo.


### **Pacotes Instalados Automaticamente** <a name="pacotes"></a>

* Dash automaticamente instala os seguintes pacotes:
    > `dash-renderer`

    > `dash-core-components`

    > `dash-html-components`

    > `dash-table`

    > `plotly` - _caso você não tenha instalado_


### **Versão dos Pacotes Instalados** <a name="versoes"></a>

* As versões abaixo estão atualizadas de acordo com a atualização em 25 de setembro de 2020.

| Dash | Dash Renderer | Dash Core Components | Dash HTML Components | Dash Table | Plotly |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.16.2 | 1.8.2 | 1.12.1 | 1.1.1 | 4.10.1 | 4.9.0 |


### **Instalando a Biblioteca Dash** <a name="installdash"></a>

* Com o seu terminal/prompt de comando aberto, escreva o seguinte código para instalação:
    > `pip install dash==1.16.2`

**Obs.:** _Caso você não especifique a versão que deseja instalar, utilizando o `pip`, pode ser que esse gerenciador de pacotes instale uma versão diferente na sua máquina, ocasionando, assim, problemas para desenvolver alguma aplicação._


### **Verificação da Versão Instalada** <a name="versãoinstalada"></a>

* Para verificar a versão de um pacote, você tem as duas opções abaixo.


#### **Utilizando o Interpretador Python** <a name="interpython"></a>

* Com o interpretador Python ativado no seu prompt de comando (para ativar é necessário somente escrever `python`), faça:
    > `import [nome do pacote]`
    >
    > `print([nome do pacote].__version__)`


#### **Utilizando `pip`** <a name="piplist"></a>

* Outra opção é utilizar o comando:

    > `pip freeze` => _esse método irá te apresentar todos os pacotes existentes em sua máquina, porém  sem a versão desses._

    > `pip list` => _esse comando irá retornar uma lista com todos os pacotes existentes em sua máquina e com suas respectivas versões._

**Obs.:** _Sugiro que faça isso para conferir a versão de cada pacote e caso algum esteja desatualizado, atualize com:_
> `pip install [nome do pacote]==[versão]`


## **Links de Apoio** <a name="links"></a>

* [Site Oficial Dash](https://plotly.com/dash/)
* [Documentação Oficial Dash](https://dash.plotly.com/introduction)
    * [Layout](https://dash.plotly.com/layout)
    * [Basic CallBacks](https://dash.plotly.com/basic-callbacks)
    * [Dash Dev Tools](https://dash.plotly.com/devtools)
    * [Multi-Page Apps](https://dash.plotly.com/urls)
    * [Overview Dash Core Components](https://dash.plotly.com/dash-core-components)
    * [Overview Dash HTML Components](https://dash.plotly.com/dash-html-components)
    * [Dash DataTable](https://dash.plotly.com/datatable)
        * [Dash DataTable - Styling](https://dash.plotly.com/datatable/style).
        * [Dash DataTable - Interactivity](https://dash.plotly.com/datatable/interactivity).
        * [Editable DataTable](https://dash.plotly.com/datatable/editable).
* [Introducing JupyterDash](https://medium.com/plotly/introducing-jupyterdash-811f1f57c02e)

<hr></hr>

<img src="rodape_no_github.jpg" align='center'>


# Bons estudos!