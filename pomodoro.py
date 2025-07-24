import time


def formatar_tempo(segundos):
    minutos = segundos // 60
    resto_segundos = segundos % 60
    return f"{minutos:02}:{resto_segundos:02}"


def pomodoro(tempo):
    print("Técnica pomodoro iniciada.")
    while tempo >= 0:
        print(f"Faltam {formatar_tempo(tempo)}")
        time.sleep(1)
        tempo -= 1
    print("\nTempo finalizado, agora uma pausa de 5 minutos.\n")


def pausa(tempo):
    print("Pausa iniciada.")
    while tempo >= 0:
        print(f"Faltam {formatar_tempo(tempo)}")
        time.sleep(1)
        tempo -= 1
    print("\nTempo de pausa finalizado.\n")


print("--- Bem-vindo à técnica pomodoro ---\n")
print("Para iniciar digite 's'")
sim_ou_nao = input()

if sim_ou_nao.lower() == "s":
    while True:
        pomodoro(25 * 60)
        pausa(5 * 60)
