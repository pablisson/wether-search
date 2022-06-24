
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
   * [Como executar o projeto](#-como-executar-o-projeto)
   * [Tecnologias](#-tecnologias)
     * [WebSite](#user-content-website--react----typescript)
     * [Server](#user-content-server--nodejs----typescript)
     * [Pré-requisitos](#pré-requisitos)
     * [Rodando o Backend (servidor)](#user-content--rodando-o-backend-servidor)
     * [Rodando a aplicação web (Frontend)](#user-content--rodando-a-aplicação-web-frontend)
   * [Autor](#-autor)

<!--te-->


## 💻 Sobre o projeto

🌦️ Weather search - é uma plataforma que tem por objetivo mostrar o clima dos cinco próximos dias da cidade. A estrutura do projeto é composta por um webservice desenvolvido em python e um frontend desenvolvido em ReactJs.


---

## ⚙️ Funcionalidades

- [x] O Usuário busca o clima dos ulmos 5 dias da cidade desejada:
  - [x] O usuário poderá visualizar o clima dos próximos 5 dias
  - [x] Os dados meterológicos poderão serem salvos na base de dados utilizando o botão salvar
  - [x] Os dados serão visualizados no frontend


---

## 🛫 Funcionalidades e estruturas futuras

- [x] Fazer um refactory no código. Um dos pontos a serem melhorados são as 3 classes responsáveis por pegar os dados da página web e gerar um arquivo json. É possível Aplicar um padrão de projeto no qual deixe a classe mais flexivel podendo gerar o arquivo não somente em json mas também em xml ou alguma outra estrutura.
- [x] Gerar um nova tela com o histórico das temperaturas já salvas.
- [x] entrar em contato com a entidade através do E-mail ou do WhatsApp



---

## 🚀 Como executar o projeto

Este projeto é divido em duas partes:
1. Backend (pasta server) 
2. Frontend (pasta web))

💡Python é uma linguagem de programação utilizadas para criar estruturas backend.
💡O React é uma biblioteca escrita en javaScript que ao conectar com outras bibliotecas pode controlar as interfaces de usuário.
💡O Frontend precisa que o Backend esteja sendo executado para para buscar os dados de temperatura.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Node.js](https://nodejs.org/en/) e o [python](https://www.python.org/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

#### 🎲 Rodando o Backend (servidor)

```bash

# Clone este repositório
$ git clone git@github.com:pablisson/wether-search.git

# Acesse a pasta do projeto no terminal/powershell
$ cd README-ecoleta

# Vá para a pasta server
$ cd server

# Instale as dependências
$ npm install

# Execute a aplicação em modo de desenvolvimento
$ npm run dev:server

# O servidor inciará na porta:3333 - acesse http://localhost:3333 

```
<p align="center">
  <a href="https://github.com/tgmarinho/README-ecoleta/blob/master/Insomnia_API_Ecoletajson.json" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>
</p>


#### 🧭 Rodando a aplicação web (Frontend)

```bash

# Clone este repositório
$ git clone git@github.com:tgmarinho/README-ecoleta.git

# Acesse a pasta do projeto no seu terminal/cmd
$ cd README-ecoleta

# Vá para a pasta da aplicação Front End
$ cd web

# Instale as dependências
$ npm install

# Execute a aplicação em modo de desenvolvimento
$ npm run start

# A aplicação será aberta na porta:3000 - acesse http://localhost:3000

```

---

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:
No frontend utilizamos, além do Reac, React dom e React Plugin utilizamos o vite que é utilizado para substituir o web pack e o babel, fazendo com que os navegadores entendam a última versão dos scripts utilizados além de entender importações entre arquivos javaScript

#### **Website**  ([React](https://reactjs.org/)  +  [Vite](https://vitejs.dev/guide/))

-   **[Vite](https://vitejs.dev/guide/#trying-vite-online)**
-   **[Cors](https://www.npmjs.com/package/cors)**
-   **[Axios](https://github.com/axios/axios)**
-   **[Leaflet](https://www.npmjs.com/package/cors)**
-   **[React Leaflet](https://react-leaflet.js.org/)**
-   **[React Dropzone](https://github.com/react-dropzone/react-dropzone)**

> Veja o arquivo  [package.json](https://github.com/tgmarinho/README-ecoleta/blob/master/web/package.json)

#### [](https://github.com/tgmarinho/Ecoleta#server-nodejs--typescript)**Server**  ([NodeJS](https://nodejs.org/en/)  +  [TypeScript](https://www.typescriptlang.org/))

-   **[Express](https://expressjs.com/)**
-   **[CORS](https://expressjs.com/en/resources/middleware/cors.html)**
-   **[KnexJS](http://knexjs.org/)**
-   **[SQLite](https://github.com/mapbox/node-sqlite3)**
-   **[ts-node](https://github.com/TypeStrong/ts-node)**
-   **[dotENV](https://github.com/motdotla/dotenv)**
-   **[Multer](https://github.com/expressjs/multer)**
-   **[Celebrate](https://github.com/arb/celebrate)**
-   **[Joi](https://github.com/hapijs/joi)**

> Veja o arquivo  [package.json](https://github.com/tgmarinho/README-ecoleta/blob/master/server/package.json)

#### [](https://github.com/tgmarinho/Ecoleta#mobile-react-native--typescript)**Mobile**  ([React Native](http://www.reactnative.com/)  +  [TypeScript](https://www.typescriptlang.org/))

-   **[Expo](https://expo.io/)**
-   **[Expo Google Fonts](https://github.com/expo/google-fonts)**
-   **[React Navigation](https://reactnavigation.org/)**
-   **[React Native Maps](https://github.com/react-native-community/react-native-maps)**
-   **[Expo Constants](https://docs.expo.io/versions/latest/sdk/constants/)**
-   **[React Native SVG](https://github.com/react-native-community/react-native-svg)**
-   **[Axios](https://github.com/axios/axios)**
-   **[Expo Location](https://docs.expo.io/versions/latest/sdk/location/)**
-   **[Expo Mail Composer](https://docs.expo.io/versions/latest/sdk/mail-composer/)**

> Veja o arquivo  [package.json](https://github.com/tgmarinho/README-ecoleta/blob/master/mobile/package.json)

#### [](https://github.com/tgmarinho/Ecoleta#utilit%C3%A1rios)**Utilitários**

-   Terminal: WSL - Subsistema ubuntu no windows, Power Shell
-   Editor:  **[Visual Studio Code](https://code.visualstudio.com/)**  
-   Administração de banco de dados: Dbeaver - Sistema de gerenciamento de vários banco de dado distintos
-   Teste de API:  **[Insomnia](https://insomnia.rest/)**


---

## 🦸 Autor


 <img style="border-radius: 50%;" src="https://media-exp1.licdn.com/dms/image/C4D03AQFICWmbaQJtJw/profile-displayphoto-shrink_200_200/0/1516768728498?e=2147483647&v=beta&t=GtFjq-GOh1stWfxZZEc5ICR8yvwXfxelw58E8pX1H10" width="100px;" alt=""/>
 <br />
 <sub><b>Páblisson Araújo</b></sub> 🚀
 <br />

<a href="www.linkedin.com/in/páblisson-araujo">linkedin</a>


---

