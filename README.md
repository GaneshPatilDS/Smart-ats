
---

# Smart ATS 📄💼

Smart ATS is an application built to assist in improving resumes by leveraging Google's Gemini Pro AI. It functions as an Application Tracking System (ATS), providing evaluations of resumes based on job descriptions to enhance candidates' profiles.

## Features

- **PDF Resume Processing**: Users can upload PDF resumes for evaluation.
- **Job Description Analysis**: Users can input job descriptions to evaluate resumes against.
- **AI Evaluation**: The application utilizes Google's Gemini Pro AI to evaluate resumes based on job descriptions.
- **Detailed Feedback**: The app provides detailed feedback, including percentage match, missing keywords, and profile summary.

## Getting Started

To run Smart ATS locally, follow these steps:

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/GaneshPatilDS/Smart-ats.git
   cd smart-ats
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Create a `.env` file and add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage

1. Enter or paste the job description into the text area provided.
2. Upload a PDF resume using the file uploader.
3. Click the "Submit" button to initiate the evaluation process.
4. View the detailed feedback provided by Smart ATS.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Google Generative AI**: For resume evaluation using Gemini Pro AI.
- **PyPDF2**: For PDF file processing.
- **Python**: For application logic and backend processing.

## Acknowledgements

Special thanks to Google Generative AI for providing access to the Gemini Pro AI.

## Screenshots

![Screenshot 1](screenshot1.png)
![Screenshot 2](screenshot2.png)

---
