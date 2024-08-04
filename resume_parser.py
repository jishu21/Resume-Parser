import json

def parse_resume(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    resume = {
        "name": "",
        "contact_information": "",
        "summary": "",
        "experience": [],
        "education": [],
        "skills": [],
        "projects": []
    }

    current_section = None

    for line in lines:
        line = line.strip()
        if line.lower().startswith('name:'):
            resume["name"] = line[len('name:'):].strip()
        elif line.lower().startswith('contact information:'):
            resume["contact_information"] = line[len('contact information:'):].strip()
        elif line.lower().startswith('summary:'):
            current_section = "summary"
            resume["summary"] = line[len('summary:'):].strip()
        elif line.lower().startswith('experience:'):
            current_section = "experience"
        elif line.lower().startswith('education:'):
            current_section = "education"
        elif line.lower().startswith('skills:'):
            current_section = "skills"
        elif line.lower().startswith('projects:'):
            current_section = "projects"
        else:
            if current_section == "experience":
                if line:
                    parts = line.split(';')
                    experience_item = {
                        "company": parts[0].strip(),
                        "position": parts[1].strip(),
                        "duration": parts[2].strip(),
                        "details": parts[3].strip() if len(parts) > 3 else ""
                    }
                    resume["experience"].append(experience_item)
            elif current_section == "education":
                if line:
                    parts = line.split(';')
                    education_item = {
                        "institution": parts[0].strip(),
                        "degree": parts[1].strip(),
                        "year": parts[2].strip()
                    }
                    resume["education"].append(education_item)
            elif current_section == "skills":
                if line:
                    skills = line.split(',')
                    resume["skills"].extend([skill.strip() for skill in skills])
            elif current_section == "projects":
                if line:
                    parts = line.split(';')
                    project_item = {
                        "name": parts[0].strip(),
                        "description": parts[1].strip()
                    }
                    resume["projects"].append(project_item)

    return resume

if __name__ == "__main__":
    resume_path = 'sample_resume.txt'
    parsed_resume = parse_resume(resume_path)
    with open('output.json', 'w') as json_file:
        json.dump(parsed_resume, json_file, indent=4)
    print(f"Resume parsed successfully and saved to output.json")
