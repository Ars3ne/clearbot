# ClearBot

[![Python Version](https://img.shields.io/badge/python-%E2%89%A53.5.3-yellow.svg)](https://www.python.org/downloads/)

------

O ``ClearBot`` é um robô que detecta e remove spam dos comentários dos mapas do jogo ``KoGaMa``.

------


# Instalação:
Para instalar a última versão do ClearBot, basta clicar [aqui](https://github.com/ars3ne/clearbot/releases/latest).

### Dependências:
Para executar o ClearBot, você precisará ter as seguintes dependências:
* Python na versão 3.5.3 ou maior
* ``kogama.py``
* ``requests``
* ``beautifulsoup4``

Depois de instalar o Python, para instalar as outras dependências, basta instalar o ``kogama.py``, usando o comando abaixo:
```
pip install kogama.py
```

As outras dependências devem ser baixadas automáticamente depois de baixar o ``kogama.py``

### Configurações
------
Depois de instalar o ClearBot, abra o arquivo ``ClearBot.py``. Já nas primeiras linhas terá algumas configurações que você não precisa mudar, mas recomendamos que você de uma olhada nelas.

```python
# Configurações:
check_comments = 30 # A quantidade de comentários que o bot verificará. Se você estiver executando o bot na sua conta, é recomendado que coloque um valor alto.
auto_add = False # Não recomendado se estiver executando o bot na sua conta e não funciona com a versão pública do Kogama.py. Se estiver como 'True', o bot aceitará todos os pedidos de amizade, e depois deletará todos os amigos depois de um tempo.
auto_join = False # Não recomendado se estiver executando o bot na sua conta. Se estiver como 'True', o bot aceitará todos os convites de projetos automaticamente.
acceptable_emotes = 10 # Coloque aqui o número máximo de emojis que uma mensagem pode ter.
debug_map_id = 0 # Não funciona corretamente com a versão pública do Kogama.py. Aqui fica um ID de um mapa que você queira que sirva como debug. Muito provavelmente você não quer isso, então deixe 0.
```

Para finalizar, depois de mudar ou não as configurações, você verá o seguinte trecho:
```python
# Realizando o login...
print("[ClearBot] Iniciando bot...")
k = Kogama.Kogama("br") # Caso queira usar no servidor WWW, mude para "www". Se quiser no friends, mude para "friends".
l = k.Auth().login('username', 'password') # Tente fazer o login.
```
Você terá que mudar a última linha, trocando a palavra ``username`` pelo usuário e a palavra ``password`` pela senha da conta que você quer executar o robô, sem remover ás aspas.

E pronto! Todas as configurações já foram feitas. Para executar o ClearBot, basta abrir o terminal e executar o seguinte comando:

```python
python ClearBot.py
```

------
### Robô público
Caso você achou complicado configurar o ClearBot ou não tem condições de executar no seu computador, não tem problema! Nós temos o nosso própio ClearBot sendo executado 24 horas por dia.

Para usar-lo, adicione o usuário [ClearBot](https://kogama.com.br/profile/5236862/) no KoGaMa BR. Depois, o convide para um projeto, e pronto! O seu mapa estará protegido.

Tenha em mente de que o robô público tem algumas limitações e você tem que confiar em que nós não destruiremos o seu mapa usando a conta do ClearBot. Por isso, nós recomendamos que execute o ClearBot em sua conta e no seu própio computador.
  
  
