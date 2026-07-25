import os
import subprocess
import sys
import json
import urllib.request
import datetime

def get_git_diff_and_commits():
    try:
        # Get commit logs from the last push / commit
        log_cmd = ["git", "log", "-n", "5", "--pretty=format:- %s (%h)"]
        log_output = subprocess.check_output(log_cmd, text=True).strip()
        
        # Get diff summary
        stat_cmd = ["git", "diff", "HEAD~1", "HEAD", "--stat"]
        try:
            stat_output = subprocess.check_output(stat_cmd, text=True).strip()
        except Exception:
            stat_output = ""
            
        content = f"Recent Commits:\n{log_output}\n\nFile Changes Summary:\n{stat_output}"
        return content
    except Exception as e:
        print(f"Error getting git info: {e}")
        return "Minor repository updates and maintenance."

def call_nvidia_nim(content, api_key):
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""You are an automated README update assistant.
Analyze the following recent git commits and diff summary, then write a concise, clean 2-4 bullet point summary of what changed in the project.

Format requirement:
Return ONLY markdown bullet points. Do not include introductory text, conversational filler, or markdown code block fences (no ``` markdown).

Git Info:
{content}
"""

    payload = {
        "model": "meta/llama-3.3-70b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "top_p": 0.7,
        "max_tokens": 1024,
        "stream": False
    }

    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error calling NVIDIA NIM API: {e}")
        return None

def update_readme(summary_text):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("README.md not found.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    start_tag = "<!-- RECENT_UPDATES_START -->"
    end_tag = "<!-- RECENT_UPDATES_END -->"

    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    
    formatted_block = f"{start_tag}\n> 💡 **Latest Repo Updates ({today}):**\n{summary_text}\n{end_tag}"

    if start_tag in readme_content and end_tag in readme_content:
        pre = readme_content.split(start_tag)[0]
        post = readme_content.split(end_tag)[1]
        new_content = pre + formatted_block + post
    else:
        # Insert before Features or at top
        if "## Features" in readme_content:
            new_content = readme_content.replace("## Features", f"{formatted_block}\n\n## Features")
        else:
            new_content = readme_content + f"\n\n{formatted_block}\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README.md updated successfully!")

def main():
    api_key = os.environ.get("NVIDIA_API_KEY")
    if not api_key:
        print("NVIDIA_API_KEY environment variable not set.")
        sys.exit(1)

    git_info = get_git_diff_and_commits()
    print("Analyzing git info...")
    summary = call_nvidia_nim(git_info, api_key)
    if summary:
        print(f"Generated Summary:\n{summary}")
        update_readme(summary)
    else:
        print("Failed to generate summary.")

if __name__ == "__main__":
    main()
