import {useEffect,useState} from 'react';
import {useMachine} from './store';
import {audio} from './audio';
export default function Protocol(){const [revealed,setRevealed]=useState(false);const m=useMachine();useEffect(()=>{audio.tone('warning');const t=setTimeout(()=>{setRevealed(true);audio.tone('meow');},2000);return()=>clearTimeout(t);},[]);return <div className="ending protocol" role="dialog" aria-label="Toffee protocol"><p className="eyebrow">UNKNOWN ACTIVITY DETECTED</p><p>PRIMARY ASSET APPROACHING</p>{revealed&&<><div className="protocol-cat">⌁</div><h1>TOFFEE</h1><p>CLASSIFICATION: FELINE</p><p>SYSTEM ACCESS: APPARENTLY UNRESTRICTED</p><p>PRIORITY: ABSURDLY HIGH</p><button className="action" onClick={()=>m.set({flash:''})}>Accept feline authority ↗</button></>}</div>;}
