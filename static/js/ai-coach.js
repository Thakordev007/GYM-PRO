(function () {
  'use strict';

  const toggle = document.getElementById('aiCoachToggle');
  const panel = document.getElementById('aiCoachPanel');
  const closeBtn = document.getElementById('aiCoachClose');
  const messagesEl = document.getElementById('aiCoachMessages');
  const inputEl = document.getElementById('aiCoachInput');
  const sendBtn = document.getElementById('aiCoachSend');
  const quickActions = document.getElementById('aiQuickActions');

  if (!toggle || !panel) return;

  let context = {};
  let isLoading = false;

  const QUICK_ACTIONS = [
    { label: '🏋️ Workout Plan', msg: 'workout plan' },
    { label: '🥗 Diet Plan', msg: 'diet plan' },
    { label: 'ℹ️ Gym Info', msg: 'gym info' },
    { label: '💰 Plans', msg: 'plans' },
    { label: '👨‍🏫 Trainers', msg: 'trainers' },
  ];

  function getCsrfToken() {
    const cookie = document.cookie.split(';').find((c) => c.trim().startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
  }

  function formatReply(text) {
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n/g, '<br>');
  }

  function appendMessage(text, role) {
    const div = document.createElement('div');
    div.className = `ai-msg ${role}`;
    div.innerHTML = role === 'bot' ? formatReply(text) : text;
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function showTyping() {
    const div = document.createElement('div');
    div.className = 'ai-typing';
    div.id = 'aiTyping';
    div.innerHTML = '<span></span><span></span><span></span>';
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function hideTyping() {
    document.getElementById('aiTyping')?.remove();
  }

  async function sendMessage(text) {
    const msg = text.trim();
    if (!msg || isLoading) return;

    appendMessage(msg, 'user');
    inputEl.value = '';
    isLoading = true;
    showTyping();

    try {
      const res = await fetch('/api/ai-coach/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ message: msg, context }),
      });

      const data = await res.json();
      hideTyping();

      if (data.reply) {
        appendMessage(data.reply, 'bot');
        context = data.context || {};
      } else {
        appendMessage('Sorry, something went wrong. Please try again.', 'bot');
      }
    } catch {
      hideTyping();
      appendMessage('Connection error. Please check your network and try again.', 'bot');
    }

    isLoading = false;
  }

  function renderQuickActions() {
    quickActions.innerHTML = '';
    QUICK_ACTIONS.forEach(({ label, msg }) => {
      const btn = document.createElement('button');
      btn.className = 'ai-quick-btn';
      btn.type = 'button';
      btn.textContent = label;
      btn.addEventListener('click', () => sendMessage(msg));
      quickActions.appendChild(btn);
    });
  }

  function openPanel() {
    panel.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    inputEl.focus();
  }

  function closePanel() {
    panel.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  }

  toggle.addEventListener('click', () => {
    if (panel.classList.contains('open')) closePanel();
    else openPanel();
  });

  closeBtn?.addEventListener('click', closePanel);
  sendBtn?.addEventListener('click', () => sendMessage(inputEl.value));
  inputEl?.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') sendMessage(inputEl.value);
  });

  renderQuickActions();

  setTimeout(() => {
    appendMessage(
      "Hey! I'm **FitBot**, your GYM PRO fitness assistant. Ask me about gym info, workout plans, or diet plans — or tap a quick button below!",
      'bot'
    );
  }, 400);
})();
