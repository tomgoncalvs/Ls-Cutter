from PIL import Image
from functions.loading import loading_animation
from functions.cutterlogo import cutterlogo
import os

def cutter():
    cutterlogo()
    try:
        while True:
            img = input('Digite o nome da sua imagem com a extensão. Exemplo: imagem.png\n')

            nome_imagem = img

            pasta_destino = nome_imagem.replace(".", "-cortada.")
            if not os.path.exists(pasta_destino):
                os.mkdir(pasta_destino)

            imagem = Image.open(nome_imagem)

            parte1 = imagem.crop((0, 0, 512, 512))
            parte1.save(os.path.join(pasta_destino, "parte1.png"), "PNG")
            print('Parte 1 salva com sucesso.')
            loading_animation()

            parte2 = imagem.crop((512, 0, 1024, 512))
            parte2.save(os.path.join(pasta_destino, "parte2.png"), "PNG")
            print('Parte 2 salva com sucesso.')
            loading_animation()

            parte3 = imagem.crop((0, 512, 512, 768))
            parte4 = imagem.crop((512, 512, 1024, 768))

            nova_imagem = Image.new("RGB", (512, 512))
            nova_imagem.paste(parte3, (0, 0))
            nova_imagem.paste(parte4, (0, 256))
            nova_imagem.save(os.path.join(pasta_destino, "parte3_e_4.png"), "PNG")
            print('Parte 3 e 4 salva com sucesso.')
            loading_animation()

            resposta = input('Deseja cortar outra imagem? (S para sim): ')
            if resposta.lower() != "s":
                break

        print('Encerrando o programa.')
    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário.')