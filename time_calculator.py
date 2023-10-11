def split(input_string, delim):
    parts = []
    current_part = ""

    for char in input_string:
        if char == delim:
            current_part.strip('"').strip()
            parts.append(current_part)
            current_part = ""
        else:
            current_part += char
    current_part.strip('"').strip()
    parts.append(current_part)

    return parts

def add_time(start, duration, day = 0):
  flag_nd = 0
  days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
  if day == 0:
    flag = 0
    day = 0
  else:
    flag = 1
    for indeks, element in enumerate(days):
      if element.lower() == day.lower():
          #print(f"Znaleziono '{szukany_string}' na indeksie {indeks}")
          break
    day = indeks
    day_name = days[day]
    
  start_ = split(start, ' ')
  start_time = start_[0]
  start_part = start_[1]

  start_time_h = int(start_time.split(":")[0])
  start_time_m = int(start_time.split(":")[1])

  duration_ = split(duration, ":")
  duration_h = int(duration_[0])
  duration_m = int(duration_[1])

  hours = start_time_h + duration_h
  min = start_time_m + duration_m

  while min >= 60:
    min -= 60
    hours += 1

  if min < 10:
    min = f"0{min}"
    
  d_count = 0
  day_i = day

  while hours >= 12:
    hours -=  12
    if start_part == "AM":
      start_part = "PM"
    elif start_part == "PM":
      flag_nd = 1
      d_count += 1
      start_part = "AM"
      if flag == 0:
        day += 1
      else:
        day += 1
        day_i += 1
        if day_i > 6:
          day_i = 0

  if hours == 0:
    hours = 12
  
  if flag_nd == 1 and flag == 0:  # następne dni bez nazwy dnia tygodnia
    if d_count == 1:
      day_name = " (next day)"
    else:
      day_name = " (" + str(d_count) + " days later)"
    #print(f"{hours}:{min} {start_part} {day_name}")
    new_time = str(hours) + ":" + str(min) + " " + start_part + day_name
  if flag_nd == 1 and flag == 1: # następne dni z nazwą dnia tygodnia
    if d_count == 1:
      day_name = ", " + days[day_i] + " (next day)"
    else:
      day_name = ", " + days[day_i] + " (" + str(d_count) + " days later)"
    #print(f"{hours}:{min} {start_part} {day_name}")
    new_time = str(hours) + ":" + str(min) + " " + start_part + day_name
  if flag_nd == 0 and flag == 0: # ten sam dzień bez nazwy dnia tygodnia
    #print(f"{hours}:{min} {start_part}")
    new_time = str(hours) + ":" + str(min) + " " + start_part
  if flag_nd == 0 and flag == 1: # ten sam dzień z nazwą dnia tygodnia
    day_name = ", " + days[day_i]
    new_time = str(hours) + ":" + str(min) + " " + start_part  + day_name
    
  return new_time