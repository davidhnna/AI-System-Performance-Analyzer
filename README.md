# AI System Performance Analyzer

A Python-based tool that leverages Google's Gemini AI to analyze your system's top 5 processes and provide intelligent recommendations to optimize performance.

## Features

- **Real-time Process Monitoring**: Captures and analyzes the top 5 most resource-intensive processes on your system
- **AI-Powered Analysis**: Uses Google's Gemini AI to provide intelligent insights about system performance
- **Actionable Recommendations**: Receives specific instructions on how to improve system performance
- **Easy to Use**: Simple command-line interface for quick performance checks

## Prerequisites

Before running this tool, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/davidhnna/AI-System-Performance-Analyzer.git
cd AI-System-Performance-Analyzer
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Google Gemini API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Set it as an environment variable:
   
   **Windows (Command Prompt):**
   ```cmd
   set GEMINI_API_KEY=your_api_key_here
   ```
   
   **Windows (PowerShell):**
   ```powershell
   $env:GEMINI_API_KEY="your_api_key_here"
   ```
   
   **Linux/Mac:**
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the system monitor:

```bash
python sysmonitor.py
```

The tool will:
1. Analyze your system's current resource usage
2. Identify the top 5 most resource-intensive processes
3. Send the data to Gemini AI for analysis
4. Display performance recommendations and optimization instructions

## What Gets Analyzed

The tool monitors and analyzes:
- CPU usage per process
- Memory consumption
- Process IDs and names
- Overall system resource utilization

## AI Analysis

The Gemini AI model analyzes your system data and provides:
- Performance bottleneck identification
- Process-specific optimization suggestions
- System configuration recommendations
- Best practices for resource management

## Dependencies

- `psutil` - For system and process monitoring
- `google-generativeai` - For Gemini AI integration
- Other standard Python libraries

## Configuration

You can customize the analysis by modifying `sysmonitor.py`:
- Change the number of processes to analyze
- Adjust monitoring intervals
- Customize AI prompts for specific use cases

## Example Output

```
Analyzing top 5 system processes...

Process Analysis:
1. Chrome.exe - CPU: 45%, Memory: 2.1 GB
2. Python.exe - CPU: 23%, Memory: 512 MB
3. Discord.exe - CPU: 15%, Memory: 890 MB
...

AI Recommendations:
- Chrome is consuming significant resources. Consider closing unused tabs...
- Multiple Python processes detected. Review running scripts...
- Overall system memory usage is at 78%. Consider upgrading RAM...
```

## Privacy & Security

- All system data is processed locally and sent only to Google's Gemini API
- No personal data is stored or shared beyond what's necessary for AI analysis
- API keys should be kept secure and never committed to version control


## 📄 License

This project is open source 
