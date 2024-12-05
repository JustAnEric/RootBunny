window.rootbunny={};
window.rootbunny.app={audio:{play:function(context,URL,funcToRunOnAudioFinish,funcToRunOnAudioTimeUpdate){return(pywebview.api.on('audio:player/open',context,URL,funcToRunOnAudioFinish,funcToRunOnAudioTimeUpdate));}},audioPlaybackAllowed:true,interface:{load:function(app_name){return(pywebview.api.on('interface:apps/open',app_name));},init:function(){return(pywebview.api.on('interface:apps/load/init'))}},appSwitchingAllowed:true};
window.rootbunny.bridge={};
window.rootbunny.isadmin=false;