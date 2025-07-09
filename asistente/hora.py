import datetime

fecha = datetime.datetime.now()

print("Hoy es dia {} del año {} con la hora {}:{}, segundos {}".format(fecha.day, fecha.year, fecha.hour,fecha.minute, fecha.second))