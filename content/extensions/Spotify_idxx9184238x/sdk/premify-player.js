import { PlayerAPI } from './Player/API.js';

export class Player {
    constructor() {
        /*this.player = new Audio();
        this.player.setAttribute('type', 'audio/mpeg');
        this.player.hidden = true;*/
        this.run_on_finish = null;

        this.API = new PlayerAPI();

        /**
         * Used for accessing audio information.
         */
        this.audioInfo = {};

        /**
         * Used for accessing player information on the RootBunny backend.
         */
        this.playerInfo = { context: 'premify-player', index: 0 };

        window.run_on_finish_rootbunny = async() => {
            if (this.run_on_finish) this.run_on_finish();
        }

        window.run_on_timeupdate_rootbunny = async(time, outOf) => {
            const pgm = document.querySelector('.progress-bar.duration');
            const pg = pgm.querySelector('.progress');
            pg.style.width = `${(time / outOf)*100}%`;
        }
    }

    base64ArrayBuffer(arrayBuffer) {
        let base64 = '';
        const encodings = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
        const bytes = new Uint8Array(arrayBuffer);
        const byteLength = bytes.byteLength;
        const byteRemainder = byteLength % 3;
        const mainLength = byteLength - byteRemainder;
        let a, b, c, d;
        let chunk;

        // Main loop: Process in 3-byte chunks
        for (let i = 0; i < mainLength; i += 3) {
            chunk = (bytes[i] << 16) | (bytes[i + 1] << 8) | bytes[i + 2];
            a = (chunk & 16515072) >> 18; // 16515072 = (2^6 - 1) << 18
            b = (chunk & 258048) >> 12;   // 258048 = (2^6 - 1) << 12
            c = (chunk & 4032) >> 6;      // 4032 = (2^6 - 1) << 6
            d = chunk & 63;               // 63 = 2^6 - 1
            base64 += encodings[a] + encodings[b] + encodings[c] + encodings[d];
        }

        // Handle remainder and padding
        if (byteRemainder === 1) {
            chunk = bytes[mainLength];
            a = (chunk & 252) >> 2;  // 252 = (2^6 - 1) << 2
            b = (chunk & 3) << 4;    // 3 = 2^2 - 1
            base64 += encodings[a] + encodings[b] + '==';
        } else if (byteRemainder === 2) {
            chunk = (bytes[mainLength] << 8) | bytes[mainLength + 1];
            a = (chunk & 64512) >> 10; // 64512 = (2^6 - 1) << 10
            b = (chunk & 1008) >> 4;   // 1008 = (2^6 - 1) << 4
            c = (chunk & 15) << 2;     // 15 = 2^4 - 1
            base64 += encodings[a] + encodings[b] + encodings[c] + '=';
        }

        return base64;
    }

    async play() {
        //this.player.play();
        await window.rootbunny.app.audio.resumeAudio(this.playerInfo.context, this.playerInfo.index);
    }

    async renderAudioInfo(audioId) {
        this.audioInfo = null;
        this.audioInfo = await this.API.get_song(audioId);
        document.querySelector('.music-player .song-info .song-details .song-title').innerHTML = this.audioInfo.description;
        if (this.audioInfo.artist){
            document.querySelector('.music-player .song-info .song-details .song-artist').innerHTML = this.audioInfo.artist;
        } else {
            document.querySelector('.music-player .song-info .song-details .song-artist').innerHTML = "Unknown";
        }
    }

    async load(audioId) {
        this.audioInfo = null;
        this.audioInfo = await this.API.get_song(audioId);
        if(this.audioInfo){
            const [songStream, audioType] = await this.API.get_song_stream(audioId);
            console.log(audioType);
            //const blob = new Blob([songStream]);
            //const objURL = window.URL.createObjectURL(songStream);

            let b64;

            // make base64 from audio data
            const buffer = await songStream.arrayBuffer();
            b64 = this.base64ArrayBuffer(buffer);

            //const playerSession = await window.rootbunny.app.audio.play('premify-player', `http://127.0.0.1:4000/apps/spotify/api/v1/player/songs/stream/less?sid=${audioId}`, 'run_on_finish_rootbunny', 'run_on_timeupdate_rootbunny');
            const playerSession = await window.rootbunny.app.audio.playBase64('premify-player', b64, audioType, 'run_on_finish_rootbunny', 'run_on_timeupdate_rootbunny');

            this.playerInfo = {
                index: playerSession.index,
                context: playerSession.context
            }

            const metadataSession = await window.rootbunny.app.audio.setInfo(this.playerInfo.context, this.playerInfo.index, {
                mediaSession: {
                    title: this.audioInfo.description,
                    artist: this.audioInfo.artist,
                    metadata: {
                        songId: audioId
                    }
                }
            });

            console.log("Audio inserted");
            //this.player.src = objURL;

            document.querySelector('.music-player .song-info .song-details .song-title').innerHTML = this.audioInfo.description;
            if (this.audioInfo.artist){
                document.querySelector('.music-player .song-info .song-details .song-artist').innerHTML = this.audioInfo.artist;
            } else {
                document.querySelector('.music-player .song-info .song-details .song-artist').innerHTML = "Unknown";
            }
        }
    }

    async pause(){
        //this.player.pause();
        await window.rootbunny.app.audio.pauseAudio(this.playerInfo.context, this.playerInfo.index);
    }

    async stop(){
        await window.rootbunny.app.audio.close(this.playerInfo.context, this.playerInfo.index);
    }
}