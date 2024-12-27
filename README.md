# **AI POWERED MENTOR MENTEE MACHING SYSTEM**

## **Overview**
This project aims to develop an AI-powered system for alloting the right mentors to students based on sharesd interests, alignment of goals, mentor availability. It leverages a encoded vector based similaity searching technique. BERT's advanced encoding technique helps make the vectors contextually rich and appropriate.

---

## **Implementation Details**
1. **Mock Dataset Generation**:
    - Generated mock dataset of 300 mentors with 6 key attributes.
        - Expertise
        - Weaknesses
        - Interests
        - Teching Style
        - Professional Goals
        - Availability

    - All the attibutes are a key indicator of a mentor profile. With carefully crafted prompts to GPT-4o model, a pseudo-realistic dataset was crafted.

    - Combining this dataset with student dataset from the [AI-powered-personalised-learning-path-for-students task](https://github.com/coder-utkarshchaudhary/AI-powered-personalised-learning-path-for-students.git), we get two rich datasets containing explicit information about students and mentors.

2. **Feature Engineering**:
    - Explicit feature engineering is done on both student and mentor datasets.
    - This adds more information about an object (read: students and mentors) and help make the vectors more information rich.

3. **Vector DB powered similarity search**:
    - [Google's BERT](https://huggingface.co/docs/transformers/en/model_doc/bert) model is used to encode the textual database into vector collections with the schema
    ```plaintext
    {"id" : <vector_representation>}
    ```
    - The solution involves the use of MilvusDB to store these vectors. MilvusDB provides in-built similarity search techniques that can be used to find the perfect mentor for each student.

---

## **How to Run?**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/coder-utkarshchaudhary/AI-powered-mentor-mentee-matching-system.git 
   cd AI-powered-mentor-mentee-matching-system
   ```

2. **Install Dependencies**:
   Ensure `pip` is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
   <i><b>NOTE: This is only needed if you want to make a new dataset from scratch.</b></i>

4. **Run the project**:
   In the ```main.ipynb``` file, press Run All.
   <i><b>NOTE:<br>1. Ensure that you have a GPU to run BERT tokenizer.<br>2. BERT tokenizer takes some tme to download, so allow the notebook to run completely.</b></i>

---

## **Final Submission**
- **Codebase**: [Link to GitHub repository](https://github.com/coder-utkarshchaudhary/AI-powered-mentor-mentee-matching-system.git)
- **Technical Document**: [Link to project report](https://docs.google.com/document/d/1U4k_Bzr_40DBIplSuO9Fs8wz9nGNRPyxr0QXCobkv8g/edit?usp=sharing)

---

## **Notes**
1. This project uses GPT-4o model. The model's API is access via On-Demand platform. The code will not directly work for OpenAI API calls directly. Please modify the ```get_llm_response``` function in ```datagen.py```.

2. BERT needs a GPU for faster inference. On each run, the BERT configurations download from huggingface. Be patient while the model is downloading.

    #### Future Scope:
    1. A RAG system can be incorporated on mentor and student datasets for Agent powered mentor-mentee matching.
    2. Implementation of ML models like Linear Regression, XGBoost, ANNs etc. for assigning custom weights to custom embeddings generated using BERT.
    3. Implementation of a UI system with user input importance for search criteria.

---

## **Acknowledgement**
Thanks to the open-source libraries and tools used in this project --> OpenAI, MilvusDB, Torch, Huggingface and On-Demand.<br>
This project was made as a part of the **Alcovia Intern Optional Task - 1**. I extend a heartfelt thank you to the Alcovia team for providing me this opportunity.

---

## **License**
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute this software, provided proper attribution is given.