'''
/*
 * ClearBot - Versão 1.0
 * Desenvolvido por: Ars3ne
*/
'''
from kogama import Kogama
from bs4 import BeautifulSoup
import json
import re
import threading

# Configurações:
check_comments = 30 # A quantidade de comentários que o bot verificará. Se você estiver executando o bot na sua conta, é recomendado que coloque um valor alto.
auto_add = False # Não recomendado se estiver executando o bot na sua conta e não funciona com a versão pública do Kogama.py. Se estiver como 'True', o bot aceitará todos os pedidos de amizade, e depois deletará todos os amigos depois de um tempo.
auto_join = False # Não recomendado se estiver executando o bot na sua conta. Se estiver como 'True', o bot aceitará todos os convites de projetos automaticamente.
acceptable_emotes = 10 # Coloque aqui o número máximo de emojis que uma mensagem pode ter.
debug_map_id = 0 # Não funciona corretamente com a versão pública do Kogama.py. Aqui fica um ID de um mapa que você queira que sirva como debug. Muito provavelmente você não quer isso, então deixe 0.
# Abaixo, uma lista de palavras bloqueadas. Se elas forem detectadas em um comentário, este será deletado imediatamente.
blocked_keywords = ['ouro', 'f1', 'f5', 'espaços', '.­', 'profile', 'avatar', 'games', 'market', 'youtu', 'hack de elite', 'tire os', 'esse link', 'remova os', 'copie', 'cole', 'ganhe', 'cupom', 'grátis', 'ganhar', 'sorteio', 'testei', 'esse perfil', 'receba', 'não acredita', 'hack de ouro', 'senha', 'var' , 'email', 'essa mensagem', 'código', 'ler', 'morrerá', 'morreu']

# Realizando o login...
print("[ClearBot] Iniciando bot...")
k = Kogama.Kogama("br") # Caso queira usar no servidor WWW, mude para "www". Se quiser no friends, mude para "friends".
l = k.Auth().login('username', 'password') # Tente fazer o login.

# A PARTIR DAQUI, NÃO MUDE NENHUMA LINHA SEM SABER O QUE ESTÁ FAZENDO.

if not l: exit('[ClearBot] Não foi possível fazer login.') # Se não deu para logar, fale que não deu para logar.
print("[ClearBot] Bot logado com sucesso!")

info = k.User().get_info()
bot_id = info['data']['id'] # Se deu para logar, pegue o ID do bot.

# Funções
def getGames(): # Obtém os mapas que o bot é membro.
  r = k.session.get('https://br-lb3.kgoma.com/game/')
  return json.loads(r.text)

def getGameComments(gameId): # Obtém os últimos comentários de um mapa
  r = k.session.get('https://br-lb3.kgoma.com/game/{}/comment?page=1?count={}'.format(gameId, check_comments))
  return json.loads(r.text)

#Funções de adicionar amigos

def getFriends(): # Obtem os amigos
  f = k.session.get("https://br-lb3.kgoma.com/profile/{}/friends".format(bot_id))
  html = f.content
  soup = BeautifulSoup(html, 'lxml')
  data = soup.find_all("script")[8].string
  options = re.findall("options.bootstrap\s*=(.+)", data)
  return json.loads(options[0][:-1])

def addFriends(): # Adiciona os amigos pendentes. Não funciona na versão pública do Kogama.py.
 threading.Timer(30.0, addFriends).start()
 friends = getFriends()
 print("[ClearBot] Verificando pedidos de amizade...")
 for user in friends['friends_requests']:
   k.User().add_friend(user['profile_id'])
   print("[ClearBot] Usuário {} adicionado!".format(user['profile_username']))

def removeFriends(): # Remove todos os amigos.
  threading.Timer(900.0, removeFriends).start()
  friends = getFriends()
  print("[ClearBot] Removendo amigos...")
  for user in friends['friends']:
    if user['friend_profile_id'] == 6587062: continue # Caso você não queira que o bot te delete, coloque o seu ID aqui.
    k.User().remove_friend(user['friend_profile_id'])
    print("[ClearBot] Usuário {} removido!".format(user['friend_username']))

#Funções para aceitar projetos
def getGameInvites(): # Obtem os convites
  g = k.session.get("https://br-lb3.kgoma.com/user/{}/invitations".format(bot_id))
  return json.loads(g.text)

def acceptGameInvites(): # Aceita os convites
 threading.Timer(30.0, acceptGameInvites).start()
 invites = getGameInvites()
 print("[ClearBot] Verificando convites...")
 for game in invites['data']:
   print(game['game_id'])
   g = k.Game().accept_invite(game['game_id'])
   #k.Game().add_comment(game['game_id'], " :herocheer2c | A partir de agora, eu estou protegendo os comentários desse mapa de correntes de ouro, golpes, e várias outras coisas!")
   print("[ClearBot] Convite do mapa {} aceito!".format(game['game_id']))

debug_comments = [] # Lista para armazenar os comentários já analisados no mapa debug.

def deleteComment(gameId, commentId, reason): # Função para deletar os comentários
  if gameId == debug_map_id: # Se o ID for igual ao mapa de testes, faça um comentário explicando o motivo do comentário ter sido detectado
    k.Game().add_comment(gameId, reason)
    debug_comments.append(commentId)
  else: # Se não, então apenas delete o comentário.
    k.Game().remove_comment(gameId, commentId)

  print("[ClearBot] " + reason) # Seja lá qual caso for, mande o motivo para o console.

def ClearBot(): # E, finalmente, a função do bot.
  games = getGames()
  print("[ClearBot] Obtendo mapas...")
  for game in games['data']: # Obtem os mapas que o bot é membro e faz um loop neles.
    comments = getGameComments(game['id'])
    print("[ClearBot] Verificando mapa {}".format(game['id']))
    print("[ClearBot] Lendo comentários...")
    for comment in comments['data']: # Obtem os comentários do mapa e faz um loop deles.

      if comment['profile_id'] == bot_id: continue # Se o comentário for do bot, ignore.
      if comment['id'] in debug_comments: continue # Se o comentário já foi analisado no modo debug, ignore.

      comment_json = json.loads(comment['_data'])
      has_blocked_words = re.findall(r"(?=("+'|'.join(blocked_keywords)+r"))",comment_json['data'].lower())

      if 'emotes' in comment_json: # Se existem emotes no comentário, faça a verificação de emotes aceitáveis.
        rx = re.findall('(?<=:)\w[^\s]*', comment_json['data'])
        if len(rx) > acceptable_emotes: # Se existem mais emotes do que o aceitável, delete a mensagem.
          deleteComment(game['id'], comment['id'], "Uso excessivo de emojis detectado. ({}/{}). ID: {}".format(len(rx), acceptable_emotes, comment['id']))
          continue

      if has_blocked_words: # Se a palavra estiver na lista negra, delete o comentário.
        deleteComment(game['id'], comment['id'], "Palavra(s) não permitida(s) detectada(s)! Palavra(s): {}. ID: {}".format(",".join(has_blocked_words), comment['id']))
        continue

      if re.search('[^\w\s]{6,}', comment_json['data']): # Se o comentário tiver mais de 6 caracteres seguidos que não são letras, será considerado como uma arte ASCII e será deletado.
        deleteComment(game['id'], comment['id'], "Arte ASCII (provável mensagem de ouro) detectada. ID: {}".format(comment['id']))
        continue

      if re.search('[a-zA-Z]{20}', comment_json['data']): # Se o comentário tiver um caractere que e repetido várias vezes seguidas, então delete a nensagem.
        deleteComment(game['id'], comment['id'], "Flood detectado. ID: {}".format(comment['id']))      
        continue

      if game['id'] == debug_map_id: # Se o mapa for o mapa de testes, então fale que não achou nada de errado no comentário.
        k.Game().add_comment(game['id'], "Eu não consegui achar nada de errado no seu comentário.")
        debug_comments.append(comment['id'])
        continue

# E, para finalizar, chame as funções.

if auto_add: # Se auto_add está True, então chame as funções para adicionar automaticamente.
  removeFriends()
  addFriends()

if auto_join: # Se auto_join está True, então chame a função de entrar em projetos automaticamente.
  acceptGameInvites()

while True:
  ClearBot() # E por último, chame a função principal do bot.