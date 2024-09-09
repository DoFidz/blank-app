import streamlit as st
import time

if 'question' not in st.session_state:
    st.session_state['question'] = 1
if 'score' not in  st.session_state:
    st.session_state['score'] = 0

def question1():
    placeholder = st.empty()

    with placeholder.container():
        st.title("Quiz Matematika!")
        st.write("---")
        st.write("Selamat datang di quiz MATEMATIKA!!!!")
        st.write("Soal Pertama!")
        st.write("5x4 = ...")
    
        # Use a radio button to display the options
        choice = st.radio("Pilih Jawaban:", ['a. 25', 'b. 30', 'c. 20'], index=None, key='q1_choice')

        # Convert the user's choice to lowercase and check the answer
        if st.button("Submit", key='q1_submit'):
            if choice == 'a. 25':
                st.write("❌")
                time.sleep(1)
                placeholder.empty()
                st.session_state['question'] = 2
            elif choice == 'b. 30':
                st.write("❌")
                time.sleep(1)
                placeholder.empty()
                st.session_state['question'] = 2
            elif choice == 'c. 20':
                st.write("✔️")
                time.sleep(1)
                st.session_state['score'] += 1
                placeholder.empty()
                st.session_state['question'] = 2

def question2():
    placeholder1 = st.empty()

    with placeholder1.container():
        st.title("Quiz Matematika!")
        st.write("---")
        st.write("Soal Kedua!")
        st.write("8x8 = ...")
    
        # Use a radio button to display the options
        choice1 = st.radio("Pilih jawaban:", ['a. 64', 'b. 98', 'c. 72'], index=None, key='q2_choice')

        # Convert the user's choice to lowercase and check the answer
        if st.button("Submit", key='q2_submit'):
            if choice1 == 'a. 64':
                st.write("✔️")
                time.sleep(1)
                st.session_state['score'] += 1
                placeholder1.empty()
                st.session_state['question']  = 3
            elif choice1 == 'b. 98':
                st.write("❌")
                time.sleep(1)
                placeholder1.empty()
                st.session_state['question']  = 3
            elif choice1 == 'c. 72':
                st.write("❌")
                time.sleep(1)
                placeholder1.empty()
                st.session_state['question']  = 3

def question3():
    placeholder2 = st.empty()

    with placeholder2.container():
        st.title("Quiz Matematika!")
        st.write("---")
        st.write("Soal Terakhir!")
        st.write("6x7 = ...")
    
        # Use a radio button to display the options
        choice2 = st.radio("Pilih jawaban:", ['a. 42', 'b. 24', 'c. 58'], index=None, key='q3_choice')

        # Convert the user's choice to lowercase and check the answer
        if st.button("Submit", key='q3_submit'):
            if choice2 == 'a. 42':
                st.write("✔️")
                time.sleep(1)
                st.session_state['score'] += 1
                placeholder2.empty()
                st.session_state['question']  = 4
            elif choice2 == 'b. 24':
                st.write("❌")
                time.sleep(1)
                placeholder2.empty()
                st.session_state['question']  = 4
            elif choice2 == 'c. 58':
                st.write("❌")
                time.sleep(1)
                placeholder2.empty()
                st.session_state['question']  = 4

def question4():
    placeholder3 = st.empty()

    with placeholder3.container():
        st.title("Anda Menyelsaikan Quiznya!")
        st.write("---")
        st.write(f"Skor Anda Adalah {st.session_state['score']}" + "/3.")

        if st.button("Redo"):
            placeholder4 = st.empty()

            with placeholder4.container():
                st.session_state['score'] = 0
                st.session_state['question']  = 1
        st.markdown('<p style="color:gray;font-size:12px;">Redo The Questions? Click The Redo Button x2 If You Want!</p>', unsafe_allow_html=True)

if st.session_state['question'] == 1:
    question1()
if st.session_state['question'] == 2:
    question2()
if st.session_state['question'] == 3:
    question3()
if st.session_state['question'] == 4:
    question4()