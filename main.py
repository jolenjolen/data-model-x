
logo="""
██████╗  █████╗ ████████╗ █████╗     ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗         ██╗  ██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║         ╚██╗██╔╝
██║  ██║███████║   ██║   ███████║    ██╔████╔██║██║   ██║██║  ██║█████╗  ██║          ╚███╔╝ 
██║  ██║██╔══██║   ██║   ██╔══██║    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ██║          ██╔██╗ 
██████╔╝██║  ██║   ██║   ██║  ██║    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗    ██╔╝ ██╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝    (v1.5-bw)
""" # text to ASCII art (ANSI Shadow) generated from https://patorjk.com/
# Do not make changes to the code unless you know what you are doing. refer to the guide on Github https://github.com/jolenjolen


import csv # this library will be used to read from the csv file. Please don't remove this line. If removed, the program will be unable to read the data from the csv files
import os # the os library performs many functions such as reading the directory and also the ability to scan for csv data files as well as color the terminal text in color version of this program (DATA_MODEL_X_vx.x-color)

try: # using try and except to check/validate if the graphics.py file is in the same directory
    from graphics import * # importing the graphics library in this code. Don't forget to include the graphics.py file in the same directory as this code file. needed to display the histogram.
except ImportError: # if the graphics.py file is not found, print an error and quit
    print("\nError: 'graphics' library not found. Make sure graphics.py is in the same directory.")
    quit() # inbuilt function to exit the program
    # Note to programmer/maintainer: For future update, the program can ask the user to enter the graphics.py file path so that the program doesn't need to terminate. A pro update can be to install it directly for the user using pip: pip install graphics.py


########## Global variables ##########
data_list = []  # An empty list to load and hold data from the csv file(s).
csv_file_list = [] # As the program automatically scans for the .csv files from the current working directory, we store the file names in this list
# add more global variables here if needed 
######################################


def prerequisite(): # checks if the data files (.csv) are available and accessible from the same working directory
    global csv_file_list # this list will store the csv file names.
    current_directory = os.getcwd() # gets the path of the program (gets the current working directory)
    files_and_dirs = os.listdir(current_directory) # lists all the sub-directories and files in this dir (same as `ls` in cmd or terminal)
    
    for item in files_and_dirs: # code to append the variable csv_file_list with the filenames that end with .csv
        if os.path.isfile(os.path.join(current_directory, item)) and item.endswith('.csv'): # if the listed output is a file (and not a directory), join the path,the file name, and validate that it ends with .csv (eg. `path/to/`+`filename` and ends with `.csv`)
            csv_file_list.append(item) # if the file is CSV, append the list with the filename.

    if not csv_file_list: # after a complete sprint and no csv files found, give an error and quit the program
        print("\nError: '.csv' file(s) are not in the directory. Make sure at least 1 data file ending with .csv is in the same directory.")
        quit() # inbuilt function to exit the program
        # Note to programmer/maintainer: For future update, the program can ask the user to enter the csv file path so that the program doesn't need to terminate.
    elif csv_file_list: # afer a complete sprint and csv file(s) were found, all the runtime checks are complete so print the logo and run the function load_data()
        file_,row_length=load_data() # the function load_data() returns the filename that we want to focus for analysis

    return file_,row_length # returns the same filename to main for analysis along with the row length

def load_data():
    global data_list # global variable. this means i can access it both inside/outside the function and make changes to its values
    global csv_file_list # same goes for this variable as well. this is a list that holds the data from the specific csv file that we will select.
    print("\nPlease enter the date of the survey in the format DD/MM/YYYY") 
    while True: # this looks a bit messed up but hang on...
        # What happens if the user enters the wrong date or uses a different format?
        day_,month_,year_ = validate_date() # so, we are validating that input which will make our lives way easier -- this is the first stage of our date validation | the date entered by the user in one string DD/MM/YYYY is then splitted into DD, MM, YYYY and stored in respective variables
        # after fetching a proper date, we check each csv file from the csv_file_list by opening it and checking if the date inside matches the date entered by the user -- this is the second stage of our date validation
        for file_ in csv_file_list: # if the date entered is not the first file, then the second file, third file, etc are checked until the correct file matching the date is found. in none found, gives an error
            data_list = [] # since this request will run multiple times if the user enters another date at the end of the program, we flush all the values stored in var data_list so that we can have a fresh start
            with open(file_, 'r') as file:     #
                csvreader = csv.reader(file)   # don't even ask about this snippet.
                header = next(csvreader)       # I only used this because it was already given in the template file.
                for row in csvreader:          # (long story short: it reads the file by taking the filename from csv_file_list, then appends the data to data_list)
                    data_list.append(row)      #
            column_length=len(header) # not even needed here but i'll keep it for debugging purposes
            row_length=len(data_list) # this is very important. it matters more than  my life to run this program properly

            date = data_list[0][1] # now since the data from this file is stored in data_list, i'll just store the date found in this data_list at row 1 and column 2 in var date
            day, month, year = map(int, date.split('/')) # split the date from DD/MM/YYYY to DD, MM, and YYYY and store in respective variables
            if(day==day_ and month==month_ and year==year_): # the second stage validation checks the date_ enetered by the user by the date found in the data file
                return file_,row_length # if both dates matches, return the filename and the row length
        if(day!=day_ or month!=month_ or year!=year_): # this is the error message that is displayed if the data for the selected date doesn't exist
            print("\nNo data for this date exists")

def validate_date(): # first stage validation that literally gave me first stage cance-
    while True:
        date_ = input("\nDate: ") # takes the date from the user
        try:
            day_, month_, year_ = map(int, date_.split('/')) # tries to split the date in 3 sections DD, MM, YYYY by using the '/' as the split initiator 
        except ValueError:
            print("\nInteger required") # yea... the date should be an interger except for the slashes '/'
            continue # rerun the above section until the user die out of exhaustion of inputing wrong values

        if year_ < 2000 or year_ > 2024: # that's what i was told to do
            print("\nThe date is out of range") # give error if the year is out of range
            continue # and... same thing like before, re-run until the user gives up
            
            # Validate the month range.
        if month_ < 1 or month_ > 12:
            print("\nThe date is out of range")
            continue
            
            # Validate the day range based on the month
        if day_ < 1 or day_ > 31:
            print("\nThe date is out of range")
            continue
            
            # Check for months with fewer than 31 days
        if month_ in [4, 6, 9, 11] and day_ > 30: # months april, june, september and november all have 30 days. so if the day is more than 30 for this month, then you know they are faking it!!
            print("\nThe date is out of range")
            continue
            
            # Check for February (28 days, or 29 in a leap year) # part of code taken from tutorial excersise coz i'm too lazy to do it all over again
        if month_ == 2: # basically the month of fabruary
            if (year_ % 4 == 0 and year_ % 100 != 0) or (year_ % 400 == 0): # the YEAR/4 = remainder 0, and YEAR/100 = remainder not 0, OR and a big OR, YEAR/400 = remainder 0, then run the below code
                if day_ > 29: # this means that theres a chance of it being a leap year or heck it is a leap year. but if the date's more than 29, you are not living on planet earth dude!!
                    print("\nThe date is out of range")
                    continue
            else:
                if day_ > 28: # if its not a leap year, then there shouldn't be any reason for the date to be above 28. Caught ya!!
                    print("\nThe date is out of range")
                    continue

        return day_, month_, year_ # after a successful validation, return the date, month, and year
    
def total_vehicles_on_day(row_length):
    total_vehicles_on_day=0
    for i in range(row_length): # this will read every row where `i` is the row number
        total_vehicles_on_day+=1 # when you know there's a row, you know there's data there. 
    return f"The total number of vehicles recorded for this date is {total_vehicles_on_day}" # idk why, but i kinda like using f strings

def total_trucks_on_day(row_length):
    total_trucks_on_day=0
    for i in range(row_length):
        if data_list[i][8]=='Truck': # only if data_list[i][8] = 'Truck' | in data_list[i][8]--> i is the row number and 8 is the column number. you migh be wondering how i knew it was the 8th column, well i just looked it up in the data myself
            total_trucks_on_day+=1 # increment! hopefully that's the word you were looking for ;) 
    return f"The total number of trucks recorded for this date is {total_trucks_on_day}"

def total_ev_on_day(row_length):
    total_ev_on_day=0
    for i in range(row_length):
            if data_list[i][9]=='True':
                total_ev_on_day+=1
    return f"The total number of ev's recorded for this date is {total_ev_on_day}"

def total_two_wheelers_on_day(row_length):
    total_two_wheelers_on_day=0
    for i in range(row_length):
            if data_list[i][8]=='Bicycle' or data_list[i][8]=='Motorcycle' or data_list[i][8]=='Scooter': # or maybe i could have just done  if data_list[i][8] in ["Bicycle","Motorcycle","Scooter"] to check if its either 1 of the 3 from the list
                total_two_wheelers_on_day+=1
    return f"The total number of two wheelers recorded for this date is {total_two_wheelers_on_day}"

def total_buses_leaving_elm_North(row_length):
    total_buses_leaving_elm_North=0
    for i in range(row_length):
            if data_list[i][0]=='Elm Avenue/Rabbit Road' and data_list[i][4]=='N' and data_list[i][8]=='Buss': # junction to focus on: elm avenue; direction of exit: North; type of vehicle: Buss
                total_buses_leaving_elm_North+=1
    return f"The total number of buses leaving Elm Avenue/Rabbit Road heading North, recorded for this date is {total_buses_leaving_elm_North}"

def total_vehicles_straight_through(row_length):
    total_vehicles_straight_through=0
    for i in range(row_length):
            if data_list[i][3]==data_list[i][4]: # checking if direction in and direction out is the same
                total_vehicles_straight_through+=1
    return f"The total number of vehicles through both junctions not turning left or right, recorded for this date is {total_vehicles_straight_through}"

def percent_of_trucks_on_day(row_length):
    total_trucks_on_day=0
    total_vehicles_on_day=0
    for i in range(row_length):
            total_vehicles_on_day+=1
            if data_list[i][8]=="Truck": 
                total_trucks_on_day+=1
    percent_of_trucks_on_day=round((total_trucks_on_day/total_vehicles_on_day)*100)
    return f"The percentage of Trucks for this date is {percent_of_trucks_on_day}%"

def average_bicycles_per_hr_on_day(row_length):
    total_bicycles=0
    for i in range(row_length):
            if data_list[i][8] == "Bicycle":
                total_bicycles+=1
    average_bicycles_per_hour = round(total_bicycles / 24)
    return f"the average number of Bicycles per hour for this date is {average_bicycles_per_hour}"

def vehicles_overspeeding_on_day(row_length):
    vehicles_overspeeding_on_day=0
    for i in range(row_length):
        if int(data_list[i][7])>int(data_list[i][6]):
            vehicles_overspeeding_on_day+=1
    return f"The total number of vehicles recorded as over the speed limit for this date is {vehicles_overspeeding_on_day}"

def vehicles_only_through_elm_on_day(row_length):
    vehicles_only_through_elm_on_day=0
    for i in range(row_length):
        if data_list[i][0]=="Elm Avenue/Rabbit Road":
            vehicles_only_through_elm_on_day+=1
    return f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {vehicles_only_through_elm_on_day}"

def vehicles_only_through_hanley_on_day(row_length):
    vehicles_only_through_hanley_on_day=0
    for i in range(row_length):
        if data_list[i][0]=="Hanley Highway/Westway":
            vehicles_only_through_hanley_on_day+=1
    return f"The total number of vehicles recorded through Hanley Highway/Westway junction is {vehicles_only_through_hanley_on_day}"

def percent_of_scooters_through_elm(row_length):
    total_scooters_through_elm=0
    total_vehicles_through_elm=0
    for i in range(row_length):
        if data_list[i][0]=="Elm Avenue/Rabbit Road":
            total_vehicles_through_elm+=1
            if data_list[i][8]=="Scooter":
                total_scooters_through_elm+=1
    percent_of_scooters_on_day=round((total_scooters_through_elm/total_vehicles_through_elm)*100)
    return f"The percentage of scooters through Elm Avenue/Rabbit Road for this date is {percent_of_scooters_on_day}%"

def total_vehicles_during_peak_hr_at_hanley(row_length):
    vehicle_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for row in range(row_length):
        if data_list[row][0] == "Hanley Highway/Westway":
            
            hour = int(data_list[row][2][:2])  # Extract the hour from the time column. [:2] takes the first 2 characters of the time string (HH)
            vehicle_count[hour] += 1  # Increment the count for that hour

            # Now, find the hour with the maximum count
    max_count = max(vehicle_count)
    #max_hour = vehicle_count.index(max_count)  # Get the index of the max count 
    return f"The highest number of vehicles in an hour on Hanley Highway/Westway is {max_count}"

def time_of_peak_at_hanley(row_length):
    vehicle_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for row in range(row_length):
        if data_list[row][0] == "Hanley Highway/Westway":
            
            hour = int(data_list[row][2][:2])  # Extract the hour from the time column. [:2] takes the first 2 characters of the time string (HH)
            vehicle_count[hour] += 1  # Increment the count for that hour

            # Now, find the hour with the maximum count
    max_count = max(vehicle_count)
    max_hour = vehicle_count.index(max_count)  # Get the index of the max count
    
    hours_with_max_count = []
    
    for i in range(len(vehicle_count)):
        if vehicle_count[i] == max_count:
            hours_with_max_count.append(i)
    
    if len(hours_with_max_count)>1:
        time="The most vehicles through Hanley Highway/Westway were recorded between "
        for i in range(len(hours_with_max_count)):
            time+=f"{hours_with_max_count[i]}:00-{hours_with_max_count[i]+1}:00"
            if i+1==len(hours_with_max_count)-1:
                time+=" and "
            elif i+1==len(hours_with_max_count):
                time+=""
            elif i<len(hours_with_max_count):
                time+=", "
        return time
    else:
        return f"The most vehicles through Hanley Highway/Westway were recorded between {max_hour}:00 and {max_hour+1}:00"

def total_rainy_hrs(row_length):
    rainy_hours = set()  # Set to store distinct hours where it rained
    for row in range(row_length):
        # Check if the weather condition is "Light Rain" or "Heavy Rain"
        weather_condition = data_list[row][5]
        if weather_condition in ["Light Rain", "Heavy Rain"]:
            hour = int(data_list[row][2][:2])  # Extract the hour from the time column again
            rainy_hours.add(hour)  # Add the hour to the set of rainy hours
    num_rainy_hours = len(rainy_hours)  # The size of the set gives the number of distinct rainy hours
    return f"The number of hours of rain for this date is {num_rainy_hours}"

def save_results_to_file(file_name, results):
    # Open the file in append mode
    with open(file_name, 'a') as file:
        file.write(results + '\n')  # Write the values and a newline character
    

def draw_histogram(win,row_length):
    global data_list
    vehicle_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    section1_height=Rectangle(Point(1,563), Point(1000,1))
    
    for row in range(row_length):
        hour = int(data_list[row][2][:2])  # Extract the hour from the time column
        vehicle_count[hour] += 1  # Increment the count for that hour
    
    # Find the maximum vehicle count to scale the bars
    max_height = max(vehicle_count)
    if max_height == 0:
        max_height = 1
    #section1_height.setFill("yellow")
    window_height = 400  # Max height of the bars (vertical space in the window)
    scaling_factor = window_height / max_height
    #section1_height.draw(win)
    vehicle_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    

    for row in range(row_length):
        
        if data_list[row][0] == "Hanley Highway/Westway":
            
            hour = int(data_list[row][2][:2])  # Extract the hour from the time column. [:2] takes the first 2 characters of the time string (HH)
            vehicle_count[hour] += 1  # Increment the count for that hour
    x1=114
    x2=x1+14
    y1=500 # const
    y2= 500# const - height in -ve
    for i in range(len(vehicle_count)):
        constt=vehicle_count[i]*scaling_factor
        bar=Rectangle(Point(x1,y1), Point(x2,y2-constt))
        vehicle_count_per_hr=Text(Point(x1+9, y2-constt-15), f"{vehicle_count[i]}")
        vehicle_count_per_hr.setSize(8)
        vehicle_count_per_hr.setTextColor("dark blue")
        vehicle_count_per_hr.draw(win)
        x1+=33.33
        x2=x1+14
        bar.setFill("cyan")
        bar.draw(win)

    vehicle_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for row in range(row_length):
        if data_list[row][0] == "Elm Avenue/Rabbit Road":
            
            hour = int(data_list[row][2][:2])  # Extract the hour from the time column. [:2] takes the first 2 characters of the time string (HH)
            vehicle_count[hour] += 1  # Increment the count for that hour
    x1=100
    x2=x1+14
    y1=500 # const
    y2= 500# const - height in -ve
    for i in range(len(vehicle_count)):
        constt=vehicle_count[i]*scaling_factor
        bar=Rectangle(Point(x1,y1), Point(x2,y2-constt))
        vehicle_count_per_hr=Text(Point(x1+7, y2-constt-15), f"{vehicle_count[i]}")
        vehicle_count_per_hr.setSize(8)
        vehicle_count_per_hr.setTextColor("red")
        vehicle_count_per_hr.draw(win)
        x1+=33.33
        x2=x1+14
        bar.setFill("pink")
        bar.draw(win)
        


def legend(win):
    elm_legend= Rectangle(Point(50,50), Point(70,70))
    elm_legend.setFill("pink")
    elm_legend.draw(win)
    elm_text=Text(Point(200, 62), "Traffic at Elm Avenue/Rabbit Road")
    elm_text.draw(win)
    hanley_legend= Rectangle(Point(50,75), Point(70,95))
    hanley_legend.setFill("cyan")
    hanley_legend.draw(win)
    hanley_text=Text(Point(200, 88), "Traffic at Hanley Highway/Westway")
    hanley_text.draw(win)


def main(): # THE FIRST FUNCTION THAT IS EXECUTED 
    global data_list # using global variable data_list instead of creating a new variable with similar name inside the function
    global file_list # using global variable file_list to access the .csv filenames that are stored in it
    print(logo) # printing the ASCII art
    while True:
        file_,row_length=prerequisite() # calling function prerequisite() to check if the program has necessary dependencies to run properly. 

        datafile=f"\nThe data file selected is {file_}\n"

        var_total_vehicles_on_day=total_vehicles_on_day(row_length)                                              #
        var_total_trucks_on_day=total_trucks_on_day(row_length)                                                  #
        var_total_ev_on_day=total_ev_on_day(row_length)                                                          #
        var_total_two_wheelers_on_day=total_two_wheelers_on_day(row_length)                                      #
        var_total_buses_leaving_elm_North=total_buses_leaving_elm_North(row_length)                              #
        var_total_vehicles_straight_through=total_vehicles_straight_through(row_length)                          #
        var_percent_of_trucks_on_day=percent_of_trucks_on_day(row_length)                                        #
        var_average_bicycles_per_hr_on_day=average_bicycles_per_hr_on_day(row_length)                            # Calling functions for analysis, and storing the returned value in respective variables
        var_vehicles_overspeeding_on_day=vehicles_overspeeding_on_day(row_length)                                #
        var_vehicles_only_through_elm_on_day=vehicles_only_through_elm_on_day(row_length)                        #
        var_vehicles_only_through_hanley_on_day=vehicles_only_through_hanley_on_day(row_length)                  #
        var_percent_of_scooters_through_elm=percent_of_scooters_through_elm(row_length)                          #
        var_total_vehicles_during_peak_hr_at_hanley=total_vehicles_during_peak_hr_at_hanley(row_length)          #
        var_time_of_peak_at_hanley=time_of_peak_at_hanley(row_length)                                            #
        var_total_rainy_hrs=total_rainy_hrs(row_length)                                                          #

        print(datafile) # printing the name of the selected CSV file

        # I hope i dont need to explain the below print statements coz im lazy af rn 
        print(var_total_vehicles_on_day)                                                                      
        print(var_total_trucks_on_day)
        print(var_total_ev_on_day)
        print(var_total_two_wheelers_on_day)
        print(var_total_buses_leaving_elm_North)
        print(var_total_vehicles_straight_through)
        print(var_percent_of_trucks_on_day)
        print(var_average_bicycles_per_hr_on_day)
        print(var_vehicles_overspeeding_on_day)
        print(var_vehicles_only_through_elm_on_day)
        print(var_vehicles_only_through_hanley_on_day)
        print(var_percent_of_scooters_through_elm)
        print(var_total_vehicles_during_peak_hr_at_hanley)
        print(var_time_of_peak_at_hanley)
        print(var_total_rainy_hrs)

        # creating a variable that can store all this data in string format so that we can save the output to a file 
        results= datafile + var_total_vehicles_on_day + "\n" + var_total_trucks_on_day + "\n" + var_total_ev_on_day + "\n" + var_total_two_wheelers_on_day + "\n" + var_total_buses_leaving_elm_North + "\n" + var_total_vehicles_straight_through + "\n" + var_percent_of_trucks_on_day + "\n" + var_average_bicycles_per_hr_on_day + "\n" + var_vehicles_overspeeding_on_day + "\n" + var_vehicles_only_through_elm_on_day + "\n" + var_vehicles_only_through_hanley_on_day + "\n" + var_percent_of_scooters_through_elm + "\n" + var_total_vehicles_during_peak_hr_at_hanley + "\n" + var_time_of_peak_at_hanley + "\n" + var_total_rainy_hrs + "\n"
        save_results_to_file('results.txt', results) # call function to save this data to a file
        print("\nThe results have been successfully saved to results.txt") 
        
        # ok dont ask me how this works, i banged my head for 3 hours understanding the sh*t i wrote
        win = GraphWin("Histogram", 1000, 750) # 4:3 ratio 
        win.setBackground("white")
        title=Text(Point(304, 30), f"Histogram of vehicle frequency per hour ({data_list[0][1]})") # point(x,y) where x and y are the respective cordinates
        title.setSize(15) # dont even know if thats in px or rem lol
        title.setStyle("bold")
        title.draw(win) # places the title to the set cordinates in the app window

        legend(win) # calling function to display the legend
        x_axis = Line(Point(100,500), Point(900,500)) # this is the x-axis line
        x_axis.draw(win) # and im drawing the x-axis
        hour_margin=0 # ok this is complicated but hour_margin is just a left margin for the numbers on the x-axis. so, if the margin is 0, as it is here, the number will be displayed very left of the line.
        for i in range(24):
            numbering=Text(Point(116.6+hour_margin, 520), f"{i}")
            hour_margin+=33.33 # im adding this value so that the next number will be displaced to the right. this number is very special as the number line itself is 800 long and dividing it by 24 (hours) and doing some unholy maths somehow gives me this number.
            numbering.draw(win) 
        x_axis_label=Text(Point(500, 560), "Hours 00:00 to 24:00") # this is the number that will be displayed on the x-axis
        x_axis_label.setSize(10)
        x_axis_label.draw(win)
        draw_histogram(win,row_length) # function to draw histogram
        
        section2_height=Rectangle(Point(1,750), Point(1000,563)) # not needed by any means but just there to prevent me from getting anxiety and high blood pressure thinking that removing this will give an error even though i'm 100% sure that it'll be all right
        #section2_height.setFill("blue")     # erase the comment for debugging
        #section2_height.draw(win)           # erase the comment for debugging
        instructions = Text(Point(500, 656), "Click anywhere to close the window") # you heard the instruction. so dont click on close button to close the window popup. just click it!!!!
        instructions.draw(win)

        win.getMouse() # wait for mouse click! 
        win.close()

        # loop to re-execute the parts of code (mostly everything), but also with an option to close the program for good.
        while True:    
            option=input("\nDo you want to analyse data for another date? (Y/N)\nOption: ")
            if(option.lower()=="y" or option.lower()=="yes"):
                break # break will not break the program. it will just get out of the loop. and guess what? there is another big loop that will take control now.
            elif(option.lower()=="n" or option.lower()=="no"):
                print("\nClosing the program. Thank you!")
                quit() # i hate to use this !!!
            else:
                print("\nInvalid input. please enter either Y or N") # what a shame. you should have known better!!
main() # the program is calling the very first function which will be executed when the program runs.
