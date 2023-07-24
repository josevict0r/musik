# musik

PARA EXECUTAR O PROGRAMA:

- Primeiramente, é necessário ter o python instalado em seu computador
- No prompt de comando, vá até a pasta que possui o arquivo "manage.py"
- Uma vez dentro da pasta, é necessário criar um Virtual Environment (Ambiente Virtual), para isolar as modificações e instalações de Python/Django do projeto de outros arquivos e pastas do seu computador.
- Para criar o ambiente virtual digite o seguinte comando:
No Windows:
```sh
  python -m venv nome-do-ambiente-virtual
```
No Linux e OS X
```sh
  python3 -m venv nome-do-ambiente-virtual
```
>o ambiente virtual pode ter qualquer nome

- Depois disso, vamos ativar o seu ambiente virtual

No Windows:
```sh
  .\nome-do-ambiente-virtual\Scripts\activate
```
No Linux e OS X:
```sh
  source nome_do_ambiente_virtual/bin/activate
```
>caso surja "(nome_do_ambiente_virtual)" no começo da linha do seu terminal, o ambiente está ativado

Agora é preciso garantir que você tem o necessário para executar o arquivo
```sh
  pip install -r requirements.txt
```
Por fim, basta executar estes dois comandos em sequência:
```sh
  py manage.py migrate
```
```sh
  py manage.py runserver
```
Agora é só ir no seu navegador e digitar:
```sh
  http://localhost:8000/
```
# Sobre o projeto

  Para essa tarefa, optei por desenvolver um site que exibe uma lista de Cantores/Bandas em que ao clicar em um dos ícones, exibe uma tela com algumas músicas do respectivo artista e ao escolher uma das músicas, a letra da respectiva música é exibida. Um dos motivos para a escolha dessa temática, foi o fato de que as letras das músicas já estavam disponíveis facilmente na internet, o que facilitou a pesquisa e montagem do banco de dados do projeto. Ao todo, são 3 telas: a de artistas, a de músicas e a da letra da música.  
  O projeto foi realizado com a utilização de Django4, um framework de Python para desenvolvimento web. Além disso, para o front-end foram utilizados HTML5 e CSS3, bem como, o framework Bootstrap.   
