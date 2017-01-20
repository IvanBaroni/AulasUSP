### Exercício 3

# Entrada
segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")

total_segs = int(segundos_str)   #Deixa como INT pq, por default, input sempre receve STR


dias = total_segs // 86400
sobra_segs_1 = total_segs % 86400  #Define o que sobrou da div por dia

horas = sobra_segs_1 // 3600
sobra_segs_2 = sobra_segs_1 % 3600  #Define o que sobrou da div por hora

minutos = sobra_segs_2 // 60
sobra_segs_3 = sobra_segs_2 % 60  #Define o que sobrou da div por minuto

# Saída
print(dias, "dias,", horas, "horas,", minutos, "minutos e", sobra_segs_3, "segundos.")