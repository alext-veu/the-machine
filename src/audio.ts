class AudioController {
 context:AudioContext|null=null; master:GainNode|null=null; ambient:GainNode|null=null; volume=.3; effects=.55; enabled=false; last=0;
 async enable(){try{this.context??=new AudioContext();await this.context.resume();if(!this.master){this.master=this.context.createGain();this.master.connect(this.context.destination);this.ambient=this.context.createGain();this.ambient.gain.value=.035;this.ambient.connect(this.master);[55,82.5].forEach(f=>{const o=this.context!.createOscillator();o.frequency.value=f;o.type='sine';o.connect(this.ambient!);o.start();});}this.enabled=true;this.setVolume(this.volume);}catch{this.enabled=false;}}
 mute(){this.enabled=false;if(this.master)this.master.gain.setTargetAtTime(0,this.context!.currentTime,.1);}
 setVolume(v:number){this.volume=v;if(this.master)this.master.gain.setTargetAtTime(this.enabled?v:0,this.context!.currentTime,.08);}
 setAmbience(v:number){if(this.ambient)this.ambient.gain.setTargetAtTime(v*.07,this.context!.currentTime,.1);}
 tone(kind='click'){if(!this.enabled||!this.context||!this.master||Date.now()-this.last<70)return;this.last=Date.now();const c=this.context,o=c.createOscillator(),g=c.createGain();const f=kind==='warning'?95:kind==='unlock'?660:kind==='meow'?540:kind==='key'?240:420;o.type=kind==='warning'?'triangle':'sine';o.frequency.setValueAtTime(f,c.currentTime);o.frequency.exponentialRampToValueAtTime(kind==='meow'?260:f*.65,c.currentTime+.18);g.gain.setValueAtTime(0,c.currentTime);g.gain.linearRampToValueAtTime(.12*this.effects,c.currentTime+.008);g.gain.exponentialRampToValueAtTime(.001,c.currentTime+.3);o.connect(g);g.connect(this.master);o.start();o.stop(c.currentTime+.32);o.onended=()=>{o.disconnect();g.disconnect();};}
}
export const audio=new AudioController();
