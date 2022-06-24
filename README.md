
<h1 align="center">
     🌦️ <a href="#" alt="app weather search"> Weather search </a>
</h1>

<h3 align="center">
    O clima da sua cidade na semana.  
</h3>



<h4 align="center">
	🚧   Em Evolução ... 🚀 🚧
</h4>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#-sobre-o-projeto)
   * [Funcionalidades](#-funcionalidades)
   * [Funcionalidades e estruturas futuras](#-funcionalidades-e-estruturas-futuras)
   * [Tecnologias](#-tecnologias)
     * [Pré-requisitos](#pré-requisitos)
     * [WebSite](#user-content-website--react----typescript)
     * [Server](#user-content-server--nodejs----typescript)   
   * [Como executar o projeto](#-como-executar-o-projeto)     
     * [Rodando o Backend (servidor)](#user-content--rodando-o-backend-servidor)
     * [Rodando a aplicação web (Frontend)](#user-content--rodando-a-aplicação-web-frontend)
   * [Desafios Superados](#-desafios-superados)
   * [Autor](#-autor)

<!--te-->


## 💻 Sobre o projeto

🌦️ Weather search - é uma plataforma que tem por objetivo mostrar o clima dos cinco próximos dias da cidade. A estrutura do projeto é composta por um webservice desenvolvido em Python e um frontend desenvolvido em ReactJs.


---

## ⚙️ Funcionalidades

- [x] O Usuário busca o clima dos ulmos 5 dias da cidade desejada:
  - [x] O usuário poderá visualizar o clima dos próximos 5 dias
  - [x] Os dados meterológicos poderão serem salvos na base de dados utilizando o botão salvar
  - [x] Os dados serão visualizados no frontend


---

## 🛫 Funcionalidades e estruturas futuras

- [ ] Fazer um refactory no código. Um dos pontos a serem melhorados são as 3 classes responsáveis por pegar os dados da página web e gerar um arquivo json. É possível Aplicar um padrão de projeto no qual deixe a classe mais flexivel podendo gerar o arquivo não somente em json mas também em xml ou alguma outra estrutura.
- [ ] Dividir as informações em modelos distintos e estabelecer um relacionamento com os mesmos
- [ ] Gerar um nova tela com o histórico das temperaturas já salvas.
- [ ] Gerar um gráfico com as variações da temperatura
- [ ] Gerar mais segurança na aplicação encapsular o token utilizando na api para buscar os dados da temperatura

---

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:
No frontend utilizamos, além do Reac, React dom e React Plugin utilizamos o vite que é utilizado para substituir o web pack e o babel, fazendo com que os navegadores entendam a última versão dos scripts utilizados além de entender importações entre arquivos javaScript. Com vite algumas coisas já vem configuradas como o fast refresh, que alterará a nossa aplicação visual no momento em que o novo código for salvo.

No backend utilizamos Python com Django Rest Framework. O Django é uma biblioteca escrita em Python para criar sistemas web. O Django agrupa muitas bibliotecas e funcionalidades que agilizam o desenvolvimento e se integra no projeto.
### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Node.js](https://nodejs.org/en/) e o [python](https://www.python.org/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

#### **Website**  ([React](https://reactjs.org/)  +  [Vite](https://vitejs.dev/guide/))

A Instalação do frontend seguiu os seguintes passos
```bash

# Crie um projeto react utilizando o vit
# Ao executar o comando abaixo será solicitado as seguintes opções: 
# 1 - "Project name", escolha o nome do projeto desejado
# 2 - "Select a framework", escolha react
# 3 - "Select a varian", escolha react (a opção sem typeScript)
$ npm create vite@latest

# Instalar as dependências. Aqui será intalado o axios
$ npm install

# Execute a aplicação em modo de desenvolvimento
$ npm run dev

# A aplicação será aberta na porta:3000 - acesse http://localhost:3000

```
-   **[Vite](https://vitejs.dev/guide/#trying-vite-online)**
-   **[Axios](https://github.com/axios/axios)**

> Veja o arquivo   [package.json](https://github.com/pablisson/wether-search/blob/main/frontend/weather-front/package.json)

#### **Backend / Server**  ([Python](https://www.python.org/)  +  [Django REST framework](https://www.django-rest-framework.org/)

A Instalação do backend seguiu os seguintes passos

```bash

# Crie uma virtual env
# O comando abaixo cria o ambiente virtual, algo parecido com um node modules 
$ npm python -m venv ./venv	

# Para ativar a venv no windows digite o comando abaixo 
$venv/Scripts/activate.bat

# Instalar as dependências. O pip é semelhante ao npm
$ pip install django

# Com o comando abaixo é possível ver as dependências utilizadas no projeto
$ pip freeze

# Para criar a aplicação será executado o comando abaixo
# O config é opcional, apenas por questão organização para deixar tudo relacionado às configurações do projeto
$ django-admin startproject config

# Para subir o servidor basta executar esse comando
$ python manage.py runserver

# A aplicação será aberta na porta:8000 - acesse http://localhost:8000

```

-   **[Python](https://expressjs.com/)**
-   **[Django](https://expressjs.com/en/resources/middleware/cors.html)**
-   **[DjangoRestFramework](https://www.django-rest-framework.org/)**
-   **[jsonpath]**
-   **[SQLite]()**


> Veja o arquivo [package.json](https://github.com/pablisson/wether-search/blob/main/config/settings.py)

---

## 🚀 Como executar o projeto

Este projeto é divido em duas partes:
1. Backend (pasta server) 
2. Frontend (pasta web))

💡Python é uma linguagem de programação utilizadas para criar estruturas backend.
💡O React é uma biblioteca escrita en javaScript que ao conectar com outras bibliotecas pode controlar as interfaces de usuário.
💡O Frontend precisa que o Backend esteja sendo executado para para buscar os dados de temperatura.


#### 🎲 Rodando o Backend (servidor)

```bash

# Clone este repositório
$ git clone git@github.com:pablisson/wether-search.git

# Acesse a pasta do projeto no terminal/powershell
# Vá para a pasta server
$ cd web-service

# Execute o comando para subir o servidor
$ python manage.py runserver

# Instale as dependências
$ npm install

# Execute a aplicação em modo de desenvolvimento
$ npm run dev:server

# O servidor inciará na porta:3333 - acesse http://localhost:3333 

```


#### 🧭 Rodando a aplicação web (Frontend)

```bash
# Uma vez que os dois projetos então dentro do mesmo repositório 
# basta ir para a pasta da aplicação Front End
$ cd frontend\weather-front\

# Instale as dependências
$ npm install

# Instale o axios
$ npm install axios

# Instale o cors
$ npm install cors

# Execute a aplicação em modo de desenvolvimento
$ npm run dev


# A aplicação será aberta na porta:3000 - acesse http://localhost:3000

```

---



#### [](https://github.com/tgmarinho/Ecoleta#utilit%C3%A1rios)**Utilitários**

-   Terminal: WSL - Subsistema ubuntu no windows, Power Shell
-   Editor:  **[Visual Studio Code](https://code.visualstudio.com/)**  
-   Administração de banco de dados: Dbeaver - Sistema de gerenciamento de vários banco de dado distintos
-   Teste de API:  **[Insomnia](https://insomnia.rest/)**


---

## 🤹🏻‍♀️ Desafios Superados
No inicio do projeto não possuia nenhum conhecimento em Python e pouco conhecimento em react. Foi uma grande experiência e superação poder fazer essa aplicação e aprensentá-a. Gerou em mim um desejo de avançar na mesma, fazendo os ajustes necessários e aumentando a complexidade


## 🦸 Autor


 <img style="border-radius: 50%;" src="https://media-exp1.licdn.com/dms/image/C4D03AQFICWmbaQJtJw/profile-displayphoto-shrink_200_200/0/1516768728498?e=2147483647&v=beta&t=GtFjq-GOh1stWfxZZEc5ICR8yvwXfxelw58E8pX1H10" width="100px;" alt=""/>
 <br />
 <sub><b>Páblisson Araújo</b></sub> 🚀
 <br />

<a href="www.linkedin.com/in/páblisson-araujo">linkedin</a>


---

