async (page) => {
 const results=[]; await page.emulateMedia({reducedMotion:"reduce"}); await page.evaluate(()=>localStorage.clear()); await page.reload(); await page.waitForTimeout(7500);
 const assert=(ok,label)=>{if(!ok)throw new Error(label);results.push(label);};
 await page.setViewportSize({width:1440,height:900});
 await page.getByRole('button',{name:/^TERMINAL(?: 07)?$/}).click();
 const command=async text=>{if(!await page.getByRole('textbox',{name:'Terminal command'}).isVisible())await page.getByRole('button',{name:/^TERMINAL(?: 07)?$/}).click();await page.getByRole('textbox',{name:'Terminal command'}).fill(text);await page.getByRole('textbox',{name:'Terminal command'}).press('Enter');};
 await command('HELP');assert(await page.getByRole('log').innerText().then(t=>t.includes('COMMANDS:')),'terminal help');
 for(const key of ['FINCH','ROOT','SHAW','REESE','BEAR','TOFFEE','FUSCO','CARTER','CONTROL','SAMARITAN'])await command(key);
 assert(await page.getByRole('log').innerText().then(t=>t.includes('TOFFEE WINS')),'Bear + Toffee crossover');
 await command('GOD MODE');assert(await page.getByRole('log').innerText().then(t=>t.includes('ADMINISTRATOR REQUIRED')),'GOD MODE access gate');
 await command('ADMIN');assert(await page.getByText('WELCOME ALEXANDER / ACCESS GRANTED').isVisible(),'admin unlock');
 await command('GOD MODE');assert(await page.getByRole('heading',{name:'Inside the Machine'}).isVisible(),'God mode rendering');
 await command('TOFFEE MODE');assert(await page.getByRole('heading',{name:'Inside the Machine'}).isVisible(),'Toffee mode command');
 await page.getByRole('button',{name:'Close module'}).click();
 await page.getByRole('button',{name:'Track TOFFEE',exact:true}).click();
 await page.getByRole('button',{name:'ASSETS 03',exact:true}).click();
 await page.getByRole('button',{name:/TOFFEE FELINE ASSET TRACKED/}).click();
 await page.getByRole('button',{name:'CAMERAS 04',exact:true}).click();
 await page.getByRole('button',{name:'Inspect feline silhouette'}).click();
 await page.getByRole('button',{name:'NETWORK 02',exact:true}).click();
 await page.getByRole('button',{name:'Inspect hidden paw node'}).click();
 assert(await page.evaluate(()=>JSON.parse(localStorage.getItem('machine-primary-assets-v1')).state.eggs.includes('TOFFEE PROTOCOL')),'feline protocol unlock');
 await page.getByRole('button',{name:'Accept feline authority ↗'}).waitFor(); await page.getByRole('button',{name:'Accept feline authority ↗'}).click(); await page.getByRole('button',{name:'EVENTS 05',exact:true}).click();
 for(const action of ['Inspect packet','Trace source','Recover camera','Correlate messages','Analyse routes','Run counterfactual','Investigate container','Negotiate settlement'])await page.getByRole('button',{name:action,exact:true}).click();
 assert(await page.getByRole('heading',{name:'PRIMARY ASSETS PROTECTED'}).isVisible(),'full Violeta investigation');
 await command('FINAL');assert(await page.getByRole('dialog',{name:'Final archive'}).isVisible(),'final secret gated unlock');
 await page.getByRole('button',{name:'Return to observation'}).waitFor({timeout:15000});await page.getByRole('button',{name:'Return to observation'}).click();
 await page.reload();assert(await page.getByText('ADMIN ACCESS',{exact:true}).isVisible()||await page.getByText('GOD MODE ACTIVE',{exact:true}).isVisible(),'persistent admin and intro');
 assert(await page.evaluate(()=>JSON.parse(localStorage.getItem('machine-primary-assets-v1')).state.phase===8),'persistent story');
 await page.getByRole('button',{name:'Enable sound'}).click();assert(await page.getByRole('button',{name:'Mute sound'}).isVisible(),'audio gesture unlock');await page.getByRole('button',{name:'Mute sound'}).click();assert(await page.getByRole('button',{name:'Enable sound'}).isVisible(),'mute');
 await page.getByRole('button',{name:'CAMERAS 04',exact:true}).click();for(const c of ['0031','0117','2048','7721']){await page.getByRole('button',{name:c,exact:true}).click();assert(await page.getByText('● REC · CAM '+c).isVisible(),'camera '+c);}
 await page.getByRole('button',{name:'Close module'}).click();await page.getByRole('button',{name:'MACHINE POV',exact:true}).click();assert(await page.getByRole('button',{name:'MACHINE POV',exact:true}).getAttribute('class').then(c=>c==='active'),'POV controls');
 await command('SIMULATE');await page.getByRole('button',{name:'Run simulation',exact:true}).click();await page.getByText(/PREFERRED BRANCH: INTERCEPT ROUTE/).waitFor();results.push('simulation result');
 await page.getByRole('button',{name:'ADMIN 08',exact:true}).click();await page.getByRole('button',{name:'Reset experience',exact:true}).click();await page.getByRole('button',{name:'Cancel reset',exact:true}).click();assert(await page.getByText('WELCOME ALEXANDER / ACCESS GRANTED').isVisible(),'reset cancellation');await page.getByRole('button',{name:'Reset experience',exact:true}).click();await page.getByRole('button',{name:'Confirm reset — erase local discoveries',exact:true}).click();assert(await page.evaluate(()=>JSON.parse(localStorage.getItem('machine-primary-assets-v1')).state.phase===0),'reset clears progress');
 await page.setViewportSize({width:390,height:844});await page.getByRole('button',{name:/^TERMINAL(?: 07)?$/}).click();await command('FIND TOFFEE');assert(await page.getByRole('log').innerText().then(t=>t.includes('PROVIDE TREATS')),'mobile terminal');
 assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'mobile no horizontal overflow');
 await page.screenshot({path:'output/playwright/mobile.png'});
 await page.emulateMedia({reducedMotion:'reduce'});await page.getByRole('button',{name:'Close module'}).click();results.push('reduced motion renders');
 await page.setViewportSize({width:1440,height:900});await page.screenshot({path:'output/playwright/desktop-final.png'});
 console.log(JSON.stringify(results));
}




