import os
import re

def fix_skills(skills_dir):
    for root, dirs, files in os.walk(skills_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if "SKILL.md" in files:
            skill_path = os.path.join(root, "SKILL.md")
            with open(skill_path, 'r', encoding='utf-8') as f:
                content = f.read()

            fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if not fm_match:
                continue
            
            fm_text = fm_match.group(1)
            folder_name = os.path.basename(root)
            new_fm_lines = []
            changed = False
            
            for line in fm_text.split('\n'):
                if line.startswith('name:'):
                    old_name = line.split(':', 1)[1].strip().strip('"').strip("'")
                    if old_name != folder_name:
                        new_fm_lines.append(f"name: {folder_name}")
                        changed = True
                    else:
                        new_fm_lines.append(line)
                elif line.startswith('description:'):
                    desc = line.split(':', 1)[1].strip().strip('"').strip("'")
                    if len(desc) > 200:
                        # trim to 197 chars and add "..."
                        short_desc = desc[:197] + "..."
                        new_fm_lines.append(f'description: "{short_desc}"')
                        changed = True
                    else:
                        new_fm_lines.append(line)
                else:
                    new_fm_lines.append(line)
            
            if changed:
                new_fm_text = '\n'.join(new_fm_lines)
                new_content = content[:fm_match.start(1)] + new_fm_text + content[fm_match.end(1):]
                with open(skill_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed {skill_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_path = os.path.join(base_dir, "skills")
    fix_skills(skills_path)
