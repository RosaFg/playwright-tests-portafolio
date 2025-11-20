import subprocess
import json
from datetime import datetime
from pathlib import Path

print("Generando reporte de tests...")
print("=" * 60)

result = subprocess.run(
    ["pytest", "-v", "--tb=short"],
    capture_output=True,
    text=True,
    encoding='utf-8',
    errors='replace'
)

lines = result.stdout.split('\n')
passed = 0
failed = 0
total = 0
failed_tests = []
passed_tests = []

for line in lines:
    if 'PASSED' in line:
        passed += 1
        total += 1
        test_name = line.split('::')[1].split('[')[0] if '::' in line else line
        passed_tests.append(test_name)
    elif 'FAILED' in line:
        failed += 1
        total += 1
        test_name = line.split('::')[1].split('[')[0] if '::' in line else line
        failed_tests.append(test_name)


screenshots_dir = Path("screenshots")
screenshots = list(screenshots_dir.glob("*FAILED*.png")) if screenshots_dir.exists() else []

html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Tests - Portafolio Rosa Fuentes</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 40px;
            background: #f8f9fa;
        }}
        .stat-card {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }}
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        .stat-number {{
            font-size: 3em;
            font-weight: bold;
            margin: 10px 0;
        }}
        .stat-label {{
            color: #666;
            font-size: 1.1em;
        }}
        .success {{ color: #28a745; }}
        .danger {{ color: #dc3545; }}
        .info {{ color: #17a2b8; }}
        .section {{
            padding: 40px;
        }}
        .section h2 {{
            font-size: 2em;
            margin-bottom: 20px;
            color: #333;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        .test-list {{
            list-style: none;
        }}
        .test-item {{
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            display: flex;
            align-items: center;
            gap: 15px;
            transition: all 0.3s;
        }}
        .test-item:hover {{
            transform: translateX(10px);
        }}
        .test-passed {{
            background: #d4edda;
            border-left: 5px solid #28a745;
        }}
        .test-failed {{
            background: #f8d7da;
            border-left: 5px solid #dc3545;
        }}
        .badge {{
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9em;
        }}
        .badge-success {{
            background: #28a745;
            color: white;
        }}
        .badge-danger {{
            background: #dc3545;
            color: white;
        }}
        .screenshot-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        .screenshot-card {{
            background: white;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .screenshot-card img {{
            width: 100%;
            border-radius: 8px;
            margin-top: 10px;
        }}
        .screenshot-name {{
            font-size: 0.9em;
            color: #666;
            word-break: break-all;
        }}
        .footer {{
            background: #2c3e50;
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .percentage {{
            font-size: 1.5em;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Reporte de Tests E2E</h1>
            <p>Portafolio Rosa Fuentes</p>
            <p style="font-size: 0.9em; margin-top: 10px;">Generado: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-label">Total de Tests</div>
                <div class="stat-number info">{total}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Tests Exitosos</div>
                <div class="stat-number success">{passed}</div>
                <div class="percentage success">{(passed/total*100) if total > 0 else 0:.1f}%</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Tests Fallidos</div>
                <div class="stat-number danger">{failed}</div>
                <div class="percentage danger">{(failed/total*100) if total > 0 else 0:.1f}%</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Screenshots</div>
                <div class="stat-number info">{len(screenshots)}</div>
            </div>
        </div>
        
        <div class="section">
            <h2> Tests Exitosos ({passed})</h2>
            <ul class="test-list">
"""

for test in passed_tests[:10]:  #
    html += f"""
                <li class="test-item test-passed">
                    <span class="badge badge-success">✓ PASS</span>
                    <span>{test}</span>
                </li>
"""

if len(passed_tests) > 10:
    html += f"""
                <li class="test-item" style="background: #e9ecef; text-align: center;">
                    <span>... y {len(passed_tests) - 10} tests más exitosos</span>
                </li>
"""

html += """
            </ul>
        </div>
        
        <div class="section">
            <h2> Tests Fallidos ({0})</h2>
            <ul class="test-list">
""".format(failed)

for test in failed_tests:
    html += f"""
                <li class="test-item test-failed">
                    <span class="badge badge-danger">✗ FAIL</span>
                    <span>{test}</span>
                </li>
"""

html += """
            </ul>
        </div>
"""

if screenshots:
    html += """
        <div class="section">
            <h2> Screenshots Capturados</h2>
            <div class="screenshot-grid">
"""
    for screenshot in screenshots:
        html += f"""
                <div class="screenshot-card">
                    <div class="screenshot-name">{screenshot.name}</div>
                    <img src="screenshots/{screenshot.name}" alt="{screenshot.name}">
                </div>
"""
    html += """
            </div>
        </div>
"""

html += f"""
        <div class="footer">
            <p><strong>Rosa Fuentes</strong> - QA Automation Engineer</p>
            <p style="margin-top: 10px;">https://portafolio-rosafg.netlify.app/</p>
            <p style="margin-top: 20px; font-size: 0.9em; opacity: 0.8;">
                Reporte generado automáticamente con Playwright + Pytest
            </p>
        </div>
    </div>
</body>
</html>
"""

report_path = Path("reporte_simple.html")
report_path.write_text(html, encoding='utf-8')

print(f"\n✓ Reporte generado: {report_path}")
print(f"✓ Tests totales: {total}")
print(f"✓ Tests exitosos: {passed}")
print(f"✓ Tests fallidos: {failed}")
print(f"✓ Screenshots: {len(screenshots)}")
print("=" * 60)
print(f"\nAbre el reporte: start {report_path}")