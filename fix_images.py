import os
import re

templates_dir = 'c:/Users/User/Desktop/props 2026/templates'

for filename in os.listdir(templates_dir):
    if filename.endswith('.html'):
        path = os.path.join(templates_dir, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We need to replace src="/main.py/templates/images/..." with src="{% static 'images/...' %}"
        pattern = r'src="/main\.py/templates/images/([^"]+)"'
        replacement = r'src="{% static \'images/\1\' %}"'
        
        new_content = re.sub(pattern, replacement, content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print('Done fixing image paths!')
