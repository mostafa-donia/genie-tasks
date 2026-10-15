import json
import os

target_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\genie-tasks-platform"
artifact_dir = r"C:\Users\Admin\.gemini\antigravity\brain\254f8f1d-ee3b-47dd-abe1-87a1bb03754d"

logo_path = os.path.join(artifact_dir, "logo_base64.txt")
with open(logo_path, "r", encoding="utf-8") as f:
    logo_base64 = f.read().strip()

with open(os.path.join(target_dir, "tasks.json"), "r", encoding="utf-8") as f:
    tasks_week_01_json = f.read()

with open(os.path.join(target_dir, "tasks_reference.json"), "r", encoding="utf-8") as f:
    tasks_reference_json = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تاسكات Genie Tech التعليمية للأبطال 🐍 | Interactive Python Tasks</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
    <!-- Confetti JS for fun rewards -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {{
            --bg-page: #FAF7F0;
            --bg-card: #FFFFFF;
            --text-primary: #1A1235;
            --text-secondary: #58506D;
            --text-muted: #8E87A2;
            --border-color: #E8E2D2;
            
            --purple-primary: #4E2799;
            --purple-light: #F3E8FF;
            --purple-hover: #3E1F7C;
            --gold-accent: #F5A623;
            --gold-light: #FEF3D6;
            
            --green: #10B981;
            --green-light: #D1FAE5;
            --yellow: #F59E0B;
            --yellow-light: #FEF3C7;
            --red: #EF4444;
            --red-light: #FEE2E2;
            --blue: #3B82F6;
            --blue-light: #DBEAFE;

            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --radius-xl: 28px;
            --shadow-sm: 0 2px 8px rgba(78, 39, 153, 0.04);
            --shadow-md: 0 6px 20px rgba(78, 39, 153, 0.08);
            --shadow-lg: 0 14px 34px rgba(78, 39, 153, 0.12);
            --transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Cairo', 'Inter', -apple-system, sans-serif;
            background-color: var(--bg-page);
            color: var(--text-primary);
            line-height: 1.5;
            min-height: 100vh;
            padding: 16px;
        }}

        .container {{
            max-width: 1080px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        /* TOP NAVBAR */
        .app-header {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 14px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-sm);
            flex-wrap: wrap;
            gap: 12px;
        }}

        .brand-section {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .brand-logo {{
            width: 52px;
            height: 52px;
            background: linear-gradient(135deg, var(--purple-light), #fff);
            border: 2px solid var(--purple-primary);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2px;
            box-shadow: 0 4px 10px rgba(78, 39, 153, 0.1);
        }}

        .brand-logo img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}

        .brand-titles h1 {{
            font-size: 1.25rem;
            font-weight: 900;
            color: var(--purple-primary);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .brand-titles p {{
            font-size: 0.82rem;
            color: var(--text-secondary);
            font-weight: 700;
        }}

        .student-pill {{
            background: var(--bg-page);
            border: 1px solid var(--border-color);
            border-radius: 30px;
            padding: 6px 14px;
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            transition: var(--transition);
        }}

        .student-pill:hover {{
            border-color: var(--purple-primary);
            background: var(--purple-light);
        }}

        .student-avatar {{
            width: 28px;
            height: 28px;
            background: var(--purple-primary);
            color: #fff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 800;
        }}

        .student-name-text {{
            font-size: 0.9rem;
            font-weight: 800;
            color: var(--text-primary);
        }}

        .btn-teacher-toggle {{
            background: var(--gold-light);
            border: 1px solid var(--gold-accent);
            color: #B45309;
            font-family: inherit;
            font-size: 0.85rem;
            font-weight: 800;
            padding: 7px 14px;
            border-radius: 12px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: var(--transition);
        }}

        .btn-teacher-toggle:hover {{
            background: var(--gold-accent);
            color: #FFFFFF;
        }}

        /* PROGRESS & QUESTION NAVIGATOR MAP */
        .navigator-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 12px 18px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            box-shadow: var(--shadow-sm);
        }}

        .navigator-top {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--text-secondary);
        }}

        .progress-bar-bg {{
            width: 100%;
            height: 8px;
            background: var(--bg-page);
            border-radius: 20px;
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
            padding-bottom: 4px;
        }}

        .nav-chip {{
            min-width: 38px;
            height: 38px;
            border-radius: 10px;
            border: 1px solid var(--border-color);
            background: var(--bg-page);
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
            position: relative;
        }}

        .nav-chip:hover {{
            border-color: var(--purple-primary);
            transform: translateY(-2px);
        }}

        .nav-chip.active {{
            border: 2px solid var(--purple-primary);
            box-shadow: 0 0 0 3px rgba(78, 39, 153, 0.15);
            font-weight: 900;
        }}

        .nav-chip.solved {{
            background: var(--green);
            color: #FFFFFF;
            border-color: var(--green);
        }}

        .nav-chip.skipped {{
            background: var(--yellow-light);
            color: #B45309;
            border-color: var(--yellow);
        }}

        .nav-chip.special {{
            min-width: 60px;
            font-size: 0.75rem;
            font-family: 'Cairo', sans-serif;
        }}

        /* MAIN TASK STAGE CARD (FOCUSED 1-QUESTION VIEW) */
        .task-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            padding: 24px 28px;
            box-shadow: var(--shadow-md);
            display: flex;
            flex-direction: column;
            gap: 18px;
            min-height: 480px;
        }}

        .task-header-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 12px;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .task-badge-group {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .badge-stage {{
            background: var(--purple-light);
            color: var(--purple-primary);
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
            background: var(--bg-page);
            color: var(--text-muted);
        }}

        .status-solved {{
            background: var(--green-light);
            color: #065F46;
        }}

        .status-skipped {{
            background: var(--yellow-light);
            color: #B45309;
        }}

        .task-title {{
            font-size: 1.35rem;
            font-weight: 900;
            color: var(--text-primary);
            line-height: 1.4;
        }}

        .task-hint-box {{
            background: var(--bg-page);
            border-right: 4px solid var(--gold-accent);
            border-radius: 8px;
            padding: 10px 14px;
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--text-secondary);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        /* CODE BLOCK DISPLAY (VS Code style) */
        .code-box {{
            background: #1E1B2E;
            color: #F8F8F2;
            border-radius: 12px;
            padding: 14px 16px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.95rem;
            direction: ltr;
            text-align: left;
            position: relative;
            overflow-x: auto;
            border: 1px solid #2D274A;
        }}

        /* MCQ OPTIONS LIST */
        .mcq-options {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .mcq-option-btn {{
            background: var(--bg-page);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 14px 18px;
            font-family: inherit;
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-primary);
            text-align: right;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .mcq-option-btn:hover {{
            border-color: var(--purple-primary);
            background: #FFFFFF;
            transform: translateX(-4px);
        }}

        .mcq-option-btn.selected {{
            border-color: var(--purple-primary);
            background: var(--purple-light);
            color: var(--purple-primary);
            font-weight: 800;
        }}

        .mcq-option-btn.correct-show {{
            border-color: var(--green);
            background: var(--green-light);
            color: #065F46;
        }}

        .mcq-option-btn.wrong-show {{
            border-color: var(--red);
            background: var(--red-light);
            color: #991B1B;
        }}

        .option-letter {{
            width: 30px;
            height: 30px;
            background: #FFFFFF;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--purple-primary);
            flex-shrink: 0;
        }}

        /* FIX CODE EDITOR INTERFACE */
        .fix-code-wrap {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            background: #1E1B2E;
            border-radius: 12px;
            padding: 14px;
            border: 1px solid #2D274A;
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
            color: #6C6789;
            width: 24px;
            text-align: right;
            user-select: none;
            font-size: 0.82rem;
        }}

        .line-content-locked {{
            color: #E2E8F0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .lock-icon {{
            font-size: 0.75rem;
            color: #94A3B8;
        }}

        .line-input-editable {{
            flex: 1;
            background: #2D274A;
            border: 1px solid #6366F1;
            color: #F8FAFC;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.95rem;
            padding: 6px 10px;
            border-radius: 6px;
            outline: none;
        }}

        .line-input-editable:focus {{
            border-color: var(--gold-accent);
            box-shadow: 0 0 0 2px rgba(245, 166, 35, 0.3);
        }}

        /* FULL CODE TEXTAREA (Guided & Solo) */
        .code-textarea {{
            width: 100%;
            height: 180px;
            background: #1E1B2E;
            color: #F8FAFC;
            border: 1px solid #2D274A;
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
            box-shadow: 0 0 0 2px rgba(78, 39, 153, 0.25);
        }}

        /* TERMINAL CONSOLE OUTPUT BOX */
        .terminal-box {{
            background: #0F0D1B;
            border: 1px solid #262142;
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
            border-bottom: 1px solid #262142;
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
            background: var(--green-light);
            border: 1px solid var(--green);
            color: #065F46;
        }}

        .feedback-banner.error {{
            background: var(--red-light);
            border: 1px solid var(--red);
            color: #991B1B;
        }}

        /* FOOTER ACTIONS BAR */
        .task-actions-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: auto;
            padding-top: 16px;
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
            background: var(--bg-page);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 8px 14px;
            font-family: inherit;
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--text-primary);
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .btn-nav:hover:not(:disabled) {{
            border-color: var(--purple-primary);
            color: var(--purple-primary);
        }}

        .btn-nav:disabled {{
            opacity: 0.4;
            cursor: not-allowed;
        }}

        .submit-btns-group {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .btn-skip {{
            background: var(--yellow-light);
            border: 1px solid var(--yellow);
            color: #B45309;
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
            color: #FFFFFF;
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
            box-shadow: 0 4px 14px rgba(78, 39, 153, 0.25);
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

        /* MODALS (Student Name / Instructor Auth / Teacher Dashboard) */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(26, 18, 53, 0.55);
            backdrop-filter: blur(5px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            padding: 20px;
        }}

        .modal-overlay.open {{
            display: flex;
        }}

        .modal-card {{
            background: #FFFFFF;
            border-radius: var(--radius-xl);
            width: 100%;
            max-width: 820px;
            max-height: 90vh;
            overflow-y: auto;
            padding: 24px 28px;
            box-shadow: var(--shadow-lg);
            display: flex;
            flex-direction: column;
            gap: 16px;
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
            background: var(--bg-page);
            border: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 1.1rem;
            font-weight: 800;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        /* TEACHER DASHBOARD TABLE */
        .teacher-stats-strip {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 10px;
        }}

        .t-stat-pill {{
            background: var(--bg-page);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 10px 14px;
        }}

        .t-stat-label {{
            font-size: 0.75rem;
            color: var(--text-muted);
            font-weight: 700;
        }}

        .t-stat-val {{
            font-size: 1.2rem;
            font-weight: 900;
            color: var(--purple-primary);
        }}

        .students-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
        }}

        .students-table th, .students-table td {{
            padding: 10px 12px;
            text-align: right;
            border-bottom: 1px solid var(--border-color);
        }}

        .students-table th {{
            background: var(--bg-page);
            color: var(--text-secondary);
            font-weight: 800;
        }}

        .btn-inspect-student {{
            background: var(--purple-light);
            border: 1px solid var(--purple-primary);
            color: var(--purple-primary);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 800;
            cursor: pointer;
        }}

        /* TEACHER MANAGEMENT ACTIONS */
        .teacher-file-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            background: var(--bg-page);
            padding: 14px;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            align-items: center;
        }}

        .btn-secondary-action {{
            background: #FFFFFF;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 7px 12px;
            font-family: inherit;
            font-size: 0.82rem;
            font-weight: 800;
            color: var(--purple-primary);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
        }}

        .btn-secondary-action:hover {{
            border-color: var(--purple-primary);
            background: var(--purple-light);
        }}

        /* TOAST ALERT */
        .toast {{
            position: fixed;
            bottom: 20px;
            left: 20px;
            background: var(--text-primary);
            color: #FFFFFF;
            padding: 10px 18px;
            border-radius: 30px;
            font-size: 0.85rem;
            font-weight: 700;
            box-shadow: 0 6px 20px rgba(0,0,0,0.25);
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
    </style>
</head>
<body>

<div class="container">
    <!-- APP TOP HEADER -->
    <header class="app-header">
        <div class="brand-section">
            <div class="brand-logo">
                <img src="{logo_base64}" alt="Genie Tech Academy">
            </div>
            <div class="brand-titles">
                <h1 id="weekDisplayTitle">
                    تاسكات الأسبوع 01 🐍
                </h1>
                <p id="weekDisplayTopic">المتغيرات، الطباعة print، المدخلات input، والعمليات الحسابية</p>
            </div>
        </div>

        <div style="display: flex; align-items: center; gap: 10px;">
            <div class="student-pill" onclick="promptStudentName()">
                <div class="student-avatar" id="avatarLetter">ع</div>
                <span class="student-name-text" id="headerStudentName">علي (اضغط لتغيير الاسم)</span>
            </div>
            <button class="btn-teacher-toggle" onclick="requestTeacherAccess()">
                <span>👨‍🏫</span>
                <span>لوحة المدرس</span>
            </button>
        </div>
    </header>

    <!-- QUESTION NAVIGATOR STRIP & PROGRESS -->
    <div class="navigator-card">
        <div class="navigator-top">
            <span id="progressSummaryText">تم حل 0 من 14 سؤال • 0 متخطي</span>
            <span id="percentText">0%</span>
        </div>
        <div class="progress-bar-bg">
            <div class="progress-bar-fill" id="progressBarFill"></div>
        </div>
        <div class="nav-chips-strip" id="navChipsStrip">
            <!-- Chips rendered dynamically -->
        </div>
    </div>

    <!-- MAIN ACTIVE TASK CANVAS (1 QUESTION FOCUS) -->
    <main class="task-card" id="taskCardMain">
        <!-- TASK HEADER -->
        <div class="task-header-row">
            <div class="task-badge-group">
                <span class="badge-stage" id="stageBadge">المرحلة الأولى: اختيار من متعدد</span>
                <span class="badge-status status-unsolved" id="taskStatusBadge">لم يتم التسليم بعد</span>
            </div>
            <span style="font-size: 0.82rem; font-weight: 700; color: var(--text-muted);" id="questionCounter">سؤال 1 من 14</span>
        </div>

        <!-- TASK TITLE & INSTRUCTIONS -->
        <h2 class="task-title" id="taskTitleText">الخزان يعني Variable في البرمجة، بنستخدمه عشان إيه؟</h2>

        <!-- HINT BOX (SHORT & KID FRIENDLY) -->
        <div class="task-hint-box" id="taskHintBox">
            <span>💡</span>
            <span id="taskHintText">فكر: زي العلبة أو الدرج اللي بنحط جواه لعبتنا ونقدر نغيرها.</span>
        </div>

        <!-- OPTIONAL CODE SNIPPET (IF ANY) -->
        <div class="code-box" id="taskCodeSnippetBox" style="display: none;">
            <pre><code id="taskCodeSnippetText">cup = "tea"</code></pre>
        </div>

        <!-- DYNAMIC TASK BODY CONTAINER -->
        <div id="dynamicTaskBody">
            <!-- Renders MCQ options OR Fix-Code Editor OR Guided Project OR Solo Challenge -->
        </div>

        <!-- TERMINAL CONSOLE (FOR RUNNING PYTHON TASKS) -->
        <div class="terminal-box" id="terminalBox" style="display: none;">
            <div class="terminal-header">
                <span>🖥️ شاشة تشغيل البرنامج (Python Console Output)</span>
                <span id="termStatus">جاهز للتشغيل</span>
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
                    <span>تخطي السؤال مؤقتاً</span>
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

<!-- INSTRUCTOR PASSWORD MODAL -->
<div class="modal-overlay" id="instructorAuthModal">
    <div class="modal-card" style="max-width: 440px; text-align: center;">
        <div style="font-size: 2.2rem; margin-bottom: 4px;">🔐</div>
        <h3 style="font-size: 1.25rem; color: var(--purple-primary); font-weight: 900;">دخول لوحة المدرس</h3>
        <p style="font-size: 0.88rem; color: var(--text-secondary); font-weight: 700;">من فضلك أدخل كلمة مرور المدرس للمتابعة وإدارة الواجبات:</p>
        <div style="position: relative; margin: 12px 0;">
            <input type="password" id="instructorPasscodeInput" placeholder="اكتب كلمة المرور هنا" 
                   style="width: 100%; padding: 12px 16px; border: 2px solid var(--purple-primary); border-radius: 12px; font-family: 'JetBrains Mono', inherit; font-size: 1.1rem; font-weight: 800; text-align: center; outline: none;"
                   onkeydown="if(event.key==='Enter') verifyInstructorPassword()">
        </div>
        <div id="authErrorMsg" style="display: none; color: var(--red); font-weight: 800; font-size: 0.85rem; margin-bottom: 8px;">
            ❌ كلمة المرور غير صحيحة! تأكد من الكود وحاول مرة أخرى.
        </div>
        <div style="display: flex; gap: 8px;">
            <button class="btn-submit-task" style="flex: 1; justify-content: center;" onclick="verifyInstructorPassword()">
                <span>دخول اللوحة 🚀</span>
            </button>
            <button class="btn-nav" onclick="closeAuthModal()">
                <span>إلغاء</span>
            </button>
        </div>
    </div>
</div>

<!-- STUDENT NAME PROMPT MODAL -->
<div class="modal-overlay" id="nameModal">
    <div class="modal-card" style="max-width: 440px; text-align: center;">
        <div style="font-size: 2.5rem; margin-bottom: 6px;">🧞‍♂️</div>
        <h3 style="font-size: 1.3rem; color: var(--purple-primary); font-weight: 900;">أهلاً بك يا بطل المستقبل!</h3>
        <p style="font-size: 0.9rem; color: var(--text-secondary); font-weight: 700;">اكتب اسمك عشان مستر مصطفى يتابع حلك للواجب أسبوع بأسبوع:</p>
        <input type="text" id="studentNameInput" placeholder="اكتب اسمك هنا (مثلاً: علي أحمد)" 
               style="width: 100%; padding: 12px 16px; border: 2px solid var(--purple-primary); border-radius: 12px; font-family: inherit; font-size: 1rem; font-weight: 800; text-align: center; outline: none; margin: 10px 0;">
        <button class="btn-submit-task" style="width: 100%; justify-content: center;" onclick="saveStudentName()">
            <span>يلا نبدأ حل الواجب 🚀</span>
        </button>
    </div>
</div>

<!-- TEACHER DASHBOARD MODAL -->
<div class="modal-overlay" id="teacherModal">
    <div class="modal-card">
        <div class="modal-header">
            <div style="display: flex; align-items: center; gap: 10px;">
                <h3>👨‍🏫 لوحة متابعة المدرس (Teacher Review Dashboard)</h3>
                <span style="background: var(--green-light); color: var(--green); font-size: 0.72rem; font-weight: 800; padding: 2px 8px; border-radius: 10px;">
                    مُسجل دخول ✓
                </span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <button class="btn-secondary-action" style="color: var(--red); border-color: var(--red-light);" onclick="lockInstructorMode()">
                    <span>قفل اللوحة 🔒</span>
                </button>
                <button class="modal-close-btn" onclick="closeTeacherDashboard()">✕</button>
            </div>
        </div>

        <div class="teacher-stats-strip">
            <div class="t-stat-pill">
                <div class="t-stat-label">إجمالي الطلاب المسجلين</div>
                <div class="t-stat-val" id="tStatStudents">1</div>
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

        <!-- WEEK REPLACEMENT & TEMPLATE DOWNLOAD (FOR EVERY WEEK) -->
        <div class="teacher-file-actions">
            <div style="font-size: 0.85rem; font-weight: 800; color: var(--purple-primary); margin-left: 10px;">
                ⚙️ إدارة واجبات الأسابيع:
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
            <button class="btn-secondary-action" onclick="switchDemoWeek()">
                <span>🔄 التبديل بين الأسبوع 1 و 2</span>
            </button>
            <button class="btn-secondary-action" onclick="exportSubmissionsCSV()">
                <span>📊 تصدير درجات الطلاب (CSV)</span>
            </button>
        </div>

        <!-- REGISTERED STUDENTS TABLE -->
        <h4 style="font-size: 1rem; color: var(--purple-primary); font-weight: 800; margin-top: 6px;">
            📋 سجل حلول الطلاب ومتابعة تقدمهم سؤال بسؤال:
        </h4>
        <div style="overflow-x: auto;">
            <table class="students-table">
                <thead>
                    <tr>
                        <th>اسم الطالب</th>
                        <th>الأسئلة المحلولة</th>
                        <th>المتخطي</th>
                        <th>نسبة الإنجاز</th>
                        <th>آخر نشاط</th>
                        <th>معاينة الحل الكامل</th>
                    </tr>
                </thead>
                <tbody id="teacherStudentsTbody">
                    <!-- Loaded dynamically -->
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- STUDENT SUBMISSION INSPECTOR MODAL -->
<div class="modal-overlay" id="studentDetailModal">
    <div class="modal-card">
        <div class="modal-header">
            <h3 id="detailStudentTitle">تفاصيل حل الطالب: علي</h3>
            <button class="modal-close-btn" onclick="document.getElementById('studentDetailModal').classList.remove('open')">✕</button>
        </div>
        <div id="studentDetailContent" style="display: flex; flex-direction: column; gap: 12px;">
            <!-- Detailed inspection of all student questions and code -->
        </div>
    </div>
</div>

<!-- TOAST -->
<div class="toast" id="toastMsg">تم تسليم السؤال بنجاح ✓</div>

<script>
    // INSTRUCTOR PASSCODE
    const INSTRUCTOR_PASSCODE = "100020003000";

    // EMBEDDED DEFAULT DATA & REFERENCE
    const DEFAULT_TASKS = {tasks_week_01_json};
    const REFERENCE_TASKS = {tasks_reference_json};

    let activeTasksData = DEFAULT_TASKS;
    let allQuestionsList = [];
    let currentQuestionIndex = 0;
    let currentStudentName = localStorage.getItem('genie_active_student') || 'علي';
    let currentSubmissions = {{}}; // questionId -> {{ status: 'solved'|'skipped', answer: any, code: string, timestamp: '' }}
    let selectedOptionIndex = null;

    // INITIALIZATION
    function initApp() {{
        loadStudentData();
        buildQuestionList();
        renderNavChips();
        renderCurrentQuestion();
        updateHeaderInfo();

        if (!localStorage.getItem('genie_active_student')) {{
            openNameModal();
        }}
    }}

    function buildQuestionList() {{
        allQuestionsList = [];

        // 1. MCQ
        if (activeTasksData.mcq_questions) {{
            activeTasksData.mcq_questions.forEach((q, idx) => {{
                allQuestionsList.push({{
                    type: 'mcq',
                    stageName: 'المرحلة 1: مراجعة واختيار من متعدد',
                    data: q,
                    index: allQuestionsList.length
                }});
            }});
        }}

        // 2. Fix Code
        if (activeTasksData.fix_code_tasks) {{
            activeTasksData.fix_code_tasks.forEach((q, idx) => {{
                allQuestionsList.push({{
                    type: 'fix_code',
                    stageName: 'المرحلة 2: صلح الكود وعدله',
                    data: q,
                    index: allQuestionsList.length
                }});
            }});
        }}

        // 3. Guided Project
        if (activeTasksData.guided_project) {{
            allQuestionsList.push({{
                type: 'guided_project',
                stageName: 'المرحلة 3: مشروع موجه بالكومنتات',
                data: activeTasksData.guided_project,
                index: allQuestionsList.length
            }});
        }}

        // 4. Solo Challenge
        if (activeTasksData.solo_challenge) {{
            allQuestionsList.push({{
                type: 'solo_challenge',
                stageName: 'المرحلة 4: تحدي كتابة الكود كامل لوحدك',
                data: activeTasksData.solo_challenge,
                index: allQuestionsList.length
            }});
        }}
    }}

    function updateHeaderInfo() {{
        document.getElementById('weekDisplayTitle').innerText = activeTasksData.week_title || 'الواجب الأسبوعي 🐍';
        document.getElementById('weekDisplayTopic').innerText = activeTasksData.topic_ar || '';
        document.getElementById('headerStudentName').innerText = `${{currentStudentName}} (اضغط لتغيير الاسم)`;
        document.getElementById('avatarLetter').innerText = currentStudentName.charAt(0) || 'ط';
    }}

    // RENDER NAVIGATOR CHIPS
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
                chip.innerText = `صلح ${{idx - (activeTasksData.mcq_questions ? activeTasksData.mcq_questions.length : 0) + 1}}`;
            }} else if (q.type === 'guided_project') {{
                chip.classList.add('special');
                chip.innerText = 'المشروع 🍕';
            }} else if (q.type === 'solo_challenge') {{
                chip.classList.add('special');
                chip.innerText = 'التحدي 🚀';
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
    }}

    // RENDER CURRENT QUESTION CANVAS
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

        document.getElementById('taskTitleText').innerText = data.title ? `${{data.title}}: ${{data.question || data.instructions}}` : (data.question || data.instructions);
        document.getElementById('taskHintText').innerText = data.hint || 'اقرأ المطلوب بهدوء وفكر خطوة بخطوة يا بطل.';

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

    // 1. RENDER MCQ
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

    // 2. RENDER FIX CODE
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
                const savedVal = (sub && sub.code) ? sub.code : (lineItem.placeholder || lineItem.code);
                row.innerHTML = `
                    <span class="line-num">${{lineItem.line}}</span>
                    <input type="text" class="line-input-editable" id="editableLineInput" value="${{escapeHtml(savedVal)}}" spellcheck="false">
                `;
            }}
            wrap.appendChild(row);
        }});

        container.appendChild(wrap);
    }}

    // 3. RENDER GUIDED & SOLO CODING
    function renderCodingBody(container, data, sub) {{
        document.getElementById('terminalBox').style.display = 'flex';

        const savedCode = (sub && sub.code) ? sub.code : (data.initial_code || '');
        const textarea = document.createElement('textarea');
        textarea.className = 'code-textarea';
        textarea.id = 'fullCodeTextarea';
        textarea.value = savedCode;
        textarea.spellcheck = false;

        container.appendChild(textarea);
    }}

    // SUBMIT QUESTION BY QUESTION
    function submitCurrentTask() {{
        const qObj = allQuestionsList[currentQuestionIndex];
        const data = qObj.data;
        const qId = data.id;

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

            saveSubmission(qId, {{
                status: 'solved',
                answer: selectedOptionIndex,
                is_correct: isCorrect,
                timestamp: new Date().toLocaleString('ar-EG')
            }});

        }} else if (qObj.type === 'fix_code') {{
            const inputElem = document.getElementById('editableLineInput');
            const codeVal = inputElem ? inputElem.value : '';

            const result = runCurrentCode();
            const isMatch = result.output.trim() === (data.expected_output || '').trim();

            if (isMatch) {{
                showFeedback(true, `عاش يا باشمهندس! الكود صلح المشكلة وطلع النتيجة المطلوبة (${{data.expected_output}}). 🎉`);
                triggerConfetti();
            }} else {{
                showFeedback(false, `الناتج الفعلي: "${{result.output.trim()}}"، والمطلوب: "${{data.expected_output}}". جرب تعدل السطر تاني.`);
            }}

            saveSubmission(qId, {{
                status: 'solved',
                code: codeVal,
                output: result.output,
                is_correct: isMatch,
                timestamp: new Date().toLocaleString('ar-EG')
            }});

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
                showFeedback(false, `شاشة الرن طلعت: "${{result.output.trim()}}". اتأكد من أرقامك والعمليات الحسابية.`);
            }}

            saveSubmission(qId, {{
                status: 'solved',
                code: codeVal,
                output: result.output,
                is_correct: isMatch,
                timestamp: new Date().toLocaleString('ar-EG')
            }});
        }}

        renderNavChips();
        renderCurrentQuestion();
        showToast('تم تسليم السؤال وحفظه في سجل الطالب ✓');
    }}

    // SKIP TASK
    function skipCurrentTask() {{
        const qObj = allQuestionsList[currentQuestionIndex];
        const qId = qObj.data.id;

        saveSubmission(qId, {{
            status: 'skipped',
            timestamp: new Date().toLocaleString('ar-EG')
        }});

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

    // RUN CODE (IN-BROWSER PYTHON RUNNER FOR KIDS)
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
                    scope[varName] = evaluateExpr(expr, scope);
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

    function loadStudentData() {{
        const allData = JSON.parse(localStorage.getItem('genie_academy_tasks_db') || '{{}}');
        if (!allData[currentStudentName]) {{
            allData[currentStudentName] = {{
                week_id: activeTasksData.week_id,
                submissions: {{}}
            }};
        }}
        currentSubmissions = allData[currentStudentName].submissions || {{}};
    }}

    function saveSubmission(qId, subObj) {{
        const allData = JSON.parse(localStorage.getItem('genie_academy_tasks_db') || '{{}}');
        if (!allData[currentStudentName]) {{
            allData[currentStudentName] = {{
                student_name: currentStudentName,
                week_id: activeTasksData.week_id,
                submissions: {{}}
            }};
        }}
        allData[currentStudentName].submissions[qId] = subObj;
        allData[currentStudentName].last_active = new Date().toLocaleString('ar-EG');
        localStorage.setItem('genie_academy_tasks_db', JSON.stringify(allData));
        currentSubmissions = allData[currentStudentName].submissions;
    }}

    function promptStudentName() {{
        openNameModal();
    }}

    function openNameModal() {{
        document.getElementById('studentNameInput').value = currentStudentName;
        document.getElementById('nameModal').classList.add('open');
    }}

    function saveStudentName() {{
        const val = document.getElementById('studentNameInput').value.trim();
        if (val) {{
            currentStudentName = val;
            localStorage.setItem('genie_active_student', val);
            loadStudentData();
            updateHeaderInfo();
            renderNavChips();
            renderCurrentQuestion();
            document.getElementById('nameModal').classList.remove('open');
            showToast(`أهلاً بك يا ${{currentStudentName}}! بالتوفيق في الواجب 🌟`);
        }}
    }}

    // INSTRUCTOR MODE PASSWORD VERIFICATION
    function requestTeacherAccess() {{
        if (sessionStorage.getItem('genie_instructor_authed') === 'true') {{
            openTeacherDashboard();
        }} else {{
            document.getElementById('instructorPasscodeInput').value = '';
            document.getElementById('authErrorMsg').style.display = 'none';
            document.getElementById('instructorAuthModal').classList.add('open');
            setTimeout(() => document.getElementById('instructorPasscodeInput').focus(), 150);
        }}
    }}

    function verifyInstructorPassword() {{
        const inputVal = document.getElementById('instructorPasscodeInput').value.trim();
        if (inputVal === INSTRUCTOR_PASSCODE) {{
            sessionStorage.setItem('genie_instructor_authed', 'true');
            document.getElementById('instructorAuthModal').classList.remove('open');
            openTeacherDashboard();
            showToast('تم التحقق بنجاح! مرحباً بك في لوحة المدرس 👨‍🏫');
        }} else {{
            document.getElementById('authErrorMsg').style.display = 'block';
            document.getElementById('instructorPasscodeInput').select();
        }}
    }}

    function closeAuthModal() {{
        document.getElementById('instructorAuthModal').classList.remove('open');
    }}

    function lockInstructorMode() {{
        sessionStorage.removeItem('genie_instructor_authed');
        closeTeacherDashboard();
        showToast('تم قفل لوحة المدرس بنجاح 🔒');
    }}

    // TEACHER DASHBOARD
    function openTeacherDashboard() {{
        const db = JSON.parse(localStorage.getItem('genie_academy_tasks_db') || '{{}}');
        const students = Object.keys(db);

        document.getElementById('tStatStudents').innerText = Math.max(students.length, 1);
        document.getElementById('tStatWeek').innerText = activeTasksData.week_id || 'Week 01';
        document.getElementById('tStatQuestions').innerText = allQuestionsList.length;

        const tbody = document.getElementById('teacherStudentsTbody');
        tbody.innerHTML = '';

        let totalSolvedAll = 0;

        if (students.length === 0) {{
            tbody.innerHTML = `<tr><td colspan="6" style="text-align: center; color: var(--text-muted);">لا توجد تسليمات مسجلة بعد.</td></tr>`;
        }} else {{
            students.forEach(stName => {{
                const stData = db[stName];
                const subs = stData.submissions || {{}};
                let solved = 0;
                let skipped = 0;

                Object.values(subs).forEach(s => {{
                    if (s.status === 'solved') solved++;
                    if (s.status === 'skipped') skipped++;
                }});

                totalSolvedAll += solved;
                const totalQ = allQuestionsList.length;
                const pct = totalQ > 0 ? Math.round((solved / totalQ) * 100) : 0;

                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><strong>${{stName}}</strong></td>
                    <td><span style="color: var(--green); font-weight: 800;">${{solved}} / ${{totalQ}}</span></td>
                    <td><span style="color: #B45309; font-weight: 800;">${{skipped}}</span></td>
                    <td><strong>${{pct}}%</strong></td>
                    <td style="font-size: 0.78rem; color: var(--text-secondary);">${{stData.last_active || 'اليوم'}}</td>
                    <td>
                        <button class="btn-inspect-student" onclick="inspectStudent('${{stName}}')">
                            معاينة الحل 👁️
                        </button>
                    </td>
                `;
                tbody.appendChild(tr);
            }});
        }}

        const avg = students.length > 0 ? Math.round((totalSolvedAll / (students.length * allQuestionsList.length)) * 100) : 0;
        document.getElementById('tStatAvg').innerText = `${{avg}}%`;

        document.getElementById('teacherModal').classList.add('open');
    }}

    function closeTeacherDashboard() {{
        document.getElementById('teacherModal').classList.remove('open');
    }}

    function inspectStudent(stName) {{
        const db = JSON.parse(localStorage.getItem('genie_academy_tasks_db') || '{{}}');
        const stData = db[stName];
        if (!stData) return;

        document.getElementById('detailStudentTitle').innerText = `تفاصيل إجابات الطالب: ${{stName}} (${{activeTasksData.week_title}})`;
        const wrap = document.getElementById('studentDetailContent');
        wrap.innerHTML = '';

        allQuestionsList.forEach((q, idx) => {{
            const qId = q.data.id;
            const sub = stData.submissions ? stData.submissions[qId] : null;

            const card = document.createElement('div');
            card.style.background = 'var(--bg-page)';
            card.style.border = '1px solid var(--border-color)';
            card.style.borderRadius = '10px';
            card.style.padding = '10px 14px';

            let statusHtml = '<span style="color: var(--text-muted); font-weight: 800;">لم يُحل</span>';
            if (sub && sub.status === 'solved') {{
                statusHtml = `<span style="color: var(--green); font-weight: 800;">تم التسليم (${{sub.is_correct ? 'صح ✓' : 'بحاجة لمراجعة ❌'}})</span>`;
            }} else if (sub && sub.status === 'skipped') {{
                statusHtml = '<span style="color: #B45309; font-weight: 800;">تم التخطي ⏭️</span>';
            }}

            let detailAnswer = '';
            if (q.type === 'mcq') {{
                if (sub && sub.answer !== undefined) {{
                    detailAnswer = `<p style="font-size: 0.85rem; margin-top: 4px;">اختيار الطالب: <strong>${{q.data.options[sub.answer] || 'غير محدد'}}</strong></p>`;
                }}
            }} else {{
                if (sub && sub.code) {{
                    detailAnswer = `
                        <div style="background: #1E1B2E; color: #fff; padding: 6px 10px; border-radius: 6px; font-family: monospace; font-size: 0.8rem; direction: ltr; margin-top: 6px;">
                            ${{escapeHtml(sub.code)}}
                        </div>
                    `;
                }}
            }}

            card.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 800; color: var(--purple-primary); font-size: 0.9rem;">${{idx + 1}}. ${{q.data.title || q.data.question || ''}}</span>
                    ${{statusHtml}}
                </div>
                ${{detailAnswer}}
            `;
            wrap.appendChild(card);
        }});

        document.getElementById('studentDetailModal').classList.add('open');
    }}

    function handleTeacherUpload(event) {{
        const file = event.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = function(e) {{
            try {{
                const newTasks = JSON.parse(e.target.result);
                activeTasksData = newTasks;
                currentQuestionIndex = 0;
                buildQuestionList();
                renderNavChips();
                renderCurrentQuestion();
                updateHeaderInfo();
                closeTeacherDashboard();
                showToast(`تم تحميل الواجب الجديد بنجاح: ${{newTasks.week_title || ''}} 🎉`);
            }} catch (err) {{
                alert('خطأ في قراءة ملف الـ JSON: ' + err.message);
            }}
        }};
        reader.readAsText(file);
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
        const db = JSON.parse(localStorage.getItem('genie_academy_tasks_db') || '{{}}');
        let csv = "\\uFEFFاسم الطالب,السؤال,الحالة,الإجابة/الكود,التوقيت\\n";

        for (const [stName, stData] of Object.entries(db)) {{
            const subs = stData.submissions || {{}};
            allQuestionsList.forEach(q => {{
                const qId = q.data.id;
                const s = subs[qId];
                const status = s ? s.status : 'unsolved';
                const ans = s ? (s.answer !== undefined ? s.answer : (s.code ? s.code.replace(/\\n/g, ' ') : '')) : '';
                const time = s ? (s.timestamp || '') : '';
                csv += `"${{stName}}","${{q.data.title || q.data.question || qId}}","${{status}}","${{ans}}","${{time}}"\\n`;
            }});
        }}

        const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Genie_Tech_Tasks_Submissions_${{activeTasksData.week_id}}.csv`;
        a.click();
        showToast('تم تصدير ملف النتائج CSV بنجاح');
    }}

    let demoWeekCounter = 1;
    function switchDemoWeek() {{
        demoWeekCounter = (demoWeekCounter === 1) ? 2 : 1;
        if (demoWeekCounter === 2) {{
            activeTasksData = {{
                "week_id": "week_02",
                "week_title": "الواجب الأسبوعي 02: الشروط وقرارات if / else 🚦",
                "topic_ar": "مراجعة الشروط المنطقية وعلامات المقارنة (==, >, <)",
                "mcq_questions": [
                    {{
                        "id": "w2_mcq_1",
                        "title": "معنى if في البرمجة",
                        "question": "كلمة if في بايثون معناها إيه؟",
                        "hint": "لو كذا حصل اعمل كذا.",
                        "code_snippet": "if score >= 50:\\n    print(\\"Pass\\")",
                        "options": ["لو أو إذا كان الشرط صح", "اطفي الجهاز", "كرر 10 مرات"],
                        "correct_index": 0,
                        "explanation": "صح يا بطل! if معناها إذا كان الشرط صح."
                    }}
                ],
                "fix_code_tasks": [
                    {{
                        "id": "w2_fix_1",
                        "title": "صلح شرط إشارة المرور 🚦",
                        "instructions": "لو الإشارة green المفروض يطبع Go! صلح السطر 2.",
                        "template_lines": [
                            {{"line": 1, "code": "light = \\"green\\"", "locked": true}},
                            {{"line": 2, "code": "if light != \\"green\\":", "locked": false, "placeholder": "if light == \\"green\\":"}},
                            {{"line": 3, "code": "    print(\\"Go!\\")", "locked": true}}
                        ],
                        "expected_output": "Go!",
                        "hint": "استخدم == للمقارنة."
                    }}
                ],
                "guided_project": {{
                    "id": "w2_proj_1",
                    "title": "مشروع اختبار درجات الطالب 🎓",
                    "instructions": "اكتب شرط النجاح في السطر 2.",
                    "initial_code": "# 1. درجة الطالب\\ndegree = 85\\n\\n# 2. لو الدرجة >= 50 اطبع Success\\nif degree >= 50:\\n    print(\\"Success\\")",
                    "expected_output": "Success"
                }},
                "solo_challenge": {{
                    "id": "w2_solo_1",
                    "title": "تحدي فحص كلمة السر 🔐",
                    "instructions": "عرف كلمة سر وافحص لو بتساوي 1234 اطبع Welcome!",
                    "initial_code": "password = \\"1234\\"\\nif password == \\"1234\\":\\n    print(\\"Welcome!\\")",
                    "expected_output_contains": ["Welcome!"]
                }}
            }};
        }} else {{
            activeTasksData = DEFAULT_TASKS;
        }}

        currentQuestionIndex = 0;
        buildQuestionList();
        renderNavChips();
        renderCurrentQuestion();
        updateHeaderInfo();
        closeTeacherDashboard();
        showToast(`تم التبديل إلى ${{activeTasksData.week_title}}`);
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
                origin: {{ y: 0.7 }}
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

print(f"Generated index.html: {index_path} ({os.path.getsize(index_path)} bytes)")
print(f"Generated artifact: {artifact_html_path} ({os.path.getsize(artifact_html_path)} bytes)")
