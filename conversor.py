import time

# Usuário informa
tempUsuario = input('Coloque sua temperatura [C - Celsius] [F - Fahrenheit] [K - Kelvin]')

if tempUsuario == 'C' or tempUsuario == 'c':
    print('Você está convertendo Celsius para Fahrenheit e Kelvin.')
    C = input('Qual valor você quer converter?')

    F = int(C) * 1.8 + 32
    K = int(C) + 273.15

    print('Celsius -> Fahrenheit: ' + str(F) + '°F')
    print('Celsius -> Kelvin: ' + str(K) + 'K')

elif tempUsuario == 'F' or tempUsuario == 'f':
    print('Você está convertendo Fahrenheit para Celsius e Kelvin.')
    F = input('Qual valor você quer converter?')

    C = (int(F) - 32) / 1.8
    K = ((int(F) - 32) * 5) / 9 + 273.15

    print('Fahrenheit -> Celsius: ' + str(C) + '°C')
    print('Fahrenheit -> Kelvin: ' + str(K) + 'K')

elif tempUsuario == 'K' or tempUsuario == 'k':
    print('Você está convertendo Kelvin para Fahrenheit e Celsius.')
    K = input('Qual valor você quer converter?')

    C = int(K) - 273.15
    F = (int(K) - 273.15) * 1.8 + 32

    print('Kelvin -> Celsius: ' + str(C) + '°C')
    print('Kelvin -> Fahrenheit: ' + str(F) + '°F')

else:
    print('Você precisa digitar uma escala de medida para continuar.')
    print('O programa será encerrado.')

print('Fim do programa')

time.sleep(5)