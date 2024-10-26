# Hierarchical_Multiagent_System

Hierarchical Process Overview
By default, tasks in CrewAI are managed through a sequential process. However, adopting a hierarchical approach allows for a clear hierarchy in task management, where a ‘manager’ agent coordinates the workflow, delegates tasks, and validates outcomes for streamlined and effective execution. This manager agent can now be either automatically created by CrewAI or explicitly set by the user.

Key Features
Task Delegation: A manager agent allocates tasks among crew members based on their roles and capabilities.
Result Validation: The manager evaluates outcomes to ensure they meet the required standards.
Efficient Workflow: Emulates corporate structures, providing an organized approach to task management.
System Prompt Handling: Optionally specify whether the system should use predefined prompts.
Stop Words Control: Optionally specify whether stop words should be used, supporting various models including the o1 models.
Context Window Respect: Prioritize important context by enabling respect of the context window, which is now the default behavior.
Delegation Control: Delegation is now disabled by default to give users explicit control.
Max Requests Per Minute: Configurable option to set the maximum number of requests per minute.
Max Iterations: Limit the maximum number of iterations for obtaining a final answer.

Implementation : 

![image](https://github.com/user-attachments/assets/ce8d3000-b292-434d-b029-15eb0d3de4d9)


The crew comprises of :
1. Agents : 3 (research_analyst_agent , report_writer_agent , report_editor_agent)
2. Tasks : 4 (data_collection_task , data_analysis_task , report_writing_task , report_assessment_task )
3. Tools : 2 (SerperDevTool, ScrapeWebsiteTool)
4. Crew = Agents + Tasks + Tools + Manager_llm(since it's a hierarchical process )

Hyperparameters to play with : 

Agents : 
  max_iter=15,  # Optional
  max_rpm=None, # Optional
  max_execution_time=None, # Optional
  verbose=True,  # Optional
  allow_delegation=False,  # Optional

Crew : 
  manager_llm : i considered open ai model "gpt-4o-mini" . 

Steps to execute the project in VS code .

Step 1 : Download all the files 

Step 2 : Create a project and upload the files

Step 3 : run the requirements.txt file ( command : pip install -r requirements.txt ) . The application is build on python==3.12

Step 4 : update the .env file with the values : 

OPENAI_MODEL_NAME='gpt-4o-mini'
OPENAI_API_KEY='add your key'
SERPER_API_KEY='add your key'

Link to get the  keys : https://serper.dev  &   https://platform.openai.com/

Step 5 : Define the research topic 

# Define the input for the research topic ( i used 'The impact of AI on human health and longevity' as a topic , do update to topic of your choice )
    research_inputs = {
        'topic': 'The impact of AI on human health and longevity'
    }

Step 6 : Run the main.py file ( command : python main.py ) and you will see the magic in the console 

Sample output : i am not highlighting the execution process , chain of thought , delegation and all , only highlighting the final output 

**Comprehensive Research Report on the Impact of AI on Human Health and Longevity**

**1. Introduction**

**1. Introduction**
The integration of Artificial Intelligence (AI) in the healthcare sector has revolutionized medical service delivery, enhancing health outcomes and increasing efficiency within healthcare systems. This report critically evaluates the collected d**1. Introduction**
The integration of Artificial Intelligence (AI) in the healthcare sector has revolutionized medical service delivery, enhancing health outcomes and increasing efficiency within healthcare systems. This report critically evaluates the collected data concerning the impact of AI on human health and longevity, emphasizing emerging trends, benefits, and associated challenges.
The integration of Artificial Intelligence (AI) in the healthcare sector has revolutionized medical service delivery, enhancing health outcomes and increasing efficiency within healthcare systems. This report critically evaluates the collected data concerning the impact of AI on human health and longevity, emphasizing emerging trends, benefits, and associated challenges.

ata concerning the impact of AI on human health and longevity, emphasizing emerging trends, benefits, and associated challenges.

**2. Literature Review**
**2. Literature Review**
Numerous studies have highlighted AI's transformative role in healthcare. Research indicates that AI systems improve diagnostic accuracy, reduce time for patient evaluation, and facilitate personalized treatment plans. The literature also reflecNumerous studies have highlighted AI's transformative role in healthcare. Research indicates that AI systems improve diagnostic accuracy, reduce time for patient evaluation, and facilitate personalized treatment plans. The literature also reflects a growing focus on AI's predictive capabilities in preventive care, showcasing its potential for optimizing healthcare delivery.
ts a growing focus on AI's predictive capabilities in preventive care, showcasing its potential for optimizing healthcare delivery.


**3. Methodology**
**3. Methodology**
This report utilizes a qualitative analysis of existing research and data collected from healthcare institutions that have implemented AI technologies. Surveys and case studies were conducted to gather insights on the practical applications of AI, its effectiveness, and patient outcomes.

**4. Findings**
**4. Findings**
Key trends identified include:
Key trends identified include:
- **Increased Use of AI in Diagnostics**: AI algorithms are increasingly employed in medical imaging and pathology, resulting in faster and more accurate diagnoses.
- **Personalization of Treatment**: AI systems enable healthcare providers to tailor treatment plans based on individual patient data, enhancing overall patient care.
- **Personalization of Treatment**: AI systems enable healthcare providers to tailor treatment plans based on individual patient data, enhancing overall patient care.
- **Enhanced Efficiency in Healthcare Delivery**: The automation of administrative tasks allows medical staff to focus on patient care, significantly reducing waiting times.
- **Enhanced Efficiency in Healthcare Delivery**: The automation of administrative tasks allows medical staff to focus on patient care, significantly reducing waiting times.
- **Predictive Analytics for Preventive Care**: AI analyzes vast datasets to forecast potential health risks, allowing for timely interventions and better patient management.
- **Improvements in Drug Development**: AI accelerates the drug discovery process, indicating the possible effectiveness of compounds and reducing time-to-market for new medications.
- **Improvements in Drug Development**: AI accelerates the drug discovery process, indicating the possible effectiveness of compounds and reducing time-to-market for new medications.


**5. Discussion**
Despite AI's potential, several challenges must be addressed:
- **Data Privacy Concerns**: The use of sensitive patient data by AI systems raises significant privacy issues.
- **Bias in AI Algorithms**: To ensure equitable healthcare access, it is essential to address bias inherent in training data that could lead to unequal treatment outcomes.
- **Integration into Existing Systems**: AI solutions must overcome compatibility challenges with current healthcare infrastructures, which also necessitate proper staff training.

**6. Conclusion**
The application of AI in enhancing human health and longevity presents considerable promise, marked by efficiency improvements and better patient care. However, ethical considerations, data protection, and equitable access must govern these advancements. Ongoing research and open dialogue are vital for tackling challenges while maximizing AI's benefits in healthcare.

**References**
A complete bibliographic section should be included to cite all data and sources appropriately (APA or other formats as necessary).












  
  
  
