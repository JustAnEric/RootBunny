export class PlayerAPI {
    constructor() {
        this.ENDPOINT = '/api/v1/player/';
    }

    async make_request(method, url, headers, body){return(await(fetch(this.ENDPOINT+url,{headers:headers,body:body,method:method})))}
    async get_song(songId){return(await((await(this.make_request('GET','songs/info',{sid:songId},null))).json()))}
    async get_song_stream(songId){return(await((await this.make_request('GET','songs/stream',{sid:songId},null))).blob())}
}