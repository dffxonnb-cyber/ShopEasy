const dashboardData = {
  meta: {
    period: "2025.07 - 2025.09",
    updatedAt: "2026-04-24",
  },
  kpis: [
    {
      label: "완료 매출",
      value: 89439000,
      format: "currency",
      pill: "누적 실적",
      note: "완료 주문 기준 누적 매출",
      trend: "7월 대비 9월 매출 -47.9%",
      series: [60978000, 47411000, 31776000],
      color: "#356dff",
    },
    {
      label: "완료 주문",
      value: 688,
      format: "number",
      suffix: "건",
      pill: "주문 현황",
      note: "전체 주문 1,000건 중 완료 688건",
      trend: "전체 완료율 68.8%",
      series: [305, 224, 159],
      color: "#1da89b",
    },
    {
      label: "전체 세션",
      value: 2000,
      format: "number",
      suffix: "회",
      pill: "유입 규모",
      note: "구매 완료 세션 174회",
      trend: "세션 구매 전환 8.7%",
      series: [511, 715, 455],
      color: "#f2a93b",
    },
    {
      label: "활성 고객",
      value: 92,
      format: "number",
      suffix: "명",
      pill: "고객 상태",
      note: "전체 사용자 500명 중 18.4%",
      trend: "이탈위험 고객 200명",
      series: [200, 134, 92, 53, 21],
      color: "#e16357",
    },
  ],
  monthlyOrders: [
    {
      month: "2025.07",
      totalOrders: 420,
      completedOrders: 305,
      totalAmount: 60978000,
      completionRate: 72.62,
    },
    {
      month: "2025.08",
      totalOrders: 340,
      completedOrders: 224,
      totalAmount: 47411000,
      completionRate: 65.88,
    },
    {
      month: "2025.09",
      totalOrders: 240,
      completedOrders: 159,
      totalAmount: 31776000,
      completionRate: 66.25,
    },
  ],
  categoryCompletion: [
    {
      category: "식품",
      totalOrders: 183,
      completedOrders: 150,
      avgAmount: 69164,
      totalAmount: 12657000,
      completionRate: 81.97,
    },
    {
      category: "뷰티",
      totalOrders: 182,
      completedOrders: 134,
      avgAmount: 74879,
      totalAmount: 13628000,
      completionRate: 73.63,
    },
    {
      category: "홈리빙",
      totalOrders: 172,
      completedOrders: 124,
      avgAmount: 162680,
      totalAmount: 27981000,
      completionRate: 72.09,
    },
    {
      category: "패션",
      totalOrders: 249,
      completedOrders: 168,
      avgAmount: 112920,
      totalAmount: 28117000,
      completionRate: 67.47,
    },
    {
      category: "전자기기",
      totalOrders: 214,
      completedOrders: 112,
      avgAmount: 270009,
      totalAmount: 57782000,
      completionRate: 52.34,
    },
  ],
  deviceConversion: [
    {
      device: "태블릿",
      totalSessions: 143,
      avgSessionDuration: 214.15,
      completedPurchases: 24,
      conversionRate: 16.78,
      badge: "Best Efficiency",
    },
    {
      device: "데스크톱",
      totalSessions: 508,
      avgSessionDuration: 200.75,
      completedPurchases: 64,
      conversionRate: 12.6,
      badge: "Balanced Traffic",
    },
    {
      device: "모바일",
      totalSessions: 1349,
      avgSessionDuration: 153.88,
      completedPurchases: 86,
      conversionRate: 6.38,
      badge: "Highest Volume",
    },
  ],
  entryConversion: [
    {
      entryPage: "상품상세",
      totalSessions: 455,
      avgSessionDuration: 272.19,
      completedPurchases: 79,
      conversionRate: 17.36,
    },
    {
      entryPage: "카테고리",
      totalSessions: 319,
      avgSessionDuration: 185.42,
      completedPurchases: 22,
      conversionRate: 6.9,
    },
    {
      entryPage: "홈",
      totalSessions: 715,
      avgSessionDuration: 105.75,
      completedPurchases: 45,
      conversionRate: 6.29,
    },
    {
      entryPage: "검색",
      totalSessions: 511,
      avgSessionDuration: 159.65,
      completedPurchases: 28,
      conversionRate: 5.48,
    },
  ],
  ageChurn: [
    {
      ageGroup: "50대 이상",
      totalUsers: 83,
      churnedUsers: 56,
      avgPurchaseCount: 1.59,
      churnRate: 67.47,
    },
    {
      ageGroup: "20대",
      totalUsers: 163,
      churnedUsers: 95,
      avgPurchaseCount: 1.45,
      churnRate: 58.28,
    },
    {
      ageGroup: "40대",
      totalUsers: 108,
      churnedUsers: 47,
      avgPurchaseCount: 3.65,
      churnRate: 43.52,
    },
    {
      ageGroup: "30대",
      totalUsers: 146,
      churnedUsers: 55,
      avgPurchaseCount: 3.95,
      churnRate: 37.67,
    },
  ],
  lifecycleSegments: [
    { name: "이탈위험", count: 200, color: "#e16357" },
    { name: "휴면징후", count: 134, color: "#f2a93b" },
    { name: "활성고객", count: 92, color: "#356dff" },
    { name: "관심고객", count: 53, color: "#1da89b" },
    { name: "충성고객", count: 21, color: "#46526f" },
  ],
  exitAnalysis: [
    {
      exitPage: "검색",
      totalSessions: 696,
      avgSessionDuration: 129.31,
      completedPurchases: 0,
      conversionRate: 0,
    },
    {
      exitPage: "홈",
      totalSessions: 664,
      avgSessionDuration: 126.2,
      completedPurchases: 0,
      conversionRate: 0,
    },
    {
      exitPage: "장바구니",
      totalSessions: 395,
      avgSessionDuration: 207.4,
      completedPurchases: 0,
      conversionRate: 0,
    },
    {
      exitPage: "완료",
      totalSessions: 174,
      avgSessionDuration: 362.66,
      completedPurchases: 174,
      conversionRate: 100,
    },
    {
      exitPage: "결제",
      totalSessions: 71,
      avgSessionDuration: 300.92,
      completedPurchases: 0,
      conversionRate: 0,
    },
  ],
  insights: [
    {
      tag: "전환 강점",
      title: "상품상세 유입 전환율이 17.36%로 가장 높습니다.",
      body: "홈 유입 6.29% 대비 약 2.8배 높아, 상세 페이지로 바로 들어오는 세션이 실제 구매와 가장 가까운 흐름을 보입니다.",
    },
    {
      tag: "카테고리 편차",
      title: "식품 완료율 81.97%, 전자기기 완료율 52.34%입니다.",
      body: "전자기기는 매출 규모는 크지만 완료율이 낮아 가격 저항이나 결제 직전 이탈 요소를 먼저 점검할 필요가 있습니다.",
    },
    {
      tag: "세그먼트 리스크",
      title: "50대 이상 이탈률은 67.47%로 가장 높습니다.",
      body: "평균 구매 횟수 1.59회에 머물러 있어 재방문 유도 메시지와 간결한 구매 동선 개선이 함께 필요합니다.",
    },
    {
      tag: "디바이스 기회",
      title: "태블릿 전환율 16.78%로 효율이 가장 좋습니다.",
      body: "세션 규모는 작지만 성과가 좋아 태블릿 기준 상품상세 레이아웃을 기준안으로 삼아볼 만합니다.",
    },
  ],
  monthlyInsight:
    "7월 대비 9월 주문 수가 감소했고, 완료 주문 수도 함께 줄어 전체 수요보다 구매 완료 흐름의 약화 가능성을 함께 점검할 필요가 있습니다.",
};

const numberFormatter = new Intl.NumberFormat("ko-KR");

function formatNumber(value) {
  return numberFormatter.format(value);
}

function formatPercent(value) {
  return `${Number(value).toFixed(2)}%`;
}

function formatValue(item) {
  if (item.format === "currency") {
    return `${formatNumber(item.value)}원`;
  }

  return `${formatNumber(item.value)}${item.suffix ?? ""}`;
}

function formatCurrency(value) {
  return `${formatNumber(value)}원`;
}

function formatCurrencyWan(value) {
  return `${formatNumber(Math.round(value / 10000))}만원`;
}

function formatDuration(secondsValue) {
  const totalSeconds = Math.round(Number(secondsValue));
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;

  if (minutes === 0) {
    return `${seconds}초`;
  }

  return `${minutes}분 ${String(seconds).padStart(2, "0")}초`;
}

function formatMonthShort(value) {
  const monthPart = String(value).split(".")[1] ?? value;
  return `${Number(monthPart)}월`;
}

function formatDelta(current, previous) {
  if (!previous) {
    return "기준 월";
  }

  const delta = ((current - previous) / previous) * 100;
  const prefix = delta > 0 ? "+" : "";
  return `전월 대비 ${prefix}${delta.toFixed(1)}%`;
}

function sparklinePoints(series, width, height, padding) {
  const max = Math.max(...series);
  const min = Math.min(...series);
  const range = max - min || 1;

  return series
    .map((value, index) => {
      const x =
        padding + (index * (width - padding * 2)) / Math.max(series.length - 1, 1);
      const y = height - padding - ((value - min) / range) * (height - padding * 2);
      return `${x},${y}`;
    })
    .join(" ");
}

function renderKpis() {
  const container = document.querySelector("#kpi-grid");
  if (!container) {
    return;
  }

  container.innerHTML = dashboardData.kpis
    .map((item, index) => {
      const points = sparklinePoints(item.series, 92, 34, 4);
      const gradientId = `spark-gradient-${index}`;

      return `
        <article class="kpi-card">
          <div class="kpi-top">
            <div>
              <p class="kpi-label">${item.label}</p>
              <h2 class="kpi-value">${formatValue(item)}</h2>
              <p class="kpi-note">${item.note}</p>
            </div>
            <span class="kpi-pill">${item.pill}</span>
          </div>
          <div class="kpi-foot">
            <p class="kpi-trend">${item.trend}</p>
            <svg class="sparkline" viewBox="0 0 92 34" role="presentation" aria-hidden="true">
              <defs>
                <linearGradient id="${gradientId}" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="${item.color}" stop-opacity="0.25"></stop>
                  <stop offset="100%" stop-color="${item.color}" stop-opacity="1"></stop>
                </linearGradient>
              </defs>
              <polyline
                fill="none"
                stroke="url(#${gradientId})"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
                points="${points}"
              ></polyline>
            </svg>
          </div>
        </article>
      `;
    })
    .join("");
}

function renderMonthlyChart() {
  const container = document.querySelector("#monthly-chart");
  if (!container) {
    return;
  }

  const data = dashboardData.monthlyOrders;
  const width = Math.max(container.clientWidth, 360);
  const height = width < 520 ? 320 : 360;
  const margin = { top: 34, right: 24, bottom: 52, left: 56 };
  const chartWidth = width - margin.left - margin.right;
  const chartHeight = height - margin.top - margin.bottom;
  const maxOrders = Math.max(...data.flatMap((item) => [item.totalOrders, item.completedOrders]));
  const orderCeil = Math.ceil(maxOrders / 50) * 50;
  const leftAxisTicks = Array.from({ length: 5 }, (_, index) => (orderCeil / 4) * index);
  const yOrder = (value) => margin.top + chartHeight - (value / orderCeil) * chartHeight;
  const xPosition = (index) => {
    if (data.length === 1) {
      return margin.left + chartWidth / 2;
    }

    return margin.left + (index * chartWidth) / (data.length - 1);
  };

  const totalLinePoints = data
    .map((item, index) => {
      const x = xPosition(index);
      return `${x},${yOrder(item.totalOrders)}`;
    })
    .join(" ");

  const completedLinePoints = data
    .map((item, index) => {
      const x = xPosition(index);
      return `${x},${yOrder(item.completedOrders)}`;
    })
    .join(" ");

  const completedAreaPoints = `
    ${margin.left},${margin.top + chartHeight}
    ${completedLinePoints}
    ${xPosition(data.length - 1)},${margin.top + chartHeight}
  `;

  const gridLines = leftAxisTicks
    .map((tick) => {
      const y = yOrder(tick);
      return `
        <line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" stroke="#dfe7f5" stroke-width="1.2"></line>
        <text x="${margin.left - 12}" y="${y + 4}" text-anchor="end" font-size="12" fill="#7b88a5">${formatNumber(
          tick,
        )}</text>
      `;
    })
    .join("");

  const monthLabels = data
    .map((item, index) => {
      const x = xPosition(index);
      return `
        <line x1="${x}" y1="${margin.top}" x2="${x}" y2="${margin.top + chartHeight}" stroke="#f1f5fb" stroke-width="1"></line>
        <text x="${x}" y="${height - 14}" text-anchor="middle" font-size="12" fill="#66748f">${formatMonthShort(
          item.month,
        )}</text>
      `;
    })
    .join("");

  const pointMarkers = data
    .map((item, index) => {
      const x = xPosition(index);
      const totalY = yOrder(item.totalOrders);
      const completedY = yOrder(item.completedOrders);
      return `
        <circle cx="${x}" cy="${totalY}" r="5.5" fill="#7b88a5"></circle>
        <circle cx="${x}" cy="${totalY}" r="11" fill="#7b88a5" opacity="0.12"></circle>
        <circle cx="${x}" cy="${completedY}" r="5.5" fill="#356dff"></circle>
        <circle cx="${x}" cy="${completedY}" r="11" fill="#356dff" opacity="0.14"></circle>
        <text x="${x}" y="${totalY - 16}" text-anchor="middle" font-size="12" fill="#5b6782" font-weight="700">${formatNumber(
          item.totalOrders,
        )}</text>
        <text x="${x}" y="${completedY + 24}" text-anchor="middle" font-size="12" fill="#356dff" font-weight="700">${formatNumber(
          item.completedOrders,
        )}</text>
      `;
    })
    .join("");

  container.innerHTML = `
    <svg viewBox="0 0 ${width} ${height}" width="100%" height="${height}" role="presentation" aria-hidden="true">
      <defs>
        <linearGradient id="completed-area-fill" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#356dff" stop-opacity="0.16"></stop>
          <stop offset="100%" stop-color="#356dff" stop-opacity="0.01"></stop>
        </linearGradient>
      </defs>
      ${gridLines}
      ${monthLabels}
      <line x1="${margin.left}" y1="${margin.top + chartHeight}" x2="${width - margin.right}" y2="${margin.top + chartHeight}" stroke="#dbe3f2" stroke-width="1.5"></line>
      <polygon points="${completedAreaPoints}" fill="url(#completed-area-fill)"></polygon>
      <polyline fill="none" stroke="#7b88a5" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" points="${totalLinePoints}"></polyline>
      <polyline fill="none" stroke="#356dff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" points="${completedLinePoints}"></polyline>
      ${pointMarkers}
      <text x="${margin.left}" y="14" font-size="12" fill="#7b88a5">주문 수 (건)</text>
    </svg>
  `;
}

function renderMonthlyMetrics() {
  const container = document.querySelector("#monthly-metrics");
  if (!container) {
    return;
  }

  container.innerHTML = dashboardData.monthlyOrders
    .map((item, index, array) => {
      const previous = array[index - 1]?.totalOrders;
      return `
        <article class="mini-metric">
          <span class="mini-metric-label">${formatMonthShort(item.month)} 구매 완료율</span>
          <strong>${formatPercent(item.completionRate)}</strong>
          <small>전체 주문 ${formatNumber(item.totalOrders)}건 · 완료 주문 ${formatNumber(item.completedOrders)}건</small>
          <small>주문 수 ${formatDelta(item.totalOrders, previous)}</small>
        </article>
      `;
    })
    .join("");
}

function renderMonthlyInsight() {
  const container = document.querySelector("#monthly-insight");
  if (!container) {
    return;
  }

  container.innerHTML = `
    <p class="monthly-insight-label">BUSINESS INSIGHT</p>
    <p>${dashboardData.monthlyInsight}</p>
  `;
}

function renderInsights() {
  const container = document.querySelector("#insight-list");
  if (!container) {
    return;
  }

  container.innerHTML = dashboardData.insights
    .map(
      (item) => `
        <article class="insight-card">
          <span class="insight-tag">${item.tag}</span>
          <h3>${item.title}</h3>
          <p>${item.body}</p>
        </article>
      `,
    )
    .join("");
}

function createMetricRow({ name, valueText, fillWidth, fillStyle, meta }) {
  return `
    <article class="metric-row">
      <div class="metric-head">
        <p class="metric-name">${name}</p>
        <p class="metric-value">${valueText}</p>
      </div>
      <div class="metric-track">
        <div class="metric-fill" style="width: ${fillWidth}%; background: ${fillStyle};"></div>
      </div>
      <div class="metric-meta">
        ${meta.map((item) => `<span class="metric-badge">${item}</span>`).join("")}
      </div>
    </article>
  `;
}

function renderCategoryChart() {
  const container = document.querySelector("#category-chart");
  if (!container) {
    return;
  }

  const maxValue = Math.max(...dashboardData.categoryCompletion.map((item) => item.completionRate));
  container.innerHTML = dashboardData.categoryCompletion
    .map((item) =>
      createMetricRow({
        name: item.category,
        valueText: formatPercent(item.completionRate),
        fillWidth: (item.completionRate / maxValue) * 100,
        fillStyle: "linear-gradient(90deg, #356dff, #6d95ff)",
        meta: [
          `완료 ${formatNumber(item.completedOrders)} / ${formatNumber(item.totalOrders)}건`,
          `평균 객단가 ${formatCurrency(item.avgAmount)}`,
        ],
      }),
    )
    .join("");
}

function renderEntryChart() {
  const container = document.querySelector("#entry-chart");
  if (!container) {
    return;
  }

  const maxValue = Math.max(...dashboardData.entryConversion.map((item) => item.conversionRate));
  container.innerHTML = dashboardData.entryConversion
    .map((item) =>
      createMetricRow({
        name: item.entryPage,
        valueText: formatPercent(item.conversionRate),
        fillWidth: (item.conversionRate / maxValue) * 100,
        fillStyle: "linear-gradient(90deg, #1da89b, #58cfbf)",
        meta: [
          `세션 ${formatNumber(item.totalSessions)}회`,
          `평균 체류 ${formatDuration(item.avgSessionDuration)}`,
          `구매 ${formatNumber(item.completedPurchases)}건`,
        ],
      }),
    )
    .join("");
}

function renderDeviceChart() {
  const container = document.querySelector("#device-chart");
  if (!container) {
    return;
  }

  container.innerHTML = dashboardData.deviceConversion
    .map(
      (item, index) => `
        <article class="device-card">
          <div class="device-rank">
            <h3>${item.device}</h3>
            <span class="rank-chip">${index + 1}위 · ${item.badge}</span>
          </div>
          <p class="device-rate">${formatPercent(item.conversionRate)}</p>
          <p class="device-meta">세션 ${formatNumber(item.totalSessions)}회 · 구매 ${formatNumber(
            item.completedPurchases,
          )}건</p>
          <p class="device-meta">평균 체류 ${formatDuration(item.avgSessionDuration)}</p>
        </article>
      `,
    )
    .join("");
}

function renderAgeChart() {
  const container = document.querySelector("#age-chart");
  if (!container) {
    return;
  }

  const maxValue = Math.max(...dashboardData.ageChurn.map((item) => item.churnRate));
  container.innerHTML = dashboardData.ageChurn
    .map((item) =>
      createMetricRow({
        name: item.ageGroup,
        valueText: formatPercent(item.churnRate),
        fillWidth: (item.churnRate / maxValue) * 100,
        fillStyle: "linear-gradient(90deg, #e16357, #f09c7e)",
        meta: [
          `이탈 ${formatNumber(item.churnedUsers)} / ${formatNumber(item.totalUsers)}명`,
          `평균 구매 ${item.avgPurchaseCount.toFixed(2)}회`,
        ],
      }),
    )
    .join("");
}

function renderLifecycleSegments() {
  const stack = document.querySelector("#segment-stack");
  const legend = document.querySelector("#segment-legend");

  if (!stack || !legend) {
    return;
  }

  const total = dashboardData.lifecycleSegments.reduce((sum, item) => sum + item.count, 0);

  stack.innerHTML = dashboardData.lifecycleSegments
    .map(
      (item) => `
        <div
          class="segment-slice"
          style="width: ${(item.count / total) * 100}%; background: ${item.color};"
          title="${item.name} ${formatNumber(item.count)}명"
        ></div>
      `,
    )
    .join("");

  legend.innerHTML = dashboardData.lifecycleSegments
    .map(
      (item) => `
        <article class="segment-item">
          <div class="segment-left">
            <span class="segment-dot" style="background: ${item.color};"></span>
            <span class="segment-name">${item.name}</span>
          </div>
          <span class="segment-meta">${formatNumber(item.count)}명 · ${((item.count / total) * 100).toFixed(
            1,
          )}%</span>
        </article>
      `,
    )
    .join("");
}

function exitSignal(exitPage) {
  if (exitPage === "완료") {
    return {
      label: "완료 전환",
      className: "signal-success",
    };
  }

  if (exitPage === "결제" || exitPage === "장바구니") {
    return {
      label: "고의도 이탈",
      className: "signal-alert",
    };
  }

  return {
    label: "초기 이탈",
    className: "signal-alert",
  };
}

function renderExitTable() {
  const container = document.querySelector("#exit-table-body");
  if (!container) {
    return;
  }

  const rows = [...dashboardData.exitAnalysis].sort((left, right) => {
    if (left.exitPage === "완료") {
      return 1;
    }

    if (right.exitPage === "완료") {
      return -1;
    }

    return right.totalSessions - left.totalSessions;
  });

  container.innerHTML = rows
    .map((item) => {
      const signal = exitSignal(item.exitPage);
      return `
        <tr>
          <td><strong>${item.exitPage}</strong></td>
          <td>${formatNumber(item.totalSessions)}회</td>
          <td>${formatDuration(item.avgSessionDuration)}</td>
          <td>${formatNumber(item.completedPurchases)}건</td>
          <td><span class="signal-pill ${signal.className}">${signal.label}</span></td>
        </tr>
      `;
    })
    .join("");
}

function initializeDashboard() {
  renderKpis();
  renderMonthlyChart();
  renderMonthlyMetrics();
  renderMonthlyInsight();
  renderInsights();
  renderCategoryChart();
  renderEntryChart();
  renderDeviceChart();
  renderAgeChart();
  renderLifecycleSegments();
  renderExitTable();
}

let resizeTimer;
window.addEventListener("resize", () => {
  window.clearTimeout(resizeTimer);
  resizeTimer = window.setTimeout(renderMonthlyChart, 120);
});

document.addEventListener("DOMContentLoaded", initializeDashboard);
