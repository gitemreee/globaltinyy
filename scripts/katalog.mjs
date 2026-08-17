// Katalogları A4 PDF olarak basar. Chromium disinda bagimlilik yok.
import {execFileSync} from 'node:child_process';import fs from 'node:fs';import path from 'node:path';
const dir=path.join(process.cwd(),'katalog');
const chrome=[process.env.CHROME_PATH,'/opt/pw-browsers/chromium-1194/chrome-linux/chrome','/usr/bin/chromium','/usr/bin/google-chrome']
  .find(p=>p&&fs.existsSync(p));
if(!chrome)throw new Error('Chromium bulunamadi. CHROME_PATH ile yolunu verin.');
const docs=[
  ['tiny-house.html','Global-TinyHouse-Moduler-Yapilar.pdf'],
  ['mobilya.html','Global-Ic-Mekan-Ahsap-Mobilya.pdf'],
];
// --allow-file-access-from-files: harici base.css'in file:// uzerinden okunmasi icin.
for(const [src,out] of docs){
  const target=path.join(dir,out);
  execFileSync(chrome,['--headless','--disable-gpu','--no-sandbox','--no-pdf-header-footer',
    '--allow-file-access-from-files','--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=25000',`--print-to-pdf=${target}`,src],{cwd:dir,stdio:'inherit'});
  console.log(`${out} — ${(fs.statSync(target).size/1e6).toFixed(1)} MB`);
}
