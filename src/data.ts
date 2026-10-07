export type Entity = {id:string; name:string; type:string; color:string; position:[number,number,number]; detail:string; risk:number};
export const entities:Entity[]=[
{id:'001',name:'ALEXANDER',type:'ADMINISTRATOR',color:'#d7ba67',position:[-7,1,6],detail:'PRIMARY ASSET · TRUST MAXIMUM',risk:0},
{id:'002',name:'VICTOR',type:'PRIMARY ASSET',color:'#d7ba67',position:[7,1,2],detail:'PROTECTED · HIGH TRUST',risk:0},
{id:'003',name:'BORIS',type:'PRIMARY ASSET',color:'#d7ba67',position:[2,1,-8],detail:'PROTECTED · HIGH TRUST',risk:0},
{id:'004',name:'TOFFEE',type:'FELINE ASSET',color:'#d7ba67',position:[-3,1,-1],detail:'STRATEGIC NAPPING ASSET · BEHAVIOUR UNRELIABLE',risk:4},
{id:'005',name:'VIOLETA',type:'MONITORED SUBJECT',color:'#e0e1dc',position:[10,1,-8],detail:'OBSERVATION CONTINUES',risk:7},
{id:'10982',name:'ENTITY_10982',type:'IRRELEVANT',color:'#e0e1dc',position:[-12,1,-9],detail:'PREDICTION MODEL STABLE',risk:3},
{id:'20117',name:'MUNICIPAL_17',type:'GOVERNMENT NODE',color:'#7a9fb8',position:[12,1,10],detail:'OFFICIAL SYSTEM · READ ONLY',risk:2}];
export const cameras=['0031','0117','2048','7721'];
export const districts=['MIDTOWN','LOWER EAST','WEST SECTOR','NORTH GRID'];
export const story=[
{state:'NORMAL',risk:7,title:'OBSERVATION CONTINUES',text:'The network is stable. An unclassified packet waits in the event archive.',action:'Inspect packet'},
{state:'ANOMALY_01',risk:14,title:'ENCRYPTED TRAFFIC',text:'A domestic node is transmitting at unusual intervals. Trace the source.',action:'Trace source'},
{state:'VIOLETA_DETECTED',risk:23,title:'CAM 0117 · SIGNAL LOST',text:'Violeta was observed near the disrupted camera. Correlation does not imply intent.',action:'Recover camera'},
{state:'CORRELATION',risk:41,title:'UNKNOWN NODE CONTACT',text:'Victor and Boris received identical encrypted messages. Toffee is asleep on the evidence.',action:'Correlate messages'},
{state:'THREAT_RISING',risk:57,title:'PROBABILITY CHANGED',text:'Three supply routes converge on one location. Administrator attention required.',action:'Analyse routes'},
{state:'CONTINGENCY',risk:73,title:'CONTINGENCY ACTIVE',text:'A Samaritan signature has been detected in a kitchen appliance. Run a counterfactual.',action:'Run counterfactual'},
{state:'SAMARITAN_SIGNAL',risk:81,title:'HIGH PRIORITY THREAT',text:'Violeta controls the supply chain. All biscuit containers are accounted for. None are accessible.',action:'Investigate container'},
{state:'INVESTIGATION',risk:81,title:'OPERATION: LAST BISCUIT',text:'The conspiracy is domestic. Violeta has hidden the biscuits before the family film night. Toffee has secured the cardboard box.',action:'Negotiate settlement'},
{state:'RESOLUTION',risk:4,title:'PRIMARY ASSETS PROTECTED',text:'Biscuits recovered. Violeta requests tea. Victor and Boris recommend pizza. Toffee declines to comment.',action:'Case resolved'}];
export const cases=[{number:'728-401-992',name:'ELIAS WARD',location:'LOWER EAST · PLATFORM 03',text:'A lost violin case was exchanged with a lunch box. Intercept the next train before a very disappointing concert.',risk:18}, {number:'391-882-047',name:'MARA ELLIS',location:'MIDTOWN · BOOKSHOP',text:'An overdue library book contains a forgotten birthday invitation. Reconnect two old friends before closing time.',risk:9}, {number:'620-173-558',name:'NOAH VALE',location:'WEST SECTOR · CROSSING',text:'A courier and a birthday cake are on a collision course with a closed street. Reroute the delivery.',risk:26}];
