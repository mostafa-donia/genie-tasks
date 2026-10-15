import json
import os

target_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\genie-tasks-platform"
artifact_dir = r"C:\Users\Admin\.gemini\antigravity\brain\254f8f1d-ee3b-47dd-abe1-87a1bb03754d"

logo_path = os.path.join(target_dir, "new_logo_base64.txt")
with open(logo_path, "r", encoding="utf-8") as f:
    logo_base64 = f.read().strip()

# Clean tasks.json to NOT have spoiler titles
tasks_week_01 = {
    "week_id": "week_01",
    "week_number": 1,
    "week_title": "الواجب الأسبوعي 01 🐍",
    "topic_ar": "تحديات بايثون الأسبوعية للأبطال",
    "topic_en": "Python Weekly Tasks for Kids",
    "target_age": "8-12 سنة",
    "mcq_questions": [
        {
            "id": "mcq_1",
            "number": 1,
            "title": "سؤال 1",
            "question": "الخزان (Variable) بنستخدمه في البرمجة عشان إيه؟",
            "hint": "زي العلبة أو الدرج اللي بنحط جواه لعبتنا ونقدر نغيرها.",
            "code_snippet": "cup = \"tea\"",
            "options": [
                "مكان بنخزن جواه قيمة ونقدر نغير اللي جواه في أي وقت",
                "زرار بنقفله عشان نطفي الكمبيوتر خالص",
                "شاشة العرض بتاعة اللاب توب"
            ],
            "correct_index": 0,
            "explanation": "صح يا بطل! المتغير هو مكان بنخزن فيه حاجة زي اسم أو رقم، ونقدر نغير قيمته في أي وقت."
        },
        {
            "id": "mcq_2",
            "number": 2,
            "title": "سؤال 2",
            "question": "في بايثون، أي كلام بيتكتب بين إيه؟",
            "hint": "زي كلمة \"Ali\" أو \"Hello\".",
            "code_snippet": "name = \"Ali\"",
            "options": [
                "بين علامتي تنصيص \" \"",
                "بين أقواس مربعة [ ]",
                "بدون أي علامات خالص"
            ],
            "correct_index": 0,
            "explanation": "شاطر جداً! النصوص والكلام في بايثون لازم نكتبها بين علامتي تنصيص \" \"."
        },
        {
            "id": "mcq_3",
            "number": 3,
            "title": "سؤال 3",
            "question": "لو عايز أسجل عمر الطالب 8 سنوات، نوع الرقم ده إيه؟",
            "hint": "رقم سليم مفيش فيه نقطة أو فواصل.",
            "code_snippet": "age = 8",
            "options": [
                "int (رقم صحيح)",
                "String (كلام)",
                "float (رقم عشري)"
            ],
            "correct_index": 0,
            "explanation": "ممتاز! 8 هو رقم صحيح بدون فواصل عشرية، فاسمه int."
        },
        {
            "id": "mcq_4",
            "number": 4,
            "title": "سؤال 4",
            "question": "طول الطالب 1.35 متر، نوع الرقم ده إيه في بايثون؟",
            "hint": "فيه نقطة عشرية (Point).",
            "code_snippet": "height = 1.35",
            "options": [
                "float (رقم عشري فيه بوينت)",
                "int (رقم صحيح)",
                "input (إدخال)"
            ],
            "correct_index": 0,
            "explanation": "برافو! أي رقم فيه نقطة عشرية زي 1.35 أو 2.5 بيسمى float."
        },
        {
            "id": "mcq_5",
            "number": 5,
            "title": "سؤال 5",
            "question": "بص للكود ده كويس، السطر التاني هيطبع إيه على الشاشة؟",
            "hint": "ركز: هل كلمة name بين علامتي تنصيص؟ لأ، دي اسم الخزان!",
            "code_snippet": "name = \"Ali\"\nprint(name)",
            "options": [
                "هيطبع: Ali (القيمة اللي جوه الخزان)",
                "هيطبع كلمة: name بالحروف",
                "مش هيطبع أي حاجة وهيطلع غلط"
            ],
            "correct_index": 0,
            "explanation": "تركيزك عالي! بما إن مفيش علامات تنصيص، بايثون هيروح يفتح الخزان name ويطبع اللي جواه وهو Ali."
        },
        {
            "id": "mcq_6",
            "number": 6,
            "title": "سؤال 6",
            "question": "في السطر ده: print(f\"Hello {name}\") الأقواس {} وظيفتها إيه؟",
            "hint": "بتحجز مكان لحاجة جوة الرسالة.",
            "code_snippet": "name = \"Ali\"\nprint(f\"Hello {name}\")",
            "options": [
                "مكان بنحط جواه اسم الخزان عشان يطبع قيمته",
                "شكل جمالي بس وموش فايدة",
                "عشان نقفل البرنامج بعد ما يخلص"
            ],
            "correct_index": 0,
            "explanation": "صح يا نجم! القوسين {} في f-string هما المكان المخصص اللي بايثون بيحط فيه قيمة الخزان."
        },
        {
            "id": "mcq_7",
            "number": 7,
            "title": "سؤال 7",
            "question": "لو عايز أطلب من المستخدم يكتب اسمه من الكيبورد، هستخدم دالة إيه؟",
            "hint": "كلمة إنجليزية معناها (إدخال).",
            "code_snippet": "name = input(\"Enter your name: \")",
            "options": [
                "input()",
                "print()",
                "int()"
            ],
            "correct_index": 0,
            "explanation": "تمام يا بطل! دالة input() بتوقف البرنامج وتستنى المستخدم يكتب من الكيبورد."
        },
        {
            "id": "mcq_8",
            "number": 8,
            "title": "سؤال 8",
            "question": "ليه كتبنا int() برة input() في السطر ده؟",
            "hint": "input() لوحدها بتدخل كلام، واحنا عايزين نعمل حسابات برقم صحيح!",
            "code_snippet": "age = int(input(\"Enter your age: \"))",
            "options": [
                "عشان نحول اللي المستخدم هيكتبه من كلام إلى رقم صحيح نقدر نحسب بيه",
                "عشان نطبع الاسم على الشاشة بسرعة",
                "عشان نحذف الإجابة القديمة"
            ],
            "correct_index": 0,
            "explanation": "أحسنت! لو مستخدم كتب 8 في input عادية بتدخل كـ \"8\" كلام، فـ int() بتحولها لرقم حقيقي 8."
        },
        {
            "id": "mcq_9",
            "number": 9,
            "title": "سؤال 9",
            "question": "علامة الضرب في لغة بايثون بتتكتب إزاي؟",
            "hint": "شكلها نجمة مش حرف x.",
            "code_snippet": "total = 5 * 3",
            "options": [
                "علامة النجمة (*)",
                "حرف الإكس (x)",
                "علامة الشباك (#)"
            ],
            "correct_index": 0,
            "explanation": "شاطر جداً! في البرمجة كلها علامة الضرب هي النجمة (*) و 5 * 3 = 15."
        },
        {
            "id": "mcq_10",
            "number": 10,
            "title": "سؤال 10",
            "question": "ما نتيجة تشغيل هذا الكود؟",
            "hint": "معاك 10 وصرفت منهم 4، فاضل معاك كام؟",
            "code_snippet": "wallet = 10\nspent = 4\nresult = wallet - spent\nprint(result)",
            "options": [
                "6",
                "14",
                "40"
            ],
            "correct_index": 0,
            "explanation": "برافو عليك! 10 - 4 = 6، والكود هيطبع 6 على الشاشة."
        }
    ],
    "fix_code_tasks": [
        {
            "id": "fix_1",
            "number": 11,
            "title": "تحدي كود 1",
            "instructions": "الكود ده المفروض يجمع المصروف اللي كان معاك (20) على الفلوس اللي بابا إداهالك (10)، بس اللي كتب الكود غلط وعمل طرح بدل جمع! صلح السطر رقم 3 عشان يطبع 30.",
            "template_lines": [
                {"line": 1, "code": "wallet = 20", "locked": True},
                {"line": 2, "code": "gift = 10", "locked": True},
                {"line": 3, "code": "total = wallet - gift  # صلح هنا: عايزين نجمع بدل ما نطرح!", "locked": False, "placeholder": "total = wallet + gift"},
                {"line": 4, "code": "print(total)", "locked": True}
            ],
            "expected_output": "30",
            "hint": "غير علامة الطرح (-) لعلامة الجمع (+) في السطر التالت."
        },
        {
            "id": "fix_2",
            "number": 12,
            "title": "تحدي كود 2",
            "instructions": "الكود المفروض يطبع Hello Ali بس نسي يحط حرف f قبل علامة التنصيص أو نسي الأقواس! صلح السطر 2 عشان يطبع Hello Ali بالظبط.",
            "template_lines": [
                {"line": 1, "code": "name = \"Ali\"", "locked": True},
                {"line": 2, "code": "print(\"Hello name\")  # صلح هنا: استخدم f-string مع {name}", "locked": False, "placeholder": "print(f\"Hello {name}\")"}
            ],
            "expected_output": "Hello Ali",
            "hint": "اكتب print(f\"Hello {name}\") عشان بايثون يعوض عن {name} بـ Ali."
        }
    ],
    "guided_project": {
        "id": "guided_1",
        "number": 13,
        "title": "مشروع البيتزا 🍕",
        "instructions": "اقرأ التعليقات العربي اللي جوة الكود كويس، واكتب تحت كل خطوة السطر المطلوب لحساب إجمالي تمن 4 بيتزات وسعر الواحدة 50 جنيه.",
        "initial_code": "# 1. خزان لعدد البيتزا: اكتب 4\npizzas = 4\n\n# 2. خزان لسعر البيتزا الواحدة: اكتب 50\nprice = 50\n\n# 3. احسب الإجمالي: اضرب عدد البيتزا في السعر (استخدم علامة *)\ntotal = pizzas * price\n\n# 4. اطبع الناتج النهائي للخزان total\nprint(total)",
        "expected_output": "200",
        "hint": "الضرب بيتعمل بعلامة النجمة: pizzas * price وفي الآخر اطبع print(total)"
    },
    "solo_challenge": {
        "id": "solo_1",
        "number": 14,
        "title": "تحدي البطل الصغير 🚀",
        "instructions": "اكتب برنامج بالكامل من الصفر لوحدك!\nعندك 15 قطعة حلوى (candies = 15)، وعايز توزعهم بالتساوي على 3 أطفال (kids = 3). احسب نصيب كل طفل واطبع الناتج على الشاشة.",
        "initial_code": "# اكتب كودك كامل هنا يا بطل لوحدك!\n# عرف candies و kids واحسب النصيب واطبعه بالـ print\n",
        "expected_output_contains": ["5"],
        "hint": "استخدم القسمة: share = 15 // 3 أو candies // kids واطبع الناتج print(share)."
    }
}

# Save clean tasks.json
with open(os.path.join(target_dir, "tasks.json"), "w", encoding="utf-8") as f:
    json.dump(tasks_week_01, f, ensure_ascii=False, indent=2)

with open(os.path.join(target_dir, "tasks_reference.json"), "w", encoding="utf-8") as f:
    json.dump(tasks_week_01, f, ensure_ascii=False, indent=2)

tasks_week_01_json = json.dumps(tasks_week_01, ensure_ascii=False)
tasks_reference_json = tasks_week_01_json

# DARK MODE HTML TEMPLATE (Bottom Tracker, Mobile & Desktop Responsive, No Spoilers, Official Logo)
html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Genie Tech Tasks 🐍 | تحديات البرمجة للأبطال</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
    <!-- Confetti JS for fun rewards -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {{
            /* DARK MODE PALETTE - GENIE TECH BRANDING */
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
            padding-bottom: 110px; /* Space for bottom dock */
        }}

        /* APP HEADER */
        .app-header {{
            background: rgba(20, 15, 36, 0.85);
            backdrop-filter: blur(12px);
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

        .student-name-text {{
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--text-primary);
            max-width: 120px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .btn-teacher-toggle {{
            background: rgba(245, 166, 35, 0.12);
            border: 1px solid var(--gold-accent);
            color: var(--gold-accent);
            font-family: inherit;
            font-size: 0.8rem;
            font-weight: 800;
            padding: 6px 12px;
            border-radius: 12px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
            transition: var(--transition);
            white-space: nowrap;
        }}

        .btn-teacher-toggle:hover {{
            background: var(--gold-accent);
            color: #000;
            box-shadow: 0 0 14px var(--gold-glow);
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

        /* NO-SPOILER QUESTION TITLE */
        .task-question-title {{
            font-size: 1.25rem;
            font-weight: 900;
            color: #FFFFFF;
            line-height: 1.45;
        }}

        /* HINT BOX */
        .task-hint-box {{
            background: rgba(35, 28, 61, 0.6);
            border-right: 4px solid var(--gold-accent);
            border-radius: 8px;
            padding: 10px 14px;
            font-size: 0.88rem;
            font-weight: 600;
            color: #CBD5E1;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        /* CODE BLOCK (DARK THEME) */
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

        /* MCQ OPTIONS LIST */
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

        /* FIX CODE EDITOR */
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

        /* FULL CODE TEXTAREA (Guided & Solo) */
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

        /* FIXED BOTTOM DOCK (NAVIGATOR & PROGRESS - MOVED TO BOTTOM) */
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

        /* MODALS (DARK MODE) */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(4, 2, 8, 0.8);
            backdrop-filter: blur(8px);
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
            max-width: 780px;
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

        /* TEACHER STATS & TABLE */
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
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 800;
            cursor: pointer;
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

        /* RESPONSIVE DESIGN (MOBILE & LAPTOP) */
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
            <div class="student-pill" onclick="promptStudentName()">
                <div class="student-avatar" id="avatarLetter">ع</div>
                <span class="student-name-text" id="headerStudentName">علي</span>
            </div>
            <button class="btn-teacher-toggle" onclick="requestTeacherAccess()">
                <span>👨‍🏫</span>
                <span>المدرس</span>
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

        <!-- PURE QUESTION TEXT ONLY - NO SPOILER TITLES -->
        <h2 class="task-question-title" id="taskTitleText">في بايثون، أي كلام بيتكتب بين إيه؟</h2>

        <!-- HINT BOX -->
        <div class="task-hint-box" id="taskHintBox">
            <span>💡</span>
            <span id="taskHintText">فكر بهدوء خطوة بخطوة يا بطل.</span>
        </div>

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

<!-- FIXED BOTTOM DOCK (MOVED TO BOTTOM AS REQUESTED) -->
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

<!-- INSTRUCTOR PASSWORD MODAL -->
<div class="modal-overlay" id="instructorAuthModal">
    <div class="modal-card" style="max-width: 420px; text-align: center;">
        <div style="font-size: 2.2rem; margin-bottom: 4px;">🔐</div>
        <h3 style="font-size: 1.25rem; color: var(--purple-primary); font-weight: 900;">دخول لوحة المدرس</h3>
        <p style="font-size: 0.88rem; color: var(--text-secondary); font-weight: 700;">أدخل كلمة مرور المدرس للمتابعة وإدارة الواجبات:</p>
        <div style="position: relative; margin: 12px 0;">
            <input type="password" id="instructorPasscodeInput" placeholder="اكتب كلمة المرور هنا" 
                   style="width: 100%; padding: 12px 16px; background: #0A0612; border: 2px solid var(--purple-primary); color: #FFF; border-radius: 12px; font-family: 'JetBrains Mono', inherit; font-size: 1.1rem; font-weight: 800; text-align: center; outline: none;"
                   onkeydown="if(event.key==='Enter') verifyInstructorPassword()">
        </div>
        <div id="authErrorMsg" style="display: none; color: var(--red); font-weight: 800; font-size: 0.85rem; margin-bottom: 8px;">
            ❌ كلمة المرور غير صحيحة!
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
    <div class="modal-card" style="max-width: 420px; text-align: center;">
        <div style="width: 60px; height: 60px; margin: 0 auto 8px auto; border-radius: 14px; overflow: hidden; border: 2px solid var(--purple-primary);">
            <img src="{logo_base64}" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        <h3 style="font-size: 1.3rem; color: var(--purple-primary); font-weight: 900;">أهلاً بك يا بطل المستقبل!</h3>
        <p style="font-size: 0.88rem; color: var(--text-secondary); font-weight: 700;">اكتب اسمك عشان مستر مصطفى يتابع حلك للواجب أسبوع بأسبوع:</p>
        <input type="text" id="studentNameInput" placeholder="اكتب اسمك هنا (مثلاً: علي أحمد)" 
               style="width: 100%; padding: 12px 16px; background: #0A0612; border: 2px solid var(--purple-primary); color: #FFF; border-radius: 12px; font-family: inherit; font-size: 1rem; font-weight: 800; text-align: center; outline: none; margin: 10px 0;">
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
                <span style="background: rgba(16, 185, 129, 0.2); color: #34D399; font-size: 0.72rem; font-weight: 800; padding: 2px 8px; border-radius: 10px;">
                    مُسجل دخول ✓
                </span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <button class="btn-secondary-action" style="color: #F87171; border-color: rgba(239, 68, 68, 0.4);" onclick="lockInstructorMode()">
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
            <button class="btn-secondary-action" onclick="exportSubmissionsCSV()">
                <span>📊 تصدير درجات الطلاب (CSV)</span>
            </button>
        </div>

        <h4 style="font-size: 0.95rem; color: #E2E8F0; font-weight: 800; margin-top: 6px;">
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
            <h3 id="detailStudentTitle">تفاصيل حل الطالب: علي</h3>
            <button class="modal-close-btn" onclick="document.getElementById('studentDetailModal').classList.remove('open')">✕</button>
        </div>
        <div id="studentDetailContent" style="display: flex; flex-direction: column; gap: 12px;"></div>
    </div>
</div>

<!-- TOAST -->
<div class="toast" id="toastMsg">تم تسليم السؤال بنجاح ✓</div>

<script>
    const INSTRUCTOR_PASSCODE = "100020003000";

    const DEFAULT_TASKS = {tasks_week_01_json};
    const REFERENCE_TASKS = {tasks_reference_json};

    let activeTasksData = DEFAULT_TASKS;
    let allQuestionsList = [];
    let currentQuestionIndex = 0;
    let currentStudentName = localStorage.getItem('genie_active_student') || 'علي';
    let currentSubmissions = {{}};
    let selectedOptionIndex = null;

    function initApp() {{
        loadStudentData();
        buildQuestionList();
        renderNavChips();
        renderCurrentQuestion();
        updateHeaderInfo();

        if (!localStorage.getItem('genie_active_student')) {{
            openNameModal();
        }}

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
        document.getElementById('headerStudentName').innerText = `${{currentStudentName}}`;
        document.getElementById('avatarLetter').innerText = currentStudentName.charAt(0) || 'ط';
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

        // Auto scroll active chip into view smoothly
        const activeChip = strip.querySelector('.nav-chip.active');
        if (activeChip) {{
            activeChip.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
        }}
    }}

    // RENDER CURRENT QUESTION CANVAS (STRICTLY NO SPOILERS IN TITLE)
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

        // NO SPOILERS: ONLY SHOW THE QUESTION ITSELF!
        document.getElementById('taskTitleText').innerText = data.question || data.instructions || '';
        document.getElementById('taskHintText').innerText = data.hint || 'فكر بهدوء خطوة بخطوة يا بطل.';

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
                showFeedback(false, `شاشة الرن طلعت: "${{result.output.trim()}}". اتأكد من أرقامك والعمليات.`);
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

    // INSTRUCTOR AUTHENTICATION
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
                    <td><span style="color: var(--yellow); font-weight: 800;">${{skipped}}</span></td>
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
            card.style.background = 'var(--bg-card-elevated)';
            card.style.border = '1px solid var(--border-color)';
            card.style.borderRadius = '10px';
            card.style.padding = '10px 14px';

            let statusHtml = '<span style="color: var(--text-muted); font-weight: 800;">لم يُحل</span>';
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
                        <div style="background: #08060E; color: #4ADE80; padding: 6px 10px; border-radius: 6px; font-family: monospace; font-size: 0.8rem; direction: ltr; margin-top: 6px; border: 1px solid #231C3D;">
                            ${{escapeHtml(sub.code)}}
                        </div>
                    `;
                }}
            }}

            card.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 800; color: var(--gold-accent); font-size: 0.9rem;">${{idx + 1}}. ${{q.data.question ? q.data.question.substring(0, 45) + '...' : ''}}</span>
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
                csv += `"${{stName}}","${{q.data.question || qId}}","${{status}}","${{ans}}","${{time}}"\\n`;
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

print(f"Updated index.html: {index_path} ({os.path.getsize(index_path)} bytes)")
print(f"Updated artifact: {artifact_html_path} ({os.path.getsize(artifact_html_path)} bytes)")
