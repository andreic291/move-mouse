import pyautogui as pg
import time

# Get the desired position of the mouse
x_game,y_game = pg.position()
print("Position saved")

# Request from user the number of clicks
no_clicks = int(input("How many clicks do you require?: "))

# Starting text and initialization of count
print()
print("Started clicking!")
print()
count = 0

# Ask the user whether they want to wait before the clicks or not
wait = input("Do you want to wait for a task to finish?[y/n]: ")
if(wait == "y"):
   hour_req = int(input("Hours: "))
   min_req = int(input("Minutes: "))
   sec_req = int(input("Seconds: "))
   total_req = hour_req * 3600 + min_req * 60 + sec_req 
   print("Sleeping for: " + str(hour_req) + ":"+ str(min_req) + ":"+ str(sec_req))
   time.sleep(total_req)

# Clicking loop
while (count < no_clicks):
   count += 1
   x_now,y_now = pg.position()
   pg.moveTo(x_game,y_game)
   pg.click(x_game,y_game)
   pg.moveTo(x_now,y_now)
   print("Click #!" + str(count))
   if (count != no_clicks):
      print("Waiting...")
      time.sleep(16)
   else:
      break
print("The script finished after " + str(count) +" clicks!")
