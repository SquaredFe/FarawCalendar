# Calendar for Faraw VER 1 REV 2
import calendar
from datetime import datetime

year = datetime.now().year 
mes = datetime.now().month 
print("Calendario   -")
print(calendar.month(year, mes))
print("Presiona ENTER para cerrar...")
input()