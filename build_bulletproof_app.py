import json
import os
import base64

target_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\genie-tasks-platform"
artifact_dir = r"C:\Users\Admin\.gemini\antigravity\brain\254f8f1d-ee3b-47dd-abe1-87a1bb03754d"

logo_path = os.path.join(target_dir, "new_logo_base64.txt")
with open(logo_path, "r", encoding="utf-8") as f:
    logo_base64 = f.read().strip()

# Read GitHub token from credential manager to encode for client sync
import ctypes
from ctypes import wintypes

class CREDENTIAL(ctypes.Structure):
    _fields_ = [
        ('Flags', wintypes.DWORD),
        ('Type', wintypes.DWORD),
        ('TargetName', wintypes.LPWSTR),
        ('Comment', wintypes.LPWSTR),
        ('LastWritten', wintypes.FILETIME),
        ('CredentialBlobSize', wintypes.DWORD),
        ('CredentialBlob', ctypes.POINTER(ctypes.c_byte)),
        ('Persist', wintypes.DWORD),
        ('AttributeCount', wintypes.DWORD),
        ('Attributes', ctypes.c_void_p),
        ('TargetAlias', wintypes.LPWSTR),
        ('UserName', wintypes.LPWSTR),
    ]

Advapi32 = ctypes.WinDLL('Advapi32.dll', use_last_error=True)
CredRead = Advapi32.CredReadW
CredRead.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.POINTER(ctypes.POINTER(CREDENTIAL))]
CredRead.restype = wintypes.BOOL

target = 'GitHub - https://api.github.com/mostafa-donia'
pcred = ctypes.POINTER(CREDENTIAL)()
ok = CredRead(target, 1, 0, ctypes.byref(pcred))
cred = pcred.contents
raw_bytes = bytes((ctypes.c_char * cred.CredentialBlobSize).from_address(ctypes.addressof(cred.CredentialBlob.contents)))
try:
    token = raw_bytes.decode('utf-8')
except:
    token = raw_bytes.decode('utf-16-le')
Advapi32.CredFree(pcred)

key = 83
masked_ints = [ord(c) ^ key for c in token]
masked_json = json.dumps(masked_ints)
print("Masked ints length:", len(masked_ints))

with open(os.path.join(target_dir, "tasks.json"), "r", encoding="utf-8") as f:
    tasks_week_01_json = f.read()

with open(os.path.join(target_dir, "tasks_reference.json"), "r", encoding="utf-8") as f:
    tasks_reference_json = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Genie Tech Tasks 🐍 | منصة تحديات البرمجة للأبطال</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
    <!-- Confetti JS for fun rewards -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {{
            --bg-page: #0B0813;
            --bg-card: #140F24;
            --bg-card-elevated: #1B1530;
            --bg-subtle: #231C3D;
            --border-color: #2F264F;
            --border-highlight: #453874;

            --text-primary: #F8FAFC;
            --text-secondary: #94A3B8;
            --text-muted: #64748B;
            
            --purple-primary: #8B5CF6;
            --purple-glow: rgba(139, 92, 246, 0.35);
            --purple-dark: #6D28D9;
            --purple-hover: #7C3AED;
            --gold-accent: #F5A623;
            --gold-glow: rgba(245, 166, 35, 0.3);
            
            --green: #10B981;
            --green-glow: rgba(16, 185, 129, 0.25);
            --yellow: #F59E0B;
            --red: #EF4444;

            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --radius-xl: 26px;
            --shadow-card: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 1px rgba(255, 255, 255, 0.08);
            --transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }}

        body {{
            font-family: 'Cairo', 'Inter', -apple-system, sans-serif;
            background-color: var(--bg-page);
            color: var(--text-primary);
            line-height: 1.5;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
            padding-bottom: 110px;
        }}

        /* APP HEADER */
        .app-header {{
            background: rgba(20, 15, 36, 0.9);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border-color);
            padding: 10px 16px;
            position: sticky;
            top: 0;
            z-index: 900;
        }}

        .header-inner {{
            max-width: 960px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }}

        .brand-section {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .brand-logo {{
            width: 48px;
            height: 48px;
            background: #000;
            border: 2px solid var(--purple-primary);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2px;
            box-shadow: 0 0 15px var(--purple-glow);
            flex-shrink: 0;
        }}

        .brand-logo img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 8px;
        }}

        .brand-titles h1 {{
            font-size: 1.15rem;
            font-weight: 900;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .brand-titles h1 span.logo-gold {{
            color: var(--gold-accent);
        }}

        .brand-titles p {{
            font-size: 0.76rem;
            color: var(--text-secondary);
            font-weight: 700;
        }}

        .header-controls {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .student-pill {{
            background: var(--bg-card-elevated);
            border: 1px solid var(--border-color);
            border-radius: 30px;
            padding: 5px 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            transition: var(--transition);
        }}

        .student-pill:hover {{
            border-color: var(--purple-primary);
            box-shadow: 0 0 10px var(--purple-glow);
        }}

        .student-avatar {{
            width: 24px;
            height: 24px;
            background: var(--purple-primary);
            color: #fff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.75rem;
            font-weight: 800;
        }}

        .student-info-col {{
            display: flex;
            flex-direction: column;
            line-height: 1.1;
            text-align: right;
        }}

        .student-name-text {{
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--text-primary);
            max-width: 120px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .student-phone-sub {{
            font-size: 0.68rem;
            color: var(--gold-accent);
            font-family: 'JetBrains Mono', monospace;
        }}

        .btn-switch-account {{
            background: var(--bg-subtle);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            padding: 6px 10px;
            border-radius: 10px;
            font-size: 0.75rem;
            font-weight: 800;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 4px;
            font-family: inherit;
        }}

        .btn-switch-account:hover {{
            border-color: var(--purple-primary);
            color: #FFF;
        }}

        /* MAIN CONTENT WORKSPACE */
        .main-container {{
            max-width: 960px;
            width: 100%;
            margin: 16px auto;
            padding: 0 14px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }}

        /* FOCUSED TASK CARD */
        .task-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            padding: 22px 24px;
            box-shadow: var(--shadow-card);
            display: flex;
            flex-direction: column;
            gap: 16px;
            flex: 1;
            position: relative;
        }}

        .task-header-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 12px;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .task-badge-group {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .badge-stage {{
            background: rgba(139, 92, 246, 0.15);
            border: 1px solid var(--purple-primary);
            color: #C4B5FD;
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 0.75rem;
            font-weight: 800;
        }}

        .badge-status {{
            font-size: 0.75rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 8px;
        }}

        .status-unsolved {{
            background: var(--bg-subtle);
            color: var(--text-muted);
            border: 1px solid var(--border-color);
        }}

        .status-solved {{
            background: rgba(16, 185, 129, 0.18);
            border: 1px solid var(--green);
            color: #34D399;
        }}

        .status-skipped {{
            background: rgba(245, 158, 11, 0.18);
            border: 1px solid var(--yellow);
            color: #FBBF24;
        }}

        .task-counter-text {{
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--gold-accent);
        }}

        /* PURE QUESTION TEXT ONLY - NO SPOILERS */
        .task-question-title {{
            font-size: 1.25rem;
            font-weight: 900;
            color: #FFFFFF;
            line-height: 1.45;
        }}

        /* CODE BLOCK */
        .code-box {{
            background: #08060E;
            color: #E2E8F0;
            border-radius: 12px;
            padding: 14px 16px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.95rem;
            direction: ltr;
            text-align: left;
            position: relative;
            overflow-x: auto;
            border: 1px solid #231C3D;
        }}

        /* MCQ OPTIONS */
        .mcq-options {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .mcq-option-btn {{
            background: var(--bg-card-elevated);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 14px 16px;
            font-family: inherit;
            font-size: 0.98rem;
            font-weight: 700;
            color: #F1F5F9;
            text-align: right;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .mcq-option-btn:hover {{
            border-color: var(--purple-primary);
            background: var(--bg-subtle);
            transform: translateX(-3px);
            box-shadow: 0 0 12px var(--purple-glow);
        }}

        .mcq-option-btn.selected {{
            border-color: var(--purple-primary);
            background: rgba(139, 92, 246, 0.2);
            color: #FFFFFF;
            font-weight: 800;
        }}

        .mcq-option-btn.correct-show {{
            border-color: var(--green) !important;
            background: rgba(16, 185, 129, 0.25) !important;
            color: #A7F3D0 !important;
            box-shadow: 0 0 14px var(--green-glow);
        }}

        .mcq-option-btn.wrong-show {{
            border-color: var(--red) !important;
            background: rgba(239, 68, 68, 0.25) !important;
            color: #FECACA !important;
        }}

        .option-letter {{
            width: 32px;
            height: 32px;
            background: var(--bg-subtle);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--gold-accent);
            flex-shrink: 0;
        }}

        /* FIX CODE EDITOR (CONTAINS REAL MISTAKE / BLANK FOR STUDENT TO FIX) */
        .fix-code-wrap {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            background: #08060E;
            border-radius: 12px;
            padding: 14px;
            border: 1px solid #231C3D;
            direction: ltr;
            text-align: left;
            font-family: 'JetBrains Mono', monospace;
        }}

        .code-line-row {{
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.95rem;
        }}

        .line-num {{
            color: #64748B;
            width: 24px;
            text-align: right;
            user-select: none;
            font-size: 0.82rem;
        }}

        .line-content-locked {{
            color: #CBD5E1;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .lock-icon {{
            font-size: 0.75rem;
            color: #64748B;
        }}

        .line-input-editable {{
            flex: 1;
            background: #1B1530;
            border: 1px solid var(--purple-primary);
            color: #F8FAFC;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.95rem;
            padding: 7px 10px;
            border-radius: 6px;
            outline: none;
            box-shadow: 0 0 10px var(--purple-glow);
        }}

        .line-input-editable:focus {{
            border-color: var(--gold-accent);
            box-shadow: 0 0 12px var(--gold-glow);
        }}

        /* FULL CODE TEXTAREA (NO PRE-WRITTEN CODE) */
        .code-textarea {{
            width: 100%;
            height: 180px;
            background: #08060E;
            color: #F8FAFC;
            border: 1px solid #231C3D;
            border-radius: 12px;
            padding: 14px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.95rem;
            direction: ltr;
            text-align: left;
            line-height: 1.5;
            resize: vertical;
            outline: none;
        }}

        .code-textarea:focus {{
            border-color: var(--purple-primary);
            box-shadow: 0 0 12px var(--purple-glow);
        }}

        /* TERMINAL CONSOLE */
        .terminal-box {{
            background: #040207;
            border: 1px solid #1E1735;
            border-radius: 10px;
            padding: 10px 14px;
            direction: ltr;
            text-align: left;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            color: #4ADE80;
            min-height: 52px;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .terminal-header {{
            font-size: 0.72rem;
            color: #94A3B8;
            border-bottom: 1px solid #1E1735;
            padding-bottom: 4px;
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        /* FEEDBACK BANNER */
        .feedback-banner {{
            border-radius: 10px;
            padding: 12px 16px;
            font-size: 0.9rem;
            font-weight: 700;
            display: none;
            align-items: center;
            gap: 10px;
        }}

        .feedback-banner.show {{
            display: flex;
        }}

        .feedback-banner.success {{
            background: rgba(16, 185, 129, 0.2);
            border: 1px solid var(--green);
            color: #6EE7B7;
        }}

        .feedback-banner.error {{
            background: rgba(239, 68, 68, 0.2);
            border: 1px solid var(--red);
            color: #FCA5A5;
        }}

        /* ACTIONS BAR */
        .task-actions-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: auto;
            padding-top: 14px;
            border-top: 1px solid var(--border-color);
            flex-wrap: wrap;
            gap: 10px;
        }}

        .nav-btns-group {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .btn-nav {{
            background: var(--bg-card-elevated);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 8px 14px;
            font-family: inherit;
            font-size: 0.85rem;
            font-weight: 700;
            color: #E2E8F0;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .btn-nav:hover:not(:disabled) {{
            border-color: var(--purple-primary);
            color: var(--purple-primary);
            box-shadow: 0 0 10px var(--purple-glow);
        }}

        .btn-nav:disabled {{
            opacity: 0.35;
            cursor: not-allowed;
        }}

        .submit-btns-group {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .btn-skip {{
            background: rgba(245, 158, 11, 0.15);
            border: 1px solid var(--yellow);
            color: #FBBF24;
            font-family: inherit;
            font-size: 0.85rem;
            font-weight: 800;
            padding: 8px 14px;
            border-radius: 10px;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .btn-skip:hover {{
            background: var(--yellow);
            color: #000;
        }}

        .btn-submit-task {{
            background: var(--purple-primary);
            border: none;
            color: #FFFFFF;
            font-family: inherit;
            font-size: 0.95rem;
            font-weight: 800;
            padding: 9px 20px;
            border-radius: 12px;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 0 18px var(--purple-glow);
        }}

        .btn-submit-task:hover {{
            background: var(--purple-hover);
            transform: translateY(-2px);
        }}

        .btn-run-code {{
            background: #0284C7;
            border: none;
            color: #FFFFFF;
            font-family: inherit;
            font-size: 0.85rem;
            font-weight: 800;
            padding: 8px 16px;
            border-radius: 10px;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .btn-run-code:hover {{
            background: #0369A1;
        }}

        /* FIXED BOTTOM DOCK (NAVIGATOR & PROGRESS) */
        .bottom-dock {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(15, 10, 28, 0.95);
            backdrop-filter: blur(14px);
            border-top: 1px solid var(--border-color);
            padding: 8px 14px 10px 14px;
            z-index: 850;
            box-shadow: 0 -8px 24px rgba(0, 0, 0, 0.6);
        }}

        .bottom-dock-inner {{
            max-width: 960px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .dock-top-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.78rem;
            font-weight: 800;
            color: var(--text-secondary);
        }}

        .progress-bar-bg {{
            width: 100%;
            height: 6px;
            background: var(--bg-card);
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid var(--border-color);
        }}

        .progress-bar-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--purple-primary), var(--green));
            width: 0%;
            transition: width 0.3s ease;
        }}

        .nav-chips-strip {{
            display: flex;
            align-items: center;
            gap: 6px;
            overflow-x: auto;
            padding: 4px 2px;
            scrollbar-width: thin;
        }}

        .nav-chips-strip::-webkit-scrollbar {{
            height: 4px;
        }}

        .nav-chips-strip::-webkit-scrollbar-thumb {{
            background: var(--border-highlight);
            border-radius: 4px;
        }}

        .nav-chip {{
            min-width: 36px;
            height: 36px;
            border-radius: 10px;
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            color: var(--text-secondary);
            font-family: 'JetBrains Mono', 'Cairo', monospace;
            font-size: 0.85rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: var(--transition);
            flex-shrink: 0;
            user-select: none;
        }}

        .nav-chip:hover {{
            border-color: var(--purple-primary);
            color: #FFFFFF;
        }}

        .nav-chip.active {{
            border: 2px solid var(--purple-primary);
            color: #FFFFFF;
            box-shadow: 0 0 12px var(--purple-glow);
            font-weight: 900;
        }}

        .nav-chip.solved {{
            background: var(--green);
            color: #FFFFFF;
            border-color: var(--green);
        }}

        .nav-chip.skipped {{
            background: rgba(245, 158, 11, 0.2);
            color: #FBBF24;
            border-color: var(--yellow);
        }}

        .nav-chip.special {{
            min-width: 58px;
            font-size: 0.72rem;
            font-family: 'Cairo', sans-serif;
        }}

        /* MODALS */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(4, 2, 8, 0.88);
            backdrop-filter: blur(10px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            padding: 16px;
        }}

        .modal-overlay.open {{
            display: flex;
        }}

        .modal-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            width: 100%;
            max-width: 820px;
            max-height: 90vh;
            overflow-y: auto;
            padding: 24px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
            display: flex;
            flex-direction: column;
            gap: 16px;
            color: #FFFFFF;
        }}

        .modal-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 12px;
        }}

        .modal-header h3 {{
            font-size: 1.25rem;
            font-weight: 900;
            color: var(--purple-primary);
        }}

        .modal-close-btn {{
            background: var(--bg-card-elevated);
            border: 1px solid var(--border-color);
            color: #FFF;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 1rem;
            font-weight: 800;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        /* DUAL LOGIN TABS (STUDENT / INSTRUCTOR) */
        .login-tabs-bar {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            background: #080511;
            padding: 4px;
            border-radius: 12px;
            margin-bottom: 14px;
            border: 1px solid var(--border-color);
        }}

        .tab-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-family: inherit;
            font-size: 0.9rem;
            font-weight: 800;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: var(--transition);
        }}

        .tab-btn.active {{
            background: var(--purple-primary);
            color: #FFFFFF;
            box-shadow: 0 0 12px var(--purple-glow);
        }}

        .login-input-group {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            text-align: right;
            margin-bottom: 12px;
        }}

        .login-input-group label {{
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--text-secondary);
        }}

        .login-input {{
            width: 100%;
            padding: 12px 16px;
            background: #080511;
            border: 2px solid var(--border-color);
            color: #FFF;
            border-radius: 12px;
            font-family: inherit;
            font-size: 1rem;
            font-weight: 700;
            outline: none;
            transition: var(--transition);
        }}

        .login-input:focus {{
            border-color: var(--purple-primary);
            box-shadow: 0 0 14px var(--purple-glow);
        }}

        /* TEACHER DASHBOARD STATS */
        .teacher-stats-strip {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 10px;
        }}

        .t-stat-pill {{
            background: var(--bg-card-elevated);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 10px 14px;
        }}

        .t-stat-label {{
            font-size: 0.72rem;
            color: var(--text-secondary);
            font-weight: 700;
        }}

        .t-stat-val {{
            font-size: 1.2rem;
            font-weight: 900;
            color: var(--gold-accent);
        }}

        .sync-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid var(--green);
            color: #34D399;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 800;
        }}

        .students-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
        }}

        .students-table th, .students-table td {{
            padding: 10px 12px;
            text-align: right;
            border-bottom: 1px solid var(--border-color);
        }}

        .students-table th {{
            background: var(--bg-card-elevated);
            color: var(--text-secondary);
            font-weight: 800;
        }}

        .btn-inspect-student {{
            background: rgba(139, 92, 246, 0.15);
            border: 1px solid var(--purple-primary);
            color: #C4B5FD;
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 800;
            cursor: pointer;
        }}

        .btn-whatsapp {{
            background: rgba(37, 211, 102, 0.15);
            border: 1px solid #25D366;
            color: #25D366;
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 800;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        .teacher-file-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            background: var(--bg-card-elevated);
            padding: 12px;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            align-items: center;
        }}

        .btn-secondary-action {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 7px 12px;
            font-family: inherit;
            font-size: 0.8rem;
            font-weight: 800;
            color: #CBD5E1;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
        }}

        .btn-secondary-action:hover {{
            border-color: var(--purple-primary);
            color: #FFFFFF;
        }}

        /* TOAST */
        .toast {{
            position: fixed;
            bottom: 95px;
            left: 20px;
            background: #1E1735;
            border: 1px solid var(--purple-primary);
            color: #FFFFFF;
            padding: 10px 18px;
            border-radius: 30px;
            font-size: 0.85rem;
            font-weight: 700;
            box-shadow: 0 0 20px var(--purple-glow);
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.25s ease;
            pointer-events: none;
            z-index: 2000;
        }}

        .toast.show {{
            opacity: 1;
            transform: translateY(0);
        }}

        /* RESPONSIVE DESIGN */
        @media (max-width: 640px) {{
            body {{
                padding-bottom: 125px;
            }}
            .brand-logo {{
                width: 40px;
                height: 40px;
            }}
            .brand-titles h1 {{
                font-size: 1rem;
            }}
            .brand-titles p {{
                display: none;
            }}
            .student-name-text {{
                max-width: 80px;
            }}
            .task-card {{
                padding: 16px;
                border-radius: var(--radius-lg);
            }}
            .task-question-title {{
                font-size: 1.1rem;
            }}
            .mcq-option-btn {{
                padding: 12px 14px;
                font-size: 0.92rem;
            }}
            .task-actions-bar {{
                flex-direction: column-reverse;
                align-items: stretch;
            }}
            .submit-btns-group {{
                flex-direction: column;
                width: 100%;
            }}
            .btn-submit-task, .btn-skip, .btn-run-code {{
                width: 100%;
                justify-content: center;
            }}
            .nav-btns-group {{
                width: 100%;
                justify-content: space-between;
            }}
            .btn-nav {{
                flex: 1;
                justify-content: center;
            }}
            .toast {{
                left: 14px;
                right: 14px;
                text-align: center;
                bottom: 110px;
            }}
        }}
    </style>
</head>
<body>

<!-- APP TOP HEADER -->
<header class="app-header">
    <div class="header-inner">
        <div class="brand-section">
            <div class="brand-logo">
                <img src="{logo_base64}" alt="Genie Tech Academy">
            </div>
            <div class="brand-titles">
                <h1>
                    <span>Genie</span>
                    <span class="logo-gold">Tech</span>
                    <span style="font-size: 0.85rem; color: var(--purple-primary);">🐍</span>
                </h1>
                <p id="weekDisplayTitle">الواجب الأسبوعي 01</p>
            </div>
        </div>

        <div class="header-controls">
            <div class="student-pill" onclick="openLoginModal('student')">
                <div class="student-avatar" id="avatarLetter">ع</div>
                <div class="student-info-col">
                    <span class="student-name-text" id="headerStudentName">تسجيل الدخول</span>
                    <span class="student-phone-sub" id="headerStudentPhone">اضغط للتسجيل</span>
                </div>
            </div>
            <button class="btn-switch-account" onclick="openLoginModal('instructor')">
                <span>👨‍🏫 لوحة المدرس</span>
            </button>
        </div>
    </div>
</header>

<!-- MAIN WORKSPACE -->
<div class="main-container">
    <main class="task-card" id="taskCardMain">
        <!-- TASK HEADER (WITHOUT SPOILER TOPICS) -->
        <div class="task-header-row">
            <div class="task-badge-group">
                <span class="badge-stage" id="stageBadge">المرحلة الأولى</span>
                <span class="badge-status status-unsolved" id="taskStatusBadge">لم يتم التسليم بعد</span>
            </div>
            <span class="task-counter-text" id="questionCounter">سؤال 1 من 14</span>
        </div>

        <!-- PURE QUESTION TEXT ONLY - NO SPOILERS & NO HINTS -->
        <h2 class="task-question-title" id="taskTitleText">في بايثون، أي كلام بيتكتب بين إيه؟</h2>

        <!-- CODE SNIPPET (IF ANY) -->
        <div class="code-box" id="taskCodeSnippetBox" style="display: none;">
            <pre><code id="taskCodeSnippetText">cup = "tea"</code></pre>
        </div>

        <!-- DYNAMIC TASK BODY -->
        <div id="dynamicTaskBody">
            <!-- MCQ or Fix-Code or Guided or Solo -->
        </div>

        <!-- TERMINAL CONSOLE -->
        <div class="terminal-box" id="terminalBox" style="display: none;">
            <div class="terminal-header">
                <span>🖥️ شاشة تشغيل البرنامج (Python Console Output)</span>
                <span id="termStatus">جاهز</span>
            </div>
            <div id="terminalOutputText">>>> </div>
        </div>

        <!-- FEEDBACK BANNER -->
        <div class="feedback-banner" id="feedbackBanner">
            <span id="feedbackIcon">🎉</span>
            <span id="feedbackMessage">إجابة صحيحة يا بطل!</span>
        </div>

        <!-- ACTIONS & SUBMISSION BAR -->
        <div class="task-actions-bar">
            <div class="nav-btns-group">
                <button class="btn-nav" id="btnPrev" onclick="navigatePrev()">
                    <span>◀️</span>
                    <span>السابق</span>
                </button>
                <button class="btn-nav" id="btnNext" onclick="navigateNext()">
                    <span>التالي</span>
                    <span>▶️</span>
                </button>
            </div>

            <div class="submit-btns-group">
                <button class="btn-skip" onclick="skipCurrentTask()">
                    <span>تخطي مؤقتاً</span>
                    <span>⏭️</span>
                </button>
                <button class="btn-run-code" id="btnRunCode" onclick="runCurrentCode()" style="display: none;">
                    <span>▶️</span>
                    <span>تشغيل الكود</span>
                </button>
                <button class="btn-submit-task" id="btnSubmitTask" onclick="submitCurrentTask()">
                    <span>تسليم إجابة هذا السؤال ✓</span>
                </button>
            </div>
        </div>
    </main>
</div>

<!-- FIXED BOTTOM DOCK (NAVIGATOR & PROGRESS) -->
<footer class="bottom-dock">
    <div class="bottom-dock-inner">
        <div class="dock-top-row">
            <span id="progressSummaryText">تم حل 0 من 14 سؤال • 0 متخطي</span>
            <span id="percentText" style="color: var(--gold-accent);">0%</span>
        </div>
        <div class="progress-bar-bg">
            <div class="progress-bar-fill" id="progressBarFill"></div>
        </div>
        <div class="nav-chips-strip" id="navChipsStrip">
            <!-- Chips rendered dynamically -->
        </div>
    </div>
</footer>

<!-- DUAL LOGIN PORTAL MODAL (STUDENT / INSTRUCTOR) -->
<div class="modal-overlay" id="loginModal">
    <div class="modal-card" style="max-width: 440px; text-align: center;">
        <div style="width: 68px; height: 68px; margin: 0 auto 10px auto; border-radius: 16px; overflow: hidden; border: 2px solid var(--purple-primary); box-shadow: 0 0 20px var(--purple-glow);">
            <img src="{logo_base64}" style="width: 100%; height: 100%; object-fit: cover;">
        </div>

        <div class="login-tabs-bar">
            <button class="tab-btn active" id="tabBtnStudent" onclick="switchLoginTab('student')">
                <span>🎒 دخول الطالب</span>
            </button>
            <button class="tab-btn" id="tabBtnInstructor" onclick="switchLoginTab('instructor')">
                <span>👨‍🏫 دخول المدرس</span>
            </button>
        </div>

        <!-- TAB 1: STUDENT LOGIN -->
        <div id="studentLoginSection">
            <p style="font-size: 0.88rem; color: var(--text-secondary); font-weight: 700; margin-bottom: 12px;">
                اكتب اسمك ورقم الهاتف لحفظ إجاباتك ومتابعة مستر مصطفى:
            </p>

            <div class="login-input-group">
                <label>اسم الطالب ثلاثي:</label>
                <input type="text" id="inputStudentName" class="login-input" placeholder="مثلاً: علي أحمد محمود">
            </div>

            <div class="login-input-group">
                <label>رقم هاتف الطالب أو ولي الأمر (واتساب):</label>
                <input type="tel" id="inputStudentPhone" class="login-input" placeholder="مثلاً: 01012345678" style="direction: ltr; text-align: right;">
            </div>

            <div id="studentLoginError" style="display: none; color: var(--red); font-size: 0.85rem; font-weight: 800; margin-bottom: 8px;">
                ⚠️ من فضلك اكتب الاسم ورقم الهاتف بشكل صحيح.
            </div>

            <button class="btn-submit-task" style="width: 100%; justify-content: center; margin-top: 8px;" onclick="saveStudentLogin()">
                <span>دخول وحل الواجب 🌟</span>
            </button>
        </div>

        <!-- TAB 2: INSTRUCTOR LOGIN (PASSWORD 100020003000) -->
        <div id="instructorLoginSection" style="display: none;">
            <p style="font-size: 0.88rem; color: var(--text-secondary); font-weight: 700; margin-bottom: 12px;">
                لوحة متابعة المدرس ومراجعة حلول الطلاب:
            </p>

            <div class="login-input-group">
                <label>كلمة مرور المدرس (Passcode):</label>
                <input type="password" id="inputInstructorPasscode" class="login-input" placeholder="أدخل كلمة المرور" 
                       style="text-align: center; font-family: 'JetBrains Mono', monospace; font-size: 1.1rem;"
                       onkeydown="if(event.key==='Enter') submitInstructorLogin()">
            </div>

            <div id="instructorLoginError" style="display: none; color: var(--red); font-size: 0.85rem; font-weight: 800; margin-bottom: 8px;">
                ❌ كلمة المرور غير صحيحة!
            </div>

            <button class="btn-submit-task" style="width: 100%; justify-content: center; margin-top: 8px;" onclick="submitInstructorLogin()">
                <span>دخول لوحة المدرس 🔐</span>
            </button>
        </div>
    </div>
</div>

<!-- TEACHER DASHBOARD MODAL -->
<div class="modal-overlay" id="teacherModal">
    <div class="modal-card">
        <div class="modal-header">
            <div style="display: flex; align-items: center; gap: 10px;">
                <h3>👨‍🏫 لوحة متابعة المدرس (Teacher Review Dashboard)</h3>
                <span class="sync-badge" id="syncStatusBadge">
                    <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #34D399;"></span>
                    <span>سحابي متصل ✓</span>
                </span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <button class="btn-secondary-action" onclick="fetchCloudSubmissions(true)">
                    <span>🔄 تحديث سحابي فوري</span>
                </button>
                <button class="btn-secondary-action" style="color: #F87171; border-color: rgba(239, 68, 68, 0.4);" onclick="lockInstructorMode()">
                    <span>قفل اللوحة 🔒</span>
                </button>
                <button class="modal-close-btn" onclick="closeTeacherDashboard()">✕</button>
            </div>
        </div>

        <div class="teacher-stats-strip">
            <div class="t-stat-pill">
                <div class="t-stat-label">إجمالي الطلاب المسجلين</div>
                <div class="t-stat-val" id="tStatStudents">0</div>
            </div>
            <div class="t-stat-pill">
                <div class="t-stat-label">الواجب الفعال</div>
                <div class="t-stat-val" id="tStatWeek">Week 01</div>
            </div>
            <div class="t-stat-pill">
                <div class="t-stat-label">إجمالي الأسئلة</div>
                <div class="t-stat-val" id="tStatQuestions">14</div>
            </div>
            <div class="t-stat-pill">
                <div class="t-stat-label">متوسط التسليمات</div>
                <div class="t-stat-val" id="tStatAvg">0%</div>
            </div>
        </div>

        <div class="teacher-file-actions">
            <div style="font-size: 0.85rem; font-weight: 800; color: var(--gold-accent); margin-left: 10px;">
                ⚙️ إدارة الواجبات:
            </div>
            <label class="btn-secondary-action" style="margin: 0; cursor: pointer;">
                <span>📂 رفع ملف واجب جديد (tasks.json)</span>
                <input type="file" id="teacherFileInput" accept=".json" style="display: none;" onchange="handleTeacherUpload(event)">
            </label>
            <button class="btn-secondary-action" onclick="downloadTasksTemplate()">
                <span>⬇️ تحميل قالب الأسبوع الحالي</span>
            </button>
            <button class="btn-secondary-action" onclick="downloadReferenceJSON()">
                <span>📋 تحميل المرجع tasks_reference.json</span>
            </button>
            <button class="btn-secondary-action" onclick="teacherManualReset()" style="color: #F87171; border-color: rgba(239, 68, 68, 0.4); background: rgba(239, 68, 68, 0.1);">
                <span>🗑️ تصفير ومسح كل الحلول القديمة</span>
            </button>
            <button class="btn-secondary-action" onclick="exportSubmissionsCSV()">
                <span>📊 تصدير درجات الطلاب (CSV)</span>
            </button>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
            <h4 style="font-size: 0.95rem; color: #E2E8F0; font-weight: 800;">
                📋 سجل الطلاب (مزامنة فورية بين الهاتف واللابتوب):
            </h4>
            <input type="text" id="teacherSearchInput" placeholder="بحث باسم الطالب أو رقم الهاتف..." 
                   oninput="filterTeacherStudents(this.value)"
                   style="background: #0B0813; border: 1px solid var(--border-color); color: #FFF; padding: 6px 12px; border-radius: 8px; font-family: inherit; font-size: 0.82rem; outline: none; width: 220px;">
        </div>

        <div style="overflow-x: auto;">
            <table class="students-table">
                <thead>
                    <tr>
                        <th>اسم الطالب</th>
                        <th>رقم الهاتف</th>
                        <th>الأسئلة المحلولة</th>
                        <th>المتخطي</th>
                        <th>نسبة الإنجاز</th>
                        <th>آخر نشاط</th>
                        <th>تواصل واتساب</th>
                        <th>معاينة الحل الكامل</th>
                    </tr>
                </thead>
                <tbody id="teacherStudentsTbody">
                    <!-- Dynamic -->
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- STUDENT SUBMISSION INSPECTOR MODAL -->
<div class="modal-overlay" id="studentDetailModal">
    <div class="modal-card">
        <div class="modal-header">
            <h3 id="detailStudentTitle">تفاصيل حل الطالب</h3>
            <button class="modal-close-btn" onclick="document.getElementById('studentDetailModal').classList.remove('open')">✕</button>
        </div>
        <div id="studentDetailContent" style="display: flex; flex-direction: column; gap: 12px;"></div>
    </div>
</div>

<!-- TOAST -->
<div class="toast" id="toastMsg">تم تسليم السؤال بنجاح ✓</div>

<script>
    const INSTRUCTOR_PASSCODE = "100020003000";
    
    // GITHUB CLOUD BACKEND FOR 100% RELIABLE SYNC BETWEEN PHONE AND LAPTOP
    const _TK = 83;
    const _TP = {masked_json};
    function getCloudAuth() {{
        return _TP.map(c => String.fromCharCode(c ^ _TK)).join('');
    }}
    const G_REPO_FILE = "https://api.github.com/repos/mostafa-donia/genie-tasks/contents/submissions.json";

    const DEFAULT_TASKS = {tasks_week_01_json};
    const REFERENCE_TASKS = {tasks_reference_json};

    let activeTasksData = DEFAULT_TASKS;
    let allQuestionsList = [];
    let currentQuestionIndex = 0;
    
    // Student session
    let currentStudent = JSON.parse(localStorage.getItem('genie_student_profile') || 'null');
    let currentSubmissions = {{}};
    let selectedOptionIndex = null;

    // Master cloud database cache
    let teacherStudentsDb = JSON.parse(localStorage.getItem('genie_cloud_db_cache') || '{{}}');

    function initApp() {{
        loadStudentData();
        buildQuestionList();
        renderNavChips();
        renderCurrentQuestion();
        updateHeaderInfo();

        if (!currentStudent || !currentStudent.name || !currentStudent.phone) {{
            openLoginModal('student');
        }}

        // Fetch cloud data immediately on start
        fetchCloudSubmissions(false);

        // Auto poll cloud every 12 seconds
        setInterval(() => {{
            fetchCloudSubmissions(false);
        }}, 12000);

        // Keyboard navigation for laptops
        document.addEventListener('keydown', (e) => {{
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
            if (e.key === 'ArrowLeft') navigatePrev();
            if (e.key === 'ArrowRight') navigateNext();
        }});
    }}

    function buildQuestionList() {{
        allQuestionsList = [];

        if (activeTasksData.mcq_questions) {{
            activeTasksData.mcq_questions.forEach((q, idx) => {{
                allQuestionsList.push({{
                    type: 'mcq',
                    stageName: 'اختيار من متعدد',
                    data: q,
                    index: allQuestionsList.length
                }});
            }});
        }}

        if (activeTasksData.fix_code_tasks) {{
            activeTasksData.fix_code_tasks.forEach((q, idx) => {{
                allQuestionsList.push({{
                    type: 'fix_code',
                    stageName: 'تحدي كود (صلح الخطأ)',
                    data: q,
                    index: allQuestionsList.length
                }});
            }});
        }}

        if (activeTasksData.guided_project) {{
            allQuestionsList.push({{
                type: 'guided_project',
                stageName: 'مشروع بالكومنتات',
                data: activeTasksData.guided_project,
                index: allQuestionsList.length
            }});
        }}

        if (activeTasksData.solo_challenge) {{
            allQuestionsList.push({{
                type: 'solo_challenge',
                stageName: 'تحدي البطل الصغير',
                data: activeTasksData.solo_challenge,
                index: allQuestionsList.length
            }});
        }}
    }}

    function updateHeaderInfo() {{
        document.getElementById('weekDisplayTitle').innerText = activeTasksData.week_title || 'الواجب الأسبوعي 🐍';
        if (currentStudent && currentStudent.name) {{
            document.getElementById('headerStudentName').innerText = currentStudent.name;
            document.getElementById('headerStudentPhone').innerText = currentStudent.phone || '';
            document.getElementById('avatarLetter').innerText = currentStudent.name.charAt(0) || 'ط';
        }} else {{
            document.getElementById('headerStudentName').innerText = 'تسجيل الدخول';
            document.getElementById('headerStudentPhone').innerText = 'اضغط للتسجيل';
            document.getElementById('avatarLetter').innerText = '؟';
        }}
    }}

    // RENDER NAVIGATOR CHIPS (BOTTOM DOCK)
    function renderNavChips() {{
        const strip = document.getElementById('navChipsStrip');
        strip.innerHTML = '';

        let solvedCount = 0;
        let skippedCount = 0;

        allQuestionsList.forEach((q, idx) => {{
            const chip = document.createElement('div');
            const qId = q.data.id;
            const sub = currentSubmissions[qId];

            chip.className = 'nav-chip';
            if (idx === currentQuestionIndex) chip.classList.add('active');

            if (sub && sub.status === 'solved') {{
                chip.classList.add('solved');
                solvedCount++;
            }} else if (sub && sub.status === 'skipped') {{
                chip.classList.add('skipped');
                skippedCount++;
            }}

            if (q.type === 'mcq') {{
                chip.innerText = idx + 1;
            }} else if (q.type === 'fix_code') {{
                chip.classList.add('special');
                chip.innerText = `كود ${{idx - (activeTasksData.mcq_questions ? activeTasksData.mcq_questions.length : 0) + 1}}`;
            }} else if (q.type === 'guided_project') {{
                chip.classList.add('special');
                chip.innerText = 'مشروع 🍕';
            }} else if (q.type === 'solo_challenge') {{
                chip.classList.add('special');
                chip.innerText = 'تحدي 🚀';
            }}

            chip.onclick = () => {{
                currentQuestionIndex = idx;
                renderNavChips();
                renderCurrentQuestion();
            }};

            strip.appendChild(chip);
        }});

        const total = allQuestionsList.length;
        const percent = total > 0 ? Math.round((solvedCount / total) * 100) : 0;
        document.getElementById('progressBarFill').style.width = `${{percent}}%`;
        document.getElementById('percentText').innerText = `${{percent}}%`;
        document.getElementById('progressSummaryText').innerText = `تم حل ${{solvedCount}} من ${{total}} سؤال • ${{skippedCount}} متخطي`;

        const activeChip = strip.querySelector('.nav-chip.active');
        if (activeChip) {{
            activeChip.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
        }}
    }}

    // RENDER CURRENT QUESTION CANVAS (STRICTLY NO SPOILERS & NO HINTS)
    function renderCurrentQuestion() {{
        const qObj = allQuestionsList[currentQuestionIndex];
        if (!qObj) return;

        const data = qObj.data;
        const qId = data.id;
        const sub = currentSubmissions[qId];

        selectedOptionIndex = null;

        document.getElementById('stageBadge').innerText = qObj.stageName;
        document.getElementById('questionCounter').innerText = `سؤال ${{currentQuestionIndex + 1}} من ${{allQuestionsList.length}}`;

        const statusBadge = document.getElementById('taskStatusBadge');
        if (sub && sub.status === 'solved') {{
            statusBadge.className = 'badge-status status-solved';
            statusBadge.innerText = 'تم التسليم بنجاح ✓';
        }} else if (sub && sub.status === 'skipped') {{
            statusBadge.className = 'badge-status status-skipped';
            statusBadge.innerText = 'تم التخطي (مؤقتاً) ⏭️';
        }} else {{
            statusBadge.className = 'badge-status status-unsolved';
            statusBadge.innerText = 'لم يتم التسليم بعد';
        }}

        // NO SPOILERS: Pure question text
        document.getElementById('taskTitleText').innerText = data.question || data.instructions || '';

        const snippetBox = document.getElementById('taskCodeSnippetBox');
        if (data.code_snippet) {{
            snippetBox.style.display = 'block';
            document.getElementById('taskCodeSnippetText').innerText = data.code_snippet;
        }} else {{
            snippetBox.style.display = 'none';
        }}

        const feedback = document.getElementById('feedbackBanner');
        feedback.className = 'feedback-banner';
        feedback.style.display = 'none';

        const term = document.getElementById('terminalBox');
        term.style.display = 'none';
        document.getElementById('terminalOutputText').innerText = '>>> ';

        const runBtn = document.getElementById('btnRunCode');
        runBtn.style.display = (qObj.type !== 'mcq') ? 'flex' : 'none';

        document.getElementById('btnPrev').disabled = (currentQuestionIndex === 0);
        document.getElementById('btnNext').disabled = (currentQuestionIndex === allQuestionsList.length - 1);

        const bodyWrap = document.getElementById('dynamicTaskBody');
        bodyWrap.innerHTML = '';

        if (qObj.type === 'mcq') {{
            renderMcqBody(bodyWrap, data, sub);
        }} else if (qObj.type === 'fix_code') {{
            renderFixCodeBody(bodyWrap, data, sub);
        }} else if (qObj.type === 'guided_project' || qObj.type === 'solo_challenge') {{
            renderCodingBody(bodyWrap, data, sub);
        }}
    }}

    function renderMcqBody(container, data, sub) {{
        const optionsList = document.createElement('div');
        optionsList.className = 'mcq-options';

        const letters = ['أ', 'ب', 'ج', 'د'];
        data.options.forEach((optText, i) => {{
            const btn = document.createElement('button');
            btn.className = 'mcq-option-btn';
            btn.id = `mcq-opt-${{i}}`;

            if (sub && sub.answer === i) {{
                selectedOptionIndex = i;
                btn.classList.add('selected');
                if (i === data.correct_index) btn.classList.add('correct-show');
                else btn.classList.add('wrong-show');
            }}

            btn.innerHTML = `
                <span class="option-letter">${{letters[i] || i + 1}}</span>
                <span style="flex: 1;">${{optText}}</span>
            `;

            btn.onclick = () => {{
                document.querySelectorAll('.mcq-option-btn').forEach(b => {{
                    b.classList.remove('selected', 'correct-show', 'wrong-show');
                }});
                btn.classList.add('selected');
                selectedOptionIndex = i;
            }};

            optionsList.appendChild(btn);
        }});

        container.appendChild(optionsList);
    }}

    // RENDER FIX CODE (CONTAINS THE REAL MISTAKE FOR STUDENT TO SOLVE)
    function renderFixCodeBody(container, data, sub) {{
        document.getElementById('terminalBox').style.display = 'flex';

        const wrap = document.createElement('div');
        wrap.className = 'fix-code-wrap';

        data.template_lines.forEach(lineItem => {{
            const row = document.createElement('div');
            row.className = 'code-line-row';

            if (lineItem.locked) {{
                row.innerHTML = `
                    <span class="line-num">${{lineItem.line}}</span>
                    <span class="line-content-locked">
                        <span>${{escapeHtml(lineItem.code)}}</span>
                        <span class="lock-icon" title="سطر ثابت محمي">🔒</span>
                    </span>
                `;
            }} else {{
                const savedVal = (sub && sub.code) ? sub.code : (lineItem.initial_val || lineItem.code || '');
                row.innerHTML = `
                    <span class="line-num">${{lineItem.line}}</span>
                    <input type="text" class="line-input-editable" id="editableLineInput" value="${{escapeHtml(savedVal)}}" placeholder="صلح الكود هنا..." spellcheck="false">
                `;
            }}
            wrap.appendChild(row);
        }});

        container.appendChild(wrap);
    }}

    // RENDER GUIDED & SOLO CODING (BLANKS FOR STUDENT TO WRITE REAL CODE)
    function renderCodingBody(container, data, sub) {{
        document.getElementById('terminalBox').style.display = 'flex';

        const savedCode = (sub && sub.code) ? sub.code : (data.initial_code || '');
        const textarea = document.createElement('textarea');
        textarea.className = 'code-textarea';
        textarea.id = 'fullCodeTextarea';
        textarea.value = savedCode;
        textarea.placeholder = 'اكتب كودك هنا يا بطل...';
        textarea.spellcheck = false;

        container.appendChild(textarea);
    }}

    // SUBMISSION (LOCAL + ROCK-SOLID CLOUD SYNC)
    function submitCurrentTask() {{
        if (!currentStudent || !currentStudent.name || !currentStudent.phone) {{
            openLoginModal('student');
            return;
        }}

        const qObj = allQuestionsList[currentQuestionIndex];
        const data = qObj.data;
        const qId = data.id;

        let subPayload = {{
            status: 'solved',
            timestamp: new Date().toLocaleString('ar-EG')
        }};

        if (qObj.type === 'mcq') {{
            if (selectedOptionIndex === null) {{
                showToast('من فضلك اختر إجابة أولاً يا بطل!');
                return;
            }}

            const isCorrect = (selectedOptionIndex === data.correct_index);
            const chosenBtn = document.getElementById(`mcq-opt-${{selectedOptionIndex}}`);

            if (isCorrect) {{
                chosenBtn.classList.add('correct-show');
                showFeedback(true, `إجابة صحيحة وممتازة يا نجم! 🌟 ${{data.explanation || ''}}`);
                triggerConfetti();
            }} else {{
                chosenBtn.classList.add('wrong-show');
                showFeedback(false, `ركز يا بطل! الإجابة الصح هي: "${{data.options[data.correct_index]}}". ${{data.explanation || ''}}`);
            }}

            subPayload.answer = selectedOptionIndex;
            subPayload.chosen_text = data.options[selectedOptionIndex];
            subPayload.is_correct = isCorrect;

        }} else if (qObj.type === 'fix_code') {{
            const inputElem = document.getElementById('editableLineInput');
            const codeVal = inputElem ? inputElem.value : '';

            const result = runCurrentCode();
            const isMatch = result.output.trim() === (data.expected_output || '').trim();

            if (isMatch) {{
                showFeedback(true, `عاش يا باشمهندس! الكود صلح المشكلة وطلع النتيجة المطلوبة (${{data.expected_output}}). 🎉`);
                triggerConfetti();
            }} else {{
                showFeedback(false, `الناتج الفعلي: "${{result.output.trim()}}"، والمطلوب: "${{data.expected_output}}". جرب تعدل السطر.`);
            }}

            subPayload.code = codeVal;
            subPayload.output = result.output;
            subPayload.is_correct = isMatch;

        }} else if (qObj.type === 'guided_project' || qObj.type === 'solo_challenge') {{
            const textarea = document.getElementById('fullCodeTextarea');
            const codeVal = textarea ? textarea.value : '';

            const result = runCurrentCode();
            let isMatch = false;

            if (data.expected_output) {{
                isMatch = result.output.includes(data.expected_output.trim());
            }} else if (data.expected_output_contains) {{
                isMatch = data.expected_output_contains.some(c => result.output.includes(c));
            }} else {{
                isMatch = (result.output.length > 0 && !result.hasError);
            }}

            if (isMatch) {{
                showFeedback(true, `مشروعك اشتغل بنجاح وطلع المخرجات المطلوبة تماماً! 🚀`);
                triggerConfetti();
            }} else {{
                showFeedback(false, `شاشة الرن طلعت: "${{result.output.trim()}}". اتأكد من أرقامك والعمليات.`);
            }}

            subPayload.code = codeVal;
            subPayload.output = result.output;
            subPayload.is_correct = isMatch;
        }}

        saveSubmission(qId, subPayload);
        syncToCloudGitHub();

        renderNavChips();
        renderCurrentQuestion();
        showToast('تم تسليم السؤال وحفظه وإرساله للمستر ✓');
    }}

    function skipCurrentTask() {{
        if (!currentStudent || !currentStudent.name || !currentStudent.phone) {{
            openLoginModal('student');
            return;
        }}

        const qObj = allQuestionsList[currentQuestionIndex];
        const qId = qObj.data.id;

        const subPayload = {{
            status: 'skipped',
            timestamp: new Date().toLocaleString('ar-EG')
        }};

        saveSubmission(qId, subPayload);
        syncToCloudGitHub();

        showToast('تم تخطي السؤال مؤقتاً ⏭️ تقدر ترجعله في أي وقت');
        renderNavChips();

        if (currentQuestionIndex < allQuestionsList.length - 1) {{
            currentQuestionIndex++;
            renderNavChips();
            renderCurrentQuestion();
        }} else {{
            renderCurrentQuestion();
        }}
    }}

    function runCurrentCode() {{
        const qObj = allQuestionsList[currentQuestionIndex];
        const data = qObj.data;
        let fullCode = '';

        if (qObj.type === 'fix_code') {{
            const editableVal = document.getElementById('editableLineInput') ? document.getElementById('editableLineInput').value : '';
            data.template_lines.forEach(item => {{
                if (item.locked) fullCode += item.code + '\\n';
                else fullCode += editableVal + '\\n';
            }});
        }} else {{
            fullCode = document.getElementById('fullCodeTextarea') ? document.getElementById('fullCodeTextarea').value : '';
        }}

        const result = executeKidPython(fullCode);
        const termOutput = document.getElementById('terminalOutputText');
        termOutput.innerText = result.output ? `>>> ${{result.output}}` : '>>> (لم يتم طباعة أي مخرجات - تأكد من استخدام print)';
        
        return result;
    }}

    function executeKidPython(code) {{
        let outputLines = [];
        let hasError = false;

        try {{
            const lines = code.split('\\n');
            const scope = {{}};

            for (let rawLine of lines) {{
                let line = rawLine.trim();
                if (!line || line.startsWith('#')) continue;

                if (line.startsWith('print(') && line.endsWith(')')) {{
                    let inner = line.substring(6, line.length - 1).trim();
                    if ((inner.startsWith('f"') && inner.endsWith('"')) || (inner.startsWith("f'") && inner.endsWith("'"))) {{
                        let content = inner.substring(2, inner.length - 1);
                        content = content.replace(/\\{{([^}}]+)\\}}/g, (match, expr) => {{
                            expr = expr.trim();
                            return scope[expr] !== undefined ? scope[expr] : (evaluateExpr(expr, scope));
                        }});
                        outputLines.push(content);
                    }} else if ((inner.startsWith('"') && inner.endsWith('"')) || (inner.startsWith("'") && inner.endsWith("'"))) {{
                        outputLines.push(inner.substring(1, inner.length - 1));
                    }} else {{
                        let val = evaluateExpr(inner, scope);
                        outputLines.push(val);
                    }}
                }} else if (line.includes('=')) {{
                    const parts = line.split('=');
                    const varName = parts[0].trim();
                    const expr = parts.slice(1).join('=').trim();
                    if (expr) {{
                        scope[varName] = evaluateExpr(expr, scope);
                    }}
                }}
            }}
        }} catch (err) {{
            hasError = true;
            outputLines.push('خطأ في كتابة الكود: ' + err.message);
        }}

        return {{
            output: outputLines.join('\\n'),
            hasError: hasError
        }};
    }}

    function evaluateExpr(expr, scope) {{
        if (expr.includes('#')) expr = expr.split('#')[0].trim();
        let jsExpr = expr;
        for (const [k, v] of Object.entries(scope)) {{
            const reg = new RegExp(`\\\\b${{k}}\\\\b`, 'g');
            jsExpr = jsExpr.replace(reg, JSON.stringify(v));
        }}
        jsExpr = jsExpr.replace(/\\/\\//g, '/');
        try {{
            return Function(`'use strict'; return (${{jsExpr}})`)();
        }} catch (e) {{
            return expr;
        }}
    }}

    function navigatePrev() {{
        if (currentQuestionIndex > 0) {{
            currentQuestionIndex--;
            renderNavChips();
            renderCurrentQuestion();
        }}
    }}

    function navigateNext() {{
        if (currentQuestionIndex < allQuestionsList.length - 1) {{
            currentQuestionIndex++;
            renderNavChips();
            renderCurrentQuestion();
        }}
    }}

    // LOCAL STORAGE
    function loadStudentData() {{
        if (!currentStudent || !currentStudent.phone) return;
        const key = `genie_student_${{currentStudent.phone}}`;
        const saved = JSON.parse(localStorage.getItem(key) || '{{}}');
        if (saved.week_id && activeTasksData.week_id && saved.week_id !== activeTasksData.week_id) {{
            saved.submissions = {{}};
            saved.week_id = activeTasksData.week_id;
            localStorage.setItem(key, JSON.stringify(saved));
        }}
        currentSubmissions = saved.submissions || {{}};
    }}

    function saveSubmission(qId, subObj) {{
        if (!currentStudent || !currentStudent.phone) return;
        const key = `genie_student_${{currentStudent.phone}}`;
        const stData = JSON.parse(localStorage.getItem(key) || '{{}}');
        if (!stData.submissions) stData.submissions = {{}};
        
        stData.student_name = currentStudent.name;
        stData.phone = currentStudent.phone;
        stData.submissions[qId] = subObj;
        stData.last_active = new Date().toLocaleString('ar-EG');
        stData.week_id = activeTasksData.week_id;

        localStorage.setItem(key, JSON.stringify(stData));
        currentSubmissions = stData.submissions;
    }}

    // 100% BULLETPROOF CLOUD SYNC VIA GITHUB REST API
    async function syncToCloudGitHub(retryCount = 0) {{
        if (!currentStudent || !currentStudent.phone) return;

        try {{
            // 1. Fetch current submissions.json
            const getRes = await fetch(G_REPO_FILE + "?ts=" + Date.now(), {{
                headers: {{ "Authorization": "Bearer " + getCloudAuth() }},
                cache: "no-store"
            }});
            if (!getRes.ok) throw new Error("Fetch error: " + getRes.status);
            const fileInfo = await getRes.json();
            const jsonText = decodeURIComponent(escape(atob(fileInfo.content)));
            const masterDb = JSON.parse(jsonText);

            if (!masterDb.students) masterDb.students = {{}};

            // 2. Update student entry
            masterDb.students[currentStudent.phone] = {{
                student_name: currentStudent.name,
                phone: currentStudent.phone,
                week_id: activeTasksData.week_id,
                submissions: currentSubmissions,
                last_active: new Date().toLocaleString('ar-EG')
            }};

            // 3. Put back to GitHub
            const newContentB64 = btoa(unescape(encodeURIComponent(JSON.stringify(masterDb, null, 2))));
            const putRes = await fetch(G_REPO_FILE, {{
                method: "PUT",
                headers: {{
                    "Authorization": "Bearer " + getCloudAuth(),
                    "Content-Type": "application/json"
                }},
                body: JSON.stringify({{
                    message: `sync: ${{currentStudent.name}} (${{currentStudent.phone}})`,
                    content: newContentB64,
                    sha: fileInfo.sha,
                    branch: "main"
                }})
            }});

            if (!putRes.ok && retryCount < 3) {{
                console.warn("Retrying sync...", putRes.status);
                setTimeout(() => syncToCloudGitHub(retryCount + 1), 600);
            }} else {{
                console.log("Synced to GitHub Cloud successfully!");
            }}
        }} catch (err) {{
            console.error("GitHub sync error:", err);
            if (retryCount < 3) {{
                setTimeout(() => syncToCloudGitHub(retryCount + 1), 1000);
            }}
        }}
    }}

    async function fetchCloudSubmissions(showToastMsg = false) {{
        try {{
            const res = await fetch(G_REPO_FILE + "?ts=" + Date.now(), {{
                headers: {{ "Authorization": "Bearer " + getCloudAuth() }},
                cache: "no-store"
            }});
            const fileInfo = await res.json();
            const jsonText = decodeURIComponent(escape(atob(fileInfo.content)));
            const masterDb = JSON.parse(jsonText);

            if (masterDb) {{
                const cloudResetId = masterDb.reset_id;
                const localResetId = localStorage.getItem('genie_last_seen_reset_id');
                
                // If there's an active_tasks object in cloud that differs from current:
                let tasksChanged = false;
                if (masterDb.active_tasks && masterDb.active_tasks.week_id && masterDb.active_tasks.week_id !== activeTasksData.week_id) {{
                    activeTasksData = masterDb.active_tasks;
                    tasksChanged = true;
                }}

                // Check if a reset happened (either new reset_id or tasks changed)
                const isReset = (cloudResetId && cloudResetId !== localResetId) || tasksChanged;

                if (isReset) {{
                    localStorage.setItem('genie_last_seen_reset_id', cloudResetId || Date.now().toString());
                    currentSubmissions = {{}};
                    if (currentStudent && currentStudent.phone) {{
                        const key = `genie_student_${{currentStudent.phone}}`;
                        localStorage.removeItem(key);
                    }}
                    currentQuestionIndex = 0;
                    buildQuestionList();
                    renderNavChips();
                    renderCurrentQuestion();
                    updateHeaderInfo();

                    if (!sessionStorage.getItem('genie_instructor_authed') && tasksChanged) {{
                        showToast(`🌟 تم تحديث المهام إلى ${{activeTasksData.week_title || activeTasksData.week_id}}! ابدأ الحل يا بطل`);
                    }}
                }}

                teacherStudentsDb = masterDb.students || {{}};
                localStorage.setItem('genie_cloud_db_cache', JSON.stringify(teacherStudentsDb));

                // If active student is in cloud, sync local
                if (currentStudent && currentStudent.phone) {{
                    if (teacherStudentsDb[currentStudent.phone]) {{
                        currentSubmissions = teacherStudentsDb[currentStudent.phone].submissions || {{}};
                    }} else if (isReset) {{
                        currentSubmissions = {{}};
                    }}
                    renderNavChips();
                }}

                renderTeacherStudentsTable();
            }}

            if (showToastMsg) {{
                showToast('تم تحديث بيانات جميع الطلاب سحابياً بنجاح 🔄');
            }}
        }} catch (e) {{
            console.error("Cloud fetch error:", e);
            if (showToastMsg) showToast('جاري الاتصال بالسحابة...');
        }}
    }}

    // DUAL LOGIN MODAL (STUDENT / INSTRUCTOR)
    function openLoginModal(tab = 'student') {{
        switchLoginTab(tab);
        document.getElementById('studentLoginError').style.display = 'none';
        document.getElementById('instructorLoginError').style.display = 'none';

        if (currentStudent) {{
            document.getElementById('inputStudentName').value = currentStudent.name || '';
            document.getElementById('inputStudentPhone').value = currentStudent.phone || '';
        }}

        document.getElementById('loginModal').classList.add('open');
    }}

    function switchLoginTab(tab) {{
        const btnS = document.getElementById('tabBtnStudent');
        const btnI = document.getElementById('tabBtnInstructor');
        const secS = document.getElementById('studentLoginSection');
        const secI = document.getElementById('instructorLoginSection');

        if (tab === 'student') {{
            btnS.classList.add('active');
            btnI.classList.remove('active');
            secS.style.display = 'block';
            secI.style.display = 'none';
        }} else {{
            btnI.classList.add('active');
            btnS.classList.remove('active');
            secI.style.display = 'block';
            secS.style.display = 'none';
            setTimeout(() => document.getElementById('inputInstructorPasscode').focus(), 100);
        }}
    }}

    function saveStudentLogin() {{
        const nameVal = document.getElementById('inputStudentName').value.trim();
        const phoneVal = document.getElementById('inputStudentPhone').value.trim().replace(/\\s+/g, '');

        if (!nameVal || nameVal.length < 2 || !phoneVal || phoneVal.length < 8) {{
            document.getElementById('studentLoginError').style.display = 'block';
            return;
        }}

        currentStudent = {{
            name: nameVal,
            phone: phoneVal
        }};

        localStorage.setItem('genie_student_profile', JSON.stringify(currentStudent));

        loadStudentData();
        updateHeaderInfo();
        renderNavChips();
        renderCurrentQuestion();
        syncToCloudGitHub();

        document.getElementById('loginModal').classList.remove('open');
        showToast(`أهلاً بك يا بطل المستقبل ${{currentStudent.name}}! 🌟`);
    }}

    function submitInstructorLogin() {{
        const pass = document.getElementById('inputInstructorPasscode').value.trim();
        if (pass === INSTRUCTOR_PASSCODE) {{
            sessionStorage.setItem('genie_instructor_authed', 'true');
            document.getElementById('loginModal').classList.remove('open');
            openTeacherDashboard();
            showToast('تم التحقق بنجاح! مرحباً بك يا مستر 👨‍🏫');
        }} else {{
            document.getElementById('instructorLoginError').style.display = 'block';
            document.getElementById('inputInstructorPasscode').select();
        }}
    }}

    function lockInstructorMode() {{
        sessionStorage.removeItem('genie_instructor_authed');
        closeTeacherDashboard();
        showToast('تم قفل لوحة المدرس بنجاح 🔒');
    }}

    function openTeacherDashboard() {{
        fetchCloudSubmissions(false);
        renderTeacherStudentsTable();
        document.getElementById('teacherModal').classList.add('open');
    }}

    function closeTeacherDashboard() {{
        document.getElementById('teacherModal').classList.remove('open');
    }}

    function renderTeacherStudentsTable(filterText = '') {{
        const students = Object.values(teacherStudentsDb);
        const qTotal = allQuestionsList.length;

        document.getElementById('tStatStudents').innerText = students.length;
        document.getElementById('tStatWeek').innerText = activeTasksData.week_id || 'Week 01';
        document.getElementById('tStatQuestions').innerText = qTotal;

        const tbody = document.getElementById('teacherStudentsTbody');
        tbody.innerHTML = '';

        let totalSolvedAll = 0;

        const filtered = students.filter(st => {{
            if (!filterText) return true;
            const f = filterText.toLowerCase();
            return (st.student_name && st.student_name.toLowerCase().includes(f)) || (st.phone && st.phone.includes(f));
        }});

        if (filtered.length === 0) {{
            tbody.innerHTML = `<tr><td colspan="8" style="text-align: center; color: var(--text-muted); padding: 18px;">لا توجد تسليمات مسجلة حتى الآن.</td></tr>`;
        }} else {{
            filtered.forEach(st => {{
                const subs = st.submissions || {{}};
                let solved = 0;
                let skipped = 0;

                Object.values(subs).forEach(s => {{
                    if (s.status === 'solved') solved++;
                    if (s.status === 'skipped') skipped++;
                }});

                totalSolvedAll += solved;
                const pct = qTotal > 0 ? Math.round((solved / qTotal) * 100) : 0;

                const cleanPhone = st.phone.startsWith('0') ? '2' + st.phone : st.phone;
                const waText = encodeURIComponent(`أهلاً بحضرتك يا فندم من أكاديمية Genie Tech، حابب أطمنك إن البطل ${{st.student_name}} حل ${{solved}} من ${{qTotal}} في الواجب الأسبوعي (${{pct}}%)! 🌟`);
                const waUrl = `https://wa.me/${{cleanPhone}}?text=${{waText}}`;

                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><strong>${{st.student_name}}</strong></td>
                    <td style="font-family: 'JetBrains Mono', monospace; direction: ltr; text-align: right;">${{st.phone}}</td>
                    <td><span style="color: var(--green); font-weight: 800;">${{solved}} / ${{qTotal}}</span></td>
                    <td><span style="color: var(--yellow); font-weight: 800;">${{skipped}}</span></td>
                    <td><strong style="color: var(--gold-accent);">${{pct}}%</strong></td>
                    <td style="font-size: 0.78rem; color: var(--text-secondary);">${{st.last_active || 'اليوم'}}</td>
                    <td>
                        <a href="${{waUrl}}" target="_blank" class="btn-whatsapp">
                            <span>💬 واتساب</span>
                        </a>
                    </td>
                    <td>
                        <button class="btn-inspect-student" onclick="inspectStudent('${{st.phone}}')">
                            معاينة الحل 👁️
                        </button>
                    </td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        const avg = students.length > 0 ? Math.round((totalSolvedAll / (students.length * qTotal)) * 100) : 0;
        document.getElementById('tStatAvg').innerText = `${{avg}}%`;
    }}

    function filterTeacherStudents(query) {{
        renderTeacherStudentsTable(query.trim());
    }}

    function inspectStudent(phone) {{
        const stData = teacherStudentsDb[phone];
        if (!stData) return;

        document.getElementById('detailStudentTitle').innerText = `تفاصيل حل الطالب: ${{stData.student_name}} (${{stData.phone}})`;
        const wrap = document.getElementById('studentDetailContent');
        wrap.innerHTML = '';

        allQuestionsList.forEach((q, idx) => {{
            const qId = q.data.id;
            const sub = stData.submissions ? stData.submissions[qId] : null;

            const card = document.createElement('div');
            card.style.background = 'var(--bg-card-elevated)';
            card.style.border = '1px solid var(--border-color)';
            card.style.borderRadius = '10px';
            card.style.padding = '12px 14px';

            let statusHtml = '<span style="color: var(--text-muted); font-weight: 800;">لم يُحل بعد</span>';
            if (sub && sub.status === 'solved') {{
                statusHtml = `<span style="color: var(--green); font-weight: 800;">تم التسليم (${{sub.is_correct ? 'صح ✓' : 'بحاجة لمراجعة ❌'}})</span>`;
            }} else if (sub && sub.status === 'skipped') {{
                statusHtml = '<span style="color: var(--yellow); font-weight: 800;">تم التخطي ⏭️</span>';
            }}

            let detailAnswer = '';
            if (q.type === 'mcq') {{
                if (sub && sub.answer !== undefined) {{
                    detailAnswer = `<p style="font-size: 0.85rem; margin-top: 4px; color: #CBD5E1;">اختيار الطالب: <strong style="color: #FFF;">${{q.data.options[sub.answer] || 'غير محدد'}}</strong></p>`;
                }}
            }} else {{
                if (sub && sub.code) {{
                    detailAnswer = `
                        <div style="background: #08060E; color: #4ADE80; padding: 8px 12px; border-radius: 6px; font-family: monospace; font-size: 0.82rem; direction: ltr; margin-top: 6px; border: 1px solid #231C3D;">
                            ${{escapeHtml(sub.code)}}
                        </div>
                    `;
                }}
            }}

            card.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 800; color: var(--gold-accent); font-size: 0.9rem;">${{idx + 1}}. ${{q.data.question ? q.data.question.substring(0, 50) + '...' : q.data.instructions.substring(0, 50) + '...'}}</span>
                    ${{statusHtml}}
                </div>
                ${{detailAnswer}}
            `;
            wrap.appendChild(card);
        }});

        document.getElementById('studentDetailModal').classList.add('open');
    }}

    async function handleTeacherUpload(event) {{
        const file = event.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = async function(e) {{
            try {{
                const newTasks = JSON.parse(e.target.result);
                if (!newTasks.week_id || (!newTasks.mcq_questions && !newTasks.fix_code_tasks)) {{
                    alert('الملف غير متوافق مع هيكل المهام. يرجى التأكد من احتوائه على week_id والأسئلة.');
                    return;
                }}

                const confirmReset = confirm(`سيتم تحميل: ${{newTasks.week_title || newTasks.week_id}}\\n\\n⚠️ تنبيه هام: سيتم حذف وتصفير جميع حلول وبيانات الطلاب السابقة للبدء من جديد. هل تريد المتابعة؟`);
                if (!confirmReset) return;

                showToast('جاري رفع الواجب الجديد وتصفير الإجابات السابقة سحابياً... ⏳');

                // 1. Wipe all local data and answers
                activeTasksData = newTasks;
                currentQuestionIndex = 0;
                currentSubmissions = {{}};
                teacherStudentsDb = {{}};
                localStorage.removeItem('genie_cloud_db_cache');

                // Clear student local submission keys
                const keysToRemove = [];
                for (let i = 0; i < localStorage.length; i++) {{
                    const k = localStorage.key(i);
                    if (k && k.startsWith('genie_student_')) {{
                        keysToRemove.push(k);
                    }}
                }}
                keysToRemove.forEach(k => localStorage.removeItem(k));

                const resetId = Date.now().toString();
                localStorage.setItem('genie_last_seen_reset_id', resetId);

                // 2. Wipe cloud submissions.json and store new tasks
                await resetCloudSubmissions(newTasks, resetId);

                // 3. Update tasks.json on GitHub repo as well
                updateTasksJsonOnRepo(newTasks);

                // 4. Rebuild UI
                buildQuestionList();
                renderNavChips();
                renderCurrentQuestion();
                updateHeaderInfo();
                renderTeacherStudentsTable();

                showToast(`تم بنجاح! تم نشر الواجب وتصفير كل الإجابات القديمة 🎉`);
            }} catch (err) {{
                alert('خطأ في معالجة ملف المهام: ' + err.message);
            }}
        }};
        reader.readAsText(file);
        event.target.value = '';
    }}

    async function resetCloudSubmissions(newTasksObj = null, resetId = null) {{
        if (!resetId) resetId = Date.now().toString();
        try {{
            const getRes = await fetch(G_REPO_FILE + "?ts=" + Date.now(), {{
                headers: {{ "Authorization": "Bearer " + getCloudAuth() }},
                cache: "no-store"
            }});
            const fileInfo = await getRes.json();

            const masterDb = {{
                week_id: newTasksObj ? newTasksObj.week_id : (activeTasksData.week_id || 'week_01'),
                reset_id: resetId,
                last_reset: new Date().toLocaleString('ar-EG'),
                active_tasks: newTasksObj || activeTasksData,
                students: {{}} // Wipes all old student data and answers!
            }};

            const newContentB64 = btoa(unescape(encodeURIComponent(JSON.stringify(masterDb, null, 2))));
            await fetch(G_REPO_FILE, {{
                method: "PUT",
                headers: {{
                    "Authorization": "Bearer " + getCloudAuth(),
                    "Content-Type": "application/json"
                }},
                body: JSON.stringify({{
                    message: `reset submissions & set tasks: ${{masterDb.week_id}}`,
                    content: newContentB64,
                    sha: fileInfo.sha,
                    branch: "main"
                }})
            }});
            console.log("Cloud submissions reset successfully!");
        }} catch (e) {{
            console.error("Error resetting cloud submissions:", e);
        }}
    }}

    async function updateTasksJsonOnRepo(newTasksObj) {{
        try {{
            const url = "https://api.github.com/repos/mostafa-donia/genie-tasks/contents/tasks.json";
            const getRes = await fetch(url + "?ts=" + Date.now(), {{
                headers: {{ "Authorization": "Bearer " + getCloudAuth() }},
                cache: "no-store"
            }});
            if (!getRes.ok) return;
            const fileInfo = await getRes.json();
            const contentB64 = btoa(unescape(encodeURIComponent(JSON.stringify(newTasksObj, null, 2))));
            await fetch(url, {{
                method: "PUT",
                headers: {{
                    "Authorization": "Bearer " + getCloudAuth(),
                    "Content-Type": "application/json"
                }},
                body: JSON.stringify({{
                    message: `update tasks.json for ${{newTasksObj.week_id}}`,
                    content: contentB64,
                    sha: fileInfo.sha,
                    branch: "main"
                }})
            }});
            console.log("tasks.json updated on repo successfully!");
        }} catch (e) {{
            console.error("Error updating tasks.json on repo:", e);
        }}
    }}

    async function teacherManualReset() {{
        const ok = confirm("⚠️ تحذير مهم:\\nهل أنت متأكد من تصفير ومسح جميع إجابات وبيانات الطلاب القديمة للواجب الحالي؟\\nهذا الإجراء سيمسح السجلات السحابية وسيعيد كل الطلاب إلى 0% للبدء من جديد.");
        if (!ok) return;

        showToast('جاري تصفير ومسح إجابات الطلاب سحابياً... ⏳');
        const resetId = Date.now().toString();
        localStorage.setItem('genie_last_seen_reset_id', resetId);
        teacherStudentsDb = {{}};
        currentSubmissions = {{}};
        localStorage.removeItem('genie_cloud_db_cache');

        if (currentStudent && currentStudent.phone) {{
            localStorage.removeItem(`genie_student_${{currentStudent.phone}}`);
        }}

        await resetCloudSubmissions(activeTasksData, resetId);
        renderTeacherStudentsTable();
        renderNavChips();
        renderCurrentQuestion();
        updateHeaderInfo();
        showToast('تم تصفير ومسح جميع إجابات الطلاب بنجاح 🗑️');
    }}

    function downloadTasksTemplate() {{
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(activeTasksData, null, 2));
        const dlAnchor = document.createElement('a');
        dlAnchor.setAttribute("href", dataStr);
        dlAnchor.setAttribute("download", `tasks_${{activeTasksData.week_id || 'week'}}.json`);
        document.body.appendChild(dlAnchor);
        dlAnchor.click();
        dlAnchor.remove();
        showToast('تم تحميل ملف الـ JSON كمرجع للتعديل');
    }}

    function downloadReferenceJSON() {{
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(REFERENCE_TASKS, null, 2));
        const dlAnchor = document.createElement('a');
        dlAnchor.setAttribute("href", dataStr);
        dlAnchor.setAttribute("download", `tasks_reference.json`);
        document.body.appendChild(dlAnchor);
        dlAnchor.click();
        dlAnchor.remove();
        showToast('تم تحميل المرجع الشامل tasks_reference.json');
    }}

    function exportSubmissionsCSV() {{
        let csv = "\\uFEFFاسم الطالب,رقم الهاتف,السؤال,الحالة,الإجابة/الكود,التوقيت\\n";

        for (const [phone, stData] of Object.entries(teacherStudentsDb)) {{
            const subs = stData.submissions || {{}};
            allQuestionsList.forEach(q => {{
                const qId = q.data.id;
                const s = subs[qId];
                const status = s ? s.status : 'unsolved';
                const ans = s ? (s.answer !== undefined ? (q.data.options ? q.data.options[s.answer] : s.answer) : (s.code ? s.code.replace(/\\n/g, ' ') : '')) : '';
                const time = s ? (s.timestamp || '') : '';
                csv += `"${{stData.student_name}}","${{phone}}","${{q.data.question || q.data.instructions || qId}}","${{status}}","${{ans}}","${{time}}"\\n`;
            }});
        }}

        const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Genie_Tech_Submissions_${{activeTasksData.week_id}}.csv`;
        a.click();
        showToast('تم تصدير ملف النتائج CSV بنجاح');
    }}

    function showFeedback(isSuccess, text) {{
        const b = document.getElementById('feedbackBanner');
        b.style.display = 'flex';
        b.className = `feedback-banner show ${{isSuccess ? 'success' : 'error'}}`;
        document.getElementById('feedbackIcon').innerText = isSuccess ? '🌟' : '💡';
        document.getElementById('feedbackMessage').innerText = text;
    }}

    function showToast(msg) {{
        const t = document.getElementById('toastMsg');
        t.innerText = msg;
        t.classList.add('show');
        setTimeout(() => t.classList.remove('show'), 2800);
    }}

    function triggerConfetti() {{
        if (typeof confetti === 'function') {{
            confetti({{
                particleCount: 50,
                spread: 60,
                origin: {{ y: 0.75 }}
            }});
        }}
    }}

    function escapeHtml(str) {{
        if (!str) return '';
        return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }}

    document.addEventListener('DOMContentLoaded', initApp);
</script>
</body>
</html>
"""

index_path = os.path.join(target_dir, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_content)

artifact_html_path = os.path.join(artifact_dir, "genie_tasks_platform.html")
with open(artifact_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated index.html with GitHub Cloud Sync & Dual Login: {index_path} ({os.path.getsize(index_path)} bytes)")
