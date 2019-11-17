# ClearBot

[![Python Version](https://img.shields.io/badge/python-%E2%89%A53.5.3-yellow.svg)](https://www.python.org/downloads/)

------

O ``ClearBot`` é um robô que detecta e remove spam dos comentários dos mapas do jogo ``KoGaMa``.

------


# Instalação:
Para instalar a última versão do ClearBot, basta clicar [aqui](https://github.com/ars3ne/clearbot/releases/latest) e seguir os próximos passos.

### Dependências:
Para executar o ClearBot, você precisará instalar os seguintes itens:
* Python 3.5.3 ou superior (Para baixar-lo, clique [aqui](https://www.python.org/downloads/).)
* ``kogama.py`` (Veja abaixo)
* ``requests`` (Veja abaixo)
* ``beautifulsoup4`` (Veja abaixo)
* ``lxml`` (Veja abaixo)

Depois de instalar o Python, para instalar as outras dependências, basta instalar o ``kogama.py``. Para instalar-lo, abra um Prompt de Comando ou Terminal e execute o comando abaixo:
```
pip install kogama.py
```

As outras dependências devem ser baixadas automáticamente após baixar o ``kogama.py``.

### Configurações
------
Depois de baixar o ClearBot e as suas dependências, abra o arquivo ``config.json``. Lá terá várias configurações. A maioria você não precisará mexer, porém eu recomendo que de uma lida em todas.

```javascript
{
    // Configurações de Autenticação
    "server": "br", // Coloque aqui o seu serivdor.
    "username": "username", // Coloque aqui o seu usuário. 
    "password": "password", // Coloque aqui a sua senha.
    // Configurações do ClearBot
    "check_comments": 10, // Quantos comentários o ClearBot deve verificar por mapa. O padrão é 10, porém é recomendado que você coloque um valor mais alto.
    "acceptable_emotes": 10, // O limite de emotes que um comentário pode ter. Se ele tiver mais do que esse limite, o comentário é deletado. Padrão: 10 
    "comments_limit": 5, // O limite de comentários que um usuário pode mandar em seguida. Se ele passar do limite, todos os comentários serão deletados. Padrão: 5
    "auto_add": false, // Não recomendado se estiver executando o ClearBot na sua conta. Aceita todos os pedidos de amizade automaticamente, e depois os deleta em 5 minutos. Padrão: false
    "auto_join": false, // Não recomendado se estiver executando o ClearBot na sua conta. Aceite todos os convites para projetos automaticamente. Padrão: False
    "debug_map": 0 // Não é recomendado mexer. Coloque aqui o ID de um mapa para ser o mapa de debug. Padrão: 0
}
```
Porém, existem três configurações que você precisa mudar. Elas são as três primeiras:
```javascript
{
    // Configurações de Autenticação
    "server": "br", // Coloque aqui o seu serivdor.
    "username": "username", // Coloque aqui o seu usuário. 
    "password": "password", // Coloque aqui a sua senha.
    ....
}
```
Você trocará a palavra ``username`` pelo seu usuário e a palavra ``password`` pela a sua senha. Caso queira executar o robô em outro servidor, você terá que trocar a palavra ``br`` por ``www`` ou ``friends``.

E pronto! Todas as configurações já foram feitas. Para executar o ClearBot, basta abrir o terminal e executar o seguinte comando:

```python
python ClearBot.py
```

------
### Robô público
Caso você achou complicado configurar o ClearBot ou não tem condições de executar no seu computador, não tem problema! Nós temos o nosso própio ClearBot sendo executado 24 horas por dia.

Para usar-lo, adicione o usuário [ClearBot](https://kogama.com.br/profile/5236862/) no KoGaMa BR. Depois, o convide para um projeto, e pronto! O seu mapa estará protegido.

Tenha em mente de que o robô público tem algumas limitações e você tem que confiar em que nós não destruiremos o seu mapa usando a conta do ClearBot. Por isso, nós recomendamos que execute o ClearBot em sua conta e no seu própio computador.
  
  
