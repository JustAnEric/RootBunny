const audio = document.querySelector('audio');

window.addEventListener('pywebviewready', ()=>{
    audio.addEventListener('timeupdate', async(ev)=>{
        await pywebview.api.timeupdate(audio.currentTime,audio.duration);
    });

    audio.addEventListener('ended', async(ev)=>{
        await pywebview.api.audioFinished();
    });
});