import psutil
import time
from google import genai
GEMINI_API_KEY="Your API key"

def get_system_status():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    processes = []

    # initialize cpu_percent counters
    for p in psutil.process_iter(['name']):
        try:
            p.cpu_percent(None)  # initialize
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Wait a short time
    time.sleep(0.5)

    # get actual CPU and memory usage
    for p in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
        try:
            cpu_p = p.info['cpu_percent'] or 0.0
            mem_p = p.info['memory_percent'] or 0.0
            processes.append((p.pid, p.info['name'], cpu_p, mem_p))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort top 5 by CPU
    top_processes = sorted(processes, key=lambda x: x[2], reverse=True)[:5]

    return {
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "top_processes": top_processes
    }

client = genai.Client(api_key=GEMINI_API_KEY)

def ai_generate_tips(status):
    # Format top processes into a readable string
    process_lines = []
    for pid, name, cpu_p, mem_p in status.get('top_processes', []):
        process_lines.append(f"{name} (PID {pid}) - CPU: {cpu_p:.1f}%, RAM: {mem_p:.1f}%")
    process_text = "\n".join(process_lines) if process_lines else "No significant processes detected."

    # Build the AI prompt
    prompt = (
        f"System status:\n"
        f"CPU usage: {status['cpu']:.1f}%\n"
        f"Memory usage: {status['memory']:.1f}%\n"
        f"Disk usage: {status['disk']:.1f}%\n\n"
        f"Top processes:\n{process_text}\n\n"
        "Provide clear and practical tips to improve system performance, "
        "including advice on which processes to close or optimize."
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

status = get_system_status()
print("System Status:", status)

try:
    tips = ai_generate_tips(status)
    print("\nAI Performance Tips:\n", tips)
except Exception as e:
    print("Error generating AI tips:", e)