/* رفتارهای مشترک همه‌ی صفحه‌ها. محتوای صفحه در HTML ساخته شده است؛ این فایل فقط پخش ویدیو، گالری، فرم و آمار را اضافه می‌کند. */
(function(){
  var L = document.documentElement.lang === 'en' ? 'en' : 'fa';
  var T = {
    fa: {close:'بستن', prev:'قبلی', next:'بعدی', send:'ارسال پیام', sending:'در حال ارسال…',
         ok:'پیام شما ارسال شد. به‌زودی پاسخ می‌دهم.', err:'ارسال انجام نشد. لطفاً دوباره تلاش کنید یا از ایمیل استفاده کنید.', net:'ارسال انجام نشد. اتصال اینترنت را بررسی کنید.'},
    en: {close:'Close', prev:'Previous', next:'Next', send:'Send message', sending:'Sending…',
         ok:"Your message was sent. I'll reply soon.", err:'Sending failed. Please try again or use email.', net:'Sending failed. Please check your connection.'}
  }[L];
  function fmt(n){ return L === 'en' ? String(n) : String(n).replace(/\d/g, function(d){ return '۰۱۲۳۴۵۶۷۸۹'[d]; }); }

  /* آمار کلیک‌ها — دانلود فایل‌ها و لینک‌های بیرونی را «Enhanced measurement» خود گوگل ثبت می‌کند */
  window.track = function(name, params){ try{ gtag('event', name, params || {}); }catch(e){} };
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a,button'); if(!a) return;
    var card = a.closest('.m-card');
    if(card){
      var act = a.closest('.m-gal') ? 'gallery' : a.classList.contains('m-more') ? 'more' : a.tagName === 'BUTTON' ? 'play' : 'open';
      track('media_click', {label: card.getAttribute('data-id') || '', action: act});
      return;
    }
    var pc = a.closest('[data-project]');
    if(pc){ track('project_open', {label: pc.getAttribute('data-project'), place: a.getAttribute('data-place') || 'page'}); return; }
    var svc = a.closest('[data-service]');
    if(svc){ track('service_click', {label: svc.getAttribute('data-service')}); }
    var href = a.getAttribute('href') || '';
    if(a.classList.contains('lang-sw')) track('lang_switch', {label: href});
    else if(href.indexOf('tel:') === 0) track('contact_click', {label: 'phone'});
    else if(href.indexOf('mailto:') === 0) track('contact_click', {label: 'email'});
    else if(a.hasAttribute('data-contact')) track('contact_click', {label: a.getAttribute('data-contact')});
    else if(a.closest('.menu')) track('nav_click', {label: href, place: 'menu'});
    else if(href.charAt(0) === '#' && href.length > 1) track('nav_click', {label: href.slice(1), place: 'page'});
  }, true);

  /* نمایش تدریجی بخش‌ها */
  if('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    }, {threshold: 0.12});
    document.querySelectorAll('.reveal').forEach(function(el, i){ el.style.transitionDelay = (i % 3 * 0.08) + 's'; io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function(el){ el.classList.add('in'); });
  }

  /* اسکرول نرم به بخش‌های همین صفحه */
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      var t = document.getElementById(a.getAttribute('href').slice(1)); if(!t) return;
      e.preventDefault();
      var y = t.getBoundingClientRect().top + window.pageYOffset - document.querySelector('nav').offsetHeight - 12;
      window.scrollTo({top: y, behavior: 'smooth'});
    });
  });

  /* پخش ویدیوی آپارات داخل صفحه */
  document.querySelectorAll('button.m-play[data-aparat]').forEach(function(b){
    b.addEventListener('click', function(){
      var f = document.createElement('iframe');
      f.src = 'https://www.aparat.com/video/video/embed/videohash/' + encodeURIComponent(b.getAttribute('data-aparat')) + '/vt/frame';
      f.title = b.getAttribute('aria-label') || ''; f.allow = 'autoplay; fullscreen'; f.setAttribute('allowfullscreen', '');
      b.parentNode.replaceChild(f, b);
    });
  });

  /* گالری تصاویر (کارت‌های رسانه و صفحه‌ی پروژه‌ها): هر دکمه با data-full، در گروه data-lb */
  var lb, list = [], idx = 0;
  function show(i){
    idx = (i + list.length) % list.length;
    lb.querySelector('img').src = list[idx].src; lb.querySelector('img').alt = list[idx].alt || '';
    lb.querySelector('.lb-c').textContent = (list[idx].alt ? list[idx].alt + ' — ' : '') + fmt(idx + 1) + ' / ' + fmt(list.length);
  }
  function close(){ lb.classList.remove('show'); document.body.style.overflow = ''; }
  function open(items, i){
    if(!lb){
      lb = document.createElement('div'); lb.className = 'm-lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true');
      lb.innerHTML = '<img alt=""><button type="button" class="lb-x" aria-label="' + T.close + '">×</button>'
        + '<button type="button" class="lb-p" aria-label="' + T.prev + '">' + (L === 'en' ? '‹' : '›') + '</button>'
        + '<button type="button" class="lb-n" aria-label="' + T.next + '">' + (L === 'en' ? '›' : '‹') + '</button><div class="lb-c"></div>';
      lb.onclick = function(e){ if(e.target === lb) close(); };
      lb.querySelector('.lb-x').onclick = close;
      lb.querySelector('.lb-p').onclick = function(){ show(idx - 1); };
      lb.querySelector('.lb-n').onclick = function(){ show(idx + 1); };
      document.addEventListener('keydown', function(e){
        if(!lb.classList.contains('show')) return;
        if(e.key === 'Escape') close();
        else if(e.key === 'ArrowRight') show(idx + (L === 'en' ? 1 : -1));
        else if(e.key === 'ArrowLeft') show(idx + (L === 'en' ? -1 : 1));
      });
      document.body.appendChild(lb);
    }
    list = items; show(i); lb.classList.add('show'); document.body.style.overflow = 'hidden'; lb.querySelector('.lb-x').focus();
  }
  document.querySelectorAll('[data-lb]').forEach(function(g){
    var btns = Array.prototype.slice.call(g.querySelectorAll('button[data-full]'));
    var seen = [], items = [];
    btns.forEach(function(b){ var s = b.getAttribute('data-full'); if(seen.indexOf(s) < 0){ seen.push(s); items.push({src: s, alt: b.getAttribute('data-alt') || ''}); } });
    btns.forEach(function(b){ b.addEventListener('click', function(){ open(items, seen.indexOf(b.getAttribute('data-full'))); }); });
  });

  /* فرم تماس (Formspree) بدون رفرش صفحه */
  var cform = document.getElementById('contactForm');
  if(cform){
    cform.addEventListener('submit', function(e){
      e.preventDefault();
      var status = document.getElementById('cfStatus'), btn = cform.querySelector('.cf-btn');
      status.textContent = ''; status.className = 'cf-status';
      btn.disabled = true; btn.textContent = T.sending;
      fetch(cform.action, {method: 'POST', body: new FormData(cform), headers: {'Accept': 'application/json'}})
        .then(function(res){
          if(res.ok){ track('contact_form_sent'); cform.reset(); status.textContent = T.ok; status.className = 'cf-status ok'; }
          else { status.textContent = T.err; status.className = 'cf-status err'; }
        })
        .catch(function(){ status.textContent = T.net; status.className = 'cf-status err'; })
        .then(function(){ btn.disabled = false; btn.textContent = T.send; });
    });
  }
})();
