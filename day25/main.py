
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_name = turtle.Turtle()
state_coor = pandas.read_csv("50_states.csv")
states = state_coor.state.to_list()
right_guess = 0
game_is_on = True
popup_title = "Guess the state"
while game_is_on:
   
    answer_state = screen.textinput(title=popup_title, prompt="What is another state name").title()

    
    if answer_state in states:
        row = state_coor[state_coor.state == answer_state]
        state_name.penup()
        x_cor = row.x.item()
        y_cor = row.y.item()
        state_name.goto(x_cor, y_cor)
        state_name.write(answer_state, align= "center", font=('Arial', 10, 'normal'))
        right_guess += 1
        popup_title = f"You guessed {right_guess} of 50 states"
        states.remove(answer_state)
    if answer_state == "Exit":
        game_is_on = False
        rest_states = pandas.DataFrame(states)
        rest_states.to_csv("states to Learn.csv")

        print(f"States to learn!!\n{states}")



# turtle.mainloop()

# alaska_row = state_coor[state_coor.state == "Alaska"]
# x = alaska_row.x
# y = alaska_row.y