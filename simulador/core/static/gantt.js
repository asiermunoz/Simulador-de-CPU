// Simple Gantt renderer
window.renderGantt = function(container, processes){
  if(!container) return;
  container.innerHTML = '';

  // flatten all segments and find timeline bounds
  let minT = Infinity, maxT = -Infinity;
  processes.forEach(p=>{
    (p.history||[]).forEach(s=>{
      minT = Math.min(minT, s.start);
      maxT = Math.max(maxT, s.end);
    });
  });
  if(minT===Infinity) { container.textContent = 'No schedule data.'; return; }

  const total = Math.max(1, maxT - minT);

  // sort processes by pid for stable ordering
  processes.sort((a,b)=>a.pid - b.pid);

  processes.forEach((p, idx)=>{
    const row = document.createElement('div'); row.className='gantt-row';
    const label = document.createElement('div'); label.className='gantt-label'; label.textContent = 'P' + p.pid;
    const track = document.createElement('div'); track.className='gantt-track';

    (p.history||[]).forEach(seg=>{
      const segEl = document.createElement('div');
      segEl.className = 'gantt-seg gantt-color-' + (idx % 6);
      const left = ((seg.start - minT) / total) * 100;
      const width = ((seg.end - seg.start) / total) * 100;
      segEl.style.left = left + '%';
      segEl.style.width = width + '%';
      segEl.textContent = seg.end - seg.start;
      // tooltip data
      segEl.dataset.pid = p.pid;
      segEl.dataset.start = seg.start;
      segEl.dataset.end = seg.end;
      segEl.dataset.len = seg.end - seg.start;
      segEl.addEventListener('mouseenter', onSegEnter);
      segEl.addEventListener('mouseleave', onSegLeave);
      track.appendChild(segEl);
    });

    row.appendChild(label);
    row.appendChild(track);
    container.appendChild(row);
  });

  // draw time axis with ticks every unit (or scaled when long)
  const axis = document.createElement('div'); axis.className='gantt-timeaxis';
  const span = maxT - minT;
  let step = 1;
  if(span > 40) step = Math.ceil(span / 40);
  const ticks = [];
  for(let t = minT; t <= maxT; t += step){ ticks.push(t); }

  const tickRow = document.createElement('div'); tickRow.style.display = 'flex'; tickRow.style.justifyContent='space-between';
  ticks.forEach((t,i)=>{
    const lbl = document.createElement('div'); lbl.className='gantt-axis-label'; lbl.style.textAlign='center'; lbl.style.flex='1'; lbl.textContent = t;
    tickRow.appendChild(lbl);
  });
  // place ticks inside a labeled row so the 'Tiempo' label appears like P1/P2
  const timeRow = document.createElement('div'); timeRow.className = 'gantt-row';
  const timeLabel = document.createElement('div'); timeLabel.className = 'gantt-label'; timeLabel.textContent = 'Time';
  const timeTrack = document.createElement('div'); timeTrack.className = 'gantt-track';
  timeTrack.appendChild(tickRow);
  timeRow.appendChild(timeLabel);
  timeRow.appendChild(timeTrack);
  container.appendChild(timeRow);

  // compute idle segments and summary metrics display
  const flat = [];
  processes.forEach(p=>{ (p.history||[]).forEach(s=>flat.push({start:s.start,end:s.end})); });
  flat.sort((a,b)=>a.start-b.start);
  const merged = [];
  flat.forEach(s=>{
    if(!merged.length || s.start > merged[merged.length-1].end){ merged.push({start:s.start,end:s.end}); }
    else { merged[merged.length-1].end = Math.max(merged[merged.length-1].end, s.end); }
  });
  const busy = merged.reduce((acc,m)=>acc + (m.end - m.start), 0);
  const makespan = maxT - minT;
  const idle = Math.max(0, makespan - busy);

  // summary box
  const summary = document.createElement('div');
  summary.innerHTML = `<strong>Makespan:</strong> ${makespan} &nbsp; <strong>Busy:</strong> ${busy} &nbsp; <strong>Idle:</strong> ${idle} &nbsp; <strong>Processes:</strong> ${processes.length}`;
  summary.style.marginTop = '8px';
  container.insertBefore(summary, container.firstChild);

  // tooltip element
  let tooltip = document.getElementById('gantt-tooltip');
  if(!tooltip){ tooltip = document.createElement('div'); tooltip.id='gantt-tooltip'; tooltip.className='gantt-tooltip'; document.body.appendChild(tooltip); }

  function onSegEnter(e){
    const el = e.currentTarget;
    tooltip.style.display = 'block';
    tooltip.innerHTML = `P${el.dataset.pid}: ${el.dataset.start} - ${el.dataset.end} (${el.dataset.len})`;
    const rect = el.getBoundingClientRect();
    tooltip.style.left = (rect.left + rect.width/2) + 'px';
    tooltip.style.top = (rect.top - 30) + 'px';
  }
  function onSegLeave(){ tooltip.style.display='none'; }
}
