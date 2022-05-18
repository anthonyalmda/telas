import requests


class Telegram:
    def send_mensage(self, args):
        msg = args
        chave_api = '5304396569:AAGlQ3X00nvVWrTp2I_k9cruNhOZAoaMVEY'
        url = f'https://api.telegram.org/bot{chave_api}/'
        chat = -1001704314396
        try:
            url = f'{url}sendMessage?chat_id={chat}&text={msg}'
            print('entrei na rotina do bot')
            requests.get(url)
        except Exception as retorno:
            print(f'deu o seguinte erro: {retorno}')


