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

window.addEventListener('pywebviewready',async()=>{
    const getapps = await fetch(`/main/app_data`).then(resp => resp.json());
    const appList = document.querySelector('.android-auto-home');
    for (const v of getapps.apps) {
        if (!v.enabled) continue;
        const app = document.createElement('div');
        app.className = 'app';
        app.title = v.name;
        const appIcon = document.createElement('img');
        appIcon.src = v.icon;
        appIcon.alt = v.name;
        const appName = document.createElement('span');
        appName.innerText = v.name;
        app.appendChild(appIcon);
        app.appendChild(appName);
        appList.appendChild(app);
        app.addEventListener('click', ()=>{
            rootbunny.app.interface.load(app.getAttribute('title'));
        });
    }
    /*const apps = appList.querySelectorAll('.app');
    apps.forEach(async(app)=>{
        if (app.getAttribute('title') == "Spotify") {
            
        }
    });*/
});