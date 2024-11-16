# -*- coding: utf-8 -*-
"""Crew_AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dDFjY1-AYjmnlYVxJn7xooEJ520kohrc
"""

!pip install --upgrade llama-index

import os

mykey = ""
os.environ["OPENAI_API_KEY"] = mykey

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

from llama_index.llms import openai

!pip install crewai

from crewai import Agent

!pip install crewai_tools

from crewai_tools import PDFSearchTool

pdf_tool = PDFSearchTool('Business_Process_Documentation.pdf')

from crewai import Task

SAP_tool = Agent(
    role='Researcher from Business Process PDF documents',
    goal='get the step-by-step instructions for the business process {topic} from the pdf document',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in explaining business processes in a step-by-step manner."
    ),
    tools=[pdf_tool],
    allow_delegation=True
)

SAP_summarizer=Agent(
    role='Blog Writer',
    goal='Extract all the relevant information and tables about the relevant topic {topic} from the pdf document',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert at analyzing business process documents and returning the step-by-step execution of a business process."
    ),
    tools=[pdf_tool],
    allow_delegation=False
)

research_task = Task(
  description=(
    "Identify the business topic {topic}."
    "Get detailed step-by-step instruction to execute the business process."
  ),
  expected_output='A comprehensive long report outlining the table details along with the text based on the {topic} of pdf.',
  tools=[pdf_tool],
  agent=SAP_tool,
)

write_task = Task(
  description=(
    "get the relevant information from texts and tables on the topic {topic}."
  ),
  expected_output='Provide a step-by-step guide for the topic and return the relevant content.',
  tools=[pdf_tool],
  agent=SAP_summarizer,
  async_execution=False,
  output_file='new-blog-post.pdf'  # Example of output customization
)

from crewai import Crew, Process

crew = Crew(
  agents=[SAP_tool, SAP_summarizer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

result=crew.kickoff(inputs={'topic':'Business Process Improvement'})
