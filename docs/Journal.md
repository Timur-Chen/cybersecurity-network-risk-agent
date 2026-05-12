New-Item -ItemType Directory -Path "docs" -Force | Out-Null

@'
# Project Report – Step 1

# Cybersecurity Network Risk Analyzer Agent

**Submission stage:** Step 1 – 24.04

| Field | Information |
|---|---|
| Student | Temur Tursunboev |
| Project type | Python-based AI/agent software system |
| GitHub repository | https://github.com/Timur-Chen/cybersecurity-network-risk-agent |

---

## 1. Short Description of the Planned System and Its Goal

The planned system is a Cybersecurity Network Risk Analyzer Agent. The purpose of this project is to create a Python-based agent system that helps users understand possible cybersecurity risks by analyzing network scan results.

The system will focus mainly on open ports and detected network services. In a real network, an open port does not automatically mean that a system is unsafe. However, some services can become risky if they are misconfigured, outdated, or exposed to users who should not have access. Because of this, the planned system will not only list detected ports, but will also explain what those findings may mean from a security point of view.

The user will provide either an existing Nmap scan result file or, if implemented safely later, a target such as localhost or an authorized private lab address. The system will process the scan data and return a structured cybersecurity risk report. The report will include detected services, risk levels, explanations, recommendations, and an overall conclusion.

The system is intended only for defensive and educational use. It will be developed and tested with sample scan files, localhost, or private lab environments where permission is available. The project is not intended for unauthorized scanning or offensive security activity.

---

## 2. Description of the AI or Agent-Based Approach

The project will use an agent-based approach. A central agent will control the main workflow of the system. The agent will receive the user input, validate it, call the required tool, process the returned scan data, and generate the final risk report.

The external tool will provide technical information such as host data, open ports, service names, protocols, and port states. Raw scan output is useful, but it can be difficult to understand for a beginner or for a user who is not familiar with cybersecurity terminology. The role of the agent is to interpret this technical data and convert it into practical guidance.

The agent will classify detected services into risk levels such as low, medium, high, or critical. It will also generate explanations and recommendations based on the detected services. For example, if the scan result shows an open Telnet service, the agent should classify it as a serious risk because Telnet does not use encrypted communication. If SSH is detected, the agent may classify it as medium risk and recommend strong authentication and restricted access. If a database service such as MySQL or PostgreSQL is detected, the agent may classify it as high risk if it appears exposed.

In this way, the tool will provide technical scan data, while the agent will interpret the data and turn it into a useful cybersecurity report. This makes the system more than a simple scanner because it provides explanations and recommendations instead of only displaying raw results.

The agent will use a rule-based expert-system approach for risk classification. Detected ports and services from the Nmap XML parser will be compared with a predefined cybersecurity risk rule set. Each rule will include a risk level, numeric score, explanation, and recommendation. The agent will choose the highest relevant risk score to calculate the overall risk level and will generate recommendations based on the matched service rules. This makes the AI component an intelligent decision-making layer that interprets raw scan data instead of only displaying it.

I can make the AI / agent approach clearer by specifying that the agent will use a rule-based expert-system method for decision-making. After the Nmap XML Parser Tool extracts open ports and services, the agent will compare each detected service with a predefined cybersecurity rule table. Each rule will contain the port number, service name, risk level, numeric score, explanation, and recommendation. For example, Telnet on port 23 will be classified as Critical because it is unencrypted, SSH on port 22 will be classified as Medium because it can be targeted by brute-force attacks, and MySQL on port 3306 will be classified as High because database services should not usually be exposed publicly. The agent will use the matched rules to generate recommendations and will calculate the overall risk level based on the highest detected risk score.

---

## 3. List of Tools That Will Be Used in the System

The main planned tool is an Nmap-based scan or scan-result processing tool. The system may support both scan-file analysis and optional safe live scanning.

### 3.1 Nmap Scan Tool

The Nmap Scan Tool may be used to run a safe scan on localhost or an authorized private lab target. The purpose of this tool is to collect network scan data in a structured format. If this mode is implemented, it will only be used in safe and permitted environments.

### 3.2 Nmap XML Parser Tool

The Nmap XML Parser Tool will process existing Nmap XML scan result files. It will extract useful information from the scan result, including host address, open ports, protocols, service names, and port states. This tool is important because it allows the system to be developed and tested safely without scanning external systems.

### 3.3 Risk Rule Tool

The Risk Rule Tool will map detected ports and services to risk levels and security recommendations. For example, services such as Telnet, FTP, MySQL, PostgreSQL, or RDP may require more attention depending on how they are exposed and configured. This tool will help the agent decide whether a detected service should be considered low, medium, high, or critical risk.

### 3.4 Report Writer Tool

The Report Writer Tool will save the final result in a structured format, such as JSON or a text report. This will make the output easier to review, store, and compare. The report will contain the main findings, risk levels, explanations, recommendations, and an overall conclusion.

The raw scan data will be in Nmap XML format. The Nmap Scan Tool will use Nmap’s XML output option, and the XML result will then be processed by the Nmap XML Parser Tool into structured Python data such as host address, open ports, protocols, service names, and port states.

---

## 4. Preliminary List of Programming Concepts Required

The project will require several programming concepts and software development practices. The preliminary concepts are listed below:

- Python functions for implementing separate tool behavior;
- object-oriented programming for the main agent class;
- modular programming for separating the agent, tools, utilities, tests, and documentation;
- command-line input handling;
- file handling for reading scan result files and writing reports;
- XML parsing for processing Nmap scan output;
- dictionaries and lists for storing structured scan data;
- input validation for checking file paths, file types, and possible target values;
- error handling for invalid files, unsupported formats, or XML parsing problems;
- subprocess usage if live Nmap scanning is implemented;
- JSON or text report generation;
- automated testing with pytest in later stages;
- Git and GitHub for version control;
- documentation through README and journal files.

The project will use Python’s built-in `argparse` library for handling command-line input. This library will allow the user to run the program with arguments such as `--file` for an existing Nmap XML scan result or `--target` for a safe live scan target. The `argparse` module will also help validate that the user provides the correct type of input and will display helpful usage instructions if the command is incorrect.

---

## 5. Current Progress

At this stage, the project is in the planning phase. The GitHub repository has been created, and the Step 1 planning documentation has been added. The next stage will focus on creating the Python project structure and implementing the first working components of the system.

---

## Step 1 Requirement Checklist

| Requirement | Included in this report |
|---|---|
| Short description of the planned system and its goal | Yes |
| Description of the AI or agent-based approach | Yes |
| List of tools that will be used in the system | Yes |
| Preliminary list of programming concepts required | Yes |

---

## Step 1 Evaluation Result

The Step 1 planning submission was evaluated on MISK.lv and received 19/20 points. The feedback stated that the project goal, agent-based approach, and programming concepts were clear. The main suggested improvement for the next stage is to further elaborate the implementation details of the Risk Rule Tool and explain how it will be populated and managed.
'@ | Set-Content -Path "docs\journal.md" -Encoding UTF8