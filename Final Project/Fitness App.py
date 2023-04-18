import os
import tkinter as tk
from PIL import ImageTk

# initialize app
root = tk.Tk()
root.title("Fitness App")

# get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate x and y coordinates for the Tk root window
x = (screen_width / 2) - (750 / 2)
y = (screen_height / 2) - (1000 / 2)

# set the dimensions and position of the window
root.geometry('750x1000+{}+{}'.format(int(x), int(y)))

# background color
bg_color = "#000000"
# button color
button_color = "#ffffff"


# clear widgets
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# create a frame widget
frame = tk.Frame(root, width=750, height=1000, bg=bg_color)
frame1 = frame2 = frame3 = frame4 = frame5 = frame6 = frame7 = frame

for frame in (frame1, frame2, frame3, frame4, frame5, frame6):
    frame.grid(row=0, column=0)


# goal function and list
def set_goal(value):
    global goal, goal_image, routine, goal_type, tutorial, tutorial2, tutorial3
    goal = value
    # workouts
    if goal == "weight loss":
        goal_image = "weight loss.png"
        routine = ("Walk at 15% incline on treadmill", "Run outside", "Swim",
                   "Stairclimbers at level 50", "Jump rope", "Bike", "Elliptical machine")

        tutorial = ("Walk at 15% incline on treadmill",
                    "Run outside",
                    "Swim at your own pace",
                    "Set the stairclimbers to level 50 and walk",
                    "Jump rope",
                    "Ride a bicycle outside or use an exercise bike",
                    "Use an elliptical machine")

        tutorial2 = ("", "", "", "", "", "", "")
        tutorial3 = tutorial2
        goal_type = "minutes"

    elif goal == "strength training":
        goal_image = "strength training.jpg"
        routine = (
        "Barbell bench press and deadlift", "Dumbbell shoulder press, tricep pushdown, and dumbbell bicep curl",
        "Barbell back squat and box jumps", "Dumbbell fly and lat pulldown",
        "Shoulder press machine, tricep dip, and seated preacher curl",
        "Leg press machine and leg curl machine", "2 Exercises of choice")

        tutorial = ("Bench Press: Lie on a flat bench, hold the bar with a slightly wider than shoulder-width grip, "
                    "lower it to your chest, and push it back up. Repeat",
                    "Dumbbell Shoulder Press: Sit on a bench, hold dumbbells at shoulder level, press them straight up, lower them back down. Repeat",
                    "Barbell Back Squat: Stand under the bar on a squat rack, position it on your shoulders, stand with feet shoulder-width apart, "
                    "lower yourself into a squatting position, then stand back up. Repeat",
                    "Dumbbell Fly: Lie on a flat bench, hold dumbbells above your chest with arms extended and a slight bend in elbows, "
                    "lower the dumbbells to the sides of your chest, then raise them back up. Repeat",
                    "Shoulder Press Machine: Sit at the machine, adjust the seat to a comfortable height, grasp the handles with a neutral grip, "
                    "push them up and away from your shoulders, extend your arms fully, release back down. Repeat",
                    "Leg Press Machine: Sit on the machine with feet on footplate, push the plate away from you with your feet, "
                    "then release back to the starting position. Repeat",
                    "Choose any 2 exercises of choice. Repeat")

        tutorial2 = (
        "Deadlift: Stand with feet hip-width apart, bend down and grip the bar with your hands shoulder-width apart, "
        "lift the bar off the ground by straightening your hips and knees, then lower it back down. Repeat",
        "Tricep Pushdown: Stand in front of a cable machine, grasp the bar with an overhand grip, push it down "
        "towards your thighs, release back up. Repeat",
        "Box Jumps: Stand in front of a sturdy box or platform, jump onto it, then jump back down. Repeat",
        "Lat Pull Down: Sit at the machine, grasp the bar with a wide overhand grip, pull it down towards your chest while "
        "keeping your back straight, release back up. Repeat",
        "Tricep Dip: Position yourself between two parallel bars, lower yourself by bending your elbows until your arms form a 90-degree angle, "
        "push yourself back up. Repeat",
        "Leg Curl Machine: Lie face down on the machine, place your legs under the padded bar, curl your legs up towards your glutes, "
        "then release back down. Repeat",
        "")
        tutorial3 = ("",
                     "Dumbbell Bicep Curl: Stand with feet shoulder-width apart, hold dumbbells with palms facing forward, "
                     "curl them up towards your shoulders, lower back down. Repeat",
                     "",
                     "",
                     "Seated Preacher Curl: Sit on a preacher bench, with your upper arms resting on the pad and a dumbbell in your hand. "
                     "Curl the weight up towards your shoulders, then lower it back down. Repeat",
                     "",
                     "")
        goal_type = "reps"
    elif goal == "recreational":
        goal_image = "recreational.jpg"
        routine = ("Basketball", "Baseball", "Tennis", "Soccer", "Volleyball", "Skating", "Golf")
        tutorial = ("Play basketball by yourself or with a friend",
                    "Play baseball with a friend",
                    "Play tennis with a friend",
                    "Play soccer with by yourself or with a friend",
                    "Play volleyball with a friend",
                    "Go skating by yourself or with a friend",
                    "Go golfing by yourself or with a friend")

        tutorial2 = ("", "", "", "", "", "", "")
        tutorial3 = tutorial2
        goal_type = "minutes"


# stage function and calculation
def set_stage(value):
    global stage, stage_calculation
    stage = value
    stage_calculation = stage * 2


# days function
def set_days(value):
    global days
    days = value


# intensity function and calculation
def set_intensity(value):
    global intensity, intensity_calculation
    intensity = value
    intensity_calculation = int(intensity) * 2


# main frame function
def load_frame(current_frame, next_frame, image_file, title):
    clear_widgets(next_frame)
    current_frame.tkraise()
    current_frame.pack_propagate(False)
    # frame 1 widgets
    # get folder directory
    cwd = os.getcwd()
    logo_image = ImageTk.PhotoImage(file=os.path.join(cwd, image_file))
    logo_widget = tk.Label(current_frame, image=logo_image, bg=bg_color)
    logo_widget.image = logo_image
    logo_widget.pack(pady=20)
    # label
    tk.Label(current_frame, text=title, bg=bg_color, fg="white", font=("TkMenuFont", 24)).pack()


# add exercises button to frame 1 after survey
def add_exercise_button():
    tk.Button(
        frame1,
        text="Exercises", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: load_frame6()
    ).pack(pady=20)


# frame 1
# begin survey button
def load_frame1():
    load_frame(frame1, frame2, "dumbbell.jpg", "Fitness App")
    # new button
    tk.Button(
        frame1,
        text="New Survey", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: load_frame2()
    ).pack(pady=50)


# frame 2
def load_frame2():
    load_frame(frame2, frame3, "fitness.png", "Question 1")
    tk.Label(frame2, text="What is your fitness goal?", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(
        pady=20)
    # buttons
    tk.Button(
        frame2,
        text="Weight Loss", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: [load_frame3(), set_goal("weight loss")]
    ).pack(pady=20)

    tk.Button(
        frame2,
        text="Strength Training", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: [load_frame3(), set_goal("strength training")]
    ).pack(pady=20)

    tk.Button(
        frame2,
        text="Recreational", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: [load_frame3(), set_goal("recreational")]
    ).pack(pady=20)

    tk.Button(
        frame2,
        text="Back", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: load_frame1()
    ).pack(pady=120)


# frame 3
def load_frame3():
    load_frame(frame3, frame4, "stage.jpg", "Question 2")
    tk.Label(frame3, text="What stage are you in your fitness journey?", bg=bg_color, fg="white",
             font=("TkHeadingFont", 20)).pack(pady=20)
    # buttons
    tk.Button(
        frame3,
        text="Beginner", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: [load_frame4(), set_stage(1)]
    ).pack(pady=20)

    tk.Button(
        frame3,
        text="Intermediate", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: [load_frame4(), set_stage(2)]
    ).pack(pady=20)

    tk.Button(
        frame3,
        text="Advanced", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: [load_frame4(), set_stage(3)]
    ).pack(pady=20)

    tk.Button(
        frame2,
        text="Back", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: load_frame2()
    ).pack(pady=120)


# frame 4
def load_frame4():
    load_frame(frame4, frame5, "calendar.jpg", "Question 3")
    tk.Label(frame4, text="How many days per week would you like to exercise?", bg=bg_color, fg="white",
             font=("TkHeadingFont", 20)).pack(pady=20)
    # set default value
    global days
    days = 1
    # buttons and scale
    tk.Scale(
        frame3,
        font=("TkHeadingFont", 18),
        orient='horizontal',
        from_=1, to=7,
        cursor="hand2",
        length=300,
        width=50,
        command=set_days
    ).pack(pady=50)

    tk.Button(
        frame3,
        text="Enter", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: load_frame5()
    ).pack(pady=20)

    tk.Button(
        frame4,
        text="Back", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: load_frame3()
    ).pack(pady=105)


# frame 5
def load_frame5():
    load_frame(frame5, frame6, "scale.png", "Question 4")
    tk.Label(frame5, text="What would you like the intensity of your workout to be?", bg=bg_color, fg="white",
             font=("TkHeadingFont", 20)).pack(pady=20)
    # set default value
    global intensity, intensity_calculation
    intensity = 1
    intensity_calculation = 1.5
    # buttons and slider
    tk.Scale(
        frame5,
        font=("TkHeadingFont", 18),
        orient='horizontal',
        from_=1, to=5,
        cursor="hand2",
        length=300,
        width=50,
        command=set_intensity
    ).pack(pady=50)

    # enter button
    tk.Button(
        frame5,
        text="Enter", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: [load_frame1(), add_exercise_button()]
    ).pack(pady=20)
    # back button
    tk.Button(
        frame5,
        text="Back", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: load_frame4()
    ).pack(pady=105)


def load_frame6():
    load_frame(frame6, frame1, goal_image, "Exercise List")
    global string
    # loop through exercise list
    total = int(4 + stage_calculation + intensity_calculation)
    for i in range(0, int(days)):
        string = " for " + str(total) + " " + goal_type
        routine_text = routine[i] + string
        
        tk.Label(frame6, text=routine_text, bg=bg_color, fg="white",
                 font=("TkHeadingFont", 14)).pack(pady=5)
        # buttons
        tk.Button(
            frame6,
            text="View Exercise", bg=button_color,
            font=("TkHeadingFont", 14),
            cursor="hand2",
            # uses i=i to call the function at the time of clicking button instead of returning last value after loop
            command=lambda i=i: [load_frame7(i)]
        ).pack(pady=5)
    tk.Button(
        frame6,
        text="Back to Home", bg=button_color,
        font=("TkHeadingFont", 14),
        cursor="hand2",
        command=lambda: [load_frame1(), add_exercise_button()]
    ).pack(pady=40)

def load_frame7(i):
    exercise = "Exercise {}".format(i + 1)
    load_frame(frame7, frame6, goal_image, exercise)
    tk.Label(frame7, text=tutorial[i] + string + ".", bg=bg_color, fg="white",
             font=("TkHeadingFont", 18), wraplength=600).pack(pady=40)
    # removes blank tutorials
    if tutorial2[i] != "":
        tk.Label(frame7, text=tutorial2[i] + string + ".", bg=bg_color, fg="white",
                 font=("TkHeadingFont", 18), wraplength=600).pack(pady=40)
    if tutorial3[i] != "":
        tk.Label(frame7, text=tutorial3[i] + string + ".", bg=bg_color, fg="white",
                 font=("TkHeadingFont", 18), wraplength=600).pack(pady=40)
    # back button
    tk.Button(
        frame7,
        text="Back", bg=button_color,
        font=("TkHeadingFont", 18),
        cursor="hand2",
        command=lambda: load_frame6()
    ).pack(pady=20)


# load first frame and run app
load_frame1()
root.mainloop()
