import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai.process import Process

def main():
    load_dotenv()  # Load environment variables

    # Retrieve environment variables
    model_name = os.getenv("OPENAI_MODEL_NAME")
    api_key = os.getenv("OPENAI_API_KEY")
    serper_api_key = os.getenv("SERPER_API_KEY")

    # Ensure variables are loaded correctly
    if not model_name or not api_key or not serper_api_key:
        raise ValueError("Environment variables for OPENAI_MODEL_NAME, OPENAI_API_KEY, or SERPER_API_KEY are missing.")

    # Initialize the LLM model using OpenAI's GPT-4
    gpt = ChatOpenAI(
        model=model_name,
        verbose=True,
        temperature=0.5,
        openai_api_key=api_key
    )

    # Initialize SerperDevTool with the SERPER API key
    search_tool = SerperDevTool(api_key=serper_api_key)
    scrape_tool = ScrapeWebsiteTool()

    # Define agents
    research_analyst_agent = Agent(
        role="Research Analyst",
        goal="Create and analyze research points to provide comprehensive insights on various topics.",
        backstory="Specializing in research analysis, this agent employs advanced methodologies to generate detailed research points and insights.",
        verbose=True,
        allow_delegation=True,
        tools=[scrape_tool, search_tool],
        max_iter=3
    )

    report_writer_agent = Agent(
        role="Report Writer",
        goal="Compile the analyzed data into a comprehensive and well-structured research report.",
        backstory="You are skilled at transforming complex information into clear, concise, and informative reports.",
        verbose=True,
        allow_delegation=True,
        max_iter=5
    )

    report_editor_agent = Agent(
        role="Report Editor",
        goal="Review and refine research reports to ensure clarity, accuracy, and adherence to standards.",
        backstory="With a keen eye for detail and a strong background in report editing, this agent ensures that research reports are polished, coherent, and meet high-quality standards.",
        verbose=True,
        max_iter=5
    )

    # Define tasks
    data_collection_task = Task(
        description="Collect data from relevant sources about the given {topic}. Focus on identifying key trends, benefits, and challenges.",
        expected_output="A comprehensive dataset that includes recent studies, statistics, and expert opinions.",
        agent=research_analyst_agent,
    )

    data_analysis_task = Task(
        description="Analyze the collected data to identify key trends, benefits, and challenges for the {topic}.",
        expected_output="A detailed analysis report highlighting the most significant findings.",
        agent=research_analyst_agent,
    )

    report_writing_task = Task(
        description="Write a comprehensive research report that clearly presents the findings from the data analysis report.",
        expected_output="A well-structured research report that provides insights about the topic.",
        agent=report_writer_agent,
    )

    report_assessment_task = Task(
        description="Review and rewrite the research report to ensure clarity, accuracy, and adherence to standards.",
        expected_output="A polished, coherent research report that meets high-quality standards and effectively communicates the findings.",
        agent=report_editor_agent,
    )

    # Define the hierarchical crew with GPT-4 as the manager LLM
    research_crew = Crew(
        agents=[research_analyst_agent, report_writer_agent, report_editor_agent],
        tasks=[data_collection_task, data_analysis_task, report_writing_task, report_assessment_task],
        manager_llm=gpt,
        process=Process.hierarchical,
        verbose=True,
        respect_context_window=True,
        manager_agent=None,
        planning=True
    )

    # Define the input for the research topic
    research_inputs = {
        'topic': 'The impact of AI on human health and longevity'
    }

    # Start the research process
    result = research_crew.kickoff(inputs=research_inputs)
    print(result)

if __name__ == "__main__":
    main()
