async function scanPorts() {
    const ip = document.getElementById('ip').value;
    const start = document.getElementById('start').value;
    const end = document.getElementById('end').value;

    const response = await fetch('/scan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ip, start, end })
    });

    const data = await response.json();

    const results = document.getElementById('results');
    results.innerHTML = '';

    if (data.open_ports.length === 0) {
        results.innerHTML = '<li>No open ports found</li>';
    } else {
        data.open_ports.forEach(port => {
            const li = document.createElement('li');
            li.textContent = "Port " + port + " is OPEN";
            results.appendChild(li);
        });
    }
}