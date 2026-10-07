async (page) => {
 const errors=[];page.on('pageerror',e=>errors.push(e.message));page.on('console',e=>{if(e.type()==='error'||e.type()==='warning')errors.push(e.text());});
 await page.reload();await page.setViewportSize({width:1440,height:900});
 await page.getByRole('button',{name:'CITY MAP',exact:true}).click();
 await page.emulateMedia({reducedMotion:'no-preference'});
 await page.getByRole('button',{name:'Track TOFFEE',exact:true}).waitFor(); await page.waitForTimeout(700); await page.screenshot({path:'output/playwright/desktop-production.png'});
 await page.getByRole('button',{name:'TERMINAL 07',exact:true}).click();
 const input=page.getByRole('textbox',{name:'Terminal command'});await input.fill('ADMIN');await input.press('Enter');
 await page.getByRole('button',{name:'Enter GOD MODE'}).click();
 await page.getByRole('button',{name:'Close module'}).click(); await page.waitForTimeout(700); await page.screenshot({path:'output/playwright/god-mode.png'});
 await page.getByRole('button',{name:'MACHINE POV',exact:true}).click();
 await page.getByRole('button',{name:'TERMINAL 07',exact:true}).click();await input.fill('GOD MODE');await input.press('Enter');
 await page.getByRole('button',{name:'Close module'}).click();
 await page.keyboard.press('p');await page.keyboard.press('`');if(!await input.isVisible())throw new Error('keyboard terminal');await page.keyboard.press('Escape');
 await page.getByRole('button',{name:'728 — 401 — 992',exact:true}).click();
 if(!await page.getByRole('heading',{name:'ELIAS WARD'}).isVisible())throw new Error('case module');
 await page.getByRole('button',{name:'391-882-047',exact:true}).click();if(!await page.getByRole('heading',{name:'MARA ELLIS'}).isVisible())throw new Error('case navigation');
 await page.getByRole('button',{name:'Close module'}).click();
 await page.setViewportSize({width:390,height:844});await page.screenshot({path:'output/playwright/mobile-production.png'});
 await page.getByRole('button',{name:'NUMBER RECEIVED / 728-401-992 ↗',exact:true}).click();if(!await page.getByRole('heading',{name:'ELIAS WARD'}).isVisible())throw new Error('mobile cases');
 const fallback=await page.context().newPage();await fallback.addInitScript(()=>{const original=HTMLCanvasElement.prototype.getContext;HTMLCanvasElement.prototype.getContext=function(type,...args){if(type==='webgl'||type==='webgl2')return null;return original.call(this,type,...args);};});
 await fallback.goto('http://127.0.0.1:4173/');await fallback.getByText('2D NETWORK · SIMPLIFIED RENDERING').waitFor();await fallback.getByRole('button',{name:'TERMINAL 07',exact:true}).click();await fallback.getByRole('textbox',{name:'Terminal command'}).fill('STATUS');await fallback.getByRole('textbox',{name:'Terminal command'}).press('Enter');if(!await fallback.getByRole('log').innerText().then(t=>t.includes('CORE ONLINE')))throw new Error('fallback terminal');await fallback.screenshot({path:'output/playwright/fallback.png'});await fallback.close();
 if(errors.length)throw new Error(errors.join('\n'));
 await page.setViewportSize({width:1440,height:900});await page.getByRole('button',{name:'Close module'}).click();
 const fps=await page.evaluate(()=>new Promise(resolve=>{let first=performance.now(),frames=0;function tick(){frames++;if(performance.now()-first>2000)resolve(Math.round(frames*1000/(performance.now()-first)));else requestAnimationFrame(tick);}requestAnimationFrame(tick);}));
 return {productionConsoleErrors:errors,keyboard:true,cases:true,mobile:true,webglFallback:true,observedAnimationFps:fps};
}

