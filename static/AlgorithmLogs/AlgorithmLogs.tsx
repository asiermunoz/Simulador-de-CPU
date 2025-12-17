document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('refresh-btn');
  const display = document.getElementById('logs-display');
  const algorithm_name = document.getElementById('algorithm-name');
  const refresh_interval = 1000; // 1 second

  async function refresh_logs() {
    fetch('/exec-data/')
      .then(async response => {
        let json = await response.json();
        if (json.data && json.data instanceof Array && display) {        
          if (json.data.length === 0) {
            display.innerText = 'Your logs are empty for now.';
          } else {
            display.innerText = json.data.join('\n');
          }
        }
        if (json.name && algorithm_name) {
          algorithm_name.innerText = json.name;
        }
      })
      .catch(error => {
        console.error('Error fetching logs:', error);
      });
  }

  if (btn) btn.addEventListener('click', refresh_logs);
  setInterval(refresh_logs, refresh_interval);
});


