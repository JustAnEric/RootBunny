export class PlayerAPI {
    constructor() {
        this.ENDPOINT = '/apps/spotify/api/v1/player/';
    }

    async make_request(method, url, headers, body){return(await(fetch(this.ENDPOINT+url,{headers:headers,body:body,method:method})))}
    async get_song(songId){return(await((await(this.make_request('GET','songs/info',{sid:songId},null))).json()))}
    async get_song_stream(songId){const rq = await this.make_request('GET','songs/stream',{sid:songId,'Content-Type':'audio/mpeg,audio/webm'},null);return([await(rq.blob()),rq.headers.get('Content-Type')])}
    async get_song_audio_type(songId){return(await this.make_request('GET','songs/stream',{sid:songId,'Content-Type':'audio/mpeg,audio/webm'},null)).headers.get('Content-Type')}
}