
```markdown
# Project Journal

## Step 1 – 24.04

### Planned System and Goal

The planned system is a **Cybersecurity Network Risk Analyzer Agent**. The goal of the system is to help users understand possible cybersecurity risks by analyzing network scan results. The system will focus on open ports and detected services and will generate a structured risk analysis with explanations and recommendations.
In many real network environments, open services may create security risks if they are misconfigured, outdated, or exposed to users who should not have access. For this reason, the system will not only list detected ports, but will also explain what the detected services may mean from a security point of view.
The planned system will be implemented in Python and will be prepared as a local command-line application. The user will provide either an existing Nmap scan result file or, if implemented safely, a target such as localhost or an authorized private lab address. The system will then process the scan data and return a clear report.
The project is intended only for defensive and educational use. It will not be used for unauthorized scanning. The system will be tested with sample scan files, localhost, or private lab environments where permission is available.

### AI or Agent-Based Approach

The project will use an agent-based approach. A central agent will control the workflow of the system. The agent will receive the user input, validate it, call the required tool, process the returned scan data, and generate a final cybersecurity risk report.

The external tool will provide technical data such as host information, open ports, service names, and port states. However, raw scan data alone is often difficult for a beginner or non-specialist user to understand. The agent will add value by interpreting this technical information and converting it into understandable conclusions.
The agent will classify detected services into risk levels such as low, medium, high, or critical. It will also generate explanations and recommendations. For example, if the scan result shows an open Telnet service, the agent should classify it as a serious risk because Telnet does not provide encrypted communication. If the scan result shows an open SSH service, the agent may classify it as medium risk and recommend strong authentication and limited access.
The main idea is that the tool collects or provides technical scan data, while the agent interprets that data and turns it into practical security guidance.

### Planned Tools

The main planned tool is an **Nmap-based scan or scan-result processing tool**.
The planned tools are:

1. **Nmap Scan Tool**

   This tool may be used to run a safe scan on localhost or an authorized private lab target. The purpose of this tool is to collect network scan data in a structured format. If live scanning is included, it will be limited to safe and permitted environments.

2. **Nmap XML Parser Tool**

   This tool will process existing Nmap XML scan result files. It will extract useful information such as open ports, detected services, protocols, and port states. This mode is important because it allows the system to be tested safely without scanning external systems.

3. **Risk Rule Tool**

   This tool will map detected ports and services to risk levels and recommendations. For example, services such as Telnet, FTP, MySQL, PostgreSQL, or RDP may require more attention depending on how they are exposed and configured.

4. **Report Writer Tool**

   This tool will save the final result in a structured format, such as JSON or a text report. This will make the output easier to review, store, and compare.

The initial development will focus on scan-file analysis using sample Nmap XML files. Optional live scanning may be added later only for localhost or authorized lab targets.

### Preliminary Programming Concepts Required

The project will require several programming concepts and software development practices.

The preliminary concepts include:

- Python functions for implementing tool behavior,
- object-oriented programming for the main agent class,
- modular programming to separate the agent, tools, utilities, and tests,
- command-line input handling,
- file handling for reading scan result files and writing reports,
- XML parsing for processing Nmap output,
- dictionaries and lists for storing structured scan data,
- input validation for checking file paths, file types, and target values,
- error handling for invalid files, unsupported formats, or parsing problems,
- subprocess usage if live Nmap scanning is implemented,
- JSON or text report generation,
- automated testing with pytest,
- Git and GitHub for version control,
- documentation through README and journal files.

At this stage, the project is in the planning phase. The next stage will focus on creating the Python project structure and implementing the first working components of the system.