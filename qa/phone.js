async(page)=>{
 const browser=page.context().browser();const results=[];
 for(const viewport of [{width:393,height:852},{width:430,height:932},{width:402,height:874},{width:440,height:956},{width:852,height:393}]){
  const context=await browser.newContext({viewport,isMobile:true,hasTouch:true,deviceScaleFactor:3,reducedMotion:'reduce'});const phone=await context.newPage();const errors=[];phone.on('pageerror',e=>errors.push(e.message));
  await phone.addInitScript(()=>localStorage.setItem('machine-primary-assets-v1',JSON.stringify({state:{intro:true},version:0})));
  await phone.goto('http://127.0.0.1:4173/');await phone.getByRole('button',{name:'Track TOFFEE',exact:true}).waitFor();
  const buttons=phone.locator('.rail > button');for(let i=0;i<8;i++){const b=await buttons.nth(i).boundingBox();if(!b||b.x<0||b.x+b.width>viewport.width+1||b.y+b.height>viewport.height||b.width<44||b.height<44)throw new Error('Dock bounds '+JSON.stringify({viewport,index:i,b}));}
  await phone.getByRole('button',{name:'TERMINAL',exact:true}).tap();const input=phone.getByRole('textbox',{name:'Terminal command'});await input.fill('FIND TOFFEE');await input.press('Enter');if(!(await phone.getByRole('log').innerText()).includes('PROVIDE TREATS'))throw new Error('phone terminal');if(await input.evaluate(e=>parseFloat(getComputedStyle(e).fontSize))<16)throw new Error('Safari input zoom');
  await phone.screenshot({path:`output/playwright/phone-terminal-${viewport.width}.png`});await phone.getByRole('button',{name:'Close module'}).tap();
  await phone.getByRole('button',{name:'CAMERAS',exact:true}).tap();await phone.getByRole('button',{name:'7721',exact:true}).tap();await phone.getByText('● REC · CAM 7721').waitFor();await phone.getByRole('button',{name:'Close module'}).tap();
  if(viewport.height>500){await phone.getByRole('combobox',{name:'Select district'}).selectOption('2');await phone.getByRole('button',{name:'NUMBER RECEIVED / 728-401-992 ↗',exact:true}).tap();await phone.getByRole('heading',{name:'ELIAS WARD'}).waitFor();await phone.getByRole('button',{name:'Close module'}).tap();await phone.screenshot({path:`output/playwright/phone-city-${viewport.width}.png`});
   await phone.getByRole('button',{name:'TERMINAL',exact:true}).tap();await phone.evaluate(()=>{document.documentElement.style.setProperty('--phone-height','430px');document.documentElement.classList.add('keyboard-open');});const keyboardInput=await input.boundingBox();if(!keyboardInput||keyboardInput.y+keyboardInput.height>430)throw new Error('keyboard obscures terminal');await phone.screenshot({path:`output/playwright/phone-keyboard-${viewport.width}.png`});
  }
  if(await phone.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw new Error('horizontal overflow');if(errors.length)throw new Error(errors.join('\n'));results.push({viewport,allModulesVisible:true,terminal:true,cameras:true,errors});await context.close();
 }
 return results;
}
