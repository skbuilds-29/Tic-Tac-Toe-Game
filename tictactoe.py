import streamlit as st
st.title("Play Tic-Tac-Toe!")
if "b" not in st.session_state:
    st.session_state.b = True
def rerun():
    st.session_state.b = True
    st.session_state.board = [""]*9
def turn(i):
    if st.session_state.board[i] != "" or check_win(st.session_state.board):
        return
    if st.session_state.b:
        symbol = "X"
    else:
        symbol = "O"
    st.session_state.b = not st.session_state.b
    st.session_state.board[i] = symbol
def check_win(board):
    if board[0]==board[1]==board[2]!= "":
        return True
    elif board[3]==board[4]==board[5]!= "":
        return True
    elif board[6]==board[7]==board[8]!= "":
        return True
    elif board[0]==board[3]==board[6]!= "":
        return Truei
    elif board[1]==board[4]==board[7]!= "":
        return True
    elif board[2]==board[5]==board[8]!= "":
        return True
    elif board[0]==board[4]==board[8]!= "":
        return True
    elif board[2]==board[4]==board[6]!= "":
        return True
    else:
        return False
if "board" not in st.session_state:
    st.session_state.board = [""]*9
with st.grid(3, wrap = False):
    for i in range (0,9):
        st.button(st.session_state.board[i],key=f'board{i}', width="stretch", wrap=True, on_click = turn, args = (i,))
if check_win(st.session_state.board):
    if st.session_state.b:
        st.success("Congratulations! O  won!")
    else:
        st.success("Congratulations! X won!")
elif "" not in st.session_state.board:
    st.write("It was a tie!")
if st.button("Play Again!"):
    rerun()
    st.rerun()
