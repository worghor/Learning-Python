velocidade = 61  # velocidade atual do carro
local_carro = 90  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
Carro_multado_radar_1 =  local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1:
    print("Carro passou pelo radar 1")

if velocidade > RADAR_1 and velocidade_carro_passou_radar_1:
    print("Carro multado pelo radar 1")