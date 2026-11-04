# -*- coding: utf-8 -*-
"""محتوای سایت — فارسی و انگلیسی کنار هم. همه‌ی صفحه‌ها از همین فایل (و media.js) ساخته می‌شوند.
بعد از هر تغییر:  python3 site-src/build_site.py
قواعد نگارش: «ی» میانجی با نیم‌فاصله (پروژه‌ی، نه پروژهٔ)، «ی» و «ک» فارسی، ارقام فارسی در متن فارسی.
"""

# آدرس پایه‌ی سایت. بعد از وصل شدن دامنه‌ی hassannasiri.ir، این را به "https://hassannasiri.ir" تغییر بده و دوباره بساز.
BASE = "https://nasiri2752.github.io"

GA_ID = "G-6RH63PTDCY"
FORMSPREE = "https://formspree.io/f/mrevzvga"
EMAIL = "Nasiri2752@Gmail.com"
PHONE = "+989368047725"
PHONE_FA = "۰۹۳۶۸۰۴۷۷۲۵"
PHONE_EN = "+98 936 804 7725"
LINKEDIN = "https://www.linkedin.com/in/hassan-nasiri-khonsari-44bb49198/"
TELEGRAM = "https://t.me/Hnkh94"
BALE = "https://ble.ir/hnkh94"
INSTAGRAM = "https://www.instagram.com/Nasiri_2752/"
DOI = "https://doi.org/10.1038/s41598-025-25586-0"
SAME_AS = [LINKEDIN, TELEGRAM, BALE, INSTAGRAM]

NAME = dict(fa="حسن نصیری خونساری", en="Hassan Nasiri Khonsari")
JOB = dict(fa="مهندس طراحی مکانیک و مکاترونیک", en="Mechanical & Mechatronics Design Engineer")
# جمله‌ی تمایز برای موتورهای جستجو و هوش مصنوعی (فقط در داده‌ی ساخت‌یافته و llms.txt)
DISAMBIG = dict(
    fa="مهندس طراحی مکانیک و مکاترونیک، دانش‌آموخته‌ی دانشگاه صنعتی شریف و برگزیده‌ی جایزه‌ی البرز؛ این شخص با حسن نصیری، خواننده، متفاوت است.",
    en="Iranian mechanical and mechatronics design engineer (Sharif University of Technology alumnus, Alborz Prize laureate); not to be confused with the singer Hassan Nasiri.")

# ---------------------------------------------------------------- ناوبری و متن‌های عمومی
UI = {
 "fa": dict(
  nav=[("index", "خانه"), ("services", "خدمات و همکاری"), ("projects", "پروژه‌ها"), ("media", "رسانه"), ("about", "درباره و سوابق")],
  contact="تماس", lang_label="EN", call="تماس تلفنی", home="خانه",
  footer="همه‌ی حقوق محفوظ است.", resume="دانلود رزومه", all_projects="همه‌ی پروژه‌ها", all_media="همه‌ی رسانه‌ها",
  more_about="بیشتر درباره‌ی من", all_services="جزئیات خدمات و همکاری", view="مشاهده", year="سال",
  my_role="نقش من", key_facts="مشخصات و اعداد", related_media="در رسانه‌ها", awards="افتخارات این پروژه",
  similar="پروژه‌ی مشابهی دارید؟", similar_p="اگر ماشین، ربات یا دستگاهی شبیه این لازم دارید، از فرم پایین صفحه یا تلگرام پیام بدهید.",
  start_chat="شروع گفت‌وگو", photos="تصویرها", videos="ویدیوها", prev="پروژه‌ی قبلی", next="پروژه‌ی بعدی",
  no_photo="تصویر این پروژه به‌زودی اضافه می‌شود.", proof="نمونه", read="مطالعه‌ی خبر ↗", watch_tw="تماشا در تلوبیون ↗",
  play="پخش: ", gallery="گالری تصاویر", photo="تصویر ", close="بستن", prevb="قبلی", nextb="بعدی",
 ),
 "en": dict(
  nav=[("index", "Home"), ("services", "Services"), ("projects", "Projects"), ("media", "Media"), ("about", "About")],
  contact="Contact", lang_label="فارسی", call="Call", home="Home",
  footer="All rights reserved.", resume="Download Resume", all_projects="All projects", all_media="All media",
  more_about="More about me", all_services="Services and collaboration", view="View", year="Year",
  my_role="My role", key_facts="Key facts", related_media="In the media", awards="Awards for this project",
  similar="Have a similar project?", similar_p="If you need a machine, robot or rig like this, send a message through the form below or Telegram.",
  start_chat="Start a conversation", photos="Photos", videos="Videos", prev="Previous project", next="Next project",
  no_photo="Photos of this project will be added soon.", proof="Example", read="Read the article ↗", watch_tw="Watch on Telewebion ↗",
  play="Play: ", gallery="Photo gallery", photo="Photo ", close="Close", prevb="Previous", nextb="Next",
 ),
}

# ---------------------------------------------------------------- صفحه‌ی اصلی
HOME = {
 "fa": dict(
  title="حسن نصیری خونساری | مهندس طراحی مکانیک، رباتیک و ماشین‌آلات سفارشی",
  desc="حسن نصیری خونساری، مهندس طراحی مکانیک و مکاترونیک؛ طراحی و ساخت ماشین‌آلات سفارشی و ربات‌های صنعتی، تولید تیراژی قطعات با کنترل کیفیت و مشاوره. دانش‌آموخته‌ی شریف و برگزیده‌ی جایزه‌ی البرز.",
  eyebrow="مهندس طراحی مکانیک و مکاترونیک",
  headline="ربات‌های صنعتی، <b>ماشین‌آلات سفارشی</b> و اتوماسیون.",
  lead="ماشین‌ها و ربات‌های صنعتی را طراحی می‌کنم و ساخت، مونتاژ و راه‌اندازی‌شان را تا تحویل پیگیری می‌کنم. کارشناسی ارشد طراحی کاربردی از دانشگاه صنعتی شریف.",
  cta1="خدمات و همکاری", cta2="مشاهده‌ی پروژه‌ها",
  stats=[("۲۸۰", "ربات سورتر پستی در سه نسل"), ("+۸٬۰۰۰", "قطعه‌ی صنعتی تحویل‌شده"), ("۳", "جایزه‌ی ملی: البرز و دو خوارزمی"), ("۸", "پروژه‌ی طراحی و ساخت")],
  intro_kk="معرفی", intro_h="از ایده تا دستگاهی که کار می‌کند",
  intro=[
   "من حسن نصیری خونساری هستم؛ مهندس طراحی مکانیک و مکاترونیک، با کارشناسی ارشد طراحی کاربردی از دانشگاه صنعتی شریف. کارم طراحی ماشین‌آلات سفارشی و ربات‌های صنعتی است و فقط به نقشه بسنده نمی‌کنم: ساخت، مونتاژ و راه‌اندازی را هم تا روزی که دستگاه کار کند پیگیری می‌کنم.",
   "طراحی مکانیکی ربات‌های سورتر پستی شرکت ملی پست را در سه نسل انجام داده‌ام: ۸۰ ربات از نسل‌های اول و دوم در مراکز توزیع تهران و کرمانشاه کار می‌کنند و نسل سوم در تیراژ ۲۰۰ دستگاه به تولید رسید. دستگاه تست تقید و پایداری پروتز زانو، که پیش از آن نمونه‌ی مشابهی در ایران نداشت، برایم مقام دوم جشنواره‌ی جوان خوارزمی و برگزیدگی در شصت‌وچهارمین جایزه‌ی البرز را آورد.",
  ],
  svc_kk="همکاری", svc_h="چه کاری می‌توانم برایتان انجام دهم؟", svc_p="طراحی و ساخت، تولید تیراژی و مشاوره؛ هر کدام با نمونه‌ای واقعی که ساخته شده و کار می‌کند.",
  hon_kk="دستاوردها", hon_h="افتخارات برجسته",
  proj_kk="نمونه‌کارها", proj_h="پروژه‌های منتخب", proj_p="روی هر پروژه بزنید تا تصویرها، جزئیات و نقش من در آن را ببینید.",
  media_kk="رسانه", media_h="تازه‌ترین‌ها در رسانه‌ها",
 ),
 "en": dict(
  title="Hassan Nasiri Khonsari | Mechanical Design Engineer — Robotics & Custom Machinery",
  desc="Hassan Nasiri Khonsari, mechanical and mechatronics design engineer: custom machinery and industrial robots from design to commissioning, quality-controlled batch production of parts, and consulting. Sharif University alumnus, Alborz Prize laureate.",
  eyebrow="Mechanical & Mechatronics Design Engineer",
  headline="Industrial robots, <b>custom machinery</b> and automation.",
  lead="I design industrial machines and robots and follow them through fabrication, assembly and commissioning, until they are delivered and working. MSc in Applied Design, Sharif University of Technology.",
  cta1="Services", cta2="View projects",
  stats=[("280", "postal sorting robots, three generations"), ("8,000+", "industrial parts delivered"), ("3", "national awards: Alborz & two Khwarizmi"), ("8", "design-and-build projects")],
  intro_kk="Introduction", intro_h="From an idea to a working machine",
  intro=[
   "I'm Hassan Nasiri Khonsari, a mechanical and mechatronics design engineer with an MSc in Applied Design from Sharif University of Technology. I design custom machinery and industrial robots, and I don't stop at drawings: I follow fabrication, assembly and commissioning until the machine works.",
   "I led the mechanical design of Iran National Post's postal sorting robots across three generations: 80 robots from the first two generations run in the Tehran and Kermanshah distribution centers, and the third generation went into production as a 200-unit series. My knee prosthesis constraint and stability test apparatus — the first of its kind in Iran — won 2nd place at the Khwarizmi Youth Award and was selected at the 64th Alborz Prize.",
  ],
  svc_kk="Work with me", svc_h="What I can do for you", svc_p="Design and build, batch production and consulting — each backed by a real machine that was built and works.",
  hon_kk="Achievements", hon_h="Highlights",
  proj_kk="Portfolio", proj_h="Selected projects", proj_p="Open a project to see its photos, details and my role in it.",
  media_kk="Media", media_h="Latest in the media",
 ),
}

# ---------------------------------------------------------------- خدمات
SERVICES_PAGE = {
 "fa": dict(
  title="خدمات و همکاری | حسن نصیری خونساری — طراحی ماشین، ربات و تولید قطعات",
  desc="طراحی و ساخت ماشین‌آلات سفارشی، ربات‌های متحرک گروهی و خدماتی، تولید تیراژی قطعات با کنترل کیفیت، اتوماسیون و PLC، تجهیزات آزمون و مشاوره‌ی مسیر شغلی و جشنواره‌ها.",
  kk="خدمات و همکاری", h1="با هم چه کاری می‌توانیم انجام دهیم؟",
  lead="اگر پروژه‌ی طراحی و ساخت ماشین یا ربات دارید، قطعه‌ای را در تیراژ با کیفیت قابل‌اطمینان می‌خواهید، یا فقط دوست دارید درباره‌ی مسیر شغلی، یک ایده یا آماده شدن برای یک جشنواره گپ بزنیم، خوشحال می‌شوم با هم صحبت کنیم.",
  svc_h="طراحی، ساخت و تولید", cons_h="مشاوره و گفت‌وگو",
  cons_p="بخشی از تجربه‌ای که در این سال‌ها به دست آمده، به درد کسی می‌خورد که تازه در همین مسیر است.",
  steps_h="روند همکاری",
  steps=[("گفت‌وگوی اولیه", "نیاز، محدودیت‌ها، بودجه و زمان را دقیق می‌شنوم؛ با پیام، تماس یا جلسه."),
         ("بررسی فنی و پیشنهاد", "راه‌حل، دامنه‌ی کار، زمان‌بندی و هزینه را مکتوب پیشنهاد می‌دهم."),
         ("طراحی", "طراحی مکانیکی، محاسبات و نقشه‌های ساخت؛ با بازبینی شما در هر مرحله."),
         ("ساخت و کنترل کیفیت", "پیگیری ساخت قطعات و مونتاژ، با بازرسی ابعادی و کنترل کیفیت."),
         ("تحویل و راه‌اندازی", "نصب، تست و راه‌اندازی دستگاه و تحویل مستندات.")],
  faq_h="سؤال‌های رایج",
 ),
 "en": dict(
  title="Services | Hassan Nasiri Khonsari — Machine Design, Robotics & Parts Production",
  desc="Custom machinery design and build, multi-robot mobile fleets and service robots, quality-controlled batch production of parts, automation and PLC, test rigs, and consulting on engineering careers and award applications.",
  kk="Services", h1="What we can do together",
  lead="If you have a machine or robot to design and build, need parts produced in batches with reliable quality, or just want to talk about a career path, an idea, or preparing for an award — I'd be glad to talk.",
  svc_h="Design, build and production", cons_h="Consulting and conversations",
  cons_p="Part of what I've learned over these years is useful to someone just starting out on the same path.",
  steps_h="How we work",
  steps=[("First conversation", "I listen carefully to the need, constraints, budget and timeline — by message, call or meeting."),
         ("Technical review & proposal", "A written proposal with the solution, scope, schedule and cost."),
         ("Design", "Mechanical design, calculations and manufacturing drawings, reviewed with you at each step."),
         ("Fabrication & quality control", "Follow-up of part fabrication and assembly, with dimensional inspection and QC."),
         ("Delivery & commissioning", "Installation, testing, commissioning and documentation.")],
  faq_h="Frequently asked questions",
 ),
}

SERVICES = [
 dict(id="custom-machinery", icon="gear", proof=["knee-prosthesis-test-rig", "dual-purpose-cnc"],
  fa=("طراحی و ساخت ماشین‌آلات سفارشی",
      "دستگاهی لازم دارید که در بازار نیست، یا نمونه‌ی خارجی‌اش گران و دور از دسترس است؟ از ایده و محاسبه تا نقشه‌ی ساخت طراحی می‌کنم و ساخت، مونتاژ و راه‌اندازی را تا تحویل پیگیری می‌کنم."),
  en=("Custom machinery, designed and built",
      "Need a machine that isn't on the market, or whose foreign equivalent is expensive and out of reach? I design it from concept and calculations to manufacturing drawings, and follow fabrication, assembly and commissioning through to delivery.")),
 dict(id="mobile-robot-fleets", icon="robot", proof=["postal-sorting-robots", "waiter-robots", "leamech-mobile-robots"],
  fa=("ربات‌های متحرک گروهی و خدماتی",
      "طراحی و ساخت ناوگان ربات‌های متحرک برای تفکیک و جابه‌جایی بار در انبارها و مراکز توزیع، و ربات‌های خدماتی؛ از شاسی و سیستم حرکت تا مکانیزم بار و آماده‌سازی برای تولید تیراژی. ۲۸۰ ربات سورتر پستی در سه نسل حاصل همین کار است."),
  en=("Multi-robot mobile fleets and service robots",
      "Design and build of mobile robot fleets for sorting and moving loads in warehouses and distribution centers, and of service robots — from chassis and drive system to load mechanisms and preparation for batch production. 280 postal sorting robots across three generations came out of this work.")),
 dict(id="batch-parts-production", icon="layers", proof=[],
  fa=("تولید تیراژی قطعات با کنترل کیفیت",
      "اگر قطعه‌ی صنعتی را در تیراژ می‌خواهید و دنبال جایی هستید که با ساختار مهندسی و حرفه‌ای، قطعه‌ی کنترل‌کیفی‌شده تحویل بدهد: بازبینی نقشه و تلرانس‌گذاری (GD&T)، انتخاب روش ساخت، مدیریت کارگاه‌های ماشین‌کاری و ساخت، و بازرسی ابعادی و جوش. با همین روند تاکنون بیش از ۸٬۰۰۰ قطعه‌ی صنعتی تحویل شده است."),
  en=("Batch production of quality-controlled parts",
      "If you need industrial parts in batches and want them delivered with an engineering-driven, professional process and quality control: drawing review and GD&T, choice of manufacturing method, management of machining and fabrication workshops, and dimensional and weld inspection. More than 8,000 industrial parts have been delivered this way so far.")),
 dict(id="automation-plc", icon="cpu", proof=["knee-prosthesis-test-rig", "dmd-powder-feeder"],
  fa=("اتوماسیون، PLC و راه‌اندازی",
      "معماری اتوماسیون، برنامه‌نویسی PLC (دلتا و زیمنس)، طراحی HMI و کنترل حرکت؛ برای ماشین جدید یا ارتقای دستگاهی که دارید."),
  en=("Automation, PLC and commissioning",
      "Automation architecture, PLC programming (Delta and Siemens), HMI design and motion control — for a new machine or to upgrade one you already have.")),
 dict(id="test-rigs", icon="flask", proof=["knee-prosthesis-test-rig"],
  fa=("تجهیزات آزمون آزمایشگاهی و پزشکی",
      "دستگاه‌های تست مطابق استاندارد برای آزمایشگاه‌ها، دانشگاه‌ها و تولیدکنندگان تجهیزات پزشکی؛ مثل دستگاه تست پروتز زانو مطابق ASTM F1223 و دستگاه آزمون اصطکاکی که داده‌هایش به مقاله‌ای در Scientific Reports رسید."),
  en=("Laboratory and medical test rigs",
      "Standards-based test rigs for labs, universities and medical device makers — such as the knee prosthesis tester built to ASTM F1223, and a friction test rig whose data led to a paper in Scientific Reports.")),
 dict(id="design-for-production", icon="refresh", proof=["postal-sorting-robots"],
  fa=("نمونه‌سازی و بازطراحی برای تولید",
      "تبدیل نمونه‌ی اولیه به محصولی که بشود ارزان‌تر، سریع‌تر و با کیفیت یکنواخت تولید کرد. در نسل سوم ربات سورتر پستی، وزن از حدود ۳۰ به ۱۰ کیلوگرم رسید، سرعت از ۱٫۱ به ۱٫۸ متر بر ثانیه رسید و ابعاد از ۷۰×۷۰ به ۵۵×۵۵ سانتی‌متر کوچک شد."),
  en=("Prototyping and redesign for production",
      "Turning a prototype into a product that can be made cheaper, faster and with consistent quality. In the third-generation postal sorting robot, weight dropped from about 30 to 10 kg, speed rose from 1.1 to 1.8 m/s, and the footprint shrank from 70×70 to 55×55 cm.")),
]

CONSULTING = [
 dict(id="career-consulting", icon="compass",
  fa=("مشاوره‌ی مسیر شغلی مهندسی",
      "برای دانشجوها و مهندس‌هایی که می‌خواهند از دانشگاه به کار واقعی طراحی و ساخت برسند: انتخاب حوزه، ساختن نمونه‌کار، و راه ورود به پروژه‌های صنعتی."),
  en=("Engineering career consulting",
      "For students and engineers who want to get from university to real design-and-build work: choosing a field, building a portfolio, and finding a way into industrial projects.")),
 dict(id="award-consulting", icon="trophy",
  fa=("آماده‌سازی و ارائه برای جشنواره‌ها و جوایز",
      "اگر طرحی دارید و می‌خواهید آن را برای جشنواره‌هایی مثل خوارزمی یا جایزه‌هایی مثل البرز آماده کنید: مسئله، نوآوری و نتیجه را چطور روشن و قانع‌کننده ارائه کنید. پشتوانه‌ی این مشاوره، دو مقام دوم جشنواره‌ی جوان خوارزمی و برگزیدگی در جایزه‌ی البرز است."),
  en=("Preparing for festivals and awards",
      "If you have a project you want to present at festivals such as Khwarizmi or for awards such as the Alborz Prize: how to present the problem, the innovation and the results clearly and convincingly. Backed by two 2nd places at the Khwarizmi Youth Award and an Alborz Prize selection.")),
 dict(id="tech-chat", icon="chat",
  fa=("گپ فنی و بررسی ایده",
      "ایده‌ای دارید و نمی‌دانید از کجا شروع کنید، یا فقط دوست دارید درباره‌ی یک مسئله‌ی فنی گپ بزنیم؟ پیام بدهید."),
  en=("A technical chat about your idea",
      "Have an idea and don't know where to start, or just want to talk through a technical problem? Send a message.")),
]

FAQ = {
 "fa": [
  ("حسن نصیری خونساری کیست؟",
   "حسن نصیری خونساری مهندس طراحی مکانیک و مکاترونیک و دانش‌آموخته‌ی کارشناسی ارشد طراحی کاربردی از دانشگاه صنعتی شریف است. طراحی مکانیکی ربات‌های سورتر پستی شرکت ملی پست در سه نسل و دستگاه تست تقید و پایداری پروتز زانو از کارهای شناخته‌شده‌ی اوست. برگزیده‌ی شصت‌وچهارمین جایزه‌ی البرز و دو بار صاحب مقام دوم جشنواره‌ی جوان خوارزمی است."),
  ("چه نوع پروژه‌هایی را می‌پذیرید؟",
   "طراحی و ساخت ماشین‌آلات سفارشی، ربات‌های متحرک و خدماتی، تجهیزات آزمون آزمایشگاهی و پزشکی، اتوماسیون و PLC، بازطراحی محصول برای تولید، و تولید تیراژی قطعات صنعتی با کنترل کیفیت. مشاوره‌ی مسیر شغلی و آماده‌سازی برای جشنواره‌ها هم انجام می‌دهم."),
  ("فقط طراحی می‌کنید یا ساخت را هم پیگیری می‌کنید؟",
   "هر دو. تقریباً همه‌ی پروژه‌های من از طراحی تا ساخت، مونتاژ و راه‌اندازی پیش رفته‌اند و دستگاه در پایان کار تحویل شده و کار می‌کند."),
  ("تولید تیراژی قطعات با کنترل کیفیت را چطور انجام می‌دهید؟",
   "نقشه‌ها را از نظر قابلیت ساخت و تلرانس‌گذاری (GD&T) بازبینی می‌کنم، روش ساخت مناسب را انتخاب می‌کنم، ساخت را در کارگاه‌های ماشین‌کاری و ساخت مدیریت می‌کنم و قطعه‌ها پیش از تحویل بازرسی ابعادی و، در صورت نیاز، بازرسی جوش می‌شوند. با همین روند تاکنون بیش از ۸٬۰۰۰ قطعه‌ی صنعتی تحویل شده است."),
  ("مشاوره برای جشنواره‌ها شامل چه چیزی است؟",
   "کمک می‌کنم مسئله، نوآوری، نتیجه‌ها و اثر طرحتان را روشن و مستند ارائه کنید؛ از نوشتن خلاصه‌ی طرح تا آماده شدن برای داوری و ارائه‌ی حضوری."),
  ("مشاوره حضوری است یا آنلاین؟",
   "هر دو ممکن است. من در تهران هستم و گفت‌وگو را می‌شود با تماس تلفنی، تلگرام، بله یا جلسه‌ی آنلاین هم انجام داد."),
  ("مهم‌ترین پروژه‌های شما کدام‌اند؟",
   "ربات‌های سورتر پستی (۸۰ ربات در تهران و کرمانشاه و نسل سوم در تیراژ ۲۰۰ دستگاه)، دستگاه تست تقید و پایداری پروتز زانو مطابق ASTM F1223، پنج پرینتر سه‌بعدی صنعتی، CNC صنعتی دوکاره و ناوگان ربات‌های گارسون."),
  ("چطور شروع کنیم؟",
   "از فرم پایین صفحه، تلگرام، بله یا تلفن، کوتاه بنویسید چه چیزی لازم دارید. اگر نقشه، عکس یا نمونه دارید، همان اول بفرستید تا گفت‌وگوی اول دقیق‌تر باشد."),
 ],
 "en": [
  ("Who is Hassan Nasiri Khonsari?",
   "Hassan Nasiri Khonsari is an Iranian mechanical and mechatronics design engineer with an MSc in Applied Design from Sharif University of Technology. He led the mechanical design of Iran National Post's postal sorting robots across three generations and built a knee prosthesis constraint and stability test apparatus. He is a laureate of the 64th Alborz Prize and a two-time 2nd-place winner of the Khwarizmi Youth Award."),
  ("What kind of projects do you take on?",
   "Custom machinery design and build, mobile and service robots, laboratory and medical test rigs, automation and PLC, redesign for production, and quality-controlled batch production of industrial parts. I also offer career consulting and help with preparing award applications."),
  ("Do you only design, or also follow fabrication?",
   "Both. Almost all of my projects went from design through fabrication, assembly and commissioning, and ended with a delivered, working machine."),
  ("How do you handle batch production with quality control?",
   "I review drawings for manufacturability and tolerancing (GD&T), choose the manufacturing method, manage machining and fabrication workshops, and parts get dimensional and, where needed, weld inspection before delivery. More than 8,000 industrial parts have been delivered this way."),
  ("What does award consulting include?",
   "Helping you present the problem, the innovation, the results and the impact of your project clearly and with evidence — from writing the summary to preparing for judging and in-person presentation."),
  ("Is consulting in person or online?",
   "Both are possible. I'm based in Tehran, and conversations can also happen by phone, Telegram, Bale or an online meeting."),
  ("What are your key projects?",
   "Postal sorting robots (80 robots in Tehran and Kermanshah, third generation produced as a 200-unit series), a knee prosthesis constraint and stability test apparatus per ASTM F1223, five industrial 3D printers, a dual-purpose industrial CNC and a fleet of waiter robots."),
  ("How do we start?",
   "Use the form at the bottom of the page, Telegram, Bale or phone and briefly describe what you need. If you have drawings, photos or samples, send them up front so the first conversation is more precise."),
 ],
}

# ---------------------------------------------------------------- افتخارات (top=True روی صفحه‌ی اصلی هم می‌آید)
HONORS = [
 dict(icon="medal", top=True, fa=("برگزیده‌ی شصت‌وچهارمین جایزه‌ی البرز", "یکی از ۱۲ برگزیده‌ی بخش فناوران و مخترعان، برای دستگاه تست تقید و پایداری پروتز زانو؛ همراه با تقدیر دانشگاه صنعتی شریف و اهدای مدال نقره — ۱۴۰۵."),
      en=("Laureate, 64th Alborz Prize", "One of 12 laureates in the Technologists & Inventors category, for the knee prosthesis constraint and stability test apparatus; also honored by Sharif University of Technology with its silver medal — 2026.")),
 dict(icon="trophy", top=True, fa=("مقام دوم بیست‌وششمین جشنواره‌ی جوان خوارزمی", "برای طراحی مکانیکی ربات‌های سورتر پستی — ۱۴۰۳."),
      en=("2nd Place, 26th Khwarizmi Youth Award", "For the mechanical design of postal sorting robots — 2025.")),
 dict(icon="trophy", top=True, fa=("مقام دوم بیست‌وچهارمین جشنواره‌ی جوان خوارزمی", "برای دستگاه تست تقید و پایداری پروتز زانو، همراه با گواهی یونسکو و تقدیر رئیس‌جمهور — ۱۴۰۱."),
      en=("2nd Place, 24th Khwarizmi Youth Award", "For the knee prosthesis constraint and stability test apparatus, with a UNESCO certificate and recognition by the President — 2023.")),
 dict(icon="star", fa=("برترین پروژه‌ی فناورانه‌ی شریف", "عنوان برترین پایان‌نامه‌ی فناورانه‌ی دانشکده‌ی مهندسی مکانیک — ۱۴۰۰."),
      en=("Top Technological Project, Sharif University", "Top technological thesis, Department of Mechanical Engineering — 2022.")),
 dict(icon="star", fa=("استارتاپ برتر پارک علم و فناوری شریف", "برای تیم ربات‌های هوشمند پستی (ماشین‌های هوشمند تنسور) — ۱۴۰۳."),
      en=("Top Startup, Sharif Science and Technology Park", "For the smart postal robots team (Tensor Intelligent Machines) — 2024.")),
 dict(icon="trophy", fa=("طرح برتر چهارمین جشنواره‌ی طراحی صنعتی ایران", "برای ربات‌های هوشمند پستی (ماشین‌های هوشمند تنسور) — ۱۴۰۳."),
      en=("Top Design, 4th Iran Industrial Design Festival", "For the smart postal robots (Tensor Intelligent Machines) — 2024.")),
 dict(icon="target", fa=("رتبه‌ی ۱۶ کنکور کارشناسی ارشد مکانیک", "از میان بیش از ۱۰٬۰۰۰ شرکت‌کننده؛ و رتبه‌ی ۱۱ مرحله‌ی نهایی المپیاد علمی دانشجویی مکانیک — ۱۳۹۷."),
      en=("Rank 16, National MSc Entrance Exam (Mechanical Eng.)", "Among more than 10,000 participants; also ranked 11th at the final stage of the National Student Olympiad in Mechanical Engineering — 2019.")),
 dict(icon="flask", fa=("دستاورد ده‌درصد برتر KANS", "در حوزه‌های «الکترونیک و رباتیک» و «سلامت و فناوری پزشکی»."),
      en=("KANS Top 10% Achievement", "In the “Electronics & Robotics” and “Health & Medical Technology” categories.")),
 dict(icon="book", fa=("تألیف کتاب", "«المپیادهای فیزیک در ایران» — نشر خوشخوان، ۱۳۹۷."),
      en=("Book", "“Physics Olympiads in Iran” — Khoshkhan Publications, 2018.")),
]

# ---------------------------------------------------------------- درباره و سوابق
ABOUT = {
 "fa": dict(
  title="درباره و سوابق | حسن نصیری خونساری — مهندس مکانیک و مکاترونیک",
  desc="سوابق کاری، تحصیلات، افتخارات، مقاله و مهارت‌های حسن نصیری خونساری؛ مهندس طراحی مکانیک و مکاترونیک، دانش‌آموخته‌ی کارشناسی ارشد دانشگاه صنعتی شریف.",
  kk="درباره و سوابق", h1="درباره‌ی من",
  paras=[
   "من حسن نصیری خونساری هستم؛ مهندس طراحی مکانیک و مکاترونیک. کارم طراحی مکانیکی ماشین‌ها و ربات‌های صنعتی و پیگیری ساخت، مونتاژ و راه‌اندازی آن‌هاست.",
   "کارشناسی ارشد مهندسی مکانیک (طراحی کاربردی) را در دانشگاه صنعتی شریف زیر نظر دکتر محمد دورعلی و کارشناسی را در دانشگاه علم و صنعت ایران گذراندم. دو بار مقام دوم جشنواره‌ی جوان خوارزمی را کسب کرده‌ام و برگزیده‌ی جایزه‌ی البرز در بخش فناوران و مخترعان شده‌ام.",
   "از ربات‌های سورتر پستی که نسل‌های اول و دومش در تهران و کرمانشاه به کار افتاد و نسل سومش در تیراژ ۲۰۰ دستگاه به تولید رسید، تا دستگاه تست پروتز زانو، تغذیه‌کننده‌ی پودر برای لایه‌نشانی مستقیم فلز، پنج پرینتر سه‌بعدی صنعتی، ناوگان هفت‌تایی ربات گارسون و ربات‌های متحرک همه‌جهته.",
   "این روزها در کارون، طراحی قطعه و مجموعه، بازرسی ابعادی و جوش، و مدیریت کارگاه‌های ماشین‌کاری و ساخت بیرونی را بر عهده دارم؛ تا امروز بیش از ۸٬۰۰۰ قطعه‌ی صنعتی تحویل شده است.",
  ],
  facts=[("موقعیت", "تهران، ایران"), ("کار فعلی", "مهندس ارشد مکانیک — کارون"), ("تحصیلات", "ارشد طراحی کاربردی — شریف"),
         ("بنیاد ملی نخبگان", "۳۰۰ امتیاز سینا"), ("همکاری", "پروژه‌ی طراحی و ساخت، تولید تیراژی و مشاوره")],
  hon_h="افتخارات و رتبه‌ها", exp_h="تجربه‌ی حرفه‌ای", edu_h="تحصیلات", pub_h="مقاله‌ی علمی", skills_h="مهارت‌ها و نرم‌افزارها",
 ),
 "en": dict(
  title="About | Hassan Nasiri Khonsari — Mechanical & Mechatronics Engineer",
  desc="Experience, education, awards, publication and skills of Hassan Nasiri Khonsari, mechanical and mechatronics design engineer and MSc graduate of Sharif University of Technology.",
  kk="About", h1="About me",
  paras=[
   "I'm Hassan Nasiri Khonsari, a mechanical and mechatronics design engineer. My work is the mechanical design of industrial machines and robots, followed through fabrication, assembly and commissioning.",
   "I hold an MSc in Mechanical Engineering (Applied Design) from Sharif University of Technology, supervised by Prof. Mohammad Durali, and a BSc from Iran University of Science and Technology. I have twice won 2nd place at the Khwarizmi Youth Award and was named a laureate of the Alborz Prize in the Technologists & Inventors category.",
   "My work ranges from postal sorting robots — the first two generations deployed in Tehran and Kermanshah, the third produced as a 200-unit series — to a knee prosthesis test apparatus, a powder feeder for direct metal deposition, five industrial 3D printers, a fleet of seven waiter robots and omnidirectional mobile robots.",
   "At Karun I currently handle part and assembly design, dimensional and weld inspection, and management of external machining and fabrication workshops; over 8,000 industrial parts have been delivered to date.",
  ],
  facts=[("Location", "Tehran, Iran"), ("Current role", "Senior Mechanical Engineer — Karun"), ("Education", "MSc Applied Design — Sharif"),
         ("National Elites Foundation", "300 Sina points"), ("Open to", "Design-and-build projects, batch production and consulting")],
  hon_h="Honors & awards", exp_h="Professional experience", edu_h="Education", pub_h="Publication", skills_h="Skills & software",
 ),
}

EXPERIENCE = [
 dict(fa=("۱۴۰۴ تا اکنون", "مهندس ارشد مکانیک", "کارون (Karun HiTech Solutions) — تهران",
          "طراحی قطعه و مجموعه، بازرسی ابعادی و جوش، و مدیریت کارگاه‌های ماشین‌کاری و ساخت بیرونی؛ بیش از ۸٬۰۰۰ قطعه‌ی صنعتی تحویل‌شده."),
      en=("Apr 2025 – Present", "Senior Mechanical Engineer", "Karun HiTech Solutions — Tehran",
          "Part and assembly design, dimensional and weld inspection, and management of external machining and fabrication workshops; over 8,000 industrial parts delivered.")),
 dict(fa=("۱۴۰۲", "مدرس", "دانشگاه تهران، پردیس بین‌المللی کیش", "تدریس دروس «روش‌های تولید» و «فیزیک ۲» در نیم‌سال دوم ۱۴۰۲-۱۴۰۳."),
      en=("Feb – Jun 2024", "Lecturer", "University of Tehran, Kish International Campus", "Taught Manufacturing Processes and Physics II for one semester.")),
 dict(project="leamech-mobile-robots",
      fa=("۱۴۰۰ تا ۱۴۰۳", "مدیر طراحی محصول (پاره‌وقت)", "لیمک (LeaMech) — تیم فناوری بین‌المللی با اعضایی در آمریکا، ایران و کشورهای دیگر",
          "طراحی، ساخت و راه‌اندازی مکانیک ربات‌های متحرک کاچ و کارناک (همه‌جهته با چرخ مکانوم) و سامانه‌ی شارژ خودکار مفهومی؛ مشارکت در پروژه‌های موقعیت‌یابی خودرو و در کالیبراسیون دوربین و تبدیل دستگاه‌های مختصات برای پروژه‌ی دوقلوی دیجیتال."),
      en=("2021 – 2024", "Product Design Manager (part-time)", "LeaMech — an international technology team with members in the USA, Iran and other countries",
          "Designed, built and commissioned the mechanics of the Kach and Karnak mobile robots (omnidirectional, mecanum wheels) and a concept auto-charging system; contributed to vehicle-positioning projects and to camera calibration and coordinate-frame transformations for a digital twin project.")),
 dict(project="postal-sorting-robots",
      fa=("۱۳۹۹ تا ۱۴۰۴", "مدیر واحد مهندسی مکانیک", "ماشین‌های هوشمند تنسور (Tensor) — تهران",
          "طراحی و توسعه‌ی مکانیکی ربات‌های صنعتی؛ مدیریت ساخت ۵۰ ربات سورتر برای مرکز توزیع مرسولات چهارراه لشکر و ۳۰ ربات برای مرکز توزیع کرمانشاه، هماهنگی کارگاه‌ها و سرپرستی تیم مونتاژ و یکپارچه‌سازی."),
      en=("Jan 2021 – May 2025", "Head of Mechanical Engineering Department", "Tensor Intelligent Machines — Tehran",
          "Mechanical design and development of industrial robots; managed production of 50 sorter robots for the Chaharrah-e Lashkar parcel distribution center and 30 for the Kermanshah center, coordinating workshops and supervising the assembly and integration team.")),
 dict(fa=("۱۳۹۸", "کارآموز پروژه — اتوماسیون و ماشین‌آلات تئاتر شهر", "شرکت طراحی و اتوماسیون سیستم دورعلی (DSDA)", ""),
      en=("Oct 2019 – Mar 2020", "Project Intern — City Theater Automation and Machinery", "DSDA (Durali System Design & Automation Co.)", "")),
 dict(fa=("۱۳۹۸ و ۱۳۹۹", "دستیار آموزشی استاتیک", "دانشگاه صنعتی شریف", ""),
      en=("2020 – 2021", "Teaching Assistant — Statics", "Sharif University of Technology", "")),
 dict(fa=("۱۳۹۵ و ۱۳۹۶", "دستیار آموزشی فیزیک ۱ و دینامیک", "دانشگاه علم و صنعت ایران", ""),
      en=("2016 – 2018", "Teaching Assistant — Physics I and Dynamics", "Iran University of Science and Technology", "")),
 dict(fa=("۱۳۹۵ و ۱۳۹۷", "کارآموزی تابستانی", "سیگما و صدرا", "سیگما: نقشه‌کشی قطعات با CATIA. صدرا: کنترل موقعیت یک میز سه‌درجه‌آزادی."),
      en=("Summers 2016 and 2018", "Summer Internships", "Sigma and Sadra", "Sigma: part drafting in CATIA. Sadra: position control of a 3-DOF table.")),
]

EDUCATION = [
 dict(fa=("۱۳۹۸ تا ۱۴۰۱", "کارشناسی ارشد مهندسی مکانیک — طراحی کاربردی", "دانشگاه صنعتی شریف",
          ["استاد راهنما: دکتر محمد دورعلی", "پایان‌نامه: طراحی، ساخت و کالیبراسیون دستگاه تست تقید و پایداری پروتز زانو در شش درجه‌ی آزادی — دفاع با نمره‌ی عالی؛ برترین پایان‌نامه‌ی فناورانه‌ی دانشکده", "معدل: ۱۷٫۱۵ از ۲۰"]),
      en=("2019 – 2022", "MSc, Mechanical Engineering — Applied Design", "Sharif University of Technology",
          ["Supervisor: Prof. Mohammad Durali", "Thesis: design, fabrication and calibration of a 6-DOF knee prosthesis constraint and stability test apparatus — graded Excellent; the department's top technological thesis", "GPA: 17.15 / 20"])),
 dict(fa=("۱۳۹۴ تا ۱۳۹۸", "کارشناسی مهندسی مکانیک", "دانشگاه علم و صنعت ایران",
          ["استاد راهنما: دکتر سید علی نیکنام", "پایان‌نامه: طراحی تفصیلی دستگاه تغذیه‌ی پودر برای فرآیند لایه‌نشانی مستقیم فلز (DMD)", "معدل: ۱۷٫۳۰ از ۲۰"]),
      en=("2015 – 2019", "BSc, Mechanical Engineering", "Iran University of Science and Technology",
          ["Supervisor: Dr. Seyed Ali Niknam", "Thesis: detail design of a powder feeder for direct metal deposition (DMD)", "GPA: 17.30 / 20"])),
]
EDU_NOTE = dict(
 fa="رتبه‌ی ۱۶ کنکور کارشناسی ارشد مهندسی مکانیک در میان بیش از ۱۰٬۰۰۰ شرکت‌کننده و رتبه‌ی ۷۹۵ کنکور سراسری در میان ۱۸۲٬۰۰۰ نفر؛ ورود به کارشناسی ارشد به‌عنوان استعداد درخشان.",
 en="Rank 16 among more than 10,000 in the national MSc entrance exam (Mechanical Engineering) and rank 795 among 182,000 in the national university entrance exam; admitted to the MSc through the exceptional-talent track.")

PUB = dict(
 title="Frictional behavior between bone and additively manufactured Ti6Al4V implants is affected by bone density and surface texture under varying loads",
 authors="Ali Abedi, Farzam Farahmand, Mohammadjavad Salmanimehrjardi &amp; <b>Hasan Nasiri Khonsari</b>",
 authors_plain=["Ali Abedi", "Farzam Farahmand", "Mohammadjavad Salmanimehrjardi", "Hasan Nasiri Khonsari"],
 journal="Scientific Reports", year="2025",
 fa=dict(badge="📄 Scientific Reports — <b>Nature</b> · مجله‌ی Q1",
  abstract="بررسی رفتار اصطکاکی میان استخوان و ایمپلنت‌های تیتانیومی (Ti6Al4V) ساخته‌شده با روش ذوب لیزری انتخابی (SLM). در این پژوهش، ضریب اصطکاک برای ترکیب‌های مختلفِ چگالی استخوان، بافت سطح ایمپلنت و میزان بار اندازه‌گیری شد — نتایجی که به طراحی ایمپلنت‌های ارتوپدی سفارشی و متناسب با ویژگی‌های استخوانی هر بیمار کمک می‌کند.",
  role="نقش من در این پژوهش: توسعه و ساخت دستگاه آزمون اصطکاک (تجهیز آزمایشگاهی).",
  meta=["سال انتشار: <b>۲۰۲۵</b>", "دانشگاه صنعتی شریف", "DOI: 10.1038/s41598-025-25586-0"], link="مشاهده‌ی مقاله ↗"),
 en=dict(badge="📄 Scientific Reports — <b>Nature</b> · Q1 journal",
  abstract="A study of the frictional behavior between bone and titanium (Ti6Al4V) implants made by selective laser melting (SLM). Friction coefficients were measured across combinations of bone density, implant surface texture and load — results that support the design of custom orthopedic implants matched to each patient’s bone properties.",
  role="My role: developing and building the friction test apparatus.",
  meta=["Published: <b>2025</b>", "Sharif University of Technology", "DOI: 10.1038/s41598-025-25586-0"], link="View article ↗"),
)

SKILLS = [
 dict(fa=("طراحی و تحلیل", ["SolidWorks", "CATIA", "ANSYS", "طراحی مکانیزم", "تحلیل اجزای محدود (FEA)"]),
      en=("Design & Analysis", ["SolidWorks", "CATIA", "ANSYS", "Mechanism design", "Finite element analysis (FEA)"])),
 dict(fa=("ساخت و تولید", ["ماشین‌کاری CNC", "SolidCAM", "Mastercam", "GD&T", "سازه‌های جوشی", "بازرسی ابعادی و کنترل کیفیت"]),
      en=("Manufacturing", ["CNC machining", "SolidCAM", "Mastercam", "GD&T", "Welded structures", "Dimensional inspection & QC"])),
 dict(fa=("اتوماسیون و کنترل", ["PLC دلتا", "Siemens TIA Portal", "HMI", "LabVIEW", "کنترل حرکت", "ROS"]),
      en=("Automation & Control", ["Delta PLC", "Siemens TIA Portal", "HMI", "LabVIEW", "Motion control", "ROS"])),
 dict(fa=("الکترونیک و نمونه‌سازی", ["ARM / STM32", "AVR / Arduino", "Raspberry Pi", "Altium", "MATLAB", "پرینت سه‌بعدی"]),
      en=("Electronics & Prototyping", ["ARM / STM32", "AVR / Arduino", "Raspberry Pi", "Altium", "MATLAB", "3D printing"])),
]

# ---------------------------------------------------------------- پروژه‌ها
# هر پروژه یک صفحه دارد: /projects/<slug>.html و /en/projects/<slug>.html
# imgs: عکس‌ها (src به .webp ختم شود و نسخه‌ی کوچک -t.webp هم کنارش باشد). اولین عکس، کاور پروژه است.
# videos: کد ویدیوهای آپارات (بخش آخر aparat.com/v/xxxx) با عنوان؛ مثل: dict(aparat="xxxx", fa="…", en="…")
PROJECTS = [
 dict(slug="postal-sorting-robots", year=("۱۳۹۹ تا ۱۴۰۴", "2021 – 2025"), date="2021",
  imgs=[("p-sorter-1.webp", 1344, 896, "نسل اول", "Generation 1"), ("p-sorter-2.webp", 1288, 924, "نسل دوم", "Generation 2"), ("p-sorter-3.webp", 1288, 952, "نسل سوم", "Generation 3")],
  videos=[],
  fa=dict(title="ربات‌های سورتر پستی", short="نخستین ربات سورتر پستی از این نوع در ایران؛ ۸۰ ربات در تهران و کرمانشاه و نسل سوم در تیراژ ۲۰۰ دستگاه.",
   tags=["طراحی مکانیک", "ربات متحرک گروهی", "تولید انبوه"],
   desc=["نخستین ربات سورتر پستی از این نوع در ایران، برای تفکیک خودکار مرسولات در شرکت ملی پست. نسل‌های اول و دوم را طراحی و ساختیم: ۵۰ دستگاه برای مرکز توزیع مرسولات چهارراه لشکر تهران و ۳۰ دستگاه برای مرکز توزیع کرمانشاه، در مجموع ۸۰ ربات. طراحی نسل سوم هم کار من است که در تیراژ ۲۰۰ دستگاه به تولید رسید.",
         "در نسل سوم، ربات سبک‌تر، سریع‌تر و جمع‌وجورتر شد و ساختار دوطبقه پیدا کرد؛ تغییراتی که هم کارایی مرکز توزیع را بالا می‌برد و هم تولید تیراژی را ساده‌تر و ارزان‌تر می‌کند."],
   role="طراحی مکانیزم تخلیه‌ی بار، سامانه‌ی توزین، استراکچر و سیستم حرکت ربات‌ها و طراحی سامانه‌ی شارژ خودکار؛ به‌عنوان مدیر واحد مهندسی مکانیک ماشین‌های هوشمند تنسور، هماهنگی کارگاه‌ها و سرپرستی تیم مونتاژ و یکپارچه‌سازی.",
   facts=[("تعداد", "۸۰ ربات نسل اول و دوم + ۲۰۰ ربات نسل سوم"), ("محل کار", "مراکز توزیع مرسولات تهران (چهارراه لشکر) و کرمانشاه"),
          ("سرعت نسل سوم", "۱٫۸ متر بر ثانیه (نسل قبل: ۱٫۱)"), ("وزن نسل سوم", "حدود ۱۰ کیلوگرم (نسل قبل: حدود ۳۰)"), ("ابعاد نسل سوم", "۵۵×۵۵ سانتی‌متر (نسل قبل: ۷۰×۷۰)")],
   awards=["مقام دوم بیست‌وششمین جشنواره‌ی جوان خوارزمی", "استارتاپ برتر پارک علم و فناوری شریف", "طرح برتر چهارمین جشنواره‌ی طراحی صنعتی ایران"]),
  en=dict(title="Postal Sorting Robots", short="Iran's first postal sorting robot of its type: 80 robots in Tehran and Kermanshah, and a 200-unit third generation.",
   tags=["Mechanical design", "Multi-robot fleets", "Mass production"],
   desc=["Iran's first postal sorting robot of its type, built for automated parcel sorting at Iran National Post. We designed and built the first two generations: 50 units for the Chaharrah-e Lashkar distribution center in Tehran and 30 for the Kermanshah center, 80 robots in total. The third-generation design is also mine and went into production as a 200-unit series.",
         "The third generation became lighter, faster and more compact, with a two-level structure — changes that raise the distribution center's throughput and make batch production simpler and cheaper."],
   role="Load-discharge mechanism, weighing system, structure and drive system, and the automatic charging system; as head of the mechanical engineering department at Tensor Intelligent Machines, I also coordinated workshops and supervised the assembly and integration team.",
   facts=[("Units", "80 first/second-generation + 200 third-generation robots"), ("In service at", "Parcel distribution centers in Tehran (Chaharrah-e Lashkar) and Kermanshah"),
          ("Gen 3 speed", "1.8 m/s (previously 1.1)"), ("Gen 3 weight", "about 10 kg (previously about 30)"), ("Gen 3 footprint", "55×55 cm (previously 70×70)")],
   awards=["2nd Place, 26th Khwarizmi Youth Award", "Top Startup, Sharif Science and Technology Park", "Top Design, 4th Iran Industrial Design Festival"])),

 dict(slug="knee-prosthesis-test-rig", year=("۱۴۰۰", "2021"), date="2021",
  imgs=[("p-knee.webp", 952, 1288, "", "")], videos=[],
  fa=dict(title="دستگاه تست تقید و پایداری پروتز زانو", short="آزمون پروتز کامل زانو در شش درجه‌ی آزادی مطابق ASTM F1223؛ نخستین نمونه در ایران.",
   tags=["تجهیزات پزشکی", "اتوماسیون", "ASTM F1223"],
   desc=["دستگاهی برای آزمون تقید و پایداری پروتز کامل زانو در شش درجه‌ی آزادی، مطابق استاندارد ASTM F1223؛ پایان‌نامه‌ی کارشناسی ارشد من در دانشگاه صنعتی شریف، زیر نظر دکتر محمد دورعلی و با مشاوره‌ی دکتر فرهمند. دستگاه تحویل شده و برای کارهای پژوهشی استفاده می‌شود.",
         "پیش از این، نمونه‌ی مشابهی در ایران وجود نداشت و معادل‌های تجاری آن را شرکت‌هایی مثل EndoLab آلمان و AMTI آمریکا می‌سازند. بعدها همین دستگاه را برای مطالعه‌ی اصطکاک میان استخوان و ایمپلنت بازپیکربندی کردم که حاصلش مقاله‌ای در Scientific Reports شد."],
   role="طراحی مکانیکی، معماری اتوماسیون، برنامه‌نویسی PLC و توسعه‌ی HMI؛ و بعدها بازپیکربندی دستگاه برای آزمون اصطکاک.",
   facts=[("استاندارد", "ASTM F1223"), ("درجه‌ی آزادی", "شش"), ("معادل‌های تجاری", "EndoLab (آلمان) و AMTI (آمریکا)"), ("حاصل پژوهشی", "مقاله در Scientific Reports (۲۰۲۵)")],
   awards=["برگزیده‌ی شصت‌وچهارمین جایزه‌ی البرز", "مقام دوم بیست‌وچهارمین جشنواره‌ی جوان خوارزمی", "برترین پایان‌نامه‌ی فناورانه‌ی دانشکده‌ی مهندسی مکانیک شریف"]),
  en=dict(title="Knee Prosthesis Constraint and Stability Test Apparatus", short="Six-DOF testing of total knee replacements per ASTM F1223 — the first apparatus of its kind in Iran.",
   tags=["Medical equipment", "Automation", "ASTM F1223"],
   desc=["A six-degree-of-freedom apparatus for constraint and stability testing of total knee replacements per ASTM F1223 — my MSc thesis at Sharif University of Technology, supervised by Prof. Mohammad Durali with Prof. Farahmand as consulting advisor. The apparatus has been delivered and is used for research.",
         "No comparable apparatus existed in Iran; commercial equivalents are built by companies such as EndoLab (Germany) and AMTI (USA). I later reconfigured the same rig for a bone–implant friction study, which led to a paper in Scientific Reports."],
   role="Mechanical design, automation architecture, PLC programming and HMI development; later, reconfiguring the rig for friction testing.",
   facts=[("Standard", "ASTM F1223"), ("Degrees of freedom", "Six"), ("Commercial equivalents", "EndoLab (Germany), AMTI (USA)"), ("Research output", "Paper in Scientific Reports (2025)")],
   awards=["Laureate, 64th Alborz Prize", "2nd Place, 24th Khwarizmi Youth Award", "Top technological thesis, Sharif Mechanical Engineering"])),

 dict(slug="industrial-3d-printers", year=("۱۳۹۹ تا ۱۴۰۲", "2020 – 2023"), date="2020",
  imgs=[("p-printer-1.webp", 1288, 952, "نسل اول — ۳۰×۳۰×۴۰ سانتی‌متر", "Generation 1 — 30×30×40 cm"), ("p-printer-2.webp", 756, 1008, "نسل دوم — ۳۰×۳۰×۴۰ سانتی‌متر", "Generation 2 — 30×30×40 cm"), ("p-printer-3.webp", 980, 1232, "نسل سوم — ۵۰×۵۰×۴۰ سانتی‌متر", "Generation 3 — 50×50×40 cm")],
  videos=[],
  fa=dict(title="پرینترهای سه‌بعدی FDM صنعتی", short="پنج دستگاه، از ۲۰۰×۲۰۰×۱۵۰ تا ۵۰۰×۵۰۰×۴۰۰ میلی‌متر با بال‌اسکرو و ریل خطی صنعتی.",
   tags=["پرینت سه‌بعدی", "طراحی مکانیزم", "الکترونیک و فرم‌ور"],
   desc=["پنج دستگاه که از صفر طراحی و ساختم و نسل‌به‌نسل بازمهندسی شدند: از یک دستگاه ۲۰۰×۲۰۰×۱۵۰ میلی‌متری تا ماشینی صنعتی با حجم کاری ۵۰۰×۵۰۰×۴۰۰ میلی‌متر که روی همه‌ی محورها بال‌اسکرو و ریل خطی صنعتی دارد."],
   role="سازه، مکانیزم، انتخاب موتورها، الکترونیک، فرم‌ور و بهینه‌سازی اسلایسر؛ همه را مستقل انجام دادم.",
   facts=[("تعداد", "پنج دستگاه در سه نسل"), ("بزرگ‌ترین حجم کاری", "۵۰۰×۵۰۰×۴۰۰ میلی‌متر"), ("محورها", "بال‌اسکرو و ریل خطی صنعتی")], awards=[]),
  en=dict(title="Industrial FDM 3D Printers", short="Five machines, from 200×200×150 mm up to 500×500×400 mm with ball screws and industrial linear rails.",
   tags=["3D printing", "Mechanism design", "Electronics & firmware"],
   desc=["Five machines designed and built from scratch, then re-engineered across generations: from a 200×200×150 mm unit to an industrial machine with a 500×500×400 mm build volume, running ball screws and industrial linear rails on every axis."],
   role="Frame, mechanism, motor selection, electronics, firmware and slicer optimization — all done independently.",
   facts=[("Units", "Five machines in three generations"), ("Largest build volume", "500×500×400 mm"), ("Axes", "Ball screws and industrial linear rails")], awards=[])),

 dict(slug="dual-purpose-cnc", year=("۱۴۰۲", "2023"), date="2023",
  imgs=[("p-cnc.webp", 1372, 896, "دستگاه", "Machine"), ("p-cnc-panel.webp", 1148, 1064, "تابلو برق", "Control cabinet"), ("p-cnc-panel-open.webp", 952, 1288, "داخل تابلو برق", "Inside the control cabinet")],
  videos=[],
  fa=dict(title="CNC صنعتی دوکاره", short="CNC برای چوب و فلزات سبک که با تعویض هد به پرینتر سه‌بعدی بزرگ تبدیل می‌شود.",
   tags=["CNC", "CAM", "طراحی سازه"],
   desc=["یک دستگاه CNC صنعتی برای برش چوب و فلزات سبک با میز کاری بزرگ (حدود ۱۰۰×۱۰۰ سانتی‌متر) که به‌صورت ماژولار طراحی شده است؛ یعنی با تعویض ساده‌ی هد، می‌تواند به یک پرینتر سه‌بعدی قدرتمند تبدیل شود.",
         "هدف، ساخت یک ماشین چندکاره و مقرون‌به‌صرفه برای کارگاه‌های کوچک و متوسط بود."],
   role="طراحی سازه، انتخاب درایوها و موتورها و راه‌اندازی سیستم کنترل با G-Code.",
   facts=[("ابعاد کاری", "حدود ۱۰۰×۱۰۰×۳۰ سانتی‌متر"), ("مواد", "چوب و فلزات سبک"), ("ویژگی", "هد قابل‌تعویض: فرز CNC یا پرینتر سه‌بعدی")], awards=[]),
  en=dict(title="Dual-Purpose Industrial CNC", short="A CNC for wood and light metals that becomes a large 3D printer with a head change.",
   tags=["CNC", "CAM", "Structural design"],
   desc=["An industrial CNC machine for cutting wood and light metals, with a large work table (about 100×100 cm) and a modular design: with a simple head change it becomes a high-capacity 3D printer.",
         "The goal was an affordable multi-purpose machine for small and medium workshops."],
   role="Structural design, drive and motor selection, and commissioning the G-code control system.",
   facts=[("Working envelope", "about 100×100×30 cm"), ("Materials", "Wood and light metals"), ("Feature", "Interchangeable head: CNC router or 3D printer")], awards=[])),

 dict(slug="waiter-robots", year=("۱۴۰۰", "2021"), date="2021",
  imgs=[("p-waiter.webp", 896, 1344, "", "")], videos=[],
  fa=dict(title="ربات‌های گارسون", short="ناوگانی هفت‌تایی از ربات‌های گارسون؛ نخستین ربات گارسون از این نوع در ایران.",
   tags=["رباتیک خدماتی", "ربات متحرک گروهی", "طراحی بدنه"],
   desc=["نخستین ربات گارسون از این نوع در ایران؛ طراحی، ساخت و مونتاژ مکانیکی ناوگانی هفت‌تایی از ربات‌های گارسون برای حمل و سرو غذا در رستوران.",
         "تمرکز اصلی روی شاسی و سیستم حرکت بود تا ربات‌ها روی کف ناهموار رستوران هم پایدار و قابل اعتماد کار کنند؛ بدنه هم با در نظر گرفتن ایمنی و ظاهر مناسب محیط پذیرایی طراحی شد."],
   role="طراحی، ساخت و مونتاژ مکانیکی؛ شاسی، سیستم حرکت و بدنه.",
   facts=[("تعداد", "ناوگان هفت‌تایی"), ("کاربرد", "حمل و سرو غذا در رستوران")], awards=[]),
  en=dict(title="Waiter Robots", short="A fleet of seven waiter robots — Iran's first waiter robot of its type.",
   tags=["Service robotics", "Multi-robot fleets", "Body design"],
   desc=["Iran's first waiter robot of its type: mechanical design, fabrication and assembly of a fleet of seven waiter robots for carrying and serving food in restaurants.",
         "The main focus was the chassis and drive system, so the robots run reliably on uneven restaurant floors; the body was designed with safety and a suitable look for a dining environment in mind."],
   role="Mechanical design, fabrication and assembly: chassis, drive system and body.",
   facts=[("Units", "A fleet of seven"), ("Use", "Carrying and serving food in restaurants")], awards=[])),

 # عکس‌ها و ویدیوهای لیمک: فایل‌ها را با نام‌هایی مثل p-leamech-1.webp (و p-leamech-1-t.webp) کنار بقیه بگذار و در imgs اضافه کن؛
 # ویدیوهای آپارات را در videos اضافه کن: dict(aparat="xxxx", fa="ربات کارناک روی مسیر دایره", en="Karnak on a circular path")
 dict(slug="leamech-mobile-robots", year=("۱۴۰۰ تا ۱۴۰۳", "2021 – 2024"), date="2021",
  imgs=[], videos=[],
  fa=dict(title="ربات‌های متحرک کاچ و کارناک (لیمک)", short="بستری برای ربات‌های خدماتی متحرک: ربات کاچ با ROS و ربات همه‌جهته‌ی کارناک با چرخ مکانوم.",
   tags=["ربات متحرک", "چرخ مکانوم", "ROS", "شارژ خودکار"],
   desc=["در لیمک (LeaMech)، تیمی بین‌المللی با اعضایی در آمریکا، ایران و کشورهای دیگر که برای راه‌اندازی یک استارتاپ و گرفتن بودجه از بنیاد ملی علوم آمریکا (NSF) تلاش می‌کرد و قرار بود نخستین شعبه‌اش در ترکیه راه بیفتد، بستری برای ربات‌های خدماتی متحرک ساختیم؛ ربات‌هایی که بار را حمل می‌کنند و می‌توانند در زمین‌های ناهموار دنبال یک نفر بروند: برای کمپینگ، رساندن تجهیزات کمک‌رسانی به جاهایی مثل جنگل که خودرو به آن‌ها دسترسی ندارد، یا جابه‌جایی اشیا در صنعت. هدف اول، بالا آوردن بستر بود و مکانیک در حد MVP نگه داشته شد.",
         "ربات اول، **کاچ**، یک ربات متحرک چهارچرخ با موتورهای استپر بود که کنترل موقعیتش پیاده شد و مسیرهای مشخص را با اجرای دستور طی می‌کرد؛ نرم‌افزارش بر پایه‌ی ROS بود. ربات دوم، **کارناک**، یک ربات همه‌جهته با چرخ‌های مکانوم و موتورهای استپر بود که می‌توانست در هر جهتی حرکت کند. مغز آن Raspberry Pi و Arduino Mega بود و انواع مسیرها، مثل دایره و مربع، از طریق اپلیکیشن موبایلی که برایش نوشتم تست می‌شد. بدنه‌ی کارناک محکم و صنعتی بود و چرخ‌های مکانوم را، چون در ایران پیدا نمی‌شد، از چین وارد کردیم. یک سامانه‌ی شارژ خودکار ساده و مفهومی هم برایش طراحی کردم و ساختم که تست اولیه را با موفقیت گذراند.",
         "در لیمک روی پروژه‌های دیگری هم کار کردم: **کنوم** (به ترکی یعنی «موقعیت»)، سامانه‌ی موقعیت‌یابی خودروهای پارک‌شده برای نمایندگی‌های فروش خودرو در آمریکا که پیدا کردن و تحویل خودرو را سریع‌تر می‌کرد؛ ادامه‌ی آن، **کوش**، که قرار بود موقعیت خودروها را با پهپاد ردگیری کند؛ و پروژه‌ی دوقلوی دیجیتال **آکتار و نما** برای محیط‌های صنعتی و فیزیکی، که در آن پیاده‌سازی میدانی، کالیبراسیون دوربین‌ها و محاسبه‌ی تبدیل دستگاه مختصات دوربین به دستگاه مختصات فضای فیزیکی (ماتریس‌های تبدیل مورد نیاز کد) با من بود."],
   role="طراحی، ساخت و راه‌اندازی کامل مکانیک ربات‌ها از طراحی تا پیگیری ساخت؛ اپلیکیشن موبایل تست مسیر؛ سامانه‌ی شارژ خودکار مفهومی؛ کالیبراسیون و تبدیل مختصات دوربین در پروژه‌ی دوقلوی دیجیتال.",
   facts=[("کاچ", "چهارچرخ، موتور استپر، کنترل موقعیت، ROS"), ("کارناک", "همه‌جهته با چرخ مکانوم، موتور استپر، Raspberry Pi و Arduino Mega"),
          ("تست مسیر", "اپلیکیشن موبایل: مسیرهای دایره، مربع و…"), ("کاربرد هدف", "ربات خدماتی حمل بار و دنبال‌کننده در زمین ناهموار")], awards=[]),
  en=dict(title="Kach and Karnak Mobile Robots (LeaMech)", short="A platform for mobile service robots: the ROS-based Kach and the omnidirectional, mecanum-wheeled Karnak.",
   tags=["Mobile robots", "Mecanum wheels", "ROS", "Auto-charging"],
   desc=["At LeaMech — an international team with members in the USA, Iran and other countries, working to launch a startup with funding from the US National Science Foundation (NSF) and planning its first branch in Turkey — we built a platform for mobile service robots: robots that carry loads and can follow a person over rough terrain, for camping, for bringing aid equipment to places such as forests that vehicles can't reach, or for moving objects in industry. The first goal was the platform itself, so the mechanics were kept at MVP level.",
         "The first robot, **Kach**, was a four-wheeled mobile robot with stepper motors; its position control was implemented and it followed defined paths on command, with software based on ROS. The second, **Karnak**, was an omnidirectional robot with mecanum wheels and stepper motors that could move in any direction. A Raspberry Pi and an Arduino Mega were its brain, and paths such as circles and squares were tested through a mobile app I wrote for it. Karnak's body was rigid and industrial, and we imported the mecanum wheels from China because they weren't available in Iran. I also designed and built a simple concept auto-charging system for it, which passed its initial tests.",
         "I also worked on other LeaMech projects: **Konum** (Turkish for “position”), a positioning system for parked cars at US car dealerships that made finding and delivering cars faster; its follow-up, **Kuş**, which was to track car positions with a drone; and the **Aktar & Nema** digital twin project for industrial and physical environments, where I handled field implementation, camera calibration and the transformation between the camera and physical-space coordinate frames (the transformation matrices the code needed)."],
   role="Full mechanical design, build and commissioning of the robots, from design to fabrication follow-up; the mobile path-testing app; the concept auto-charging system; camera calibration and coordinate transforms in the digital twin project.",
   facts=[("Kach", "Four wheels, stepper motors, position control, ROS"), ("Karnak", "Omnidirectional, mecanum wheels, stepper motors, Raspberry Pi + Arduino Mega"),
          ("Path testing", "Mobile app: circles, squares and more"), ("Target use", "Load-carrying, person-following service robot on rough terrain")], awards=[])),

 dict(slug="dmd-powder-feeder", year=("۱۳۹۸", "2019"), date="2019",
  imgs=[("p-dmd.webp", 1288, 952, "", "")], videos=[],
  fa=dict(title="سامانه‌ی تغذیه‌ی پودر DMD", short="تغذیه‌کننده‌ی پودر برای لایه‌نشانی مستقیم فلز با لیزر؛ نرخ ۱ تا ۱۰۰ گرم بر دقیقه.",
   tags=["ساخت افزایشی فلز", "کنترل", "الکترونیک"],
   desc=["تغذیه‌کننده‌ی پودر برای فرآیند لایه‌نشانی مستقیم فلز با لیزر (DMD)؛ نرخ تغذیه در بازه‌ی ۱ تا ۱۰۰ گرم بر دقیقه کنترل می‌شود.",
         "این پروژه پایان‌نامه‌ی کارشناسی من در دانشگاه علم و صنعت ایران بود، زیر نظر دکتر سید علی نیکنام."],
   role="طراحی تفصیلی، ساخت و پیاده‌سازی کامل الکترونیک، کنترل و منطق دستگاه.",
   facts=[("نرخ تغذیه", "۱ تا ۱۰۰ گرم بر دقیقه"), ("فرآیند", "لایه‌نشانی مستقیم فلز با لیزر (DMD)")], awards=[]),
  en=dict(title="DMD Powder Feeder", short="A powder feeder for laser direct metal deposition, controlled from 1 to 100 g/min.",
   tags=["Metal additive manufacturing", "Control", "Electronics"],
   desc=["A powder feeder for laser direct metal deposition (DMD); the feed rate is controlled across 1–100 g/min.",
         "This was my BSc thesis at Iran University of Science and Technology, supervised by Dr. Seyed Ali Niknam."],
   role="Detail design, fabrication, and full implementation of the electronics, control and logic.",
   facts=[("Feed rate", "1–100 g/min"), ("Process", "Laser direct metal deposition (DMD)")], awards=[])),

 dict(slug="cable-drawing-robot", year=("۱۳۹۹", "2020"), date="2020",
  imgs=[("p-painter.webp", 896, 1344, "", "")], videos=[],
  fa=dict(title="ربات نقاش کابلی", short="ربات کابلی که هر عکس را به نقاشی سیاه‌قلم تبدیل می‌کند و روی بوم می‌کشد.",
   tags=["ربات کابلی", "پردازش تصویر", "کنترل"],
   desc=["یک ربات نقاش بر پایه‌ی مکانیزم ربات‌های کابلی که قلم را با کنترل طول کابل‌ها در صفحه حرکت می‌دهد. این ربات می‌تواند هر عکس را به یک نقاشی سیاه‌قلم تبدیل کند و روی بوم بکشد (در تصویر، طرح یک گل رز را کشیده است)."],
   role="الگوریتم تبدیل تصویر به مسیر قلم و هماهنگی دقیق حرکت کابل‌ها برای رسیدن قلم به نقطه‌ی دلخواه.",
   facts=[("مکانیزم", "ربات کابلی"), ("ورودی", "هر عکس دلخواه")], awards=[]),
  en=dict(title="Cable-Driven Drawing Robot", short="A cable robot that turns any photo into a line drawing and draws it on canvas.",
   tags=["Cable robot", "Image processing", "Control"],
   desc=["A drawing robot based on a cable-driven mechanism that moves the pen across the board by controlling cable lengths. It converts a photo into a line drawing and draws it on the canvas (the photo shows a rose it drew)."],
   role="The algorithm that turns an image into a pen path, and the precise coordination of the cables to place the pen at any point.",
   facts=[("Mechanism", "Cable-driven robot"), ("Input", "Any photo")], awards=[])),
]

PROJECTS_PAGE = {
 "fa": dict(title="پروژه‌ها | حسن نصیری خونساری — ربات‌ها و ماشین‌هایی که طراحی و ساخته‌ام",
            desc="پروژه‌های طراحی و ساخت حسن نصیری خونساری: ربات‌های سورتر پستی، دستگاه تست پروتز زانو، پرینترهای سه‌بعدی صنعتی، CNC دوکاره، ربات‌های گارسون، ربات‌های متحرک همه‌جهته و…",
            kk="نمونه‌کارها", h1="پروژه‌ها", lead="ماشین‌ها و ربات‌هایی که طراحی کرده‌ام و ساخت و راه‌اندازی‌شان را پیگیری کرده‌ام. روی هر پروژه بزنید تا جزئیاتش را ببینید."),
 "en": dict(title="Projects | Hassan Nasiri Khonsari — Robots and Machines I Designed and Built",
            desc="Design-and-build projects by Hassan Nasiri Khonsari: postal sorting robots, a knee prosthesis test apparatus, industrial 3D printers, a dual-purpose CNC, waiter robots, omnidirectional mobile robots and more.",
            kk="Portfolio", h1="Projects", lead="Machines and robots I designed and followed through fabrication and commissioning. Open any project for details."),
}
MEDIA_PAGE = {
 "fa": dict(title="رسانه | حسن نصیری خونساری — گفت‌وگوها، گزارش‌ها و مستندها",
            desc="گفت‌وگوهای تلویزیونی، مستند، خبرها و مقاله‌های مربوط به حسن نصیری خونساری؛ از شبکه‌ی افق و شبکه‌ی یک تا ایرنا، دانشگاه صنعتی شریف و بنیاد البرز.",
            kk="رسانه", h1="در رسانه‌ها", lead="گفت‌وگوها، گزارش‌ها و مستندهایی درباره‌ی کارهایم."),
 "en": dict(title="Media | Hassan Nasiri Khonsari — Interviews, Reports and Documentaries",
            desc="TV interviews, a documentary, news and articles about Hassan Nasiri Khonsari — from Ofogh TV and IRIB TV1 to IRNA, Sharif University of Technology and the Alborz Foundation.",
            kk="Media", h1="In the media", lead="Interviews, reports and documentaries about my work."),
}
CONTACT = {
 "fa": dict(h="تماس", p="برای همکاری در پروژه‌های طراحی، ساخت، تولید تیراژی قطعات یا مشاوره، از فرم زیر یا راه‌های ارتباطی دیگر استفاده کنید.",
            name="نام شما", email="ایمیل شما", msg="پیام شما…", send="ارسال پیام", sending="در حال ارسال…", other="راه‌های ارتباطی دیگر:",
            ok="پیام شما ارسال شد. به‌زودی پاسخ می‌دهم.", err="ارسال انجام نشد. لطفاً دوباره تلاش کنید یا از ایمیل استفاده کنید.", net="ارسال انجام نشد. اتصال اینترنت را بررسی کنید.",
            links=[("email", "mailto:" + EMAIL, EMAIL), ("phone", "tel:" + PHONE, PHONE_FA), ("linkedin", LINKEDIN, "لینکدین"),
                   ("telegram", TELEGRAM, "تلگرام"), ("bale", BALE, "بله"), ("instagram", INSTAGRAM, "اینستاگرام")]),
 "en": dict(h="Contact", p="For design-and-build projects, batch production of parts or consulting, use the form below or any of the other channels.",
            name="Your name", email="Your email", msg="Your message…", send="Send message", sending="Sending…", other="Other channels:",
            ok="Your message was sent. I'll reply soon.", err="Sending failed. Please try again or use email.", net="Sending failed. Please check your connection.",
            links=[("email", "mailto:" + EMAIL, EMAIL), ("phone", "tel:" + PHONE, PHONE_EN), ("linkedin", LINKEDIN, "LinkedIn"),
                   ("telegram", TELEGRAM, "Telegram"), ("bale", BALE, "Bale"), ("instagram", INSTAGRAM, "Instagram")]),
}
