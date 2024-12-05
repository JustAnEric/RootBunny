'use strict';

function a(num){
    if(num<10){
        return("0"+num);
    }
    return num;
};
function b(){
    var p={d:new Date()};
    p.h=a(p.d.getHours());
    p.m=a(p.d.getMinutes());
    p.s=a(p.d.getSeconds());
    return(p);
}
setInterval(()=>{
    let d=b();
    document.querySelector('.time').innerHTML=d.h+':'+d.m+':'+d.s;
},1);
setTimeout(function(){
    document.querySelector('.android-auto-home').classList.add('pull');
},5000);

window.addEventListener('pywebviewready',()=>{
    const apps = document.querySelectorAll('.android-auto-home .app');
    apps.forEach(async(app)=>{
        if (app.getAttribute('title') == "Spotify") {
            app.addEventListener('click', ()=>{
                pywebview.api.openApp(app.getAttribute('title'));
            });
        }
    });
});