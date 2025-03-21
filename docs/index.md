# Welcome to My Versioned Docs Demo

This is versioned documentation powered by `mike`.

const currentVersion = window.location.pathname.split('/')[2]; // Extract v1.0
versions.forEach(v => {
  const opt = document.createElement('option');
  opt.value = `${v}/`;
  opt.textContent = v;
  if (v === currentVersion) opt.selected = true;
  sel.appendChild(opt);
});

Some text here
