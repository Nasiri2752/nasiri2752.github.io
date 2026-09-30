# -*- coding: utf-8 -*-
"""محتوای رزومه — دو زبان کاملاً متناظر. هر مورد: en و fa.
کلید full=True یعنی فقط در نسخه‌ی کامل می‌آید."""

WEB = "https://nasiri2752.github.io/"
LI = "https://www.linkedin.com/in/hassan-nasiri-khonsari-44bb49198/"
DOI = "https://doi.org/10.1038/s41598-025-25586-0"

T = {
 "en": dict(
  name="Hassan Nasiri Khonsari",
  headline="Mechanical &amp; Mechatronics Design Engineer — Industrial Robots, Custom Machinery &amp; Automation",
  contact=["Tehran, Iran", "+98 936 804 7725", '<a href="mailto:Nasiri2752@Gmail.com">Nasiri2752@Gmail.com</a>',
           f'<a href="{WEB}">nasiri2752.github.io</a>', f'<a href="{LI}">LinkedIn</a>'],
  qr_web="Website", qr_li="LinkedIn",
  h=dict(summary="Summary", exp="Experience", honors="Honors &amp; Awards", proj="Selected Projects",
         earlier="Earlier Projects", edu="Education", pub="Publications", skills="Skills",
         lang="Languages", media="Media", comps="Student Competitions"),
  footer="Hassan Nasiri Khonsari — Résumé", updated="Updated Sep 2026 · v1.5",
  summary="Mechanical and mechatronics engineer with an MSc in Applied Design from Sharif University of Technology. "
          "I design industrial machines and robots and follow them through fabrication, assembly and commissioning — "
          "from postal sorting robots in national service to medical test equipment, industrial CNC machines and 3D printers.",
 ),
 "fa": dict(
  name="حسن نصیری خونساری",
  headline="مهندس طراحی مکانیک و مکاترونیک — ربات‌های صنعتی، ماشین‌آلات سفارشی و اتوماسیون",
  contact=["تهران، ایران", "۰۹۳۶۸۰۴۷۷۲۵", '<a href="mailto:Nasiri2752@Gmail.com">Nasiri2752@Gmail.com</a>',
           f'<a href="{WEB}">nasiri2752.github.io</a>', f'<a href="{LI}">لینکدین</a>'],
  qr_web="وب‌سایت", qr_li="لینکدین",
  h=dict(summary="خلاصه", exp="سوابق کاری", honors="افتخارات", proj="پروژه‌های منتخب",
         earlier="پروژه‌های پیشین", edu="تحصیلات", pub="انتشارات", skills="مهارت‌ها",
         lang="زبان‌ها", media="رسانه", comps="مسابقه‌های دانشجویی"),
  footer="رزومه‌ی حسن نصیری خونساری", updated="به‌روزرسانی: مهر ۱۴۰۵ · نسخه‌ی ۱٫۵",
  summary="مهندس مکانیک و مکاترونیک، دانش‌آموخته‌ی کارشناسی ارشد طراحی کاربردی از دانشگاه صنعتی شریف. "
          "ماشین‌ها و ربات‌های صنعتی را طراحی می‌کنم و ساخت، مونتاژ و راه‌اندازی آن‌ها را هم پیگیری می‌کنم؛ "
          "از ربات‌های سورتر پستی که در شبکه‌ی ملی پست به کار گرفته شده‌اند تا تجهیزات آزمون پزشکی، CNC صنعتی و پرینترهای سه‌بعدی.",
 ),
}

EXP = [
 dict(en=("Apr 2025 – Present", "Senior Mechanical Engineer", "Karun HiTech Solutions — Tehran",
          ["Part and assembly design; dimensional and weld inspection.",
           "Management of external machining and fabrication workshops; over 8,000 industrial parts delivered to date."]),
      fa=("فروردین ۱۴۰۴ تا اکنون", "مهندس ارشد مکانیک", "کارون (Karun HiTech Solutions) — تهران",
          ["طراحی قطعه و مجموعه؛ بازرسی ابعادی و جوش.",
           "مدیریت کارگاه‌های ماشین‌کاری و ساخت بیرونی؛ تا امروز بیش از ۸٬۰۰۰ قطعه‌ی صنعتی تحویل شده است."])),
 dict(en=("Feb – Jun 2024", "Lecturer", "University of Tehran, Kish International Campus",
          ["Taught Manufacturing Processes and Physics II."]),
      fa=("بهمن ۱۴۰۲ تا خرداد ۱۴۰۳", "مدرس", "دانشگاه تهران، پردیس بین‌المللی کیش",
          ["تدریس دروس «روش‌های تولید» و «فیزیک ۲»."])),
 dict(en=("Jan 2021 – May 2025", "Head of Mechanical Engineering Department", "Tensor Intelligent Machines — Tehran",
          ["Led the mechanical design and development of industrial robots, including Iran’s first postal sorting robot of its type and its automatic charging system.",
           "Managed production of 50 sorter robots for the Chaharrah-e Lashkar parcel center in Tehran and 30 for the Kermanshah center; the third-generation design went into production as a 200-unit series.",
           "Coordinated fabrication workshops and supervised the assembly and integration team."]),
      fa=("دی ۱۳۹۹ تا اردیبهشت ۱۴۰۴", "مدیر واحد مهندسی مکانیک", "ماشین‌های هوشمند تنسور — تهران",
          ["هدایت طراحی و توسعه‌ی مکانیکی ربات‌های صنعتی، از جمله نخستین ربات سورتر پستی از این نوع در ایران و سامانه‌ی شارژ خودکار آن.",
           "مدیریت ساخت ۵۰ ربات سورتر برای مرکز توزیع مرسولات چهارراه لشکر تهران و ۳۰ ربات برای مرکز کرمانشاه؛ طراحی نسل سوم در تیراژ ۲۰۰ دستگاه به تولید رسید.",
           "هماهنگی کارگاه‌های ساخت و سرپرستی تیم مونتاژ و یکپارچه‌سازی."])),
 dict(en=("2021 – 2024", "Product Design Manager (part-time)", "LeaMech Group — Tehran",
          ["Mechanical and mechatronic design of a smart mobile robot with omnidirectional wheels, from concept to working prototype, covering both mechanics and electronics."]),
      fa=("۱۴۰۰ تا ۱۴۰۳", "مدیر طراحی محصول (پاره‌وقت)", "گروه لیمک (LeaMech) — تهران",
          ["طراحی مکانیک و مکاترونیک یک موبوربات هوشمند با چرخ‌های همه‌جهته، از مفهوم تا نمونه‌ی کارکردی، در هر دو بخش مکانیک و الکترونیک."])),
 dict(en=("", "Engineer — Automatic Coil-Winding Machine", "Viraafanavar",
          ["Worked on a fully automatic coil-winding machine for the solenoid bobbins of ABS brake systems."]),
      fa=("", "مهندس — دستگاه سیم‌پیچی تمام‌خودکار", "ویرافناور",
          ["کار روی دستگاه تمام‌خودکار سیم‌پیچی بوبین سلونوئیدهای ترمز ABS."])),
 dict(en=("Oct 2019 – Mar 2020", "Project Intern — City Theater Automation", "Durali System Design &amp; Automation (DSDA)",
          ["Automation of the stage machinery in the main hall of Tehran City Theater."]),
      fa=("مهر تا اسفند ۱۳۹۸", "کارآموز پروژه — اتوماسیون تئاتر شهر", "شرکت طراحی و اتوماسیون سیستم دورعلی (DSDA)",
          ["اتوماسیون ماشین‌آلات صحنه‌ی تالار اصلی تئاتر شهر تهران."])),
 dict(en=("2020 – 2021", "Teaching Assistant — Statics (two semesters)", "Sharif University of Technology", []),
      fa=("۱۳۹۸ و ۱۳۹۹", "دستیار آموزشی استاتیک (دو نیم‌سال)", "دانشگاه صنعتی شریف", [])),
 dict(en=("2016 – 2018", "Teaching Assistant — Physics I and Dynamics", "Iran University of Science and Technology", []),
      fa=("۱۳۹۵ و ۱۳۹۶", "دستیار آموزشی فیزیک ۱ و دینامیک", "دانشگاه علم و صنعت ایران", [])),
 dict(en=("Summers 2016, 2018", "Summer Internships", "Sadra (Rahpooyan-e Aflak) · Sigma Design &amp; Modeling",
          ["Sadra: mechatronics and control — position control of a 3-DOF table (2018).",
           "Sigma: part drafting and modeling in CATIA (2016)."]),
      fa=("تابستان ۱۳۹۵ و ۱۳۹۷", "کارآموزی تابستانی", "صنعت و دانش رهپویان افلاک (صدرا) · طراحی هواگرد سیگما",
          ["صدرا: مکاترونیک و کنترل؛ کنترل موقعیت یک میز سه‌درجه‌آزادی (۱۳۹۷).",
           "سیگما: نقشه‌کشی و مدل‌سازی قطعات با CATIA (۱۳۹۵)."])),
]

HONORS_TOP = [
 dict(en=("2026", "64th Alborz Prize — Laureate",
          "Technologists &amp; Inventors category, one of 12 laureates; for the knee prosthesis constraint and stability test apparatus. Honored by Sharif University of Technology with its silver medal."),
      fa=("۱۴۰۵", "برگزیده‌ی شصت‌وچهارمین جشنواره‌ی البرز",
          "بخش فناوران و مخترعان، یکی از ۱۲ برگزیده؛ برای دستگاه تست تقید و پایداری پروتز زانو. همراه با تقدیر دانشگاه صنعتی شریف و اهدای مدال نقره‌ی شریف.")),
 dict(en=("2025", "26th Khwarizmi Youth Award — 2nd Place", "For the mechanical design of postal sorting robots."),
      fa=("۱۴۰۳", "مقام دوم بیست‌وششمین جشنواره‌ی جوان خوارزمی", "برای طراحی مکانیکی ربات‌های سورتر پستی.")),
 dict(en=("2023", "24th Khwarizmi Youth Award — 2nd Place",
          "For the knee prosthesis constraint and stability test apparatus; recognized by the President, with a UNESCO certificate."),
      fa=("۱۴۰۱", "مقام دوم بیست‌وچهارمین جشنواره‌ی جوان خوارزمی",
          "برای دستگاه تست تقید و پایداری پروتز زانو؛ با تقدیر رئیس‌جمهور و گواهی یونسکو.")),
]
HONORS = [
 dict(en=("2024", "Top Startup, Sharif Science and Technology Park — smart postal robots team (Tensor)"),
      fa=("۱۴۰۳", "استارتاپ برتر پارک علم و فناوری شریف — تیم ربات‌های هوشمند پستی (تنسور)")),
 dict(en=("2024", "Top Design, 4th Iran Industrial Design Festival — smart postal robots (Tensor)"),
      fa=("۱۴۰۳", "طرح برتر چهارمین جشنواره‌ی طراحی صنعتی ایران — ربات‌های هوشمند پستی (تنسور)")),
 dict(en=("2022", "Top Technological Thesis, Department of Mechanical Engineering, Sharif University of Technology"),
      fa=("۱۴۰۰", "برترین پایان‌نامه‌ی فناورانه‌ی دانشکده‌ی مهندسی مکانیک دانشگاه صنعتی شریف")),
 dict(en=("2019", "Rank 11, final stage of the National Student Olympiad in Mechanical Engineering"),
      fa=("۱۳۹۷", "رتبه‌ی ۱۱ مرحله‌ی نهایی المپیاد علمی دانشجویی مهندسی مکانیک")),
 dict(en=("", "3rd KANS Scientific Competition — top 10% solutions in Electronics &amp; Robotics, and in Health &amp; Med-Tech"),
      fa=("", "سومین مسابقه‌ی علمی KANS — راه‌حل‌های ده‌درصد برتر در «الکترونیک و رباتیک» و «سلامت و فناوری پزشکی»")),
]
COMPS = [
 dict(en="IUST Scissor Lift Design &amp; Build Competition — 1st place", fa="مسابقه‌ی طراحی و ساخت بالابر قیچی دانشگاه علم و صنعت — رتبه‌ی اول"),
 dict(en="IUST Pasta Bridge Competition — 4th place", fa="مسابقه‌ی پل ماکارونی دانشگاه علم و صنعت — رتبه‌ی چهارم"),
 dict(en="National Robots-in-the-City Competition — line follower, 5th place", fa="مسابقه‌ی کشوری ربات‌ها در شهر — ربات مسیریاب، رتبه‌ی پنجم"),
 dict(en="Khwarizmi National Competition — manual mine-detector robot", fa="مسابقات خوارزمی — ربات مین‌یاب دستی"),
]

EDU = [
 dict(en=("2019 – 2022", "MSc, Mechanical Engineering — Applied Design", "Sharif University of Technology",
          ["Supervisor: Prof. Mohammad Durali",
           "Thesis: Design, fabrication and calibration of a 6-DOF knee prosthesis constraint and stability test apparatus — graded Excellent",
           "GPA: 17.15 / 20"]),
      fa=("۱۳۹۸ تا ۱۴۰۱", "کارشناسی ارشد مهندسی مکانیک — طراحی کاربردی", "دانشگاه صنعتی شریف",
          ["استاد راهنما: دکتر محمد دورعلی",
           "پایان‌نامه: طراحی، ساخت و کالیبراسیون دستگاه تست تقید و پایداری پروتز زانو در شش درجه‌ی آزادی — دفاع با نمره‌ی عالی",
           "معدل: ۱۷٫۱۵ از ۲۰"])),
 dict(en=("2015 – 2019", "BSc, Mechanical Engineering", "Iran University of Science and Technology",
          ["Supervisor: Dr. Seyed Ali Niknam",
           "Thesis: Detail design of a powder supply machine for direct metal deposition (DMD)",
           "GPA: 17.30 / 20"]),
      fa=("۱۳۹۴ تا ۱۳۹۸", "کارشناسی مهندسی مکانیک", "دانشگاه علم و صنعت ایران",
          ["استاد راهنما: دکتر سید علی نیکنام",
           "پایان‌نامه: طراحی تفصیلی دستگاه تغذیه‌ی پودر برای فرآیند لایه‌نشانی مستقیم فلز (DMD)",
           "معدل: ۱۷٫۳۰ از ۲۰"])),
]
EDU_NOTE = dict(
 en="National entrance exams: rank 16 among more than 10,000 (MSc, Mechanical Engineering) and rank 795 among 182,000 (BSc). Admitted to the MSc through the exceptional-talent track. National Elites Foundation: 300 points in the Sina system.",
 fa="کنکور سراسری: رتبه‌ی ۱۶ در میان بیش از ۱۰٬۰۰۰ شرکت‌کننده (کارشناسی ارشد مهندسی مکانیک) و رتبه‌ی ۷۹۵ در میان ۱۸۲٬۰۰۰ نفر (کارشناسی). برگزیده‌ی استعداد درخشان برای ورود به مقطع کارشناسی ارشد. بنیاد ملی نخبگان: ۳۰۰ امتیاز در سامانه‌ی سینا.")

PUB = dict(
 en=dict(authors="A. Abedi, F. Farahmand, M. Salmanimehrjardi, <b>H. Nasiri Khonsari</b>",
         venue="<i>Scientific Reports</i> (Nature Portfolio), 2025 · DOI: 10.1038/s41598-025-25586-0",
         role="My role: developed and built the friction test apparatus.",
         book="<b>Physics Olympiads in Iran</b> — co-author, Khoshkhan Publications, 2018."),
 fa=dict(authors="A. Abedi, F. Farahmand, M. Salmanimehrjardi, <b>H. Nasiri Khonsari</b>",
         venue="مجله‌ی <i>Scientific Reports</i> از مجموعه‌ی Nature، ۲۰۲۵ · DOI: 10.1038/s41598-025-25586-0",
         role="نقش من: توسعه و ساخت دستگاه آزمون اصطکاک.",
         book="<b>المپیادهای فیزیک در ایران</b> — هم‌نویسنده، نشر خوشخوان، ۱۳۹۷."),
 title="Frictional behavior between bone and additively manufactured Ti6Al4V implants is affected by bone density and surface texture under varying loads")

PROJ = [
 dict(imgs=[("sorter-1", "Generation 1", "نسل اول"), ("sorter-2", "Generation 2", "نسل دوم"),
            ("sorter-3", "Generation 3", "نسل سوم"), ("fleet-sorter", "In service", "در حال کار")],
      en=("Postal Sorting Robots", "Tensor · 2021 – 2025",
          "Iran’s first postal sorting robot of its type, developed across three generations. I was responsible for the load-discharge mechanism, weighing system, structure and drive system, and designed its automatic charging system. 80 robots serve the Tehran and Kermanshah parcel centers, and the third generation went into production as a 200-unit series. Project value of the first 50-unit set: about US$67,000. 2nd place, 26th Khwarizmi Youth Award."),
      fa=("ربات‌های سورتر پستی", "تنسور · ۱۳۹۹ تا ۱۴۰۴",
          "نخستین ربات سورتر پستی از این نوع در ایران که در سه نسل توسعه یافت. طراحی مکانیزم تخلیه‌ی بار، سامانه‌ی توزین، استراکچر و سیستم حرکت با من بود و سامانه‌ی شارژ خودکار آن را هم طراحی کردم. ۸۰ ربات در مراکز توزیع مرسولات تهران و کرمانشاه کار می‌کنند و نسل سوم در تیراژ ۲۰۰ دستگاه به تولید رسید. ارزش نخستین مجموعه‌ی ۵۰ دستگاهی: حدود ۶۷ هزار دلار. مقام دوم بیست‌وششمین جشنواره‌ی جوان خوارزمی.")),
 dict(imgs=[("knee", "", "")],
      en=("Knee Prosthesis Constraint &amp; Stability Test Apparatus", "Sharif University of Technology · 2021",
          "A 6-DOF apparatus for constraint and stability testing of total knee replacements per ASTM F1223 — my MSc thesis under Prof. Mohammad Durali, with Prof. Farahmand as consulting advisor. Mechanical design, automation architecture, PLC programming and HMI development. No comparable apparatus existed in Iran; commercial equivalents are made by EndoLab (Germany) and AMTI (USA). Later reconfigured for a bone–implant friction study published in Scientific Reports. 64th Alborz Prize; 2nd place, 24th Khwarizmi Youth Award."),
      fa=("دستگاه تست تقید و پایداری پروتز زانو", "دانشگاه صنعتی شریف · ۱۴۰۰",
          "دستگاهی برای آزمون تقید و پایداری پروتز کامل زانو در شش درجه‌ی آزادی، مطابق استاندارد ASTM F1223؛ پایان‌نامه‌ی کارشناسی ارشد زیر نظر دکتر محمد دورعلی و با مشاوره‌ی دکتر فرهمند. طراحی مکانیکی، معماری اتوماسیون، برنامه‌نویسی PLC و توسعه‌ی HMI. پیش از این نمونه‌ی مشابهی در ایران وجود نداشت و معادل‌های تجاری آن را EndoLab آلمان و AMTI آمریکا می‌سازند. بعدها برای مطالعه‌ی اصطکاک میان استخوان و ایمپلنت بازپیکربندی شد که حاصلش مقاله‌ای در Scientific Reports است. برگزیده‌ی شصت‌وچهارمین جشنواره‌ی البرز و مقام دوم بیست‌وچهارمین جشنواره‌ی جوان خوارزمی.")),
 dict(imgs=[("cnc", "Machine", "دستگاه"), ("cnc-panel", "Control cabinet", "تابلو برق"), ("cnc-open", "Inside the cabinet", "داخل تابلو")],
      en=("Dual-Purpose Industrial CNC", "2023",
          "An industrial CNC machine for wood and light metals with a working envelope of about 100 × 100 × 30 cm, designed to be modular: with a simple head change it becomes a high-capacity 3D printer. Structural design, drive and motor selection, and commissioning of the G-code control system."),
      fa=("CNC صنعتی دوکاره", "۱۴۰۲",
          "دستگاه CNC صنعتی برای برش چوب و فلزات سبک با ابعاد کاری حدود ۱۰۰×۱۰۰×۳۰ سانتی‌متر که ماژولار طراحی شده است: با تعویض ساده‌ی هد، به یک پرینتر سه‌بعدی قدرتمند تبدیل می‌شود. طراحی سازه، انتخاب درایوها و موتورها و راه‌اندازی سیستم کنترل G-Code.")),
 dict(imgs=[("printer-1", "Generation 1", "نسل اول"), ("printer-2", "Generation 2", "نسل دوم"), ("printer-3", "Generation 3", "نسل سوم")],
      en=("Industrial FDM 3D Printers", "2020 – 2023",
          "Five machines designed and built from scratch and re-engineered across generations, from a 200 × 200 × 150 mm unit to an industrial machine with a 500 × 500 × 400 mm build volume running ball screws and industrial linear rails on every axis. Frame, mechanism, motor selection, electronics, firmware and slicer optimization were all done independently."),
      fa=("پرینترهای سه‌بعدی FDM صنعتی", "۱۳۹۹ تا ۱۴۰۲",
          "پنج دستگاه که از صفر طراحی و ساخته و نسل‌به‌نسل بازمهندسی شدند؛ از یک دستگاه ۲۰۰×۲۰۰×۱۵۰ میلی‌متری تا ماشینی صنعتی با حجم کاری ۵۰۰×۵۰۰×۴۰۰ میلی‌متر که روی همه‌ی محورها بال‌اسکرو و ریل خطی صنعتی دارد. سازه، مکانیزم، انتخاب موتورها، الکترونیک، فرم‌ور و بهینه‌سازی اسلایسر، همه مستقل انجام شد.")),
 dict(imgs=[("waiter", "", ""), ("fleet-waiter", "Fleet of seven", "ناوگان هفت‌تایی")],
      en=("Waiter Robots", "2021",
          "Iran’s first waiter robot of its type. Mechanical design, fabrication and assembly of a seven-unit fleet; the chassis and drive system were designed for reliable operation on uneven restaurant floors."),
      fa=("ربات‌های گارسون", "۱۴۰۰",
          "نخستین ربات گارسون از این نوع در ایران. طراحی، ساخت و مونتاژ مکانیکی ناوگانی هفت‌تایی؛ شاسی و سیستم حرکت طوری طراحی شد که ربات‌ها روی کف ناهموار رستوران هم قابل اعتماد کار کنند.")),
 dict(imgs=[("dmd", "", "")],
      en=("DMD Powder Feeder", "Iran University of Science and Technology · 2018",
          "A powder feeder for laser direct metal deposition (DMD): detail design, fabrication, and full implementation of the electronics, control and logic; the feed rate is controlled across 1–100 g/min. BSc thesis."),
      fa=("سامانه‌ی تغذیه‌ی پودر DMD", "دانشگاه علم و صنعت ایران · ۱۳۹۷",
          "تغذیه‌کننده‌ی پودر برای فرآیند لایه‌نشانی مستقیم فلز با لیزر (DMD): طراحی تفصیلی، ساخت و پیاده‌سازی کامل الکترونیک، کنترل و منطق دستگاه؛ نرخ تغذیه در بازه‌ی ۱ تا ۱۰۰ گرم بر دقیقه کنترل می‌شود. پایان‌نامه‌ی کارشناسی.")),
 dict(imgs=[("painter", "", ""), ("plotter-portrait", "Portrait drawing", "رسم چهره")],
      en=("Cable-Driven Drawing Robot", "2020",
          "A drawing robot based on a cable-driven mechanism: the pen is positioned by controlling cable lengths. It converts any photo into a hatched drawing and draws it on the canvas."),
      fa=("ربات نقاش کابلی", "۱۳۹۹",
          "ربات نقاش بر پایه‌ی مکانیزم ربات‌های کابلی: قلم با کنترل طول کابل‌ها جابه‌جا می‌شود. هر عکسی را به نقاشی هاشورخورده تبدیل می‌کند و روی بوم می‌کشد.")),
]

EARLIER_LINE = dict(
 en="<b>Earlier projects (2011 – 2020):</b> automation of a spinning process for kettle production; inverted pendulum and 3-DOF table with PID control; 2.5-axis plotters; a smart cooler controller with an Android app; an SMS home alarm; a high-voltage (&gt;1 kV) supply for electrowetting research; a greenhouse timer; ultrasonic range-finder calibration; mine-detector and line-follower robots.",
 fa="<b>پروژه‌های پیشین (۱۳۹۰ تا ۱۳۹۹):</b> اتوماسیون فرآیند اسپینینگ برای تولید کتری؛ پاندول معکوس و میز سه‌درجه‌آزادی با کنترل PID؛ پلاترهای دوونیم‌محوره؛ کنترلر هوشمند کولر با اپلیکیشن اندرویدی؛ دزدگیر پیامکی؛ مدار ولتاژ بالا (بیش از یک کیلوولت) برای پژوهش الکترووتینگ؛ تایمر گلخانه؛ کالیبراسیون فاصله‌سنج اولتراسونیک؛ و ربات‌های مین‌یاب و مسیریاب.")

EARLIER_PHOTOS = [
 ("table-3dof", "3-DOF simulation table", "میز شبیه‌ساز سه‌درجه‌آزادی"),
 ("plotter-iran", "Cable plotter — map drawing", "ربات نقاش — رسم نقشه"),
 ("plotter-25", "2.5-axis plotter", "پلاتر دوونیم‌محوره"),
 ("plotter-mini", "Mini 2.5-axis plotter", "پلاتر کوچک دوونیم‌محوره"),
 ("cooler", "Smart cooler controller", "کنترلر هوشمند کولر"),
 ("alarm", "Smart home alarm", "دزدگیر هوشمند"),
 ("scissor", "Scissor lift", "بالابر قیچی"),
 ("mine", "Mine-detector robot", "ربات مین‌یاب"),
 ("printer-old", "First 3D printer", "نخستین پرینتر سه‌بعدی"),
 ("cnc-cad", "CNC — computer model", "CNC — مدل کامپیوتری"),
]
EARLIER_LIST = [
 ("Automation of a forming/spinning process for kettle production (2018)", "اتوماسیون فرآیند Forming/Spinning برای تولید کتری (۱۳۹۷)"),
 ("Inverted pendulum setup controlled with Arduino and a PID controller (2018)", "ساخت ستاپ پاندول معکوس و کنترل آن با آردوینو و کنترلر PID (۱۳۹۷)"),
 ("PID control of the DC motors of a 3-DOF table with encoders, on ARM microcontrollers (2017)", "راه‌اندازی و کنترل میز سه‌درجه‌آزادی با کنترلر PID و انکودر روی میکروکنترلرهای ARM (۱۳۹۶)"),
 ("Smart air-water cooler controller with a custom Android app (2017)", "کنترلر هوشمند کولر آبی با اپلیکیشن اندرویدی اختصاصی (۱۳۹۶)"),
 ("2.5-axis plotter for vector drawings on A4 paper (2019)", "پلاتر دوونیم‌محوره برای رسم فایل‌های وکتوری روی کاغذ A4 (۱۳۹۸)"),
 ("Mini 2.5-axis plotter for 7 cm drawings (2017)", "پلاتر کوچک دوونیم‌محوره برای رسم روی کاغذ ۷ سانتی‌متری (۱۳۹۶)"),
 ("Home alarm that calls the owner directly and switches appliances by SMS (2019)", "دزدگیر با تماس تلفنی مستقیم با صاحبخانه و کنترل وسایل برقی با پیامک (۱۳۹۸)"),
 ("High-voltage circuit generating over 1 kV for electrowetting research (2017)", "مدار ولتاژ بالا با توان تولید بیش از یک کیلوولت برای پژوهش در الکترووتینگ (۱۳۹۶)"),
 ("Ultrasonic range-finder measurement project: calibration and static and dynamic error analysis (2017)", "پروژه‌ی سیستم اندازه‌گیری با فاصله‌سنج اولتراسونیک: کالیبراسیون و تحلیل خطای استاتیک و دینامیک (۱۳۹۶)"),
 ("Two-channel 220 V timer for greenhouse equipment (2020)", "تایمر دوکاناله‌ی ۲۲۰ ولت برای تجهیزات گلخانه (۱۳۹۹)"),
 ("Special-purpose thermometer circuit (2015)", "مدار دماسنج با کاربری خاص (۱۳۹۴)"),
 ("Mine-detector and line-follower robots (2011, 2012)", "ربات‌های مین‌یاب و مسیریاب (۱۳۹۰ و ۱۳۹۱)"),
 ("Work with industrial servo motors, Delta three-phase servo drives and industrial mechatronic equipment", "کار با سروو موتور صنعتی، سروو درایو سه‌فاز دلتا و تجهیزات مکاترونیکی صنعتی"),
]

SKILLS = [
 dict(en=("Design &amp; analysis", "SolidWorks, CATIA, ANSYS Workbench (Fluent, Meshing, ICEM), SolidWorks Simulation, mechanism design, FEA, MATLAB, Mathematica"),
      fa=("طراحی و تحلیل", "SolidWorks، CATIA، ANSYS Workbench (Fluent، Meshing، ICEM)، SolidWorks Simulation، طراحی مکانیزم، تحلیل اجزای محدود، MATLAB، Mathematica")),
 dict(en=("Manufacturing", "CNC machining, SolidCAM, Mastercam, G-code, GD&amp;T, welded structures, 3D printing (Cura, Simplify3D)"),
      fa=("ساخت و تولید", "ماشین‌کاری CNC، SolidCAM، Mastercam، G-Code، GD&amp;T، سازه‌های جوشی، پرینت سه‌بعدی (Cura، Simplify3D)")),
 dict(en=("Automation &amp; control", "Delta PLC (WPLSoft), Siemens TIA Portal (LAD/FBD), SIMATIC Manager, HMI, LabVIEW, Delta servo drives, motion control"),
      fa=("اتوماسیون و کنترل", "PLC دلتا (WPLSoft)، Siemens TIA Portal (LAD/FBD)، SIMATIC Manager، HMI، LabVIEW، سروو درایو دلتا، کنترل حرکت")),
 dict(en=("Electronics &amp; embedded", "ARM/STM32 (Keil, STM32CubeMX, STMStudio), AVR and Arduino (C), CodeVision, Proteus, Altium Designer"),
      fa=("الکترونیک و میکروکنترلر", "ARM/STM32 (Keil، STM32CubeMX، STMStudio)، AVR و Arduino (C)، CodeVision، Proteus، Altium Designer")),
 dict(en=("Project management", "MS Project"), fa=("مدیریت پروژه", "MS Project")),
 dict(full=True, en=("Other", "Blender, Android Studio (Java/XML), Carrier, Revit MEP, pipe-flow and duct sizing"),
      fa=("سایر", "Blender، Android Studio (Java/XML)، Carrier، Revit MEP، طراحی لوله‌کشی و کانال")),
]
LANGS = dict(en="Persian — native · English — professional working proficiency · Arabic — limited working proficiency",
             fa="فارسی — زبان مادری · انگلیسی — سطح کاری حرفه‌ای · عربی — سطح کاری محدود")

MEDIA = [
 dict(qr="n-sharif", en=("From Design to Fabrication: The Researcher Who Built a Knee Prosthesis Test Apparatus in Iran", "Sharif University of Technology Public Relations · 26 Sep 2026"),
      fa=("از طراحی تا ساخت؛ روایت پژوهشگری که دستگاه آزمون پروتز زانو را در کشور ساخت", "روابط عمومی دانشگاه صنعتی شریف · ۴ مهر ۱۴۰۵"), url="https://news.sharif.ir/fa/article/76256078"),
 dict(qr="n-honor", en=("Sharif University Honors Three Alborz Prize Laureates", "Sharif University of Technology · 21 Sep 2026"),
      fa=("تجلیل از سه برگزیده جایزه البرز در دانشگاه صنعتی شریف", "دانشگاه صنعتی شریف · ۳۰ شهریور ۱۴۰۵"), url="https://www.sharif.ir/fa/web/news/w/%D8%AA%D8%AC%D9%84%DB%8C%D9%84-%D8%A7%D8%B2-%D8%B3%D9%87-%D8%A8%D8%B1%DA%AF%D8%B2%DB%8C%D8%AF%D9%87-%D8%AC%D8%A7%DB%8C%D8%B2%D9%87-%D8%A7%D9%84%D8%A8%D8%B1%D8%B2-%D8%AF%D8%B1-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4"),
 dict(qr="v-alborz", en=("64th Alborz Prize ceremony", "Alborz Foundation · 25 Aug 2026"),
      fa=("مراسم شصت‌وچهارمین جایزه‌ی البرز", "بنیاد البرز · ۳ شهریور ۱۴۰۵"), url="https://www.aparat.com/v/xdw0223"),
 dict(qr="n-bmn14", en=("Iran on the Path of Progress: Linking Universities and Industry", "Paper, 14th National Elites Conference · 2 Oct 2024"),
      fa=("ایران در مسیر پیشرفت؛ پیوند دانشگاه و صنعت", "مقاله‌ی چهاردهمین همایش ملی نخبگان · ۱۱ مهر ۱۴۰۳"), url="https://openaccess.ir/c/bmn14/paper_114387"),
 dict(qr="v-ofogh", en=("Documentary: Hassan Nasiri Khonsari", "Ofogh TV, “Tazeh Nafas” · aired 5–6 Jun 2024"),
      fa=("مستند زندگی حسن نصیری خونساری", "شبکه‌ی افق، برنامه‌ی «تازه‌نفس» · پخش: ۱۶ و ۱۷ خرداد ۱۴۰۳"), url="https://telewebion.net/episode/0xd5fdaa5"),
 dict(qr="v-amoozesh", en=("Interview on “Va Amma Emrooz”", "Amoozesh TV · 13 Jan 2024"),
      fa=("گفت‌وگو در برنامه‌ی «و اما امروز»", "شبکه‌ی آموزش · ۲۳ دی ۱۴۰۲"), url="https://telewebion.net/episode/0xac965d7"),
 dict(qr="n-irna", en=("“Student projects should be drawn from industry needs”", "IRNA News Agency · 7 Apr 2023"),
      fa=("«پروژه‌های دانشجویان باید برگرفته از نیازهای صنعتی باشد»", "خبرگزاری ایرنا · ۱۸ فروردین ۱۴۰۲"), url="https://www.irna.ir/news/85069178/"),
 dict(qr="v-ch1", en=("Interview on “Iran Emrooz”", "IRIB TV1 · 12 Mar 2023"),
      fa=("گفت‌وگو در برنامه‌ی «ایران امروز»", "شبکه‌ی یک · ۲۱ اسفند ۱۴۰۱"), url="https://telewebion.net/episode/0x5cc2d6f"),
 dict(qr="v-ch6", en=("Special news interview: support for Khwarizmi Festival winners", "IRINN (TV6) · 28 Feb 2023"),
      fa=("گفت‌وگوی ویژه‌ی خبری: حمایت از برگزیدگان جشنواره‌ی خوارزمی", "شبکه‌ی خبر (شبکه‌ی ۶) · ۹ اسفند ۱۴۰۱"), url="https://telewebion.net/episode/0x59748e1"),
]
