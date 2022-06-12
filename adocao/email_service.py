from django.core.mail import send_mail


def enviar_email_confirmacao(adocao):
    assunto = "Adoção realizada com sucesso."
    conteudo = f"Parabéns por realizar a adoção do  { adocao.pet.nome }, com o valor de {adocao.valor} por mês."
    remetente = "pythonadoteumpet@gmail.com"
    destinatario = [adocao.email]
    send_mail(assunto, conteudo, remetente, destinatario)

