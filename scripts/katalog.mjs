// Katalog HTML'ini A4 PDF olarak basar. Chromium disinda bagimlilik yok.
import {execFileSync} from 'node:child_process';import fs from 'node:fs';import path from 'node:path';
const root=process.cwd();const dir=path.join(root,'katalog');
const chrome=[process.env.CHROME_PATH,'/opt/pw-browsers/chromium-1194/chrome-linux/chrome','/usr/bin/chromium','/usr/bin/google-chrome']
  .find(p=>p&&fs.existsSync(p));
if(!chrome)throw new Error('Chromium bulunamadi. CHROME_PATH ile yolunu verin.');
const out=path.join(dir,'Global-Katalog-2026.pdf');
execFileSync(chrome,['--headless','--disable-gpu','--no-sandbox','--no-pdf-header-footer',
  '--run-all-compositor-stages-before-draw','--virtual-time-budget=25000',
  `--print-to-pdf=${out}`,'katalog.html'],{cwd:dir,stdio:'inherit'});
console.log(`Katalog hazir: ${out} (${(fs.statSync(out).size/1e6).toFixed(1)} MB)`);
