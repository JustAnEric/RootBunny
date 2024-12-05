window.rootbunny={};
window.rootbunny.app={audio:{play:function(context,URL,funcToRunOnAudioFinish,funcToRunOnAudioTimeUpdate){return(pywebview.api.on('audio:player/open',context,URL,funcToRunOnAudioFinish,funcToRunOnAudioTimeUpdate));}},audioPlaybackAllowed:true};
window.rootbunny.bridge={};
window.rootbunny.isadmin=false;