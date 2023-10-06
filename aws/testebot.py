import requests

# Token do seu bot Telegram
token = "6472487476:AAE_-AnAwtb8o74kqAyiEuG67BUugr2mQWQ"

# ID do chat para o qual você deseja enviar a mensagem



chat_ids = ["1301216791", "1930602886", "5702572389", ""]
# Mensagem que você deseja enviar
# mensagem = "Olá, esta é uma mensagem do meu script Python!"

# URL da API do Telegram para enviar mensagens
url = f"https://api.telegram.org/bot{token}/sendMessage"

# Parâmetros da requisição

# Enviar a mensagem para o bot Telegram
def send_msg(mensagem, url):
    for chat_id in chat_ids:
        params = {
            "chat_id": chat_id,
            "text": mensagem
        }
        response = requests.post(url, params=params)

        # Verificar se a mensagem foi enviada com sucesso
        if response.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print("Erro ao enviar a mensagem:", response.status_code)
            print(response.text)



def tratamsg13(sequencia, label1):
    mensagem = f"🥷 ENTRE NA ROLETA!⚡\nGatilho 1:3 acionado.\nÚltimo número: {sequencia[:3]}\n✅ Padrões ativos:\n"
    for label, val in label1.items():
        if val == True:
            mensagem = mensagem + f"-> {label}\n"
    continuacao = "\n- Apostar nas duas opostas\n- Cobrir ZERO e Nºs quentes!\n\n🔘 Proteção:\n- Triplicar 1ª vez: ainda ganha\n- Triplicar 2ª* vez: somente recupera\n- Triplicar 3 ou + vezes: obrigado a triplicar e aumentar (martingale ofensivo)\n*proteger mais de 1x somente se entrar baixo\n"
    mensagem = mensagem + continuacao
    return mensagem


def tratamsg12(sequencia,label2):
    if list(label2.values())[6] == True or list(label2.values())[7] == True:
        mensagem = f"🥷 ENTRE NA ROLETA!⚡\nGatilho RACETRACK acionado.\nÚltimo número: {sequencia[:3]}\n✅ Padrões ativos:\n"
        for label, val in label2.items():
            if val == True:
                mensagem = mensagem + f"-> {label}\n"
        if list(label2.values())[6]:
            continuacao =  "\n- Apostar com 9 vizinhos no número [22]\n- Cobrir Nºs quentes somente se entrar ALTO!\n\n 🔘Proteção:\n- Duplicar e aumentar (2,5x - Martingale ofensivo)"
        else:
            continuacao =  "\n- Apostar com 9 vizinhos no número [34]\n- Cobrir Nºs quentes somente se entrar ALTO!\n\n 🔘Proteção:\n- Duplicar e aumentar (2,5x - Martingale ofensivo)"
        mensagem = mensagem + continuacao
    else:
        mensagem = f"🥷 ENTRE NA ROLETA!⚡\nGatilho 50/50 acionado.\nÚltimo número: {sequencia[:3]}\n✅ Padrões ativos:\n" 
        for label, val in label2.items():
            if val == True:
                mensagem = mensagem + f"-> {label}\n"
        continuacao = "\n- Apostar no oposto\n- Cobrir ZERO e Nºs quentes!\n\n🔘Proteção:\n- Sempre duplicar  ou\n- Martingale Ofensivo (duplicar e aumentar)*\n\n*Caso entre baixo ou atrasado!"
        mensagem = mensagem + continuacao
    return mensagem          