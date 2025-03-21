# Welcome to My Versioned Docs Demo

This is versioned documentation powered by `mike`.

<select id="version-select"></select>
<script>
  fetch('/my-mkdocs-mike-demo/versions.json')
    .then(res => res.json())
    .then(versions => {
      const sel = document.getElementById('version-select');
      const currentVersion = window.location.pathname.split('/')[2];

      versions.forEach(v => {
        const version = v.version;  // Extract version name from the object
        const opt = document.createElement('option');
        opt.value = `${version}/`;  // relative path
        opt.textContent = v.title || version;  // Use title if available, otherwise use version
        
        if (version === currentVersion) opt.selected = true;
        
        sel.appendChild(opt);
      });

      sel.onchange = () => window.location.href = sel.value;
    })
    .catch(error => {
      console.error('Error fetching versions:', error);
    });
</script>

Some text here
