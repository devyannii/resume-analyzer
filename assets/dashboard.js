const views = document.querySelectorAll('.view');
const links = document.querySelectorAll('[data-view]');
const title = document.querySelector('#page-title');
const titles = { dashboard: 'Dashboard', resume: 'My resume', match: 'Role match', insights: 'Insights' };
let resumeAnalysis = null;

function showView(viewId) {
  views.forEach((view) => view.classList.toggle('active', view.id === viewId));
  document.querySelectorAll('.nav-link').forEach((link) => link.classList.toggle('active', link.dataset.view === viewId));
  title.textContent = titles[viewId];
  window.location.hash = viewId;
}

function makeTags(items) {
  const container = document.createElement('div');
  items.forEach((item) => {
    const tag = document.createElement('span');
    tag.className = 'skill-pill';
    tag.textContent = item;
    container.append(tag);
  });
  return container;
}

function renderResume(result) {
  const summary = document.querySelector('.resume-summary');
  summary.replaceChildren();
  const skillsPanel = document.createElement('div');
  skillsPanel.className = 'panel';
  skillsPanel.innerHTML = `<p class="overline">Detected skills</p><h3>${result.skills.length} skills found</h3>`;
  skillsPanel.append(makeTags(result.skills.slice(0, 16)));
  const sectionsPanel = document.createElement('div');
  sectionsPanel.className = 'panel accent-panel';
  sectionsPanel.innerHTML = `<p class="overline">Resume snapshot</p><h3>${result.word_count} words</h3>`;
  Object.entries(result.sections).forEach(([name, content]) => {
    const item = document.createElement('p');
    item.textContent = `${name}: ${content.length} entries`;
    sectionsPanel.append(item);
  });
  summary.append(skillsPanel, sectionsPanel);
  document.querySelector('.welcome-orb span').textContent = Math.min(100, 55 + result.skills.length * 3);
}

async function getJson(response) {
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || 'Request failed.');
  return data;
}

links.forEach((link) => link.addEventListener('click', (event) => {
  if (!link.dataset.view) return;
  event.preventDefault();
  showView(link.dataset.view);
}));

const fileInput = document.querySelector('#resume-file');
const uploadStatus = document.querySelector('#upload-status');
fileInput.addEventListener('change', async () => {
  const file = fileInput.files[0];
  if (!file) return;
  uploadStatus.textContent = `Analyzing ${file.name}...`;
  const form = new FormData();
  form.append('resume', file);
  try {
    resumeAnalysis = await getJson(await fetch('/api/analyze', { method: 'POST', body: form }));
    uploadStatus.textContent = `${file.name} analyzed successfully.`;
    renderResume(resumeAnalysis);
  } catch (error) {
    uploadStatus.textContent = error.message;
  }
});

document.querySelector('#match-button').addEventListener('click', async () => {
  const description = document.querySelector('#job-description').value.trim();
  const preview = document.querySelector('.score-preview');
  if (!resumeAnalysis) {
    preview.querySelector('p:last-child').textContent = 'Upload your resume before checking a role match.';
    return;
  }
  if (!description) return;
  try {
    const analysis = await getJson(await fetch('/api/match', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ job_description: description, resume_skills: resumeAnalysis.skills }),
    }));
    preview.innerHTML = `<p class="overline">Your match</p><div class="mini-ring">${analysis.score}%<span>ATS score</span></div><h3>${analysis.verdict}</h3><p>${analysis.matched_count} skills match · ${analysis.missing_count} skills to improve</p>`;
    preview.append(makeTags(analysis.missing));
  } catch (error) {
    preview.querySelector('p:last-child').textContent = error.message;
  }
});

const initialView = window.location.hash.slice(1);
if (titles[initialView]) showView(initialView);
document.querySelector('.activity-grid').innerHTML = '<i></i>'.repeat(35);
