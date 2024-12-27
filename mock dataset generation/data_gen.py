import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
EXTERNAL_USER_ID = "user"

def get_llm_response(system_query=None, user_query=None):
    create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
    create_session_headers = {
        'apikey': OPENAI_API_KEY
    }
    create_session_body = {
        "pluginIds": [],
        "externalUserId": EXTERNAL_USER_ID
    }

    response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)
    response_data = response.json()
    session_id = response_data.get('data', {}).get('id')

    if session_id:
        print("Success!! Session created!")
        if system_query:
            system_prompt_body = {
                "endpointId": "predefined-openai-gpt4o",
                "query": system_query,
                "pluginIds": [],
                "responseMode": "sync",
                "modelConfigs": { "temperature": 0 },
                "role": "system"
            }
        
            system_prompt_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
            system_prompt_headers = {
                'apikey': OPENAI_API_KEY
            }
        
            requests.post(system_prompt_url, headers=system_prompt_headers, json=system_prompt_body)
            print("System prompt made.")
        
        if user_query:
            while True:
                query_body = {
                    "endpointId": "predefined-openai-gpt4o",
                    "query": user_query,
                    "pluginIds": [],
                    "responseMode": "sync",
                    "modelConfigs": { "temperature": 0 }
                }
            
                submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
                submit_query_headers = {
                    'apikey': OPENAI_API_KEY
                }
        
                query_response = requests.post(submit_query_url, headers=submit_query_headers, json=query_body)
                query_response_data = query_response.json()

                if query_response.status_code == 200:
                    print("Query response received")
                    return query_response_data["data"]["answer"]
        
    else:
        print("Failed to create chat session.")

mentor_attributes = ["Expertise", "Weaknesses", "Interests", "Teaching Style", "Professional Goals", "Availability"]

_format = """{
    "mentor_id": {
        "Expertise": ["<areas_of_expertise>"],
        "Weaknesses": ["<areas_for_improvement>"],
        "Interests": ["<list_of_interests>"],
        "Teaching Style": "<learning_style>",
        "Professional Goals": ["<list_of_goals>"],
        "Availability": "<availability_in_hours_or_days>"
    }
}
"""

USER_PROMPT = f"""
You are tasked with creating a mock dataset of mentors based on the following attributes: {mentor_attributes}.

**Instructions**:
- Generate a dataset of 10 mentors with diverse profiles.
- The dataset must represent mentors from various regions (e.g., North America, Middle East, Asia, Europe, Africa, Australia).
- Each mentor should have realistic and unique attributes. Avoid placeholder names like "John Doe" or "Jane Doe."
- For each mentor, ensure:
    - **Expertise**: Includes 3-5 areas of professional expertise.
    - **Weaknesses**: Lists 3-5 areas where the mentor feels less confident or avoids providing guidance.
    - **Interests**: Mentions 3-5 fields or topics the mentor enjoys exploring or is passionate about.
    - **Teaching Style**: Describes their preferred teaching or mentoring approach (e.g., hands-on, conceptual, collaborative).
    - **Professional Goals**: Contains 3-5 realistic long-term aspirations or career objectives.
    - **Availability**: Specifies realistic time availability in hours, days, or specific schedules (e.g., weekends, weekday evenings).

**Constraints**:
- Ensure cultural diversity in the mentor names and profiles.
- Attribute lists (e.g., Expertise, Weaknesses) must have 3-5 elements for each mentor.
- The dataset should be as real as possible and formatted strictly in the example JSON format provided.

**Output**:
- Return the dataset as a formatted JSON object, following this example:
{_format}

**Reminder**:
- Do not include explanations or extra text in the output.
- Only return the formatted JSON object.
"""


SYSTEM_PROMPT = f"""
You are an experienced academician who has mentored multiple students and knows a lot of co-mentors. Your goal is to generate a **mock dataset of mentors with their attributes**.

**Attrbiutes**:  
1. Expertise
2. Weaknesses
3. Interests
4. Teaching Style
5. Professional Goals
6. Availability

**Descriptions**:  
1. **Expertise**:The specific areas of knowledge or skills where the mentor excels and can provide guidance to students. This includes academic subjects, technical skills, and professional expertise.
2. **Weaknesses**:Areas where the mentor feels less confident or prefers not to provide guidance. This can include topics or skills outside their specialization.
3. **Interests**:Topics or fields that the mentor is curious about or enjoys exploring, even if they are not directly related to their expertise.
4. **Teaching Style**:The mentor’s preferred approach to teaching or guiding students. This includes their pedagogical methods and interaction style.
5. **Professional Goals**:The mentor’s long-term career aspirations or objectives that align with their current role and expertise.
6. **Availability**:The amount of time and schedule constraints the mentor has for providing guidance or mentoring students.


Some examples are as follows, you can add more if you want:
1. **Expertise**:
- Data Science, Machine Learning, Python Programming
- Physics, Astrophysics, Computational Modeling
- Marketing Strategies, Business Analytics, Public Speaking

2. **Weaknesses**
- Artistic Creativity, Fine Arts
- Advanced Theoretical Physics, String Theory
- Advanced Finance Concepts, Derivatives Trading


3. **Interests**
- Reading about Quantum Mechanics, Learning Guitar, Blogging
- Exploring Sustainable Energy Solutions, Photography, Gardening
- Experimenting with AI Art, Traveling, Learning New Languages


4. **Teaching Style**
- Hands-on Approach, Practical Demonstrations, Real-World Projects
- Conceptual Explanations, Detailed Discussions, Step-by-Step Guidance
- Group Sessions, Peer-Learning Advocacy, Collaborative Problem-Solving

5. **Professional Goals**
- Publish Research Papers on Deep Learning, Become a Senior Data Scientist
- Start an EdTech Venture, Design AI-powered Learning Systems
- Become a Thought Leader in Marketing, Conduct Workshops Worldwide

6. **Availability**
- Available on Weekends, 2 hours per session
- Evening Hours (6 PM - 9 PM), Flexible on Public Holidays
- 1 Hour Daily (Monday-Friday), Not Available on Weekends
"""

if __name__ == "__main__":
    for i in range(30):
        response = get_llm_response(system_query=SYSTEM_PROMPT, user_query=USER_PROMPT)
        response = response.replace("```json", "").replace('```', '')
        # print(response)
        try:
            resp = json.loads(response)
            with open(f'datasets/dataset_{i+1}.json', 'w') as f:
                json.dump(resp, f)
            print(f"Dataset {i+1} created and saved successfully.")
        except:
            print(f"Failed iteration {i+1}. Continuing....")
            continue

    # response = get_llm_response(system_query=SYSTEM_PROMPT, user_query=USER_PROMPT)
    # response = response.replace("```json", "").replace('```', '')
    # print(response)