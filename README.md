# Autofollow
#### Robô seguidor automático para Instagram baseado em lista de usuários

## Como funciona ?

### BOT1
Usa a urllib (biblioteca do python) para capturar o source das paginas das tags (que estão no arquivo tags.txt), trata o source para encontrar os ID's dos usuários e por fim utiliza a biblioteca instaloader para transformar os ID's em nomes de usuário (sem API do Instagram), depois salva os nomes dos usuários no arquivo 'users.txt'.

### BOT2
Usa a biblioteca Selenium junto com o Chromedriver para logar, entrar na página do usuário e seguir. Como todo o processo automatizado é feito pelo Selenium, sem usar nenhuma biblioteca para manipular o mouse ou teclado, o navegador pode rodar minimizado ou em segundo plano.

## Como utilizar ?

### BOT1
Basta editar o arquivo 'tags.txt' e executar o bot usando o python, normalmente, sem nenhum argumento.

### BOT2
Execute o script do bot usando o python com dois argumentos: -u (usuário) e -p (senha).
