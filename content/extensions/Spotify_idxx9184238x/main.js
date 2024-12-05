import { Player } from './sdk/premify-player.js';
let audId = 11;
let songsTotal = 0;

(async()=>{
    const player = new Player();

    songsTotal = parseInt((await(await(player.API.make_request('GET','songs/total',{},null))).json())['song_count']);

    //typically you'd want to load this with the song
    player.load(audId);

    document.querySelector('.play-pause-btn').addEventListener('click', function() {
        const icon = this.querySelector('i');
        if (icon.classList.contains('fa-play')) {
            icon.classList.replace('fa-play', 'fa-pause');
            // Implement play functionality here
            player.play(); // lets just try and play it :)
        } else {
            icon.classList.replace('fa-pause', 'fa-play');
            // Implement pause functionality here
            player.pause();
        }
    });

    document.querySelector('.next-btn').addEventListener('click',async()=>{
        window.next();
        console.log(audId);

        const icon = document.querySelector('.play-pause-btn i');
        if (icon.classList.contains('fa-play')) {
            icon.classList.replace('fa-play', 'fa-pause');
        }
    });

    document.querySelector('.prev-btn').addEventListener('click',async()=>{
        window.previous();
        console.log(audId);
        const icon = document.querySelector('.play-pause-btn i');
        if (icon.classList.contains('fa-play')) {
            icon.classList.replace('fa-play', 'fa-pause');
        }
    });

    player.player.addEventListener('timeupdate', async(ev)=>{
        const pgm = document.querySelector('.progress-bar.duration');
        const pg = pgm.querySelector('.progress');
        pg.style.width = `${(player.player.currentTime / player.player.duration)*100}%`;
        //console.log(player.player.currentTime / player.player.duration*100);
    });

    player.player.addEventListener('ended', async(ev)=>{
        audId+=1;
        player.pause();
        player.load(audId).then(()=>{
            player.play();
        });
    });

    window.audio = player.player;

    window.next = async()=>{
        if (audId >= songsTotal) {
            audId = 1;
            player.pause();
            player.load(audId).then(()=>{
                player.play();
            });
        } else {
            audId+=1;
            player.pause();
            player.load(audId).then(()=>{
                player.play();
            });
        }
    }

    window.previous = async()=>{
        if (player.player.currentTime >= 3) {
            player.player.currentTime = 0;
        } else {
            if (audId <= 1) {
                audId = songsTotal;
                player.pause();
                player.load(audId).then(()=>{
                    player.play();
                });
            } else {
                audId-=1;
                player.pause();
                player.load(audId).then(()=>{
                    player.play();
                });
            }
        }
    }

    document.querySelector('.top-nav input[type=text]').addEventListener('change',async()=>{
        // make request
        const results = await ( await player.API.make_request('GET','songs/search',{'q':document.querySelector('.top-nav input[type=text]').value}) )
                            .json();
        console.log(results);

        // 1st result is what we play
        /*player.load(results[0].index).then(()=>{
            player.play();
        });*/

        const PLAYLIST_RESULT = `
<div class="playlist-card">
    <img src="https://via.placeholder.com/150" alt="Playlist 1">
    <p>[[song_title]]</p>
    <span>[[song_artist]]</span>
</div>
        `;

        for(var child of (document.querySelector('.playlists').children)){child.remove();};
        for(const song of results){
            document.querySelector('.playlists').insertAdjacentHTML('beforeend', PLAYLIST_RESULT.replaceAll('[[song_title]]',song.song_info.description).replaceAll('[[song_artist]]',song.song_info.artist));
            document.querySelector('.playlists').children[document.querySelector('.playlists').children.length-1].addEventListener('click',async()=>{
                // play the song
                player.load(song.index).then(()=>{
                    player.play();
                });
            });
        };
    });
})();