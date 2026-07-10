const views = document.querySelectorAll('.view');
const links = document.querySelectorAll('[data-view]');
const title = document.querySelector('#page-title');
const titles = { dashboard: 'Dashboard', resume: 'My resume', match: 'Role match', insights: 'Insights' };

function showView(viewId) {
  views.forEach((view) => view.classList.toggle('active', view.id === viewId));
  document.querySelectorAll('.nav-link').forEach((link) => link.classList.toggle('active', link.dataset.view === viewId));
  title.textContent = titles[viewId];
  window.location.hash = viewId;
}

links.forEach((link) => link.addEventListener('click', (event) => {
  const viewId = link.dataset.view;
  if (!viewId) return;
  event.preventDefault();
  showView(viewId);
}));

const fileInput = document.querySelector('#resume-file');
const uploadStatus = document.querySelector('#upload-status');
fileInput.addEventListener('change', () => {
  uploadStatus.textContent = fileInput.files.length ? `${fileInput.files[0].name} is ready for analysis.` : 'No file selected yet';
});

document.querySelector('#match-button').addEventListener('click', () => {
  const description = document.querySelector('#job-description').value.trim();
  if (description) alert('Your job description is ready. Connect the Python analyzer API next to calculate the live ATS score.');
});

const initialView = window.location.hash.slice(1);
if (titles[initialView]) showView(initialView);

document.querySelector('.activity-grid').innerHTML = '<i></i>'.repeat(35);
