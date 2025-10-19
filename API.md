# RootBunny Developer SDK

The RootBunny Developer SDK is a tool to assist in the composition of applications. The RootBunny SDK is automatically available to your app through the `rootbunny.app` window variable.

## Audio Playback

This is a core function of the app library, and it allows audios to be played in the global context (which includes outside the app.)

If you need an API which can handle global audio playback with ease, `rootbunny.app.audio` is automatically the perfect toolkit for your use with RootBunny apps.

### `rootbunny.app.audio.play` -> Promise\<AudioPlayerCreatedStateObject\>

This function allows you to open a global audio player context.

Arguments:
> `context` -> string

This argument controls the context that the audio player is ran under. Audio contexts are then *useful* in **writing/reading audio data, changing audio state, etc.**

> `url` -> string

This argument controls the URL that audio is played from.

> `funcToRunOnAudioFinish` -> string

This argument controls the function that is ran when an audio finishes playback. **It is recommended** to give a global function name that is accessible under the `window` object.

> `funcToRunOnAudioTimeUpdate` -> string

This argument controls the function that is ran when an audio time is changed. **It is recommended** to give a global function name that is accessible under the `window` object.

### `rootbunny.app.audio.stateChange` -> void

This function allows the SDK to receive audio state change events. It's recommended to not overwrite this function.

Arguments:
> `o` -> **{** "data": Array\<AudioPlayerStateDataObject\>, "context": string **}**

This argument is sent from the backend which includes all the data that's required for registering audio states. Here's an applicable, real example:

```json
{
    "data": [
        {
            "volume": 100,
            "playing": true,
            "context": "example-app",
            "info": {
                "mediaSession": {

                }
            }
        }
    ],
    "context": "example-app"
}
```

### `rootbunny.app.audio.timeChange` -> void

This function allows the SDK to receive audio time update events. It's recommended to not overwrite this function.

Arguments:
> `o` -> AudioPlayerTimeUpdateObject

This argument is sent from the backend which includes all the data that's required for registering the audio state after the time update event was facilitated. Here's an applicable, real example:

```json
{
    "data": {
        "time": 0.1,
        "outOf": 242.3
    },
    "context": "example-app",
    "index": 0
}
```

### `rootbunny.app.audio.getStates` -> Promise\<Array\<AudioPlayerStateDataObject\>\>

This function allows you to get updated audio states from the backend. You may run this function at any time, under any context. Application audio states are viewable and modifiable by other applications.

Sample:

```json
[
    {
        "volume": 100,
        "playing": true,
        "context": "example-app",
        "info": {
            "mediaSession": {

            }
        }
    }
]
```

Arguments:
> `context` -> string

This argument controls which context the states need to be retrieved from. It must match the contexts in which audio players are registered underneath.

### `rootbunny.app.audio.pauseAudio` -> Promise\<boolean\>

This function allows you to pause an audio state underneath a context. For this, you need a `context` and an `index`.

Returns:

- `True` - if audio state was successfully paused
- `False` - if audio state didn't exist under context

Arguments:
> `context` -> string

This argument controls which context the state needs to be retrieved from. It must match the context in which the audio state is registered.

> `index` -> number

This argument controls which index the state should be matched to. If the index doesn't exist, nothing will be paused.

### `rootbunny.app.audio.resumeAudio` -> Promise\<boolean\>

This function allows you to resume an audio state underneath a context. For this, you need a `context` and an `index`.

Returns:

- `True` - if audio state was successfully resumed
- `False` - if audio state didn't exist under context

Arguments:
> `context` -> string

This argument controls which context the state needs to be retrieved from. It must match the context in which the audio state is registered.

> `index` -> number

This argument controls which index the state should be matched to. If the index doesn't exist, nothing will be resumed.

### `rootbunny.app.audio.close` -> Promise\<boolean\>

This function allows you to close an audio state underneath a context. For this, you need a `context` and an `index`.

Returns:

- `True` - if audio state was successfully closed and destroyed
- `False` - if audio state didn't exist under context

Arguments:
> `context` -> string

This argument controls which context the state needs to be retrieved from. It must match the context in which the audio state is registered.

> `index` -> number

This argument controls which index the state should be matched to. If the index doesn't exist, nothing will be stopped and closed.

### `rootbunny.app.audio.playBase64` -> Promise\<AudioPlayerCreatedStateObject\>

This function allows you to open a global audio player context for Base64-encoded audio.
**You do not need to provide a data URL.**

Arguments:
> `context` -> string

This argument controls the context that the audio player is ran under. Audio contexts are then *useful* in **writing/reading audio data, changing audio state, etc.**

> `b64` -> string

This argument controls the base64 that audio is played from.

> `codec` -> string

This argument defines the codec via a MimeType string, which is useful for the backend to identify the type of audio data that is supplied.

> `funcToRunOnAudioFinish` -> string

This argument controls the function that is ran when an audio finishes playback. **It is recommended** to give a global function name that is accessible under the `window` object.

> `funcToRunOnAudioTimeUpdate` -> string

This argument controls the function that is ran when an audio time is changed. **It is recommended** to give a global function name that is accessible under the `window` object.

### `rootbunny.app.audio.getInfo` -> Promise\<AudioPlayerStateDynamicInfoObject | null\>

This function allows you to get information registered for a global audio player context.

Arguments:
> `context` -> string

This argument controls which context the state needs to be retrieved from. It must match the context in which the audio state is registered.

> `index` -> number

This argument controls which index the state should be matched to. If the index doesn't exist, this function will return `null`.

### `rootbunny.app.audio.setInfo` -> Promise\<boolean\>

This function allows you to register information for a global audio player context.

Arguments:
> `context` -> string

This argument controls which context the state needs to be retrieved from. It must match the context in which the audio state is registered.

> `index` -> number

This argument controls which index the state should be matched to. If the index doesn't exist, this function will return `null`.

> `o` -> AudioPlayerStateDynamicInfoObject

This argument controls what information should be applied to the audio state. This object usually contains the default properties for all apps to access:

```json
{
    "mediaSession": {
        "title": "Sample App Title",
        "track": {
            "name": "Sample Track",
            "artists": ["Sample Artist"],
            "album": "Sample Album"
        }
    } // Controls the media session details, store audio data here or set it to an empty object.
}
```

If you don't include the default properties listed, other apps may bug with your audio player session. Set it wisely to the recommendations, and only pass-through basic types (`string`, `number`, `Object`, `Array`, etc.) into the object.

## Main RootBunny Interface

This is a core function of the app library, and it allows apps to directly contact RootBunny to control interface functions.

### `rootbunny.app.interface.home` -> void

This function allows you to navigate to the RootBunny home screen. There are no arguments needed for this function.

### `rootbunny.app.interface.load` -> void

This function allows you to navigate to a different RootBunny application.

Arguments:
> `app_name` -> string

The app name of the app to load.

### `rootbunny.app.interface.init` -> Promise\<boolean\>

This function allows you to send the `init_sent` event to the backend of your app's extension. You MUST send this function before your `window.location` changes for your extension to be found.

Returns:

- `True` - if application was found via path selector
- `False` - if application wasn't found via path selector

### `rootbunny.app.interface.apps` -> Promise\<Array\<App\>\>

This function allows you to grab data for all the registered applications. Here's an adequate example of what this function returns:

```json
[
    {
        "name": "Sample App Name",
        "icon": "Sample App Icon",
        "version": "1.0.0.0",
        "enabled": true
    }
]
```
