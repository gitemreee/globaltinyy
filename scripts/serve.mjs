import http from 'node:http';import fs from 'node:fs';import path from 'node:path';import {execSync} from 'node:child_process';
import {basePath,target,siteUrl} from './config.mjs';
execSync('node scripts/build.mjs',{stdio:'inherit'});
const root=path.join(process.cwd(),'dist');const port=Number(process.env.PORT||4173);
const types={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.webp':'image/webp','.xml':'application/xml','.txt':'text/plain; charset=utf-8','.json':'application/json'};
http.createServer((req,res)=>{
  let p=decodeURIComponent(req.url.split('?')[0]);
  // Yayin kokunu ("/globaltinyy/" gibi) kirp; dist icinde her sey koke gore durur.
  if(basePath!=='/'&&p.startsWith(basePath.slice(0,-1)))p=p.slice(basePath.length-1)||'/';
  let f=path.join(root,path.normalize(p));
  if(!f.startsWith(root))return res.writeHead(403).end('Forbidden');
  if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
  let code=200;
  if(!fs.existsSync(f)){code=404;f=path.join(root,'404.html')}
  res.writeHead(code,{'content-type':types[path.extname(f)]||'application/octet-stream'});
  fs.createReadStream(f).pipe(res);
}).listen(port,()=>console.log(`\ntarget=${target} | canonical=${siteUrl}\nhttp://localhost:${port}${basePath}`));
