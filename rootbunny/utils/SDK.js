window.rootbunny={};
window.rootbunny.app={audio:{play:async function(context,URL,funcToRunOnAudioFinish,funcToRunOnAudioTimeUpdate){return await pywebview.api.on('audio:player/open',context,URL,funcToRunOnAudioFinish,funcToRunOnAudioTimeUpdate);},stateChange:function(o){console.log('Audio State Change', o);},timeChange:function(o){console.log('Audio Time Change', o);},getStates:async function(context){return await pywebview.api.on('audio:player/getContext',context);},pauseAudio:async function(context,index){return await pywebview.api.on('audio:player/pauseAudio',context,index);},resumeAudio:async function(context,index){return await pywebview.api.on('audio:player/resumeAudio',context,index);},close:async function(context,index){return await pywebview.api.on('audio:player/close',context,index);},playBase64:async function(context,b64,codec,funcToRunOnAudioFinish,funcToRunOnAudioTimeUpdate){return await pywebview.api.on('audio:player/playBase64',context,b64,codec,funcToRunOnAudioFinish,funcToRunOnAudioTimeUpdate);},getInfo:async function(context,index){return await pywebview.api.on('audio:player/getInfo',context,index);},setInfo:async function(context,index,o){return await pywebview.api.on('audio:player/setInfo',context,index,o);}},audioPlaybackAllowed:true,interface:{home:function(){return(pywebview.api.on('interface:home'));}, load:function(app_name){return(pywebview.api.on('interface:apps/open',app_name));},init:function(){return(pywebview.api.on('interface:apps/load/init'))},apps:async function(){return(await fetch(`http://127.0.0.1:4000/main/app_data`).then(resp => resp.json())).apps}},appSwitchingAllowed:true};
window.rootbunny.bridge={};
window.rootbunny.isadmin=false;

// rootbunny icon
(async()=>{
    const rbi = document.createElement('div');
    rbi.className = 'rootb rootbunny-icon';
    rbi.addEventListener('click', async()=>{
        await window.rootbunny.app.interface.home();
    });
    document.body.appendChild(rbi);
    // apply stylesheet
    const rbissh = document.createElement('style');
    rbissh.innerText = ".rootb.rootbunny-icon { background-image: url(/assets/splash/logos/RootBunny.png); background-size: cover; width: 74px; height: 74px; position: fixed; top: 14px; left: 14px; z-index: 9999999999; }";
    document.head.appendChild(rbissh);
})();

// dispatch event
window.dispatchEvent(new Event('rootbunnyready'));