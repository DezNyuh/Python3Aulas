velocidade = 350 #uma variavel com letra minuscula = variavel
local_carro = 99

RADAR_1 = 60 #uma variavel com letra maiuscula = constante 
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_no_radar = velocidade > RADAR_1
passando_no_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_no_radar:
    print('O carro passou a cima da velocidade do radar 1!')

if passando_no_radar and velocidade_no_radar:
    print('O carro foi multado!')