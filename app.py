# Line 1-3: Import the required external libraries
import streamlit as st
import pandas as pd
import os

# Line 5-6: Configure the browser tab title and app icon
st.set_page_config("Anudip Chatbot", page_icon=":book")

# Line 8-12: Safely check for and display the main header logo image
if os.path.exists("AnudipLogoWithGit_Update_3.png"):
    st.image("AnudipLogoWithGit_Update_3.png")
else:
    st.warning("Logo image 'AnudipLogoWithGit_Update_3.png' missing from repository.")

# Line 14-16: Define and display the hyperlinked text for booking a SPOC slot
SPOC_SLOT_BOOK_LINK = "[CLICK HERE TO BOOK SPOC SLOT](https://bookslotapp.streamlit.app/)"
st.markdown(SPOC_SLOT_BOOK_LINK, unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---

# Line 21-28: Define a reusable function to load CSV files safely with error catching
def load_data(file_name):
    """Safely loads CSV files and handles errors gracefully."""
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        st.error(f"Error: The file '{file_name}' was not found. Please ensure it is uploaded to your GitHub repository.")
        return None

# Line 30-39: Query the active dataframe to return the Answer text and PicturePath
def get_answer(question, data):
    """Finds the corresponding answer and file path for a given question."""
    answer_row = data[data['Question'] == question]
    if not answer_row.empty:
        answer = answer_row.iloc[0]['Answer']
        picture_path = answer_row.iloc[0]['PicturePath']
        return answer, picture_path
    else:
        return "I'm sorry, I don't know the answer to that question.", None

# Line 41-53: Fix directory paths across Windows/Linux architectures and check for image validity
def display_image_safely(picture_path):
    """Normalizes paths for Linux compatibility and checks file existence before loading."""
    if picture_path and pd.notna(picture_path):
        # Crucial Fix: Converts Windows backslashes (\) to standard cross-platform forward slashes (/)
        clean_path = str(picture_path).strip().replace('\\', '/')
        
        if os.path.exists(clean_path):
            st.image(clean_path, caption='', use_container_width=True)
        else:
            st.error(f"⚠️ Image File Missing: The application is trying to look for **'{clean_path}'**, but it does not exist in your repository folder. Please check your filename casing and paths.")
    else:
        st.warning("No picture available for this answer.")


# --- DEPARTMENT/OPTION FUNCTIONS ---

# Line 58-69: Placement UI container module
def Placement():
    st.title("Placement")
    data = load_data("data.csv")
    if data is not None:
        user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique(), key="sb_placement")

        if st.button("Get Answer", key="btn_placement"):
            answer, picture_path = get_answer(user_question, data)
            st.markdown(f"**Answer:** {answer}")
            display_image_safely(picture_path)

# Line 71-82: Enrollment UI container module
def Enrollment():
    st.title("Enrollment")
    data = load_data("dataen.csv")
    if data is not None:
        user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique(), key="sb_enrollment")

        if st.button("Get Answer", key="btn_enrollment"):
            answer, picture_path = get_answer(user_question, data)
            st.markdown(f"**Answer:** {answer}")
            display_image_safely(picture_path)

# Line 84-95: Certificate UI container module
def certificate():
    st.title("Certificate")
    data = load_data("datacerti.csv")
    if data is not None:
        user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique(), key="sb_cert")

        if st.button("Get Answer", key="btn_cert"):
            answer, picture_path = get_answer(user_question, data)
            st.markdown(f"**Answer:** {answer}")
            display_image_safely(picture_path)

# Line 97-108: Finance UI container module
def FinanceDepartment():
    st.title("Finance Department")
    data = load_data("datafi.csv")
    if data is not None:
        user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique(), key="sb_finance")

        if st.button("Get Answer", key="btn_finance"):
            answer, picture_path = get_answer(user_question, data)
            st.markdown(f"**Answer:** {answer}")
            display_image_safely(picture_path)

# Line 110-121: SPOC Details UI container module
def spoc():
    st.title("M&E SPOC")
    data = load_data("datasp.csv")
    if data is not None:
        user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique(), key="sb_spoc")

        if st.button("Get Answer", key="btn_spoc"):
            answer, picture_path = get_answer(user_question, data)
            st.markdown(f"**Answer:** {answer}")
            display_image_safely(picture_path)

# Line 123-136: Reports & External Links module
def link():
    st.title("Reports")
    data = load_data("datali.csv")
    if data is not None:
        user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique(), key="sb_link")

        if st.button("Get Answer", key="btn_link"):
            link_row = data[data['Question'] == user_question]
            if not link_row.empty:
                report_link = link_row.iloc[0]['Link']
                st.markdown(f"[View Report]({report_link})", unsafe_allow_html=True)
            else:
                st.warning("No link available for this question.")


# --- NAVIGATION LOGIC ---

# Line 141-142: Render the primary Department dropdown selector
department = st.selectbox("Select Department :", ("M&E Department",), key="sb_dept_main")

# Line 144-156: Evaluate user choice and call the matching function to render specific layout options
if department == "M&E Department":
    selection = st.selectbox("Select Option :", ("Placement Parameters", "Enrollment Parameters", "M&E SPOC Details", "Certificate Process", "Reports"), key="sb_selection_main")
    if selection == "Placement Parameters":
        Placement()
    elif selection == "Enrollment Parameters":
        Enrollment()
    elif selection == "M&E SPOC Details":
        spoc()
    elif selection == "Certificate Process":
        certificate()
    elif selection == "Reports":
        link()

# Line 158-159: Output the Google Form query hyperlink at the absolute bottom of the application
google_form_link_query = "[For Other Query Please Fill This Form](https://forms.gle/zsf1S146zbaaHuiWA)"
st.markdown(google_form_link_query)