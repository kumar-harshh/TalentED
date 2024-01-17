# TalentED: Personal ATS for Job-Seekers & Recruiters

Welcome to **TalentED 😎**, your Personal Applicant Tracking System for both Job-Seekers and Recruiters. This Streamlit application is designed to help you evaluate resumes against specific job descriptions efficiently. 

## Features

- **Animated Introduction**: Enjoy a captivating introduction with an animated illustration that sets the tone for TalentED.
  Note: This beautiful Animation is downloaded as JSON from (https://lottiefiles.com/) and is used in the code as animation.json:
  
  ![Animation - 1705515758529](https://github.com/kumar-harshh/TalentED/assets/88376961/039fb7aa-a701-4267-8259-7141017b19d8)

  
- **Job Role and Description Input**: Input the desired job role and paste the job description to tailor the evaluation process.

- **Resume Upload**: Upload your resume in PDF format using the file uploader. Ensure that the uploaded file is a PDF for accurate processing.

- **ATS Scanner Dashboard**: Get a comprehensive evaluation of your resume with the ATS Scanner Dashboard, providing insights into the percentage match, missing keywords, and a profile summary.

## Getting Started

**Recommendations**
- Use a virtual environment in order to avoid "library-pollution" in your system. It's just few commands:
  - Navigate to your project directory & based on your system(Windows/Mac) Use the command
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  ```
- Keep all your secret in .env file-Shhhhhh! No One Should Know your API Keys
- Use .gitignore with standard python template-It's Just a google search away


1. **Installation:**
    ```bash
    pip install streamlit google.generativeai PyPDF2 python-dotenv streamlit-lottie
    ```

2. **API Configuration:**
    - Obtain a Google API key and store it in a `.env` file as `GOOGLE_API_KEY=your_api_key`.
    - If not created already, Get your API Key here: (https://makersuite.google.com/app/apikey)
  
3. **Run the Application:**
    ```bash
    streamlit run your_app_filename.py
    ```
    Replace `your_app_filename.py` with the name of your Python script containing the provided code.

4. **Usage:**
    - Enter the job role and paste the job description.
    - Upload your resume in PDF format.
    - Click the "Submit" button to initiate the evaluation process.

5. **Results:**
    - View the percentage match, missing keywords, and profile summary in the ATS Scanner Dashboard.

## Example

Here's an example of how to use the application:

```python
# Replace 'app.py' with your actual filename
streamlit run app.py
```

## Dependencies

- [Streamlit](https://www.streamlit.io/)
- [Google Generative AI](https://cloud.google.com/ai-platform/training/docs/algorithms/gpt)
- [PyPDF2](https://pythonhosted.org/PyPDF2/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [streamlit-lottie](https://github.com/streamlit/streamlit-lottie)

## Note

Make sure to keep your Google API key secure and do not share it publicly.

**Disclaimer:** This application relies on Google Gemini's API which has a limit of 60 req per second. Ensure that you comply with the terms of service for each dependency.

Feel free to customize and enhance this application according to your needs! Happy Coding! 🚀
