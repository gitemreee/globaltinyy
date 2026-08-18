import fs from 'node:fs';import path from 'node:path';
const root=process.cwd();
export const site=JSON.parse(fs.readFileSync(path.join(root,'data/site.json'),'utf8'));
// Hedef platform: DEPLOY_TARGET ile secilir. Netlify build ortaminda NETLIFY=true otomatik gelir.
export const target=(process.env.DEPLOY_TARGET||(process.env.NETLIFY?'netlify':'pages')).toLowerCase();
const t=site.targets[target];
if(!t)throw new Error(`Bilinmeyen DEPLOY_TARGET: "${target}". Secenekler: ${Object.keys(site.targets).join(', ')}`);
// Canonical/sitemap adresi. Netlify build'inde URL degiskeni projenin canli adresini verir.
export const siteUrl=(process.env.SITE_URL||process.env.URL||t.siteUrl).replace(/\/+$/,'');
// basePath her zaman "/" ile baslar ve biter: "/" (Netlify) veya "/globaltinyy/" (Pages alt dizini).
const raw=(process.env.BASE_PATH??t.basePath).replace(/^\/+|\/+$/g,'');
export const basePath=raw?`/${raw}/`:'/';
