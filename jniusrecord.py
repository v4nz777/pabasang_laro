from jnius import autoclass
from time import sleep
from kivy.utils import platform



def android_record(output):
    if platform == 'android':
        from android.permissions import request_permissions, Permission

        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,
                             Permission.INTERNET, Permission.RECORD_AUDIO,
                             Permission.CAPTURE_AUDIO_OUTPUT])

        # get the needed Java classes
        MediaRecorder = autoclass('android.media.MediaRecorder')
        AudioSource = autoclass('android.media.MediaRecorder$AudioSource')
        OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
        AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')

        # create out recorder
        mRecorder = MediaRecorder()
        mRecorder.setAudioSource(AudioSource.MIC)
        mRecorder.setOutputFormat(OutputFormat.RAW_AMR)
        mRecorder.setOutputFile(output)
        mRecorder.setAudioEncoder(AudioEncoder.AMR_NB)
        mRecorder.prepare()

        # record 5 seconds
        mRecorder.start()
        sleep(5)
        mRecorder.stop()
        mRecorder.release()
        return True
