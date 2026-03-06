import re

with open('c:\\personal\\ref_styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

replacements = [
    (r'--bg: #070a0f;', '--bg: #F7F5F0;'),
    (r'--bg-elevated: #101520;', '--bg-elevated: #FFFFFF;'),
    (r'--bg-soft: #141a26;', '--bg-soft: #EFEBE0;'),
    (r'--accent: #c43b2f;', '--accent: #355E3B;'),
    (r'--accent-soft: rgba\(196, 59, 47, 0\.18\);', '--accent-soft: rgba(53, 94, 59, 0.18);'),
    (r'--accent-strong: #ff6b4a;', '--accent-strong: #2a4a2f;'),
    (r'--text: #f7f7f7;', '--text: #5B3A2E;'),
    (r'--muted: #a2a8b9;', '--muted: rgba(91, 58, 46, 0.7);'),
    (r'--outline: rgba\(255, 255, 255, 0\.06\);', '--outline: rgba(53, 94, 59, 0.15);'),
    (r'--shadow-soft: 0 18px 50px rgba\(0, 0, 0, 0\.6\);', '--shadow-soft: 0 18px 50px rgba(53, 94, 59, 0.1);'),
    
    (r'rgba\(196, 59, 47', 'rgba(227, 138, 174'), # rose
    (r'rgba\(255, 215, 160', 'rgba(212, 167, 64'), # gold
    (r'rgba\(7, 10, 15', 'rgba(247, 245, 240'), # cream
    
    (r'#fdd29a', '#C9D8C1'), # sage
    (r'#fcd59a', '#C9D8C1'), # sage
    (r'#f4d29a', '#C9D8C1'), # sage

    (r'rgba\(0, 0, 0, 0\.5\)', 'rgba(53, 94, 59, 0.15)'),
    (r'rgba\(0, 0, 0, 0\.7\)', 'rgba(53, 94, 59, 0.15)'),
    (r'rgba\(0, 0, 0, 0\.8\)', 'rgba(53, 94, 59, 0.2)'),
    (r'rgba\(0, 0, 0, 0\.9\)', 'rgba(247, 245, 240, 0.9)'),
    
    (r'rgba\(255, 255, 255, 0\.04\)', 'rgba(53, 94, 59, 0.04)'),
    (r'rgba\(255, 255, 255, 0\.35\)', 'rgba(53, 94, 59, 0.35)'),
    (r'rgba\(255, 255, 255, 0\.06\)', 'rgba(53, 94, 59, 0.15)'),
    
    (r'#242938', '#FFFFFF'),
    (r'#121623', '#F7F5F0'),
    (r'#222639', '#FFFFFF'),
    (r'#101520', '#F7F5F0'),
    (r'#1d2130', '#FFFFFF'),
    
    (r'rgba\(20, 26, 38, 0\.95\)', 'rgba(255, 255, 255, 0.95)'),
    (r'rgba\(20, 26, 38, 0\.96\)', 'rgba(255, 255, 255, 0.96)'),
    
    (r'rgba\(244, 210, 155, 0\.8\)', 'rgba(201, 216, 193, 0.8)'),
    
    (r'color: #fff;', 'color: #F7F5F0;')
]

for pattern, repl in replacements:
    css = re.sub(pattern, repl, css, flags=re.IGNORECASE)

# Insert the original variables at the top for reference
user_vars = """
/* User original variables */
:root {
  --forest: #355E3B;
  --sage: #C9D8C1;
  --gold: #D4A740;
  --cocoa: #5B3A2E;
  --rose: #E38AAE;
  --cream: #F7F5F0;
  --forest-dark: #2a4a2f;
  --cocoa-light: #7a5240;
  --gold-light: #e8c468;
  --rose-light: #f0a8c4;
}
"""

with open('c:\\personal\\styles.css', 'w', encoding='utf-8') as f:
    f.write(user_vars + "\n" + css)

print("CSS rewritten successfully")
