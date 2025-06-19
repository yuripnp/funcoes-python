"""
apos digitar a hora, devemos mostrar se é de manhã, tarde e noite
"""

def saudacao(hora: int):
    try:
        if hora > 23 or hora < 0:
            raise ValueError(f"hora incerta {hora}")
        elif hora > 18 or hora < 5:
            print("boa noite!")
        elif 12 < hora < 19:
            print(f"boa tarde!")
        elif 4 < hora < 13:
            print(f"bom dia!")
    except TypeError as e:
        print(f"valor invalido {e}")

saudacao(12)
saudacao(3)
saudacao(13)
saudacao(25)
saudacao("a")