#setup of variables
start_x_coordinate = 0
start_y_coordinate = 0
start_z_coordinate = 0
work_coordinate = "G54"
tool_number = 1
spindle_rpm = 1000
feedrate = 20
z_feedrate = 10
z_clear = .25
z_start = 0
z_end = -1
use_coolant = True
end_x_coordinate = 2
end_y_coordinate = 2
safety_line = "G17 G90  (XY Plane, Absolute Distance Mode)\nG20 (units in inches)"
g64_line = "G64"

#setup of file
file_name = "my_gcode_file"
file_path = "/Users/nkowalczyk/Downloads/" + file_name + ".nc"

#open file
with open(file_path, "w") as file:
    file.write(str(safety_line) + "\n")
    file.write(str(g64_line) + "\n")
    file.write("G20 (units in inches)" + "\n)")
    file.write(str(work_coordinate) + " (Set work offset)" + "\n")
    file.write("G30 (move to G30 location)" + "\n")
    file.write("\n")
    file.write("T" + str(tool_number) + " G43 H" + str(tool_number) + "\n")
    file.write("F" + feedrate + " (Feed, inches/minute)" + "\n")
    file.write("S" + spindle_rpm + " (RPM)" + "\n")
    file.write("\n")
    if use_coolant:
        file.write("M8" + " (Flood coolant on)" + "\n")
    file.write("M3" + " (Spindle on, forward)" + "\n")
    file.write("G0 X" + start_x_coordinate + " Y" + start_y_coordinate + "\n")
    file.write("F" + z_feedrate + " (Z feed, inches/minute)" + "\n")
    file.write("G0 Z" + start_z_coordinate + "\n")

