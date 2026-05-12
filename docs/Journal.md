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



---

# Step 2 – 08.05

## 1. Updated Description of the System Based on Implementation Progress

At this stage, the project has moved from the planning phase to the first working implementation. The basic Python project structure has been created, and the main components of the Cybersecurity Network Risk Analyzer Agent have been implemented.

The current version of the system can receive an existing Nmap XML scan result file as input, validate the file, parse the scan data, identify open ports and detected services, classify the services by risk level, and generate a structured cybersecurity risk report.

The system now works as a local command-line application. A user can run the program with a command such as:

```bash
python src/main.py --file examples/sample_scan.xml
```
---

# Step 2 – 08.05

## 1. Updated Description of the System Based on Implementation Progress

At this stage, the project has moved from the planning phase to the first working implementation. The basic Python project structure has been created, and the main components of the **Cybersecurity Network Risk Analyzer Agent** have been implemented.

The current version of the system can receive an existing Nmap XML scan result file as input, validate the file, parse the scan data, identify open ports and detected services, classify the services by risk level, and generate a structured cybersecurity risk report.

The system now works as a local command-line application. A user can run the program with this command:

`python src/main.py --file examples/sample_scan.xml`

The system also supports a `--no-save` option if the user wants to display the result without saving a report file.

The current implementation focuses mainly on scan-file analysis. This is the safest and most controlled mode because it allows the system to be developed and demonstrated using sample Nmap XML files without scanning external systems.

An optional safe live scan mode has also been prepared through the Nmap Scan Tool. This mode is restricted to localhost or private IP addresses only. Public IP addresses are rejected by the validation logic to reduce the risk of unauthorized scanning.

The system currently includes:

- a command-line interface in `main.py`;
- a central agent class in `agent.py`;
- an Nmap XML Parser Tool in `tools/xml_parser.py`;
- an optional safe Nmap Scan Tool in `tools/nmap_tool.py`;
- a Risk Rule Tool in `risk_rules.py`;
- validation utilities in `utils/validators.py`;
- a Report Writer Tool in `utils/report_writer.py`;
- a sample Nmap XML file in `examples/sample_scan.xml`;
- a `requirements.txt` file for dependencies.

The first working version has already been manually checked by running the system with the sample XML file. The program correctly detected SSH, HTTP, and MySQL services, classified their risk levels, calculated the overall risk as **High**, and generated a structured result.

---

## 2. Refined List of Programming Concepts Actually Used

The programming concepts and libraries actually used in the implementation are:

- modular programming;
- object-oriented programming;
- command-line argument handling with `argparse`;
- XML parsing with `xml.etree.ElementTree`;
- file path handling with `pathlib`;
- dictionaries and lists for structured data;
- input validation;
- error handling with exceptions;
- rule-based expert-system logic;
- JSON report generation with `json`;
- date and time handling with `datetime`;
- optional external tool execution with `subprocess`;
- external command availability checking with `shutil`;
- Git and GitHub version control;
- basic dependency management through `requirements.txt`.

---

## 3. Explanation of How These Concepts Are Applied in the Project

Modular programming is used by separating the system into different files and folders. The command-line interface is placed in `main.py`, the main agent workflow is placed in `agent.py`, risk classification logic is placed in `risk_rules.py`, tool modules are placed in the `tools` folder, and utility modules are placed in the `utils` folder.

Object-oriented programming is used through the `CybersecurityRiskAgent` class. This class coordinates the main workflow of the system. It receives user input indirectly from the command-line interface, calls the required tools, processes the parsed scan data, applies risk rules, and builds the final report.

Command-line argument handling is implemented with Python's built-in `argparse` library. The user can provide an XML scan result file using the `--file` argument. The program also supports the `--no-save` option to display output without writing a report file. The optional `--target` argument is prepared for safe live scanning.

XML parsing is implemented with Python's built-in `xml.etree.ElementTree` library. The XML Parser Tool reads Nmap XML data and extracts the target address, open ports, protocols, service names, products, and port states. The parser then converts raw XML into Python dictionaries and lists.

File handling is implemented with `pathlib`. The validation utility checks whether the provided file exists, whether it is a real file, whether it has the `.xml` extension, and whether it is not empty.

Dictionaries and lists are used to represent structured scan data. For example, each detected open service is stored as a dictionary containing the host, port, protocol, state, service name, and product. The final report is also represented as a dictionary before it is displayed and saved.

Input validation is used in two areas. First, XML file input is validated before parsing. Second, optional live scan targets are validated to allow only localhost or private IP addresses. This supports safe and ethical use of the system.

Error handling is used to prevent the program from crashing without explanation. Invalid file paths, empty files, unsupported file types, broken XML content, missing Nmap installation, and unsafe live scan targets are handled with clear error messages.

Rule-based expert-system logic is used in the Risk Rule Tool. The system contains a predefined rule dictionary where common ports and services are mapped to risk levels, numeric scores, explanations, and recommendations. This directly addresses the Step 1 feedback that the Risk Rule Tool should be explained and developed more clearly.

JSON report generation is implemented with the `json` library. The Report Writer Tool saves the final cybersecurity risk analysis as a structured JSON file inside the `reports` folder.

The optional Nmap Scan Tool uses `subprocess` to call the external Nmap command-line tool if live scanning is used. It also uses `shutil.which()` to check whether Nmap is installed and available in the system PATH.

Git and GitHub are used for version control. The project has been developed through separate commits so that the implementation progress is visible.

---

## 4. Description of How Tools Are Integrated Into the System

The tools are integrated through the central agent workflow.

The first important tool is the **Nmap XML Parser Tool**. When the user provides an XML scan result file, the agent calls this parser. The parser validates and reads the XML file, extracts only open services, and converts the raw XML into structured Python data. This gives the agent a clean internal format to work with.

The second tool is the **Risk Rule Tool**. After the parser returns the detected services, the agent sends each service to the risk analysis logic. The Risk Rule Tool compares each open port with a predefined risk rule dictionary. Each rule contains a risk level, numeric score, reason, and recommendation. For example, port `22` is classified as Medium risk because SSH is commonly targeted by brute-force attempts, while port `3306` is classified as High risk because database services should not usually be exposed publicly.

The third tool is the **Report Writer Tool**. After the agent creates the final result, this tool saves the report as a JSON file. The report contains the detected services, risk information, overall risk score, conclusion, and original input information.

The optional fourth tool is the **Nmap Scan Tool**. If live scanning is used later, this tool will call the external Nmap command-line program and return XML output. That XML output will then be passed to the same XML Parser Tool, which keeps the internal data format consistent.

The agent connects all these tools together. The user does not need to manually parse XML, classify risks, or write reports. The agent controls the process and converts technical scan data into a meaningful cybersecurity report.

---

## 5. Step 2 Current Result

The current Step 2 implementation demonstrates that the system is no longer only a planned concept. It has a working command-line interface, working tool integration, a functioning risk rule system, structured output, and report generation.

The main working command is:

`python src/main.py --file examples/sample_scan.xml`

The current implementation successfully analyzes the sample scan file and produces a risk report for detected SSH, HTTP, and MySQL services.

The next stage will focus on formal testing, including functional tests, tool tests, input validation tests, error handling tests, and test scenarios with expected results.

---

## Step 2 Requirement Checklist

| Requirement | Included in this report |
|---|---|
| Updated description of the system based on implementation progress | Yes |
| Refined list of programming concepts actually used | Yes |
| Explanation of how these concepts are applied in the project | Yes |
| Description of how tools are integrated into the system | Yes |