# Welcome to My Versioned Docs Demo

This is versioned documentation powered by `mike`.

<select id="version-select"></select>
<script>
  fetch('versions.json')
    .then(res => {
      if (!res.ok) {
        console.error('Failed to load versions.json', res.statusText);
        return Promise.reject('Failed to fetch versions.json');
      }
      return res.json();
    })
    .then(versions => {
      const sel = document.getElementById('version-select');
      
      // Log versions to check if they're being fetched
      console.log('Fetched versions:', versions);

      // Get the current version from the URL (it should be in the format /v1.0/)
      const currentVersion = window.location.pathname.split('/')[2]; // Extract version like v1.0
      console.log('Current Version:', currentVersion);  // Log current version

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
    })
    .catch(error => {
      console.error('Error fetching versions:', error);
    });
</script>

Some text here

