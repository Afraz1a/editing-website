$css = Get-Content -Raw -Path "c:\personal\ref_styles.css" -Encoding UTF8

$replacements = @(
    @('--bg: #070a0f;', '--bg: #F7F5F0;'),
    @('--bg-elevated: #101520;', '--bg-elevated: #FFFFFF;'),
    @('--bg-soft: #141a26;', '--bg-soft: #EFEBE0;'),
    @('--accent: #c43b2f;', '--accent: #355E3B;'),
    @('--accent-soft: rgba\(196, 59, 47, 0\.18\);', '--accent-soft: rgba(53, 94, 59, 0.18);'),
    @('--accent-strong: #ff6b4a;', '--accent-strong: #2a4a2f;'),
    @('--text: #f7f7f7;', '--text: #5B3A2E;'),
    @('--muted: #a2a8b9;', '--muted: rgba(91, 58, 46, 0.7);'),
    @('--outline: rgba\(255, 255, 255, 0\.06\);', '--outline: rgba(53, 94, 59, 0.15);'),
    @('--shadow-soft: 0 18px 50px rgba\(0, 0, 0, 0\.6\);', '--shadow-soft: 0 18px 50px rgba(53, 94, 59, 0.1);'),
    @('rgba\(196, 59, 47', 'rgba(227, 138, 174'),
    @('rgba\(255, 215, 160', 'rgba(212, 167, 64'),
    @('rgba\(7, 10, 15', 'rgba(247, 245, 240'),
    @('#fdd29a', '#C9D8C1'),
    @('#fcd59a', '#C9D8C1'),
    @('#f4d29a', '#C9D8C1'),
    @('rgba\(0, 0, 0, 0\.5\)', 'rgba(53, 94, 59, 0.15)'),
    @('rgba\(0, 0, 0, 0\.7\)', 'rgba(53, 94, 59, 0.15)'),
    @('rgba\(0, 0, 0, 0\.8\)', 'rgba(53, 94, 59, 0.2)'),
    @('rgba\(0, 0, 0, 0\.9\)', 'rgba(247, 245, 240, 0.9)'),
    @('rgba\(255, 255, 255, 0\.04\)', 'rgba(53, 94, 59, 0.04)'),
    @('rgba\(255, 255, 255, 0\.35\)', 'rgba(53, 94, 59, 0.35)'),
    @('rgba\(255, 255, 255, 0\.06\)', 'rgba(53, 94, 59, 0.15)'),
    @('#242938', '#FFFFFF'),
    @('#121623', '#F7F5F0'),
    @('#222639', '#FFFFFF'),
    @('#101520', '#F7F5F0'),
    @('#1d2130', '#FFFFFF'),
    @('rgba\(20, 26, 38, 0\.95\)', 'rgba(255, 255, 255, 0.95)'),
    @('rgba\(20, 26, 38, 0\.96\)', 'rgba(255, 255, 255, 0.96)'),
    @('rgba\(244, 210, 155, 0\.8\)', 'rgba(201, 216, 193, 0.8)'),
    @('color: #fff;', 'color: #F7F5F0;')
)

foreach ($r in $replacements) {
    # Powershell regex replace is case insensitive by default (-replace).
    $css = $css -replace $r[0], $r[1]
}

$user_vars = @"
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

"@

$finalCss = $user_vars + $css
Set-Content -Path "c:\personal\styles.css" -Value $finalCss -Encoding UTF8
