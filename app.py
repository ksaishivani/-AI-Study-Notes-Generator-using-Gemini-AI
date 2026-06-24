import streamlit as st
import google.generativeai as genai
import fitz

# ----------------------------
# Gemini API Key
# ----------------------------

genai.configure(api_key="AQ.Ab8RN6JzNDuroX84YR3nZw9bAFvVcVTA0wEhEK4KGEqGFoExBw")

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# PDF Text Extraction
# ----------------------------

def extract_pdf_text(pdf_file):

    text = ""

    pdf = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    return text

# ----------------------------
# Streamlit UI
# ----------------------------

st.title("📚 AI Study Notes Generator")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF Uploaded Successfully")

    if st.button("Generate Notes"):

        text = extract_pdf_text(uploaded_file)

        prompt = f"""
        Create study notes from:

        {text}

        Include:
        - Summary
        - Important Points
        - Key Concepts
        """

        response = model.generate_content(prompt)

        notes = response.text

        st.subheader("Generated Notes")

        st.write(notes)

        # Download Button

        st.download_button(
            label="📥 Download Notes",
            data=notes,
            file_name="study_notes.txt",
            mime="text/plain"
        )