/**
 * Dashboard Analytics
 */

'use strict';

(function () {
  let cardColor, labelColor, borderColor, chartBgColor, bodyColor;

  cardColor = config.colors.cardColor;
  labelColor = config.colors.textMuted;
  borderColor = config.colors.borderColor;
  chartBgColor = config.colors.chartBgColor;
  bodyColor = config.colors.bodyColor;

  // Albums Released Over Time
fetch('/api/albums-over-time/')
  .then(res => res.json())
  .then(data => {
    
    new ApexCharts(document.querySelector("#albumsOverTimeChart"), {
      chart: { type: 'line', height: 300 },
      series: [{ name: 'Albums', data: data.counts }],
      xaxis: { categories: data.years },
    }).render();
  });

  // Album Type Distribution
fetch('/api/album-type-distribution/')
  .then(res => res.json())
  .then(data => {
    
    new ApexCharts(document.querySelector("#albumTypeDistributionChart"), {
      chart: { type: 'pie', height: 300 },
      series: data.counts,
      labels: data.labels,
    }).render();
  });

  // Awards by Album
fetch('/api/awards-by-album/')
  .then(res => res.json())
  .then(data => {
    const barHeight = 35; 
    const chartHeight = data.counts.length * barHeight;

    new ApexCharts(document.querySelector("#awardsByAlbumChart"), {
      chart: {
        type: 'bar',
        height: chartHeight 
      },
      series: [{ name: 'Awards', data: data.counts }],
      xaxis: { categories: data.titles },
      plotOptions: {
        bar: { horizontal: true }
      },
      dataLabels: { enabled: true }
    }).render();
  });

// Award Per Artist
fetch('/api/most-awarded-artist/')
  .then(res => res.json())
  .then(data => {
    
    new ApexCharts(document.querySelector("#mostAwardedArtistChart"), {
      chart: { type: 'donut', height: 300 },
      series: data.counts,
      labels: data.labels,
    }).render();
  });

})();