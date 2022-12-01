import telebot, csv
from telebot.types import LabeledPrice

token = 'token boot telegram here'
token_provider='token payment here'
img_produto='https://i.ibb.co/J2H7NCX/key1.jpg'

#interagindo com os usuários
respostas = {'oi' : 'Oi em que posso ajudar ?' , 'ola' : 'Olá, em que posso ajudar?'}

bot = telebot.TeleBot(token)

precos = [
    LabeledPrice(label='Pack 1 de Fotos', amount=550)  
]

#função salvar os ids dos usuários que interagem
def salvar(id_telegram):
    with open('ids_telegram.csv' , 'a') as ids:
        e = csv.writer(ids)
        e.writerow([id_telegram])

#função que interage com o usuário quando ele digita /inicio ou /start ou /bunda, o que você quiser definir

@bot.message_handler(commands=['start' , 'inicio', 'bunda'])
def start(message):
    salvar(message.from_user.id)
    bot.send_message(message.chat.id, 'Olá, tudo bom? \n Deseja comprar meus packs com fotos e vídeos? \nClick /comprar para ter meu conteúdo.')

@bot.message_handler(commands=['comprar'])
def comprar(message):
    bot.send_invoice(
      message.from_user.id,
      title='Robo Vendedor',
      description='Já pensou em ter todas as minhas fotos todos os meses?',
      provider_token='350862534:LIVE:NjgzOWRhMmVjYzJk',
      currency='BRL',
      photo_url='https://i.ibb.co/J2H7NCX/key1.jpg',
      photo_height=512,
      photo_size=512,
      photo_width=512,
      is_flexible=False,
      prices=precos,
      invoice_payload='PAYLOAD'
    )

bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(
        pre_checkout_query.id, ok=True, error_message="Transação não realizada, tente novamente em alguns minutos"
    )

bot.message_handler(content_types=['sucessful_payment'])
def pagou(message):
    doc = open('pack1/key1.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    doc = open('pack1/key2.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    doc = open('pack1/key3.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    doc = open('pack1/key4.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    doc = open('pack1/key5.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    doc = open('pack1/key6.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    doc = open('pack1/key7.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    doc = open('pack1/key8.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    doc = open('pack1/key9.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    doc = open('pack1/key10.jpg', 'rb')
    bot.send_document(message.chat.id, doc)

    bot.send_message(message.from_user.id,'Oiiiieee, muito obrigado. Espero que goste, segue o conteúdo...')

# teste de envio de arquivos.
#modelo de envio de arquivo pdf para o bot, assim que o usuário digita /download /pegar etc
#@bot.message_handler(commands=['download', 'baixar'])
#def download(message):
#    doc = open('DOCTORCHOPP.pdf', 'rb')
#    bot.send_document(message.chat.id, doc)

@bot.message_handler(func=lambda m: True)
def tudo(message):
    print("Mensagem: ", message.text)
    resp = respostas.get(str(message.text).lower(), 'Não entendi o que quis dizer, tente novamente')
    bot.send_message(message.from_user.id, resp)

bot.skip_pending = True
bot.polling(none_stop=True, interval=0)

bot.polling()