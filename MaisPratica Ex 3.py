seg=int(input("Por favor, digite o número de segundos que deseja converter:"))
dias=seg//86400
segundos=seg%86400
horas=seg//3600
segundos=seg%3600
minutos=seg//60
segundos=seg%60
print(dias,"dias, ",horas,"horas, ",minutos,"minuto e",segundos,"segundos")
'''1 hora = 3600 segundos 
   1 minuto = 60 segundos
   1 dia = 24 horas = 86400 segundos '''
   