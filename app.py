import streamlit as st
import random

# List of questions and point values
questions_and_points = [
    ('Name my two closest friends.',2),
    ('What is my favorite musical group, composer, or instrument?',2),
    ('What was I wearing when we first met?',2),
    ('Name one of my hobbies.',3),
    ('Where was I born?',1),
    ('What stresses am I facing right now?',4),
    ('Describe in detail what I did today, or yesterday.',4),
    ('When is my birthday?',1),
    ('What is the date of our anniversary?',1),
    ('Who is my favorite relative?',2),
    ('What is my fondest unrealized dream?',5),
    ('What is my favorite website?',2),
    ('What is one of my greatest fears or disaster scenarios?',3),
    ('What is my favorite time of day for lovemaking?',3),
    ('What makes me feel most competent?',4),
    ('What turns me on sexually?',3),
    ('What is my favorite meal?',2),
    ('What is my favorite way to spend an evening?',2),
    ('What is my favorite color?',1),
    ('What personal improvements do I want to make in my life?',4),
    ('What kind of present would I like best?',2),
    ('What was one of my best childhood experiences?',2),
    ('What was my favorite vacation?',2),
    ('What is one of my favorite ways to relax?',4),
    ('Who is my greatest source of support? (other than you)',3),
    ('What is my favorite sport?',2),
    ('What do I most like to do with time off?',2),
    ('What is one of my favorite weekend activities?',2),
    ('What is my dream getaway place?',3),
    ('What is my favorite movie?',2),
    ('What are some of the important events coming up in my life? How do I feel about them?',4),
    ('What are some of my favorite ways to work out?',2),
    ('Who was my best friend in childhood?',3),
    ('What is one of my favorite magazines?',2),
    ('Name one of my major rivals or "enemies."',3),
    ('What would I consider my ideal job?',4),
    ('What do I fear the most?',4),
    ('Who is my least favorite relative?',3),
    ('What is my favorite holiday?',2),
    ('What kinds of books do I most like to read?',3),
    ('What is my favorite TV show?',2),
    ('Which side of the bed do I prefer?',2),
    ('What am I most sad about?',4),
    ('Name one of my concerns or worries.',4),
    ('What medical problems do I worry about?',2),
    ('What was my most embarrassing moment?',3),
    ('What was my worst childhood experience?',3),
    ('Name two of the people I most admire.',4),
    ('Name my major rival or enemy.',3),
    ('Of all the people we both know, who do I like the least?',3),
    ('What is one of my favorite desserts?',2),
    ('What is my social security number?',2),
    ('Name one my favorite novels.',2),
    ('What is my favorite restaurant?',2),
    ('What are two of my aspirations, hopes, wishes?',4),
    ('Do I have a secret ambition? What is it?',4),
    ('What foods do I hate?',2),
    ('What is my favorite animal?',2),
    ('What is my favorite song?',2),
    ('Which sports team is my favorite?',2),
]

# Shuffle the questions
# random.shuffle(questions_and_points)

# Main function to run the Streamlit app
def main():
    # Use session state to keep track of the game state
    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.scores = [0, 0]
        st.session_state.player_names = ["", ""]
        st.session_state.random_numbers = [random.sample(range(1, 61), 10), random.sample(range(1, 61), 10)]
        st.session_state.current_question_index = 0

    # Step 0: Input player names
    if st.session_state.step == 0:
        st.title("Enter Player Names")
        st.session_state.player_names[0] = st.text_input("Player 1 Name:")
        st.session_state.player_names[1] = st.text_input("Player 2 Name:")
        if st.button("Next"):
            st.session_state.step = 1

    # Step 1: Welcome message
    if st.session_state.step == 1:
        st.title(f"Welcome {st.session_state.player_names[0]} and {st.session_state.player_names[1]}!")
        st.write("You are about to play \"The Love Map 20 Questions Game\".")
        st.write(f"{st.session_state.player_names[0]}: {', '.join(map(str, st.session_state.random_numbers[0]))}")
        st.write(f"{st.session_state.player_names[1]}: {', '.join(map(str, st.session_state.random_numbers[1]))}")
        if st.button("Let's get started!"):
            st.session_state.step = 2

    # Step 2: Game loop
    elif st.session_state.step == 2:
        current_player = st.session_state.current_question_index % 2
        question_number = st.session_state.random_numbers[current_player][st.session_state.current_question_index // 2]
        question, point_value = questions_and_points[question_number - 1]
        st.title(f"Question about {st.session_state.player_names[current_player]}:")
        st.write(question)

        # Answer buttons
        correct = st.button("Correct!")
        nope =  st.button("Nope.")
        if correct:
            st.session_state.scores[current_player] += point_value
            st.session_state.scores[(current_player + 1) % 2] += 1
        st.session_state.current_question_index += 1

        # Show scores
        st.write(f"Scores:\n{st.session_state.player_names[0]}: {st.session_state.scores[0]}\n{st.session_state.player_names[1]}: {st.session_state.scores[1]}")

        # Check if the game is over
        if st.session_state.current_question_index >= 20:
            st.session_state.step = 3

    # Step 3: Game over
    if st.session_state.step == 3:
        st.title("Game Over!")
        st.write(f"Final Scores:\n{st.session_state.player_names[0]}: {st.session_state.scores[0]}\n{st.session_state.player_names[1]}: {st.session_state.scores[1]}")

if __name__ == "__main__":
    main()
