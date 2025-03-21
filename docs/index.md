# Welcome to My Versioned Docs Demo

This is versioned documentation powered by `mike`.

<select id="version-select"></select>
<script>
  fetch('versions.json')
    .then(res => res.json())
    .then(versions => {
      const sel = document.getElementById('version-select');
      
      // Get the current version from the URL (it should be in the format /v1.0/)
      const currentVersion = window.location.pathname.split('/')[2]; // Extract version like v1.0

      // Create dropdown options for each version
      versions.forEach(v => {
        const opt = document.createElement('option');
        opt.value = `${v}/`;  // relative path
        opt.textContent = v;
        
        // Set the current version as selected
        if (v === currentVersion) opt.selected = true;
        
        sel.appendChild(opt);
      });

      // Redirect to selected version when changed
      sel.onchange = () => window.location.href = sel.value;
    });
</script>

Some text here

