# Transforma o ângulo em radiano e calcula seno, cosseno e tangente
from math import sin, cos, tan, radians

ang = float(input("Digite o valor do ângulo: "))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('Para o ãngulo {0}:\nO seno é {1:.2f}\nO cosseno é {2:.2f}\nA tangente é {3:.2f}'.format(ang, sen, cos, tan))
