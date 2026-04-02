import logging
import os


def pegar_caminho():
    logging.basicConfig( level=logging.INFO )

    caminho =input('insira o caminho que voce deseja')

    while not os.path.exists( os.path.join( caminho ) ):
        logging.warning( 'caminho errado, insira outro' )
        caminho=input( 'insira novamente o caminho' )

    logging.info( 'caminho pego com sucesso' )

    return caminho
