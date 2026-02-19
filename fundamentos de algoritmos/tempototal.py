dias=int(input("digite os dias"))
horas=int(input("digite as horas"))
minutos=int(input("digite os minutos"))
segundos=int(input("digite os segundos"))
total=(dias*86400) + (horas*3600) + (minutos*60) + segundos
print ("o tempo total foi de", total, "segundos")