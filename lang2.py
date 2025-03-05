import asyncio
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
import re

# Initialize the Ollama model
llm = OllamaLLM(model="deepseek-r1:8b")

# Function to process the PDF and generate a response asynchronously
async def process_pdf_and_ask_question(pdf_path, exercise_question):
    # Load PDF file
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Combine text from all pages
    text = "\n".join([doc.page_content for doc in documents])

    # Define the prompt template for solving problems by searching chapter texts
    prompt_template = PromptTemplate.from_template(
        """SOLVING PROBLEMS BY SEARCHING chapters texts:     
        {exercise}

        
        Your response should be detailed and formatted clearly.
        """
    )

    # Format prompt
    prompt = prompt_template.format(exercise=exercise_question)

    # Query the LLM asynchronously
    response = await asyncio.to_thread(llm.invoke, prompt)

    # Remove <think>...</think> block from response
    clean_response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)
    
    return clean_response

# Load the default answers from markdown files
def load_default_answer(exercise_number):
    try:
        with open(f"{exercise_number}.md", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No default answer available."

# Streamlit UI elements
st.set_page_config(page_title="Samayun AI", page_icon="🤖")
st.title("Samayun AI")
st.subheader("পারলে টেকা!")

# Load profile image and info
st.sidebar.image("https://avatars.githubusercontent.com/u/31636535?v=4", use_column_width=True)
st.sidebar.write("**Samayun AI**")

# Default uploaded PDF path
pdf_path = "https://raw.githubusercontent.com/samayun/devbooks/refs/heads/master/Russell%20S.,%20Norvig%20P.%20Artificial%20intelligence-%20a%20modern%20approach%202nd%20edition.pdf"

# Function to display exercises
async def display_exercise(exercise_number, exercise_question, default_answer):
    st.header(f"Exercise {exercise_number}")
    st.markdown(exercise_question)

    # Display default answer
    st.subheader("AI's Default Solution")
    st.markdown(default_answer)

    # Input field to allow users to update the question
    exercise_question_updated = st.text_area(f"Update the question (Exercise {exercise_number})", exercise_question)
    
    if st.button(f"Regenerate Answer for Exercise {exercise_number}"):
        with st.spinner(f"Processing Exercise {exercise_number}..."):
            # Process the answer asynchronously
            response = await process_pdf_and_ask_question(pdf_path, exercise_question_updated)
        
        st.subheader(f"AI's Regenerated Solution for Exercise {exercise_number}")
        st.markdown(response)

# Exercise 3.1
exercise_question_3_1 = "Define in your own words the following terms: state, state space, search tree, search node, goal, action, successor function, and branching factor."
default_answer_3_1 = load_default_answer("3.1")

# Exercise 3.2
exercise_question_3_2 = "Explain why problem formulation must follow goal formulation."
default_answer_3_2 = load_default_answer("3.2")


# Tab functionality for different exercises
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Exercise 3.1", "Exercise 3.2", "Exercise 3.3", 
    "Exercise 3.6", "Exercise 3.7", "Exercise 3.8", "Exercise 3.12"
])


async def main():
    # Exercise 3.1
    with tab1:
        await display_exercise(3.1, exercise_question_3_1, default_answer_3_1)

    # Exercise 3.2
    with tab2:
        await display_exercise(3.2, exercise_question_3_2, default_answer_3_2)

    # Exercise 3.3
    exercise_question_3_3 = "Suppose that LEGAL-ACTIONS(~) denotes the set of actions that are legal in state s, and RESULT(^, s) denotes the state that results from performing a legal action a in state s. Define SUCCESSOR-FN in terms of LEGAL-ACTIONS and RESULT, and vice versa."
    default_answer_3_3 = load_default_answer("3.3")

    with tab3:
        await display_exercise(3.3, exercise_question_3_3, default_answer_3_3)

    # Exercise 3.6
    exercise_question_3_6 = "Does a finite state space always lead to a finite search tree? How about a finite state space that is a tree? Can you be more precise about what types of state spaces always lead to finite search trees?"
    default_answer_3_6 = load_default_answer("3.6")


    with tab4:
        await display_exercise(3.6, exercise_question_3_6, default_answer_3_6)

    # Exercise 3.7
    exercise_question_3_7 = """Give the initial state, goal test, successor function, and cost function for each of the following:
    a. You have to color a planar map using only four colors, in such a way that no two adjacent regions have the same color.
    b. A 3-foot-tall monkey is in a room where some bananas are suspended from the 8-foot ceiling. He would like to get the bananas. The room contains two stackable, movable, climbable 3-foot-high crates.
    c. You have a program that outputs the message 'illegal input record' when fed a certain file of input records. You know that processing of each record is independent of the other records. You want to discover what record is illegal.
    d. You have three jugs, measuring 12 gallons, 8 gallons, and 3 gallons, and a water faucet. You can fill the jugs up or empty them out from one to another or onto the ground. You need to measure out exactly one gallon."""
    default_answer_3_7 = load_default_answer("3.7")

    with tab5:
        await display_exercise(3.7, exercise_question_3_7, default_answer_3_7)

    # Exercise 3.8
    exercise_question_3_8 = """Consider a state space where the start state is number 1 and the successor function for state n returns two states, numbers 2n and 2n + 1.
    a. Draw the portion of the state space for states 1 to 15.
    b. Suppose the goal state is 11. List the order in which nodes will be visited for breadth-first search, depth-limited search with limit 3, and iterative deepening search.
    c. Would bidirectional search be appropriate for this problem? If so, describe in detail how it would work.
    d. What is the branching factor in each direction of the bidirectional search?
    e. Does the answer to (c) suggest a reformulation of the problem that would allow you to solve the problem of getting from state 1 to a given goal state with almost no search?"""
    default_answer_3_8 = load_default_answer("3.8")


    with tab6:
        await display_exercise(3.8, exercise_question_3_8, default_answer_3_8)

    # Exercise 3.12
    exercise_question_3_12 = """Prove that uniform-cost search and breadth-first search with constant step costs are optimal when used with the GRAPH-SEARCH algorithm. Show a state space with varying step costs in which GRAPH-SEARCH using iterative deepening finds a suboptimal solution."""
    default_answer_3_12 = load_default_answer("3.12")


    with tab7:
        await display_exercise(3.12, exercise_question_3_12, default_answer_3_12)

# Run the main function
asyncio.run(main())