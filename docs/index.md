# Welcome to My Versioned Docs Demo

This is versioned documentation powered by `mike`.


<select id="version-select"></select>
<script>
fetch('/versions.json')
  .then(res => res.json())
  .then(versions => {
    const sel = document.getElementById('version-select');
    versions.forEach(v => {
      const opt = document.createElement('option');
      opt.value = `/${v}/`;
      opt.textContent = v;
      sel.appendChild(opt);
    });
    sel.onchange = () => window.location.href = sel.value;
  });
</script>

