// Render SVG figures to a PNG contact sheet so you can look at them.
// Usage: PWPATH=$(npm root -g)/playwright node scripts/render_svgs.js out.png a.svg b.svg ...
const { chromium } = require(process.env.PWPATH || "playwright");
const fs = require("fs");
(async () => {
  const [out, ...files] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 820, height: 500 * files.length + 20 } });
  const html = files.map((f) => `<img style="display:block;border:1px solid #999;margin:4px" width="800" src="data:image/svg+xml;charset=utf-8,${encodeURIComponent(fs.readFileSync(f, "utf8"))}">`).join("");
  await p.setContent(`<body style="margin:0;background:#fff">${html}</body>`);
  await p.waitForTimeout(300);
  await p.screenshot({ path: out, fullPage: true });
  await b.close();
  console.log("wrote", out);
})();
