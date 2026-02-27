import os
import re
import json

def fix_yaml_quotes(skills_dir):
    print(f"Scanning for YAML quoting errors in {skills_dir}...")
    fixed_count = 0
    
    for root, dirs, files in os.walk(skills_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if 'SKILL.md' in files:
            file_path = os.path.join(root, 'SKILL.md')
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue

            fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if not fm_match:
                continue
                
            fm_text = fm_match.group(1)
            new_fm_lines = []
            changed = False
            
            for line in fm_text.split('\n'):
                if line.startswith('description:'):
                    key, val = line.split(':', 1)
                    val = val.strip()
                    
                    # Store original to check if it matches the fixed version
                    orig_val = val
                    
                    # Strip matching outer quotes if they exist
                    if val.startswith('"') and val.endswith('"') and len(val) >= 2:
                        val = val[1:-1]
                    elif val.startswith("'") and val.endswith("'") and len(val) >= 2:
                        val = val[1:-1]
                        
                    # Now safely encode using JSON to handle internal escapes
                    safe_val = json.dumps(val)
                    
                    if safe_val != orig_val:
                        new_line = f"description: {safe_val}"
                        new_fm_lines.append(new_line)
                        changed = True
                        continue
                new_fm_lines.append(line)
                
            if changed:
                new_fm_text = '\n'.join(new_fm_lines)
                new_content = content[:fm_match.start(1)] + new_fm_text + content[fm_match.end(1):]
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed quotes in {os.path.relpath(file_path, skills_dir)}")
                fixed_count += 1
                
    print(f"Total files fixed: {fixed_count}")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fix_yaml_quotes(os.path.join(base_dir, 'skills'))
