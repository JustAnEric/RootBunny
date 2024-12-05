import { PlayerAPI } from './Player/API.js';

export class Player {
    constructor() {
        this.player = new Audio();
        this.player.setAttribute('type', 'audio/mpeg');
        this.player.hidden = true;

        this.API = new PlayerAPI();

        /**
         * Used for accessing audio information.
         */
        this.audioInfo = {};
    }

    async play() {
        this.player.play();
    }

    async load(audioId) {
        this.audioInfo = null;
        this.audioInfo = await this.API.get_song(audioId);
        if(this.audioInfo){
            const songStream = await this.API.get_song_stream(audioId);
            //const blob = new Blob([songStream]);
            const objURL = window.URL.createObjectURL(songStream);

            console.log("Audio inserted");
            this.player.src = objURL;

            document.querySelector('.music-player .song-info .song-details .song-title').innerHTML = this.audioInfo.description;
            if (this.audioInfo.artist){
                document.querySelector('.music-player .song-info .song-details .song-artist').innerHTML = this.audioInfo.artist;
            } else {
                document.querySelector('.music-player .song-info .song-details .song-artist').innerHTML = "Unknown";
            }
        }
    }

    async pause(){
        this.player.pause();
    }
}