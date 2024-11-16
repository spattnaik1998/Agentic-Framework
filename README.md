# Agentic-Framework

# Overview

This repository provides an AI-powered solution for extracting and summarizing step-by-step instructions and relevant details from PDF documents related to business processes. The project leverages tools such as LlamaIndex, CREWAI, and CREWAI Tools to automate the process of retrieving and organizing information in a user-friendly format.

# Features

- PDF Analysis: Extracts text and tables from PDF documents for in-depth analysis.
- Step-by-step Instruction Retrieval: Provides detailed guidance on business processes.
- Comprehensive Summaries: Summarizes relevant content and tables into structured outputs.
- Agent-Based Architecture: Utilizes AI agents for targeted task handling, enhancing efficiency and output quality.
- Customizable Outputs: Supports output in different formats, such as generating new PDFs with results.

# Agents

SAP_tool:
Role: Researcher for extracting step-by-step instructions.
Goal: Retrieves business process steps from the PDF.
Backstory: Expert in business process explanations.
Features: Delegation allowed for further research.

SAP_summarizer:
Role: Blog writer for summarizing data.
Goal: Extracts and compiles relevant information and tables for a report.
Backstory: Specialist in creating detailed business process analyses.

Tasks:
Research Task: Extracts detailed steps for executing the specified business process.
Write Task: Summarizes the extracted information and tables into a comprehensive document.
