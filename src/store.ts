import {create} from 'zustand';
import {persist} from 'zustand/middleware';
import {audio} from './audio';
import {story} from './data';
type State={worldLight:"day"|"night";landmark:string;mode:string; selected:string; camera:string; panel:string; phase:number; admin:boolean; god:boolean; toffee:boolean; eggs:string[]; sightings:string[]; intro:boolean; history:string[]; events:string[]; flash:string; ending:boolean; bearAt:number; set:(v:Partial<State>)=>void; discover:(s:string)=>void; sight:(s:string)=>void; advance:()=>void; command:(s:string)=>void; reset:()=>void};
const initial={worldLight:'night' as 'day'|'night',landmark:'',mode:'MAP',selected:'004',camera:'0031',panel:'',phase:0,admin:false,god:false,toffee:false,eggs:[],sightings:[],intro:false,history:['SECURE SHELL ESTABLISHED','Type HELP to explore available commands.'],events:['NETWORK MODEL ONLINE','PRIMARY ASSETS ACQUIRED','IRRELEVANT NUMBER RECEIVED · 728-401-992'],flash:'',ending:false,bearAt:0};
export const useMachine=create<State>()(persist((set,get)=>({ ...initial,set,discover:s=>{if(!get().eggs.includes(s)){set({eggs:[...get().eggs,s]});audio.tone('unlock');}},sight:s=>{const sightings=[...new Set([...get().sightings,s])];set({sightings});if(sightings.length>=5){get().discover('TOFFEE PROTOCOL');set({flash:'TOFFEE PROTOCOL · ACCESS APPARENTLY UNRESTRICTED'});}},advance:()=>{let phase=Math.min(get().phase+1,8);set({phase,events:[story[phase].title,...get().events].slice(0,30)});audio.tone(phase>=5?'warning':'click');if(phase===8)get().discover('VIOLETA');},command:raw=>{
const s=raw.trim().toUpperCase();if(!s)return;let reply='COMMAND NOT RECOGNISED · Type HELP.';const a=get();audio.tone('key');
const replies:Record<string,string>={HELP:'COMMANDS: STATUS · ASSETS · CAMERAS · NUMBERS · EVENTS · NETWORK · SIMULATE · INVESTIGATE · FIND TOFFEE · TOFFEE MODE · ARCHIVE · ADMIN\nArchive keys: FINCH · REESE · ROOT · SHAW · BEAR · FUSCO · CARTER · CONTROL · SAMARITAN\nNavigation: MAP · POV · CLEAR · EXIT',STATUS:`CORE ONLINE · ASSETS PROTECTED · STORY ${story[a.phase].state}`,FINCH:'ARCHIVE MATCH: HAROLD FINCH\nSTATUS UNKNOWN · ACCESS RESTRICTED\nFILE: wren.memory.041',ROOT:'ANALOG INTERFACE DETECTED\nACCESS PATTERN RECOGNISED\nCAN YOU HEAR ME?',SHAW:'SAMEEN SHAW · GOVERNMENT ASSET\nSTATUS ACTIVE · PATTERN UNPREDICTABLE\nTHREAT RESPONSE HIGH',REESE:'JOHN REESE · PRIMARY ASSET\nLOCATION REDACTED · MISSION ACTIVE\nSIGNATURE LOST',BEAR:'ENTITY CANINE · LOYALTY ABSOLUTE\nCOMMAND RESPONSE HIGH · GOOD BOY CONFIRMED',FUSCO:'LIONEL FUSCO · DETECTIVE\nLOYALTY: MORE THAN HE ADMITS.',CARTER:'JOSS CARTER · ARCHIVE PRESERVED\nINTEGRITY: UNCOMPROMISED.',CONTROL:'GOVERNMENT INTERFACE · ACCESS DENIED\nBLUE CHANNEL REMAINS READ ONLY.',SAMARITAN:'EXTERNAL ASI SIGNATURE DETECTED\nUNKNOWN SYSTEM ACCESS · COUNTERMEASURE ACTIVE\nSIGNATURE LOST',TOFFEE:'TOFFEE · FELINE · CONFIDENCE 99.8%\nCOMMAND RESPONSE OPTIONAL · RECOMMENDATION: PROVIDE TREATS.','FIND TOFFEE':'SEARCHING... FELINE SIGNATURE DETECTED\nLIKELY LOCATIONS: SOFA · WINDOW · BED · KEYBOARD\nCURRENT ACTIVITY CLASSIFIED\nRECOMMENDATION: PROVIDE TREATS.',FAMILY:'ALL PRIMARY ASSETS PRESENT\nALEXANDER SAFE · VICTOR SAFE · BORIS SAFE\nTOFFEE ASLEEP\nCORRECTION: PRETENDING TO BE ASLEEP.',PIZZA:'PRIMARY ASSET DISPUTE: VICTOR + BORIS\nRESOLUTION PROBABILITY 12%\nRECOMMENDED ACTION: PIZZA.'};
if(replies[s])reply=replies[s];
if(['FINCH','ROOT','SHAW','REESE','BEAR','FUSCO','CARTER','CONTROL','SAMARITAN','FAMILY','PIZZA'].includes(s))a.discover(s);
if(s==='BEAR')set({bearAt:Date.now()});
if(s.includes('TOFFEE')&&a.bearAt&&Date.now()-a.bearAt<30000)reply+='\nCROSS-SPECIES ANALYSIS · TOFFEE WINS.';
if(s==='TOFFEE'||s==='FIND TOFFEE'){set({selected:'004'});a.sight('terminal');}
if(s==='ROOT'||s==='SAMARITAN'){set({flash:s});audio.tone(s==='ROOT'?'unlock':'warning');setTimeout(()=>set({flash:''}),3200);}
if(s==='REESE'){set({selected:'10982',mode:'POV'});setTimeout(()=>set({selected:'004'}),4500);}
if(s==='ADMIN'){set({admin:true,panel:'ADMIN'});a.discover('ADMIN');reply='ADMIN ACCESS GRANTED · WELCOME ALEXANDER\nHidden architecture available. Try GOD MODE.';audio.tone('unlock');}
if(s==='GOD MODE'){if(a.admin){set({god:!a.god,mode:'NETWORK'});a.discover('GOD MODE');reply='GOD MODE · INTERNAL ARCHITECTURE REVEALED';}else reply='ADMINISTRATOR REQUIRED';}
if(s==='TOFFEE MODE'){set({toffee:!a.toffee,selected:'004'});a.discover('TOFFEE MODE');reply='PRIMARY THREAT: VACUUM CLEANER\nHIGH VALUE TARGET: TREAT CONTAINER\nRUNNING 14,382 SIMULATIONS... REQUEST FOR FOOD\nPREDICTION FAILURE · RECALCULATING FELINE MODEL';audio.tone('meow');}
if(s==='INVESTIGATE'){a.advance();set({panel:'EVENTS'});reply=story[Math.min(a.phase+1,8)].title;}
if(s==='SIMULATE'){set({panel:'SIMULATIONS'});reply='BRANCH MODEL READY';}
if(['ASSETS','CAMERAS','NUMBERS','EVENTS','ARCHIVE','NETWORK'].includes(s)){set({panel:s});reply=`${s} MODULE ACQUIRED`;}
if(s==='MAP'||s==='POV'){set({mode:s,panel:''});reply=`${s} ENABLED`;}
if(s==='EXIT')set({panel:''});
if(s==='CLEAR'){set({history:[]});return;}
if(s==='FINAL'){const ready=['ADMIN','GOD MODE','ROOT','SAMARITAN','TOFFEE PROTOCOL','VIOLETA'].every(e=>a.eggs.includes(e));if(ready){set({ending:true});a.discover('FINAL');reply='SYSTEM ARCHIVE COMPLETE';}else reply='ARCHIVE INCOMPLETE · Required: administrator, internal architecture, analog interface, external signature, feline protocol and resolved investigation.';}
set({history:[...get().history,`> ${s}`,reply].slice(-100)});
},reset:()=>set({...initial,intro:true})}),{name:'machine-primary-assets-v1',partialize:s=>({phase:s.phase,admin:s.admin,eggs:s.eggs,sightings:s.sightings,intro:s.intro,god:s.god,worldLight:s.worldLight})}));


